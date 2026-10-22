# Transfer cells — alibaba_2018 ↔ fingrid (method v9, profile v1, seed 0)

Own libraries: alibaba_2018 2.635 bits (triviality 2.481); fingrid 1.615 bits (triviality 1.603)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8). Controls: the median of ten derangements and the marginal control (the source's type frequencies through the mapping, v9); **structure** = learned cell net of the larger control; share = structure / the receiver's diagonal structure (its ceiling), where a diagonal exists.

| direction | zero-shot (learned) | zero-shot, derangement | zero-shot, marginal | cell (bit-H) | derangement cell | marginal cell | net (derangement) | structure | share of ceiling | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| alibaba_2018 → fingrid | 4.051 | 4.099 | 4.981 | 11.27 | 12.77 | 7.10 | -1.50 | **-1.50** (derangement) | — | 6/16 | not measured (no mapping key) | damage |
| fingrid → alibaba_2018 | 5.998 | 6.598 | 6.848 | 1.56 | -0.40 | -0.31 | 1.96 | **1.87** (marginal) | — | 6/27 | not measured (no mapping key) | damage |
