# Transfer cells — fingrid ↔ fingrid (method v9, profile v1, seed 0)

Own libraries: fingrid 1.547 bits (triviality 1.550); fingrid 1.615 bits (triviality 1.603)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8). Controls: the median of ten derangements and the marginal control (the source's type frequencies through the mapping, v9); **structure** = learned cell net of the larger control; share = structure / the receiver's diagonal structure (its ceiling), where a diagonal exists.

| direction | zero-shot (learned) | zero-shot, derangement | zero-shot, marginal | cell (bit-H) | derangement cell | marginal cell | net (derangement) | structure | share of ceiling | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fingrid_stretch → fingrid (diagonal, identity) | 2.394 | 6.099 | 4.016 | 92.83 | -66.45 | -43.05 | 159.28 | **135.88** (marginal) | — | 16/16 | identity |  |
