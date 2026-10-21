# Transfer cells — tennessee_eastman ↔ physionet_slp (method v8, profile v1, seed 0)

Own libraries: tennessee_eastman 3.033 bits (triviality 3.171); physionet_slp 3.136 bits (triviality 3.328)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8); the control is the median of ten derangements, moved share at widths (clock, dimension) / clock / all.

| direction | zero-shot (all) | zero-shot (shared) | zero-shot, derangement | cell (bit-H) | control cell | net cell | types moved by width | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tennessee_eastman → physionet_slp | 5.382 | 5.382 | 5.355 | 0.00 | 0.00 | **0.00** | 1.00 / 1.00 / 1.00 | 10/10 | not measured (no mapping key) |  |
| physionet_slp → tennessee_eastman | 6.632 | 4.145 | 8.728 | 81.03 | 19.13 | **61.91** | 1.00 / 1.00 / 1.00 | 4/40 | not measured (no mapping key) | damage |
