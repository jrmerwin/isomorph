# Transfer cells — nasa_battery ↔ fingrid (method v8, profile v1, seed 0)

Own libraries: nasa_battery 0.838 bits (triviality 0.827); fingrid 1.615 bits (triviality 1.603)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8); the control is the median of ten derangements, moved share at widths (clock, dimension) / clock / all.

| direction | zero-shot (all) | zero-shot (shared) | zero-shot, derangement | cell (bit-H) | control cell | net cell | types moved by width | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nasa_battery → fingrid | 7.132 | 4.524 | 7.369 | 11.17 | 9.06 | **2.11** | 1.00 / 1.00 / 1.00 | 8/16 | not measured (no mapping key) | damage |
| fingrid → nasa_battery | 6.282 | 3.395 | 6.426 | -0.22 | -0.27 | **0.05** | 1.00 / 1.00 / 1.00 | 6/12 | not measured (no mapping key) | short, damage |
