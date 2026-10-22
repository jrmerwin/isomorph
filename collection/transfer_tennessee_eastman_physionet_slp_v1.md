# Transfer cells — tennessee_eastman ↔ physionet_slp (method v9, profile v1, seed 0)

Own libraries: tennessee_eastman 3.033 bits (triviality 3.171); physionet_slp 3.136 bits (triviality 3.328)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8). Controls: the median of ten derangements and the marginal control (the source's type frequencies through the mapping, v9); **structure** = learned cell net of the larger control; share = structure / the receiver's diagonal structure (its ceiling), where a diagonal exists.

| direction | zero-shot (learned) | zero-shot, derangement | zero-shot, marginal | cell (bit-H) | derangement cell | marginal cell | net (derangement) | structure | share of ceiling | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tennessee_eastman → physionet_slp | 5.378 | 5.351 | 5.395 | 0.00 | 0.00 | 0.00 | 0.00 | **0.00** (marginal) | — | 10/10 | not measured (no mapping key) |  |
| physionet_slp → tennessee_eastman | 6.615 | 8.715 | 9.180 | 81.83 | 19.44 | 7.13 | 62.39 | **62.39** (derangement) | — | 4/40 | not measured (no mapping key) | damage |
