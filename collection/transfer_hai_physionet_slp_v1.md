# Transfer cells — hai ↔ physionet_slp (method v9, profile v1, seed 0)

Own libraries: hai 3.714 bits (triviality 3.675); physionet_slp 3.136 bits (triviality 3.328)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8). Controls: the median of ten derangements and the marginal control (the source's type frequencies through the mapping, v9); **structure** = learned cell net of the larger control; share = structure / the receiver's diagonal structure (its ceiling), where a diagonal exists.

| direction | zero-shot (learned) | zero-shot, derangement | zero-shot, marginal | cell (bit-H) | derangement cell | marginal cell | net (derangement) | structure | share of ceiling | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hai → physionet_slp | 6.998 | 6.781 | 3.679 | 0.00 | 0.00 | 0.00 | 0.00 | **0.00** (marginal) | — | 10/10 | not measured (no mapping key) |  |
| physionet_slp → hai | 7.542 | 8.259 | 7.658 | 37.84 | 32.82 | 36.84 | 5.02 | **0.99** (marginal) | — | 4/168 | not measured (no mapping key) | short, damage |
