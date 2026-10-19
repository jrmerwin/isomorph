# Benchmark card — building_a_auto (method v1, profile v1, seed 0)

Kind: synthetic · entities: A, B, C · types: 18 · events/day: 569 · lag edges: [3.0, 11.0, 36.0] · dropped for gaps: 0

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 4.060 | 4.060 | None |
| markov-1 | 2.805 | 2.805 | None |
| markov-2 | 2.682 | 2.682 | None |
| markov-3 | not measured | | |
| hawkes | not measured | | |
| logistic markov features | 2.269 | 2.269 | None |
| logistic triviality library | 1.947 | 1.947 | None |
| logistic library | 1.897 | 1.897 | None |
| logistic unselected contexts | 1.859 | 1.859 | None |

Gain over triviality: 0.050 bits · over best baseline (2.269): 0.371 bits · claim: **no gain**
Library: 61 fragments (39 used), 88 compositions, chatty share 0.07
Recovery: not measured
