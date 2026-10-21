# Benchmark card — fingrid (method v8, profile v1, seed 0)

Kind: real power system (Nordic synchronous area, Fingrid) · entities: grid · types: 16 · events/day: 217 · lag edges: [9.321697517861576, 28.96468153816889, 90.0] · dropped for gaps: 0

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 3.783 | 3.783 | None |
| markov-1 | 2.828 | 2.828 | None |
| markov-2 | 2.659 | 2.659 | None |
| markov-3 | 2.626 | 2.626 | None |
| hawkes-like decay features | 2.588 | 2.588 | None |
| logistic markov features | 2.638 | 2.638 | None |
| logistic triviality library | 1.603 | 1.603 | None |
| logistic library | 1.615 | 1.615 | None |
| logistic unselected contexts | 1.603 | 1.603 | None |

Gain over triviality: -0.012 bits · over best baseline (2.588): 0.974 bits · claim: **no gain**
Library: 71 fragments (30 used), 185 compositions, chatty share 0.15
Syntax (3.15): 15 chains (15 used), 3 returns

Loop roles (3.16, recorded, not in the prefix):

| rule | resolved | unresolved | roles by tag | dimension check (REACTS dimensionless / RESPONDS dimensioned) | flowsheet check |
| --- | --- | --- | --- | --- | --- |
| timing | 3 | 0 | afrr_down REACTS, afrr_up RESPONDS, f REACTS | — | 0 of 0 |
| determinism | 2 | 1 | afrr_down REACTS, afrr_up RESPONDS, f REACTS | — | 0 of 0 |

Admission (section 6): 364.98 days · 5839.7 H (test split 1459.9 H) · slow periods None · period_slow None · period_fast 14.97478692077291 → **admitted** (by days)
Recovery: {'recall': 0.8571428571428571, 'precision': 0.28169014084507044, 'n_mechanisms': 7, 'n_found': 6}
