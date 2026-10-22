# Transfer cells — alibaba_2018 ↔ building_59 (method v9, profile v1, seed 0)

Own libraries: alibaba_2018 2.635 bits (triviality 2.481); building_59 2.760 bits (triviality 2.638)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8). Controls: the median of ten derangements and the marginal control (the source's type frequencies through the mapping, v9); **structure** = learned cell net of the larger control; share = structure / the receiver's diagonal structure (its ceiling), where a diagonal exists.

| direction | zero-shot (learned) | zero-shot, derangement | zero-shot, marginal | cell (bit-H) | derangement cell | marginal cell | net (derangement) | structure | share of ceiling | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| alibaba_2018 → building_59 | 8.482 | 9.054 | 8.545 | 117.26 | 112.98 | 112.45 | 4.29 | **4.29** (derangement) | — | 16/89 | not measured (no mapping key) |  |
| building_59 → alibaba_2018 | 5.461 | 7.660 | 5.272 | 2.64 | -1.39 | 0.00 | 4.03 | **2.64** (marginal) | — | 27/27 | not measured (no mapping key) |  |
