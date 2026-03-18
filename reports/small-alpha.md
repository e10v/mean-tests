# Comparison of two-sample mean tests

| parameter                             | value |
| :------------------------------------ | ----: |
| number of simulations                 | 10000 |
| alpha                                 |  0.01 |
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
| sample size                             | 51785 |

| test              |       level | type I error |   type I error ci |
| :---------------- | ----------: | -----------: | ----------------: |
| Mann–Whitney U    |       users |         1.00 |      [1.00, 1.00] |
| Z-test (unpooled) |  10 buckets |       0.0189 |  [0.0164, 0.0218] |
| Z-test (unpooled) |  20 buckets |       0.0159 |  [0.0136, 0.0186] |
| Mann–Whitney U    | 100 buckets |       0.0137 |  [0.0116, 0.0162] |
| Z-test (unpooled) | 100 buckets |       0.0119 | [0.00991, 0.0143] |
| Z-test (unpooled) |  50 buckets |       0.0117 | [0.00973, 0.0141] |
| Student's t-test  |  20 buckets |       0.0117 | [0.00973, 0.0141] |
| Welch's t-test    |  20 buckets |       0.0114 | [0.00945, 0.0137] |
| Student's t-test  | 100 buckets |       0.0112 | [0.00927, 0.0135] |
| Welch's t-test    | 100 buckets |       0.0111 | [0.00918, 0.0134] |
| Z-test (unpooled) |       users |       0.0107 | [0.00882, 0.0130] |
| Welch's t-test    |       users |       0.0107 | [0.00882, 0.0130] |
| Student's t-test  |       users |       0.0107 | [0.00882, 0.0130] |
| Student's t-test  |  50 buckets |       0.0107 | [0.00882, 0.0130] |
| Mann–Whitney U    |  50 buckets |       0.0107 | [0.00882, 0.0130] |
| Welch's t-test    |  50 buckets |       0.0106 | [0.00873, 0.0129] |
| Student's t-test  |  10 buckets |       0.0105 | [0.00864, 0.0127] |
| Mann–Whitney U    |  20 buckets |       0.0104 | [0.00855, 0.0126] |
| Welch's t-test    |  10 buckets |       0.0102 | [0.00836, 0.0124] |
| Mann–Whitney U    |  10 buckets |      0.00800 | [0.00639, 0.0100] |

## A/A 0%: -5% top, +5% bottom (relative to total)

| parameter                               | value |
| :-------------------------------------- | ----: |
| top users effect (relative to total)    | -0.05 |
| bottom users effect (relative to total) |  0.05 |
| total relative effect                   |   0.0 |
| sample size                             | 31990 |

| test              |       level | type I error |    type I error ci |
| :---------------- | ----------: | -----------: | -----------------: |
| Mann–Whitney U    |       users |         1.00 |       [1.00, 1.00] |
| Z-test (unpooled) |  10 buckets |       0.0210 |   [0.0183, 0.0241] |
| Z-test (unpooled) |  20 buckets |       0.0159 |   [0.0136, 0.0186] |
| Z-test (unpooled) |  50 buckets |       0.0118 |  [0.00982, 0.0142] |
| Mann–Whitney U    | 100 buckets |       0.0114 |  [0.00945, 0.0137] |
| Student's t-test  |  20 buckets |       0.0108 |  [0.00891, 0.0131] |
| Student's t-test  |  50 buckets |       0.0105 |  [0.00864, 0.0127] |
| Z-test (unpooled) | 100 buckets |       0.0104 |  [0.00855, 0.0126] |
| Welch's t-test    |  50 buckets |       0.0103 |  [0.00846, 0.0125] |
| Welch's t-test    |  20 buckets |       0.0103 |  [0.00846, 0.0125] |
| Student's t-test  |  10 buckets |       0.0103 |  [0.00846, 0.0125] |
| Z-test (unpooled) |       users |      0.00980 |  [0.00800, 0.0120] |
| Welch's t-test    |       users |      0.00980 |  [0.00800, 0.0120] |
| Student's t-test  |       users |      0.00980 |  [0.00800, 0.0120] |
| Welch's t-test    | 100 buckets |      0.00970 |  [0.00791, 0.0119] |
| Welch's t-test    |  10 buckets |      0.00970 |  [0.00791, 0.0119] |
| Student's t-test  | 100 buckets |      0.00970 |  [0.00791, 0.0119] |
| Mann–Whitney U    |  20 buckets |      0.00970 |  [0.00791, 0.0119] |
| Mann–Whitney U    |  50 buckets |      0.00950 |  [0.00773, 0.0117] |
| Mann–Whitney U    |  10 buckets |      0.00770 | [0.00612, 0.00967] |

## A/B +5%: +3.5% top, +1.5% bottom (relative to total)

| parameter                               | value |
| :-------------------------------------- | ----: |
| top users effect (relative to total)    | 0.035 |
| bottom users effect (relative to total) | 0.015 |
| total relative effect                   |  0.05 |
| sample size                             | 39369 |

| test              |       level | power |       power ci |
| :---------------- | ----------: | ----: | -------------: |
| Mann–Whitney U    |       users | 0.972 | [0.968, 0.975] |
| Student's t-test  |       users | 0.801 | [0.793, 0.809] |
| Z-test (unpooled) |       users | 0.801 | [0.793, 0.809] |
| Welch's t-test    |       users | 0.801 | [0.793, 0.809] |
| Z-test (unpooled) | 100 buckets | 0.801 | [0.793, 0.809] |
| Z-test (unpooled) |  50 buckets | 0.799 | [0.791, 0.807] |
| Z-test (unpooled) |  20 buckets | 0.799 | [0.791, 0.807] |
| Welch's t-test    | 100 buckets | 0.794 | [0.786, 0.802] |
| Student's t-test  | 100 buckets | 0.794 | [0.786, 0.802] |
| Student's t-test  |  50 buckets | 0.787 | [0.779, 0.795] |
| Welch's t-test    |  50 buckets | 0.787 | [0.779, 0.795] |
| Z-test (unpooled) |  10 buckets | 0.786 | [0.778, 0.794] |
| Mann–Whitney U    | 100 buckets | 0.783 | [0.774, 0.791] |
| Mann–Whitney U    |  50 buckets | 0.763 | [0.755, 0.772] |
| Student's t-test  |  20 buckets | 0.760 | [0.751, 0.768] |
| Welch's t-test    |  20 buckets | 0.757 | [0.749, 0.766] |
| Mann–Whitney U    |  20 buckets | 0.720 | [0.711, 0.729] |
| Student's t-test  |  10 buckets | 0.698 | [0.689, 0.707] |
| Welch's t-test    |  10 buckets | 0.685 | [0.676, 0.695] |
| Mann–Whitney U    |  10 buckets | 0.617 | [0.607, 0.626] |

## A/B +5%: +5% top, 0% bottom (relative to total)

| parameter                               | value |
| :-------------------------------------- | ----: |
| top users effect (relative to total)    |  0.05 |
| bottom users effect (relative to total) |   0.0 |
| total relative effect                   |  0.05 |
| sample size                             | 42245 |

| test              |       level |  power |         power ci |
| :---------------- | ----------: | -----: | ---------------: |
| Student's t-test  |       users |  0.796 |   [0.788, 0.804] |
| Z-test (unpooled) |       users |  0.796 |   [0.788, 0.804] |
| Welch's t-test    |       users |  0.796 |   [0.788, 0.804] |
| Z-test (unpooled) | 100 buckets |  0.794 |   [0.786, 0.802] |
| Z-test (unpooled) |  50 buckets |  0.794 |   [0.786, 0.802] |
| Z-test (unpooled) |  20 buckets |  0.794 |   [0.786, 0.802] |
| Student's t-test  | 100 buckets |  0.788 |   [0.780, 0.796] |
| Welch's t-test    | 100 buckets |  0.788 |   [0.780, 0.796] |
| Z-test (unpooled) |  10 buckets |  0.787 |   [0.779, 0.795] |
| Student's t-test  |  50 buckets |  0.780 |   [0.772, 0.788] |
| Welch's t-test    |  50 buckets |  0.780 |   [0.772, 0.788] |
| Mann–Whitney U    | 100 buckets |  0.764 |   [0.756, 0.772] |
| Student's t-test  |  20 buckets |  0.752 |   [0.743, 0.761] |
| Welch's t-test    |  20 buckets |  0.750 |   [0.741, 0.758] |
| Mann–Whitney U    |  50 buckets |  0.748 |   [0.739, 0.756] |
| Mann–Whitney U    |  20 buckets |  0.712 |   [0.703, 0.721] |
| Student's t-test  |  10 buckets |  0.696 |   [0.687, 0.705] |
| Welch's t-test    |  10 buckets |  0.684 |   [0.674, 0.693] |
| Mann–Whitney U    |  10 buckets |  0.611 |   [0.601, 0.620] |
| Mann–Whitney U    |       users | 0.0165 | [0.0141, 0.0192] |

## A/B +5%: 0% top, +5% bottom (relative to total)

| parameter                               | value |
| :-------------------------------------- | ----: |
| top users effect (relative to total)    |   0.0 |
| bottom users effect (relative to total) |  0.05 |
| total relative effect                   |  0.05 |
| sample size                             | 34073 |

| test              |       level | power |       power ci |
| :---------------- | ----------: | ----: | -------------: |
| Mann–Whitney U    |       users |  1.00 |   [1.00, 1.00] |
| Mann–Whitney U    | 100 buckets | 0.813 | [0.805, 0.820] |
| Student's t-test  |       users | 0.795 | [0.787, 0.803] |
| Z-test (unpooled) |       users | 0.794 | [0.786, 0.802] |
| Welch's t-test    |       users | 0.794 | [0.786, 0.802] |
| Z-test (unpooled) | 100 buckets | 0.793 | [0.785, 0.801] |
| Z-test (unpooled) |  50 buckets | 0.791 | [0.783, 0.799] |
| Z-test (unpooled) |  20 buckets | 0.790 | [0.781, 0.798] |
| Student's t-test  | 100 buckets | 0.786 | [0.778, 0.794] |
| Welch's t-test    | 100 buckets | 0.786 | [0.778, 0.794] |
| Z-test (unpooled) |  10 buckets | 0.783 | [0.775, 0.791] |
| Mann–Whitney U    |  50 buckets | 0.780 | [0.772, 0.788] |
| Student's t-test  |  50 buckets | 0.778 | [0.769, 0.786] |
| Welch's t-test    |  50 buckets | 0.777 | [0.769, 0.785] |
| Student's t-test  |  20 buckets | 0.749 | [0.740, 0.757] |
| Welch's t-test    |  20 buckets | 0.746 | [0.737, 0.754] |
| Mann–Whitney U    |  20 buckets | 0.721 | [0.712, 0.730] |
| Student's t-test  |  10 buckets | 0.698 | [0.689, 0.707] |
| Welch's t-test    |  10 buckets | 0.686 | [0.677, 0.696] |
| Mann–Whitney U    |  10 buckets | 0.610 | [0.600, 0.619] |
