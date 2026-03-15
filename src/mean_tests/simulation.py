from __future__ import annotations

import concurrent.futures
import functools
from typing import TYPE_CHECKING

import numpy as np
import polars as pl
import scipy.stats
import tea_tasting.experiment
import tea_tasting.utils
import tqdm

import mean_tests.metrics
import mean_tests.sample
import mean_tests.utils


if TYPE_CHECKING:
    import tea_tasting as tt

    import mean_tests.config  # noqa: TC004


PRECISION = 0.00001


def generate_simulation_report(
    rng: int | np.random.Generator,
    n_simulations: int,
    alpha: float,
    power: float,
    pp_diff_default: float,
    buckets: tuple[int, ...],
    control: mean_tests.config.ControlConfig,
    treatments: tuple[mean_tests.config.TreatmentConfig, ...],
) -> str:
    rng = np.random.default_rng(rng)
    user_experiment = mean_tests.metrics.get_user_experiment()
    bucket_experiments = mean_tests.metrics.get_bucket_experiments(buckets)

    top_users, top_value = control.top_users, control.top_value
    sigma0 = mean_tests.sample.calc_sigma(top_users, top_value)
    mu0 = mean_tests.sample.calc_mu(control.mean, sigma0)

    report = ["# Simulation"]
    report.append(mean_tests.utils.render_dict({
        "number of simulations": n_simulations,
        "alpha": alpha,
        "power": power,
        "top users": top_users,
        "value created by top users": top_value,
    }))

    for treatment in treatments:
        pp_diff_top, pp_diff_bottom = treatment.pp_diff_top, treatment.pp_diff_bottom
        pp_diff_total = pp_diff_top + pp_diff_bottom
        if abs(pp_diff_total) > PRECISION:
            pp_diff = pp_diff_total
            rate_col = "power"
        else:
            pp_diff = pp_diff_default
            rate_col = "type I error"

        sigma1 = mean_tests.sample.calc_sigma(
            top_users=control.top_users,
            top_value=(top_value + pp_diff_top) / (1 + pp_diff_total),
        )
        mu1 = mean_tests.sample.calc_mu(control.mean * (1 + pp_diff_total), sigma1)
        sample_size = mean_tests.sample.calc_sample_size(
            alpha=alpha,
            power=power,
            sigma0=sigma0,
            sigma1=sigma1,
            pp_diff=pp_diff,
        )

        tqdm.tqdm.write(treatment.name)
        report.append(f"## {treatment.name}")
        report.append(mean_tests.utils.render_dict({
            "effect on top users": mean_tests.utils.format_pp(pp_diff_top),
            "effect on bottom users": mean_tests.utils.format_pp(pp_diff_bottom),
            "total effect": mean_tests.utils.format_pp(pp_diff_total),
            "sample size": sample_size,
        }))
        tqdm.tqdm.write(report[-1])

        simulation_results = run_simulation(
            rng,
            n_simulations=n_simulations,
            user_experiment=user_experiment,
            bucket_experiments=bucket_experiments,
            sample_size=sample_size,
            mu0=mu0,
            sigma0=sigma0,
            mu1=mu1,
            sigma1=sigma1,
        )
        results = summarize_results(
            simulation_results.to_polars(),
            alpha=alpha,
            rate_col=rate_col,
        )

        report.append(mean_tests.utils.render_dicts(
            results.lazy()
                .sort(rate_col, "test", descending=True)
                .select(
                    "test",
                    pl.col(rate_col).map_elements(tea_tasting.utils.format_num),
                    pl.col(f"{rate_col} ci")
                        .map_elements(mean_tests.utils.format_ci, pl.String),
                )
                .collect()
                .to_dicts(),  # ty:ignore[unresolved-attribute]
        ))
        tqdm.tqdm.write(report[-1])

    return "\n\n".join(report)


def run_simulation(
    rng: np.random.Generator,
    *,
    n_simulations: int,
    user_experiment: tt.Experiment,
    bucket_experiments: dict[int, tt.Experiment],
    sample_size: int,
    mu0: float,
    sigma0: float,
    mu1: float,
    sigma1: float,
) -> tea_tasting.experiment.SimulationResults:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        raw_results = executor.map(
            functools.partial(
                analyze_experiment,
                user_experiment=user_experiment,
                bucket_experiments=bucket_experiments,
                sample_size=sample_size,
                mu0=mu0,
                sigma0=sigma0,
                mu1=mu1,
                sigma1=sigma1,
            ),
            rng.spawn(n_simulations),
        )
        results = tqdm.tqdm(raw_results, total=n_simulations)
        return tea_tasting.experiment.SimulationResults(results)


def analyze_experiment(
    rng: np.random.Generator,
    *,
    user_experiment: tt.Experiment,
    bucket_experiments: dict[int, tt.Experiment],
    sample_size: int,
    mu0: float,
    sigma0: float,
    mu1: float,
    sigma1: float,
) -> tea_tasting.experiment.ExperimentResult:
    sample = mean_tests.sample.make_sample(
        rng.spawn(1)[0],
        sample_size=sample_size,
        mu0=mu0,
        sigma0=sigma0,
        mu1=mu1,
        sigma1=sigma1,
    )
    result = user_experiment.analyze(sample)
    for n_buckets, bucket_experiment in bucket_experiments.items():
        grouped_sample = mean_tests.sample.group_by_buckets(
            sample=sample,
            rng=rng.spawn(1)[0],
            n_buckets=n_buckets,
        )
        result.update(bucket_experiment.analyze(grouped_sample))
    return result


def summarize_results(
    results: pl.DataFrame,
    alpha: float,
    rate_col: str,
) -> pl.DataFrame:
    return (
        results.lazy()
        .filter(pl.col("pvalue").is_not_nan())
        .group_by("metric")
        .agg(
            pl.col("pvalue").le(alpha).cast(int).sum().alias("null rejected"),
            pl.col("pvalue").count().alias("total"),
        )
        .select(
            pl.col("metric").alias("test"),
            pl.col("null rejected").truediv(pl.col("total")).alias(rate_col),
            pl.concat_list("null rejected", "total")
                .map_elements(calc_binom_ci, return_dtype=pl.List(pl.Float64))
                .alias(rate_col + " ci"),
        )
        .collect()  # ty:ignore[invalid-return-type]
    )


def calc_binom_ci(k_n: list[int]) -> list[float]:
    k, n = k_n
    low, upp = scipy.stats.binomtest(k, n).proportion_ci(method="wilsoncc")
    return [low, upp]
