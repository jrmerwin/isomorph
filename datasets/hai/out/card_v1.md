# Benchmark card — hai (method v2, profile v1, seed 0)

Kind: real ICS testbed (HAI 21.03) · entities: P1, P2, P3 · types: 168 · events/day: 2238 · lag edges: [4.986630952238645, 24.8664882538245, 124.0] · dropped for gaps: 1234

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 6.859 | 6.837 | 7.39 |
| markov-1 | 5.276 | 5.475 | 0.392 |
| markov-2 | 5.771 | 5.990 | 0.441 |
| markov-3 | 6.188 | 6.423 | 0.462 |
| hawkes-like decay features | 3.876 | 3.905 | 3.153 |
| logistic markov features | 4.937 | 5.118 | 0.518 |
| logistic triviality library | 3.696 | 3.826 | 0.509 |
| logistic library | 3.721 | 3.851 | 0.545 |
| logistic unselected contexts | 3.736 | 3.865 | 0.575 |

Gain over triviality: -0.024 bits · over best baseline (3.905): 0.055 bits · claim: **no gain**
Library: 2096 fragments (431 used), 0 compositions, chatty share 0.25
Recovery: {'recall': 0.4666666666666667, 'precision': 0.023377862595419848, 'n_mechanisms': 15, 'n_found': 7}
