# Benchmark card — building_59 (method v8, profile v1, seed 0)

Kind: real office building (LBNL Building 59, 4 RTUs, ~50 zones) · entities: rtu1, rtu2, rtu3, rtu4, zone016, zone017, zone018, zone019, zone021, zone022, zone023, zone024, zone025, zone026, zone027, zone028, zone030, zone032, zone033, zone035, zone036, zone037, zone038, zone039, zone040, zone041, zone042, zone043, zone044, zone045, zone046, zone047, zone048, zone049, zone051, zone052, zone053, zone054, zone055, zone056, zone057, zone058, zone059, zone061, zone062, zone063, zone064, zone065, zone066, zone067, zone068, zone069, zone070, zone071, zone072 · types: 89 · events/day: 757 · lag edges: [27.36851837399214, 149.80715959750904, 820.0] · dropped for gaps: 0

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 5.843 | 5.843 | None |
| markov-1 | 3.614 | 3.614 | None |
| markov-2 | 3.533 | 3.533 | None |
| markov-3 | 3.821 | 3.821 | None |
| hawkes-like decay features | 3.368 | 3.368 | None |
| logistic markov features | 3.235 | 3.235 | None |
| logistic triviality library | 2.638 | 2.638 | None |
| logistic library | 2.760 | 2.760 | None |
| logistic unselected contexts | 2.756 | 2.756 | None |

Gain over triviality: -0.122 bits · over best baseline (3.235): 0.476 bits · claim: **no gain**
Library: 1285 fragments (237 used), 0 compositions, chatty share 0.17
Syntax (3.15): 1044 chains (0 used), 299 returns

Loop roles (3.16, recorded, not in the prefix):

| rule | resolved | unresolved | roles by tag | dimension check (REACTS dimensionless / RESPONDS dimensioned) | flowsheet check |
| --- | --- | --- | --- | --- | --- |
| timing | 214 | 85 | T RESPONDS, fan REACTS, ma_t RESPONDS, oa_damper REACTS, oa_flow REACTS, oa_t REACTS, plenum_p RESPONDS, ra_t RESPONDS, rf_spd REACTS, sa_flow REACTS, sf_spd RESPONDS | 0.5 / 0.8 (n 6 / 5) | 35 of 56 = 0.62 |
| determinism | 204 | 95 | T REACTS, Tsp_c RESPONDS, hw_valve RESPONDS, ma_t RESPONDS, oa_damper REACTS, oa_flow REACTS, plenum_p REACTS, ra_t RESPONDS, rf_spd REACTS, sa_flow RESPONDS, sa_t RESPONDS, sf_spd RESPONDS | 0.4 / 0.7142857142857143 (n 5 / 7) | 30 of 63 = 0.48 |

Admission (section 6): 364.97 days · 640.9 H (test split 160.2 H) · slow periods 384.5 · period_slow 1366.8576394863867 · period_fast None → **admitted** (by days)
Recovery: {'recall': 0.8181818181818182, 'precision': 0.10194552529182879, 'n_mechanisms': 11, 'n_found': 9}
