# Transfer cells — alibaba_2018 ↔ building_a (method v9, profile v1, seed 0)

Own libraries: alibaba_2018 2.635 bits (triviality 2.481); building_a 2.164 bits (triviality 2.169)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8). Controls: the median of ten derangements and the marginal control (the source's type frequencies through the mapping, v9); **structure** = learned cell net of the larger control; share = structure / the receiver's diagonal structure (its ceiling), where a diagonal exists.

| direction | zero-shot (learned) | zero-shot, derangement | zero-shot, marginal | cell (bit-H) | derangement cell | marginal cell | net (derangement) | structure | share of ceiling | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| alibaba_2018 → building_a | 5.627 | 9.226 | 6.046 | 22.68 | 17.19 | 23.78 | 5.49 | **-1.10** (marginal) | — | 8/20 | not measured (no mapping key) |  |
| building_a → alibaba_2018 | 7.427 | 7.034 | 6.336 | -0.18 | 0.04 | -0.04 | -0.22 | **-0.22** (derangement) | — | 21/27 | not measured (no mapping key) | damage |
