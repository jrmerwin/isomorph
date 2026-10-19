# Benchmark card — building_a (method v1, profile v1, seed 0)

Kind: synthetic · entities: A, B, C · types: 20 · events/day: 194 · lag edges: [5.0, 21.0, 71.64999999999964] · dropped for gaps: 0

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 4.376 | 4.376 | None |
| markov-1 | 3.286 | 3.286 | None |
| markov-2 | 3.185 | 3.185 | None |
| markov-3 | 3.329 | 3.329 | None |
| hawkes-like decay features | 2.737 | 2.737 | None |
| logistic markov features | 2.691 | 2.691 | None |
| logistic triviality library | 2.210 | 2.210 | None |
| logistic library | 2.214 | 2.214 | None |
| logistic unselected contexts | 2.099 | 2.099 | None |

Gain over triviality: -0.004 bits · over best baseline (2.691): 0.478 bits · claim: **no gain**
Library: 90 fragments (39 used), 225 compositions, chatty share 0.09
Recovery: {'recall': 0.75, 'precision': 0.14444444444444443, 'n_mechanisms': 12, 'n_found': 9}
