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

TODO

## How to reproduce the results

TODO

## Discussion of the results

TODO

## Conclusions

TODO

## Note on "outliers"

TODO
