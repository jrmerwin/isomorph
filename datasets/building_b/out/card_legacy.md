# Benchmark card — building_b (method v1, profile legacy, seed 0)

Kind: synthetic · entities: u1, u2, u3, u4 · types: 22 · events/day: 348 · lag edges: [5.0, 30.0, 90.0] · dropped for gaps: 0

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 3.828 | 3.828 | None |
| markov-1 | 2.639 | 2.639 | None |
| markov-2 | 2.331 | 2.331 | None |
| markov-3 | 2.353 | 2.353 | None |
| hawkes-like decay features | 2.026 | 2.026 | None |
| logistic markov features | 2.220 | 2.220 | None |
| logistic triviality library | 2.220 | 2.220 | None |
| logistic library | 1.638 | 1.638 | None |
| logistic unselected contexts | 1.564 | 1.564 | None |

Gain over triviality: 0.583 bits · over best baseline (2.026): 0.389 bits · claim: **beats baselines**
Library: 96 fragments (43 used), 215 compositions, chatty share 0.26
Recovery: not measured
