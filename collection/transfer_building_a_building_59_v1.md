# Transfer cells — building_a ↔ building_59 (method v9, profile v1, seed 0)

Own libraries: building_a 2.164 bits (triviality 2.169); building_59 2.760 bits (triviality 2.638)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8). Controls: the median of ten derangements and the marginal control (the source's type frequencies through the mapping, v9); **structure** = learned cell net of the larger control; share = structure / the receiver's diagonal structure (its ceiling), where a diagonal exists.

| direction | zero-shot (learned) | zero-shot, derangement | zero-shot, marginal | cell (bit-H) | derangement cell | marginal cell | net (derangement) | structure | share of ceiling | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| building_a → building_59 | 8.447 | 8.503 | 8.465 | 118.64 | 117.96 | 119.56 | 0.68 | **-0.93** (marginal) | — | 22/89 | not measured (no mapping key) |  |
| building_59 → building_a | 6.128 | 6.689 | 4.949 | 20.85 | 16.26 | 22.78 | 4.59 | **-1.93** (marginal) | — | 12/20 | not measured (no mapping key) | damage |
