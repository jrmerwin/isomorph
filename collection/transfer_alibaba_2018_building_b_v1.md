# Transfer cells — alibaba_2018 ↔ building_b (method v9, profile v1, seed 0)

Own libraries: alibaba_2018 2.635 bits (triviality 2.481); building_b 1.341 bits (triviality 1.530)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8). Controls: the median of ten derangements and the marginal control (the source's type frequencies through the mapping, v9); **structure** = learned cell net of the larger control; share = structure / the receiver's diagonal structure (its ceiling), where a diagonal exists.

| direction | zero-shot (learned) | zero-shot, derangement | zero-shot, marginal | cell (bit-H) | derangement cell | marginal cell | net (derangement) | structure | share of ceiling | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| alibaba_2018 → building_b | 7.205 | 10.668 | 4.749 | 12.16 | 7.65 | 12.46 | 4.50 | **-0.30** (marginal) | — | 21/22 | 0.00 | damage |
| building_b → alibaba_2018 | 7.468 | 7.964 | 5.195 | 0.42 | 0.27 | 1.45 | 0.16 | **-1.03** (marginal) | — | 27/27 | not measured (no mapping key) |  |
