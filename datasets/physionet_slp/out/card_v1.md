# Benchmark card — physionet_slp (method v6, profile v1, seed 0)

Kind: real physiological records (MIT-BIH polysomnographic, 18 nights) · entities: slp01a, slp01b, slp02a, slp02b, slp03, slp04, slp14, slp16, slp32, slp37, slp41, slp45, slp48, slp59, slp60, slp61, slp66, slp67x · types: 14 · events/day: 22053 · lag edges: [0.048733627663697154, 0.14249799361776522, 0.41666666650007755] · dropped for gaps: 0

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 4.799 | 4.799 | None |
| markov-1 | 5.475 | 5.475 | None |
| markov-2 | 6.181 | 6.181 | None |
| markov-3 | 6.775 | 6.775 | None |
| hawkes-like decay features | 5.284 | 5.284 | None |
| logistic markov features | 5.362 | 5.362 | None |
| logistic triviality library | 4.813 | 4.813 | None |
| logistic library | 4.931 | 4.931 | None |
| logistic unselected contexts | 4.813 | 4.813 | None |

Gain over triviality: -0.118 bits · over best baseline (4.799): -0.132 bits · claim: **no gain**
Library: 37 fragments (27 used), 42 compositions, chatty share 0.16
Syntax (3.15): 1 chains (0 used), 0 returns
Recovery: {'recall': 0.4, 'precision': 0.21621621621621623, 'n_mechanisms': 5, 'n_found': 2}
