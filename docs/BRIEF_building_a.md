# Brief — building_a (method v8, a view)

*Lifts are odds ratios on the proposal split (3.6-3.8), confirmed on the confirmation split; absence is informative only above the signal floor (3.5); `no gain` means found but already carried by the trivial alternation model (3.11); loop-rule verdicts are recorded, not promoted (3.16); cells are bit-horizons net of the larger of two controls, with share of the receiver's ceiling where a diagonal exists (3.12).*

## Identity

- kind: synthetic; standing: synthetic
- entity: zone (3 units); H = 177.5 min; lag edges [5.62, 31.58, 177.5] min
- periods: slow 1440.0, fast —; admission: {'days': 59.97, 'slow_periods': 60.0, 'horizons': 486.5, 'test_horizons': 121.6, 'admitted': True, 'by': 'days'}
- claim: **no gain** — library 2.164 bits, triviality 2.169, best baseline 2.562; gain over triviality 0.005
- events 11661, types 20, signal floor 22

## Vocabulary

| role | full tag | quantity | scheme | loop tags (timing / determinism) |
| --- | --- | --- | --- | --- |
| CO2 | — | — | silent | — / — |
| RH | — | — | silent | — / — |
| T | — | — | silent | — / — |
| T_out | — | — | silent | — / — |
| heater | — | — | silent | — / — |
| occ | — | — | silent | — / — |
| setpoint | — | — | silent | — / — |
| vent | — | — | silent | — / — |

## Couplings (validated fragments)

| prior | lag | target | lift | conf. lift | n | binding | shape | confirmed in | failed in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| setpoint:up | m | T:up20 | 24.327 | 24.838 | 34 | False | `None` | — | — |
| RH:up70 | s | RH:down70 | 23.833 | 18.816 | 4 | False | `None` | — | — |
| RH:down70 | m | RH:up70 | 17.055 | 11.252 | 19 | True | `None` | — | — |
| RH:up70 | m | RH:down70 | 14.766 | 11.05 | 19 | True | `None` | — | — |
| CO2:down700 | s | vent:off | 14.5 | 15.075 | 146 | True | `None` | — | — |
| vent:off | s | CO2:up700 | 13.114 | 11.584 | 60 | True | `None` | — | — |
| CO2:up900 | s | vent:on | 12.721 | 14.908 | 146 | True | `None` | — | — |
| heater:on | s | T:up20 | 11.093 | 11.162 | 59 | True | `None` | — | — |
| RH:down50 | m | RH:up50 | 9.812 | 10.575 | 14 | False | `None` | — | — |
| RH:down70 | s | RH:up70 | 9.425 | 9.425 | 3 | False | `None` | — | — |
| vent:on | s | CO2:down900 | 9.274 | 10.568 | 99 | True | `None` | — | — |
| CO2:down700 | s | CO2:up700 | 7.372 | 6.989 | 91 | True | `None` | — | — |
| T:down20 | s | T:up20 | 6.976 | 7.742 | 52 | True | `None` | — | — |
| T_out:down10 | m | T:down20 | 6.597 | 3.503 | 14 | False | `None` | — | — |
| CO2:up900 | s | CO2:down900 | 5.733 | 5.113 | 105 | True | `None` | — | — |
| setpoint:up | s | heater:on | 5.323 | 5.126 | 33 | False | `None` | — | — |
| CO2:up700 | m | vent:on | 4.76 | 4.329 | 121 | True | `None` | — | — |
| setpoint:down | s | heater:off | 4.442 | 3.3 | 10 | False | `None` | — | — |
| CO2:down900 | s | T:down20 | 4.401 | 2.92 | 18 | True | `None` | — | — |
| occ:leave | s | CO2:down700 | 4.079 | 4.142 | 50 | True | `None` | — | — |
| vent:off | m | vent:on | 4.025 | 3.687 | 70 | True | `None` | — | — |
| CO2:down700 | m | vent:on | 3.578 | 3.244 | 65 | True | `None` | — | — |
| setpoint:up | l | occ:arrive | 3.573 | 3.198 | 229 | False | `None` | — | — |
| occ:leave | s | vent:off | 3.501 | 3.65 | 35 | True | `None` | — | — |
| heater:on | m | heater:off | 3.492 | 3.303 | 638 | True | `None` | — | — |
| occ:arrive | s | CO2:up900 | 3.467 | 4.0 | 45 | True | `None` | — | — |
| vent:on | m | vent:off | 3.232 | 2.135 | 47 | True | `None` | — | — |
| occ:arrive | s | vent:on | 3.197 | 3.351 | 26 | False | `None` | — | — |
| CO2:up700 | m | CO2:up900 | 3.155 | 2.977 | 128 | True | `None` | — | — |
| T_out:up10 | l | T:up20 | 3.122 | 2.362 | 52 | False | `None` | — | — |
| T:down20 | m | vent:off | 3.024 | 2.465 | 28 | True | `None` | — | — |
| CO2:down900 | m | vent:off | 3.022 | 2.554 | 60 | True | `None` | — | — |
| vent:off | l | CO2:down700 | 3.001 | 2.823 | 93 | True | `None` | — | — |
| T:down20 | m | RH:down70 | 2.99 | 2.068 | 11 | False | `None` | — | — |
| vent:off | s | T:up20 | 2.916 | 5.366 | 12 | True | `None` | — | — |
| heater:on | s | CO2:down700 | 2.875 | 1.699 | 17 | True | `None` | — | — |
| vent:on | s | T:down20 | 2.865 | 2.7 | 21 | True | `None` | — | — |
| heater:off | m | RH:up70 | 2.787 | 2.826 | 25 | True | `None` | — | — |
| vent:off | l | T:down20 | 2.743 | 2.958 | 76 | True | `None` | — | — |
| T:down20 | m | CO2:down700 | 2.731 | 2.393 | 31 | False | `None` | — | — |
| RH:up50 | m | vent:on | 2.715 | 2.84 | 13 | True | `None` | — | — |
| occ:arrive | m | vent:on | 2.708 | 2.275 | 49 | False | `None` | — | — |
| vent:off | m | CO2:up900 | 2.702 | 2.73 | 75 | True | `None` | — | — |
| occ:leave | m | vent:off | 2.663 | 1.906 | 63 | False | `None` | — | — |
| vent:on | m | CO2:down700 | 2.637 | 1.741 | 47 | True | `None` | — | — |
| RH:up50 | m | CO2:down900 | 2.617 | 2.225 | 20 | True | `None` | — | — |
| CO2:up700 | m | CO2:down900 | 2.588 | 2.316 | 105 | True | `None` | — | — |
| CO2:down900 | m | CO2:down700 | 2.588 | 2.273 | 63 | True | `None` | — | — |
| occ:leave | l | T:down20 | 2.524 | 2.619 | 78 | False | `None` | — | — |
| CO2:down900 | s | occ:arrive | 2.518 | 2.417 | 28 | False | `None` | — | — |
| CO2:down900 | s | occ:leave | 2.518 | 2.283 | 28 | False | `None` | — | — |
| CO2:up900 | m | CO2:down900 | 2.517 | 2.283 | 85 | True | `None` | — | — |
| CO2:up700 | l | CO2:down700 | 2.474 | 2.233 | 104 | True | `None` | — | — |
| CO2:down700 | m | CO2:up900 | 2.449 | 2.231 | 71 | True | `None` | — | — |
| vent:on | m | RH:down70 | 2.424 | 1.869 | 14 | False | `None` | — | — |
| occ:leave | m | CO2:up700 | 2.413 | 2.357 | 70 | False | `None` | — | — |
| vent:off | m | CO2:down900 | 2.378 | 2.153 | 66 | True | `None` | — | — |
| vent:on | m | T:up20 | 2.37 | 2.862 | 38 | True | `None` | — | — |
| T:down20 | s | heater:on | 2.357 | 2.677 | 85 | True | `None` | — | — |
| T:up20 | l | T:down20 | 2.274 | 2.203 | 106 | True | `None` | — | — |
| vent:on | m | T:down20 | 2.259 | 3.727 | 36 | True | `None` | — | — |
| CO2:up900 | m | T:down20 | 2.243 | 3.596 | 52 | True | `None` | — | — |
| setpoint:up | l | vent:on | 2.138 | 2.084 | 46 | False | `None` | — | — |
| occ:arrive | m | CO2:down900 | 2.112 | 1.814 | 61 | True | `None` | — | — |
| RH:up50 | m | occ:leave | 2.103 | 1.668 | 30 | False | `None` | — | — |
| CO2:down900 | m | T:up20 | 2.101 | 2.106 | 46 | True | `None` | — | — |
| CO2:down700 | m | CO2:down900 | 2.07 | 1.934 | 60 | True | `None` | — | — |
| T:up20 | l | occ:arrive | 1.933 | 1.581 | 245 | True | `None` | — | — |
| setpoint:up | l | CO2:up900 | 1.893 | 1.791 | 65 | False | `None` | — | — |
| occ:arrive | m | CO2:up900 | 1.87 | 2.074 | 54 | False | `None` | — | — |
| CO2:up900 | m | T:up20 | 1.8 | 2.427 | 42 | True | `None` | — | — |
| setpoint:up | l | CO2:up700 | 1.782 | 1.7 | 47 | False | `None` | — | — |
| vent:on | s | occ:arrive | 1.706 | 1.788 | 34 | True | `None` | — | — |
| CO2:down900 | m | T:down20 | 1.7 | 2.542 | 37 | True | `None` | — | — |
| occ:leave | s | CO2:down900 | 1.692 | 2.088 | 27 | False | `None` | — | — |
| RH:down50 | l | occ:arrive | 1.604 | 2.23 | 86 | True | `None` | — | — |
| CO2:up900 | m | RH:down70 | 1.547 | 2.059 | 13 | False | `None` | — | — |
| occ:leave | m | T:up20 | 1.533 | 1.505 | 40 | False | `None` | — | — |

## Loops (returns; verdicts recorded, not promoted)

| X | l1 | Y | l2 | X′ | n | cond. lift | timing (g1 / g2) | determinism (p1 / p2) | used |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T:down20 | m | vent:off | s | T:up20 | 6 | 2.65 | X reacts (8.0 / 2.0) | X reacts (0.087 / 0.208) | True |

Chains (non-return): 14.

## Absences

- silent roles: none
- roles never a target: ['T_out', 'setpoint']
- keyed pairs not found: none
- signal floor: 22 (absence is informative only for pairs whose support would exceed the signal floor)

## Regimes

none recorded

## Matrix row

Cells in (this system as receiver):

| source | structure | net (derangement) | raw | marginal | derangement | larger control | share of ceiling | types | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| building_a_stretch (diagonal) | 235.76 | 386.89 | 126.34 | -109.42 | -260.55 | marginal | — | 20/20 |  |
| building_59 | -1.93 | 4.59 | 20.85 | 22.78 | 16.26 | marginal | -0.01 | 12/20 | damage |
| alibaba_2018 | -1.10 | 5.49 | 22.68 | 23.78 | 17.19 | marginal | -0.00 | 8/20 |  |

Cells out (this system as source):

| receiver | structure | net (derangement) | raw | marginal | derangement | larger control | share of ceiling | types | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| building_59 | -0.93 | 0.68 | 118.64 | 119.56 | 117.96 | marginal | -0.01 | 22/89 |  |
| alibaba_2018 | -0.22 | -0.22 | -0.18 | -0.04 | 0.04 | derangement | — | 21/27 | damage |

Nearest taxa by distance: 
