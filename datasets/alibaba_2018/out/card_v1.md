# Benchmark card — alibaba_2018 (method v9, profile v1, seed 0)

Kind: real cluster trace (Alibaba 2018, 200 machines) — negative control · entities: m_100, m_1000, m_1020, m_1060, m_1080, m_1100, m_1120, m_1140, m_1160, m_1180, m_120, m_1200, m_1220, m_1240, m_1260, m_1280, m_1300, m_1320, m_1340, m_1360, m_1380, m_140, m_1400, m_1420, m_1440, m_1460, m_1480, m_1500, m_1520, m_1540, m_1560, m_1580, m_160, m_1600, m_1620, m_1640, m_1660, m_1680, m_1700, m_1720, m_1740, m_1760, m_1780, m_180, m_1800, m_1820, m_1840, m_1860, m_1880, m_1900, m_1920, m_1940, m_1960, m_1980, m_20, m_200, m_2000, m_2020, m_2040, m_2060, m_2080, m_2100, m_2120, m_2140, m_2160, m_2180, m_220, m_2200, m_2220, m_2240, m_2260, m_2280, m_2300, m_2320, m_2340, m_2360, m_2380, m_240, m_2400, m_2420, m_2440, m_2460, m_2480, m_2500, m_2520, m_2540, m_2560, m_2580, m_260, m_2600, m_2620, m_2640, m_2660, m_2680, m_2700, m_2720, m_2740, m_2760, m_2780, m_280, m_2800, m_2820, m_2840, m_2860, m_2880, m_2900, m_2920, m_2940, m_2960, m_2980, m_300, m_3000, m_3020, m_3040, m_3060, m_3080, m_3100, m_3120, m_3140, m_3160, m_3180, m_320, m_3200, m_3220, m_3240, m_3260, m_3280, m_3300, m_3320, m_3340, m_3360, m_3380, m_340, m_3400, m_3420, m_3440, m_3460, m_3480, m_3500, m_3540, m_3560, m_3580, m_360, m_3600, m_3620, m_3640, m_3660, m_3680, m_3700, m_3720, m_3740, m_3760, m_3780, m_380, m_3800, m_3820, m_3840, m_3860, m_3880, m_3900, m_3920, m_3940, m_3960, m_3980, m_40, m_400, m_4000, m_420, m_440, m_460, m_480, m_500, m_520, m_540, m_560, m_580, m_60, m_600, m_620, m_640, m_660, m_680, m_700, m_720, m_740, m_760, m_780, m_80, m_800, m_820, m_840, m_860, m_880, m_900, m_920, m_940, m_960, m_980 · types: 27 · events/day: 59439 · lag edges: [3.2865692257212147, 10.801537275457743, 35.5] · dropped for gaps: 0

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 4.168 | 4.168 | None |
| markov-1 | 3.555 | 3.555 | None |
| markov-2 | 3.028 | 3.028 | None |
| markov-3 | 2.761 | 2.761 | None |
| hawkes-like decay features | 2.963 | 2.963 | None |
| logistic markov features | 2.991 | 2.991 | None |
| logistic triviality library | 2.481 | 2.481 | None |
| logistic library | 2.635 | 2.635 | None |
| logistic unselected contexts | 2.482 | 2.482 | None |

Gain over triviality: -0.154 bits · over best baseline (2.761): 0.126 bits · claim: **no gain**
Library: 86 fragments (40 used), 151 compositions, chatty share 0.21
Syntax (3.15): 18 chains (18 used), 13 returns

Loop roles (3.16, recorded, not in the prefix):

| rule | resolved | unresolved | roles by tag | dimension check (REACTS dimensionless / RESPONDS dimensioned) | flowsheet check |
| --- | --- | --- | --- | --- | --- |
| timing | 9 | 4 | cpu RESPONDS, disk_io REACTS | — | — |
| determinism | 2 | 11 | cpu REACTS, disk_io RESPONDS | — | — |

Admission (section 6): 8.0 days · 324.4 H (test split 81.1 H) · slow periods 95.2 · period_slow 121.0205218111858 · period_fast None → **admitted** (by slow periods)
Recovery: {'recall': 0.0, 'precision': 0.0, 'n_mechanisms': 0, 'n_found': 0}
