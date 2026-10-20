# Motif Transfer Method — Specification v1

Oct 18, 2026 · @Jason Merwin

## Purpose and stance

One ruler, applied unchanged to every dataset, so that every result is a number the data produced rather than a choice I made. The method turns an event stream into a validated motif library, scores the library against fixed baselines in bits per event, and measures how much that library helps on every other dataset already in the collection. The collection's output is a directed transfer matrix and the lineage of a shared library grown across datasets.

Three commitments govern everything below.

- Every parameter is either a fixed constant (section 7) or chosen by a stated rule that the data settles, usually held-out compression. There are no per-dataset decisions.
- A claim is reported with its control and its sign, never more. Trivial structure, negative transfer and failures are results of the same standing as gains.
- The pipeline is deterministic end to end given a seed. The one human act is choosing which dataset to feed it.

What this is not: a search for universals. Universals, if any exist, must survive the triviality baseline (3.11) and the negative controls (section 6); until then the object of study is the matrix.

## Canonical data format

Every dataset is converted to one event table and one sidecar before anything runs; nothing downstream ever reads the raw source.

| File | Columns | Rule |
| --- | --- | --- |
| `events.csv` | `event_id` (unique, stable across re-runs), `t` (float, dataset time unit), `entity` (string, or `ALL` for system-wide events), `type` (string, opaque), `value` (float, optional), `tie_rank` (integer, see ties) | One row per event, sorted by `t` then `tie_rank`; types are opaque labels and carry no meaning the pipeline may use |
| `observation.csv` | `entity`, `start`, `end` | The intervals during which each entity was actually observed; absence of events outside them is unknown, not zero |
| `gaps.csv` | `entity`, `start`, `end`, `reason` (optional) | Missing-data intervals inside an observation interval (sensor dropouts, outages); an observed entity with no gaps still has a row-less file |
| `raw/` | the original series or log, untouched | Kept for the symbolization step only (3.2); never read after it |
| `sidecar.json` | `time_unit`, `entity_key` (name of the column that was chosen as entity, or `auto`), `period` (`auto` or a number), `system_wide_types` (list), `tie_rule` (`source` or `canonical`), `answer_key` (optional) | Declares what is known; `auto` means the rule decides |
| `answer_key.json` (optional) | ground-truth mechanisms as a list of (cause type, effect type, lag range) and, for a dataset pair, the role mapping between their types | Used only for scoring recovery; never visible to the pipeline |

Two conventions keep datasets comparable.

- Time is continuous in the dataset's own unit; the pipeline never resamples. Lag classes (3.3) are defined in quantiles of that dataset's inter-event gaps, so they mean the same thing in seconds or in days.
- A dataset with no natural entity gets a single entity named `sys`; system-wide events bind to every entity as context and are never prediction targets.

Four rules make the contract explicit about what event data usually leaves implicit.

- Ties. Events with equal `t` are ordered by `tie_rank`: the source order when the source has one (`tie_rule: source`), otherwise entity then type, lexicographic (`canonical`). Tied events are never each other's predecessor: a context requires a strictly positive gap, so simultaneous events are contemporaneous, not causal.
- Identity. `event_id` is unique within the dataset and stable across re-runs; every fragment instance, null draw and recovered mechanism is recorded by `event_id`, so a result can be traced to the rows that produced it.
- Observation. Counts, lifts, horizons and null shifts are computed only inside an entity's observation intervals; a null shift that would move an event outside its interval wraps within the interval. An entity observed for less than the horizon (3.3) contributes no contexts.
- Gaps. A context window that spans a gap is dropped, not truncated; the same holds for the Markov adjacency features. Gap time is excluded from inter-event gap statistics (3.3) and from period estimation (3.4). The card reports the share of events lost to gap handling.

Outputs are canonical too: `library.json` (fragments with lag class, lift, counts, null survival, provenance), `benchmark.json` (the card in section 4) and one row and column added to `transfer_matrix.csv`.

## Pipeline stage rules

Thirteen stages, in order. Each names what it decides, the rule that decides it, and what it emits. Where a rule says "by compression", the measure is prequential bits per event on the dataset's own confirmation split (3.7), the same measure used for scoring.

&#91;embedded content: pipeline · 10 stages, one loop\]

The upper row is run once per dataset and never revisited; the lower row is re-run for the whole collection every time a dataset is added, which is what makes the matrix and the lineage grow together.

**3.1 Entity.** Candidates are every categorical column of the raw data with between 2 and 1,000 distinct values, plus `sys` (no entity). For each candidate, build per-entity streams and fit the stage-9 model with Markov features only; the candidate with the lowest confirmation-split bits is the entity. Ties within 0.02 bits go to the candidate with more entities (more units, more transfer).

**3.2 Symbolization.** Each continuous variable is first denoised: with f = 1 − acf(1) its white-noise fraction, it is replaced by its centred moving average over w = ⌈f / (0.05 (1 − f))⌉ samples, the window at which the noise left is at most 5% of the signal variance. A clean series (acf(1) ≈ 1) has w = 1 and is unchanged; a variable whose window would exceed 1% of its length has no detectable signal at the sampling scale and emits no events. The scheme is chosen per variable (role) and shared by every unit that has it, so the same mechanism gets the same symbols in every unit; thresholds and windows are each unit's own (its quantiles, its correlation time), so a symbol such as `P:upq80` means the same thing — crossing this unit's 80th percentile — in units that run at different levels. Candidate schemes, all on the denoised series: crossings of its 20/50/80 quantiles; crossings of its 10/90 quantiles; turning points that persist over the series' correlation time (a peak is the maximum within ± one correlation time, the lag at which the autocorrelation first falls below 0.5; troughs likewise, alternation enforced). Per-variable change-points (PELT) are deferred to a later version. Binary and categorical variables emit transitions. Each scheme is debounced for 3 samples. A scheme is admissible only if it is faithful: the denoised series reconstructed from its events (band medians for quantile schemes, interpolation between turning points for the derivative scheme) has a residual median absolute deviation at most 0.5 of the series' own MAD — robust on both sides, because a handful of large fault excursions must not decide whether the symbols describe the bulk of the series; a variable with no faithful scheme emits no events, and a variable with exactly one faithful scheme takes it without comparison. The scheme chosen per variable minimises the TOTAL confirmation bits of the whole table (Markov features plus every lagged context with count at least 3), with system-wide events counted as targets, so a variable is penalised for the events it adds as well as credited for the events it explains; the coordinate search starts from each variable's coarsest faithful scheme and optimises variables one at a time in order of event count, two passes. The result is recorded in the sidecar and never revisited for that dataset. *(v1.0 amended: per-event bits ignored system-wide chatter, and total bits without the faithfulness floor drifted every variable to its coarsest scheme — changelog. The noise floor was added on Tennessee Eastman, whose measurements carry white noise at the 3-minute sampling scale: without it the extrema scheme tracked every noise wiggle, 240,000 events a year for one role, and quantile crossings toggled at the debounce limit; the buildings' signals have acf(1) > 0.999 and are unchanged.)*

**3.3 Lag classes and horizon (v2).** Horizon H = the system's recurrence time: for each target type, the median gap until the same symbol recurs in a stream; H is the median of those medians over types (each type counts once, so chatty types do not set the memory). Lag classes = three geometric bands between the data's time resolution δ (the smallest positive gap) and H: (δ, δr^{1/3}], (δr^{1/3}, δr^{2/3}], (δr^{2/3}, H] with r = H/δ, labelled s/m/l; classes are closed on the right so a gap equal to the sampling interval has a class. Computed on the proposal split only. *(v1: horizon = 95th percentile of inter-event gaps, classes = terciles of within-horizon gaps. On Tennessee Eastman that gave a 21-minute horizon for a plant whose thermal mechanisms act over hours, because 2,300 events a day make the gaps short; and with 3-minute samples the first tercile sat at the sampling interval, leaving class s empty. Terciles of context gaps under an hours-long horizon put the whole short-lag range into one class, hence geometric bands. The change moved every v1 card, so the method is at version 2 and all cards were regenerated.)*

**3.4 Period.** Autocorrelation of the entity-level event rate binned at 0.1% of the proposal span. A qualifying peak is a local maximum above 0.2, at a lag shorter than an eighth of the span (at least eight repetitions), rising at least 0.1 above the autocorrelation minimum before it (a cycle has a trough before its peak), refined to the peak centre by parabolic interpolation. The period is the fundamental: the shortest qualifying peak within 80% of the strongest; `none` if no peak qualifies. Recorded; used only by the cycle null. *(v1.0 amended: 1% bins could not see a daily cycle; "first peak" picked a 5-hour component on building A over the daily cycle, and the dominant peak there is the weekly one; on Tennessee Eastman, which has no cycle, a decaying autocorrelation gave a 9.4-hour bump without the prominence test and a 10.7-day hump with only four repetitions required.)*

**3.5 Signal floor.** Before mining, the median planted-support equivalent: for each of 50 random (context, target) pairs with any proposal count, the support needed to exceed the maximum of its per-type circular-shift null over 19 draws. Reported on the card as a description of the dataset's noise level. It is NOT an admission threshold: admission is decided per pair by that pair's own nulls (3.8). *(v1.0 amended: applied as an absolute minimum count it discarded planted mechanisms whose true support was below the median noise support.)*

**3.6 Candidate contexts.** Within each entity stream, for each event, the set of (prior type, lag class) within the horizon, most recent occurrence per type; system-wide events are included in every entity's context. A target whose horizon window overlaps a missing-data interval of its entity emits no contexts and is counted as dropped. Candidates are all (context, next type) pairs with count at least 3 on the proposal split.

**3.7 Splits.** Chronological 50 / 25 / 25 by time, never shuffled, with three distinct roles. Proposal (first 50%): generate candidates and fit them initially; lifts, counts and null draws are computed here. Confirmation (next 25%): every selection is made here and only here, with the same prequential bits measure: the entity (3.1), the symbolization (3.2), lag classes and horizon (3.3), the retained fragments (3.8), the compositions kept (3.10), the regularisation and mixing weights (3.9, 3.12). Test (last 25%): the fully frozen result is evaluated exactly once; nothing is tuned, chosen or re-run against it, and a second look at the test split is a new version of the method (section 7). Transfer measurements use the receiving dataset's test split only.

**3.8 Validation and nulls.** A candidate is retained if, on the proposal split, lift is at least 1.5 and count exceeds the maximum over 19 draws of every applicable null, and, on the confirmation split, lift is at least 1.5 with count at least 3. Nulls, all run, each reported. Gates (the count must exceed each one's maximum): per-type circular shift (each type's timestamps shifted by one independent offset, modulo the span); cycle shift (offsets in whole periods when a period exists, drawn DISTINCT across types from both directions so no two types keep their relative alignment). Attribute, not a gate: degree-preserving rewire (within each type, entity labels permuted across events; run when the entity count exceeds 1) is recorded per fragment as `binding_evidence` — whether its evidence is bound to the entity — because it is blind by construction to system-wide causes and uninformative when units run a synchronized schedule. A fragment records which nulls it survived. *(v1.0 amended: equal whole-period offsets preserved alignment and rejected planted mechanisms; the rewire gate rejected setpoint-to-heater.)*

**3.9 Model and scoring.** The predictive model is a multinomial logistic regression (L2, C = 0.5) over indicator features: Markov-1 and Markov-2 adjacent contexts within the entity stream plus one feature per retained context. Score = bits per event on the test split. Baselines, always all: unigram; interpolated-backoff Markov-1, -2 and -3 on the entity stream; Hawkes-like decay features (per type, exp(−gap/τ) over its most recent occurrence within the horizon, τ = the middle lag edge, fed to the same logistic model with no Markov or lag-class features); the same logistic model with Markov features only; the triviality library (3.11). Deterministic pairs (a type followed by one other type more than 95% of the time) are reported in a separate column and excluded from the headline figure.

**3.10 Library.** The retained contexts form the fragment library. Compositions (two retained contexts sharing a target, co-matched at or above the floor) are added as features only if they reduce confirmation bits. Library size is whatever the rules admit; no cap.

**3.11 Triviality baseline.** A name-free generic library of alternating pairs: two types within an entity stream whose merged subsequence strictly alternates (X Y X Y …) at least 90% of the time over at least 20 transitions — on/off and up/down partners whatever they are called — each at every lag class, fitted on each dataset with the same model. The pairs found are listed on the card. *(v1.0 amended: matching `on`/`off` and `up`/`down` by name found nothing on a name-scrambled dataset, which then beat the baseline for free.)* Every library score and every transfer score is reported as the gain over this baseline, not over the unigram. Structure that transfers but does not beat the triviality baseline is recorded as trivial.

**3.12 Transfer.** For an ordered pair (A, B): align A's and B's lagged-pair lift matrices (three lag classes, z-scored, equal proposal-split sizes) with signature-initialised Hungarian assignment refined to a fixed point, 20 restarts, dummy nodes for the size difference. Anchors: the two B types with the largest signature margin to their second-best A match are fixed. Then A's fitted model is applied to B's test split through the mapping (zero-shot bits), and a per-fragment mixture with B's own model is fitted on B's proposal split, with mixing weights per translated fragment. Report zero-shot bits, the learning-curve shift (bits on B's test split as a function of B's training days 1, 2, 3, 5, 10, 20, all), bits on B's types with no A counterpart (negative transfer), and the mapping accuracy when an answer key exists. The pair's cell in the matrix is the area between B's own learning curve and the mixed curve, in bit-days. **Role-level alignment (v4):** when types are spelled `role:symbol` in both datasets, alignment is between roles, not types: a role may map only to a role of the same symbol kind (quantile, turning point, binary) and, when tags exist, the same part of speech (falling back to the coarse speed class, then to the kind), so that symbols cross by their spelling — `up` stays `up`, `q80` stays `q80`, `peak` stays `peak`. Lift matrices are aggregated to role × role (mean over symbol pairs) and the Hungarian assignment, refinement and anchors run on those; TEP ↔ HAI shrinks from 186 × 190 types to 40 × 57 roles. **Control (v3):** the same source model is also applied through three permuted mappings (the same B types mapped, their A targets shuffled among them — within each part-of-speech class when tags exist, so the control keeps the grammar and loses only the word-level correspondence), mixed with the same weights; the control cell is the median of their areas, and the cell reported is the learned cell **net** of the control. A permuted mapping keeps the translated model's size and smoothness and loses only the correspondence, so whatever it gains is regularisation of a data-starved receiver, not shared structure — on the first cross-kind pair (TEP → HAI) the raw cell was 0.25 bit-days with a zero-shot of 8.9 bits, worse than the receiver's unigram, which is what prompted the control.

**3.14 Grammar: parts of speech and shapes (v4).** Before alignment, every role is tagged with a part of speech computed from its series alone, in dimensionless terms relative to the system's own horizon H: `SET` (piecewise constant: zero increments ≥ 90% of samples — schedules, setpoints, booleans), `TEX` (no detectable signal at the sampling scale, 3.2), otherwise a speed class from the ratio of correlation time to H (`FAST` < 0.1, `SLOW` > 1.0, else `MID`), with `-S` appended when the series sits at its minimum or maximum (within 1% of range) at least 5% of the time (limit-hitting, actuator-like). A role's tag is the majority over the units that carry it; tags are recorded in the sidecar. A fragment's **shape** is its type-free, tag-prefixed spelling — `MID.up.q80 -s-> MID.down.q20`, with a `[same role]` marker — and the library records each dataset's shape inventory. Tags and shapes are an added field: they do not revisit a dataset's entity or symbolization. *(Tried and dropped: a reversion feature from median-crossing recurrence relative to H — H is itself a recurrence time of threshold crossings, so every symbol-emitting series "reverts"; speed carries it.)*

**3.13 Growth and provenance.** After each dataset, the shared library is regrown: every fragment carries the dataset that first validated it, every dataset it was later confirmed in through a mapping, and every dataset where it was tested and failed. A fragment confirmed in a second family is marked inherited. The similarity tree is hierarchical clustering of the symmetrised matrix; the lineage is the inheritance graph, which is the only object the word phylogeny applies to.

## Benchmark card

Every dataset produces one card with exactly these fields, in this order. A field that cannot be filled is reported as `not measured`, never omitted.

| Field | Content | Why it is on the card |
| --- | --- | --- |
| Identity | name, source, span, time unit, entity chosen (3.1) and the runner-up with its bit gap, symbolization chosen per variable (3.2) | So the result can be reproduced and the two data-driven choices can be questioned |
| Scale | events per day, event types, entities, period found (3.4), signal floor (3.5) | Tells a reader before any result whether discoveries can be trusted at all |
| Headline bits | test-split bits per event: unigram, Markov-1/2/3, Hawkes, logistic with Markov features, logistic with library; deterministic pairs in a separate column; gain over the triviality baseline (3.11) | The only number that counts as the method's performance is the library row's gain over triviality |
| Library | fragment count, compositions kept, fraction surviving each null, share of fragments involving the chattiest 10% of types | The last field is the chatty-sensor check from building A |
| Recovery | when an answer key exists: fraction of known mechanisms present as validated fragments at the right lag class; fraction of validated fragments that are known mechanisms | Precision and recall against ground truth, both, never one |
| Transfer row | for every dataset already in the collection: zero-shot bits through the learned mapping, learning-curve area in bit-days, negative-transfer bits on unshared types, mapping accuracy where a key exists | One cell per existing dataset, in both directions |
| Lineage | fragments newly validated here; fragments inherited from earlier datasets and confirmed; fragments tested and failed | What this dataset added to, confirmed in, or removed from the shared library |
| Seeds | the seed; for synthetic datasets, a second-seed replication of the headline | A headline that fails to replicate is reported as failed |

The card is written by the pipeline, not by hand. Prose about a dataset goes after its card and may interpret but not restate it.

## Claim rules

A result is one of the following claims or it is not a claim. Each has a threshold fixed here so that the finding is read off the card, not argued.

| Claim | Condition | Reported as |
| --- | --- | --- |
| The method beats standard models on this dataset | library bits are at least 0.10 below the best baseline on the non-deterministic events, and the gain over the triviality baseline is at least 0.10 | "beats baselines by X bits" with the best baseline named |
| The method adds nothing here | the above fails | "no gain"; the dataset stays in the collection as a negative result |
| A mechanism is recovered | a validated fragment matches an answer-key mechanism in type and lag class | counted in the recovery field; individual fragments are never cited as findings outside that count |
| A fragment is trivial | it is in the triviality baseline, or transfers to every dataset with the same lift within 20% | labelled trivial; excluded from superfamily and universality statements |
| A transfers to B | zero-shot bits through the learned mapping are below B's unigram, and the learning-curve area is positive | one matrix cell; direction stated |
| A damages B | the mixed curve is above B's own curve at any training size on B's unshared types | reported with the same standing as a gain |
| A superfamily exists | hierarchical clustering of the symmetrised matrix yields a cluster whose within-cluster mean transfer is at least twice the between-cluster mean, with at least three members | named only by its members, never by a hypothesised common mechanism, until 5.9 |
| A fragment is inherited | validated in dataset A, confirmed in dataset B through the learned mapping with lift at least 1.5, where B is not in A's superfamily | the only basis for a cross-family statement |
| A motif has a function | the same shape (type-free pattern plus lag classes) is inherited across at least two superfamilies and beats triviality in each | the strongest claim the framework can make; stated with the shapes and the datasets, nothing more |

Two prohibitions. A statement about reality, systems in general, or universality is never made from fewer than three superfamilies. And a single dataset's result is never generalised beyond that dataset in any document produced by this method.

## Dataset admission and running order

A dataset is admitted when it has at least 20 days (or 20 natural periods) of events, at least 10 event types after symbolization, and a documented origin. Ground truth is welcome but not required; a dataset with an answer key fills the recovery field, one without leaves it `not measured`. Synthetic datasets are admitted only with their generator and are flagged as synthetic in every matrix view.

The first collection, in running order, with the role each plays:

| Order | Dataset | Kind | Role |
| --- | --- | --- | --- |
| 1 | Building A (this project) | synthetic, answer key | calibration: the card must reproduce the recorded result |
| 2 | Building B' (this project) | synthetic, answer key, role mapping to A | calibration of the transfer cell against the recorded zero-shot and curve |
| 3 | Tennessee Eastman process — first 120 days of the 1-year continuous run of Souza et al. (2023), Ricker's revised model; 3-min samples; the fault label is excluded from the events and kept as regime annotations; the answer key is the actuator→measurement pairs of the flowsheet | semi-natural, flowsheet as answer key, labelled faults | first real regulator; recovery and regime fields; days 120–365 held as a continuation |
| 4 | HAI 21.03 (in place of SWaT, which iTrust distributes on request only) — 1-minute means of the 1-s source; files concatenated with boundaries as gaps; attack labels as regimes; 15.3 days, admitted provisionally | real testbed, attacks as regime changes, point descriptions as answer key | second regulator; the first real transfer cell (3 ↔ 4) |
| 5 | A real building management log | real, no key | third regulator; first key-free card |
| 6 | Server or cluster telemetry (e.g. a public cluster trace) | real, no key | negative control: should not join the regulator superfamily |
| 7 | Clickstream or transaction log | real, no key | second negative control, different kind again |
| 8 | A biological regulation event series | real or simulated, partial key | the first test of transfer across a kind boundary |

The negative controls are not optional. A collection in which everything transfers to everything has failed the triviality baseline or the symbolization step, and the next action is to fix the instrument, not to report a universal.

Datasets 1 and 2 are run first on every change to the pipeline (section 7); their cards must match the recorded results within 0.02 bits before any other dataset is run.

## Fixed constants and change control

These are the only free numbers in the method. Each was set by the experiments recorded in RESULTS.md (A through H and the building tests); none is tuned per dataset.

| Constant | Value | Set by |
| --- | --- | --- |
| Lift threshold | 1.5 (proposal and confirmation) | building library runs |
| Null draws | 19 per null (p < 0.05 when the observed count exceeds all) | Experiments F, building runs |
| Confirmation minimum count | 3 | Experiment A |
| Debounce | 3 samples | building symbolization |
| Lag classes | horizon = median type recurrence time; three geometric bands from the time resolution to the horizon | Experiment G (coarse bins beat fine ones); Tennessee Eastman (density-set horizon too short) |
| Period detection | acf peak > 0.2, prominence ≥ 0.1, ≥ 8 repetitions, fundamental within 80% of the strongest; 0.1% bins | buildings (daily 1436 min recovered; weekly rejected as harmonic), Tennessee Eastman (none) |
| Faithfulness floor | reconstruction residual MAD ≤ 0.5 of the variable's MAD (std on the buildings; identical on Gaussian and AR(1) cores, 0.36 for q20/50/80) | building A symbolization; made robust on Tennessee Eastman |
| Noise floor | residual white noise ≤ 5% of signal variance after denoising; no signal if the window exceeds 1% of the length | Tennessee Eastman |
| Triviality pairs | alternation ≥ 0.9 over ≥ 20 transitions | buildings A and B′ |
| Logistic regularisation | L2, C = 0.5 | building runs |
| Splits | 50 / 25 / 25 by time | building runs (30 / 30 there; 50 / 25 / 25 generalises the confirmation idea) |
| Alignment | 20 restarts, 30 refinement iterations, 2 anchors by signature margin | Experiments B, G3, second-building test |
| Learning-curve points | 1, 2, 3, 5, 10, 20, all training days | second-building test |
| Claim thresholds | 0.10 bits; superfamily ratio 2; minimum members 3 | section 5 |
| Parts of speech | SET ≥ 0.9 zero increments; FAST < 0.1 and SLOW > 1.0 of correlation time / H; -S at ≥ 5% of samples on a limit | v4, set on TEP and HAI; to be checked on dataset 5 |
| Permuted-mapping controls | 3, same λ per curve point, median | v3 |

Change control is deliberately light. A change to any rule or constant gets one line in a changelog with the date and the reason. An implementation correction (the rule as written, now done right) keeps the version: datasets 1 and 2 are re-run and must reproduce their recorded cards within 0.02 bits. A change to a rule itself is a new integer version: the calibration reference is re-recorded and every card already in the collection is regenerated under the new version, so the matrix is never a mixture of methods; a card states the version it was produced under. The upper row of the pipeline (entity, symbolization) is never revisited for a dataset once chosen, whatever the version. A change confined to the collection step (3.12–3.13) increments the version and regenerates the matrix, not the cards, which remain valid from the version at which the per-dataset rules last changed. No other process, review or sign-off is required.

Versions: **v1** (2026-10-18) the method as first specified, with the implementation corrections listed above; **v2** (2026-10-19) horizon by recurrence time and geometric lag bands (3.3), after dataset 3; **v3** (2026-10-19) transfer cells reported net of a permuted-mapping control (3.12), after the first cross-kind cell; **v4** (2026-10-19) grammar: parts of speech, tagged shapes, role-level tag-constrained alignment (3.14, 3.12), after the cross-kind cells came out at chance.

Amendments under v1 (each has a changelog line; the buildings reproduce within 0.02 bits after each): 3.2 criterion, faithfulness floor and smoothing window; 3.4 resolution; 3.5 floor descriptive only; 3.8 cycle offsets distinct, rewire an attribute; 3.9 Markov-3 and decay baselines added; 3.11 name-free pairs. These are implementation corrections found on the two synthetic buildings, made before any real dataset was run, so the test split of no real dataset has been seen under more than one version.

Open items the method does not yet settle, listed so they are not mistaken for rules: type-level alignment (3.12) finds correspondences within a kind (buildings: learned mapping 3–5 bits better than permuted) and not across kinds (TEP ↔ HAI at chance; net cells 0.37 and 0.06), so cross-kind transfer needs alignment at the level of shapes (type-free fragment topology) rather than types — the v4 question; the triviality baseline (3.11) absorbs deterministic cross-variable couplings (HAI: 99 of 188 alternating pairs join different roles — command → position, setpoints stepping together), so a library that recovers the plant's couplings can still show no gain; whether such couplings are trivial is a definitional choice to make, and version, before dataset 5; fast-oscillation channels (vibration, rpm) need an envelope symbolization; online refitting during the test split (regime adaptation on real data); per-fragment transfer weights are specified (3.12) but were only run with a global weight on the second building; alignment currently uses each dataset's own lag terciles, which reduces comparability of the lift matrices (mapping accuracy 0.40 under v1 lags vs 0.60 under fixed lags on A→B′) — pooled lag classes for the pair are the likely fix; raised by Tennessee Eastman and settled in v2: the horizon and lag classes (3.3). Still open from it: an answer key should name only pairs whose effect is a target role under the chosen entity; vessel level was never predicted by anything. The period and entity rules have now met one semi-natural dataset (period: none, correctly; entity: vessel over plant).
