# Benchmark card — tennessee_eastman (method v1, profile v1, seed 0)

Kind: simulated plant (Tennessee Eastman) · entities: reactor, separator, stripper · types: 40 · events/day: 2333 · lag edges: [3.0, 9.0, 21.0] · dropped for gaps: 0

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 5.087 | 5.087 | None |
| markov-1 | 4.524 | 4.524 | None |
| markov-2 | 4.606 | 4.606 | None |
| markov-3 | 5.188 | 5.188 | None |
| hawkes-like decay features | 3.978 | 3.978 | None |
| logistic markov features | 4.196 | 4.196 | None |
| logistic triviality library | 3.569 | 3.569 | None |
| logistic library | 3.387 | 3.387 | None |
| logistic unselected contexts | 3.477 | 3.477 | None |

Gain over triviality: 0.183 bits · over best baseline (3.978): 0.592 bits · claim: **beats baselines**
Library: 606 fragments (179 used), 0 compositions, chatty share 0.16
Recovery: {'recall': 0.1, 'precision': 0.036303630363036306, 'n_mechanisms': 10, 'n_found': 1}
