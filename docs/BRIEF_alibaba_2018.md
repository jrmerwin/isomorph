# Brief — alibaba_2018 (method v9, a view)

*Lifts are odds ratios on the proposal split (3.6-3.8), confirmed on the confirmation split; absence is informative only above the signal floor (3.5); `no gain` means found but already carried by the trivial alternation model (3.11); loop-rule verdicts are recorded, not promoted (3.16); cells are bit-horizons net of the larger of two controls, with share of the receiver's ceiling where a diagonal exists (3.12).*

## Identity

- kind: real cluster trace (Alibaba 2018, 200 machines) — negative control; standing: negative control (admitted by horizons if so; flagged as a negative control in every view)
- entity: machine (198 units); H = 35.5 min; lag edges [3.29, 10.8, 35.5] min
- periods: slow 121.0, fast —; admission: {'days': 8.0, 'slow_periods': 95.2, 'horizons': 324.4, 'test_horizons': 81.1, 'admitted': True, 'by': 'slow periods'}
- claim: **no gain** — library 2.635 bits, triviality 2.481, best baseline 2.761; gain over triviality -0.154
- events 475385, types 27, signal floor 1045

## Vocabulary

| role | full tag | quantity | scheme | loop tags (timing / determinism) |
| --- | --- | --- | --- | --- |
| cpu | SLOW·LOCAL·RELAY | — | q20_50_80 | RESPONDS / REACTS |
| disk_io | SLOW·LOCAL·RELAY | — | q20_50_80 | REACTS / RESPONDS |
| mem | SLOW·LOCAL·RELAY | — | q20_50_80 | — / — |
| net_in | SLOW·ISOLATED | — | q20_50_80 | — / — |
| net_out | SLOW·ISOLATED | — | q20_50_80 | — / — |

## Couplings (validated fragments)

| prior | lag | target | lift | conf. lift | n | binding | shape | confirmed in | failed in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cpu:upq80 | s | cpu:downq80 | 6.055 | 5.337 | 2012 | True | `SLOW.up.q80 -s-> SLOW.down.q80 [same role]` | — | — |
| mem:downq20 | m | mem:upq20 | 5.171 | 5.84 | 3593 | True | `SLOW.down.q20 -m-> SLOW.up.q20 [same role]` | — | — |
| disk_io:downq20 | m | disk_io:upq20 | 5.034 | 5.244 | 3311 | True | `SLOW.down.q20 -m-> SLOW.up.q20 [same role]` | — | — |
| cpu:upq80 | m | cpu:downq80 | 4.997 | 5.681 | 4192 | True | `SLOW.up.q80 -m-> SLOW.down.q80 [same role]` | — | — |
| disk_io:upq80 | m | disk_io:downq80 | 4.889 | 4.271 | 3129 | True | `SLOW.up.q80 -m-> SLOW.down.q80 [same role]` | — | — |
| cpu:downq20 | s | cpu:upq20 | 4.817 | 3.892 | 2385 | True | `SLOW.down.q20 -s-> SLOW.up.q20 [same role]` | — | — |
| mem:upq80 | m | mem:downq80 | 4.653 | 5.196 | 6348 | True | `SLOW.up.q80 -m-> SLOW.down.q80 [same role]` | — | — |
| mem:downq80 | s | mem:downq50 | 4.478 | 3.669 | 3147 | True | `SLOW.down.q80 -s-> SLOW.down.q50 [same role]` | — | — |
| mem:upq80 | s | mem:downq80 | 4.446 | 4.917 | 1879 | True | `SLOW.up.q80 -s-> SLOW.down.q80 [same role]` | — | — |
| cpu:downq20 | m | cpu:upq20 | 4.426 | 4.197 | 6372 | True | `SLOW.down.q20 -m-> SLOW.up.q20 [same role]` | — | — |
| mem:downq20 | s | mem:upq20 | 4.319 | 5.851 | 1070 | True | `SLOW.down.q20 -s-> SLOW.up.q20 [same role]` | — | — |
| mem:upq20 | m | mem:downq20 | 3.989 | 3.623 | 2928 | True | `SLOW.up.q20 -m-> SLOW.down.q20 [same role]` | — | — |
| cpu:downq80 | m | cpu:upq80 | 3.967 | 4.402 | 2867 | True | `SLOW.down.q80 -m-> SLOW.up.q80 [same role]` | — | — |
| mem:upq50 | s | mem:upq80 | 3.941 | 4.415 | 2368 | True | `SLOW.up.q50 -s-> SLOW.up.q80 [same role]` | — | — |
| mem:downq50 | s | mem:downq20 | 3.621 | 2.554 | 1578 | True | `SLOW.down.q50 -s-> SLOW.down.q20 [same role]` | — | — |
| disk_io:downq50 | s | disk_io:downq20 | 3.439 | 3.362 | 1150 | True | `SLOW.down.q50 -s-> SLOW.down.q20 [same role]` | — | — |
| disk_io:downq20 | s | disk_io:upq20 | 3.22 | 2.997 | 740 | True | `SLOW.down.q20 -s-> SLOW.up.q20 [same role]` | — | — |
| cpu:downq20 | s | disk_io:downq20 | 3.115 | 3.373 | 1064 | True | `SLOW.down.q20 -s-> SLOW.down.q20` | — | — |
| mem:upq50 | m | mem:downq50 | 3.067 | 3.037 | 6014 | True | `SLOW.up.q50 -m-> SLOW.down.q50 [same role]` | — | — |
| cpu:downq80 | s | cpu:upq80 | 3.017 | 3.736 | 1024 | True | `SLOW.down.q80 -s-> SLOW.up.q80 [same role]` | — | — |
| cpu:upq20 | m | cpu:downq20 | 2.98 | 3.874 | 4608 | True | `SLOW.up.q20 -m-> SLOW.down.q20 [same role]` | — | — |
| disk_io:downq80 | m | disk_io:upq80 | 2.895 | 3.118 | 1917 | True | `SLOW.down.q80 -m-> SLOW.up.q80 [same role]` | — | — |
| mem:downq50 | m | mem:upq50 | 2.848 | 3.663 | 4984 | True | `SLOW.down.q50 -m-> SLOW.up.q50 [same role]` | — | — |
| disk_io:downq20 | s | cpu:downq20 | 2.809 | 3.099 | 911 | True | `SLOW.down.q20 -s-> SLOW.down.q20` | — | — |
| cpu:upq50 | s | cpu:downq50 | 2.767 | 2.39 | 3143 | True | `SLOW.up.q50 -s-> SLOW.down.q50 [same role]` | — | — |
| disk_io:downq50 | m | disk_io:upq50 | 2.737 | 2.288 | 2993 | True | `SLOW.down.q50 -m-> SLOW.up.q50 [same role]` | — | — |
| disk_io:upq80 | s | cpu:upq80 | 2.708 | 3.249 | 711 | True | `SLOW.up.q80 -s-> SLOW.up.q80` | — | — |
| cpu:upq50 | m | cpu:downq50 | 2.705 | 2.388 | 7790 | True | `SLOW.up.q50 -m-> SLOW.down.q50 [same role]` | — | — |
| disk_io:upq20 | s | disk_io:upq50 | 2.699 | 2.296 | 1102 | True | `SLOW.up.q20 -s-> SLOW.up.q50 [same role]` | — | — |
| cpu:upq20 | s | cpu:upq50 | 2.674 | 1.594 | 2440 | True | `SLOW.up.q20 -s-> SLOW.up.q50 [same role]` | — | — |
| disk_io:upq20 | m | disk_io:downq20 | 2.671 | 3.138 | 2072 | True | `SLOW.up.q20 -m-> SLOW.down.q20 [same role]` | — | — |
| cpu:downq80 | s | mem:downq20 | 2.644 | 1.797 | 851 | True | `SLOW.down.q80 -s-> SLOW.down.q20` | — | — |
| disk_io:upq20 | s | cpu:upq20 | 2.602 | 3.079 | 1236 | True | `SLOW.up.q20 -s-> SLOW.up.q20` | — | — |
| mem:downq80 | m | mem:upq80 | 2.598 | 3.644 | 3055 | True | `SLOW.down.q80 -m-> SLOW.up.q80 [same role]` | — | — |
| mem:upq20 | s | mem:downq20 | 2.598 | 2.677 | 766 | True | `SLOW.up.q20 -s-> SLOW.down.q20 [same role]` | — | — |
| disk_io:upq50 | m | disk_io:downq50 | 2.55 | 3.232 | 2908 | True | `SLOW.up.q50 -m-> SLOW.down.q50 [same role]` | — | — |
| mem:upq20 | s | mem:upq50 | 2.445 | 2.609 | 1115 | True | `SLOW.up.q20 -s-> SLOW.up.q50 [same role]` | — | — |
| cpu:downq50 | m | cpu:upq50 | 2.421 | 2.466 | 6149 | True | `SLOW.down.q50 -m-> SLOW.up.q50 [same role]` | — | — |
| cpu:upq20 | s | disk_io:upq20 | 2.356 | 2.438 | 1152 | True | `SLOW.up.q20 -s-> SLOW.up.q20` | — | — |
| cpu:downq50 | s | cpu:downq20 | 2.293 | 2.248 | 1766 | True | `SLOW.down.q50 -s-> SLOW.down.q20 [same role]` | — | — |
| disk_io:upq80 | l | disk_io:downq80 | 2.243 | 2.017 | 4161 | True | `SLOW.up.q80 -l-> SLOW.down.q80 [same role]` | — | — |
| disk_io:downq80 | m | disk_io:downq50 | 2.234 | 1.753 | 1940 | True | `SLOW.down.q80 -m-> SLOW.down.q50 [same role]` | — | — |
| cpu:downq80 | m | disk_io:downq80 | 2.23 | 2.054 | 1458 | True | `SLOW.down.q80 -m-> SLOW.down.q80` | — | — |
| cpu:upq80 | s | disk_io:upq80 | 2.188 | 2.348 | 654 | True | `SLOW.up.q80 -s-> SLOW.up.q80` | — | — |
| disk_io:downq50 | m | disk_io:downq20 | 2.147 | 3.053 | 1884 | True | `SLOW.down.q50 -m-> SLOW.down.q20 [same role]` | — | — |
| disk_io:downq20 | m | cpu:upq20 | 2.13 | 2.424 | 1987 | True | `SLOW.down.q20 -m-> SLOW.up.q20` | — | — |
| cpu:downq80 | s | disk_io:downq80 | 2.121 | 2.55 | 651 | True | `SLOW.down.q80 -s-> SLOW.down.q80` | — | — |
| cpu:upq50 | s | cpu:upq80 | 2.109 | 2.3 | 1325 | True | `SLOW.up.q50 -s-> SLOW.up.q80 [same role]` | — | — |
| cpu:upq20 | s | mem:upq80 | 2.1 | 2.575 | 1284 | True | `SLOW.up.q20 -s-> SLOW.up.q80` | — | — |
| cpu:downq50 | s | cpu:upq50 | 2.015 | 2.273 | 2053 | True | `SLOW.down.q50 -s-> SLOW.up.q50 [same role]` | — | — |
| disk_io:upq80 | m | cpu:downq80 | 2.001 | 2.362 | 1418 | True | `SLOW.up.q80 -m-> SLOW.down.q80` | — | — |
| disk_io:upq20 | m | disk_io:upq50 | 1.997 | 2.204 | 1930 | True | `SLOW.up.q20 -m-> SLOW.up.q50 [same role]` | — | — |
| mem:upq50 | s | mem:downq50 | 1.98 | 2.039 | 1444 | True | `SLOW.up.q50 -s-> SLOW.down.q50 [same role]` | — | — |
| cpu:upq80 | s | mem:upq50 | 1.947 | 2.015 | 948 | True | `SLOW.up.q80 -s-> SLOW.up.q50` | — | — |
| mem:downq20 | s | cpu:downq80 | 1.91 | 1.667 | 500 | True | `SLOW.down.q20 -s-> SLOW.down.q80` | — | — |
| mem:downq50 | s | mem:upq50 | 1.906 | 3.132 | 1285 | True | `SLOW.down.q50 -s-> SLOW.up.q50 [same role]` | — | — |
| cpu:upq80 | s | mem:upq80 | 1.892 | 2.93 | 760 | True | `SLOW.up.q80 -s-> SLOW.up.q80` | — | — |
| cpu:upq20 | s | cpu:downq20 | 1.889 | 3.847 | 1303 | True | `SLOW.up.q20 -s-> SLOW.down.q20 [same role]` | — | — |
| cpu:upq80 | l | disk_io:downq80 | 1.871 | 1.646 | 2837 | True | `SLOW.up.q80 -l-> SLOW.down.q80` | — | — |
| disk_io:downq20 | l | disk_io:upq20 | 1.859 | 2.228 | 3602 | True | `SLOW.down.q20 -l-> SLOW.up.q20 [same role]` | — | — |
| cpu:downq80 | s | mem:downq50 | 1.832 | 2.333 | 913 | True | `SLOW.down.q80 -s-> SLOW.down.q50` | — | — |
| disk_io:downq80 | s | cpu:downq80 | 1.819 | 2.444 | 516 | True | `SLOW.down.q80 -s-> SLOW.down.q80` | — | — |
| disk_io:upq80 | s | disk_io:downq80 | 1.815 | 1.601 | 431 | True | `SLOW.up.q80 -s-> SLOW.down.q80 [same role]` | — | — |
| disk_io:upq80 | s | cpu:downq80 | 1.799 | 2.454 | 473 | True | `SLOW.up.q80 -s-> SLOW.down.q80` | — | — |
| cpu:upq50 | s | mem:upq80 | 1.797 | 2.149 | 1366 | True | `SLOW.up.q50 -s-> SLOW.up.q80` | — | — |
| cpu:downq20 | m | disk_io:upq20 | 1.778 | 1.91 | 1805 | True | `SLOW.down.q20 -m-> SLOW.up.q20` | — | — |
| cpu:downq50 | s | disk_io:downq50 | 1.768 | 1.851 | 1178 | True | `SLOW.down.q50 -s-> SLOW.down.q50` | — | — |
| cpu:downq50 | s | mem:downq50 | 1.758 | 1.617 | 1456 | True | `SLOW.down.q50 -s-> SLOW.down.q50` | — | — |
| mem:upq20 | s | cpu:upq80 | 1.737 | 1.864 | 540 | True | `SLOW.up.q20 -s-> SLOW.up.q80` | — | — |
| disk_io:upq80 | m | cpu:upq80 | 1.734 | 2.186 | 1227 | True | `SLOW.up.q80 -m-> SLOW.up.q80` | — | — |
| cpu:downq20 | s | disk_io:downq50 | 1.734 | 1.549 | 739 | True | `SLOW.down.q20 -s-> SLOW.down.q50` | — | — |
| mem:downq50 | s | cpu:downq80 | 1.726 | 1.976 | 794 | True | `SLOW.down.q50 -s-> SLOW.down.q80` | — | — |
| cpu:downq20 | m | disk_io:downq20 | 1.665 | 2.358 | 1654 | True | `SLOW.down.q20 -m-> SLOW.down.q20` | — | — |
| cpu:upq50 | s | disk_io:upq50 | 1.653 | 1.829 | 1225 | True | `SLOW.up.q50 -s-> SLOW.up.q50` | — | — |
| disk_io:upq80 | s | mem:downq80 | 1.644 | 1.927 | 523 | True | `SLOW.up.q80 -s-> SLOW.down.q80` | — | — |
| mem:upq50 | m | mem:downq80 | 1.636 | 1.858 | 2647 | True | `SLOW.up.q50 -m-> SLOW.down.q80 [same role]` | — | — |
| disk_io:upq80 | l | cpu:downq80 | 1.607 | 1.884 | 3300 | True | `SLOW.up.q80 -l-> SLOW.down.q80` | — | — |
| disk_io:downq20 | m | cpu:downq20 | 1.577 | 1.711 | 1464 | True | `SLOW.down.q20 -m-> SLOW.down.q20` | — | — |
| disk_io:downq20 | l | cpu:upq20 | 1.575 | 1.788 | 4328 | True | `SLOW.down.q20 -l-> SLOW.up.q20` | — | — |
| cpu:upq80 | m | disk_io:upq80 | 1.569 | 1.503 | 1184 | True | `SLOW.up.q80 -m-> SLOW.up.q80` | — | — |
| disk_io:downq50 | s | cpu:downq20 | 1.557 | 1.932 | 751 | True | `SLOW.down.q50 -s-> SLOW.down.q20` | — | — |
| cpu:upq80 | m | mem:downq50 | 1.555 | 1.645 | 1913 | True | `SLOW.up.q80 -m-> SLOW.down.q50` | — | — |
| cpu:upq20 | l | disk_io:downq20 | 1.536 | 1.94 | 3146 | True | `SLOW.up.q20 -l-> SLOW.down.q20` | — | — |
| cpu:downq20 | l | disk_io:upq20 | 1.526 | 2.095 | 3251 | True | `SLOW.down.q20 -l-> SLOW.up.q20` | — | — |
| cpu:upq50 | s | mem:upq50 | 1.524 | 1.78 | 1405 | True | `SLOW.up.q50 -s-> SLOW.up.q50` | — | — |
| mem:upq20 | m | cpu:downq80 | 1.509 | 1.674 | 1169 | True | `SLOW.up.q20 -m-> SLOW.down.q80` | — | — |

## Loops (returns; verdicts recorded, not promoted)

| X | l1 | Y | l2 | X′ | n | cond. lift | timing (g1 / g2) | determinism (p1 / p2) | used |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cpu:upq80 | s | disk_io:upq80 | s | cpu:downq80 | 174 | 4.318 | unresolved (2.0 / 2.0) | unresolved (0.097 / 0.113) | True |
| disk_io:upq80 | s | cpu:downq80 | m | disk_io:downq80 | 188 | 2.613 | Y reacts (2.0 / 7.0) | unresolved (0.113 / 0.086) | True |
| cpu:upq80 | m | mem:downq50 | s | cpu:downq80 | 300 | 2.515 | X reacts (6.0 / 1.0) | unresolved (0.111 / 0.091) | True |
| disk_io:upq80 | m | cpu:downq80 | s | disk_io:downq80 | 231 | 2.419 | X reacts (7.0 / 2.0) | unresolved (0.109 / 0.106) | True |
| disk_io:downq20 | s | cpu:downq20 | m | disk_io:upq20 | 282 | 2.365 | Y reacts (2.0 / 7.0) | Y reacts (0.195 / 0.085) | True |
| mem:upq20 | m | cpu:downq80 | s | mem:downq20 | 231 | 2.202 | X reacts (6.0 / 2.0) | unresolved (0.077 / 0.078) | True |
| cpu:upq80 | m | disk_io:upq80 | s | cpu:downq80 | 149 | 2.176 | X reacts (5.0 / 2.0) | X reacts (0.062 / 0.113) | True |
| disk_io:downq20 | m | cpu:upq20 | s | disk_io:upq20 | 360 | 2.04 | X reacts (7.0 / 2.0) | unresolved (0.153 / 0.109) | True |
| cpu:upq80 | s | disk_io:upq80 | m | cpu:downq80 | 220 | 2.03 | Y reacts (2.0 / 6.0) | unresolved (0.097 / 0.109) | True |
| disk_io:upq80 | m | cpu:downq80 | m | disk_io:downq80 | 453 | 1.943 | unresolved (6.0 / 6.0) | unresolved (0.109 / 0.086) | True |
| disk_io:downq20 | m | cpu:downq20 | m | disk_io:upq20 | 357 | 1.924 | unresolved (6.0 / 7.0) | unresolved (0.108 / 0.085) | True |
| cpu:downq20 | s | disk_io:downq20 | m | cpu:upq20 | 440 | 1.913 | Y reacts (2.0 / 7.0) | unresolved (0.147 / 0.153) | True |
| disk_io:upq80 | s | cpu:downq80 | s | disk_io:downq80 | 46 | 1.579 | unresolved (2.0 / 2.0) | unresolved (0.113 / 0.106) | True |

Chains (non-return): 5.

## Absences

- silent roles: none
- roles never a target: ['net_in', 'net_out']
- keyed pairs not found: none
- signal floor: 1045 (absence is informative only for pairs whose support would exceed the signal floor)

## Regimes

none recorded

## Matrix row

Cells in (this system as receiver):

| source | structure | net (derangement) | raw | marginal | derangement | larger control | share of ceiling | types | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tennessee_eastman | 4.56 | 6.63 | 5.41 | 0.85 | -1.23 | marginal | — | 27/27 |  |
| hai | 2.08 | 2.62 | 2.89 | 0.81 | 0.26 | marginal | — | 25/27 | damage |
| nasa_battery | -0.74 | 0.01 | 0.90 | 1.63 | 0.88 | marginal | — | 9/27 | damage |
| physionet_slp | 0.00 | — | 1.25 | 1.25 | 1.25 | marginal | — | 0/27 | uncontrolled |
| building_59 | 2.64 | 4.03 | 2.64 | 0.00 | -1.39 | marginal | — | 27/27 |  |
| fingrid | 1.87 | 1.96 | 1.56 | -0.31 | -0.40 | marginal | — | 6/27 | damage |
| building_a | -0.22 | -0.22 | -0.18 | -0.04 | 0.04 | derangement | — | 21/27 | damage |
| building_b | -1.03 | 0.16 | 0.42 | 1.45 | 0.27 | marginal | — | 27/27 |  |

Cells out (this system as source):

| receiver | structure | net (derangement) | raw | marginal | derangement | larger control | share of ceiling | types | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tennessee_eastman | 51.23 | 80.61 | 124.43 | 73.19 | 43.81 | marginal | 0.29 | 30/40 | damage |
| hai | 4.71 | 6.37 | 36.46 | 31.76 | 30.09 | marginal | — | 30/168 | short, damage |
| nasa_battery | 0.44 | 0.54 | 0.16 | -0.28 | -0.38 | marginal | 0.17 | 10/12 | short, damage |
| physionet_slp | 0.00 | — | 0.00 | 0.00 | 0.00 | marginal | — | 0/10 | uncontrolled |
| building_59 | 4.29 | 4.29 | 117.26 | 112.45 | 112.98 | derangement | 0.04 | 16/89 |  |
| fingrid | -1.50 | -1.50 | 11.27 | 7.10 | 12.77 | derangement | -0.01 | 6/16 | damage |
| building_a | -1.10 | 5.49 | 22.68 | 23.78 | 17.19 | marginal | -0.00 | 8/20 |  |
| building_b | -0.30 | 4.50 | 12.16 | 12.46 | 7.65 | marginal | -0.00 | 21/22 | damage |

Nearest taxa by distance: 
