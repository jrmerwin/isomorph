# Brief — building_b (method v8, a view)

*Lifts are odds ratios on the proposal split (3.6-3.8), confirmed on the confirmation split; absence is informative only above the signal floor (3.5); `no gain` means found but already carried by the trivial alternation model (3.11); loop-rule verdicts are recorded, not promoted (3.16); cells are bit-horizons net of the larger of two controls, with share of the receiver's ceiling where a diagonal exists (3.12).*

## Identity

- kind: synthetic; standing: synthetic
- entity: zone (scrambled) (4 units); H = 321.8 min; lag edges [6.85, 46.95, 321.75] min
- periods: slow 1440.0, fast —; admission: {'days': 59.99, 'slow_periods': 60.0, 'horizons': 268.5, 'test_horizons': 67.1, 'admitted': True, 'by': 'days'}
- claim: **beats baselines** — library 1.341 bits, triviality 1.530, best baseline 1.860; gain over triviality 0.189
- events 20878, types 22, signal floor 51

## Vocabulary

| role | full tag | quantity | scheme | loop tags (timing / determinism) |
| --- | --- | --- | --- | --- |
| x00 | — | — | silent | — / — |
| x02 | — | — | silent | — / — |
| x03 | — | — | silent | — / — |
| x04 | — | — | silent | — / — |
| x05 | — | — | silent | — / — |
| x09 | — | — | silent | — / — |
| x11 | — | — | silent | — / — |
| x12 | — | — | silent | — / — |
| x13 | — | — | silent | — / — |
| x14 | — | — | silent | — / — |
| x15 | — | — | silent | — / — |
| x16 | — | — | silent | — / — |
| x17 | — | — | silent | — / — |
| x18 | — | — | silent | — / — |
| x19 | — | — | silent | — / — |
| x20 | — | — | silent | — / — |
| x21 | — | — | silent | — / — |
| x22 | — | — | silent | — / — |
| x23 | — | — | silent | — / — |
| x24 | — | — | silent | — / — |
| x25 | — | — | silent | — / — |
| x26 | — | — | silent | — / — |
| x27 | — | — | silent | — / — |
| x28 | — | — | silent | — / — |
| x29 | — | — | silent | — / — |
| x30 | — | — | silent | — / — |

## Couplings (validated fragments)

| prior | lag | target | lift | conf. lift | n | binding | shape | confirmed in | failed in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| x24 | s | x26 | 44.092 | 33.947 | 112 | True | `None` | — | — |
| x28 | s | x26 | 26.221 | 24.67 | 108 | True | `None` | — | — |
| x25 | m | x13 | 19.868 | 21.088 | 72 | True | `None` | — | — |
| x02 | s | x09 | 18.917 | 15.956 | 176 | True | `None` | — | — |
| x20 | m | x00 | 16.805 | 19.988 | 76 | False | `None` | — | — |
| x27 | s | x05 | 16.015 | 16.493 | 232 | True | `None` | — | — |
| x28 | s | x24 | 15.493 | 14.595 | 123 | True | `None` | — | — |
| x18 | s | x02 | 15.427 | 15.325 | 216 | True | `None` | — | — |
| x23 | m | x30 | 11.17 | 11.656 | 23 | True | `None` | — | — |
| x17 | s | x27 | 11.048 | 10.178 | 273 | True | `None` | — | — |
| x19 | s | x22 | 10.987 | 9.489 | 247 | True | `None` | — | — |
| x17 | s | x05 | 10.984 | 10.772 | 223 | True | `None` | — | — |
| x15 | s | x19 | 9.242 | 7.382 | 140 | True | `None` | — | — |
| x25 | s | x15 | 8.603 | 9.141 | 48 | True | `None` | — | — |
| x18 | s | x09 | 7.767 | 7.784 | 166 | True | `None` | — | — |
| x05 | s | x04 | 6.616 | 8.491 | 16 | True | `None` | — | — |
| x20 | s | x12 | 6.368 | 6.103 | 77 | False | `None` | — | — |
| x26 | s | x05 | 5.738 | 6.786 | 8 | False | `None` | — | — |
| x23 | l | x13 | 5.531 | 4.007 | 55 | True | `None` | — | — |
| x21 | l | x25 | 5.281 | 3.871 | 62 | False | `None` | — | — |
| x21 | l | x13 | 5.111 | 3.871 | 60 | False | `None` | — | — |
| x25 | s | x19 | 4.974 | 9.06 | 21 | True | `None` | — | — |
| x00 | s | x29 | 4.848 | 3.916 | 44 | True | `None` | — | — |
| x23 | l | x25 | 4.727 | 3.339 | 47 | True | `None` | — | — |
| x13 | m | x05 | 4.712 | 3.46 | 58 | True | `None` | — | — |
| x04 | s | x19 | 4.433 | 2.153 | 20 | True | `None` | — | — |
| x13 | m | x27 | 3.871 | 2.842 | 58 | True | `None` | — | — |
| x00 | m | x29 | 3.776 | 2.975 | 308 | True | `None` | — | — |
| x25 | m | x17 | 3.706 | 2.322 | 61 | True | `None` | — | — |
| x11 | s | x19 | 3.587 | 3.519 | 106 | True | `None` | — | — |
| x22 | m | x27 | 3.49 | 3.159 | 387 | True | `None` | — | — |
| x19 | m | x27 | 3.359 | 3.11 | 290 | True | `None` | — | — |
| x27 | s | x04 | 3.289 | 3.369 | 22 | True | `None` | — | — |
| x05 | s | x18 | 3.286 | 2.249 | 21 | True | `None` | — | — |
| x09 | s | x17 | 3.267 | 2.626 | 23 | True | `None` | — | — |
| x03 | m | x19 | 3.151 | 3.436 | 60 | False | `None` | — | — |
| x29 | s | x17 | 3.14 | 3.14 | 82 | True | `None` | — | — |
| x26 | m | x04 | 3.122 | 2.547 | 15 | True | `None` | — | — |
| x12 | m | x14 | 3.022 | 2.637 | 1176 | True | `None` | — | — |
| x13 | m | x17 | 3.006 | 4.325 | 37 | True | `None` | — | — |
| x22 | m | x17 | 2.975 | 2.801 | 271 | True | `None` | — | — |
| x27 | m | x19 | 2.934 | 2.928 | 197 | True | `None` | — | — |
| x22 | m | x05 | 2.931 | 2.445 | 267 | True | `None` | — | — |
| x27 | m | x15 | 2.874 | 2.506 | 255 | True | `None` | — | — |
| x15 | m | x22 | 2.871 | 2.701 | 406 | True | `None` | — | — |
| x26 | l | x02 | 2.831 | 2.538 | 140 | True | `None` | — | — |
| x22 | s | x09 | 2.798 | 3.409 | 36 | True | `None` | — | — |
| x00 | m | x04 | 2.783 | 3.525 | 33 | True | `None` | — | — |
| x18 | m | x09 | 2.766 | 3.017 | 104 | True | `None` | — | — |
| x19 | m | x17 | 2.763 | 2.315 | 196 | True | `None` | — | — |
| x28 | l | x02 | 2.76 | 2.653 | 137 | True | `None` | — | — |
| x25 | l | x11 | 2.74 | 1.977 | 254 | True | `None` | — | — |
| x24 | l | x02 | 2.735 | 2.511 | 238 | True | `None` | — | — |
| x09 | s | x27 | 2.685 | 2.589 | 23 | True | `None` | — | — |
| x11 | s | x15 | 2.663 | 2.97 | 104 | True | `None` | — | — |
| x19 | m | x05 | 2.608 | 2.159 | 185 | True | `None` | — | — |
| x29 | s | x27 | 2.58 | 2.139 | 82 | True | `None` | — | — |
| x13 | l | x11 | 2.565 | 2.38 | 237 | False | `None` | — | — |
| x29 | l | x11 | 2.556 | 2.667 | 954 | False | `None` | — | — |
| x17 | m | x15 | 2.518 | 1.903 | 150 | True | `None` | — | — |
| x05 | m | x19 | 2.511 | 2.15 | 132 | True | `None` | — | — |
| x14 | m | x12 | 2.506 | 2.412 | 1040 | True | `None` | — | — |
| x25 | m | x22 | 2.493 | 2.405 | 66 | True | `None` | — | — |
| x05 | m | x15 | 2.49 | 2.178 | 173 | True | `None` | — | — |
| x03 | s | x14 | 2.468 | 2.496 | 45 | False | `None` | — | — |
| x29 | m | x17 | 2.466 | 2.677 | 117 | False | `None` | — | — |
| x02 | l | x28 | 2.436 | 1.718 | 100 | True | `None` | — | — |
| x02 | l | x26 | 2.412 | 1.684 | 99 | True | `None` | — | — |
| x15 | m | x27 | 2.402 | 2.196 | 257 | True | `None` | — | — |
| x15 | s | x11 | 2.402 | 2.262 | 95 | False | `None` | — | — |
| x02 | m | x09 | 2.398 | 2.386 | 41 | False | `None` | — | — |
| x24 | m | x04 | 2.368 | 2.514 | 19 | True | `None` | — | — |
| x22 | s | x29 | 2.321 | 3.344 | 77 | False | `None` | — | — |
| x20 | l | x29 | 2.311 | 2.155 | 728 | False | `None` | — | — |
| x17 | l | x11 | 2.307 | 2.468 | 803 | True | `None` | — | — |
| x17 | m | x04 | 2.281 | 4.735 | 39 | True | `None` | — | — |
| x13 | m | x18 | 2.264 | 2.835 | 34 | True | `None` | — | — |
| x12 | m | x00 | 2.262 | 2.213 | 94 | True | `None` | — | — |
| x16 | l | x12 | 2.253 | 1.873 | 431 | False | `None` | — | — |
| x02 | m | x12 | 2.244 | 2.183 | 135 | True | `None` | — | — |
| x16 | l | x14 | 2.223 | 1.845 | 424 | False | `None` | — | — |
| x29 | m | x05 | 2.213 | 1.906 | 105 | False | `None` | — | — |
| x29 | l | x19 | 2.189 | 1.955 | 313 | True | `None` | — | — |
| x15 | m | x17 | 2.139 | 1.799 | 188 | True | `None` | — | — |
| x30 | m | x22 | 2.123 | 3.917 | 31 | True | `None` | — | — |
| x22 | l | x19 | 2.1 | 1.701 | 264 | True | `None` | — | — |
| x27 | m | x04 | 2.081 | 3.586 | 53 | True | `None` | — | — |
| x27 | l | x11 | 2.077 | 2.12 | 753 | True | `None` | — | — |
| x02 | l | x24 | 2.035 | 1.979 | 161 | True | `None` | — | — |
| x09 | s | x22 | 2.031 | 1.795 | 23 | True | `None` | — | — |
| x22 | m | x04 | 1.997 | 2.744 | 84 | True | `None` | — | — |
| x20 | l | x17 | 1.966 | 1.943 | 195 | False | `None` | — | — |
| x29 | l | x15 | 1.942 | 1.841 | 367 | False | `None` | — | — |
| x03 | s | x15 | 1.917 | 1.851 | 13 | False | `None` | — | — |
| x20 | l | x05 | 1.906 | 1.83 | 189 | False | `None` | — | — |
| x12 | m | x02 | 1.886 | 2.11 | 137 | True | `None` | — | — |
| x05 | l | x11 | 1.885 | 1.783 | 695 | True | `None` | — | — |
| x17 | l | x19 | 1.883 | 1.63 | 251 | False | `None` | — | — |
| x09 | m | x27 | 1.875 | 1.678 | 77 | True | `None` | — | — |
| x03 | m | x22 | 1.868 | 1.929 | 47 | False | `None` | — | — |
| x04 | s | x12 | 1.866 | 2.484 | 30 | True | `None` | — | — |
| x09 | s | x18 | 1.863 | 2.797 | 16 | False | `None` | — | — |
| x00 | l | x05 | 1.852 | 1.608 | 183 | True | `None` | — | — |
| x20 | l | x27 | 1.839 | 1.674 | 222 | False | `None` | — | — |
| x27 | m | x22 | 1.837 | 1.812 | 163 | True | `None` | — | — |
| x15 | m | x05 | 1.832 | 1.542 | 161 | True | `None` | — | — |
| x23 | l | x22 | 1.817 | 2.011 | 132 | True | `None` | — | — |
| x11 | m | x22 | 1.798 | 1.588 | 179 | True | `None` | — | — |
| x21 | l | x22 | 1.795 | 1.59 | 154 | False | `None` | — | — |
| x24 | m | x12 | 1.792 | 1.606 | 135 | True | `None` | — | — |
| x29 | s | x22 | 1.785 | 1.952 | 75 | True | `None` | — | — |
| x21 | l | x15 | 1.784 | 1.501 | 153 | False | `None` | — | — |
| x22 | m | x15 | 1.781 | 1.7 | 261 | True | `None` | — | — |
| x00 | m | x22 | 1.768 | 1.698 | 73 | True | `None` | — | — |
| x00 | m | x27 | 1.76 | 2.157 | 55 | True | `None` | — | — |
| x05 | l | x27 | 1.727 | 1.59 | 244 | True | `None` | — | — |
| x12 | m | x09 | 1.686 | 1.586 | 187 | True | `None` | — | — |
| x17 | l | x15 | 1.669 | 1.513 | 294 | False | `None` | — | — |
| x27 | s | x18 | 1.641 | 1.658 | 29 | True | `None` | — | — |
| x26 | l | x18 | 1.633 | 1.658 | 122 | True | `None` | — | — |
| x27 | s | x29 | 1.629 | 1.567 | 75 | False | `None` | — | — |
| x26 | l | x09 | 1.616 | 1.6 | 122 | True | `None` | — | — |
| x09 | m | x05 | 1.601 | 1.559 | 54 | True | `None` | — | — |
| x28 | l | x18 | 1.586 | 1.776 | 119 | True | `None` | — | — |
| x19 | s | x11 | 1.576 | 1.543 | 70 | False | `None` | — | — |
| x28 | l | x09 | 1.557 | 1.653 | 118 | True | `None` | — | — |
| x05 | m | x04 | 1.554 | 3.074 | 31 | True | `None` | — | — |
| x11 | m | x27 | 1.553 | 1.548 | 117 | False | `None` | — | — |
| x24 | l | x18 | 1.536 | 1.599 | 202 | True | `None` | — | — |
| x05 | m | x11 | 1.516 | 1.508 | 208 | False | `None` | — | — |
| x00 | l | x11 | 1.506 | 1.555 | 473 | True | `None` | — | — |

## Loops (returns; verdicts recorded, not promoted)

| X | l1 | Y | l2 | X′ | n | cond. lift | timing (g1 / g2) | determinism (p1 / p2) | used |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Chains (non-return): 32.

## Absences

- silent roles: none
- roles never a target: ['x03', 'x16', 'x20', 'x21', 'x23']
- keyed pairs not found: none
- signal floor: 51 (absence is informative only for pairs whose support would exceed the signal floor)

## Regimes

none recorded

## Matrix row

Cells in (this system as receiver):

| source | structure | net (derangement) | raw | marginal | derangement | larger control | share of ceiling | types | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| building_b_stretch (diagonal) | 92.12 | 150.00 | 44.22 | -47.89 | -105.78 | marginal | — | 22/22 |  |
| building_59 | -1.11 | 0.34 | 11.28 | 12.39 | 10.94 | marginal | -0.01 | 22/22 |  |
| alibaba_2018 | -0.30 | 4.50 | 12.16 | 12.46 | 7.65 | marginal | -0.00 | 21/22 | damage |

Cells out (this system as source):

| receiver | structure | net (derangement) | raw | marginal | derangement | larger control | share of ceiling | types | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| building_59 | -4.51 | -1.33 | 119.17 | 123.69 | 120.51 | marginal | -0.04 | 26/89 |  |
| alibaba_2018 | -1.03 | 0.16 | 0.42 | 1.45 | 0.27 | marginal | — | 27/27 |  |

Nearest taxa by distance: 
