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

In large-scale experiments, it becomes costly to store and analyze data on user level. Often the bucket-level analysis is applied:

- Variants are still randomized on a user level.
- Users are randomly distributed between buckets using hash-functions, typically about 100 buckets per variant.

### Mann–Whitney U test

TODO

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
