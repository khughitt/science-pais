---
id: question:0002-antigen-clearance-rescues-symptoms
type: question
title: Does clearing persistent antigen (e.g. antiviral treatment in long COVID) rescue
  post-acute symptoms, establishing antigen persistence as a driver rather than an
  epiphenomenon?
status: active
ontology_terms:
- antigen persistence
- viral reservoir
- therapeutics
- long COVID
datasets: []
source_refs:
- cite:Peluso2024
- cite:McClune2025
- cite:Skevaki2025
related:
- topic:antigen-pathogen-persistence
- discussion:0003-antigen-persistence-treatable-vs-fixed
- proposition:0020-antigen-clearance-rescues-established-pais
- proposition:0021-acute-antigen-burden-determines-pais-incidence
- interpretation:0011-t046-antigen-clearance-trials-ingestion
- hypothesis:0002-tissue-reservoir-antigen-fragment
created: '2026-06-11'
updated: '2026-06-24'
---
# Does clearing persistent antigen (e.g. antiviral treatment in long COVID) rescue post-acute symptoms, establishing antigen persistence as a driver rather than an epiphenomenon?

## Summary

Persisting antigen is detected in long COVID (Peluso2024, Skevaki2025) and pathogen fragments persist after Borrelia clearance (McClune2025), but detection alone does not establish that antigen *drives* symptoms. This question asks the decisive interventional test: does clearing the persisting antigen attenuate or resolve post-acute symptoms? A positive result would promote antigen persistence from correlate to driver and validate antigen-clearance therapeutics; a null would push the field toward self-sustaining-loop or autoimmune explanations.

## Why It Matters

- Decides whether antiviral / antigen-clearance strategies (extended nirmatrelvir-ritonavir, monoclonals) are a rational PAIS therapeutic class, or whether the post-acute state is "locked" independent of the original trigger.
- If unanswered, antigen persistence remains attractive but untestable, and the field cannot rationally prioritize antiviral vs immunomodulatory trials.

## Current Evidence

- Supporting: Peluso2024 detects spike/S1/N in ~25% of survivors to 14 months with burden correlating to acute severity; McClune2025 shows persisting pPG^Bb is biologically active (alters host proteome, suppresses PBMC energy metabolism); Vreeman2025 supplies a mechanism (spike → αvβ6 → TGF-β) by which residual antigen could sustain damage.
- Conflicting / gaps: Peluso2024 explicitly declines to test symptom linkage; early antivirals in established long COVID have not produced a clear positive; antigen could reflect slower clearance rather than cause illness.
- **Interventional trials formalized (t046, 2026-06-24; `interpretation:0011-t046-antigen-clearance-trials-ingestion`)** — verdict **`[~]` contested-but-untested**, split into two propositions:
  - *Established-disease clearance (`proposition:0020`):* three independent interventional nulls — Geng2024/STOP-PASC (NMV/r, `evidence-line:0053`), Peluso2026/outSMART-LC (anti-RBD mAb AER002, `evidence-line:0055`) — across two unrelated clearance modalities. But the **decisive load-bearing finding** is Bhattacharjee2026/PAX-LC (`evidence-line:0054`): 15-day NMV/r changed *neither circulating Spike antigen, anti-Spike antibody, nor PBMC subsets*. **No completed trial both demonstrated antigen clearance AND measured symptom change**, so these nulls cannot adjudicate this question — they are broken tests, not disconfirmations.
  - *Acute-phase prevention (`proposition:0021`):* metformin RCTs — Bramante2023/COVID-OUT (LC incidence ↓~41%, HR 0.59; `evidence-line:0056`) and Bramante2026/ACTIV-6 (primary endpoint missed but clinician-dx LC RR 0.50; `evidence-line:0057`) — show acute-phase intervention lowers PAIS *incidence*. The treatment-null + prevention-positive pattern is the basis of the fixed-risk-factor-at-onset reconciliation.
  - *Methodological gate (load-bearing):* future evidence on this question should be gated on **demonstrated antigen target-engagement** + **antigen-positive enrichment** (analogous to the functional-vs-binding-assay gate on `question:0009`). A clearance-demonstrated, antigen-enriched, symptom-endpoint trial — ideally with an early/established timing arm — is the single design that can decide it.

## Thoughts

- Best current interpretation: antigen clearance is plausibly *necessary but not sufficient* (Peluso2024b, Skevaki2025) — once a self-sustaining loop is established, removing the seed may not reverse it (Trautmann2025, Komaroff2025).
- Major uncertainty: timing (acute-phase prevention window vs established disease) and compartment (plasma antigen may not reflect tissue-reservoir burden) likely determine whether clearance helps.

## Connections to Project

- Related hypotheses: `hypothesis:0002-tissue-reservoir-antigen-fragment`, `hypothesis:0001-shared-dysregulated-attractor`.
- Required data or analyses: RCTs of antigen-clearing agents stratified by baseline antigen positivity, with symptom and biomarker co-endpoints; tissue (not just plasma) antigen quantification.
- Priority level: P1 — the most consequential mechanistic test for therapeutics.

## Related

- Topic notes: `topic:antigen-pathogen-persistence`, `topic:long-covid-immune-dysregulation`.
- Article notes: Peluso2024, McClune2025, Skevaki2025, Vreeman2025, Peluso2024b.
- Methods/Datasets: LIINC cohort; RECOVER-VITAL trial.
