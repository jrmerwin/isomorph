# Transfer cells — tennessee_eastman ↔ nasa_battery (method v9, profile v1, seed 0)

Own libraries: tennessee_eastman 3.033 bits (triviality 3.171); nasa_battery 0.838 bits (triviality 0.827)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8). Controls: the median of ten derangements and the marginal control (the source's type frequencies through the mapping, v9); **structure** = learned cell net of the larger control; share = structure / the receiver's diagonal structure (its ceiling), where a diagonal exists.

| direction | zero-shot (learned) | zero-shot, derangement | zero-shot, marginal | cell (bit-H) | derangement cell | marginal cell | net (derangement) | structure | share of ceiling | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tennessee_eastman → nasa_battery | 3.677 | 5.418 | 4.258 | 0.15 | -0.35 | -0.26 | 0.50 | **0.41** (marginal) | — | 12/12 | not measured (no mapping key) | short |
| nasa_battery → tennessee_eastman | 8.772 | 9.031 | 8.290 | 26.82 | 18.36 | 33.50 | 8.46 | **-6.68** (marginal) | — | 6/40 | not measured (no mapping key) | damage |
