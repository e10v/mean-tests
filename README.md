# Comparison of two-sample mean tests

## TL;DR

TODO

## Problem

### Analysis of means

In A/B tests, we usually want to check if the total amount of some value differ between two variants of a product. Examples of such values are revenue, transactions, clicks, impressions, and sessions. For this purpose, we compare the average values per user, where user is a randomization unit, and use a two-sample test of means to test the statistical significance of the difference.

Welch's t-test is a typical choice for analysis of means in a two-sample experiment. It's designed for unequal population variances and assumes that variances are unknown and inferred from the data. The alternative choices are:

- Student's t-test, assuming equal variances.
- Z-test of means with unpooled variance, assuming variances are known (while still inferred from the data when the test is used).

There is also a Z-test of means with *pooled* variance, assuming equal variances that are known. But I don't consider it here as it wouldn't provide any new meaningful insights about tests applicability.

### Bucket tests for large scale experiments

In large-scale experiments, it becomes costly to store and analyze data at user level. Often the bucket-level analysis is applied:

- Variants are still randomized at a user level.
- Users are randomly distributed between buckets using hash-functions, typically about 100 buckets per variant.
- Metrics are aggregated and analyzed at bucket level. For example, average revenue per average number of users in a bucket.

Bucket-level analysis still conforms to independence assumption.

### Mann–Whitney U test

Mann–Whitney U test is not a conventional choice if we want to check the total amount of some value differ between two variants. It's not a test of means. It tests the null hypothesis that probability of `x > y` is equal to probability of `x < y` for any pair `x` and `y` from control and treatment variants respectively.

*User-level* Mann–Whitney U test is an obvious bad choice, but some teams use the *bucket-level* Mann–Whitney U test as a test of means. Their reasoning is the following:

- Bucketization makes the distribution closer to normal.
- Under assumption of equal variances, Mann–Whitney U test can be used to test the equality of means of two normally distributed random variables.

### Problem formulation

This repository compares the following statistical test both at user- and bucket-level in the context of the analysis of two-sample means:

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
