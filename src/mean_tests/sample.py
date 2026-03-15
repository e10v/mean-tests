from __future__ import annotations

import math

import numpy as np
import polars as pl
import scipy.stats


def calc_sigma(pareto_users: float, pareto_value: float) -> float:
    return scipy.stats.norm.isf(pareto_users) + scipy.stats.norm.ppf(pareto_value)


def calc_mu(mean: float, sigma: float) -> float:
    return math.log(mean) - square(sigma)/2


def calc_sample_size(
    alpha: float,
    power: float,
    sigma0: float,
    sigma1: float,
    rel_diff: float,
) -> int:
    z_crit = scipy.stats.norm.isf(alpha/2) + scipy.stats.norm.ppf(power)
    rel_var0 = math.exp(square(sigma0)) - 1
    rel_var1 = (math.exp(square(sigma1)) - 1) * square(1 + rel_diff)
    return round(2 * square(z_crit) * (rel_var0 + rel_var1) / square(rel_diff))


def square(x: float) -> float:
    return x * x


def make_sample(
    rng: int | np.random.Generator,
    *,
    sample_size: int,
    n_buckets: int,
    mu0: float,
    sigma0: float,
    mu1: float,
    sigma1: float,
) -> pl.DataFrame:
    rng = np.random.default_rng(rng)
    variant = rng.integers(2, size=sample_size)
    bucket = rng.integers(n_buckets, size=sample_size)
    value = rng.lognormal(mu0 + variant*(mu1 - mu0), sigma0 + variant*(sigma1 - sigma0))
    return pl.DataFrame({"variant": variant, "bucket": bucket, "value": value})
