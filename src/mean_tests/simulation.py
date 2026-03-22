from __future__ import annotations

import concurrent.futures
import functools
import itertools
import math
import multiprocessing as mp
from typing import TYPE_CHECKING

import numpy as np
import polars as pl
import pydantic
import tea_tasting.utils
import tqdm

import mean_tests.config
import mean_tests.sample
import mean_tests.utils


if TYPE_CHECKING:
    from typing import Any

    import tea_tasting as tt


ABS_TOL = 1e-5


class SampleParams(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")

    sample_size: mean_tests.config.PositiveInt
    ratio: mean_tests.config.PositiveFloat
    mu0: pydantic.StrictFloat
    sigma0: mean_tests.config.PositiveFloat
    mu1: pydantic.StrictFloat
    sigma1: mean_tests.config.PositiveFloat


def generate_simulation_report(
    *,
    simulation: mean_tests.config.SimulationConfig,
    user_tests: tuple[mean_tests.config.TestConfig, ...],
    bucket_tests: tuple[mean_tests.config.TestConfig, ...],
    buckets: tuple[int, ...],
    sample: mean_tests.config.SampleConfig,
    treatments: tuple[mean_tests.config.TreatmentConfig, ...],
) -> str:
    rng = np.random.default_rng(simulation.rng)
    user_experiment = mean_tests.utils.create_experiment(user_tests)
    bucket_experiment = mean_tests.utils.create_experiment(bucket_tests)

    top_users, top_value = sample.top_users, sample.top_value
    sigma0 = mean_tests.sample.calc_sigma(top_users, top_value)
    mu0 = mean_tests.sample.calc_mu(sigma0)

    report = ["# Comparison of two-sample mean tests"]
    report.append(mean_tests.utils.render_dict({
        "number of simulations": simulation.n_simulations,
        "alpha": sample.alpha,
        "reference power": sample.power,
        "treatment-to-control allocation ratio": sample.ratio,
        "top users": top_users,
        "value created by top users": top_value,
    }))

    for treatment in treatments:
        rel_diff_top = treatment.rel_diff_top
        rel_diff_bottom = treatment.rel_diff_bottom
        rel_diff_total = rel_diff_top + rel_diff_bottom
        if math.isclose(rel_diff_total, 0, abs_tol=ABS_TOL):
            rel_diff = sample.rel_diff_default
            rate_col = "type I error"
        else:
            rel_diff = rel_diff_total
            rate_col = "power"

        sigma1 = mean_tests.sample.calc_sigma(
            top_users=sample.top_users,
            top_value=(top_value + rel_diff_top) / (1 + rel_diff_total),
        )
        mu1 = mean_tests.sample.calc_mu(sigma1, 1 + rel_diff_total)
        sample_size = mean_tests.sample.calc_sample_size(
            alpha=sample.alpha,
            power=sample.power,
            ratio=sample.ratio,
            sigma0=sigma0,
            sigma1=sigma1,
            rel_diff=rel_diff,
        )

        report.append(f"## {treatment.name}")
        report.append(mean_tests.utils.render_dict({
            "top users effect (relative to total)": rel_diff_top,
            "bottom users effect (relative to total)": rel_diff_bottom,
            "total relative effect": rel_diff_total,
            "sample size": sample_size,
        }))

        tqdm.tqdm.write(treatment.name)
        result = run_simulation(
            rng,
            n_simulations=simulation.n_simulations,
            batch_size=simulation.batch_size,
            max_workers=simulation.max_workers,
            user_experiment=user_experiment,
            bucket_experiment=bucket_experiment,
            buckets=buckets,
            sample_params=SampleParams(
                sample_size=sample_size,
                ratio=sample.ratio,
                mu0=mu0,
                sigma0=sigma0,
                mu1=mu1,
                sigma1=sigma1,
            ),
        )

        report.append(mean_tests.utils.render_dicts(summarize_result(
            result,
            alpha=sample.alpha,
            rate_col=rate_col,
        )))

    return "\n\n".join(report)


def run_simulation(
    rng: np.random.Generator,
    *,
    n_simulations: int,
    batch_size: int,
    max_workers: int,
    user_experiment: tt.Experiment,
    bucket_experiment: tt.Experiment,
    buckets: tuple[int, ...],
    sample_params: SampleParams,
) -> pl.DataFrame:
    rng_batches = tuple(
        itertools.batched(rng.spawn(n_simulations), batch_size, strict=False))
    batch_sizes = tuple(len(rng_batch) for rng_batch in rng_batches)

    simulation = functools.partial(
        analyze_batch,
        user_experiment=user_experiment,
        bucket_experiment=bucket_experiment,
        buckets=buckets,
        sample_params=sample_params,
    )

    with concurrent.futures.ProcessPoolExecutor(
        max_workers=max_workers if max_workers > 0 else None,
        mp_context=mp.get_context("spawn"),
    ) as executor:
        results = []
        with tqdm.tqdm(total=n_simulations) as progress:
            for batch_result, completed_batch_size in zip(
                executor.map(simulation, rng_batches),
                batch_sizes,
                strict=True,
            ):
                results.append(batch_result)
                progress.update(completed_batch_size)
        return pl.concat(results)


def analyze_batch(
    rng_batch: tuple[np.random.Generator, ...],
    *,
    user_experiment: tt.Experiment,
    bucket_experiment: tt.Experiment,
    buckets: tuple[int, ...],
    sample_params: SampleParams,
) -> pl.DataFrame:
    return pl.concat(
        analyze_experiment(
            rng,
            user_experiment=user_experiment,
            bucket_experiment=bucket_experiment,
            buckets=buckets,
            sample_params=sample_params,
        )
        for rng in rng_batch
    )


def analyze_experiment(
    rng: np.random.Generator,
    *,
    user_experiment: tt.Experiment,
    bucket_experiment: tt.Experiment,
    buckets: tuple[int, ...],
    sample_params: SampleParams,
) -> pl.DataFrame:
    sample = mean_tests.sample.make_sample(
        rng,
        sample_size=sample_params.sample_size,
        ratio=sample_params.ratio,
        mu0=sample_params.mu0,
        sigma0=sample_params.sigma0,
        mu1=sample_params.mu1,
        sigma1=sample_params.sigma1,
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


def summarize_result(
    result: pl.DataFrame,
    alpha: float,
    rate_col: str,
) -> list[dict[str, Any]]:
    return (
        result.lazy()
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
