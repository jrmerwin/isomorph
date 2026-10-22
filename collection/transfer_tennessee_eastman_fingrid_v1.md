# Transfer cells — tennessee_eastman ↔ fingrid (method v9, profile v1, seed 0)

Own libraries: tennessee_eastman 3.033 bits (triviality 3.171); fingrid 1.615 bits (triviality 1.603)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8). Controls: the median of ten derangements and the marginal control (the source's type frequencies through the mapping, v9); **structure** = learned cell net of the larger control; share = structure / the receiver's diagonal structure (its ceiling), where a diagonal exists.

| direction | zero-shot (learned) | zero-shot, derangement | zero-shot, marginal | cell (bit-H) | derangement cell | marginal cell | net (derangement) | structure | share of ceiling | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tennessee_eastman → fingrid | 4.210 | 4.248 | 5.223 | 18.35 | 18.00 | 10.89 | 0.35 | **0.35** (derangement) | — | 16/16 | not measured (no mapping key) |  |
| fingrid → tennessee_eastman | 8.799 | 8.645 | 8.284 | 35.27 | 32.06 | 43.36 | 3.20 | **-8.10** (marginal) | — | 10/40 | not measured (no mapping key) | damage |
