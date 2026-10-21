# Benchmark card — tclab (method v7, profile v1, seed 0)

Kind: real lab kit (TCLab, two heaters) · entities: h1, h2 · types: 12 · events/day: 1471 · lag edges: [0.5225057352610519, 3.276146920569055, 20.54166666666666] · dropped for gaps: 16

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 3.069 | 3.069 | None |
| markov-1 | 2.243 | 2.243 | None |
| markov-2 | 1.776 | 1.776 | None |
| markov-3 | 1.714 | 1.714 | None |
| hawkes-like decay features | 2.530 | 2.530 | None |
| logistic markov features | 2.080 | 2.080 | None |
| logistic triviality library | 1.779 | 1.779 | None |
| logistic library | 1.949 | 1.949 | None |
| logistic unselected contexts | 1.956 | 1.956 | None |

Gain over triviality: -0.170 bits · over best baseline (1.714): -0.235 bits · claim: **no gain**
Library: 3 fragments (3 used), 0 compositions, chatty share 1.00
Syntax (3.15): 0 chains (0 used), 0 returns
Loop roles (3.16): 0 resolved / 0 unresolved returns · roles {} · dimension check None · flowsheet check None
Admission (section 6): 0.32 days · 22.4 H (test split 5.6 H) · slow periods None · period_slow None · period_fast None → **NOT admitted**
Recovery: {'recall': 0.0, 'precision': 0.0, 'n_mechanisms': 3, 'n_found': 0}
