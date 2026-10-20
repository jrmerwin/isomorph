# Benchmark card — nasa_battery (method v5, profile v1, seed 0)

Kind: real battery test bed (NASA PCoE, 4 cells) · entities: B0005, B0006, B0007, B0018 · types: 12 · events/day: 259 · lag edges: [5.806314960941695, 33.71329342565535, 195.75] · dropped for gaps: 11436

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 3.506 | 3.506 | None |
| markov-1 | 2.910 | 2.910 | None |
| markov-2 | 2.745 | 2.745 | None |
| markov-3 | 2.750 | 2.750 | None |
| hawkes-like decay features | 3.024 | 3.024 | None |
| logistic markov features | 2.841 | 2.841 | None |
| logistic triviality library | 2.711 | 2.711 | None |
| logistic library | 2.781 | 2.781 | None |
| logistic unselected contexts | 2.720 | 2.720 | None |

Gain over triviality: -0.071 bits · over best baseline (2.745): -0.036 bits · claim: **no gain**
Library: 12 fragments (9 used), 0 compositions, chatty share 0.25
Recovery: {'recall': 0.6666666666666666, 'precision': 0.5, 'n_mechanisms': 3, 'n_found': 2}
