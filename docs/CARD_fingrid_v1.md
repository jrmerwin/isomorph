# Benchmark card — Fingrid, Nordic grid frequency regulation (dataset 9), method v8, profile v1, seed 0

Run 2026-10-21. Source: Fingrid open data (https://data.fingrid.fi, CC BY 4.0), fetched with a registered key that is
never stored (`scripts/fetch_fingrid.py`): series 177 frequency (Hz, 3 min), 343 / 344 FCR-N activated down / up
(MW, 15 min), 349 / 350 aFRR energy activation up / down (MW, 15 min), 194 net import / export (MW, 3 min);
2024-07-01 to 2025-07-01. The Rosetta member whose measured quantity is ⟨T⁻¹⟩ and whose loop is the whole Nordic
synchronous area: the frequency falls, the reserve activates, the frequency recovers.

## Declarations

- **3-minute samples**, the native interval of the frequency and the net transfer. The 15-minute reserve series
  are **held within their quarter** on the 3-minute grid (a value observed over a quarter is the value at every
  sample in it) — which makes every leg *into* a reserve at least one quarter long by construction (see loop roles).
- **One entity.** The synchronous area is one system with one copy of every role; 3.1 has a single candidate
  (`grid`) and nothing to compare. No gaps declared; missing samples are missing values.
- The calculated imbalance series (397, 1 min) begins 2025-06-25 and is left out of the year.

## Identity and scale

| | |
| --- | --- |
| Entity | **grid**, one unit, six roles |
| Symbolization (3.2) | turning points for f, fcrn_up, fcrn_down, afrr_down, net_ie (noise windows 1–9 samples; the frequency is denoised over 9 × 3 min); afrr_up q20/50/80 at 0 / 1.9 / 30.2 MW (it sits at zero most of the time) |
| Events | 79,367 in 365 days (217/day); 16 types; net_ie 373 events (a smooth series at 3 min) |
| Lag classes (3.3) | 9.3 / 29.0 / 90.0 min (recurrence horizon 1.5 h) |
| Period (3.4) | slow: none; **fast: 15.0 min** — the market quarter, i.e. the interval the reserve series are held over; the cycle null runs at it |
| Admission (section 6) | 365 days · 5,840 H (test 1,460 H) → **admitted** |
| Nulls (3.8) | circular 0.69; cycle 0.65 (no rewire: one entity) |
| Discovery | 664 candidates → **71 validated fragments** (30 used), 185 compositions; chatty share 0.15 |
| Syntax (3.15) | 367 chain candidates → 17 with conditional lift → 17 above the null → **15 admitted, 3 returns**, all 15 used as features |
| Test split | 21,998 events (the last 91 days), evaluated once |

## Headline (bits per event on the test split)

| model | all |
| --- | --- |
| unigram | 3.783 |
| markov-1 / -2 / -3 | 2.828 / 2.659 / 2.626 |
| hawkes-like decay features | **2.588** |
| logistic markov features | 2.638 |
| logistic triviality library (3.11) | 1.603 |
| logistic library | 1.615 |
| logistic unselected contexts | 1.603 |

Gain over triviality **−0.012** bits; over the best baseline (Hawkes-like, 2.588) +0.974 → claim: **no gain**. The
alternation model carries a bounded frequency and reserves that switch on and off; the library's 0.97-bit margin
over every sequence baseline is the largest in the collection and the rule reports the smaller number.

## Reading the result

**Recovery 6 of 7.** The frequency containment loop is the top of the library: `fcrn_down:trough -s-> f:peak`
(n 1,311, lift 9.7), `fcrn_down:peak -s-> f:trough` (9.7), `fcrn_up:peak -s-> f:trough` (7.7), `fcrn_up:trough -s->
f:peak` (7.3) — the reserve's turning points and the frequency's within nine minutes of each other, both
directions keyed and found; `f:trough -s-> afrr_down:peak` and `f:peak -s-> afrr_down:trough` (4.2, 3.5) for the
restoration reserve. Not found: net import / export → frequency (373 events: at 3 min the net transfer is smooth
and emits almost nothing).

**The loop closes on the reserve, not on the frequency.** Three returns, all on aFRR up-regulation with the
frequency or the down-regulation in the middle: `afrr_up:upq80 -s-> f:trough -m-> afrr_up:downq80` (n 202, cond.
lift 2.46; up-regulation rises, the frequency bottoms within nine minutes, the up-regulation falls a quarter or
two later). A return *on f* — f falls, reserve rises, f recovers — is not admitted: the frequency's own
re-crossing (`f:trough → f:peak`) is a function word the triviality baseline owns, and the chain through the
reserve does not beat its last link by 1.5.

**Loop roles.** Timing: 3 of 3 resolved, **f REACTS**, afrr_up RESPONDS, afrr_down REACTS; determinism agrees
(2 of 3). That the frequency "reacts" and the reserve "responds" is the hold: every leg into a reserve is a
multiple of 15 min by declaration (g₂ = 15 or 24 min against g₁ = 3–6), so the timing rule can only ever put the
frequency on the fast side here. The flowsheet check has nothing to count: the key's only pure actuator is
net_ie, and the reserves are both causes and effects. No prediction was declared for this dataset.

## Open items raised by this dataset (not rules)

1. **Held series and the timing rule.** A 15-minute series held on a 3-minute grid fixes the minimum gap of
   every leg into it; a loop rule based on realised gaps cannot be read on a mixed-resolution dataset. The
   honest declaration for the loop is the reserves' own 15 minutes, which would also change the frequency's clock.
2. **The fast period is the market.** 15.0 min on the fine grid is the quarter-hour of the reserve series, not
   a dynamic of the grid; the cycle null at that period is right to run and the card should say what it found.
3. **A return on the frequency** needs the frequency's re-crossing not to be trivial: the same question HAI
   and the battery raised about 3.11, now for the one dataset whose whole point is that loop.
