---
id: "interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation"
type: "interpretation"
title: "t025: the within-cohort PEM-stratified molecular comparison does not exist, and PEM's objective correlate is trigger- and endpoint-specific"
status: "active"
source_refs: &id001
  - "paper:McGregor2019"
  - "paper:Gattoni2025"
  - "paper:Keller2014"
  - "paper:Appelman2024"
  - "paper:Che2025"
related:
  - "question:0015-does-pem-requirement-improve-cross-study-comparability"
  - "question:0001-shared-molecular-signature-across-triggers"
  - "question:0011-mitochondrial-basis-of-pem"
  - "hypothesis:0001-shared-dysregulated-attractor"
  - "proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode"
  - "interpretation:0001-cross-trigger-pathway-overlap-reanalysis-t035-null-nonarbitrating"
  - "interpretation:0007-t044-stop-pasc-pem-proteome-severity-unadjusted-gap-stands"
  - "paper:Maestri2025"
  - "evidence-line:0036-maestri2025-pem-symptom-resolved-proteome-but-severity-unadjusted-confirms-gap"
  - "topic:mecfs-long-covid-convergence"
  - "task:t025"
  - "task:t044"
created: "2026-06-22"
updated: "2026-06-23"
input: *id001
prior_interpretations:
  - "interpretation:0001-cross-trigger-pathway-overlap-reanalysis-t035-null-nonarbitrating"
relations: []
---

<!-- Mode: CONCEPTUAL. Input is a three-pronged literature-discovery sweep (no empirical pipeline output);
findings are expert_judgment / literature_evidence reframing existing belief, not new data. -->

# Interpretation: t025 — the PEM-stratified molecular comparison does not exist, and PEM's objective correlate is trigger-/endpoint-specific

## Verdict

**null-but-informative** (conceptual mode): the within-cohort PEM-positive vs PEM-negative molecular comparison that `task:t025` set out to find **has not been published**; the search instead surfaces a *cross-trigger dissociation* in PEM's objective correlates that qualifies — does not overturn — the project's PEM-requirement policy.

## Findings Summary

A three-pronged literature-discovery sweep (PASC PEM-stratified omics; ME/CFS PEM-stratified omics; the PEM-vs-severity confound) returned two convergent results.

1. **The decisive design does not exist (`null`, `literature_evidence`).** Across ~25 targeted queries spanning RECOVER, IMPACC, MY-LC, STOP-PASC and the ME/CFS omics literature, **no study performs a true within-cohort, between-group PEM-positive vs PEM-negative blood-omics contrast on a single platform in PASC.** In ME/CFS the design exists in exactly one study — McGregor2019 (PEM+/NoPEM/HC metabolomics; hypoxanthine/purine-metabolism deregulation tracks continuous PEM severity) — which is small (n≈47, 35 PEM+), metabolomics-only, 2019 (pre-DSQ-PEM), and **does not model-adjust for broader illness severity or disease-duration structure**. Its PEM and NoPEM arms have similar fatigue scores, so fatigue alone does not explain the signal, but the design still cannot cleanly separate a PEM-specific molecular state from chronic-illness severity, episode timing, duration, or small-NoPEM-sample artifacts. The field systematically substitutes the easier designs: within-subject exercise *provocation* (Che2025; Germain2022/2025; PEM-epigenetics) and *overall-severity* stratification (UK Biobank; T-cell preprints). q0015's central gap (its line 49) is confirmed **still open as of mid-2026**.

2. **PEM's objective correlate is trigger- and endpoint-specific (`suggestive`, `negative_result` on naive convergence).** The ME/CFS whole-body 2-day-CPET signature (Keller2014: 13.8% day-2 VO₂peak decrement, deconditioning excluded) does **not** transfer to PEM-enriched long COVID (Gattoni2025: whole-body 2-day-CPET **null** despite 80% mDSQ-PEM, though n=15 and underpowered) — yet long-COVID PEM **does** show an objective lesion at the **peripheral-muscle** endpoint (Appelman2024: worsened mitochondrial OXPHOS after provoked PEM, deconditioning ruled out). Same symptom label, different measurable lesion and measurement channel. This is now graph-encoded as `proposition:0011` (three independent cohorts).

## Evidence Quality

Conceptual-mode assessment (reasoning quality / grounding / independence / testability):

- **Grounding.** Finding 1 is grounded in an exhaustive multi-angle search whose *absence* result is corroborated by three independent agents converging on the same non-existence — a defensible "research gap" claim, not a failure to look. Finding 2 is grounded in three named, independent cohorts on direct physiological/tissue assays.
- **Independence.** The three arms of `proposition:0011` are genuinely independent (distinct triggers, cohorts, and assay endpoints). The McGregor2019 within-cohort design and the provocation designs are *not* independent confirmations of the target design — they are the substitutes that mark the gap.
- **The load-bearing weakness** is Gattoni2025: a small, underpowered null (n=15, mDSQ-retrospective PEM, no ME/CFS or PEM-negative arm, 40% deconditioned). It is held at `weak` in `evidence-line:0027`; a true zero and a missed ME/CFS-sized effect are not yet distinguishable. The proposition deliberately does **not** rest on it alone.

## Data Quality Checks

Not a data pipeline. The relevant checks are entity-provenance: McGregor2019 ingested from Europe PMC full text; Gattoni2025 from Europe PMC abstract only (methods/CIs inaccessible in the available source — flagged in the entity); Keller2014 and Appelman2024 pre-existing full-text entities. No control/dimensionality/sample-count checks apply.

## Proposition-Level Updates

- **New: `proposition:0011`** — "objective PEM correlates are trigger- and endpoint-specific, not one shared whole-body failure mode." Three supporting evidence-lines: `evidence-line:0026` (Keller2014, ME/CFS whole-body positive, `background_constraint`, moderate); `evidence-line:0027` (Gattoni2025, long-COVID whole-body null, `proxy_support`, weak); `evidence-line:0028` (Appelman2024, long-COVID muscle positive, `proxy_support`, moderate).
- **No change to a "PEM molecular signature" proposition** — none is minted, because the within-cohort PEM-stratified molecular contrast that would license one does not exist. McGregor2019 is recorded as the nearest template (q0011, q0015) but its severity confound is unresolved.

## Hypothesis-Level Implications

`hypothesis:0001-shared-dysregulated-attractor` is **constrained, not refuted**. If a shared failed-recovery attractor exists, its objective bioenergetic expression is **not uniform** across triggers: the ME/CFS whole-body CPET signature does not appear in long COVID at the same endpoint. This aligns with `interpretation:0001`'s t035 cross-trigger pathway-overlap null (non-arbitrating) — two independent analyses now find that cross-trigger convergence is weaker at the *mechanistic/physiological* level than the shared-symptom framing assumes. The attractor frame survives as an organising idea; a strong "single shared bioenergetic lesion" reading does not.

## Evidence vs. Open Questions

- **q0015** (does PEM-requirement improve cross-study comparability?) — **partially addressed.** The direct test remains unanswerable from existing data; the new evidence qualifies the standing read: PEM-requirement plausibly improves *within-trigger* coherence (McGregor2019; the ME/CFS CPET literature) but does **not** guarantee *cross-trigger* biological exchangeability (Gattoni2025 vs Keller2014). The severity-vs-PEM confound is **untested at the molecular level** in any cohort.
- **q0001** (shared molecular signature across triggers?) — uncertainty increased: functional-level divergence adds to t035's molecular-level null.
- **q0011** (mitochondrial basis of PEM?) — sharpened: the long-COVID lesion is mitochondrial *at the muscle level* (Appelman2024) even where whole-body VO₂ is preserved (Gattoni2025), pointing to a periphery-vs-whole-body dissociation.

## New Questions Raised

1. **(empirical, high)** Does a PEM-associated molecular signal survive adjustment for overall illness/fatigue severity — i.e., is PEM a mechanism or a severity marker? No study has run this test. This is the decisive, still-missing experiment behind q0015.
2. **(empirical, high)** Why does long-COVID PEM show muscle-level OXPHOS pathology (Appelman2024) without a whole-body 2-day-CPET decrement (Gattoni2025)? Is this a periphery-vs-central-delivery dissociation, a power artifact, or a kinetics/interval mismatch?
3. **(methodological, medium)** Is the long-COVID 2-day-CPET null stable at adequate N, with provocation-confirmed PEM, a PEM-negative arm, and longer inter-test intervals (48–72 h)?

## User Questions

None blocking. The disposition decision (record + ingest + mint) was taken before authoring.

## Limitations & Residual Uncertainty

- An **absence-of-evidence** claim (no within-cohort PEM-stratified omics study) can be falsified by a single missed or future paper; the sweep was thorough but not a registered systematic review.
- The cross-trigger contrast is **between-study**, not within one harmonised design — confounded by case definition (Fukuda vs WHO), protocol, deconditioning prevalence, and platform. "Endpoint-specific relocation" is the most parsimonious reading of three non-commensurable assays, not a measured equivalence.
- The Gattoni2025 null is underpowered (see Evidence Quality).
- **Provenance note (close substitutes surfaced by the sweep):** STOP-PASC/Maestri2025 (Olink protein-vs-PEM-severity *regression*, n=152, preprint), Singh2023 (invasive-CPET O₂-extraction-endotype proteomics), Germain2022/2025 (ME/CFS provocation omics), and two single-analyte PEM-graded studies (Azimi2025 FGF-21; Moezzi2025 haptoglobin). **[t044 update, 2026-06-23]:** STOP-PASC/Maestri2025 has since been **ingested** as `paper:Maestri2025` and used as an evidence-line source (`evidence-line:0036` → `proposition:0011`); see the Updated Priorities bullet and `interpretation:0007`. The remaining leads (Singh2023, Germain2022/2025, Azimi2025, Moezzi2025) are still recorded only as leads and must be ingested as `paper:` entities before any is used as an evidence-line `source:`.

## Updated Priorities

- **Close `task:t025`** with the gap-finding (the comparison must be *computed/commissioned*, not found).
- **File a follow-up** to compute the comparison where feasible: convert STOP-PASC/Maestri2025's protein-vs-PEM-severity regression to a group contrast, or pursue a within-cohort severity-adjusted PEM-stratified analysis on an accessible cohort (RECOVER/IMPACC) — the decisive test behind q0015. **[t044 update, 2026-06-23 — interpretation:0007]:** route (a) attempted and **blocked**. STOP-PASC/Maestri2025 was ingested (`paper:Maestri2025`); its PEM–protein associations turn out to be *univariate proportional-odds regressions adjusted only for batch plate* (no overall-severity covariate), and the individual-level data needed to refit them is gated ("upon publication"; repo 404 as of 2026-06). The decisive severity-adjusted contrast therefore **remains uncomputable from public data**. A weak symptom-resolved increment (PEM ↓IL1RL1/IL1R2, distinct from fatigue/dyspnea/CV) was recorded (`evidence-line:0036`) supporting `proposition:0011` at the blood-proteome endpoint. Route (b) (RECOVER/IMPACC) stays open and data-access-gated.
- **Watch** for a larger, provocation-confirmed long-COVID 2-day-CPET study; it would directly strengthen or overturn `evidence-line:0027` and `proposition:0011`.
