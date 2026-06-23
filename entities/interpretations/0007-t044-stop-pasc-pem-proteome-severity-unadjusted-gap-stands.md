---
id: interpretation:0007-t044-stop-pasc-pem-proteome-severity-unadjusted-gap-stands
type: interpretation
title: 't044: STOP-PASC PEM proteome is severity-unadjusted; the decisive q0015 severity-vs-PEM
  test stays open, with a weak symptom-resolved increment'
status: active
source_refs: &id001
- paper:Maestri2025
related:
- question:0015-does-pem-requirement-improve-cross-study-comparability
- proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode
- evidence-line:0036-maestri2025-pem-symptom-resolved-proteome-but-severity-unadjusted-confirms-gap
- interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation
- task:t044
created: '2026-06-23'
updated: '2026-06-23'
input: *id001
prior_interpretations:
- interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation
relations:
- predicate: "sci:amends"
  target: "interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation"
---
<!--
Conclusion chains:
- Use `relations:` with `predicate: "sci:amends"` when this interpretation revises,
  narrows, qualifies, or extends an older conclusion.
- Use `relations:` with `predicate: "sci:supersedes"` when this interpretation
  replaces an older conclusion as the current canonical reading.
- Keep `prior_interpretations` only as a narrative breadcrumb. The graph relation
  is the machine-readable source of truth.
-->

<!-- Mode: CONCEPTUAL. Input is a targeted reanalysis-feasibility assessment of one published preprint
(Maestri2025 / STOP-PASC), executing route (a) of task:t044 — no new pipeline output. Findings are
literature_evidence / expert_judgment. Amends interpretation:0004 (t025). -->

# Interpretation: t044 — STOP-PASC PEM proteome is severity-unadjusted; the decisive q0015 test stays open, with a weak symptom-resolved increment

## Verdict

**Verdict:** [~] Gap stands — the decisive severity-adjusted PEM-stratified molecular test (`question:0015`) remains **uncomputable from public data**: Maestri2025's PEM–protein associations are univariate, batch-plate-only-adjusted proportional-odds regressions, and the individual-level data needed to refit them with a severity covariate is gated. A **weak** symptom-resolved proteome increment (PEM ↓IL1RL1/IL1R2, distinct from the fatigue/dyspnea/CV signatures) supports `proposition:0011` at a new endpoint without closing the gap.

## Findings Summary

t044 chose **route (a)** of its two feasible paths: convert STOP-PASC/Maestri2025's protein-vs-PEM-severity regression into a severity-adjusted group contrast. The assessment of the now-ingested preprint (`paper:Maestri2025`, n = 152, Olink Explore HT 5400-plex) returns two findings.

1. **The decisive test cannot be computed from this source (`null`, `literature_evidence`).** Maestri2025 maps proteins to PEM, but its model is a **proportional-odds logistic regression on the ordinal Likert severity of each of seven symptoms (fatigue, brain fog, dyspnea, body aches, heart, stomach, PEM), modeled separately and adjusted only for batch plate** — with **no covariate for overall illness/fatigue severity, age, sex, or BMI**. This is exactly the confound `question:0015` targets: because the seven PROs are positively intercorrelated (the paper reports 1327 proteins associated with ≥1 PRO and **110 proteins consistent across ≥3 PROs** — a shared severity axis), a "PEM-associated" protein is **not separated** from general severity. Deriving a severity-adjusted PEM coefficient requires the **individual-level protein × multi-symptom matrix**; separate marginal proportional-odds coefficients are mathematically insufficient. That data is gated — "Olink data … available upon publication"; the analysis repo (`Khatri-Lab/STOP_PASC_biomarkers`) **did not exist (404) as of 2026-06**, and the work is still a preprint, not peer-reviewed. Route (a) is therefore **blocked until release**.

2. **A weak symptom-resolved increment is available (`suggestive`, `literature_evidence`).** PEM carries a **distinct** proteomic association profile — **IL1RL1 (ST2 / IL-33 receptor) and IL1R2 negatively associated** — differing from the fatigue/cardiovascular signature (leptin, F7, F12, positive) and dyspnea (CD38, negative). IL1RL1/IL1R2 are soluble decoy IL-1-family receptors (anti-inflammatory regulators), so the PEM signal is mechanistically distinct from the leptin/coagulation fatigue axis. That different proteins top different symptoms' rankings is *consistent with* PEM having a partly-specific molecular correlate — now at the **blood-proteome** endpoint within a single trigger (long COVID) — but it is a between-symptom discriminant pattern in **univariate** fits, not a severity-adjusted test, so it cannot rule out that the PEM proteins ride the shared severity axis.

## Evidence Quality

Conceptual-mode assessment (grounding / independence / testability):

- **Grounding.** Finding 1 is grounded in the preprint's own Methods (proportional-odds models, batch-plate-only adjustment) and its data-availability statement (upon-publication) — verified directly from the medRxiv full text plus a confirmed 404 on the named GitHub repo. Finding 2 is grounded in the reported exemplar proteins (main-text Figure 3G / Figure S8 narrative); per-protein effect sizes and CIs are **not** given in the main text, which caps the increment at `weak`.
- **Independence.** STOP-PASC is a genuinely independent cohort and a fourth, orthogonal assay endpoint (circulating proteome) relative to `proposition:0011`'s existing lines (Keller2014 whole-body CPET; Gattoni2025 whole-body CPET null; Appelman2024 muscle biopsy). `evidence-line:0036` is placed in its own `independence_group: maestri2025-stop-pasc-cohort`.
- **The load-bearing weakness** is the univariate, severity-unadjusted model — the very gap this task set out to close. The increment is recorded as `weak`/`proxy_support` precisely so it cannot over-promote `proposition:0011`.

## Data Quality Checks

Not a data pipeline (conceptual reanalysis-feasibility assessment). Entity-provenance checks: Maestri2025 ingested from medRxiv full-text HTML (v1, 2025-12-05), DOI `10.64898/2025.12.04.25341650`; methods/PRO-model details captured verbatim; data-availability and repo-existence claims verified against source. No control/dimensionality/sample-count checks apply. One methodological flag, carried as Finding 1: the published PEM model is severity-unadjusted.

## Proposition-Level Updates

- **`proposition:0011` (objective PEM correlates are trigger- and endpoint-specific) — reinforced weakly, scope extended.** New supporting `evidence-line:0036` (Maestri2025, `weak`, `proxy_support`, independent cohort/endpoint). It extends the proposition's "PEM-specific, not one shared signal" reading from the cross-trigger muscle/whole-body endpoints to the **within-long-COVID blood proteome**. Held at **weak** because univariate/severity-unadjusted; verify the proposition did **not** newly trip `belief.fragile-single-line` (it already rests on three independent lines, so adding a fourth cannot make it fragile).
- **No "PEM molecular signature" proposition minted** — same reason as `interpretation:0004`: the within-cohort, severity-adjusted PEM contrast that would license one still does not exist. Maestri2025 is recorded as the **closest public dataset**, not as that test.

## Question-Level Implications

- **`question:0015` (does PEM-requirement improve cross-study comparability?) — gap re-confirmed, with the *reason* now sharper.** `interpretation:0004` established the decisive severity-vs-PEM molecular test was unrun; t044 attempted the highest-feasibility route to run it and found it **still uncomputable from public data** — not because no cohort measured PEM against the proteome (STOP-PASC did), but because the available models are severity-unadjusted and the individual-level data is gated. The standing read is unchanged: PEM-requirement plausibly improves *within-trigger* coherence; whether a PEM-specific molecular signal survives severity adjustment remains the open, decisive question.
- **`hypothesis:0001` (shared dysregulated attractor) — marginally constrained.** STOP-PASC's negative autoantibody/EBV/microclot panel and its cross-PRO 110-protein shared severity axis neither confirm a single shared PEM-specific lesion nor a uniform autoimmune/microclot mechanism in this cohort; consistent with the attractor surviving as an organizing idea while a strong single-lesion reading does not.

## Evidence vs. Open Questions

- **q0015** — partially addressed (route to the decisive test identified and attempted; blocked on data release). The severity-vs-PEM confound remains untested at the molecular level in any *accessible* cohort.
- **q0011** (mitochondrial basis of PEM) — unchanged; STOP-PASC is blood-proteome, not bioenergetic.
- **q0001** (shared molecular signature across triggers) — unchanged; the cross-PRO shared axis is within long COVID only.

## New Questions Raised

1. **(empirical, high)** When STOP-PASC individual-level Olink + PRO data is released, does the PEM–protein signal (esp. IL1RL1/IL1R2) **survive adjustment for an overall-severity covariate** (summed non-PEM symptom score or a fatigue composite)? This is the literal decisive q0015 test and the trigger to reopen t044 route (a).
2. **(empirical, medium)** Are soluble IL-1/IL-33 decoy receptors (IL1RL1/ST2, IL1R2) reproducibly **PEM-associated across independent cohorts**? A cross-cohort PEM-specific marker would be a strong lead even before severity adjustment.
3. **(methodological, low)** Does any *accessible* cohort (RECOVER-Adult, IMPACC) carry both a validated PEM instrument (DSQ-PEM) and a severity composite on a shared omics platform — i.e., route (b)? t044's route (b) remains open and data-access-gated.

## Limitations & Residual Uncertainty

- This is a **feasibility/near-miss** verdict on one preprint, not new data. It can be overturned the moment STOP-PASC (or another cohort) releases individual-level PEM + proteome + severity data.
- The increment rests on **exemplar proteins without main-text effect sizes/CIs**; the full per-protein PEM coefficients (Figure S8) were not extractable from the available rendering.
- PEM in STOP-PASC is a **single self-report Likert item** at baseline, not provocation/CPET-confirmed; ascertainment is weaker than the DSQ-PEM/CPET designs `question:0015` favors.
- The cohort is a **treatment-trial population** with no PEM-negative-matched-for-severity arm.

## Updated Priorities

- **Close `task:t044`** with the route-(a) verdict: decisive severity-adjusted PEM contrast **not computable** from the public preprint; weak symptom-resolved increment recorded (`evidence-line:0036`); gap re-confirmed.
- **File a watch/follow-up** to monitor STOP-PASC data/repo release ("upon publication"); reopen route (a) — refit the PEM proportional-odds model with a severity covariate — once individual-level data is available.
- **Keep route (b) on the board** (within-cohort severity-adjusted PEM-stratified analysis on RECOVER-Adult / IMPACC) as the data-access-gated alternative; it does not depend on STOP-PASC publication.
- No change to the PEM-requirement policy in t001/t016: within-trigger coherence argument intact; cross-trigger exchangeability and the severity-vs-PEM separation remain open.
