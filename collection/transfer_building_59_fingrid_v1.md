# Transfer cells — building_59 ↔ fingrid (method v9, profile v1, seed 0)

Own libraries: building_59 2.760 bits (triviality 2.638); fingrid 1.615 bits (triviality 1.603)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8). Controls: the median of ten derangements and the marginal control (the source's type frequencies through the mapping, v9); **structure** = learned cell net of the larger control; share = structure / the receiver's diagonal structure (its ceiling), where a diagonal exists.

| direction | zero-shot (learned) | zero-shot, derangement | zero-shot, marginal | cell (bit-H) | derangement cell | marginal cell | net (derangement) | structure | share of ceiling | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| building_59 → fingrid | 6.289 | 6.783 | 5.393 | 15.24 | 8.16 | 11.26 | 7.08 | **3.98** (marginal) | — | 10/16 | not measured (no mapping key) | damage |
| fingrid → building_59 | 8.994 | 9.122 | 8.625 | 108.18 | 107.98 | 110.07 | 0.20 | **-1.89** (marginal) | — | 10/89 | not measured (no mapping key) |  |
