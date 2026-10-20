# Benchmark card — building_a (method v6, profile v1, seed 0)

Kind: synthetic · entities: A, B, C · types: 20 · events/day: 194 · lag edges: [5.619954323071132, 31.583886593405914, 177.5] · dropped for gaps: 0

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 4.376 | 4.376 | None |
| markov-1 | 3.286 | 3.286 | None |
| markov-2 | 3.185 | 3.185 | None |
| markov-3 | 3.329 | 3.329 | None |
| hawkes-like decay features | 2.562 | 2.562 | None |
| logistic markov features | 2.691 | 2.691 | None |
| logistic triviality library | 2.169 | 2.169 | None |
| logistic library | 2.164 | 2.164 | None |
| logistic unselected contexts | 2.003 | 2.003 | None |

Gain over triviality: 0.005 bits · over best baseline (2.562): 0.398 bits · claim: **no gain**
Library: 78 fragments (37 used), 187 compositions, chatty share 0.09
Syntax (3.15): 15 chains (15 used), 1 returns
Recovery: {'recall': 0.75, 'precision': 0.15384615384615385, 'n_mechanisms': 12, 'n_found': 9}
