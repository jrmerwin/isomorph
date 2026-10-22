# Transfer cells — nasa_battery ↔ physionet_slp (method v9, profile v1, seed 0)

Own libraries: nasa_battery 0.838 bits (triviality 0.827); physionet_slp 3.136 bits (triviality 3.328)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8). Controls: the median of ten derangements and the marginal control (the source's type frequencies through the mapping, v9); **structure** = learned cell net of the larger control; share = structure / the receiver's diagonal structure (its ceiling), where a diagonal exists.

| direction | zero-shot (learned) | zero-shot, derangement | zero-shot, marginal | cell (bit-H) | derangement cell | marginal cell | net (derangement) | structure | share of ceiling | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nasa_battery → physionet_slp | 4.425 | 4.427 | 3.899 | 0.00 | 0.00 | 0.00 | 0.00 | **0.00** (marginal) | — | 2/10 | not measured (no mapping key) |  |
| physionet_slp → nasa_battery | 6.764 | 6.795 | 7.704 | -0.27 | -0.29 | -0.32 | 0.03 | **0.03** (derangement) | — | 2/12 | not measured (no mapping key) | short, damage |
