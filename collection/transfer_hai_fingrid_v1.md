# Transfer cells — hai ↔ fingrid (method v9, profile v1, seed 0)

Own libraries: hai 3.714 bits (triviality 3.675); fingrid 1.615 bits (triviality 1.603)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8). Controls: the median of ten derangements and the marginal control (the source's type frequencies through the mapping, v9); **structure** = learned cell net of the larger control; share = structure / the receiver's diagonal structure (its ceiling), where a diagonal exists.

| direction | zero-shot (learned) | zero-shot, derangement | zero-shot, marginal | cell (bit-H) | derangement cell | marginal cell | net (derangement) | structure | share of ceiling | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hai → fingrid | 4.537 | 4.855 | 4.416 | 21.72 | 15.79 | 12.43 | 5.93 | **5.93** (derangement) | — | 16/16 | not measured (no mapping key) |  |
| fingrid → hai | 8.235 | 8.499 | 8.801 | 34.39 | 33.09 | 30.34 | 1.30 | **1.30** (derangement) | — | 10/168 | not measured (no mapping key) | short, damage |
