# Benchmark card — building_a (method v1, profile v1, seed 0)

Kind: synthetic · entities: A, B, C · types: 20 · events/day: 194 · lag edges: [5.0, 21.0, 71.64999999999964] · dropped for gaps: 0

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 4.376 | 4.376 | None |
| markov-1 | 3.286 | 3.286 | None |
| markov-2 | 3.185 | 3.185 | None |
| markov-3 | not measured | | |
| hawkes | not measured | | |
| logistic markov features | 2.691 | 2.691 | None |
| logistic triviality library | 2.210 | 2.210 | None |
| logistic library | 2.215 | 2.215 | None |
| logistic unselected contexts | 2.130 | 2.130 | None |

Gain over triviality: -0.005 bits · over best baseline (2.691): 0.476 bits · claim: **no gain**
Library: 105 fragments (45 used), 291 compositions, chatty share 0.08
Recovery: {'recall': 0.8333333333333334, 'precision': 0.13333333333333333, 'n_mechanisms': 12, 'n_found': 10}
