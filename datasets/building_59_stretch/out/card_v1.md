# Benchmark card — building_59_stretch (method v9, profile v1, seed 0)

Kind: real office building (LBNL Building 59), stretch 2018 · entities: rtu1, rtu2, rtu3, rtu4, zone016, zone017, zone018, zone019, zone021, zone022, zone023, zone024, zone025, zone026, zone027, zone028, zone030, zone032, zone033, zone035, zone036, zone037, zone038, zone039, zone040, zone041, zone042, zone043, zone044, zone045, zone046, zone047, zone048, zone049, zone051, zone052, zone053, zone054, zone055, zone056, zone057, zone058, zone059, zone061, zone062, zone063, zone064, zone065, zone066, zone067, zone068, zone069, zone070, zone071, zone072 · types: 74 · events/day: 548 · lag edges: [26.742406206196815, 143.0312579394468, 765.0] · dropped for gaps: 0

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 5.663 | 5.663 | None |
| markov-1 | 3.668 | 3.668 | None |
| markov-2 | 3.742 | 3.742 | None |
| markov-3 | 4.036 | 4.036 | None |
| hawkes-like decay features | 3.322 | 3.322 | None |
| logistic markov features | 3.288 | 3.288 | None |
| logistic triviality library | 2.705 | 2.705 | None |
| logistic library | 2.705 | 2.705 | None |
| logistic unselected contexts | 2.707 | 2.707 | None |

Gain over triviality: 0.000 bits · over best baseline (3.288): 0.583 bits · claim: **no gain**
Library: 1761 fragments (239 used), 0 compositions, chatty share 0.12
Syntax (3.15): 2366 chains (0 used), 559 returns

Loop roles (3.16, recorded, not in the prefix):

| rule | resolved | unresolved | roles by tag | dimension check (REACTS dimensionless / RESPONDS dimensioned) | flowsheet check |
| --- | --- | --- | --- | --- | --- |
| timing | 382 | 177 | T RESPONDS, fan REACTS, hw_valve REACTS, ma_t RESPONDS, oa_damper REACTS, oa_flow REACTS, oa_t REACTS, plenum_p RESPONDS, ra_t REACTS, rf_spd REACTS, sa_flow RESPONDS, sa_t RESPONDS, sat_sp REACTS, sf_spd RESPONDS | — | 54 of 90 = 0.60 |
| determinism | 431 | 128 | T REACTS, fan RESPONDS, hw_valve REACTS, ma_t REACTS, oa_damper RESPONDS, oa_flow RESPONDS, oa_t REACTS, plenum_p REACTS, ra_t RESPONDS, rf_spd REACTS, sa_flow REACTS, sa_t REACTS, sat_sp RESPONDS, sf_spd REACTS | — | 7 of 120 = 0.06 |

Admission (section 6): 364.98 days · 687.0 H (test split 171.8 H) · slow periods None · period_slow None · period_fast None → **admitted** (by days)
Recovery: {'recall': 0.6363636363636364, 'precision': 0.06643952299829642, 'n_mechanisms': 11, 'n_found': 7}
