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
| Mann–Whitney U test (100 buckets) |       0.0634 | [0.0587, 0.0684] |
| Mann–Whitney U test (50 buckets)  |       0.0568 | [0.0524, 0.0616] |
| Student's t-test (20 buckets)     |       0.0495 | [0.0454, 0.0540] |
| Welch's t-test (20 buckets)       |       0.0491 | [0.0450, 0.0536] |
| Student's t-test (users)          |       0.0491 | [0.0450, 0.0536] |
| Student's t-test (50 buckets)     |       0.0491 | [0.0450, 0.0536] |
| Welch's t-test (users)            |       0.0490 | [0.0449, 0.0535] |
| Welch's t-test (50 buckets)       |       0.0490 | [0.0449, 0.0535] |
| Mann–Whitney U test (20 buckets)  |       0.0490 | [0.0449, 0.0535] |
| Student's t-test (10 buckets)     |       0.0489 | [0.0448, 0.0534] |
| Welch's t-test (100 buckets)      |       0.0488 | [0.0447, 0.0533] |
| Student's t-test (100 buckets)    |       0.0488 | [0.0447, 0.0533] |
| Welch's t-test (10 buckets)       |       0.0467 | [0.0427, 0.0511] |
| Mann–Whitney U test (10 buckets)  |       0.0461 | [0.0421, 0.0504] |

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
| Mann–Whitney U test (100 buckets) |       0.0570 | [0.0526, 0.0618] |
| Student's t-test (10 buckets)     |       0.0512 | [0.0470, 0.0557] |
| Mann–Whitney U test (50 buckets)  |       0.0506 | [0.0464, 0.0551] |
| Welch's t-test (users)            |       0.0496 | [0.0455, 0.0541] |
| Student's t-test (users)          |       0.0495 | [0.0454, 0.0540] |
| Welch's t-test (100 buckets)      |       0.0492 | [0.0451, 0.0537] |
| Welch's t-test (10 buckets)       |       0.0492 | [0.0451, 0.0537] |
| Student's t-test (50 buckets)     |       0.0492 | [0.0451, 0.0537] |
| Student's t-test (100 buckets)    |       0.0492 | [0.0451, 0.0537] |
| Welch's t-test (50 buckets)       |       0.0489 | [0.0448, 0.0534] |
| Student's t-test (20 buckets)     |       0.0481 | [0.0440, 0.0525] |
| Mann–Whitney U test (20 buckets)  |       0.0475 | [0.0435, 0.0519] |
| Welch's t-test (20 buckets)       |       0.0470 | [0.0430, 0.0514] |
| Mann–Whitney U test (10 buckets)  |       0.0435 | [0.0396, 0.0477] |

## A/B: +5pp top, 0pp bottom, 5% total

| parameter              | value |
| :--------------------- | ----: |
| effect on top users    |   5pp |
| effect on bottom users |   0pp |
| total effect           |   5pp |
| sample size            | 28391 |

| test                              |  power |         power ci |
| :-------------------------------- | -----: | ---------------: |
| Welch's t-test (users)            |  0.806 |   [0.798, 0.814] |
| Student's t-test (users)          |  0.806 |   [0.798, 0.814] |
| Student's t-test (100 buckets)    |  0.802 |   [0.794, 0.810] |
| Welch's t-test (100 buckets)      |  0.802 |   [0.794, 0.810] |
| Student's t-test (50 buckets)     |  0.800 |   [0.792, 0.807] |
| Welch's t-test (50 buckets)       |  0.799 |   [0.791, 0.807] |
| Student's t-test (20 buckets)     |  0.790 |   [0.782, 0.798] |
| Welch's t-test (20 buckets)       |  0.789 |   [0.781, 0.797] |
| Mann–Whitney U test (50 buckets)  |  0.784 |   [0.775, 0.792] |
| Mann–Whitney U test (100 buckets) |  0.781 |   [0.773, 0.790] |
| Mann–Whitney U test (20 buckets)  |  0.765 |   [0.757, 0.774] |
| Student's t-test (10 buckets)     |  0.759 |   [0.751, 0.767] |
| Welch's t-test (10 buckets)       |  0.754 |   [0.746, 0.763] |
| Mann–Whitney U test (10 buckets)  |  0.717 |   [0.708, 0.726] |
| Mann–Whitney U test (users)       | 0.0673 | [0.0625, 0.0724] |

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
| Mann–Whitney U test (100 buckets) | 0.841 | [0.834, 0.848] |
| Mann–Whitney U test (50 buckets)  | 0.812 | [0.804, 0.819] |
| Student's t-test (users)          | 0.805 | [0.797, 0.813] |
| Welch's t-test (users)            | 0.805 | [0.797, 0.812] |
| Welch's t-test (100 buckets)      | 0.801 | [0.793, 0.809] |
| Student's t-test (100 buckets)    | 0.801 | [0.793, 0.809] |
| Student's t-test (50 buckets)     | 0.794 | [0.786, 0.802] |
| Welch's t-test (50 buckets)       | 0.794 | [0.786, 0.802] |
| Student's t-test (20 buckets)     | 0.784 | [0.776, 0.792] |
| Welch's t-test (20 buckets)       | 0.783 | [0.775, 0.791] |
| Mann–Whitney U test (20 buckets)  | 0.773 | [0.765, 0.782] |
| Student's t-test (10 buckets)     | 0.756 | [0.747, 0.764] |
| Welch's t-test (10 buckets)       | 0.751 | [0.742, 0.759] |
| Mann–Whitney U test (10 buckets)  | 0.715 | [0.706, 0.724] |