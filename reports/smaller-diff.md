# Comparison of two-sample mean tests

| parameter                             | value |
| :------------------------------------ | ----: |
| number of simulations                 | 10000 |
| alpha                                 |  0.05 |
| reference power                       |   0.8 |
| treatment-to-control allocation ratio |   1.0 |
| top users                             |   0.3 |
| value created by top users            |   0.7 |

## A/A 0%: +2% top, -2% bottom (relative to total)

| parameter                               |  value |
| :-------------------------------------- | -----: |
| top users effect (relative to total)    |   0.02 |
| bottom users effect (relative to total) |  -0.02 |
| total relative effect                   |    0.0 |
| sample size                             | 176949 |

| test              |       level | type I error |  type I error ci |
| :---------------- | ----------: | -----------: | ---------------: |
| Mann–Whitney U    |       users |         1.00 |     [1.00, 1.00] |
| Z-test (unpooled) |  10 buckets |       0.0679 | [0.0631, 0.0731] |
| Z-test (unpooled) |  20 buckets |       0.0597 | [0.0552, 0.0646] |
| Z-test (unpooled) |  50 buckets |       0.0548 | [0.0505, 0.0595] |
| Mann–Whitney U    |  50 buckets |       0.0537 | [0.0494, 0.0583] |
| Z-test (unpooled) | 100 buckets |       0.0527 | [0.0484, 0.0573] |
| Welch's t-test    |  50 buckets |       0.0523 | [0.0481, 0.0569] |
| Student's t-test  |  50 buckets |       0.0523 | [0.0481, 0.0569] |
| Z-test (unpooled) |       users |       0.0518 | [0.0476, 0.0564] |
| Welch's t-test    |       users |       0.0518 | [0.0476, 0.0564] |
| Mann–Whitney U    | 100 buckets |       0.0517 | [0.0475, 0.0563] |
| Welch's t-test    | 100 buckets |       0.0516 | [0.0474, 0.0562] |
| Student's t-test  | 100 buckets |       0.0516 | [0.0474, 0.0562] |
| Student's t-test  |       users |       0.0515 | [0.0473, 0.0561] |
| Student's t-test  |  20 buckets |       0.0515 | [0.0473, 0.0561] |
| Welch's t-test    |  20 buckets |       0.0510 | [0.0468, 0.0555] |
| Mann–Whitney U    |  20 buckets |       0.0510 | [0.0468, 0.0555] |
| Student's t-test  |  10 buckets |       0.0496 | [0.0455, 0.0541] |
| Welch's t-test    |  10 buckets |       0.0484 | [0.0443, 0.0528] |
| Mann–Whitney U    |  10 buckets |       0.0444 | [0.0405, 0.0487] |

## A/A 0%: -2% top, +2% bottom (relative to total)

| parameter                               |  value |
| :-------------------------------------- | -----: |
| top users effect (relative to total)    |  -0.02 |
| bottom users effect (relative to total) |   0.02 |
| total relative effect                   |    0.0 |
| sample size                             | 147074 |

| test              |       level | type I error |  type I error ci |
| :---------------- | ----------: | -----------: | ---------------: |
| Mann–Whitney U    |       users |         1.00 |     [1.00, 1.00] |
| Z-test (unpooled) |  10 buckets |       0.0685 | [0.0637, 0.0737] |
| Z-test (unpooled) |  20 buckets |       0.0624 | [0.0578, 0.0674] |
| Z-test (unpooled) |  50 buckets |       0.0573 | [0.0529, 0.0621] |
| Z-test (unpooled) |       users |       0.0546 | [0.0503, 0.0593] |
| Welch's t-test    |       users |       0.0546 | [0.0503, 0.0593] |
| Student's t-test  |       users |       0.0546 | [0.0503, 0.0593] |
| Student's t-test  |  20 buckets |       0.0544 | [0.0501, 0.0591] |
| Z-test (unpooled) | 100 buckets |       0.0543 | [0.0500, 0.0590] |
| Welch's t-test    |  50 buckets |       0.0543 | [0.0500, 0.0590] |
| Student's t-test  |  50 buckets |       0.0543 | [0.0500, 0.0590] |
| Welch's t-test    |  20 buckets |       0.0540 | [0.0497, 0.0587] |
| Mann–Whitney U    | 100 buckets |       0.0535 | [0.0492, 0.0581] |
| Mann–Whitney U    |  50 buckets |       0.0533 | [0.0490, 0.0579] |
| Student's t-test  | 100 buckets |       0.0532 | [0.0489, 0.0578] |
| Welch's t-test    | 100 buckets |       0.0531 | [0.0488, 0.0577] |
| Student's t-test  |  10 buckets |       0.0528 | [0.0485, 0.0574] |
| Mann–Whitney U    |  20 buckets |       0.0528 | [0.0485, 0.0574] |
| Welch's t-test    |  10 buckets |       0.0513 | [0.0471, 0.0559] |
| Mann–Whitney U    |  10 buckets |       0.0452 | [0.0413, 0.0495] |

## A/B +2%: +1.4% top, +0.6% bottom (relative to total)

| parameter                               |  value |
| :-------------------------------------- | -----: |
| top users effect (relative to total)    |  0.014 |
| bottom users effect (relative to total) |  0.006 |
| total relative effect                   |   0.02 |
| sample size                             | 160478 |

| test              |       level | power |       power ci |
| :---------------- | ----------: | ----: | -------------: |
| Mann–Whitney U    |       users | 0.958 | [0.954, 0.962] |
| Z-test (unpooled) |  50 buckets | 0.800 | [0.792, 0.808] |
| Student's t-test  |       users | 0.799 | [0.791, 0.807] |
| Z-test (unpooled) |       users | 0.799 | [0.791, 0.807] |
| Welch's t-test    |       users | 0.799 | [0.791, 0.807] |
| Z-test (unpooled) | 100 buckets | 0.797 | [0.789, 0.805] |
| Z-test (unpooled) |  20 buckets | 0.797 | [0.789, 0.805] |
| Z-test (unpooled) |  10 buckets | 0.795 | [0.787, 0.802] |
| Welch's t-test    | 100 buckets | 0.794 | [0.786, 0.802] |
| Student's t-test  | 100 buckets | 0.794 | [0.786, 0.802] |
| Welch's t-test    |  50 buckets | 0.793 | [0.785, 0.801] |
| Student's t-test  |  50 buckets | 0.793 | [0.785, 0.801] |
| Mann–Whitney U    | 100 buckets | 0.782 | [0.774, 0.790] |
| Student's t-test  |  20 buckets | 0.779 | [0.770, 0.787] |
| Welch's t-test    |  20 buckets | 0.777 | [0.769, 0.785] |
| Mann–Whitney U    |  50 buckets | 0.774 | [0.766, 0.782] |
| Mann–Whitney U    |  20 buckets | 0.755 | [0.747, 0.763] |
| Student's t-test  |  10 buckets | 0.752 | [0.743, 0.760] |
| Welch's t-test    |  10 buckets | 0.746 | [0.738, 0.755] |
| Mann–Whitney U    |  10 buckets | 0.706 | [0.697, 0.715] |

## A/B +2%: +2% top, 0% bottom (relative to total)

| parameter                               |  value |
| :-------------------------------------- | -----: |
| top users effect (relative to total)    |   0.02 |
| bottom users effect (relative to total) |    0.0 |
| total relative effect                   |   0.02 |
| sample size                             | 164966 |

| test              |       level |  power |         power ci |
| :---------------- | ----------: | -----: | ---------------: |
| Z-test (unpooled) |  50 buckets |  0.803 |   [0.795, 0.811] |
| Z-test (unpooled) |       users |  0.802 |   [0.795, 0.810] |
| Welch's t-test    |       users |  0.802 |   [0.795, 0.810] |
| Student's t-test  |       users |  0.802 |   [0.795, 0.810] |
| Z-test (unpooled) | 100 buckets |  0.800 |   [0.792, 0.808] |
| Z-test (unpooled) |  10 buckets |  0.799 |   [0.791, 0.807] |
| Z-test (unpooled) |  20 buckets |  0.799 |   [0.791, 0.807] |
| Welch's t-test    | 100 buckets |  0.797 |   [0.789, 0.805] |
| Student's t-test  | 100 buckets |  0.797 |   [0.789, 0.805] |
| Student's t-test  |  50 buckets |  0.796 |   [0.788, 0.804] |
| Welch's t-test    |  50 buckets |  0.796 |   [0.788, 0.804] |
| Student's t-test  |  20 buckets |  0.780 |   [0.772, 0.788] |
| Mann–Whitney U    |  50 buckets |  0.780 |   [0.771, 0.788] |
| Welch's t-test    |  20 buckets |  0.780 |   [0.771, 0.788] |
| Mann–Whitney U    | 100 buckets |  0.779 |   [0.771, 0.788] |
| Mann–Whitney U    |  20 buckets |  0.761 |   [0.753, 0.770] |
| Student's t-test  |  10 buckets |  0.760 |   [0.752, 0.769] |
| Welch's t-test    |  10 buckets |  0.755 |   [0.747, 0.764] |
| Mann–Whitney U    |  10 buckets |  0.715 |   [0.706, 0.723] |
| Mann–Whitney U    |       users | 0.0593 | [0.0548, 0.0642] |

## A/B +2%: 0% top, +2% bottom (relative to total)

| parameter                               |  value |
| :-------------------------------------- | -----: |
| top users effect (relative to total)    |    0.0 |
| bottom users effect (relative to total) |   0.02 |
| total relative effect                   |   0.02 |
| sample size                             | 150997 |

| test              |       level | power |       power ci |
| :---------------- | ----------: | ----: | -------------: |
| Mann–Whitney U    |       users |  1.00 |   [1.00, 1.00] |
| Student's t-test  |       users | 0.801 | [0.793, 0.809] |
| Z-test (unpooled) |       users | 0.801 | [0.793, 0.809] |
| Welch's t-test    |       users | 0.801 | [0.793, 0.809] |
| Z-test (unpooled) |  50 buckets | 0.800 | [0.792, 0.807] |
| Z-test (unpooled) | 100 buckets | 0.799 | [0.791, 0.807] |
| Z-test (unpooled) |  20 buckets | 0.797 | [0.789, 0.805] |
| Student's t-test  | 100 buckets | 0.796 | [0.788, 0.804] |
| Welch's t-test    | 100 buckets | 0.796 | [0.788, 0.804] |
| Z-test (unpooled) |  10 buckets | 0.795 | [0.787, 0.802] |
| Student's t-test  |  50 buckets | 0.794 | [0.786, 0.801] |
| Welch's t-test    |  50 buckets | 0.793 | [0.785, 0.801] |
| Mann–Whitney U    | 100 buckets | 0.789 | [0.781, 0.797] |
| Student's t-test  |  20 buckets | 0.781 | [0.772, 0.789] |
| Welch's t-test    |  20 buckets | 0.779 | [0.771, 0.787] |
| Mann–Whitney U    |  50 buckets | 0.779 | [0.770, 0.787] |
| Mann–Whitney U    |  20 buckets | 0.761 | [0.752, 0.769] |
| Student's t-test  |  10 buckets | 0.753 | [0.745, 0.762] |
| Welch's t-test    |  10 buckets | 0.748 | [0.739, 0.756] |
| Mann–Whitney U    |  10 buckets | 0.703 | [0.694, 0.712] |
