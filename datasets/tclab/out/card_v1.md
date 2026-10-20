# Benchmark card — tclab (method v5, profile v1, seed 0)

Kind: real lab kit (TCLab, two heaters) · entities: h1, h2 · types: 12 · events/day: 1471 · lag edges: [0.5225057352610519, 3.276146920569055, 20.54166666666666] · dropped for gaps: 210

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 3.069 | 3.069 | None |
| markov-1 | 2.909 | 2.909 | None |
| markov-2 | 3.176 | 3.176 | None |
| markov-3 | 3.345 | 3.345 | None |
| hawkes-like decay features | 3.031 | 3.031 | None |
| logistic markov features | 2.775 | 2.775 | None |
| logistic triviality library | 2.855 | 2.855 | None |
| logistic library | 2.747 | 2.747 | None |
| logistic unselected contexts | 2.781 | 2.781 | None |

Gain over triviality: 0.107 bits · over best baseline (2.775): 0.027 bits · claim: **no gain**
Library: 2 fragments (2 used), 0 compositions, chatty share 1.00
Recovery: {'recall': 0.0, 'precision': 0.0, 'n_mechanisms': 3, 'n_found': 0}
