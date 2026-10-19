# Motif lab — Experiments A and B (2026-10-18)

Pure numpy/scipy, pure deterministic operators, no LLM in the loop. Everything
here is synthetic; treat it as a mechanism test, not evidence about natural data.

Reproduce: `python3 exp_a_modularity.py` (≈5 s), `python3 exp_b_alignment.py`
(≈3.5 min), `python3 plots.py`. Seeds are fixed; numbers below are exact.

## Shared generator (`worlds.py`)

- World = directed multigraph of (src, dst, relation) edges over 100 entities,
  10 relation types, 200 noise edges.
- Latent grammar = 8 two-edge fragments (a→b). Hidden structure = 6 planted
  four-edge chains (r1,r2,r3,r4), 3 instances each, entities drawn from the
  shared pool so planted chains interleave with noise.
- **Modularity knob m**: each target is, with probability m, a concatenation of
  two grammar fragments; otherwise a random chain that is *not* composable from
  the grammar. m=0 is the negative-transfer world; m=1 is the Exp 07 regime.
- A discovery world has ≈6,200 four-edge paths over ≈3,200 distinct type
  sequences, so a planted target (support ≥3) competes with hundreds of
  accidental sequences at the same support. Flat frequency ranking needs a
  budget in the low hundreds to find everything.
- Validation = support ≥ 3 in an independent confirmation world with the same
  targets. Coverage = fraction of planted targets verified within budget.

## Experiment A — the modularity dial

Memory is learned on 8 training worlds (all m=1) as the top-12 two-chains by
pooled log-lift, then frozen. Mean recall of the true 8-fragment grammar: 0.80.

Coverage of planted targets vs validation budget (30 seeds):

| budget | m | flat | within-world compose | learned | oracle | adaptive |
|---|---|---|---|---|---|---|
| 10 | 0.00 | 0.18 | 0.10 | 0.02 | 0.00 | 0.07 |
| 10 | 0.50 | 0.24 | 0.10 | 0.32 | 0.44 | 0.33 |
| 10 | 1.00 | 0.26 | 0.22 | 0.52 | 0.76 | 0.53 |
| 40 | 0.00 | 0.39 | 0.13 | 0.02 | 0.00 | 0.38 |
| 40 | 0.50 | 0.47 | 0.11 | 0.33 | 0.46 | 0.54 |
| 40 | 1.00 | 0.53 | 0.27 | 0.65 | 1.00 | 0.78 |
| 300 | 0.00 | 0.89 | 0.13 | 0.02 | 0.00 | 0.88 |
| 300 | 1.00 | 0.97 | 0.27 | 0.65 | 1.00 | 0.99 |

Full tables in `results_a.txt`; full curves in `results_a.json`; figures
`fig_a1_coverage_vs_budget.png`, `fig_a2_modularity_dial.png`.

What it shows:

1. **The advantage is a curve in m, not a yes/no.** At budget 10 the learned
   library's advantage over flat search rises roughly linearly from −0.16 at
   m=0 to +0.26 at m=1 and crosses zero near m≈0.35. This turns Exp 07's
   engineered win into a measured dose–response.
2. **Memory is what matters, not composition per se.** The hand-designed,
   memory-free baseline (compose the discovery world's own top-lift two-chains)
   is the *worst* method at every m. With 3 instances per target, a single
   world's two-chain statistics are too noisy to identify fragments; the
   cross-world library works because it amortises fragment evidence over
   8 worlds. This is the cleanest separation so far between "composition
   helps" and "remembered composition helps".
3. **Negative transfer is real and detectable.** At m=0 the frozen library finds
   nothing by construction (0.02). The adaptive policy (abandon the library
   after 5 consecutive unverified candidates) recovers flat performance at m=0
   (0.38 vs 0.39 at budget 40) and dominates everything except the oracle at
   m ≥ 0.5. A library that knows when to stop trusting itself is a stronger
   object than a library.
4. **The learned/oracle gap is library quality, not search.** Learned caps at
   0.65 coverage at m=1 because recall of the grammar is 0.80. Ablating library
   size K: recall 0.68/0.80/0.85/0.93 for K = 8/12/16/24; learned coverage at
   budget 40 = 0.48/0.65/0.74/0.78. Larger K buys recall at the cost of a bigger
   candidate space (K² compositions), so the budget-10 coverage peaks at K=16.
5. False positives (noise sequences that pass validation) are 2–3× higher for
   flat than for the library methods at budget 300 (≈40–64 vs ≈10–17 per
   world). Most are near-targets — chains sharing three edges with a planted
   target. Worth a "subsumption" check in the evaluator later.

Caveats: targets are chains only (no branching, no variable sharing beyond the
chain); noise is i.i.d.; the grammar has 8 fragments over 100 possible; the
confirmation threshold is a fixed count rather than a calibrated test; the
budget counts validations only, not preprocessing (path enumeration is far
cheaper for the compositional methods because they never enumerate the flat
candidate set, but that is not quantified here).

## Experiment B — cross-domain alignment ("translation")

Two domains with privately-named relation types; B's types are a hidden
permutation of A's. Each domain's "embedding" is its 10×10 pooled log-lift
matrix of two-chains. Translation = the permutation minimising
‖C_B − P C_A Pᵀ‖ with no paired data (signature-based Hungarian init, then a
MUSE-style self-learning refinement loop, 20 random restarts).

Accuracy of the recovered type mapping (chance 0.10, 30 seeds):

| m (grammar shared) | accuracy @ 32 worlds | exact mapping | shuffled control |
|---|---|---|---|
| 0.00 | 0.10 | 0% | 0.11 |
| 0.25 | 0.10 | 0% | 0.12 |
| 0.50 | 0.22 | 3% | 0.11 |
| 0.75 | 0.19 | 0% | 0.09 |
| 1.00 | 0.76 | 27% | 0.07 |

| worlds per domain (m=1) | 1 | 2 | 4 | 8 | 16 | 32 |
|---|---|---|---|---|---|---|
| accuracy | 0.13 | 0.10 | 0.13 | 0.23 | 0.45 | 0.73 |
| exact mapping | 0% | 0% | 0% | 0% | 3% | 33% |

What it shows:

1. **Zero-shot translation of relation types from structure alone works** —
   76% of types correctly mapped, a third of runs recovering the entire
   permutation, with the label-shuffled control at chance. Nothing in the
   method saw a paired example. This is a mechanism for the "shared language"
   intuition that is independent of everything in Exps 01–07.
2. **It is data-hungry.** Below ~8 worlds per domain there is no signal; the
   curve is still rising at 32. The two-chain lift matrix is a thin embedding
   (8 informative cells out of 100).
3. **Partial overlap is brittle — and the failure is optimisation, not
   absence of signal.** Accuracy collapses from 0.76 (m=1) to 0.19 (m=0.75).
   But the true permutation had a lower objective than the one found in 63%
   of those m=0.75 runs: the global quadratic-assignment search gets stuck
   when one or two private fragments add large residuals. A partial-matching
   formulation (seed-and-grow on the most confident type pairs, or a robust
   loss that discounts unmatched cells) is the obvious next step and would
   likely move the m=0.5–0.75 numbers substantially.

Caveats: 10 types is small (10! permutations, which is why restarts matter);
the embedding uses two-chain statistics only — adding three-chain or
composition-junction statistics would thicken it; the accuracy metric is
exact-type match, which punishes near-misses that would still be useful.

## Applications parking lot (do not pursue yet)

1. Automated, interpretable interaction-feature discovery for tabular models
   (Exp 02 audit + the library-vs-flat false-positive gap here).
2. Process/log mining with a frozen fragment library and an adaptive fallback.
3. Schema matching / data integration via structural alignment (Exp B *is* an
   unsupervised schema matcher; the partial-overlap fix is the enabling step).
4. Nimble as an ingestion layer: messy observations → typed primitives.

## Suggested next steps, in order

1. Exp B partial-overlap fix (seed-and-grow); re-run the m sweep.
2. Exp A with branching targets and shared variables, and with the budget
   accounting split into proposal cost vs validation cost.
3. Syntax-only transfer: worlds with a disjoint lexicon but the same
   composition grammar (chain-through-shared-variable rules), to isolate
   meta-level memory from object-level memory.
4. Only then: online memory updates within a world, with the KL shift in the
   proposal distribution as the measured quantity.

---

# Experiment C — does syntax transfer when the lexicon doesn't? (2026-10-18)

Files: `shapes.py` (generator + enumeration), `exp_c_syntax.py`, `plots_c.py`,
`results_c.json`, `results_c.txt`, `fig_c_syntax_transfer.png`. ≈80 s to run.

## Setup

- **Lexicon** = which relation types carry structure: a 6-type vocabulary out of
  R = 20. Training vocabulary V1 ⊂ {0..9}; the disjoint test vocabulary
  V2 ⊂ {10..19} shares no type with V1.
- **Syntax** = which abstract *shapes* hidden structures take. A shape is
  (topology, identity pattern over the four relation slots): four topologies
  (chain, fan-out, fan-in, shared-middle) × canonical patterns such as
  (0,1,0,2) = "first and third relations are the same type". 48 shapes exist.
  A shape says nothing about which types are involved, so it is the only kind
  of knowledge that *could* cross a disjoint lexicon. A world family's syntax
  S is 3 of the 48 shapes.
- Targets: 6 per world, shape drawn from S, pattern labels filled with distinct
  types from the vocabulary; 3 planted instances each; 260 noise edges over
  100 entities with all 20 types. A discovery world has ≈21,000 distinct motif
  keys; validation is support ≥ 3 in an independent confirmation world.
- Learner: flat discovery with budget 300 on 8 training worlds (S, V1);
  retained = validated motifs, ≈224 per seed of which 48 are planted (so 78%
  of what the learner sees is false positives, mostly near-targets). From the
  retained set it learns a *syntax* (shape statistics) and a *lexicon* (type
  statistics). Two syntax learners: a hard top-3 shape filter, and a soft
  prior = log-enrichment of each shape among retained motifs relative to its
  base rate among all candidates, added to log support when ranking.
- Test conditions, each a fresh discovery + confirmation pair, 30 seeds:
  **A** same syntax S, disjoint lexicon V2 (the question);
  **B** different syntax S′ (disjoint shapes), disjoint lexicon V2 (control);
  **C** same syntax, same lexicon V1 (reference).
  Size-matched control: 3 random shapes. Ceiling: the true S as a hard filter.

## Results (coverage of planted targets)

Condition A — same syntax, disjoint lexicon:

| budget | flat | syntax soft | syntax hard | random shapes | true syntax | lexicon only |
|---|---|---|---|---|---|---|
| 5 | 0.08 | **0.26** | 0.12 | 0.03 | 0.38 | 0.00 |
| 10 | 0.11 | **0.38** | 0.21 | 0.04 | 0.57 | 0.00 |
| 20 | 0.17 | **0.45** | 0.32 | 0.06 | 0.80 | 0.01 |
| 40 | 0.28 | **0.52** | 0.38 | 0.06 | 0.89 | 0.03 |
| 80 | 0.41 | **0.59** | 0.44 | 0.08 | 0.99 | 0.13 |
| 300 | 0.75 | **0.79** | 0.49 | 0.34 | 1.00 | 0.67 |

Condition B — different syntax, disjoint lexicon: soft syntax 0.09 / 0.19 /
0.47 at budgets 10 / 40 / 300 vs flat 0.11 / 0.29 / 0.77; hard filter 0.02–0.07.

Condition C — same syntax, same lexicon: lexicon only 0.27 / 0.63 / 1.00 at
budgets 10 / 40 / 300; soft syntax 0.39 / 0.58 / 0.83; flat 0.16 / 0.33 / 0.77.

## What it shows

1. **Yes — syntax transfers across a fully disjoint lexicon.** With zero
   overlapping relation types, a soft prior over learned shapes gives 3.5×
   flat's coverage at budget 10 (0.38 vs 0.11) and ~2× at budget 40, with
   non-overlapping standard errors, and never falls below flat at any budget.
   Size-matched random shapes are *worse* than flat (0.04 at budget 10), so
   the gain is from the learned content of the prior, not from filtering per
   se. This is meta-level memory, cleanly separated from object-level memory.
2. **The learned lexicon is worthless — and harmful — in the new lexicon**,
   as it must be: it ranks training-vocabulary candidates first, all of which
   are noise in V2 (0.00 at budget 10). Lexicon and syntax are now empirically
   distinct kinds of memory with opposite transfer profiles.
3. **Negative syntax transfer is real but the soft prior survives it.** A
   mismatched syntax as a hard filter is catastrophic (0.02–0.07 at every
   budget — worse than random shapes). As a soft prior it costs about a third
   of flat's coverage at mid budgets and the gap narrows with budget. The hard
   filter also caps at 0.49 in condition A because it keeps only half the true
   shapes; the soft prior has no cap. Shape knowledge should be a prior, never
   a gate.
4. **The learner, not the mechanism, is the bottleneck.** The true syntax as a
   prior reaches 0.57 / 0.89 / 1.00 at budgets 10 / 40 / 80 with no lexical
   knowledge at all — in this world family, knowing the *shape* of structure
   nearly solves discovery in an unfamiliar vocabulary. The learned prior gets
   roughly half of that gap because 78% of what it learns from is false
   positives. Stricter retention or lift-based weighting of retained motifs is
   the obvious lever, and it's engineering, not a new question.
5. **When the lexicon does transfer (C), it dominates** (1.00 at budget 300 vs
   0.83 for syntax) — type knowledge is more specific than shape knowledge.
   Combining them as two hard filters is wrong (`both_learned` inherits the
   cap); a soft combination is the obvious follow-up but wasn't the question.

## Caveats

- "Syntax" here is a distribution over 48 motif shapes — an abstraction over
  topology and type-repetition, not a compositional rule system. It is
  type-free and transferable, which is what the question needed, but it is
  not a grammar in the generative sense. Rediscovering a closed composition
  table (Allen-style) remains the stronger syntax test.
- The value of a shape prior depends on how surprising its shapes are under
  noise: all-distinct patterns dominate random candidates (≈85% of keys), so a
  syntax made of those prunes little, while repeated-type or asymmetric shapes
  prune a lot. Per-seed variance in the curves is partly this.
- Same simplifications as before: i.i.d. noise, fixed count threshold for
  validation, validation-only cost accounting, chains/fans of 4 edges.

## Direction

The fork resolved toward the stronger branch: there is a type-free layer of
structural knowledge that transfers where the vocabulary does not. That makes
Question 2 (is the library worth its weight in bits — MDL amortisation) the
right next measurement, applied to *both* layers separately: a lexicon's bits
and a syntax's bits should amortise over different sets of worlds.

---

# Experiment D — is the library more than the sum of its parts, in bits? (2026-10-18)

Files: `exp_d_mdl.py`, `plots_d.py`, `results_d.json`, `results_d.txt`,
`fig_d_mdl.png`. ≈45 s to run.

## The criterion

Two-part MDL. A library L earns its keep over N worlds iff

    L(library) + Σ_k L(structure_k | library)  <  Σ_k L(structure_k | base)

Reported per library: one-off cost (bits), savings per held-out world, the
break-even N* = cost / savings, and net bits at N = 8. Every code is a real
prefix code with uniform symbol costs and 8-bit quantised escape probabilities;
library size is chosen by minimum training code length, so a library cannot
grow for free. Libraries are learned from *retained* motifs on 8 training worlds
(flat discovery, validated — 78% false positives, as before); savings are
measured on the *planted* structure of 8 fresh worlds. The question is therefore
whether a learned library compresses the generative structure of worlds it has
never seen.

Three memories, three codes:

| memory | model | base code | library code |
|---|---|---|---|
| fragment library (Exp A worlds, chains, R=10) | F two-chains, escape γ | 4 log₂R = 13.3 bits | per composition pair: in-lib −log₂γ + log₂F, else −log₂(1−γ) + 2 log₂R |
| type lexicon (Exp C worlds, R=20) | vocabulary V, in-vocab α | 2 + 4 log₂R = 19.3 bits | per type: in-V −log₂α + log₂|V|, else escape |
| shape syntax (Exp C worlds) | shape set S of 48, in-S β | same | shape under S-code + n_distinct(shape) · log₂R — repeated slots are free |

## Part 1 — fragment library across the modularity dial

| m | learned F | lib cost | savings / world | break-even N* | net @ 8 | seeds net>0 | closure cov (learned / random) |
|---|---|---|---|---|---|---|---|
| 0.00 | 1.6 | 14 | −0.7 | ∞ | −20 | 0% | 0.00 / 0.000 |
| 0.25 | 3.8 | 29 | −0.3 | ∞ | −31 | 0% | 0.03 / 0.005 |
| 0.50 | 10.8 | 59 | +3.5 | 16.7 | −31 | 13% | 0.25 / 0.019 |
| 0.75 | 13.9 | 68 | +11.5 | 5.9 | +24 | 73% | 0.57 / 0.024 |
| 1.00 | 16.6 | 75 | +20.7 | 3.6 | +91 | 100% | 0.89 / 0.038 |

Base = 79.7 bits per world (6 chains). Oracle (true 8-fragment grammar, same
two-part cost): savings −67.6 / −38.9 / −13.5 / +15.9 / +43.5 bits per world.

## Part 2 — lexicon vs syntax, same-lexicon vs disjoint-lexicon held-out worlds

Base = 115.7 bits per world (6 motifs). Learned |V| = 5.9 (recall 0.99),
learned |S| = 9.5 (recall of the 3 true shapes 0.96).

| library | cost | savings/world, same lexicon | N* | savings/world, disjoint lexicon | N* |
|---|---|---|---|---|---|
| lexicon | 27.5 | +37.8 | 0.7 | **−72.8** | ∞ |
| syntax | 44.3 | +28.8 | 1.5 | **+28.7** | 1.5 |
| both | 71.8 | +52.0 | 1.4 | −16.1 | ∞ |
| lexicon (oracle) | 27.6 | +41.3 | 0.7 | −141.6 | ∞ |
| syntax (oracle) | 27.7 | +42.7 | 0.6 | +42.7 | 0.6 |

All same-lexicon libraries are net positive at N=8 in 100% of seeds; the
disjoint-lexicon lexicon library is net positive in 0%.

## What it shows

1. **Yes, in bits, with a sign that depends on m.** The learned fragment
   library pays for itself in 3.6 worlds at m=1 and 5.9 at m=0.75, saves
   nothing at m ≤ 0.25, and MDL selection correctly shrinks it to near-empty
   (F ≈ 2) when there is nothing to amortise. The crossover sits between
   m=0.5 and 0.75 at N=8 — the same region where the discovery advantage
   crossed zero in Exp A. Two independent measures of "is composition real
   here" agree on where the line is.
2. **The parts produce wholes they do not contain.** At m=1, 89% of held-out
   planted 4-chains lie in the compositional closure of the learned 2-chain
   library, against 3.8% for a random library of the same size. No 4-chain is
   in the library; the closure is generated. This is the generative
   compositional-generalisation test, and it passes with a 23× margin.
3. **Syntax bits are portable; lexicon bits are local.** The shape syntax
   saves the same 28.7 bits per world whether or not the held-out vocabulary
   overlaps training — it is type-free, so it cannot tell the difference. The
   lexicon saves 37.8 bits per world on its own vocabulary and *costs* 72.8
   per world on a disjoint one, because every escape is more expensive than
   the base code. This is the MDL counterpart of Exp C: the two layers amortise
   over different sets of worlds, which is what makes them different kinds of
   memory rather than two features of one library.
4. **Confidence is a liability under distribution shift.** The oracle lexicon
   (α = 0.99) loses 141.6 bits per world on a disjoint vocabulary, twice the
   learned lexicon's loss (α fitted from contaminated data, hence hedged). An
   oracle fragment grammar is dead weight at m ≤ 0.5 while the learned library
   is merely useless. The library's escape probability is a calibration
   parameter, and a library that believes itself too much transfers worse.
5. **MDL is a better learner than top-k.** Exp C's top-3 shape heuristic
   recovered 0.48 of the true syntax; MDL-selected syntax recovers 0.96 (at
   |S| ≈ 9.5, absorbing a few near-target shapes as the price). The
   learner-quality bottleneck from Exp C has an off-the-shelf fix: select the
   library by code length, not by count.

## Caveats

- Savings are measured on the planted structure (6 motif types per world),
  not the raw edge list. The absolute bit savings carry over unchanged to a
  full-world code (noise edges and instance positions cost the same under both
  codes), but as a *fraction* of the full world they are small, because the
  structure is a small fraction of the data. The claim is about the structure.
- Codes are deliberately simple (uniform symbol costs, fixed escape
  probabilities). An adaptive or prequential code would compress more under
  both base and library; the comparison, not the absolute level, is the result.
- "Both" is coded as independent layers; a joint code that conditions types on
  shape would do better and is where any shape–type interaction would show.
- Same synthetic simplifications as A–C.

## Where this leaves the programme

Four of the five original "not supported yet" items now have a measured
answer at the mechanism level: a library changes what is discoverable under
budget (A), with an advantage that tracks true compositionality (A, D); a
type-free layer of structural knowledge transfers across disjoint vocabularies
(C) and is worth its weight in bits exactly where the type layer is not (D);
composition generates held-out structure the parts don't contain (D). Still
open: online adaptation within a world (Q3/temporal), survival under stronger
null models (Q4), and anything on natural data.

---

# Experiment C2 — Experiment C with the MDL-selected syntax learner (2026-10-18)

Files: `exp_c2_syntax_mdl.py`, `results_c2.json`, `results_c2.txt`. Same
worlds, seeds, conditions and budgets as Experiment C; adds the MDL-selected
shape set from Experiment D (hard filter and soft prior), and a soft
combination of MDL syntax + MDL lexicon.

Condition A — same syntax, disjoint lexicon (coverage):

| budget | flat | hard top-3 (C) | soft enrichment (C) | MDL hard | MDL soft | true syntax |
|---|---|---|---|---|---|---|
| 10 | 0.11 | 0.21 | **0.38** | 0.17 | 0.34 | 0.57 |
| 40 | 0.28 | 0.38 | **0.52** | 0.38 | 0.49 | 0.89 |
| 150 | 0.55 | 0.48 | 0.64 | **0.71** | 0.64 | 0.99 |
| 300 | 0.75 | 0.49 | 0.79 | **0.82** | 0.78 | 1.00 |

Condition C — same syntax, same lexicon: soft combination of MDL syntax and
MDL lexicon = 0.46 / 0.69 / 0.99 at budgets 10 / 40 / 300, vs lexicon alone
0.27 / 0.63 / 0.99 and syntax alone 0.39 / 0.53 / 0.85 — the best learned
method wherever both layers apply, and it degrades correctly to 0.07 at budget
10 in condition A where the lexicon is foreign.

Condition B — mismatched syntax: MDL soft prior 0.12 at budget 10 (flat 0.11),
0.51 at 300 (flat 0.77). Nearly harmless when wrong at low budget; costly at
high budget. Hard filters remain catastrophic (0.02–0.13).

## What changed, and what didn't

1. **The cap is gone.** The MDL-selected set (|S| ≈ 9.5, recall 0.92) as a
   hard filter reaches 0.82 at budget 300 where the top-3 filter stalled at
   0.49, and it is the best method from budget ~100 up.
2. **The low-budget result did not move.** The standing number for the
   syntax-transfer question stays at 0.38 vs 0.11 at budget 10 (soft
   enrichment prior). The MDL prior is slightly worse there (0.34). I
   predicted MDL would close much of the gap to the ceiling; it did not.
   Recall was the wrong proxy for a ranking prior: the MDL code spreads mass
   uniformly over its ~9.5 shapes, so the ~6 near-target shapes it admits
   dilute the 3 true ones, whereas the enrichment prior uses the retained
   counts directly, which concentrate on the true shapes. For *selection*
   (which shapes to keep) MDL is right; for *weighting* (how much to trust
   each) counts are. The remaining gap to the oracle is weight concentration,
   not set membership.
3. **Soft combination works.** Two priors added in log space beat either alone
   where both apply and fail gracefully where one doesn't, which the hard
   `both` filter in C could not do.

Standing Experiment C result, unchanged: a type-free shape prior learned from
contaminated discoveries gives 3.5× flat's coverage at budget 10 on a world
with no shared relation types; random shapes of equal size are worse than
flat; a mismatched syntax hurts. What C2 adds is a high-budget method with no
cap and a working two-layer combination.

---

# Experiment E — regime switching with online memory: does the system learn to learn? (2026-10-18)

Files: `temporal.py` (generator, time-respecting enumeration, time-shuffle
null), `exp_e_regimes.py`, `plots_e.py`, `calib_temporal.py`,
`results_e.json` / `results_e.txt` (budget 40), `results_e_b15.json` /
`results_e_b15.txt` (budget 15), `fig_e_regimes.png`. ≈45 s per budget.

## Calibration finding: time collapses the candidate space

Same events, same 6 planted 4-chains (3 instances each), R = 10:

| noise events / 100 time units | distinct 4-chains, static | distinct 4-chains, time-respecting | flat budget to find all 6 |
|---|---|---|---|
| 200 (the A–D density) | 3,283 | 16 | 5 |
| 1,200 | 10,000 (saturated) | 173 | 8 |
| 3,200 (used here) | — | 2,939 | ~103 |
| 4,000 | — | 5,280 | ~318 |

Requiring events to occur in order within a window (span 6, mean lag 1)
removes ~99.5% of candidates at the old density; flat search becomes trivial
and memory cannot matter. Temporal structure discovery is only hard in a dense
regime — many events per lag scale — so Experiment E runs at 16× the old
event rate. This is the "direction comes for free" prediction, quantified,
and it already says something about where this machinery would earn its keep
on real event data: high-rate streams, not sparse ones.

## Setup

- Stream of K = 10 epochs; each epoch has its own 6 target chains (never
  reused across epochs), so every boundary is a real regime switch.
- Three stream types: **modular** — every epoch's targets are fresh
  compositions of one shared 8-fragment grammar (m = 1); **novel** — random
  non-composable chains every epoch (m = 0); **alternating** — m = 1, 0, 1, 0, …
- Each epoch splits in two halves. Discovery uses the first half; validation
  is **prequential** on the second half (time-respecting support ≥ 3). No
  separate confirmation world — the future is the held-out data.
- Null model: the second half with timestamps permuted (graph unchanged).
  Flat search recovers 0.2–0.6% of planted targets against it, confirming the
  structure found is temporal, not just topological. Flat false positives:
  0.2–0.7 per epoch.
- Methods, each with budget B validations per epoch:
  *flat* (no memory); *online library* (MDL-selected fragment library re-fit
  after every epoch from everything verified so far; composed candidates
  first, flat fallback after 5 misses); *library + trust bandit* (a two-armed
  bandit chooses at each validation between the composed and flat lists from
  Beta posteriors on their hit rates, discounted at each epoch start — a
  running belief about m); *decaying library + bandit* (library fit with
  half-life 2 epochs: motif retirement).

## Results (coverage of the current epoch's targets; 30 seeds)

Budget 15:

| stream | method | k=0 | k=2 | k=4 | k=6 | k=8 | k=9 | mean |
|---|---|---|---|---|---|---|---|---|
| modular | flat | 0.48 | 0.54 | 0.55 | 0.62 | 0.47 | 0.50 | 0.53 |
| modular | online library | 0.52 | 0.61 | 0.84 | 0.91 | 0.93 | 0.91 | **0.77** |
| modular | library + bandit | 0.50 | 0.61 | 0.81 | 0.88 | 0.89 | 0.90 | 0.75 |
| modular | decaying + bandit | 0.51 | 0.57 | 0.75 | 0.84 | 0.88 | 0.91 | 0.72 |
| novel | flat | 0.51 | 0.44 | 0.49 | 0.43 | 0.49 | 0.54 | 0.48 |
| novel | online library | 0.52 | 0.48 | 0.51 | 0.44 | 0.49 | 0.52 | 0.48 |
| alternating | flat | 0.48 | 0.58 | 0.54 | 0.51 | 0.51 | 0.51 | 0.51 |
| alternating | online library | 0.52 | 0.54 | 0.56 | 0.58 | 0.62 | 0.43 | 0.51 |
| alternating | library + bandit | 0.50 | 0.56 | 0.53 | 0.60 | 0.66 | 0.41 | 0.51 |

Library size after epoch k (online library, modular stream): 0.3, 4.3, 6.2,
7.7, 7.7, 7.9, 7.9, 8.0, 8.0, 8.0 — it converges on exactly the 8 true
fragments. On the novel stream it is 0 at every epoch. Budget 40 shows the
same pattern with a smaller gap (modular mean 0.86 vs flat 0.73).

## What it shows

1. **The system learns to learn.** On the modular stream, recovery after a
   switch rises from 0.52 at the first epoch to 0.91–0.93 by the sixth, while
   flat search stays at 0.53 ± 0.05 throughout. Each switch is a brand-new
   target set; what improves is the system's ability to find new structure,
   because its memory has accumulated the grammar those structures are built
   from. This is claim (c) — learned structure changing subsequent discovery —
   in its strongest form, online, with the switches as the clock. The
   Kashtan–Alon result transposed from evolved circuits to discovery.
2. **Nothing is learned when there is nothing to learn, at no cost.** On the
   novel stream the MDL library is empty at every epoch (no fragment set beats
   the base code on random chains) and all memory methods track flat search
   within noise. Negative transfer under novel switching is absent because
   MDL selection refuses to build a library — a cheaper safeguard than the
   bandit or the fallback.
3. **Memory converges on the generator.** Library size settles at 8.0 = the
   true grammar size, with coverage ~0.9 at a budget where flat gets 0.5.
   The vocabulary is compact, correct, and learned from prequentially
   validated discoveries only.
4. **Alternation exposes a design split: content vs trust.** On the
   alternating stream the persistent library wins on modular epochs once
   enough have been seen (0.62–0.66 vs 0.51 at k=8) but loses on novel
   epochs (0.41–0.43 vs 0.51 at k=9): it keeps trusting composition for a
   few validations into a novel regime. The decaying library has the
   opposite profile — matches flat on novel epochs, but forgets the grammar
   during them and underperforms on the modular epochs that follow. Net, all
   methods tie flat on average. The right architecture is a *persistent*
   content memory with a *fast-switching* trust signal: the bandit's
   per-epoch discount (0.5) is too slow at budget 15 to re-learn the regime
   within the epoch. Retirement of content is the wrong tool for a world that
   comes back; what should be forgotten quickly is confidence, not
   vocabulary. This separates the two dynamic-memory states your protocol
   had lumped together.

## Caveats

- Lags are not yet part of the vocabulary: motifs are typed by relation
  sequence only, and time enters only as an ordering/window constraint. Lag-
  typed motifs (and the lag-signature fix for Exp B) are the next temporal
  layer.
- Epochs are equal length, switches are clean and synchronous, and the
  discovery/validation split is at the epoch midpoint — a kind and known
  change-point. Detecting the switch is itself a problem not posed here.
- Noise is uniform in time (no periodicity), so the time-shuffle null is the
  only temporal null applied. A cycle-preserving shuffle is still needed
  before any claim on periodic data.
- Same simplifications as before: chains only, fixed support threshold,
  validation-only cost accounting.

## Where this leaves the programme

Online adaptation — the last of the mechanism-level "not supported yet" items
from the original document — now has a positive result with its controls.
The dynamic-memory question you deferred has a first answer: content should
persist, trust should decay. Still open: stronger null models (periodicity,
degree-preserving rewiring), lag-typed vocabulary, change-point detection,
and natural data — which, on the calibration finding, should be a dense event
stream.

## Applications parking lot (additions)

5. Dense event streams — logs, transactions, telemetry, clickstreams — are
   the regime where temporal motif memory pays off; sparse event data is
   already easy for flat search.
6. Regime-aware monitoring: an online library whose MDL size collapses is a
   change detector for "the process stopped being compositional"; the trust
   bandit's arm preference is a cheap regime indicator.

---

# Experiments F, G, H — null models, lag vocabulary, change-point detection (2026-10-18)

Files: `temporal.py` (extended: hubs, periodic bursts, lag classes, three
nulls), `exp_f_nulls.py` / `results_f.*`, `exp_g_lags.py` / `results_g.*`,
`exp_h_changepoint.py` / `results_h.*`, `plots_fgh.py`, `fig_fgh.png`.
20 seeds each. F ≈ 25 min (19 shuffles × 3 nulls per validation); G ≈ 10 min;
H ≈ 30 s.

## F — null-model audit

Generator additions: Zipf(0.6) entity activity (hubs); 80% of noise events
inside 1-time-unit bursts every 10 time units (periodicity). Nulls, each
keeping every (src, dst, rel): time-shuffle (permute timestamps), cycle-shuffle
(permute within phase bin), rewire (degree-preserving endpoint swaps). A
candidate passes a null if its second-half support exceeds the maximum over 19
shuffles. Top-100 candidates by support from the discovery half.

| noise | rule | TPR | FP | survival of count-verified |
|---|---|---|---|---|
| plain | count ≥ 3 | 0.92 | 1.2 | — |
| plain | rewire+cycle | 0.88 | 2.7 | 0.90 |
| periodic | count ≥ 3 | 0.97 | 2.0 | — |
| periodic | rewire+cycle | 0.88 | 2.2 | 0.89 |
| hubs | count ≥ 3 | 0.77 | 8.3 | — |
| hubs | rewire-null | 0.52 | 4.3 | 0.51 |
| hubs | rewire+cycle | 0.26 | 1.9 | 0.26 |
| hubs+periodic | count ≥ 3 | 0.95 | 12.4 | — |
| hubs+periodic | rewire+cycle | 0.46 | 2.0 | 0.20 |

Planted targets reaching the top-100 at all: 0.90 (plain), 0.94 (periodic),
0.30 (hubs), 0.29 (hubs+periodic). Ranking by excess over rewired-null mean
does not improve this (0.32 / 0.26); neither do z-score or lift rankings
(0.25 / 0.35 at 3 instances) — the null estimate from a few rewirings is too
noisy to beat raw support as a ranking statistic.

Experiment E re-scored (modular stream, budget 15, hubs+periodic noise):

| planted instances / half | validation | mean cov | cov k=0 → k=9 | FP / epoch | library size | purity |
|---|---|---|---|---|---|---|
| 3 | count | 0.05 | 0.05 → 0.05 | 1.7 | 0.0 | — |
| 3 | rewire+cycle | 0.02 | 0.02 → 0.01 | 0.3 | 0.0 | — |
| 5 | count | 0.28 | 0.20 → 0.32 | 2.8 | 5.1 | 0.85 |
| 5 | rewire+cycle | 0.24 | 0.16 → 0.32 | 0.4 | 6.9 | 0.86 |

What it shows:

1. **Everything in A–E was scored against uniform noise, and uniform noise is
   kind.** Under plain or periodic noise the count rule is already well
   calibrated (1–2 false positives, ~90% survival under the strongest null),
   so the nulls change nothing there. Periodicity at this density did not
   manufacture spurious temporal motifs — the burst events still spread over
   10⁴ relation sequences.
2. **Hubs are the real adversary.** Degree heterogeneity inflates support for
   thousands of chains: the count rule's false positives rise to 8–12 per
   epoch half, and three-quarters of its "discoveries" fail the
   rewire+cycle null. More importantly, planted structure at 3 instances no
   longer reaches the candidate list at all (0.30), so the Experiment E
   pipeline collapses outright (coverage 0.05, no library ever forms). This
   is not a validation failure; nothing gets proposed. Null-based validation
   cannot rescue what the ranking never surfaces.
3. **The fix is signal, not statistics.** At 5 instances per target the
   planted structure returns to the candidate list (0.97 in the top-100), the
   E pipeline recovers a rising learning curve (0.20 → 0.32) and builds an
   85%-pure library under both rules. The null-calibrated rule cuts false
   positives 7× (2.8 → 0.4 per epoch) at a cost of ~0.04 coverage, while
   library purity is unchanged — MDL selection was already filtering the
   false positives out of memory. Under hubs the method has a signal floor
   (~5 instances per window rather than 3), and the honest statement for
   real data is: estimate that floor before trusting any discovery.
4. The strong null is conservative at low signal: with planted support ≈3 and
   hub-driven null support of comparable size, rewire+cycle rejects 3 in 4
   true targets. Power, not just false-positive control, has to be reported.

## G — lag as part of the vocabulary

Grammar fragments carry a lag class (short ≈ 0.4 or long ≈ 3.5 time units,
Gamma(4)); a lag-typed key is (relation sequence, lag-bin sequence). Span
raised to 10 to admit long lags, which makes every condition harder than E.

G1, same events keyed two ways (plain noise, 3 instances; hubs, 5):

| cond | keying | distinct keys | count-rule FP in top-100 | TPR in top-100 |
|---|---|---|---|---|
| plain | lag-blind | 5,037 | 13.8 | 0.55 |
| plain | lag-typed | 7,164 | **0.9** | 0.48 |
| hubs | lag-blind | 8,769 | 54.0 | 0.34 |
| hubs | lag-typed | 20,928 | **8.1** | 0.19 |

G2, Experiment E modular stream (budget 15, span 10), mean coverage over 10
epochs: flat lag-blind 0.22; flat lag-typed 0.15 (soft validation 0.17);
library lag-blind 0.30; library lag-typed 0.22 (soft 0.26). All library
curves rise with epochs (lag-typed soft: 0.20 → 0.42, matching lag-blind's
0.40 by the last epoch); learned library size 5.7–5.8 for all.

G3, cross-domain alignment (Experiment B) with lift-only vs lift + mean-lag
signatures: at the dense E density both are at chance for every data size
(pairwise statistics are swamped). At sparse density (300 noise events per
segment): lift-only 0.11 / 0.21 / 0.51 / 0.75 at 2 / 4 / 8 / 16 worlds;
lift+lag 0.17 / 0.29 / 0.55 / 0.72.

What it shows:

1. **Lag typing is a precision tool.** Splitting support across lag patterns
   cuts validated false positives 15× under plain noise and 7× under hubs,
   at a modest recall cost (TPR 0.55 → 0.48). Noise does not have a
   consistent lag signature; structure does.
2. **At 3 instances it costs discovery under a tight budget.** Lag-typed
   keys dilute planted support (each bin misclassification removes an
   instance from the exact key), enlarge the candidate space, and make the
   count threshold harder to clear. Soft validation (summing patterns within
   one bin flip) recovers most of the gap and the lag-typed library ends the
   stream level with the lag-blind one. The lag-typed library is learnable
   and composes correctly — the mechanism works — but at this signal level
   there is no discovery gain to show, only a false-positive reduction.
3. **The alignment prediction was mostly wrong.** Lag signatures add a small
   gain at very low data (+0.06–0.08 at 2–4 worlds) and nothing at 8–16. The
   real improvement over Experiment B came from somewhere else:
   time-respecting 2-chain counting is cleaner than static counting, so
   lift-only alignment now reaches 0.75 at 16 worlds where the static
   version needed 32. And in dense streams pairwise alignment fails entirely;
   translation there will need longer-motif signatures.

## H — change-point detection on regimes of unknown length

Alternating modular/novel regimes of geometric length (mean 2.9 epochs,
range 1–6) over 20 epochs; new targets every epoch; budget 15.

| method | cov, modular epochs | cov, novel epochs | cov, all | detection delay (epochs) | false alarms / 20 |
|---|---|---|---|---|---|
| flat | 0.54 | 0.48 | 0.51 | — | — |
| persistent library (patience 5) | 0.74 | 0.41 | 0.59 | — | — |
| library + bandit (discount 0.5) | 0.76 | 0.40 | 0.60 | 0.47 | 0.30 |
| detector (hit-rate thresholds, probe 3) | 0.68 | 0.42 | 0.57 | 0.30 | 0.35 |
| detector + gated memory writes | 0.66 | 0.43 | 0.56 | 0.32 | 0.40 |

What it shows:

1. **Detection is fast and nearly free; it just doesn't buy much.** Every
   adaptive method identifies a grammar switch within the epoch it happens
   (delay 0.3–0.5 epochs — usually inside the first few validations). The
   explicit detector is fastest (0.30) but its advantage over the bandit is
   within noise, and false alarms are 1.5–2 per 100 epochs for all.
2. **The novel-regime cost is the price of looking, not of slow detection.**
   Every memory method loses 0.05–0.08 on novel epochs relative to flat, and
   the loss is the same for the detector as for the patience fallback: 3–5
   of 15 validations spent confirming that composition no longer applies.
   The E conclusion stands — trust must switch within the epoch — but the
   gain available from a smarter switch is bounded by the probing cost, and
   the plain persistent-library-with-patience method is as good as anything
   fancier (0.59 vs 0.60 vs 0.57).
3. **Gating memory writes by regime belief adds nothing** (0.56 vs 0.57).
   MDL selection already keeps novel-regime motifs out of the library, as
   the empty libraries on E's novel stream showed. Content memory does not
   need protecting; it protects itself.

## Standing conclusions after F/G/H

- The mechanism results (A–E) hold under harder noise, at a higher signal
  floor: with hubs, expect to need ~5 instances per discovery window, not 3,
  and expect raw ranking — not validation — to be the limiting step.
- Report power alongside false-positive control: the strongest null rejects
  most true structure at the signal floor.
- Lag classes belong in the vocabulary for precision; use soft matching for
  recall; do not expect a discovery speed-up from them at low signal.
- Regime changes are detected within the epoch by any of the methods; the
  simplest (persistent library, patience fallback) is sufficient. The design
  principle "content persists, trust adapts" is confirmed, with the caveat
  that trust adaptation is bounded by the probing budget.
- Pairwise alignment needs sparse data; dense streams need motif-level
  signatures.

## Applications parking lot (additions)

7. A signal-floor estimator (how many instances per window a stream needs
   before discoveries are trustworthy under its own degree distribution) is
   the first thing to run on any real event log — before any motif mining.
8. Lag-typed motifs as a precision filter for alert/anomaly pipelines, where
   false positives are the dominant cost.

---

# Semi-real benchmark dataset — small office building (2026-10-18)

Folder `dataset/`: `simulate_building.py`, `symbolize.py`, `baselines.py`,
`building_1min.csv.gz`, `building_events.csv`, `sim_params.json`,
`GROUND_TRUTH.md`, `baselines.txt`, `fig_sample_day.png`.

Three zones with identical heater/ventilation control loops, real delays,
daily and weekly cycles, a five-step cascade spanning both loops, a zone that
comes online at day 30, a damper fault in zone B on days 40–49, a chatty
unrelated sensor, dropouts. Full mechanism list and benchmark definition in
`GROUND_TRUTH.md`.

Baseline result that sets the bar: a zone-context order-2 Markov model
reaches 2.49 bits/event (3.14 on non-heater events); the same model on the
interleaved building stream gets 3.97 — entity binding alone is worth 1.5
bits. Longer context overfits; adding building-wide events to the context
makes the Markov model worse (2.90) because the chatty sensor pushes real
causes out of its window. Those two facts are the room: selective,
lag-aware binding of building-wide triggers, and regime adaptation on the
fault. The bar to beat is stated explicitly in `GROUND_TRUTH.md`.

---

# Application test — the library on the building event log (2026-10-18)

Files in `dataset/`: `run_library.py`, `library_results.txt` / `.json`
(seed 7), `library_results_seed8.txt` / `.json` (seed 8, an independent
instance of the building). ≈5 s per run.

## Mapping

| synthetic world | building |
|---|---|
| entity | zone (A, B, C); building-wide events are context for every zone |
| atom | (zone, variable:event, minute) |
| fragment | lagged pair (prior event, lag class s/m/l) → next event |
| composition | two fragments with the same target, both matched |
| validation | proposed on days 0–19, confirmed on days 20–29; must beat a per-type circular-shift null (19 shifts) |
| library size | chosen by prequential log-loss on the confirmation days |
| memory → use | library contexts as features of a multinomial logistic model; the same model with only adjacent Markov-1/2 features is the control |

Scoring is the benchmark's: event type of each zone event given its zone,
train days 0–29, test days 30–59, bits per event.

## Results

Seed 7 (5,964 test events):

| model | all | zone B fault | zone C cold start | non-heater | features |
|---|---|---|---|---|---|
| Markov-2 count model (benchmark bar) | 2.621 | 2.606 | 2.263 | 3.477 | — |
| logistic, Markov features only | 2.324 | 2.343 | 1.950 | 3.036 | 420 |
| + library fragments (39 selected) | **1.845** | **1.961** | 1.478 | **2.458** | 459 |
| + compositions (162) | 1.841 | 1.965 | 1.410 | 2.454 | 596 |
| all lagged contexts, no selection (74) | 1.805 | 1.951 | 1.458 | 2.414 | 494 |

Seed 8 (6,356 test events): bar 2.300 / 2.934 non-heater; Markov features
2.169 / 2.734; + fragments **1.655 / 2.117**; + compositions 1.632 / 2.100;
unselected 1.587 / 2.040.

## What it shows

1. **It beats the bar, by a lot, on both seeds.** Against the strongest
   Markov model the library representation saves 0.6–0.8 bits per event
   overall and ~1 bit on non-heater events (3.48 → 2.46; 2.93 → 2.12) — a
   25–30% reduction in held-out code length. Against the fair control (the
   same logistic model with adjacent-Markov features only, which is already
   better than the count model) the saving is 0.45–0.5 bits. The gain holds
   on the fault regime and on the cold-start zone. The benchmark's primary
   criterion is met and replicated.
2. **What wins is the representation, not the selection.** The decisive
   ingredients are the ones the synthetic programme identified: binding by
   entity, building-wide triggers attached to every zone, lag classes, and
   contexts that skip intervening events. Using *every* lagged context with
   count ≥ 5 — no lift threshold, no null, no prequential confirmation — is
   0.04–0.07 bits *better* than the selected library. A regularized
   discriminative model on 6,000 events does not need the filter; it learns
   near-zero weights for the vibration channel on its own. The filtering
   machinery earns its keep as interpretation (39 readable rules instead of
   494 weights) and would matter for a count-based predictor or a much
   larger vocabulary, but on this problem it is not where the accuracy
   comes from. This mirrors the Exp 02 controls: exhaustive features beat
   selected ones when exhaustive is affordable.
3. **Compositions add almost nothing** (0.00–0.02 bits). The synthetic
   advantage of composition was a search-budget effect in spaces too large
   to enumerate; here all 584 count-≥5 lagged pairs are enumerable, so the
   budget argument doesn't apply and the pair-of-contexts feature adds
   little beyond what the logistic model already combines linearly.
4. **The mechanisms are recovered as explicit objects.** Top validated
   fragments on both seeds include every link of the ground-truth loops:
   occ:arrive –s→ CO2:up900 –s→ vent:on –s→ CO2:down900 –s→ vent:off;
   setpoint:up –s→ heater:on –s→ T:up20; occ:leave –m→ vent:off; window:on
   –m→ CO2:down700 (air exchange through the window). The five-step cascade
   is present as its chain of fragments. The window → heater link is not
   recovered (84 window events against 4,100 heater cycles: lift too low).
5. **A confound slipped through, and it names the next null.** "setpoint:up
   –l→ occ:arrive" (lift 5) and "T_out:up20 –m→ occ:arrive" are not
   mechanisms; both follow the clock. The per-type circular-shift null
   cannot remove shared daily-cycle confounding, exactly as flagged after
   Experiment F. A cycle-preserving shift (offsets in whole days) is the
   correct null for this data and is a one-line change.

## Verdict against the benchmark's own definition

Primary criterion met (beats 3.14 / 2.93 non-heater bits by ~1 bit, two
seeds). Secondary criteria: building-wide triggers handled without being
poisoned by the chatty sensor — yes (0–1 vibration contexts retained; the
regularized model is robust regardless); mechanisms recovered as explicit
structures — yes; faster fault adaptation than retraining — not tested yet
(the model here is static; the online variants from E/H are the next step).

Not yet done: online refitting across the test period (regime adaptation),
the cycle-preserving null, a second symbolization to check sensitivity, and a
non-trivial composition test (longer chains as single features) to see whether
anything beyond pairwise lagged contexts carries information in this system.

---

# Second-building test — does a library learned on A fit B'? (2026-10-18)

Files in `dataset/`: `building_sim.py` (configurable simulator), `symbolize_b.py`
(B' symbolized with its own thresholds, then every event type and zone name
scrambled; `building2_key.json` is the answer key), `exp_transfer.py`,
`transfer_results.txt` / `.json`, `transfer_alignment_learned.json`,
`fig_transfer.png`.

Building B': different seed; four zones; heater and vent time constants,
control delays, thresholds, setpoints (22/18), schedule (08–18) and occupancy
all different; climate colder; a **dehumidifier loop** A does not have; its own
fault. 32 event types, 30 with a role counterpart in A, 2 (dehum on/off) with
none. Nothing lexical is shared with A.

Three questions, three answers.

## 1. Does the formula transfer? Yes — given a dictionary.

A's fitted model (Markov + lagged contexts, trained on A days 0–29) applied to
B' through the TRUE role mapping, with zero B' data:

| mapping | all B' events | events with an A counterpart | dehumidifier-loop events |
|---|---|---|---|
| true | 3.13 | **2.66** | 9.98 |
| learned (structure + 2 anchors) | 3.30 | 3.00 | 7.71 |
| random | 7.15 | 7.00 | 9.30 |

2.66 bits with no B' data is better than a Markov model trained on a full
day of B' (2.75) and equal to B''s own lagged-context model at one day (2.64).
A's knowledge of the shared loops is worth about a day of B' data. A wrong
dictionary is worse than uniform guessing (7.0 bits vs 4.9); a dictionary is
not optional.

Mixture λ·P_A + (1−λ)·P_own, λ chosen on B''s own training days, bits on
events with an A counterpart:

| B' days | 1 | 2 | 3 | 5 | 10 | 20 | 30 |
|---|---|---|---|---|---|---|---|
| B' own contexts | 2.64 | 2.20 | 2.15 | 2.04 | 1.80 | 1.77 | 1.55 |
| own + A's model | **2.30** | 2.22 | **2.07** | **1.95** | 1.79 | **1.73** | 1.55 |
| chosen λ | 0.50 | 0.75 | 0.50 | 0.25 | 0.25 | 0.10 | 0.00 |

The conjunction gain is 0.34 bits at one day, still present at twenty, gone at
thirty — a leftward shift of the learning curve that fades as B''s own data
takes over, with λ decaying on its own. On the dehumidifier loop A never saw,
the mixture *hurts* (5.4 vs 4.5 bits at one day, converging by day 5):
negative transfer lands exactly where the systems don't share structure, as
every synthetic experiment predicted, and the uniform λ is the wrong tool
there (a per-token λ would confine the damage).

## 2. Can the dictionary be learned from structure? Mostly — and the misses are instructive.

Alignment of the two buildings' lagged-pair lift matrices (three lag classes,
z-scored, equal data on both sides, Hungarian + refinement, 20 restarts):

| signal | accuracy on 30 shared types (chance 0.03) |
|---|---|
| validated fragment graphs only, no anchors | 0.00 |
| validated fragment graphs, 2 anchors | 0.23 |
| full lift matrices, no anchors | 0.42 (restarts: 0.07, 0.60, 0.60) |
| full lift matrices, 2 anchors (setpoint:up, heater:on) | 0.61 |
| full lift matrices, 8 anchors | 0.63 |

The first row was my design error: sparse validated graphs from unequal
amounts of data (73 vs 201 edges) are not comparable objects. On the dense
statistics the structure-only solution is bimodal (two of three restarts find
the 0.60 solution) and two anchors make it stable.

What the learned mapping gets right, token by token: every heater, vent,
window and setpoint event; all four CO2 crossings; three of four temperature
crossings; both occupancy events; the lower RH band; and dehum:off correctly
assigned to "no counterpart". What it gets wrong: the four vibration
crossings (the chatty sensor — a symmetric quartet with no mechanism to
distinguish them), the outdoor-temperature crossings (rare, weakly coupled),
and the upper RH band. The mapping is correct exactly on the tokens that carry
mechanism and wrong exactly on the ones that don't — which is why zero-shot
through the learned mapping (3.00 bits) recovers most of the true-mapping
value (2.66) against 7.00 for random. Anchors beyond two add nothing because
the residual errors are symmetries no amount of structure can break.

## 3. Does translating the library's *context set* help? No — and that's informative.

The first version of the learning-curve test translated only *which contexts
matter* (A's 39 fragment contexts through the mapping) and let B' learn the
weights. That gave nothing beyond B''s own contexts at any k ≥ 2, even with
the true mapping. The knowledge worth transferring is the fitted
associations, not the feature list; contexts are cheap to re-identify from a
day of data, their predictive content is not.

## Standing conclusions

- The circle analogy holds: the shared loops are one formula drawn twice,
  and the formula fitted on one drawing predicts the other with no data from
  it — provided the strokes can be matched.
- Matching is learnable from structure for the mechanism-bearing tokens, is
  bimodal without anchors, and is stabilized by two. Structure gets you to
  the loops; something lexical or temporal must break the symmetries among
  tokens that carry no mechanism.
- The conjunction gain is real, graded by shared structure, fades with data,
  and goes negative precisely on unshared structure. All three signs match the
  synthetic programme (A, C, D, E).
- The right unit of transfer is the fitted model (or a prior on it), not the
  context set.

Caveats: one pair of buildings, one symbolization each; the two anchors were
chosen by me, not discovered; the mixture weight is global; A's model is the
static one (no online adaptation). The next step on this thread is per-token
transfer weights and a second B' with a different loop composition.
