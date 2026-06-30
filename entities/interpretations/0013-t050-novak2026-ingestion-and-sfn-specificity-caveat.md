---
id: interpretation:0013-t050-novak2026-ingestion-and-sfn-specificity-caveat
type: interpretation
title: "t050 — Novak2026 (largest paired-site PAIS biopsy series) reinforces h0007's lesion (P1) and single-protocol cross-trigger convergence (P4), nudges the non-length-dependent pattern (P2), and surfaces the first SFN-specificity caveat (hEDS dysautonomia shows comparable small-fiber loss)"
status: active
source_refs: &id001 []
related:
- hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
- question:0004-convergent-small-fiber-neuropathy-substrate
- proposition:0014-pais-small-fiber-structural-lesion-ienfd
- proposition:0015-pais-sfn-non-length-dependent-pattern
- proposition:0017-pais-sfn-cross-trigger-convergence
- pre-registration:0003-cross-syndrome-paired-biopsy-primary-dysautonomia-controls
- evidence-line:0063-novak2026-largest-paired-biopsy-pais-sfn-supports-p1
- evidence-line:0064-novak2026-single-protocol-two-trigger-convergence-supports-p4
- evidence-line:0065-novak2026-proximal-sgnfd-not-lesser-weakly-supports-p2
- paper:Novak2026
- topic:post-infectious-dysautonomia-and-autoimmunity
- topic:measurement-ascertainment-artifacts-in-pais
- task:t050
created: '2026-06-24'
updated: '2026-06-24'
input: *id001
prior_interpretations: []
relations:
- predicate: "sci:amends"
  target: interpretation:0009-t049-sfn-cross-syndrome-ingestion
---

# Interpretation: t050 — Novak2026 ingestion reinforces h0007's lesion (P1) and single-protocol cross-trigger convergence (P4), nudges the NLD pattern (P2), and surfaces the first SFN-specificity caveat

## Verdict

**Verdict:** [+] Net-positive for h0007's existence/convergence legs, **but with a new specificity caveat
that pressures `question:0004`'s "distinguishes from primary dysautonomia" clause** — not h0007's
falsifiers. Novak2026 was surfaced by the `task:t050` vehicle hunt; it is **inadmissible as the
`pre-registration:0003` promotion vehicle** (fails G2 — no clean primary-dysautonomia arm) but is strong
*supporting* evidence ingested for P1/P4 and weak for P2. h0007 stays **candidate** (criterion #1 still
needs the G2 vehicle); no proposition changes belief band (all remain `speculative` on observational
literature), but the P1 and P4 bases are materially strengthened in quality.

## Findings Summary

This is an **evidence-ingestion** pass (single paper, three lines), a by-product of the t050 vehicle hunt.
Novak2026 (PLoS One; PMC12829881) is the **largest paired-site PAIS skin-biopsy series** in the corpus:
long COVID n=143, ME/CFS n=170, hEDS n=290, healthy controls n=73, with **paired proximal thigh + distal
calf** ENFD/SGNFD (PGP9.5/Therapath), QASAT-graded.

- **P1 (`proposition:0014`, lesion) — reinforced (`evidence-line:0063`, moderate, independent cohort).**
  Biopsy SFN 67% (LC) / 53% (ME/CFS) vs **0% controls**. The largest-n lesion evidence to date; adds a new
  independent cohort to a base previously carried by Oaklander2022 + Joseph2021 (against the Walitt2024
  null).
- **P4 (`proposition:0017`, cross-trigger convergence) — reinforced in *quality* (`evidence-line:0064`,
  moderate, shared-source).** This is the **first single-protocol, single-center head-to-head** of two
  PAIS triggers (LC vs ME/CFS) with convergent SFN *and* autonomic-failure profiles — directly answering
  the standing `evidence-line:0043` caveat that prior convergence was "of the finding, not of a
  standardized protocol." It adds no new *cohort count* (same patients as the P1 line) but upgrades the
  methodological strength of the convergence claim.
- **P2 (`proposition:0015`, non-length-dependent pattern) — nudged, not measured (`evidence-line:0065`,
  weak).** Proximal SGNFD involvement is not lesser than distal (consistent with NLD), but the paper gives
  **group-level site densities, no per-subject NLD/LD classification, no NLD fraction** — the same
  limitation as Oaklander2022. P2 remains h0007's thinnest leg; only `pre-registration:0003`'s
  per-subject-classified paired-site vehicle moves it from "asserted" to "measured."

## The specificity caveat (the consequential new result)

Novak2026's **hEDS arm (n=290) — a non-infectious heritable dysautonomia — shows SFN comparable to or
greater than the PAIS arms** (63% biopsy; "more pronounced peripheral neurodegeneration") [@Novak2026]. This is the
first corpus data point indicating the small-fiber substrate is **not exclusive to post-infectious
syndromes**. It does **not** dispute P1 (the lesion is real) or P4 (it recurs across PAIS triggers); it
pressures the *specificity* half of `question:0004` ("distinguishes from primary dysautonomia") and A1
(subtype distinctness). Operationally it is a **live preview of `pre-registration:0003`'s
"reverse/diagnostic-surprise" branch** (Δ≈0 because a non-PAIS dysautonomia comparator is also
lesion-positive): lesion *existence* is now well-evidenced, while PAIS-*specificity of the pattern* — the
discriminating claim — looks like the harder contrast to win. hEDS is not the locked G2 comparator
(idiopathic POTS / familial dysautonomia, no SFN comorbidity), and hEDS's own SFN makes it a *contaminated*
proxy — but the direction of the signal is a caution the discriminating test must confront.

## Evidence Quality

- **Independence:** Novak2026 is a new independent cohort for P1; its P4/P2 lines re-use the same cohort
  (`shared-source`), so they add quality, not vote count.
- **Metric caveat (`topic:measurement-ascertainment-artifacts-in-pais`):** QASAT grading (abnormal =
  age/sex-adjusted score > 0) is **more inclusive** than the conventional ≤5th-percentile IENFD cutoff —
  prevalence figures are likely inflated and not directly comparable to percentile-cutoff studies. Robust
  in *direction* (vs 0% controls), metric-sensitive in *magnitude*.
- **Design bounds:** retrospective, single referral center (severity enrichment), historical controls
  without parallel labs, ME/CFS arm **without documented infectious onset** (presumptive post-infectious
  status), longer ME/CFS symptom duration (chronicity confound).

## Hypothesis-Level Implications

For **`hypothesis:0007`** (NLD-autoimmune-SFN substrate, **candidate**): P1 and P4 are now the
best-evidenced legs (largest cohort + first standardized cross-trigger protocol); P2 stays thinnest; the
autoimmune-causation leg (P3/`0016`/`0018`) is untouched by this paper. **No promotion** — criterion #1
still requires the `pre-registration:0003` G2 vehicle, and the hEDS specificity signal makes the
discriminating contrast (not lesion existence) the binding question. h0007 remains candidate, now with a
sharper account of *what specifically* the discriminating vehicle must establish: pattern specificity
against a *clean* primary-dysautonomia arm, since the lesion itself is no longer in serious doubt.

## New Questions Raised

1. **Is the PAIS NLD *pattern* specific vs primary dysautonomia, or is the whole dysautonomia family
   non-length-dependent?** Novak2026 cannot say (hEDS is contaminated; no per-subject NLD). This is exactly
   `pre-registration:0003`'s headline P2 contrast.
2. **Does requiring documented infectious onset change the ME/CFS SFN rate?** Novak2026's ME/CFS arm was
   not infection-onset-restricted; the infection-associated subset may differ.
3. **Does QASAT-vs-percentile scoring reconcile the heterogeneous LC SFN prevalence** across the corpus
   (Oaklander 63% / Joseph 31% / Walitt null / Novak 53–67%)? A metric-harmonization re-analysis would test
   whether prevalence scatter is partly a scoring artifact.

## Updated Priorities

1. **t050 stays blocked** on the G2 vehicle; the screening log + this specificity caveat now define what
   the admissible vehicle must prove (pattern specificity, not mere lesion presence).
2. Watch the **Novak group** as the most likely source of an admissible vehicle (one protocol amendment
   away — add an idiopathic-POTS/familial arm, re-score to percentile cutoffs).
3. Carry the **metric-ascertainment** caveat forward to all future SFN-prevalence claims.
