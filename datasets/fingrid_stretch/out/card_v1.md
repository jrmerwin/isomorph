# Benchmark card — fingrid_stretch (method v9, profile v1, seed 0)

Kind: real power system (Nordic synchronous area, Fingrid), stretch 2025-26 · entities: grid · types: 16 · events/day: 175 · lag edges: [9.321697517861576, 28.96468153816889, 90.0] · dropped for gaps: 0

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 3.652 | 3.652 | None |
| markov-1 | 2.630 | 2.630 | None |
| markov-2 | 2.315 | 2.315 | None |
| markov-3 | 2.125 | 2.125 | None |
| hawkes-like decay features | 2.508 | 2.508 | None |
| logistic markov features | 2.310 | 2.310 | None |
| logistic triviality library | 1.550 | 1.550 | None |
| logistic library | 1.547 | 1.547 | None |
| logistic unselected contexts | 1.551 | 1.551 | None |

Gain over triviality: 0.003 bits · over best baseline (2.125): 0.578 bits · claim: **no gain**
Library: 54 fragments (33 used), 106 compositions, chatty share 0.19
Syntax (3.15): 7 chains (7 used), 1 returns

Loop roles (3.16, recorded, not in the prefix):

| rule | resolved | unresolved | roles by tag | dimension check (REACTS dimensionless / RESPONDS dimensioned) | flowsheet check |
| --- | --- | --- | --- | --- | --- |
| timing | 1 | 0 | afrr_down REACTS, afrr_up RESPONDS | — | 0 of 0 |
| determinism | 1 | 0 | afrr_down REACTS, afrr_up RESPONDS | — | 0 of 0 |

Admission (section 6): 362.78 days · 5804.5 H (test split 1451.1 H) · slow periods None · period_slow None · period_fast 15.031398071741307 → **admitted** (by days)
Recovery: {'recall': 0.5714285714285714, 'precision': 0.18518518518518517, 'n_mechanisms': 7, 'n_found': 4}
