# Benchmark card — building_a_stretch (method v9, profile v1, seed 0)

Kind: synthetic · entities: A, B, C · types: 20 · events/day: 187 · lag edges: [4.983277467062981, 24.833054313737644, 123.75] · dropped for gaps: 0

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 3.731 | 3.731 | None |
| markov-1 | 2.459 | 2.459 | None |
| markov-2 | 2.144 | 2.144 | None |
| markov-3 | 2.183 | 2.183 | None |
| hawkes-like decay features | 2.048 | 2.048 | None |
| logistic markov features | 2.063 | 2.063 | None |
| logistic triviality library | 1.591 | 1.591 | None |
| logistic library | 1.481 | 1.481 | None |
| logistic unselected contexts | 1.458 | 1.458 | None |

Gain over triviality: 0.110 bits · over best baseline (2.048): 0.567 bits · claim: **beats baselines**
Library: 110 fragments (51 used), 297 compositions, chatty share 0.10
Syntax (3.15): 26 chains (0 used), 7 returns

Loop roles (3.16, recorded, not in the prefix):

| rule | resolved | unresolved | roles by tag | dimension check (REACTS dimensionless / RESPONDS dimensioned) | flowsheet check |
| --- | --- | --- | --- | --- | --- |
| timing | 6 | 1 | CO2 REACTS, RH REACTS, T REACTS, vent RESPONDS, window RESPONDS | — | — |
| determinism | 6 | 1 | CO2 REACTS, RH RESPONDS, vent REACTS, window RESPONDS | — | — |

Admission (section 6): 59.96 days · 697.7 H (test split 174.4 H) · slow periods 60.0 · period_slow 1440.0 · period_fast None → **admitted** (by days)
Recovery: {'recall': 0.8333333333333334, 'precision': 0.12727272727272726, 'n_mechanisms': 12, 'n_found': 10}
