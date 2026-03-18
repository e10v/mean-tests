# Comparison of two-sample mean tests

| parameter                             | value |
| :------------------------------------ | ----: |
| number of simulations                 | 10000 |
| alpha                                 |  0.05 |
| reference power                       |   0.8 |
| treatment-to-control allocation ratio |   1.0 |
| top users                             |   0.3 |
| value created by top users            |   0.7 |

## A/A 0%: +5% top, -5% bottom (relative to total)

| parameter                               | value |
| :-------------------------------------- | ----: |
| top users effect (relative to total)    |  0.05 |
| bottom users effect (relative to total) | -0.05 |
| total relative effect                   |   0.0 |
| sample size                             | 34802 |

| test              |       level | type I error |  type I error ci |
| :---------------- | ----------: | -----------: | ---------------: |
| Mann–Whitney U    |       users |         1.00 |     [1.00, 1.00] |
| Z-test (unpooled) |  10 buckets |       0.0678 | [0.0630, 0.0729] |
| Mann–Whitney U    | 100 buckets |       0.0674 | [0.0626, 0.0725] |
| Z-test (unpooled) |  20 buckets |       0.0587 | [0.0542, 0.0635] |
| Mann–Whitney U    |  50 buckets |       0.0565 | [0.0521, 0.0612] |
| Z-test (unpooled) |  50 buckets |       0.0548 | [0.0505, 0.0595] |
| Z-test (unpooled) | 100 buckets |       0.0528 | [0.0485, 0.0574] |
| Student's t-test  |  10 buckets |       0.0525 | [0.0482, 0.0571] |
| Student's t-test  |  50 buckets |       0.0519 | [0.0477, 0.0565] |
| Welch's t-test    |  50 buckets |       0.0517 | [0.0475, 0.0563] |
| Mann–Whitney U    |  20 buckets |       0.0517 | [0.0475, 0.0563] |
| Student's t-test  | 100 buckets |       0.0512 | [0.0470, 0.0557] |
| Welch's t-test    | 100 buckets |       0.0511 | [0.0469, 0.0556] |
| Welch's t-test    |  10 buckets |       0.0508 | [0.0466, 0.0553] |
| Student's t-test  |  20 buckets |       0.0508 | [0.0466, 0.0553] |
| Z-test (unpooled) |       users |       0.0505 | [0.0463, 0.0550] |
| Welch's t-test    |       users |       0.0505 | [0.0463, 0.0550] |
| Student's t-test  |       users |       0.0504 | [0.0462, 0.0549] |
| Welch's t-test    |  20 buckets |       0.0501 | [0.0459, 0.0546] |
| Mann–Whitney U    |  10 buckets |       0.0452 | [0.0413, 0.0495] |

## A/A 0%: -5% top, +5% bottom (relative to total)

| parameter                               | value |
| :-------------------------------------- | ----: |
| top users effect (relative to total)    | -0.05 |
| bottom users effect (relative to total) |  0.05 |
| total relative effect                   |   0.0 |
| sample size                             | 21499 |

| test              |       level | type I error |  type I error ci |
| :---------------- | ----------: | -----------: | ---------------: |
| Mann–Whitney U    |       users |         1.00 |     [1.00, 1.00] |
| Z-test (unpooled) |  10 buckets |       0.0678 | [0.0630, 0.0729] |
| Mann–Whitney U    | 100 buckets |       0.0628 | [0.0582, 0.0678] |
| Z-test (unpooled) |  20 buckets |       0.0582 | [0.0537, 0.0630] |
| Z-test (unpooled) |  50 buckets |       0.0570 | [0.0526, 0.0618] |
| Mann–Whitney U    |  50 buckets |       0.0558 | [0.0514, 0.0605] |
| Student's t-test  |  50 buckets |       0.0541 | [0.0498, 0.0588] |
| Welch's t-test    |  50 buckets |       0.0539 | [0.0496, 0.0586] |
| Student's t-test  |       users |       0.0538 | [0.0495, 0.0584] |
| Z-test (unpooled) |       users |       0.0537 | [0.0494, 0.0583] |
| Welch's t-test    |       users |       0.0537 | [0.0494, 0.0583] |
| Z-test (unpooled) | 100 buckets |       0.0535 | [0.0492, 0.0581] |
| Student's t-test  |  10 buckets |       0.0532 | [0.0489, 0.0578] |
| Mann–Whitney U    |  20 buckets |       0.0526 | [0.0483, 0.0572] |
| Welch's t-test    | 100 buckets |       0.0518 | [0.0476, 0.0564] |
| Student's t-test  | 100 buckets |       0.0518 | [0.0476, 0.0564] |
| Student's t-test  |  20 buckets |       0.0517 | [0.0475, 0.0563] |
| Welch's t-test    |  20 buckets |       0.0507 | [0.0465, 0.0552] |
| Welch's t-test    |  10 buckets |       0.0506 | [0.0464, 0.0551] |
| Mann–Whitney U    |  10 buckets |       0.0488 | [0.0447, 0.0533] |

## A/B +5%: +3.5% top, +1.5% bottom (relative to total)

| parameter                               | value |
| :-------------------------------------- | ----: |
| top users effect (relative to total)    | 0.035 |
| bottom users effect (relative to total) | 0.015 |
| total relative effect                   |  0.05 |
| sample size                             | 26458 |

| test              |       level | power |       power ci |
| :---------------- | ----------: | ----: | -------------: |
| Mann–Whitney U    |       users | 0.962 | [0.958, 0.966] |
| Z-test (unpooled) | 100 buckets | 0.810 | [0.803, 0.818] |
| Z-test (unpooled) |       users | 0.810 | [0.802, 0.818] |
| Welch's t-test    |       users | 0.810 | [0.802, 0.818] |
| Student's t-test  |       users | 0.810 | [0.802, 0.817] |
| Z-test (unpooled) |  20 buckets | 0.809 | [0.801, 0.816] |
| Z-test (unpooled) |  50 buckets | 0.808 | [0.801, 0.816] |
| Mann–Whitney U    | 100 buckets | 0.808 | [0.800, 0.816] |
| Welch's t-test    | 100 buckets | 0.807 | [0.799, 0.814] |
| Student's t-test  | 100 buckets | 0.807 | [0.799, 0.814] |
| Student's t-test  |  50 buckets | 0.802 | [0.794, 0.810] |
| Z-test (unpooled) |  10 buckets | 0.802 | [0.794, 0.810] |
| Welch's t-test    |  50 buckets | 0.802 | [0.794, 0.810] |
| Student's t-test  |  20 buckets | 0.791 | [0.783, 0.799] |
| Welch's t-test    |  20 buckets | 0.790 | [0.782, 0.798] |
| Mann–Whitney U    |  50 buckets | 0.789 | [0.781, 0.797] |
| Mann–Whitney U    |  20 buckets | 0.772 | [0.763, 0.780] |
| Student's t-test  |  10 buckets | 0.762 | [0.754, 0.771] |
| Welch's t-test    |  10 buckets | 0.757 | [0.749, 0.766] |
| Mann–Whitney U    |  10 buckets | 0.714 | [0.705, 0.722] |

## A/B +5%: +5% top, 0% bottom (relative to total)

| parameter                               | value |
| :-------------------------------------- | ----: |
| top users effect (relative to total)    |  0.05 |
| bottom users effect (relative to total) |   0.0 |
| total relative effect                   |  0.05 |
| sample size                             | 28391 |

| test              |       level |  power |         power ci |
| :---------------- | ----------: | -----: | ---------------: |
| Z-test (unpooled) |  50 buckets |  0.807 |   [0.800, 0.815] |
| Student's t-test  |       users |  0.807 |   [0.799, 0.815] |
| Z-test (unpooled) |       users |  0.807 |   [0.799, 0.815] |
| Welch's t-test    |       users |  0.807 |   [0.799, 0.815] |
| Z-test (unpooled) | 100 buckets |  0.805 |   [0.798, 0.813] |
| Z-test (unpooled) |  20 buckets |  0.804 |   [0.796, 0.811] |
| Student's t-test  | 100 buckets |  0.802 |   [0.794, 0.810] |
| Welch's t-test    | 100 buckets |  0.802 |   [0.794, 0.809] |
| Student's t-test  |  50 buckets |  0.800 |   [0.792, 0.808] |
| Welch's t-test    |  50 buckets |  0.800 |   [0.792, 0.808] |
| Z-test (unpooled) |  10 buckets |  0.798 |   [0.790, 0.806] |
| Student's t-test  |  20 buckets |  0.784 |   [0.776, 0.792] |
| Welch's t-test    |  20 buckets |  0.784 |   [0.775, 0.792] |
| Mann–Whitney U    |  50 buckets |  0.778 |   [0.770, 0.786] |
| Mann–Whitney U    | 100 buckets |  0.775 |   [0.767, 0.784] |
| Mann–Whitney U    |  20 buckets |  0.759 |   [0.751, 0.768] |
| Student's t-test  |  10 buckets |  0.757 |   [0.749, 0.765] |
| Welch's t-test    |  10 buckets |  0.752 |   [0.744, 0.761] |
| Mann–Whitney U    |  10 buckets |  0.710 |   [0.701, 0.718] |
| Mann–Whitney U    |       users | 0.0662 | [0.0614, 0.0713] |

## A/B +5%: 0% top, +5% bottom (relative to total)

| parameter                               | value |
| :-------------------------------------- | ----: |
| top users effect (relative to total)    |   0.0 |
| bottom users effect (relative to total) |  0.05 |
| total relative effect                   |  0.05 |
| sample size                             | 22899 |

| test              |       level | power |       power ci |
| :---------------- | ----------: | ----: | -------------: |
| Mann–Whitney U    |       users |  1.00 |   [1.00, 1.00] |
| Mann–Whitney U    | 100 buckets | 0.840 | [0.832, 0.847] |
| Mann–Whitney U    |  50 buckets | 0.806 | [0.798, 0.813] |
| Z-test (unpooled) |  50 buckets | 0.799 | [0.791, 0.807] |
| Student's t-test  |       users | 0.799 | [0.791, 0.807] |
| Z-test (unpooled) |       users | 0.798 | [0.790, 0.806] |
| Welch's t-test    |       users | 0.798 | [0.790, 0.806] |
| Z-test (unpooled) | 100 buckets | 0.796 | [0.788, 0.804] |
| Z-test (unpooled) |  20 buckets | 0.795 | [0.787, 0.803] |
| Student's t-test  |  50 buckets | 0.794 | [0.786, 0.801] |
| Welch's t-test    |  50 buckets | 0.793 | [0.785, 0.801] |
| Student's t-test  | 100 buckets | 0.793 | [0.784, 0.800] |
| Welch's t-test    | 100 buckets | 0.792 | [0.784, 0.800] |
| Z-test (unpooled) |  10 buckets | 0.792 | [0.784, 0.800] |
| Student's t-test  |  20 buckets | 0.776 | [0.768, 0.784] |
| Welch's t-test    |  20 buckets | 0.775 | [0.766, 0.783] |
| Mann–Whitney U    |  20 buckets | 0.767 | [0.759, 0.776] |
| Student's t-test  |  10 buckets | 0.752 | [0.744, 0.761] |
| Welch's t-test    |  10 buckets | 0.747 | [0.738, 0.755] |
| Mann–Whitney U    |  10 buckets | 0.713 | [0.704, 0.722] |
