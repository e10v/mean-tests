# Simulation

| parameter                  | value |
| :------------------------- | ----: |
| number of simulations      | 10000 |
| alpha                      |  0.05 |
| power                      |   0.8 |
| top users                  |   0.3 |
| value created by top users |   0.7 |

## A/A: +5pp top, -5pp bottom, 0pp total

| parameter              | value |
| :--------------------- | ----: |
| effect on top users    |   5pp |
| effect on bottom users |  -5pp |
| total effect           |   0pp |
| sample size            | 34802 |

| test           | level       | type I error |  type I error ci |
| :------------- | :---------- | -----------: | ---------------: |
| Mann–Whitney U | users       |         1.00 |     [1.00, 1.00] |
| Mann–Whitney U | 100 buckets |       0.0577 | [0.0532, 0.0625] |
| Mann–Whitney U | 50 buckets  |       0.0497 | [0.0456, 0.0542] |
| Welch's t-test | 100 buckets |       0.0479 | [0.0438, 0.0523] |
| Welch's t-test | 50 buckets  |       0.0476 | [0.0435, 0.0520] |
| Mann–Whitney U | 20 buckets  |       0.0475 | [0.0435, 0.0519] |
| Welch's t-test | 10 buckets  |       0.0473 | [0.0433, 0.0517] |
| Welch's t-test | 20 buckets  |       0.0472 | [0.0432, 0.0516] |
| Welch's t-test | users       |       0.0457 | [0.0417, 0.0500] |
| Mann–Whitney U | 10 buckets  |       0.0441 | [0.0402, 0.0484] |

## A/A: -5pp top, +5pp bottom, 0pp total

| parameter              | value |
| :--------------------- | ----: |
| effect on top users    |  -5pp |
| effect on bottom users |   5pp |
| total effect           |   0pp |
| sample size            | 21499 |

| test           | level       | type I error |  type I error ci |
| :------------- | :---------- | -----------: | ---------------: |
| Mann–Whitney U | users       |         1.00 |     [1.00, 1.00] |
| Mann–Whitney U | 100 buckets |       0.0619 | [0.0573, 0.0668] |
| Mann–Whitney U | 50 buckets  |       0.0542 | [0.0499, 0.0589] |
| Welch's t-test | 20 buckets  |       0.0532 | [0.0489, 0.0578] |
| Mann–Whitney U | 20 buckets  |       0.0532 | [0.0489, 0.0578] |
| Welch's t-test | 100 buckets |       0.0525 | [0.0482, 0.0571] |
| Welch's t-test | 50 buckets  |       0.0522 | [0.0480, 0.0568] |
| Welch's t-test | users       |       0.0515 | [0.0473, 0.0561] |
| Welch's t-test | 10 buckets  |       0.0499 | [0.0458, 0.0544] |
| Mann–Whitney U | 10 buckets  |       0.0479 | [0.0438, 0.0523] |

## A/B: +3.5pp top, +1.5pp bottom, +5pp total

| parameter              | value |
| :--------------------- | ----: |
| effect on top users    | 3.5pp |
| effect on bottom users | 1.5pp |
| total effect           |   5pp |
| sample size            | 26458 |

| test           | level       | power |       power ci |
| :------------- | :---------- | ----: | -------------: |
| Mann–Whitney U | users       | 0.961 | [0.957, 0.965] |
| Welch's t-test | users       | 0.807 | [0.799, 0.814] |
| Welch's t-test | 100 buckets | 0.804 | [0.796, 0.811] |
| Welch's t-test | 50 buckets  | 0.797 | [0.789, 0.805] |
| Mann–Whitney U | 100 buckets | 0.795 | [0.787, 0.803] |
| Mann–Whitney U | 50 buckets  | 0.788 | [0.780, 0.796] |
| Welch's t-test | 20 buckets  | 0.782 | [0.774, 0.790] |
| Mann–Whitney U | 20 buckets  | 0.767 | [0.759, 0.776] |
| Welch's t-test | 10 buckets  | 0.755 | [0.746, 0.763] |
| Mann–Whitney U | 10 buckets  | 0.715 | [0.706, 0.724] |

## A/B: +5pp top, 0pp bottom, +5pp total

| parameter              | value |
| :--------------------- | ----: |
| effect on top users    |   5pp |
| effect on bottom users |   0pp |
| total effect           |   5pp |
| sample size            | 28391 |

| test           | level       |  power |         power ci |
| :------------- | :---------- | -----: | ---------------: |
| Welch's t-test | users       |  0.803 |   [0.795, 0.811] |
| Welch's t-test | 100 buckets |  0.801 |   [0.793, 0.809] |
| Welch's t-test | 50 buckets  |  0.794 |   [0.786, 0.802] |
| Welch's t-test | 20 buckets  |  0.782 |   [0.774, 0.790] |
| Mann–Whitney U | 100 buckets |  0.776 |   [0.767, 0.784] |
| Mann–Whitney U | 50 buckets  |  0.774 |   [0.766, 0.782] |
| Mann–Whitney U | 20 buckets  |  0.759 |   [0.751, 0.767] |
| Welch's t-test | 10 buckets  |  0.751 |   [0.743, 0.760] |
| Mann–Whitney U | 10 buckets  |  0.708 |   [0.699, 0.717] |
| Mann–Whitney U | users       | 0.0628 | [0.0582, 0.0678] |

## A/B: 0pp top, +5pp bottom, +5pp total

| parameter              | value |
| :--------------------- | ----: |
| effect on top users    |   0pp |
| effect on bottom users |   5pp |
| total effect           |   5pp |
| sample size            | 22899 |

| test           | level       | power |       power ci |
| :------------- | :---------- | ----: | -------------: |
| Mann–Whitney U | users       |  1.00 |   [1.00, 1.00] |
| Mann–Whitney U | 100 buckets | 0.839 | [0.831, 0.846] |
| Welch's t-test | users       | 0.802 | [0.794, 0.810] |
| Mann–Whitney U | 50 buckets  | 0.802 | [0.794, 0.809] |
| Welch's t-test | 100 buckets | 0.799 | [0.791, 0.807] |
| Welch's t-test | 50 buckets  | 0.791 | [0.783, 0.799] |
| Welch's t-test | 20 buckets  | 0.778 | [0.770, 0.787] |
| Mann–Whitney U | 20 buckets  | 0.768 | [0.759, 0.776] |
| Welch's t-test | 10 buckets  | 0.752 | [0.744, 0.761] |
| Mann–Whitney U | 10 buckets  | 0.714 | [0.705, 0.722] |
