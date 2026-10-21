# Benchmark card — NASA PCoE battery set, FY08Q4 (dataset 6), method v5, profile v1, seed 0

Run 2026-10-20. Source: NASA Ames Prognostics Center of Excellence Battery Data Set (Saha & Goebel 2007),
https://data.nasa.gov/dataset/li-ion-battery-aging-datasets, group 1 (BatteryAgingARC-FY08Q4): four 18650 Li-ion
cells cycled to end of life at 24 °C — B0005, B0006, B0007 together (2 April – 28 May 2008; 170 charge and 168
discharge cycles each) and B0018 alone (7 July – 20 August 2008; 134 / 132). A charge is 1.5 A constant current
to 4.2 V then constant voltage to a 20 mA cutoff (~3 h); a discharge is 2 A constant current to a cell-specific
cutoff (~1 h). The electrochemical member of the Rosetta set: current (actuator) ⟨I⟩ → terminal voltage and cell
temperature ⟨Θ⟩, the analogue of filling and draining a tank.

## Declarations

- **Resolution: 1-minute means** of the 3–20 s source (within a cycle every minute is sampled).
- **Time axis compressed**: the 1,280 charge and discharge cycles are placed on the real clock, then every
  unobserved stretch — the rests between cycles (median 33 min; 431 of 469 are an hour or less), the impedance
  tests (which carry no time series of the same kind and are left out) and the 41-day gap between the two
  campaigns — is removed and declared a gap for every entity observed on either side of it.
- **Observation**: B0005–7 minutes 0–38,440 (26.7 days, concurrent); B0018 minutes 38,440–68,369 (20.8 days).
- **Span 47.5 observed days — admitted on the 20-day line.** The period rule also finds the cycle (239.5 min:
  charge, discharge and the rests between them), so the cycle null is active.
- Capacity per discharge (B0005: 1.86 → 1.33 Ah over 168 cycles) is recorded in the sidecar as the slow regime
  and is not in the events.

## Identity and scale

| | |
| --- | --- |
| Entity | **cell** (B0005, B0006, B0007, B0018 as units with roles V, I, T), chosen by 3.1: 1.043 vs 14.735 bits/event Markov-only for a single system — the widest margin in the collection; three cells on one schedule as one system is four copies of every type and no cross-cell mechanism |
| Symbolization (3.2) | V: q20/50/80 — the only faithful scheme — at 3.75 / 4.205 / 4.206 V: the upper two thresholds coincide at the 4.2 V constant-voltage hold, where a cell sits for ~40% of observed time, so the two upper crossings fire together; I: q10/90 at −2.01 / +1.51 A — the crossings are the protocol's own switches (discharge on/off, charge on/off); T: turning points; no denoising needed (window 1 everywhere) |
| Events | 12,274 in 47.5 days (259/day): B0005 3,423, B0006 3,213, B0007 3,299, B0018 2,339 |
| Types | 12 |
| Lag classes (3.3) | 5.8 / 33.7 / 195.8 min (recurrence horizon 3.3 h) |
| Period (3.4) | 239.5 min |
| Signal floor (3.5) | 6 (descriptive) |
| Nulls (3.8) | circular (gate) survival 0.52; cycle (gate) 0.58; rewire (attribute) 0.12 |
| Discovery | 40 candidates → **12 validated fragments** (9 used), 0 compositions; chatty share 0.25 |
| Dropped for gaps | **11,436 of 12,274 events (93%)**: the observed stretches are one cycle long (median 169 min) and the horizon is 196 min, so nearly every target's look-back window overlaps a boundary |
| Test split | 1,371 events (last 11.9 days of B0018's campaign), evaluated once |

## Headline (bits per event on the test split)

| model | all |
| --- | --- |
| unigram | 3.506 |
| markov-1 | 2.910 |
| markov-2 | **2.745** |
| markov-3 | 2.750 |
| hawkes-like decay features | 3.024 |
| logistic markov features | 2.841 |
| logistic triviality library (3.11) | 2.711 |
| logistic library | 2.781 |
| logistic unselected contexts | 2.720 |

Gain over triviality **−0.071** bits; over the best baseline (Markov-2, 2.745) −0.036 → claim: **no gain**.

## Reading the result

**Recovery 2 of 3.** Current → temperature is in the library as `I:upq10 -m/s-> T:peak` (lift 6.9 and 9.7): the
discharge current switching off (the −2 A crossing upward) is followed by the temperature peak — the cell heats
under the 2 A load and peaks when it is removed. Voltage → current is there as six fragments `V:* -l-> I:upq10`
(lift 3.8–4.5): the voltage crossings of a charge precede the next discharge's end by one long lag. Current →
voltage is not found: the voltage response to a current step is within the same minute, and the first lag class
begins at 5.8 min. The two unkeyed fragments (`T:peak -l-> I:upq10`, `I:downq10 -m-> I:upq10`, the discharge's
own duration) are the protocol's sequence.

**The triviality baseline carries the protocol.** Every role alternates by construction — a discharge starts and
ends, a charge starts and ends, the voltage rises to 4.2 V and falls, the temperature peaks and troughs — so the
six same-role pairs at three lag classes score 2.711 and the validated library 2.781. As on HAI, the method finds
the physics and declines to claim it as non-trivial structure, correctly under its own rules: what a cell does
under a fixed cycling protocol *is* an alternation.

**93% of events are dropped before mining.** That is the card's largest fact. The protocol fragments observation
into one-cycle stretches, the horizon (a recurrence time) comes out at one cycle, and the gap rule drops any
target whose window spans a boundary. The library is built from the 838 events that sit a full horizon past the
start of a stretch, i.e. the tails of the longest charges. The fragments above are real, but the instrument has
seen a twentieth of the data.

## Open items raised by this dataset (not rules)

1. **Gap rule for fragmented observation.** Dropping the whole target when its window overlaps a gap is right
   for a dropout inside a long observation and wrong for a campaign of one-cycle stretches; a candidate rule drops
   only the context tokens on the far side of the gap and keeps the target with the contexts inside its stretch.
   A method question (v6), to settle before the rest of the Rosetta set, which will be cycled protocols too.
2. **Quantile schemes on a held series.** V's q50 and q80 coincide at the constant-voltage setpoint; the
   faithfulness floor admits only this scheme, so two of V's six types are near-duplicates. An "at setpoint"
   symbol (SET-like plateau detection) would be the honest spelling.
3. Current → voltage lives below the first lag class at 1-minute means; a finer declaration for this dataset
   would find it and lose the thermal lags. One resolution per dataset is the rule; the card records the cost.
4. Ageing is a slow regime (capacity 1.86 → 1.33 Ah) that none of the baselines or the library can see; it is
   the natural first "regime drift" test when regimes become a field.

## v6 regeneration (2026-10-20): gap clipping and syntax motifs

Rules changed in v6: 3.6 (a gap clips the window instead of dropping the target), 3.15 (chains and returns).
This is the card the gap rule was changed for, and it is a different card.

| | v5 | v6 |
| --- | --- | --- |
| events dropped for gaps | 11,436 (93%) | **1,120 (9%)** |
| validated fragments (used) | 12 (9) | **47 (24)**, 74 compositions |
| recovery | 2/3 | **3/3** (current → voltage now found) |
| logistic library / triviality / best baseline | 2.781 / 2.711 / 2.745 | 0.838 / 0.827 / 1.087 (logistic Markov) |
| gain over triviality | −0.071 | −0.011 → **no gain** |
| chains (used), returns | — | 13 (13), 1 |

Every model fell by about two bits because the Markov contexts now exist on every row (under v5 a dropped
target had none). The triviality baseline still carries the protocol: a cycling protocol is an alternation.

**Syntax (3.15).** 155 candidates → 19 with conditional lift → 19 above the null → **13 admitted, all 13 used**:
the only dataset so far where chains reduce confirmation bits. The one return is the cutoff loop:
`I:downq10 -s-> V:downq20 -s-> I:upq10` (n = 27, conditional lift 2.10, null max 4, confirmation 3 / 3.00) —
the discharge current switches on, the voltage falls through its lower quantile, the discharge switches off.
Spelled `MID-S·RELAY.down.q10 -s-> MID·RELAY.down.q20 -s-> MID-S·RELAY.up.q10 [return]`. The other chains are
the charge's constant-voltage phase (`V:upq50 -s-> V:upq80 -s-> T:peak`, n = 121) and the discharge's
temperature trough preceding the next charge.

## v7 regeneration (2026-10-21): loop roles, fine-grid period, admission in horizons

Unchanged from v6 (47 fragments, 13 chains, 1 return, library 0.838); the slow period 239.5 min is found again and
no fast one. Admission: 47.5 days, **349 H** (test 87 H), 285 slow periods → admitted by days.

**Loop roles (3.16).** The one return, `I:downq10 -s-> V:downq20 -s-> I:upq10`, has g1 = 3.0 min (current → voltage)
and g2 = 1.0 min (voltage → current): the current reacts, the voltage responds — **I REACTS, V RESPONDS**. That is
the protocol: the cycler switches the current the minute the voltage reaches cutoff. The dimension check fails
by construction (a current source is an actuator with a dimension: REACTS dimensionless 0 of 1, RESPONDS
dimensioned 1 of 1) and the flowsheet check has no actuator–measurement return to count (the key's actuator is I
itself and both ends of the return are I). The card says so; the reading holds here where the check does not.

## v8 regeneration (2026-10-21): loop rules recorded

Unchanged (47 fragments, 13 chains, 1 return; 0.838). Timing: I REACTS, V RESPONDS (as in v7). Determinism:
**unresolved** — P(V down | I down within s) and P(I up | V down within s) are within the ratio of 1.5 of each
other: in a cycling protocol both legs are deterministic. No prediction was declared for the battery.
