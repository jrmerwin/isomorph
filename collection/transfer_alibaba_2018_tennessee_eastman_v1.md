# Transfer cells — alibaba_2018 ↔ tennessee_eastman (method v9, profile v1, seed 0)

Own libraries: alibaba_2018 2.635 bits (triviality 2.481); tennessee_eastman 3.033 bits (triviality 3.171)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8). Controls: the median of ten derangements and the marginal control (the source's type frequencies through the mapping, v9); **structure** = learned cell net of the larger control; share = structure / the receiver's diagonal structure (its ceiling), where a diagonal exists.

| direction | zero-shot (learned) | zero-shot, derangement | zero-shot, marginal | cell (bit-H) | derangement cell | marginal cell | net (derangement) | structure | share of ceiling | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| alibaba_2018 → tennessee_eastman | 7.756 | 9.566 | 7.213 | 124.43 | 43.81 | 73.19 | 80.61 | **51.23** (marginal) | — | 30/40 | not measured (no mapping key) | damage |
| tennessee_eastman → alibaba_2018 | 5.358 | 7.402 | 6.169 | 5.41 | -1.23 | 0.85 | 6.63 | **4.56** (marginal) | — | 27/27 | not measured (no mapping key) |  |
