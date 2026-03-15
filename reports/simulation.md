# Simulation

| parameter                  | value |
| :------------------------- | ----: |
| number of simulations      | 10000 |
| alpha                      |  0.05 |
| power                      |   0.8 |
| top users                  |   0.3 |
| value created by top users |   0.7 |

## A/A: +5pp top, -5pp bottom, 0% total

| parameter              | value |
| :--------------------- | ----: |
| effect on top users    |   5pp |
| effect on bottom users |  -5pp |
| total effect           |   0pp |
| sample size            | 34802 |

| test                              | type I error |  type I error ci |
| :-------------------------------- | -----------: | ---------------: |
| Mann–Whitney U test (users)       |         1.00 |     [1.00, 1.00] |
| Mann–Whitney U test (100 buckets) |       0.0577 | [0.0532, 0.0625] |
| Mann–Whitney U test (50 buckets)  |       0.0497 | [0.0456, 0.0542] |
| Student's t-test (10 buckets)     |       0.0488 | [0.0447, 0.0533] |
| Welch's t-test (100 buckets)      |       0.0479 | [0.0438, 0.0523] |
| Student's t-test (100 buckets)    |       0.0479 | [0.0438, 0.0523] |
| Student's t-test (50 buckets)     |       0.0477 | [0.0436, 0.0521] |
| Welch's t-test (50 buckets)       |       0.0476 | [0.0435, 0.0520] |
| Student's t-test (20 buckets)     |       0.0475 | [0.0435, 0.0519] |
| Mann–Whitney U test (20 buckets)  |       0.0475 | [0.0435, 0.0519] |
| Welch's t-test (10 buckets)       |       0.0473 | [0.0433, 0.0517] |
| Welch's t-test (20 buckets)       |       0.0472 | [0.0432, 0.0516] |
| Welch's t-test (users)            |       0.0457 | [0.0417, 0.0500] |
| Student's t-test (users)          |       0.0456 | [0.0416, 0.0499] |
| Mann–Whitney U test (10 buckets)  |       0.0441 | [0.0402, 0.0484] |

## A/A: -5pp top, +5pp bottom, 0% total

| parameter              | value |
| :--------------------- | ----: |
| effect on top users    |  -5pp |
| effect on bottom users |   5pp |
| total effect           |   0pp |
| sample size            | 21499 |

| test                              | type I error |  type I error ci |
| :-------------------------------- | -----------: | ---------------: |
| Mann–Whitney U test (users)       |         1.00 |     [1.00, 1.00] |
| Mann–Whitney U test (100 buckets) |       0.0619 | [0.0573, 0.0668] |
| Mann–Whitney U test (50 buckets)  |       0.0542 | [0.0499, 0.0589] |
| Student's t-test (20 buckets)     |       0.0533 | [0.0490, 0.0579] |
| Welch's t-test (20 buckets)       |       0.0532 | [0.0489, 0.0578] |
| Mann–Whitney U test (20 buckets)  |       0.0532 | [0.0489, 0.0578] |
| Student's t-test (100 buckets)    |       0.0526 | [0.0483, 0.0572] |
| Welch's t-test (100 buckets)      |       0.0525 | [0.0482, 0.0571] |
| Student's t-test (50 buckets)     |       0.0523 | [0.0481, 0.0569] |
| Welch's t-test (50 buckets)       |       0.0522 | [0.0480, 0.0568] |
| Student's t-test (10 buckets)     |       0.0520 | [0.0478, 0.0566] |
| Student's t-test (users)          |       0.0516 | [0.0474, 0.0562] |
| Welch's t-test (users)            |       0.0515 | [0.0473, 0.0561] |
| Welch's t-test (10 buckets)       |       0.0499 | [0.0458, 0.0544] |
| Mann–Whitney U test (10 buckets)  |       0.0479 | [0.0438, 0.0523] |

## A/B: +5pp top, 0pp bottom, 5% total

| parameter              | value |
| :--------------------- | ----: |
| effect on top users    |   5pp |
| effect on bottom users |   0pp |
| total effect           |   5pp |
| sample size            | 28391 |

| test                              |  power |         power ci |
| :-------------------------------- | -----: | ---------------: |
| Student's t-test (users)          |  0.803 |   [0.795, 0.811] |
| Welch's t-test (users)            |  0.803 |   [0.795, 0.811] |
| Welch's t-test (100 buckets)      |  0.798 |   [0.790, 0.806] |
| Student's t-test (100 buckets)    |  0.798 |   [0.790, 0.806] |
| Student's t-test (50 buckets)     |  0.793 |   [0.785, 0.801] |
| Welch's t-test (50 buckets)       |  0.792 |   [0.784, 0.800] |
| Student's t-test (20 buckets)     |  0.778 |   [0.769, 0.786] |
| Welch's t-test (20 buckets)       |  0.776 |   [0.768, 0.785] |
| Mann–Whitney U test (100 buckets) |  0.776 |   [0.767, 0.784] |
| Mann–Whitney U test (50 buckets)  |  0.770 |   [0.762, 0.778] |
| Mann–Whitney U test (20 buckets)  |  0.759 |   [0.750, 0.767] |
| Student's t-test (10 buckets)     |  0.758 |   [0.749, 0.766] |
| Welch's t-test (10 buckets)       |  0.753 |   [0.744, 0.761] |
| Mann–Whitney U test (10 buckets)  |  0.714 |   [0.705, 0.723] |
| Mann–Whitney U test (users)       | 0.0616 | [0.0570, 0.0665] |

## A/B: 0pp top, +5pp bottom, 5% total

| parameter              | value |
| :--------------------- | ----: |
| effect on top users    |   0pp |
| effect on bottom users |   5pp |
| total effect           |   5pp |
| sample size            | 22899 |

| test                              | power |       power ci |
| :-------------------------------- | ----: | -------------: |
| Mann–Whitney U test (users)       |  1.00 |   [1.00, 1.00] |
| Mann–Whitney U test (100 buckets) | 0.838 | [0.831, 0.845] |
| Mann–Whitney U test (50 buckets)  | 0.805 | [0.797, 0.813] |
| Welch's t-test (users)            | 0.797 | [0.789, 0.805] |
| Student's t-test (users)          | 0.797 | [0.789, 0.805] |
| Student's t-test (100 buckets)    | 0.794 | [0.786, 0.802] |
| Welch's t-test (100 buckets)      | 0.794 | [0.786, 0.802] |
| Student's t-test (50 buckets)     | 0.791 | [0.783, 0.799] |
| Welch's t-test (50 buckets)       | 0.791 | [0.783, 0.799] |
| Student's t-test (20 buckets)     | 0.774 | [0.766, 0.782] |
| Welch's t-test (20 buckets)       | 0.773 | [0.764, 0.781] |
| Mann–Whitney U test (20 buckets)  | 0.765 | [0.756, 0.773] |
| Student's t-test (10 buckets)     | 0.751 | [0.742, 0.759] |
| Welch's t-test (10 buckets)       | 0.745 | [0.737, 0.754] |
| Mann–Whitney U test (10 buckets)  | 0.714 | [0.705, 0.723] |
