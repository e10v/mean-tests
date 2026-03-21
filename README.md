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

In real-world scenarios, the distribution of a metric across users is often highly skewed and follows a Pareto-like pattern: 10–30% of users create 70–90% of the value (revenue, transactions, sessions, and so on). For convenience, we call these 10–30% of users the "top" users and the rest the "bottom" users. The treatment effect is often distributed unevenly across users. Sometimes, it even goes in opposite directions for top and bottom users, with a near-zero average effect.

The code in this repository simulates many experiments with skewed data sampled from a lognormal distribution. The skewness is determined by a Pareto-like rule: the top `P` share of users creates the `Q` share of value. The treatment effect is defined separately for top and bottom users. Sample size is estimated to target a power of `0.8`.

Five types of treatments are simulated, `10_000` times each:

1. Positive effect on top users, negative effect on bottom users, and zero overall average effect.
2. Negative effect on top users, positive effect on bottom users, and zero overall average effect.
3. Positive effect on all users.
4. Positive effect on top users, zero average effect on bottom users, and a positive overall effect.
5. Zero average effect on top users, positive effect on bottom users, and a positive overall effect.

The first two are labeled A/A because the overall population means are equal, even though the treatment effect differs between top and bottom users. For these cases, the proportion of p-values below the significance level `alpha` estimates the type I error rate. The last three are A/B simulations with unequal overall population means, so the proportion of p-values below the significance level `alpha` estimates the statistical power.

The [default](configs/default.toml) configuration uses the following parameters:

- Skewness: 30% of top users create 70% of value.
- Significance level `0.05`.
- Equal allocation of users between variants.
- Relative effect size 5%:
    - In A/A simulations: reference effect size for sample size calculation.
    - In A/B simulations: average effect size in treatment relative to control.

Other configurations differ from the default as follows:

- [smaller-alpha](configs/smaller-alpha.toml): significance level `0.01`.
- [smaller-diff](configs/smaller-diff.toml): effect size 2%.
- [stronger-skewness](configs/stronger-skewness.toml): 20% of top users create 80% of value.
- [unbalanced-ratio](configs/unbalanced-ratio.toml): 1:4 treatment-to-control
  user allocation.

## How to reproduce the results

[Install uv](https://github.com/astral-sh/uv?tab=readme-ov-file#installation) if it is not already installed.

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
uv run mean-tests -c configs/default.toml
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

Three patterns stand out across the reports.

First, the mean-based tests behave as expected at the user level. In the balanced configurations, Welch's t-test, Student's t-test, and the unpooled z-test stay close to the target type I error rate and reach the planned power of about `0.8`. In other words, once the goal is to compare means, the ordinary mean tests are doing the job even under strong skewness. The main exception is the [unbalanced-ratio](configs/unbalanced-ratio.toml) configuration. There, the treatment-to-control ratio is `1:4`, the treatment variance can differ from the control variance, and Student's equal-variance assumption starts to matter. In [reports/unbalanced-ratio.md](reports/unbalanced-ratio.md), the user-level Student's t-test has type I error `0.0905` in one A/A scenario and `0.0233` in the other, while Welch's t-test and the unpooled z-test stay close to `0.05`. This is the clearest practical reason to prefer Welch's t-test by default.

Second, the user-level Mann–Whitney U test is not a test of means, and the simulations make that visible immediately. In every configuration, it rejects the null in essentially `100%` of the A/A simulations even though the overall means are equal. Its reported "power" in A/B simulations also depends much more on where the effect is concentrated than on the total mean effect. For example, when only bottom users improve, the user-level Mann–Whitney U test is close to `1.00` power in [reports/default.md](reports/default.md), [reports/smaller-alpha.md](reports/smaller-alpha.md), and [reports/stronger-skewness.md](reports/stronger-skewness.md). When only top users improve, its power collapses to `0.0662`, `0.0165`, and `0.265` in those same reports. That matches the code logic and the definition of the test: the simulation changes the ordering of observations differently for top and bottom users, so Mann–Whitney U reacts to distribution shifts that are not the same thing as a change in the mean.

Third, bucketization can preserve the behavior of mean tests, but only up to a point. With `50` or `100` buckets per variant, bucket-level Welch's t-test and Student's t-test are usually close to their user-level counterparts, and the bucket-level unpooled z-test is often similar as well. With only `10` buckets, power drops noticeably. The bucket-level unpooled z-test is also a bit liberal in A/A simulations, especially with fewer buckets. Bucket-level Mann–Whitney U is the least stable option: both type I error and power depend strongly on the number of buckets, skewness, and allocation ratio. In [reports/stronger-skewness.md](reports/stronger-skewness.md), its type I error reaches `0.0930` with `100` buckets, and in [reports/unbalanced-ratio.md](reports/unbalanced-ratio.md) it reaches `0.168`. So bucketization does not make Mann–Whitney U a reliable proxy for a test of means.

## Conclusions

If the goal is to compare the average value per user, Welch's t-test is the safest default in these simulations. It keeps the type I error rate close to the target, reaches the planned power, and stays reliable when the allocation ratio is unbalanced. Student's t-test is less robust when variances differ, while the unpooled z-test is usually similar to Welch's t-test but is a less natural default in practice.

Bucketization is a practical compromise, not a better method. With `50` or `100` buckets per variant, bucket-level mean tests are usually close to user-level results; with `10` or `20` buckets, power drops and the bucket-level unpooled z-test becomes slightly liberal. Mann–Whitney U is not a test of means and is unreliable here at both user and bucket levels.

## Note on "outliers"

TODO
