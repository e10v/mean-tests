# Comparison of two-sample mean tests

| parameter                             | value |
| :------------------------------------ | ----: |
| number of simulations                 | 10000 |
| alpha                                 |  0.05 |
| reference power                       |   0.8 |
| treatment-to-control allocation ratio |  0.25 |
| top users                             |   0.3 |
| value created by top users            |   0.7 |

## A/A 0%: +5% top, -5% bottom (relative to total)

| parameter                               | value |
| :-------------------------------------- | ----: |
| top users effect (relative to total)    |  0.05 |
| bottom users effect (relative to total) | -0.05 |
| total relative effect                   |   0.0 |
| sample size                             | 63411 |

| test              |       level | type I error |  type I error ci |
| :---------------- | ----------: | -----------: | ---------------: |
| Mann–Whitney U    |       users |         1.00 |     [1.00, 1.00] |
| Mann–Whitney U    | 100 buckets |        0.168 |   [0.160, 0.175] |
| Mann–Whitney U    |  50 buckets |       0.0946 |  [0.0890, 0.101] |
| Student's t-test  |       users |       0.0905 | [0.0850, 0.0963] |
| Z-test (unpooled) |  10 buckets |       0.0753 | [0.0702, 0.0807] |
| Mann–Whitney U    |  20 buckets |       0.0708 | [0.0659, 0.0760] |
| Z-test (unpooled) |  20 buckets |       0.0675 | [0.0627, 0.0726] |
| Student's t-test  |  20 buckets |       0.0601 | [0.0556, 0.0650] |
| Z-test (unpooled) |  50 buckets |       0.0595 | [0.0550, 0.0644] |
| Student's t-test  |  10 buckets |       0.0594 | [0.0549, 0.0643] |
| Mann–Whitney U    |  10 buckets |       0.0574 | [0.0530, 0.0622] |
| Z-test (unpooled) | 100 buckets |       0.0568 | [0.0524, 0.0616] |
| Welch's t-test    |  20 buckets |       0.0566 | [0.0522, 0.0614] |
| Student's t-test  |  50 buckets |       0.0562 | [0.0518, 0.0609] |
| Student's t-test  | 100 buckets |       0.0550 | [0.0507, 0.0597] |
| Z-test (unpooled) |       users |       0.0547 | [0.0504, 0.0594] |
| Welch's t-test    |       users |       0.0547 | [0.0504, 0.0594] |
| Welch's t-test    |  50 buckets |       0.0545 | [0.0502, 0.0592] |
| Welch's t-test    | 100 buckets |       0.0543 | [0.0500, 0.0590] |
| Welch's t-test    |  10 buckets |       0.0525 | [0.0482, 0.0571] |

## A/A 0%: -5% top, +5% bottom (relative to total)

| parameter                               | value |
| :-------------------------------------- | ----: |
| top users effect (relative to total)    | -0.05 |
| bottom users effect (relative to total) |  0.05 |
| total relative effect                   |   0.0 |
| sample size                             | 30153 |

| test              |       level | type I error |  type I error ci |
| :---------------- | ----------: | -----------: | ---------------: |
| Mann–Whitney U    |       users |         1.00 |     [1.00, 1.00] |
| Mann–Whitney U    | 100 buckets |       0.0741 | [0.0691, 0.0795] |
| Z-test (unpooled) |  10 buckets |       0.0662 | [0.0614, 0.0713] |
| Mann–Whitney U    |  50 buckets |       0.0574 | [0.0530, 0.0622] |
| Z-test (unpooled) |  20 buckets |       0.0563 | [0.0519, 0.0610] |
| Student's t-test  |  10 buckets |       0.0515 | [0.0473, 0.0561] |
| Z-test (unpooled) |  50 buckets |       0.0500 | [0.0459, 0.0545] |
| Mann–Whitney U    |  20 buckets |       0.0498 | [0.0457, 0.0543] |
| Student's t-test  |  20 buckets |       0.0494 | [0.0453, 0.0539] |
| Welch's t-test    |  10 buckets |       0.0491 | [0.0450, 0.0536] |
| Z-test (unpooled) | 100 buckets |       0.0483 | [0.0442, 0.0527] |
| Welch's t-test    |  20 buckets |       0.0479 | [0.0438, 0.0523] |
| Student's t-test  |  50 buckets |       0.0473 | [0.0433, 0.0517] |
| Student's t-test  | 100 buckets |       0.0473 | [0.0433, 0.0517] |
| Welch's t-test    | 100 buckets |       0.0471 | [0.0431, 0.0515] |
| Z-test (unpooled) |       users |       0.0470 | [0.0430, 0.0514] |
| Welch's t-test    |       users |       0.0470 | [0.0430, 0.0514] |
| Welch's t-test    |  50 buckets |       0.0468 | [0.0428, 0.0512] |
| Mann–Whitney U    |  10 buckets |       0.0457 | [0.0417, 0.0500] |
| Student's t-test  |       users |       0.0233 | [0.0205, 0.0265] |

## A/B +5%: +3.5% top, +1.5% bottom (relative to total)

| parameter                               | value |
| :-------------------------------------- | ----: |
| top users effect (relative to total)    | 0.035 |
| bottom users effect (relative to total) | 0.015 |
| total relative effect                   |  0.05 |
| sample size                             | 42550 |

| test              |       level | power |       power ci |
| :---------------- | ----------: | ----: | -------------: |
| Mann–Whitney U    |       users | 0.963 | [0.959, 0.966] |
| Student's t-test  |       users | 0.813 | [0.805, 0.821] |
| Z-test (unpooled) | 100 buckets | 0.809 | [0.801, 0.817] |
| Z-test (unpooled) |  20 buckets | 0.809 | [0.801, 0.817] |
| Z-test (unpooled) |  50 buckets | 0.809 | [0.801, 0.817] |
| Z-test (unpooled) |       users | 0.809 | [0.801, 0.817] |
| Welch's t-test    |       users | 0.809 | [0.801, 0.816] |
| Student's t-test  | 100 buckets | 0.807 | [0.799, 0.814] |
| Welch's t-test    | 100 buckets | 0.805 | [0.797, 0.813] |
| Student's t-test  |  50 buckets | 0.802 | [0.794, 0.810] |
| Z-test (unpooled) |  10 buckets | 0.800 | [0.793, 0.808] |
| Welch's t-test    |  50 buckets | 0.800 | [0.792, 0.807] |
| Student's t-test  |  20 buckets | 0.792 | [0.783, 0.799] |
| Welch's t-test    |  20 buckets | 0.784 | [0.775, 0.792] |
| Student's t-test  |  10 buckets | 0.758 | [0.750, 0.766] |
| Welch's t-test    |  10 buckets | 0.738 | [0.729, 0.746] |
| Mann–Whitney U    |  20 buckets | 0.723 | [0.714, 0.732] |
| Mann–Whitney U    |  10 buckets | 0.698 | [0.689, 0.707] |
| Mann–Whitney U    |  50 buckets | 0.680 | [0.671, 0.689] |
| Mann–Whitney U    | 100 buckets | 0.581 | [0.571, 0.590] |

## A/B +5%: +5% top, 0% bottom (relative to total)

| parameter                               | value |
| :-------------------------------------- | ----: |
| top users effect (relative to total)    |  0.05 |
| bottom users effect (relative to total) |   0.0 |
| total relative effect                   |  0.05 |
| sample size                             | 47382 |

| test              |       level |  power |         power ci |
| :---------------- | ----------: | -----: | ---------------: |
| Student's t-test  |       users |  0.837 |   [0.830, 0.844] |
| Z-test (unpooled) |       users |  0.815 |   [0.807, 0.822] |
| Welch's t-test    |       users |  0.815 |   [0.807, 0.822] |
| Z-test (unpooled) | 100 buckets |  0.814 |   [0.806, 0.822] |
| Z-test (unpooled) |  50 buckets |  0.812 |   [0.804, 0.819] |
| Student's t-test  | 100 buckets |  0.811 |   [0.803, 0.819] |
| Z-test (unpooled) |  20 buckets |  0.810 |   [0.802, 0.818] |
| Welch's t-test    | 100 buckets |  0.810 |   [0.802, 0.818] |
| Z-test (unpooled) |  10 buckets |  0.806 |   [0.798, 0.814] |
| Student's t-test  |  50 buckets |  0.804 |   [0.796, 0.812] |
| Welch's t-test    |  50 buckets |  0.802 |   [0.794, 0.809] |
| Student's t-test  |  20 buckets |  0.789 |   [0.781, 0.797] |
| Welch's t-test    |  20 buckets |  0.780 |   [0.772, 0.788] |
| Student's t-test  |  10 buckets |  0.766 |   [0.757, 0.774] |
| Welch's t-test    |  10 buckets |  0.742 |   [0.733, 0.751] |
| Mann–Whitney U    |  20 buckets |  0.720 |   [0.711, 0.729] |
| Mann–Whitney U    |  10 buckets |  0.696 |   [0.687, 0.705] |
| Mann–Whitney U    |  50 buckets |  0.673 |   [0.664, 0.682] |
| Mann–Whitney U    | 100 buckets |  0.574 |   [0.564, 0.583] |
| Mann–Whitney U    |       users | 0.0677 | [0.0629, 0.0728] |

## A/B +5%: 0% top, +5% bottom (relative to total)

| parameter                               | value |
| :-------------------------------------- | ----: |
| top users effect (relative to total)    |   0.0 |
| bottom users effect (relative to total) |  0.05 |
| total relative effect                   |  0.05 |
| sample size                             | 33652 |

| test              |       level | power |       power ci |
| :---------------- | ----------: | ----: | -------------: |
| Mann–Whitney U    |       users |  1.00 |   [1.00, 1.00] |
| Z-test (unpooled) |       users | 0.810 | [0.802, 0.818] |
| Welch's t-test    |       users | 0.810 | [0.802, 0.818] |
| Z-test (unpooled) | 100 buckets | 0.810 | [0.802, 0.817] |
| Student's t-test  | 100 buckets | 0.807 | [0.799, 0.815] |
| Welch's t-test    | 100 buckets | 0.806 | [0.798, 0.814] |
| Z-test (unpooled) |  20 buckets | 0.805 | [0.797, 0.813] |
| Z-test (unpooled) |  10 buckets | 0.805 | [0.797, 0.812] |
| Z-test (unpooled) |  50 buckets | 0.804 | [0.797, 0.812] |
| Student's t-test  |  50 buckets | 0.799 | [0.791, 0.807] |
| Welch's t-test    |  50 buckets | 0.797 | [0.789, 0.805] |
| Student's t-test  |  20 buckets | 0.785 | [0.777, 0.793] |
| Welch's t-test    |  20 buckets | 0.779 | [0.771, 0.788] |
| Student's t-test  |       users | 0.763 | [0.755, 0.771] |
| Student's t-test  |  10 buckets | 0.761 | [0.753, 0.770] |
| Welch's t-test    |  10 buckets | 0.745 | [0.736, 0.753] |
| Mann–Whitney U    |  20 buckets | 0.734 | [0.726, 0.743] |
| Mann–Whitney U    |  50 buckets | 0.705 | [0.696, 0.714] |
| Mann–Whitney U    |  10 buckets | 0.703 | [0.693, 0.711] |
| Mann–Whitney U    | 100 buckets | 0.621 | [0.612, 0.631] |
