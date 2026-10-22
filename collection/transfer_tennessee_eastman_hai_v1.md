# Transfer cells — tennessee_eastman ↔ hai (method v9, profile v1, seed 0)

Own libraries: tennessee_eastman 3.033 bits (triviality 3.171); hai 3.714 bits (triviality 3.675)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8). Controls: the median of ten derangements and the marginal control (the source's type frequencies through the mapping, v9); **structure** = learned cell net of the larger control; share = structure / the receiver's diagonal structure (its ceiling), where a diagonal exists.

| direction | zero-shot (learned) | zero-shot, derangement | zero-shot, marginal | cell (bit-H) | derangement cell | marginal cell | net (derangement) | structure | share of ceiling | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tennessee_eastman → hai | 7.631 | 9.005 | 8.078 | 39.92 | 26.19 | 31.18 | 13.73 | **8.74** (marginal) | — | 142/168 | not measured (no mapping key) | short, damage |
| hai → tennessee_eastman | 6.629 | 8.471 | 5.628 | 89.49 | 40.88 | 110.86 | 48.61 | **-21.37** (marginal) | — | 34/40 | not measured (no mapping key) | damage |
