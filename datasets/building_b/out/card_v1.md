# Benchmark card — building_b (method v1, profile v1, seed 0)

Kind: synthetic · entities: u1, u2, u3, u4 · types: 22 · events/day: 348 · lag edges: [4.0, 18.0, 65.0] · dropped for gaps: 0

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 3.832 | 3.832 | None |
| markov-1 | 2.551 | 2.551 | None |
| markov-2 | 2.149 | 2.149 | None |
| markov-3 | 2.100 | 2.100 | None |
| hawkes-like decay features | 2.115 | 2.115 | None |
| logistic markov features | 2.110 | 2.110 | None |
| logistic triviality library | 2.110 | 2.110 | None |
| logistic library | 1.452 | 1.452 | None |
| logistic unselected contexts | 1.482 | 1.482 | None |

Gain over triviality: 0.657 bits · over best baseline (2.100): 0.648 bits · claim: **beats baselines**
Library: 131 fragments (60 used), 451 compositions, chatty share 0.16
Recovery: not measured
