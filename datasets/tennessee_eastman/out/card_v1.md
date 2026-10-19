# Benchmark card — tennessee_eastman (method v2, profile v1, seed 0)

Kind: simulated plant (Tennessee Eastman) · entities: reactor, separator, stripper · types: 40 · events/day: 2333 · lag edges: [10.883762260366268, 39.48542698005769, 143.25] · dropped for gaps: 0

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 5.087 | 5.087 | None |
| markov-1 | 4.524 | 4.524 | None |
| markov-2 | 4.606 | 4.606 | None |
| markov-3 | 5.188 | 5.188 | None |
| hawkes-like decay features | 3.410 | 3.410 | None |
| logistic markov features | 4.196 | 4.196 | None |
| logistic triviality library | 3.171 | 3.171 | None |
| logistic library | 3.033 | 3.033 | None |
| logistic unselected contexts | 3.176 | 3.176 | None |

Gain over triviality: 0.138 bits · over best baseline (3.410): 0.377 bits · claim: **beats baselines**
Library: 567 fragments (186 used), 0 compositions, chatty share 0.11
Recovery: {'recall': 0.2, 'precision': 0.047619047619047616, 'n_mechanisms': 10, 'n_found': 2}
