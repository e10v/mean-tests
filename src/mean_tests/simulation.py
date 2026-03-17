from __future__ import annotations

import concurrent.futures
import functools
import multiprocessing as mp
from typing import TYPE_CHECKING

import numpy as np
import polars as pl
import tea_tasting.utils
import tqdm

import mean_tests.sample
import mean_tests.utils


if TYPE_CHECKING:
    from typing import Any

    import tea_tasting as tt

    import mean_tests.config  # noqa: TC004


PRECISION = 0.00001


def generate_simulation_report(
    rng: int | np.random.Generator,
    *,
    n_simulations: int,
    user_tests: tuple[mean_tests.config.TestConfig, ...],
    bucket_tests: tuple[mean_tests.config.TestConfig, ...],
    buckets: tuple[int, ...],
    alpha: float,
    power: float,
    rel_diff_default: float,
    control: mean_tests.config.ControlConfig,
    treatments: tuple[mean_tests.config.TreatmentConfig, ...],
) -> str:
    rng = np.random.default_rng(rng)
    user_experiment = mean_tests.utils.create_experiment(user_tests)
    bucket_experiment = mean_tests.utils.create_experiment(bucket_tests)

    top_users, top_value = control.top_users, control.top_value
    sigma0 = mean_tests.sample.calc_sigma(top_users, top_value)
    mu0 = mean_tests.sample.calc_mu(control.mean, sigma0)

    report = ["# Comparison of two-sample mean tests"]
    report.append(mean_tests.utils.render_dict({
        "number of simulations": n_simulations,
        "alpha": alpha,
        "power": power,
        "top users": top_users,
        "value created by top users": top_value,
    }))

    for treatment in treatments:
        rel_diff_top = treatment.rel_diff_top
        rel_diff_bottom = treatment.rel_diff_bottom
        rel_diff_total = rel_diff_top + rel_diff_bottom
        if abs(rel_diff_total) > PRECISION:
            rel_diff = rel_diff_total
            rate_col = "power"
        else:
            rel_diff = rel_diff_default
            rate_col = "type I error"

        sigma1 = mean_tests.sample.calc_sigma(
            top_users=control.top_users,
            top_value=(top_value + rel_diff_top) / (1 + rel_diff_total),
        )
        mu1 = mean_tests.sample.calc_mu(control.mean * (1 + rel_diff_total), sigma1)
        sample_size = mean_tests.sample.calc_sample_size(
            alpha=alpha,
            power=power,
            sigma0=sigma0,
            sigma1=sigma1,
            rel_diff=rel_diff,
        )

        tqdm.tqdm.write(treatment.name)
        simulation_results = run_simulation(
            rng,
            n_simulations=n_simulations,
            user_experiment=user_experiment,
            bucket_experiment=bucket_experiment,
            buckets=buckets,
            sample_size=sample_size,
            mu0=mu0,
            sigma0=sigma0,
            mu1=mu1,
            sigma1=sigma1,
        )
        results = summarize_results(
            simulation_results,
            alpha=alpha,
            rate_col=rate_col,
        )

        report.append(f"## {treatment.name}")
        report.append(mean_tests.utils.render_dict({
            "top users effect (relative to total)": rel_diff_top,
            "bottom users effect (relative to total)": rel_diff_bottom,
            "total relative effect": rel_diff_total,
            "sample size": sample_size,
        }))
        report.append(mean_tests.utils.render_dicts(results))

    return "\n\n".join(report)


def run_simulation(
    rng: np.random.Generator,
    *,
    n_simulations: int,
    user_experiment: tt.Experiment,
    bucket_experiment: tt.Experiment,
    buckets: tuple[int, ...],
    sample_size: int,
    mu0: float,
    sigma0: float,
    mu1: float,
    sigma1: float,
) -> pl.DataFrame:
    simulation = functools.partial(
        analyze_experiment,
        user_experiment=user_experiment,
        bucket_experiment=bucket_experiment,
        buckets=buckets,
        sample_size=sample_size,
        mu0=mu0,
        sigma0=sigma0,
        mu1=mu1,
        sigma1=sigma1,
    )
    mp_context = mp.get_context("spawn")
    with concurrent.futures.ProcessPoolExecutor(mp_context=mp_context) as executor:
        return pl.concat(tqdm.tqdm(
            executor.map(simulation, rng.spawn(n_simulations)),
            total=n_simulations,
        ))


def analyze_experiment(
    rng: np.random.Generator,
    *,
    user_experiment: tt.Experiment,
    bucket_experiment: tt.Experiment,
    buckets: tuple[int, ...],
    sample_size: int,
    mu0: float,
    sigma0: float,
    mu1: float,
    sigma1: float,
) -> pl.DataFrame:
    sample = mean_tests.sample.make_sample(
        rng,
        sample_size=sample_size,
        mu0=mu0,
        sigma0=sigma0,
        mu1=mu1,
        sigma1=sigma1,
    )
    results = [analyze_preset(user_experiment, sample, "users")]
    for n_buckets in buckets:
        grouped_sample = mean_tests.sample.group_by_buckets(
            sample=sample,
            rng=rng,
            n_buckets=n_buckets,
        )
        results.append(analyze_preset(
            bucket_experiment,
            grouped_sample,
            f"{n_buckets} buckets",
        ))
    return pl.concat(results)


def analyze_preset(
    experiment: tt.Experiment,
    sample: pl.DataFrame,
    level: str,
) -> pl.DataFrame:
    return experiment.analyze(sample).to_polars().select(
        pl.col("metric").alias("test"),
        pl.lit(level).alias("level"),
        "pvalue",
    )


def summarize_results(
    results: pl.DataFrame,
    alpha: float,
    rate_col: str,
) -> list[dict[str, Any]]:
    return (
        results.lazy()
        .filter(pl.col("pvalue").is_not_nan())
        .group_by("test", "level")
        .agg(
            pl.col("pvalue").le(alpha).cast(int).sum().alias("null rejected"),
            pl.col("pvalue").count().alias("total"),
        )
        .with_columns(pl.col("null rejected").truediv(pl.col("total")).alias(rate_col))
        .sort(rate_col, "test", "level", descending=True)
        .select(
            "test",
            "level",
            pl.col(rate_col).map_elements(tea_tasting.utils.format_num),
            pl.concat_list("null rejected", "total")
                .map_elements(mean_tests.utils.format_binom_ci, return_dtype=pl.String)
                .alias(rate_col + " ci"),
        )
        .collect()
        .to_dicts()  # ty:ignore[unresolved-attribute]
    )
