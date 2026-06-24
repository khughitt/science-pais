---
id: pre-registration:0004-jak1-inhibitor-driver-vs-marker
type: pre-registration
title: "JAK1-inhibitor (abrocitinib, NCT06597396) driver-vs-marker test for persistent\
  \ JAK-STAT/IL-6 signaling in long COVID — data-gated discriminating test of\
  \ h0003/q0006"
status: committed
committed: '2026-06-24'
mode: data-gated
spec: ''
related:
- hypothesis:0003-immune-exhaustion-feedback
- question:0006-jak-stat-il6-driver-vs-marker
- proposition:0026-lc-jakstat-exhaustion-loop-is-proximal-driver
- proposition:0025-lc-persistent-inflammatory-activation-dissociated-ifn
- topic:long-covid-immune-dysregulation
- topic:therapeutics-and-clinical-trials
- interpretation:0012-t047-h0003-ifn-reconciliation-and-jak1-trial-registration
- task:t047
commits_to:
- hypothesis:0003-immune-exhaustion-feedback
- proposition:0026-lc-jakstat-exhaustion-loop-is-proximal-driver
- question:0006-jak-stat-il6-driver-vs-marker
created: '2026-06-24'
updated: '2026-06-24'
---
# Pre-registration: JAK1-inhibitor (abrocitinib, NCT06597396) driver-vs-marker test for persistent JAK-STAT/IL-6 signaling in long COVID — data-gated discriminating test of h0003/q0006

> **Mode: data-gated.** The vehicle (a results readout of NCT06597396) does not yet exist in the corpus.
> This pre-registration commits the *interpretation rule* now and defers execution until the trial reports
> and clears the Vehicle-Admissibility Gate (G1–G5 below). Until then the standing verdict is **`[?]`
> inconclusive-for-coverage** — it produces **no `bears_on` belief update** on any commitment target. This
> is *not* a null result (a null is evidence); it is the absence of qualifying evidence. The deferred
> interpretation is tracked by an `active` task (t054) whose blocker is the trial readout. This pre-reg is
> the operationalization of `question:0006` (driver-vs-marker) and the maintenance-engine claim of
> `hypothesis:0003`.

## Hypotheses Under Test

This pre-registration is the single most discriminating test named in `question:0006` and in
`hypothesis:0003`'s "Evidence Needed To Shift Belief" / Falsifiability sections. It commits how the
abrocitinib (JAK1 inhibitor) RCT **NCT06597396** will update the following epistemic targets (the
operational protocol — that the trial ran as a placebo-controlled co-endpoint design — is checked
separately as an admissibility gate, not a `bears_on` target):

| Target | Role | Test | Class |
|---|---|---|---|
| `proposition:0026` (JAK-STAT/exhaustion loop is a **proximal driver**, reversible by inhibition) | the causal-loop conjunct of h0003 | symptom + pathway co-endpoint | **confirmatory — headline** |
| `question:0006` (driver vs marker) | the open question | same | **confirmatory** |
| `hypothesis:0003` (exhaustion-feedback maintenance engine) | the candidate frame | does interrupting the loop relieve disease? | **confirmatory** |

`proposition:0025` (the persistent-inflammatory/dissociated-IFN *descriptive state*) is in `related:` but
**not** a commitment target: it is already supported observationally and is not what this interventional
trial tests — the trial tests whether that state is *causal*, not whether it *exists*.

## Expected Outcomes

Prior (from Aid2025's failed-negative-feedback framing and the IL-6/JAK-STAT symptom correlations): JAK1
inhibition will **reduce both the inflammatory pathway signature and symptoms**, with the effect
**concentrated in the inflammatory-signature-positive endotype** (`proposition:0025`) rather than uniform
across PASC. This prior is held weakly — the competing **marker** reading (pathway suppressed, symptoms
unmoved) and the **multi-loop** reading (`hypothesis:0001`; Seo2025's broad single-agent nulls) are live,
so a null is genuinely informative.

## Decision Criteria

Epistemic (belief-updating) criteria for the commitment targets:

- **SUPPORT (driver reading; `proposition:0026` gains a supporting line, `hypothesis:0003` updates upward,
  `question:0006` → "driver"):** placebo-controlled improvement in the **co-primary symptom endpoint**
  (validated PROM — fatigue/PEM/cognitive) **AND** demonstrated **pathway/target engagement** (reduction
  of IL-6R / JAK-STAT pathway score / downstream ISGs vs placebo). Strength scales with endotype
  specificity: a larger effect in the inflammatory-signature-positive subgroup than in signature-negative
  is the strongest form.
- **WEAKEN → MARKER (disputing line on `proposition:0026`; downward/falsifier for h0003's maintenance-
  engine framing; `question:0006` → "marker"):** demonstrated **pathway suppression WITHOUT symptom
  benefit** — the loop is engaged pharmacologically but disease is unmoved, i.e. it is a marker of an
  upstream lesion (antigen `hypothesis:0002`, autoimmunity) that the inhibitor does not reach.
- **INCONCLUSIVE (no update):** symptom benefit **without** measured pathway engagement (could be
  off-target/placebo); or benefit/null reported only **pooled** with no endotype or target-engagement
  data; or trial fails an admissibility gate. → route to exploratory, await stratified replication.

## Null Result Plan

A **clean marker-not-driver null is evidence** (disputing `proposition:0026`), but its weight is gated on
**adequacy**: the trial must demonstrate target engagement, an adequate dose/duration, and — ideally —
endotype stratification. A **flat null in an unstratified cohort** is *weak* disconfirmation: it is
confounded with wrong-endotype (benefit may exist only in signature-positive patients per
`proposition:0025`) and with the multi-loop view (a single agent hitting one node of the
`hypothesis:0001` attractor; consistent with Seo2025's broad single-agent nulls). Such a result lowers
confidence in the *simple single-loop, easily-interruptible* reading without refuting that the loop
participates in maintenance. Next step on ambiguity: endotype-stratified or biomarker-enriched replication.

## Suspicious/Unexpected Result Plan

A surprisingly large symptom effect (e.g. effect size far exceeding anti-inflammatory trials in adjacent
diseases) would prompt checks for **functional unblinding** (abrocitinib has visible/known side effects),
**placebo-response inflation** on subjective PROMs, endpoint-timing cherry-picking, and per-protocol vs
ITT divergence, before accepting it as driver-confirming.

## Known Limitations

Even a perfectly executed trial cannot: localize the **cell source** of the IL-6/JAK-STAT signal
(`question:0006`); distinguish whether a positive effect reflects interrupting the *exhaustion loop*
specifically vs generic anti-inflammatory benefit; or establish **cross-PAIS** transfer (ME/CFS,
post-Q-fever) — the axis-shared-beyond-SARS-CoV-2 half of `question:0006` needs separate vehicles.

## Exploratory vs. Confirmatory

- **Confirmatory:** the symptom + pathway-engagement co-endpoint driver-vs-marker test above.
- **Exploratory:** endotype effect-modification (signature-positive vs negative); dose-response; whether
  responders co-segregate with antigen positivity (`hypothesis:0002` link, Peluso2024); biomarker
  trajectories (IL-6R, ISG dissociation per `proposition:0025`).

## Vehicle-Admissibility Gate (G1–G5)

The trial readout activates the rule only if it satisfies:

- **G1 — symptom co-primary:** a validated patient-reported symptom endpoint (not biomarker-only).
- **G2 — target engagement:** a measured pathway/biomarker readout (IL-6R / JAK-STAT score / ISGs) showing
  whether the loop was actually suppressed — the load-bearing axis that makes a null interpretable
  (parallel to the antigen target-engagement gate on `proposition:0020`/`question:0002`).
- **G3 — controlled design:** randomized, placebo-controlled.
- **G4 — endotype resolution:** stratification by, or enrichment for, the inflammatory-signature endotype
  (`proposition:0025`) available — without it, a null is only weakly disconfirming (Null Result Plan).
- **G5 — adequacy:** adequate dose, duration, and power to detect a clinically meaningful symptom effect.

Named vehicle: **NCT06597396** (abrocitinib, JAK1 inhibitor; initiated on the strength of Aid2025). Other
JAK/IL-6-axis LC trials that satisfy G1–G5 also qualify. Spent trials failing G1/G2 (biomarker-only, or no
target-engagement readout) do **not** activate the rule.

## Standing verdict

`[?]` inconclusive-for-coverage until an admissible readout exists — **no `bears_on` update** on
`proposition:0026`, `question:0006`, or `hypothesis:0003`. Tracked by **task:t054**.
