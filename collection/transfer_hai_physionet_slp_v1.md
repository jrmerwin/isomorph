# Transfer cells — hai ↔ physionet_slp (method v8, profile v1, seed 0)

Own libraries: hai 3.714 bits (triviality 3.675); physionet_slp 3.136 bits (triviality 3.328)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8); the control is the median of ten derangements, moved share at widths (clock, dimension) / clock / all.

| direction | zero-shot (all) | zero-shot (shared) | zero-shot, derangement | cell (bit-H) | control cell | net cell | types moved by width | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hai → physionet_slp | 6.998 | 6.998 | 6.781 | 0.00 | 0.00 | **0.00** | 1.00 / 1.00 / 1.00 | 10/10 | not measured (no mapping key) |  |
| physionet_slp → hai | 7.542 | 6.975 | 8.245 | 37.84 | 32.88 | **4.97** | 1.00 / 1.00 / 1.00 | 4/168 | not measured (no mapping key) | short, damage |
