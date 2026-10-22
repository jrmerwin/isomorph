# Transfer cells — hai ↔ nasa_battery (method v9, profile v1, seed 0)

Own libraries: hai 3.714 bits (triviality 3.675); nasa_battery 0.838 bits (triviality 0.827)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8). Controls: the median of ten derangements and the marginal control (the source's type frequencies through the mapping, v9); **structure** = learned cell net of the larger control; share = structure / the receiver's diagonal structure (its ceiling), where a diagonal exists.

| direction | zero-shot (learned) | zero-shot, derangement | zero-shot, marginal | cell (bit-H) | derangement cell | marginal cell | net (derangement) | structure | share of ceiling | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hai → nasa_battery | 4.721 | 4.808 | 3.958 | -0.28 | -0.39 | -0.35 | 0.11 | **0.07** (marginal) | — | 12/12 | not measured (no mapping key) | short |
| nasa_battery → hai | 9.466 | 9.445 | 9.442 | 29.73 | 29.56 | 29.50 | 0.17 | **0.17** (derangement) | — | 10/168 | not measured (no mapping key) | short |
