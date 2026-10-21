# Transfer cells — nasa_battery ↔ physionet_slp (method v8, profile v1, seed 0)

Own libraries: nasa_battery 0.838 bits (triviality 0.827); physionet_slp 3.136 bits (triviality 3.328)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8); the control is the median of ten derangements, moved share at widths (clock, dimension) / clock / all.

| direction | zero-shot (all) | zero-shot (shared) | zero-shot, derangement | cell (bit-H) | control cell | net cell | types moved by width | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nasa_battery → physionet_slp | 4.425 | 3.795 | 4.427 | 0.00 | 0.00 | **0.00** | 1.00 / 1.00 / 1.00 | 2/10 | not measured (no mapping key) |  |
| physionet_slp → nasa_battery | 6.762 | 1.619 | 6.789 | -0.27 | -0.29 | **0.02** | 1.00 / 1.00 / 1.00 | 2/12 | not measured (no mapping key) | short, damage |
