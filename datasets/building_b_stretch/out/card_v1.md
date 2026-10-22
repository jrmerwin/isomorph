# Benchmark card — building_b_stretch (method v9, profile v1, seed 0)

Kind: synthetic · entities: u1, u2, u3, u4 · types: 22 · events/day: 351 · lag edges: [5.852904783818088, 34.25649440844066, 200.5] · dropped for gaps: 0

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 3.688 | 3.688 | None |
| markov-1 | 2.528 | 2.528 | None |
| markov-2 | 2.091 | 2.091 | None |
| markov-3 | 1.950 | 1.950 | None |
| hawkes-like decay features | 1.850 | 1.850 | None |
| logistic markov features | 2.082 | 2.082 | None |
| logistic triviality library | 1.533 | 1.533 | None |
| logistic library | 1.404 | 1.404 | None |
| logistic unselected contexts | 1.387 | 1.387 | None |

Gain over triviality: 0.130 bits · over best baseline (1.850): 0.447 bits · claim: **beats baselines**
Library: 147 fragments (62 used), 503 compositions, chatty share 0.12
Syntax (3.15): 69 chains (0 used), 0 returns

Loop roles (3.16, recorded, not in the prefix):

| rule | resolved | unresolved | roles by tag | dimension check (REACTS dimensionless / RESPONDS dimensioned) | flowsheet check |
| --- | --- | --- | --- | --- | --- |
| timing | 0 | 0 |  | — | — |
| determinism | 0 | 0 |  | — | — |

Admission (section 6): 59.99 days · 430.8 H (test split 107.7 H) · slow periods 60.0 · period_slow 1440.0 · period_fast None → **admitted** (by days)
Recovery: not measured
