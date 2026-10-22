# Benchmark card — nasa_battery_stretch (method v9, profile v1, seed 0)

Kind: real battery test bed (NASA PCoE), stretch B0025-28 · entities: B0025, B0026, B0027, B0028 · types: 12 · events/day: 409 · lag edges: [5.932104979342898, 35.18986948594481, 208.75] · dropped for gaps: 174

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 3.215 | 3.215 | None |
| markov-1 | 1.671 | 1.671 | None |
| markov-2 | 1.095 | 1.095 | None |
| markov-3 | 1.046 | 1.046 | None |
| hawkes-like decay features | 1.508 | 1.508 | None |
| logistic markov features | 1.145 | 1.145 | None |
| logistic triviality library | 0.916 | 0.916 | None |
| logistic library | 1.042 | 1.042 | None |
| logistic unselected contexts | 0.916 | 0.916 | None |

Gain over triviality: -0.126 bits · over best baseline (1.046): 0.004 bits · claim: **no gain**
Library: 19 fragments (13 used), 20 compositions, chatty share 0.47
Syntax (3.15): 0 chains (0 used), 0 returns

Loop roles (3.16, recorded, not in the prefix):

| rule | resolved | unresolved | roles by tag | dimension check (REACTS dimensionless / RESPONDS dimensioned) | flowsheet check |
| --- | --- | --- | --- | --- | --- |
| timing | 0 | 0 |  | — | — |
| determinism | 0 | 0 |  | — | — |

Admission (section 6): 5.74 days · 39.6 H (test split 9.9 H) · slow periods 28.7 · period_slow 288.67684804924795 · period_fast None → **admitted** (by slow periods)
Recovery: {'recall': 1.0, 'precision': 0.5263157894736842, 'n_mechanisms': 3, 'n_found': 3}
