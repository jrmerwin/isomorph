# Benchmark card — hai (method v6, profile v1, seed 0)

Kind: real ICS testbed (HAI 21.03) · entities: P1, P2, P3 · types: 168 · events/day: 2238 · lag edges: [4.986630952238645, 24.8664882538245, 124.0] · dropped for gaps: 133

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 6.859 | 6.837 | 7.39 |
| markov-1 | 5.251 | 5.449 | 0.393 |
| markov-2 | 5.737 | 5.954 | 0.443 |
| markov-3 | 6.156 | 6.389 | 0.465 |
| hawkes-like decay features | 3.863 | 3.892 | 3.143 |
| logistic markov features | 4.918 | 5.098 | 0.521 |
| logistic triviality library | 3.675 | 3.805 | 0.493 |
| logistic library | 3.714 | 3.844 | 0.521 |
| logistic unselected contexts | 3.720 | 3.849 | 0.549 |

Gain over triviality: -0.039 bits · over best baseline (3.892): 0.048 bits · claim: **no gain**
Library: 2165 fragments (440 used), 0 compositions, chatty share 0.26
Syntax (3.15): 1437 chains (0 used), 118 returns
Recovery: {'recall': 0.4666666666666667, 'precision': 0.022170900692840646, 'n_mechanisms': 15, 'n_found': 7}
