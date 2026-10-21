# Benchmark card — Tennessee Eastman (dataset 3), method v2, profile v1, seed 0

Run 2026-10-19 under method v2 (the v1 card is kept as CARD_tennessee_eastman_v1_superseded.md). Source: Souza, de Souza & da Silva (2023) 1-year continuous run of the Tennessee Eastman
process (Ricker's revised model), https://github.com/anasouzac/new_tep_datasets, `matlab_data_1year.csv`.
Declared span: the first 120 days (57,600 samples at 3 min). Days 120–365 untouched (continuation).

## Identity and scale

| | |
| --- | --- |
| Kind | simulated plant, random fault episodes (IDV 1–20) with normal operation between; fault label excluded from events, kept as 82 regime annotations in the sidecar |
| Entity | **vessel** (reactor, separator, stripper), chosen over a single plant entity by 3.1: 4.280 vs 5.329 bits/event, Markov features only |
| Symbolization (3.2) | 40 roles; 26 quantile crossings (q20/50/80, per-unit thresholds), 13 turning points (product analysers, D/E feeds, levels, purge, purge valve), 1 silent (stripper steam: no detectable signal at the sampling scale). Noise windows 1–136 samples. |
| Events | 280,002 in 120 days (2,333/day); 78,562 vessel targets (reactor 30,427; separator 26,513; stripper 21,622), 201,440 system-wide |
| Types | 186 in all; 40 target types |
| Lag classes (3.3, v2) | edges 10.9 / 39.5 / 143.2 min — horizon = median type recurrence time (2.4 h), geometric bands from the 3-min resolution; all three classes populated (v1: 3 / 9 / 21 with class s empty) |
| Period (3.4) | none (the acf of the event rate decays slowly with regime switching; no prominent peak with ≥ 8 repetitions) |
| Signal floor (3.5) | 108 events (descriptive) |
| Nulls run (3.8) | circular (gate), rewire (attribute); survival 0.60 / 0.32 |
| Discovery | 21,863 candidates → 567 validated fragments (186 distinct contexts), 0 compositions kept |
| Test split | 19,784 events (days 90–120), evaluated once |

## Headline (bits per event on the test split; no deterministic types)

| model | bits |
| --- | --- |
| unigram | 5.087 |
| markov-1 | 4.524 |
| markov-2 | 4.606 |
| markov-3 | 5.188 |
| hawkes-like decay features | 3.410 |
| logistic markov features | 4.196 |
| logistic triviality library (3.11) | 3.171 |
| **logistic library** | **3.033** |
| logistic unselected contexts | 3.176 |

Gain over triviality **0.138** bits; over the best baseline (Hawkes-like, 3.410) **0.377** bits → claim: **beats baselines**.
The validated library beats the unselected contexts by 0.143 bits. (v1, 21-min horizon: 3.387 / 3.569 / 3.978,
gains 0.183 / 0.592; every model improved under the longer horizon, the baselines most.)

Trivial pairs found (3.11): threshold re-crossings of every quantile role (downqX ↔ upqX) and L:peak ↔ L:trough.

## What the library contains

- 567 fragments, lag classes s 269 / m 216 / l 82; target roles P 116, cw_out 108, cw_flow 107, T 106,
  underflow_valve 62, feed 60, underflow 8, L 0; chatty share 0.11; binding evidence (rewire) 32%.
- **Cooling-water mechanism** recovered with the right sign in both vessels: cw_flow:up → cw_out:down,
  24 fragments, lift up to 4.9, now at lag s (≤ 11 min) as well as m.
- **Underflow valve → underflow** recovered (3 fragments, lags m and l, lift 1.7–2.1) — invisible under
  the v1 horizon.
- Not recovered: cw_flow → T, steam → T (steam is silent), underflow → L (L is never a target of anything).

## Recovery (answer key: flowsheet actuator → measurement, role prefix, any lag)

recall 2/10, precision 0.048. Five of the ten keyed pairs (feed valves → feed flows, purge valve → purge)
are between system-wide roles, which are contexts and never targets under the vessel entity, so they are
unrecoverable by construction here; the key should list only pairs whose effect is an entity role. Of the
five recoverable pairs, two are found (cw_flow → cw_out; underflow_valve → underflow); cw_flow → T is not,
steam → T cannot be (steam silent); underflow → L finds no fragments at all.

## Open items raised by this dataset (not rules)

1. (settled in v2) The horizon followed event density; now the recurrence time, with geometric lag bands.
2. Answer keys should name only pairs whose effect is a target role under the chosen entity.
3. Vessel level (L, turning points) is never predicted by anything; whether that is the symbolization or the
   plant is open.
4. Bits per event are high (3.0) because the streams are busy and the vocabulary is 40 types; absolute
   levels are not comparable across datasets, gains are.

## v6 regeneration (2026-10-20): gap clipping and syntax motifs

Rules changed in v6: 3.6 (a gap clips the window instead of dropping the target), 3.15 (chains and returns).
TEP has no gaps, so the card above is unchanged to the third decimal: 567 fragments (186 used), library 3.033
bits, triviality 3.171, claim **beats baselines**, recovery 2/10.

**Syntax (3.15).** 5,733 chain candidates (two validated fragments sharing a middle type) → 938 with conditional
lift ≥ 1.5 → 926 above the circular null → **525 admitted, 106 of them returns**. None reduce confirmation bits
as features on top of the 186 fragment contexts, so the library score is unchanged; the chains are recorded, not
used. Returns by end role and middle role: cooling-water flow ↔ cooling-water outlet temperature 24, vessel
temperature ↔ cooling-water outlet 24, underflow valve ↔ vessel temperature 21, cooling-water flow → pressure →
cooling-water flow 7, cooling-water flow → feed → cooling-water flow 5. The cooling-water loop's strongest
return is `cw_flow:downq20 -s-> P:downq20 -m-> cw_flow:upq20` (n = 46, conditional lift 3.52, null max 11,
confirmation 30 / 2.95): the flow falls, the vessel pressure falls, the flow rises. In the tagged alphabet it is
`SLOW·RELAY.down.q20 -s-> MID·FOLLOW.down.q20 -m-> SLOW·RELAY.up.q20 [return]`.

**Place prefix of a loop.** No return in any dataset is spelled LEAD → FOLLOW → LEAD, and none can be: an
actuator inside a closed loop is both a context and a target, so the degree rule (3.14) tags it RELAY. LEAD
appears only at the start of open chains (LEAD → RELAY → RELAY, 76 here: feeds and valves that drive without
being driven). A loop closing reads RELAY → FOLLOW → RELAY (31 returns here) or RELAY → RELAY → RELAY (47).

## v7 regeneration (2026-10-21): loop roles, fine-grid period, admission in horizons

Fragments, chains and the headline are unchanged (567 fragments, 525 chains, 106 returns, library 3.033). The fine
grid finds no fast period (`period_fast: none`, as expected of a plant without a cycle). Admission: 120 days,
**1,206 H** (test split 302 H) → admitted by days.

**Loop roles (3.16).** 87 of 106 returns resolved, 19 unresolved. The realised gaps inside the fast lag class are
multiples of the 3-minute sample (g1 takes the values 3, 6, 9 … min; the strongest return,
`underflow_valve:downq20 -s-> P:downq80 -s-> underflow_valve:upq20`, has g1 = g2 = 6.0 and is unresolved), so the
verdicts rest on one or two samples' difference. Tags: **underflow_valve REACTS** (9 votes to 7), P REACTS, T
REACTS, feed REACTS; **cw_flow RESPONDS** (25 to 16), cw_out RESPONDS, underflow RESPONDS. The expectation that
both the valve and the cooling-water flow land on REACTS holds for the valve and is inverted for the flow: in the
cooling-water returns the pressure or temperature answers the flow faster than the flow answers them.

| check | result | chance |
| --- | --- | --- |
| dimension: REACTS roles dimensionless | 1 of 4 (0.25) | 0.5 |
| dimension: RESPONDS roles dimensioned | 2 of 3 (0.67) | 0.5 |
| flowsheet: actuator on the REACTS side of actuator–measurement returns | 24 of 44 (**0.55**) | 0.5 |

At 3-minute sampling the loop tag does not separate controller from plant on this plant: the flowsheet check is
at chance and the dimension check below it. The card records it; nothing is corrected by hand. The shapes are
respelled under the tags (`MID·REACTS.down.q20 -s-> MID·REACTS.down.q80 -s-> MID·REACTS.up.q20 [return]` for the
valve–pressure return) and so is the lineage.

## v8 regeneration (2026-10-21): loop rules recorded, not in the prefix

Fragments, chains, returns and the headline are unchanged (567 / 525 / 106; library 3.033). The place prefix spells
the degree tags again (cw_flow `SLOW·LOCAL·RELAY`); the loop rules are recorded with their checks (3.16, v8).

| rule | resolved | unresolved | flowsheet check | dimension check (REACTS dimensionless / RESPONDS dimensioned) | promotable (≥ 0.75, ≥ 10 returns) |
| --- | --- | --- | --- | --- | --- |
| timing (v7) | 87 | 19 | 24 of 44 = **0.55** | 0.25 / 0.67 (n 4 / 3) | no |
| determinism (v8 candidate) | 59 | 47 | 10 of 28 = **0.36** | 0.00 / 0.50 (n 2 / 4) | no |

Declared predictions (3.16) against what came out:

| role | predicted | timing | determinism |
| --- | --- | --- | --- |
| underflow_valve | REACTS | REACTS (9 : 7) | **RESPONDS** (12 : 4) |
| cw_flow | REACTS | **RESPONDS** (25 : 16) | **RESPONDS** (17 : 6) |

The determinism rule does worse than timing on this plant: both actuators land on RESPONDS, and the flowsheet
check falls below chance. The leg *into* the valve is less deterministic than the leg out of it — on a simulated
plant the measurement follows the valve almost deterministically while the valve answers a pressure deviation
only when the controller's deadband is crossed. Neither rule is promotable here; neither enters the prefix.
