# Benchmark card — tennessee_eastman_stretch (method v9, profile v1, seed 0)

Kind: simulated plant (Tennessee Eastman), stretch days 120-240 · entities: reactor, separator, stripper · types: 40 · events/day: 2160 · lag edges: [10.550774483996493, 37.10628073738383, 130.5] · dropped for gaps: 0

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 5.058 | 5.058 | None |
| markov-1 | 4.466 | 4.466 | None |
| markov-2 | 4.479 | 4.479 | None |
| markov-3 | 5.065 | 5.065 | None |
| hawkes-like decay features | 3.418 | 3.418 | None |
| logistic markov features | 4.141 | 4.141 | None |
| logistic triviality library | 3.163 | 3.163 | None |
| logistic library | 3.170 | 3.170 | None |
| logistic unselected contexts | 3.214 | 3.214 | None |

Gain over triviality: -0.007 bits · over best baseline (3.418): 0.249 bits · claim: **no gain**
Library: 285 fragments (161 used), 0 compositions, chatty share 0.09
Syntax (3.15): 140 chains (0 used), 17 returns

Loop roles (3.16, recorded, not in the prefix):

| rule | resolved | unresolved | roles by tag | dimension check (REACTS dimensionless / RESPONDS dimensioned) | flowsheet check |
| --- | --- | --- | --- | --- | --- |
| timing | 15 | 2 | P REACTS, T REACTS, cw_flow REACTS, cw_out RESPONDS, underflow_valve RESPONDS | — | 8 of 13 = 0.62 |
| determinism | 8 | 9 | P REACTS, T RESPONDS, cw_flow RESPONDS, cw_out REACTS, underflow_valve REACTS | — | 3 of 6 = 0.50 |

Admission (section 6): 119.99 days · 1324.1 H (test split 331.0 H) · slow periods 21.0 · period_slow 8236.828949351042 · period_fast None → **admitted** (by days)
Recovery: {'recall': 0.2, 'precision': 0.07017543859649122, 'n_mechanisms': 10, 'n_found': 2}
