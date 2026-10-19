# Benchmark card — building_a (method v1, profile legacy, seed 0)

Kind: synthetic · entities: A, B, C · types: 20 · events/day: 194 · lag edges: [5.0, 30.0, 90.0] · dropped for gaps: 0

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 3.836 | 3.836 | None |
| markov-1 | 2.779 | 2.779 | None |
| markov-2 | 2.601 | 2.601 | None |
| markov-3 | 2.711 | 2.711 | None |
| hawkes-like decay features | 2.221 | 2.221 | None |
| logistic markov features | 2.318 | 2.318 | None |
| logistic triviality library | 1.883 | 1.883 | None |
| logistic library | 1.818 | 1.818 | None |
| logistic unselected contexts | 1.800 | 1.800 | None |

Gain over triviality: 0.064 bits · over best baseline (2.221): 0.402 bits · claim: **no gain**
Library: 68 fragments (39 used), 134 compositions, chatty share 0.13
Recovery: {'recall': 0.8333333333333334, 'precision': 0.17647058823529413, 'n_mechanisms': 12, 'n_found': 10}
