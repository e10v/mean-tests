# Comparison of two-sample mean tests

| parameter                             | value |
| :------------------------------------ | ----: |
| number of simulations                 | 10000 |
| alpha                                 |  0.05 |
| reference power                       |   0.8 |
| treatment-to-control allocation ratio |   1.0 |
| top users                             |   0.2 |
| value created by top users            |   0.8 |

## A/A 0%: +5% top, -5% bottom (relative to total)

| parameter                               |  value |
| :-------------------------------------- | -----: |
| top users effect (relative to total)    |   0.05 |
| bottom users effect (relative to total) |  -0.05 |
| total relative effect                   |    0.0 |
| sample size                             | 329097 |

| test              |       level | type I error |  type I error ci |
| :---------------- | ----------: | -----------: | ---------------: |
| Mann–Whitney U    |       users |         1.00 |     [1.00, 1.00] |
| Mann–Whitney U    | 100 buckets |       0.0930 | [0.0874, 0.0989] |
| Z-test (unpooled) |  10 buckets |       0.0684 | [0.0636, 0.0736] |
| Mann–Whitney U    |  50 buckets |       0.0664 | [0.0616, 0.0715] |
| Z-test (unpooled) |  20 buckets |       0.0602 | [0.0557, 0.0651] |
| Mann–Whitney U    |  20 buckets |       0.0549 | [0.0506, 0.0596] |
| Z-test (unpooled) | 100 buckets |       0.0535 | [0.0492, 0.0581] |
| Student's t-test  |  20 buckets |       0.0529 | [0.0486, 0.0575] |
| Student's t-test  | 100 buckets |       0.0525 | [0.0482, 0.0571] |
| Z-test (unpooled) |  50 buckets |       0.0523 | [0.0481, 0.0569] |
| Welch's t-test    | 100 buckets |       0.0521 | [0.0479, 0.0567] |
| Welch's t-test    |  20 buckets |       0.0519 | [0.0477, 0.0565] |
| Z-test (unpooled) |       users |       0.0509 | [0.0467, 0.0554] |
| Welch's t-test    |       users |       0.0509 | [0.0467, 0.0554] |
| Student's t-test  |       users |       0.0508 | [0.0466, 0.0553] |
| Student's t-test  |  50 buckets |       0.0506 | [0.0464, 0.0551] |
| Student's t-test  |  10 buckets |       0.0506 | [0.0464, 0.0551] |
| Welch's t-test    |  50 buckets |       0.0505 | [0.0463, 0.0550] |
| Welch's t-test    |  10 buckets |       0.0487 | [0.0446, 0.0531] |
| Mann–Whitney U    |  10 buckets |       0.0461 | [0.0421, 0.0504] |

## A/A 0%: -5% top, +5% bottom (relative to total)

| parameter                               |  value |
| :-------------------------------------- | -----: |
| top users effect (relative to total)    |  -0.05 |
| bottom users effect (relative to total) |   0.05 |
| total relative effect                   |    0.0 |
| sample size                             | 162504 |

| test              |       level | type I error |  type I error ci |
| :---------------- | ----------: | -----------: | ---------------: |
| Mann–Whitney U    |       users |         1.00 |     [1.00, 1.00] |
| Mann–Whitney U    | 100 buckets |       0.0796 | [0.0744, 0.0851] |
| Z-test (unpooled) |  10 buckets |       0.0683 | [0.0635, 0.0735] |
| Mann–Whitney U    |  50 buckets |       0.0592 | [0.0547, 0.0640] |
| Z-test (unpooled) |  20 buckets |       0.0579 | [0.0534, 0.0627] |
| Mann–Whitney U    |  20 buckets |       0.0535 | [0.0492, 0.0581] |
| Student's t-test  |  10 buckets |       0.0513 | [0.0471, 0.0559] |
| Z-test (unpooled) |  50 buckets |       0.0511 | [0.0469, 0.0556] |
| Z-test (unpooled) | 100 buckets |       0.0505 | [0.0463, 0.0550] |
| Student's t-test  |  20 buckets |       0.0505 | [0.0463, 0.0550] |
| Welch's t-test    |  10 buckets |       0.0500 | [0.0459, 0.0545] |
| Student's t-test  |       users |       0.0499 | [0.0458, 0.0544] |
| Z-test (unpooled) |       users |       0.0497 | [0.0456, 0.0542] |
| Welch's t-test    |       users |       0.0497 | [0.0456, 0.0542] |
| Welch's t-test    |  20 buckets |       0.0497 | [0.0456, 0.0542] |
| Welch's t-test    | 100 buckets |       0.0495 | [0.0454, 0.0540] |
| Student's t-test  | 100 buckets |       0.0495 | [0.0454, 0.0540] |
| Student's t-test  |  50 buckets |       0.0481 | [0.0440, 0.0525] |
| Welch's t-test    |  50 buckets |       0.0478 | [0.0437, 0.0522] |
| Mann–Whitney U    |  10 buckets |       0.0474 | [0.0434, 0.0518] |

## A/B +5%: +4% top, +1% bottom (relative to total)

| parameter                               |  value |
| :-------------------------------------- | -----: |
| top users effect (relative to total)    |   0.04 |
| bottom users effect (relative to total) |   0.01 |
| total relative effect                   |   0.05 |
| sample size                             | 211250 |

| test              |       level | power |       power ci |
| :---------------- | ----------: | ----: | -------------: |
| Mann–Whitney U    |       users |  1.00 |   [1.00, 1.00] |
| Mann–Whitney U    | 100 buckets | 0.873 | [0.866, 0.879] |
| Mann–Whitney U    |  50 buckets | 0.842 | [0.835, 0.849] |
| Student's t-test  |       users | 0.816 | [0.808, 0.823] |
| Z-test (unpooled) |       users | 0.815 | [0.808, 0.823] |
| Welch's t-test    |       users | 0.815 | [0.808, 0.823] |
| Z-test (unpooled) | 100 buckets | 0.814 | [0.806, 0.821] |
| Z-test (unpooled) |  50 buckets | 0.812 | [0.805, 0.820] |
| Z-test (unpooled) |  10 buckets | 0.812 | [0.804, 0.819] |
| Student's t-test  | 100 buckets | 0.811 | [0.804, 0.819] |
| Z-test (unpooled) |  20 buckets | 0.811 | [0.803, 0.819] |
| Welch's t-test    | 100 buckets | 0.811 | [0.803, 0.819] |
| Student's t-test  |  50 buckets | 0.807 | [0.799, 0.814] |
| Welch's t-test    |  50 buckets | 0.806 | [0.799, 0.814] |
| Mann–Whitney U    |  20 buckets | 0.804 | [0.797, 0.812] |
| Student's t-test  |  20 buckets | 0.792 | [0.784, 0.800] |
| Welch's t-test    |  20 buckets | 0.790 | [0.782, 0.798] |
| Student's t-test  |  10 buckets | 0.773 | [0.764, 0.781] |
| Welch's t-test    |  10 buckets | 0.768 | [0.759, 0.776] |
| Mann–Whitney U    |  10 buckets | 0.743 | [0.734, 0.751] |

## A/B +5%: +5% top, 0% bottom (relative to total)

| parameter                               |  value |
| :-------------------------------------- | -----: |
| top users effect (relative to total)    |   0.05 |
| bottom users effect (relative to total) |    0.0 |
| total relative effect                   |   0.05 |
| sample size                             | 225912 |

| test              |       level | power |       power ci |
| :---------------- | ----------: | ----: | -------------: |
| Mann–Whitney U    | 100 buckets | 0.850 | [0.843, 0.857] |
| Mann–Whitney U    |  50 buckets | 0.831 | [0.823, 0.838] |
| Z-test (unpooled) |       users | 0.816 | [0.808, 0.824] |
| Welch's t-test    |       users | 0.816 | [0.808, 0.824] |
| Student's t-test  |       users | 0.816 | [0.808, 0.824] |
| Z-test (unpooled) | 100 buckets | 0.813 | [0.806, 0.821] |
| Z-test (unpooled) |  50 buckets | 0.813 | [0.805, 0.821] |
| Z-test (unpooled) |  20 buckets | 0.812 | [0.804, 0.820] |
| Student's t-test  | 100 buckets | 0.810 | [0.802, 0.818] |
| Welch's t-test    | 100 buckets | 0.810 | [0.802, 0.818] |
| Z-test (unpooled) |  10 buckets | 0.808 | [0.801, 0.816] |
| Student's t-test  |  50 buckets | 0.807 | [0.800, 0.815] |
| Welch's t-test    |  50 buckets | 0.807 | [0.799, 0.815] |
| Mann–Whitney U    |  20 buckets | 0.799 | [0.791, 0.807] |
| Student's t-test  |  20 buckets | 0.797 | [0.789, 0.805] |
| Welch's t-test    |  20 buckets | 0.796 | [0.788, 0.804] |
| Student's t-test  |  10 buckets | 0.768 | [0.760, 0.776] |
| Welch's t-test    |  10 buckets | 0.762 | [0.753, 0.770] |
| Mann–Whitney U    |  10 buckets | 0.740 | [0.731, 0.748] |
| Mann–Whitney U    |       users | 0.265 | [0.256, 0.274] |

## A/B +5%: 0% top, +5% bottom (relative to total)

| parameter                               |  value |
| :-------------------------------------- | -----: |
| top users effect (relative to total)    |    0.0 |
| bottom users effect (relative to total) |   0.05 |
| total relative effect                   |   0.05 |
| sample size                             | 171025 |

| test              |       level | power |       power ci |
| :---------------- | ----------: | ----: | -------------: |
| Mann–Whitney U    |       users |  1.00 |   [1.00, 1.00] |
| Mann–Whitney U    | 100 buckets | 0.919 | [0.914, 0.925] |
| Mann–Whitney U    |  50 buckets | 0.878 | [0.871, 0.884] |
| Mann–Whitney U    |  20 buckets | 0.810 | [0.802, 0.818] |
| Z-test (unpooled) |  50 buckets | 0.800 | [0.792, 0.807] |
| Z-test (unpooled) |  20 buckets | 0.800 | [0.792, 0.807] |
| Z-test (unpooled) |       users | 0.800 | [0.792, 0.807] |
| Welch's t-test    |       users | 0.800 | [0.792, 0.807] |
| Student's t-test  |       users | 0.799 | [0.791, 0.807] |
| Z-test (unpooled) |  10 buckets | 0.799 | [0.791, 0.807] |
| Z-test (unpooled) | 100 buckets | 0.798 | [0.790, 0.806] |
| Student's t-test  | 100 buckets | 0.796 | [0.788, 0.804] |
| Welch's t-test    | 100 buckets | 0.796 | [0.788, 0.804] |
| Student's t-test  |  50 buckets | 0.793 | [0.785, 0.801] |
| Welch's t-test    |  50 buckets | 0.792 | [0.784, 0.800] |
| Student's t-test  |  20 buckets | 0.782 | [0.774, 0.790] |
| Welch's t-test    |  20 buckets | 0.780 | [0.772, 0.789] |
| Student's t-test  |  10 buckets | 0.761 | [0.752, 0.769] |
| Welch's t-test    |  10 buckets | 0.756 | [0.748, 0.765] |
| Mann–Whitney U    |  10 buckets | 0.740 | [0.731, 0.748] |
