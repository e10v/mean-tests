from __future__ import annotations

import math
from typing import TYPE_CHECKING

import polars as pl
import scipy.stats


if TYPE_CHECKING:
    import numpy as np


def calc_sigma(top_users: float, top_value: float) -> float:
    return scipy.stats.norm.isf(top_users) + scipy.stats.norm.ppf(top_value)


def calc_mu(mean: float, sigma: float) -> float:
    return math.log(mean) - square(sigma)/2


def calc_sample_size(
    alpha: float,
    power: float,
    sigma0: float,
    sigma1: float,
    pp_diff: float,
) -> int:
    z_crit = scipy.stats.norm.isf(alpha/2) + scipy.stats.norm.ppf(power)
    rel_var0 = math.exp(square(sigma0)) - 1
    rel_var1 = (math.exp(square(sigma1)) - 1) * square(1 + pp_diff)
    return round(2 * square(z_crit) * (rel_var0 + rel_var1) / square(pp_diff))


def square(x: float) -> float:
    return x * x


def make_sample(
    rng: np.random.Generator,
    *,
    sample_size: int,
    mu0: float,
    sigma0: float,
    mu1: float,
    sigma1: float,
) -> pl.DataFrame:
    variant = rng.integers(2, size=sample_size)
    value = rng.lognormal(mu0 + variant*(mu1 - mu0), sigma0 + variant*(sigma1 - sigma0))
    return pl.DataFrame({"variant": variant, "value": value})


def group_by_buckets(
    sample: pl.DataFrame,
    rng: np.random.Generator,
    n_buckets: int,
) -> pl.DataFrame:
    bucket = rng.integers(n_buckets, size=len(sample))
    return (
        sample.lazy()
        .group_by("variant", pl.Series(bucket).alias("bucket"))
        .agg(pl.count().alias("users"), pl.sum("value"))
        .with_columns(pl.col("value").truediv(pl.col("users")).alias("value_per_user"))
        .collect()  # ty:ignore[invalid-return-type]
    )
