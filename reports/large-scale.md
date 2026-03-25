# Comparison of two-sample mean tests

| parameter                             | value |
| :------------------------------------ | ----: |
| number of simulations                 | 10000 |
| alpha                                 |  0.01 |
| reference power                       |   0.8 |
| treatment-to-control allocation ratio |   1.0 |
| top users                             |   0.2 |
| value created by top users            |   0.8 |

## A/A 0%: +2% top, -2% bottom (relative to total)

| parameter                               |   value |
| :-------------------------------------- | ------: |
| top users effect (relative to total)    |    0.02 |
| bottom users effect (relative to total) |   -0.02 |
| total relative effect                   |     0.0 |
| sample size                             | 2204852 |

| test              |       level | type I error |    type I error ci |
| :---------------- | ----------: | -----------: | -----------------: |
| Mann–Whitney U    |       users |         1.00 |       [1.00, 1.00] |
| Z-test (unpooled) |  10 buckets |       0.0150 |   [0.0128, 0.0176] |
| Z-test (unpooled) |  20 buckets |       0.0135 |   [0.0114, 0.0160] |
| Z-test (unpooled) |  50 buckets |       0.0109 |  [0.00900, 0.0132] |
| Mann–Whitney U    | 100 buckets |       0.0107 |  [0.00882, 0.0130] |
| Mann–Whitney U    |  50 buckets |      0.00980 |  [0.00800, 0.0120] |
| Z-test (unpooled) | 100 buckets |      0.00960 |  [0.00782, 0.0118] |
| Welch's t-test    |  50 buckets |      0.00960 |  [0.00782, 0.0118] |
| Student's t-test  |  50 buckets |      0.00960 |  [0.00782, 0.0118] |
| Student's t-test  |  20 buckets |      0.00960 |  [0.00782, 0.0118] |
| Welch's t-test    | 100 buckets |      0.00940 |  [0.00764, 0.0115] |
| Student's t-test  | 100 buckets |      0.00940 |  [0.00764, 0.0115] |
| Z-test (unpooled) |       users |      0.00930 |  [0.00755, 0.0114] |
| Welch's t-test    |       users |      0.00930 |  [0.00755, 0.0114] |
| Welch's t-test    |  20 buckets |      0.00930 |  [0.00755, 0.0114] |
| Student's t-test  |       users |      0.00930 |  [0.00755, 0.0114] |
| Student's t-test  |  10 buckets |      0.00880 |  [0.00710, 0.0109] |
| Mann–Whitney U    |  20 buckets |      0.00830 |  [0.00666, 0.0103] |
| Welch's t-test    |  10 buckets |      0.00810 |  [0.00648, 0.0101] |
| Mann–Whitney U    |  10 buckets |      0.00600 | [0.00462, 0.00777] |

## A/A 0%: -2% top, +2% bottom (relative to total)

| parameter                               |   value |
| :-------------------------------------- | ------: |
| top users effect (relative to total)    |   -0.02 |
| bottom users effect (relative to total) |    0.02 |
| total relative effect                   |     0.0 |
| sample size                             | 1695235 |

| test              |       level | type I error |    type I error ci |
| :---------------- | ----------: | -----------: | -----------------: |
| Mann–Whitney U    |       users |         1.00 |       [1.00, 1.00] |
| Z-test (unpooled) |  10 buckets |       0.0173 |   [0.0149, 0.0201] |
| Z-test (unpooled) |  20 buckets |       0.0137 |   [0.0116, 0.0162] |
| Z-test (unpooled) |  50 buckets |       0.0112 |  [0.00927, 0.0135] |
| Mann–Whitney U    | 100 buckets |       0.0104 |  [0.00855, 0.0126] |
| Student's t-test  |  20 buckets |       0.0103 |  [0.00846, 0.0125] |
| Welch's t-test    |  20 buckets |       0.0100 |  [0.00818, 0.0122] |
| Z-test (unpooled) |       users |      0.00980 |  [0.00800, 0.0120] |
| Welch's t-test    |       users |      0.00980 |  [0.00800, 0.0120] |
| Student's t-test  |       users |      0.00980 |  [0.00800, 0.0120] |
| Student's t-test  |  10 buckets |      0.00980 |  [0.00800, 0.0120] |
| Z-test (unpooled) | 100 buckets |      0.00970 |  [0.00791, 0.0119] |
| Student's t-test  |  50 buckets |      0.00960 |  [0.00782, 0.0118] |
| Welch's t-test    |  50 buckets |      0.00950 |  [0.00773, 0.0117] |
| Mann–Whitney U    |  50 buckets |      0.00940 |  [0.00764, 0.0115] |
| Student's t-test  | 100 buckets |      0.00900 |  [0.00728, 0.0111] |
| Welch's t-test    | 100 buckets |      0.00890 |  [0.00719, 0.0110] |
| Mann–Whitney U    |  20 buckets |      0.00890 |  [0.00719, 0.0110] |
| Welch's t-test    |  10 buckets |      0.00880 |  [0.00710, 0.0109] |
| Mann–Whitney U    |  10 buckets |      0.00680 | [0.00532, 0.00867] |

## A/B +2%: +1.6% top, +0.4% bottom (relative to total)

| parameter                               |   value |
| :-------------------------------------- | ------: |
| top users effect (relative to total)    |   0.016 |
| bottom users effect (relative to total) |   0.004 |
| total relative effect                   |    0.02 |
| sample size                             | 1906567 |

| test              |       level | power |       power ci |
| :---------------- | ----------: | ----: | -------------: |
| Mann–Whitney U    |       users |  1.00 |   [1.00, 1.00] |
| Mann–Whitney U    | 100 buckets | 0.805 | [0.797, 0.812] |
| Z-test (unpooled) | 100 buckets | 0.794 | [0.786, 0.802] |
| Student's t-test  |       users | 0.793 | [0.785, 0.801] |
| Z-test (unpooled) |       users | 0.793 | [0.785, 0.801] |
| Welch's t-test    |       users | 0.793 | [0.785, 0.801] |
| Z-test (unpooled) |  50 buckets | 0.791 | [0.783, 0.799] |
| Z-test (unpooled) |  20 buckets | 0.789 | [0.781, 0.797] |
| Student's t-test  | 100 buckets | 0.787 | [0.779, 0.795] |
| Welch's t-test    | 100 buckets | 0.787 | [0.779, 0.795] |
| Z-test (unpooled) |  10 buckets | 0.786 | [0.778, 0.794] |
| Student's t-test  |  50 buckets | 0.776 | [0.768, 0.784] |
| Welch's t-test    |  50 buckets | 0.775 | [0.767, 0.783] |
| Mann–Whitney U    |  50 buckets | 0.773 | [0.765, 0.781] |
| Student's t-test  |  20 buckets | 0.753 | [0.745, 0.762] |
| Welch's t-test    |  20 buckets | 0.751 | [0.742, 0.759] |
| Mann–Whitney U    |  20 buckets | 0.723 | [0.714, 0.732] |
| Student's t-test  |  10 buckets | 0.694 | [0.685, 0.703] |
| Welch's t-test    |  10 buckets | 0.684 | [0.675, 0.693] |
| Mann–Whitney U    |  10 buckets | 0.616 | [0.606, 0.625] |

## A/B +2%: +2% top, 0% bottom (relative to total)

| parameter                               |   value |
| :-------------------------------------- | ------: |
| top users effect (relative to total)    |    0.02 |
| bottom users effect (relative to total) |     0.0 |
| total relative effect                   |    0.02 |
| sample size                             | 1956962 |

| test              |       level | power |       power ci |
| :---------------- | ----------: | ----: | -------------: |
| Mann–Whitney U    | 100 buckets | 0.807 | [0.800, 0.815] |
| Z-test (unpooled) |       users | 0.806 | [0.798, 0.814] |
| Welch's t-test    |       users | 0.806 | [0.798, 0.814] |
| Student's t-test  |       users | 0.806 | [0.798, 0.814] |
| Z-test (unpooled) | 100 buckets | 0.804 | [0.796, 0.812] |
| Z-test (unpooled) |  50 buckets | 0.802 | [0.794, 0.809] |
| Z-test (unpooled) |  20 buckets | 0.801 | [0.793, 0.808] |
| Student's t-test  | 100 buckets | 0.797 | [0.789, 0.805] |
| Welch's t-test    | 100 buckets | 0.797 | [0.789, 0.805] |
| Z-test (unpooled) |  10 buckets | 0.796 | [0.788, 0.804] |
| Student's t-test  |  50 buckets | 0.787 | [0.779, 0.795] |
| Welch's t-test    |  50 buckets | 0.786 | [0.778, 0.794] |
| Mann–Whitney U    |  50 buckets | 0.779 | [0.771, 0.787] |
| Student's t-test  |  20 buckets | 0.763 | [0.754, 0.771] |
| Welch's t-test    |  20 buckets | 0.760 | [0.751, 0.768] |
| Mann–Whitney U    |  20 buckets | 0.732 | [0.723, 0.741] |
| Student's t-test  |  10 buckets | 0.705 | [0.696, 0.714] |
| Welch's t-test    |  10 buckets | 0.692 | [0.683, 0.701] |
| Mann–Whitney U    |  10 buckets | 0.628 | [0.618, 0.637] |
| Mann–Whitney U    |       users | 0.170 | [0.163, 0.178] |

## A/B +2%: 0% top, +2% bottom (relative to total)

| parameter                               |   value |
| :-------------------------------------- | ------: |
| top users effect (relative to total)    |     0.0 |
| bottom users effect (relative to total) |    0.02 |
| total relative effect                   |    0.02 |
| sample size                             | 1735207 |

| test              |       level | power |       power ci |
| :---------------- | ----------: | ----: | -------------: |
| Mann–Whitney U    |       users |  1.00 |   [1.00, 1.00] |
| Mann–Whitney U    | 100 buckets | 0.825 | [0.817, 0.832] |
| Z-test (unpooled) |       users | 0.800 | [0.792, 0.807] |
| Welch's t-test    |       users | 0.800 | [0.792, 0.807] |
| Student's t-test  |       users | 0.800 | [0.792, 0.807] |
| Z-test (unpooled) | 100 buckets | 0.797 | [0.789, 0.805] |
| Z-test (unpooled) |  50 buckets | 0.795 | [0.787, 0.803] |
| Z-test (unpooled) |  20 buckets | 0.795 | [0.787, 0.803] |
| Mann–Whitney U    |  50 buckets | 0.795 | [0.787, 0.803] |
| Student's t-test  | 100 buckets | 0.790 | [0.782, 0.798] |
| Z-test (unpooled) |  10 buckets | 0.789 | [0.781, 0.797] |
| Welch's t-test    | 100 buckets | 0.789 | [0.781, 0.797] |
| Student's t-test  |  50 buckets | 0.782 | [0.774, 0.790] |
| Welch's t-test    |  50 buckets | 0.782 | [0.773, 0.790] |
| Student's t-test  |  20 buckets | 0.755 | [0.746, 0.763] |
| Welch's t-test    |  20 buckets | 0.753 | [0.745, 0.762] |
| Mann–Whitney U    |  20 buckets | 0.730 | [0.721, 0.739] |
| Student's t-test  |  10 buckets | 0.706 | [0.697, 0.715] |
| Welch's t-test    |  10 buckets | 0.695 | [0.686, 0.704] |
| Mann–Whitney U    |  10 buckets | 0.622 | [0.613, 0.632] |
