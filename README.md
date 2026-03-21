# Comparison of two-sample mean tests

## TL;DR

TODO

## Problem

### Analysis of means

In A/B tests, we usually want to check whether the average amount of some value per user differs between two variants of a product. Examples of such values include revenue, transactions, clicks, impressions, and sessions. For this purpose, we treat the user as the randomization unit, compare the average values per user, and use a two-sample test of means to evaluate the statistical significance of the difference.

Welch's t-test is a typical choice for the analysis of means in a two-sample experiment. It is designed for unequal population variances and assumes that the variances are unknown. Alternative choices are:

- Student's t-test, which assumes equal variances.
- A z-test of means with unpooled variance, which assumes that the population variances are known.

There is also a z-test of means with *pooled* variance, which assumes that the variances are known and equal. I do not consider it here because it would not provide any additional meaningful insights into test applicability.

### Bucket tests for large-scale experiments

In large-scale experiments, storing and analyzing data at the user level can become costly. In such cases, bucket-level analysis is often used:

- Variants are still randomized at the user level.
- Users are randomly distributed between buckets using hash functions, typically into about 100 buckets per variant.
- Metrics are aggregated and analyzed at the bucket level. For example, each bucket can be represented by its mean revenue per user.

Bucket-level analysis can still satisfy the independence assumption.

### Mann–Whitney U test

The Mann–Whitney U test is not a conventional choice when the goal is to check whether the average amount per user differs between two variants. It is not a test of means. In its usual interpretation, it tests whether an observation from one variant is more likely to exceed an observation from the other variant. Under the null hypothesis for continuous distributions, `P(X > Y) = P(X < Y)`, where `X` and `Y` are independent observations from the control and treatment variants.

A *user-level* Mann–Whitney U test is generally a poor choice for this problem, but some teams use the *bucket-level* Mann–Whitney U test as if it were a test of means. Their reasoning is as follows:

- Bucketization makes the distribution closer to normal.
- Under normality with equal variances, equality of distributions is equivalent to equality of means, so the Mann–Whitney U test can serve as an indirect test in that restricted setting.

### Problem formulation

This repository compares the following statistical tests at both the user and bucket levels in the context of two-sample mean analysis:

- Welch's t-test,
- Student's t-test,
- Z-test of means with unpooled variance,
- Mann–Whitney U test.

We want a test with high statistical power while keeping the type I error rate at the desired level (for example, `0.05`).

## Simulation

In real-world scenarios, metric distribution among the users is highly skewed and follows the Pareto-like rule: 10–30% of users create 70–90% of value (revenue, transactions, sessions, etc.). For convenience, we will call these 10–30% of users the "top" users, and the rest of users the "bottom" users. Usually, the treatment effect is unevenly distributed among the users. Sometimes, it even oppositely directed for top and bottom users, with near zero average effect.

The code in this repository simulates many experiments with skewed data sampled from lognormal distribution. The skewness is determined by the Pareto-like rule: top P share of users create Q share of value. The treatment effect is defined separately for top and bottom users. Sample size is estimated to target the power `0.8`.

Five types of treatments are simulated, `10_000` times each:

1. Positive effect on top users, negative effect on bottom users, and zero average effect in total.
2. Negative effect on top users, positive effect on bottom users, and zero average effect in total.
3. Positive effect on all users.
4. Positive effect on top users, zero average effect on bottom users, and positive effect in total.
5. Zero average effect on top users, positive effect on bottom users, and positive effect in total.

The first two are A/A simulations (two sample means are equal): the proportion of p-values below the significance level `alpha` is the type I error rate. The last three are A/B simulations (two sample means are unequal): the proportion of p-values below the significance level `alpha` is the statistical power.

The [default](configs/default.toml) configuration parameters:

- Skewness: 30% of top users create 70% of value.
- Significance level `0.05`.
- Equal allocation of users between variants.
- Relative effect size 5%:
    - In A/A simulations: reference effect size for sample size calculation.
    - In A/B simulations: average effect size in treatment relative to control.

Other configurations, with difference from default:

- [smaller-alpha](configs/smaller-alpha.toml): significance level `0.01`.
- [smaller-diff](configs/smaller-diff.toml): effect size 2%.
- [stronger-skewness](configs/stronger-skewness.toml): 20% of top users create 80% of value.
- [unbalanced-ratio](configs/unbalanced-ratio.toml): 1:4 treatment to control users allocation.

## How to reproduce the results

[Install uv](https://github.com/astral-sh/uv?tab=readme-ov-file#installation) (if not already installed).

Clone the repository and change into the directory:

```bash
git clone git@github.com:e10v/mean-tests.git && cd mean-tests
```

Install dependencies:

```bash
uv sync --frozen
```

Run the simulation:

```bash
uv run mean-tests -c config/default.toml
```

Optionally run the simulations with different configurations:

```bash
uv run mean-tests -c configs/smaller-alpha.toml
uv run mean-tests -c configs/smaller-diff.toml
uv run mean-tests -c configs/stronger-skewness.toml
uv run mean-tests -c configs/unbalanced-ratio.toml
```

See the generated reports in the `reports/` directory.

## Discussion of the results

TODO

## Conclusions

TODO

## Note on "outliers"

TODO
