# Benchmark card — hai (method v8, profile v1, seed 0)

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

Loop roles (3.16, recorded, not in the prefix):

| rule | resolved | unresolved | roles by tag | dimension check (REACTS dimensionless / RESPONDS dimensioned) | flowsheet check |
| --- | --- | --- | --- | --- | --- |
| timing | 83 | 35 | B2004 RESPONDS, B2016 REACTS, B3004 REACTS, B4005 RESPONDS, B400B RESPONDS, B4022 RESPONDS, CO_rpm REACTS, FCV01D REACTS, FCV02Z REACTS, FT01Z REACTS, FT02 RESPONDS, HILout RESPONDS, LCP01D RESPONDS, LCV01D RESPONDS, LCV01Z REACTS, LIT01 REACTS, PIT01 RESPONDS, PIT02 REACTS, SIT01 REACTS, SIT02 REACTS, TIT01 REACTS, TIT02 RESPONDS, VXT02 REACTS, VXT03 REACTS, VYT02 REACTS, VYT03 RESPONDS | 0.26666666666666666 / 0.6363636363636364 (n 15 / 11) | 7 of 21 = 0.33 |
| determinism | 73 | 45 | B2004 RESPONDS, B3004 REACTS, B4005 RESPONDS, B400B RESPONDS, B4022 REACTS, CO_rpm REACTS, FCV01D RESPONDS, FCV01Z RESPONDS, FCV02Z RESPONDS, FT01 RESPONDS, FT01Z REACTS, FT02 RESPONDS, FT02Z RESPONDS, HILout RESPONDS, LCP01D RESPONDS, LCV01D REACTS, LCV01Z RESPONDS, LIT01 REACTS, PCV01D RESPONDS, PCV01Z RESPONDS, PIT01 REACTS, PIT02 REACTS, SIT01 REACTS, TIT01 REACTS, TIT02 RESPONDS, VXT02 REACTS, VXT03 RESPONDS, VYT03 RESPONDS | 0.18181818181818182 / 0.47058823529411764 (n 11 / 17) | 5 of 15 = 0.33 |

Admission (section 6): 15.32 days · 178.0 H (test split 44.5 H) · slow periods None · period_slow None · period_fast None → **NOT admitted**
Recovery: {'recall': 0.4666666666666667, 'precision': 0.022170900692840646, 'n_mechanisms': 15, 'n_found': 7}
