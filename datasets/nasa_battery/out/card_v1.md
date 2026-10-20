# Benchmark card — nasa_battery (method v6, profile v1, seed 0)

Kind: real battery test bed (NASA PCoE, 4 cells) · entities: B0005, B0006, B0007, B0018 · types: 12 · events/day: 259 · lag edges: [5.806314960941695, 33.71329342565535, 195.75] · dropped for gaps: 1120

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 3.506 | 3.506 | None |
| markov-1 | 1.841 | 1.841 | None |
| markov-2 | 1.197 | 1.197 | None |
| markov-3 | 1.114 | 1.114 | None |
| hawkes-like decay features | 1.597 | 1.597 | None |
| logistic markov features | 1.087 | 1.087 | None |
| logistic triviality library | 0.827 | 0.827 | None |
| logistic library | 0.838 | 0.838 | None |
| logistic unselected contexts | 0.827 | 0.827 | None |

Gain over triviality: -0.011 bits · over best baseline (1.087): 0.249 bits · claim: **no gain**
Library: 47 fragments (24 used), 74 compositions, chatty share 0.32
Syntax (3.15): 13 chains (13 used), 1 returns
Recovery: {'recall': 1.0, 'precision': 0.44680851063829785, 'n_mechanisms': 3, 'n_found': 3}
