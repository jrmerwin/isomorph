# Transfer cells — nasa_battery ↔ fingrid (method v9, profile v1, seed 0)

Own libraries: nasa_battery 0.838 bits (triviality 0.827); fingrid 1.615 bits (triviality 1.603)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8). Controls: the median of ten derangements and the marginal control (the source's type frequencies through the mapping, v9); **structure** = learned cell net of the larger control; share = structure / the receiver's diagonal structure (its ceiling), where a diagonal exists.

| direction | zero-shot (learned) | zero-shot, derangement | zero-shot, marginal | cell (bit-H) | derangement cell | marginal cell | net (derangement) | structure | share of ceiling | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nasa_battery → fingrid | 7.132 | 7.369 | 6.492 | 11.17 | 9.06 | 12.90 | 2.11 | **-1.73** (marginal) | — | 8/16 | not measured (no mapping key) | damage |
| fingrid → nasa_battery | 6.282 | 6.426 | 5.958 | -0.22 | -0.27 | -0.31 | 0.05 | **0.05** (derangement) | — | 6/12 | not measured (no mapping key) | short, damage |
