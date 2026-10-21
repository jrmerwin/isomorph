# Benchmark card — physionet_slp (method v8, profile v1, seed 0)

Kind: real physiological records (MIT-BIH polysomnographic, 18 nights) · entities: slp01a, slp01b, slp02a, slp02b, slp03, slp04, slp14, slp16, slp32, slp37, slp41, slp45, slp48, slp59, slp60, slp61, slp66, slp67x · types: 10 · events/day: 61956 · lag edges: [0.016623148587418504, 0.06631898716214531, 0.26458333299996184] · dropped for gaps: 0

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 3.434 | 3.434 | None |
| markov-1 | 3.718 | 3.718 | None |
| markov-2 | 4.068 | 4.068 | None |
| markov-3 | 4.435 | 4.435 | None |
| hawkes-like decay features | 3.559 | 3.559 | None |
| logistic markov features | 3.373 | 3.373 | None |
| logistic triviality library | 3.328 | 3.328 | None |
| logistic library | 3.136 | 3.136 | None |
| logistic unselected contexts | 3.328 | 3.328 | None |

Gain over triviality: 0.192 bits · over best baseline (3.373): 0.237 bits · claim: **beats baselines**
Library: 22 fragments (17 used), 32 compositions, chatty share 0.18
Syntax (3.15): 3 chains (0 used), 0 returns

Loop roles (3.16, recorded, not in the prefix):

| rule | resolved | unresolved | roles by tag | dimension check (REACTS dimensionless / RESPONDS dimensioned) | flowsheet check |
| --- | --- | --- | --- | --- | --- |
| timing | 0 | 0 |  | — | 0 of 0 |
| determinism | 0 | 0 |  | — | 0 of 0 |

Admission (section 6): 3.57 days · 19419.1 H (test split 4854.8 H) · slow periods None · period_slow None · period_fast None → **admitted** (by horizons)
Recovery: {'recall': 0.4, 'precision': 0.18181818181818182, 'n_mechanisms': 5, 'n_found': 2}
