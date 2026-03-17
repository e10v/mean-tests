# Comparison of two-sample mean tests

| parameter                  | value |
| :------------------------- | ----: |
| number of simulations      | 10000 |
| alpha                      |  0.05 |
| power                      |   0.8 |
| top users                  |   0.2 |
| value created by top users |   0.8 |

## A/A 0%: +5% top, -5% bottom (relative to total)

| parameter                               |  value |
| :-------------------------------------- | -----: |
| top users effect (relative to total)    |   0.05 |
| bottom users effect (relative to total) |  -0.05 |
| total relative effect                   |    0.0 |
| sample size                             | 329097 |

| test           |       level | type I error |  type I error ci |
| :------------- | ----------: | -----------: | ---------------: |
| Mann–Whitney U |       users |         1.00 |     [1.00, 1.00] |
| Mann–Whitney U | 100 buckets |       0.0921 | [0.0865, 0.0980] |
| Mann–Whitney U |  50 buckets |       0.0655 | [0.0608, 0.0706] |
| Mann–Whitney U |  20 buckets |       0.0564 | [0.0520, 0.0611] |
| Welch's t-test |       users |       0.0509 | [0.0467, 0.0554] |
| Welch's t-test | 100 buckets |       0.0507 | [0.0465, 0.0552] |
| Welch's t-test |  50 buckets |       0.0494 | [0.0453, 0.0539] |
| Welch's t-test |  10 buckets |       0.0479 | [0.0438, 0.0523] |
| Welch's t-test |  20 buckets |       0.0478 | [0.0437, 0.0522] |
| Mann–Whitney U |  10 buckets |       0.0467 | [0.0427, 0.0511] |

## A/A 0%: -5% top, +5% bottom (relative to total)

| parameter                               |  value |
| :-------------------------------------- | -----: |
| top users effect (relative to total)    |  -0.05 |
| bottom users effect (relative to total) |   0.05 |
| total relative effect                   |    0.0 |
| sample size                             | 162504 |

| test           |       level | type I error |  type I error ci |
| :------------- | ----------: | -----------: | ---------------: |
| Mann–Whitney U |       users |         1.00 |     [1.00, 1.00] |
| Mann–Whitney U | 100 buckets |       0.0735 | [0.0685, 0.0788] |
| Mann–Whitney U |  50 buckets |       0.0583 | [0.0538, 0.0631] |
| Mann–Whitney U |  20 buckets |       0.0522 | [0.0480, 0.0568] |
| Welch's t-test | 100 buckets |       0.0505 | [0.0463, 0.0550] |
| Welch's t-test |       users |       0.0503 | [0.0461, 0.0548] |
| Welch's t-test |  10 buckets |       0.0503 | [0.0461, 0.0548] |
| Welch's t-test |  50 buckets |       0.0499 | [0.0458, 0.0544] |
| Welch's t-test |  20 buckets |       0.0496 | [0.0455, 0.0541] |
| Mann–Whitney U |  10 buckets |       0.0482 | [0.0441, 0.0526] |

## A/B +5%: +4% top, +1% bottom (relative to total)

| parameter                               |  value |
| :-------------------------------------- | -----: |
| top users effect (relative to total)    |   0.04 |
| bottom users effect (relative to total) |   0.01 |
| total relative effect                   |   0.05 |
| sample size                             | 211250 |

| test           |       level | power |       power ci |
| :------------- | ----------: | ----: | -------------: |
| Mann–Whitney U |       users |  1.00 |   [1.00, 1.00] |
| Mann–Whitney U | 100 buckets | 0.867 | [0.860, 0.873] |
| Mann–Whitney U |  50 buckets | 0.846 | [0.839, 0.853] |
| Welch's t-test |       users | 0.812 | [0.804, 0.820] |
| Welch's t-test | 100 buckets | 0.807 | [0.799, 0.815] |
| Welch's t-test |  50 buckets | 0.802 | [0.794, 0.810] |
| Mann–Whitney U |  20 buckets | 0.798 | [0.790, 0.806] |
| Welch's t-test |  20 buckets | 0.789 | [0.781, 0.797] |
| Welch's t-test |  10 buckets | 0.763 | [0.755, 0.772] |
| Mann–Whitney U |  10 buckets | 0.737 | [0.729, 0.746] |

## A/B +5%: +5% top, 0% bottom (relative to total)

| parameter                               |  value |
| :-------------------------------------- | -----: |
| top users effect (relative to total)    |   0.05 |
| bottom users effect (relative to total) |    0.0 |
| total relative effect                   |   0.05 |
| sample size                             | 225912 |

| test           |       level | power |       power ci |
| :------------- | ----------: | ----: | -------------: |
| Mann–Whitney U | 100 buckets | 0.841 | [0.834, 0.848] |
| Mann–Whitney U |  50 buckets | 0.823 | [0.815, 0.830] |
| Welch's t-test |       users | 0.805 | [0.797, 0.813] |
| Welch's t-test | 100 buckets | 0.799 | [0.791, 0.807] |
| Welch's t-test |  50 buckets | 0.795 | [0.787, 0.802] |
| Mann–Whitney U |  20 buckets | 0.792 | [0.784, 0.800] |
| Welch's t-test |  20 buckets | 0.786 | [0.778, 0.794] |
| Welch's t-test |  10 buckets | 0.760 | [0.751, 0.768] |
| Mann–Whitney U |  10 buckets | 0.737 | [0.728, 0.745] |
| Mann–Whitney U |       users | 0.273 | [0.265, 0.282] |

## A/B +5%: 0% top, +5% bottom (relative to total)

| parameter                               |  value |
| :-------------------------------------- | -----: |
| top users effect (relative to total)    |    0.0 |
| bottom users effect (relative to total) |   0.05 |
| total relative effect                   |   0.05 |
| sample size                             | 171025 |

| test           |       level | power |       power ci |
| :------------- | ----------: | ----: | -------------: |
| Mann–Whitney U |       users |  1.00 |   [1.00, 1.00] |
| Mann–Whitney U | 100 buckets | 0.921 | [0.915, 0.926] |
| Mann–Whitney U |  50 buckets | 0.876 | [0.869, 0.882] |
| Mann–Whitney U |  20 buckets | 0.817 | [0.809, 0.824] |
| Welch's t-test |       users | 0.798 | [0.790, 0.805] |
| Welch's t-test | 100 buckets | 0.796 | [0.788, 0.804] |
| Welch's t-test |  50 buckets | 0.790 | [0.782, 0.798] |
| Welch's t-test |  20 buckets | 0.778 | [0.770, 0.786] |
| Welch's t-test |  10 buckets | 0.753 | [0.744, 0.761] |
| Mann–Whitney U |  10 buckets | 0.737 | [0.728, 0.746] |
