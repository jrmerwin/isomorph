# Benchmark card — tennessee_eastman (method v8, profile v1, seed 0)

Kind: simulated plant (Tennessee Eastman) · entities: reactor, separator, stripper · types: 40 · events/day: 2333 · lag edges: [10.883762260366268, 39.48542698005769, 143.25] · dropped for gaps: 0

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 5.087 | 5.087 | None |
| markov-1 | 4.524 | 4.524 | None |
| markov-2 | 4.606 | 4.606 | None |
| markov-3 | 5.188 | 5.188 | None |
| hawkes-like decay features | 3.410 | 3.410 | None |
| logistic markov features | 4.196 | 4.196 | None |
| logistic triviality library | 3.171 | 3.171 | None |
| logistic library | 3.033 | 3.033 | None |
| logistic unselected contexts | 3.175 | 3.175 | None |

Gain over triviality: 0.138 bits · over best baseline (3.410): 0.377 bits · claim: **beats baselines**
Library: 567 fragments (186 used), 0 compositions, chatty share 0.11
Syntax (3.15): 525 chains (0 used), 106 returns

Loop roles (3.16, recorded, not in the prefix):

| rule | resolved | unresolved | roles by tag | dimension check (REACTS dimensionless / RESPONDS dimensioned) | flowsheet check |
| --- | --- | --- | --- | --- | --- |
| timing | 87 | 19 | P REACTS, T REACTS, cw_flow RESPONDS, cw_out RESPONDS, feed REACTS, underflow RESPONDS, underflow_valve REACTS | 0.25 / 0.6666666666666666 (n 4 / 3) | 24 of 44 = 0.55 |
| determinism | 59 | 47 | P REACTS, T REACTS, cw_flow RESPONDS, cw_out RESPONDS, feed RESPONDS, underflow_valve RESPONDS | 0.0 / 0.5 (n 2 / 4) | 10 of 28 = 0.36 |

Admission (section 6): 120.0 days · 1206.2 H (test split 301.6 H) · slow periods None · period_slow None · period_fast None → **admitted** (by days)
Recovery: {'recall': 0.2, 'precision': 0.047619047619047616, 'n_mechanisms': 10, 'n_found': 2}
