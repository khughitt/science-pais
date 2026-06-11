---
id: question:0010-vascular-microclot-subphenotype
type: question
title: Does a complement/microclot/endothelial axis define a distinct vascular subphenotype
  of long COVID, and does it predict treatment response?
status: active
ontology_terms:
- thromboinflammation
- microclot
- complement system dysregulation
- endothelial dysfunction
- subphenotype
- treatment response
datasets: []
source_refs:
- cite:CerviaHasler2024
- cite:Nicolai2023
- cite:Stahlberg2025
related:
- topic:thromboinflammation-and-endothelial-dysfunction
created: '2026-06-11'
updated: '2026-06-11'
---

# Does a complement/microclot/endothelial axis define a distinct vascular subphenotype of long COVID, and does it predict treatment response?

## Summary

Long COVID is biologically heterogeneous, and a recurring proposal is that a subset of patients are defined by a *vascular* failure mode: persistent complement activation, a microclot/fibrinaloid and platelet-hyperactivation burden, and endothelial injury. This question asks (a) whether these complement/microclot/endothelial features co-segregate into a discrete, biomarker-identifiable vascular subphenotype rather than being scattered across all patients, and (b) whether membership in that subphenotype predicts response to mechanism-matched therapy (anticoagulant/antiplatelet or complement-modulating). It is the operational test of whether "vascular long COVID" is a real, actionable stratum.

## Why It Matters

- Determines whether the project should treat the vascular axis as a distinct subphenotype for stratified trials (e.g. enroll only complement/microclot-high patients into anticoagulation or complement-inhibitor arms) rather than running unstratified trials that dilute any true effect.
- If unanswered, the contested microclot literature stays unresolved, biomarker panels (C5bC6/C7, vWF/ADAMTS13, RHI) are not validated as stratifiers, and promising therapies may be discarded after failing in unselected populations.

## Current Evidence

- Supporting: CerviaHasler2024 provides a persistent complement (TCC-imbalance) + thromboinflammation signature with quantitative biomarker ratios (C5bC6/C7, vWF/ADAMTS13) that machine learning ranks as top long-COVID discriminators, plus monocyte-platelet aggregates increasing with disease duration — a coherent candidate vascular-subphenotype signature. Nicolai2023 reviews convergent endotheliopathy/coagulation evidence (vWF up, ADAMTS13 down, D-dimer, NETosis, SPECT perfusion defects) and notes ongoing trials (STIMULATE-ICP rivaroxaban) that could test treatment response. Stahlberg2025 makes the endothelial dysfunction objectively measurable (RHI abnormal in 61%) and progressive (rising NT-proBNP), supplying a functional readout for subphenotype assignment.
- Conflicting / cautionary: The fibrinaloid-microclot construct specifically is contested — detection is not standardized, controls can show signal, and no controlled trial has yet shown that clearing microclots reverses symptoms. CerviaHasler2024 is cross-sectional and cannot establish that vascular features define a separable subgroup versus a continuum, and Huang2025-scale cardiovascular heterogeneity (and overlapping mast-cell/central-sensitization mechanisms) means cardiovascular symptoms do not uniquely index a complement/microclot mechanism.

## Thoughts

- Best current interpretation: the complement/coagulation/endothelial abnormalities are real and partly biomarker-quantifiable, and plausibly enrich a vascular-symptom-dominant subgroup, but whether they form a *discrete* subphenotype with predictive treatment value (rather than a graded severity dimension overlapping other mechanisms) is unproven.
- Major uncertainty: the causal/treatment-response link — does anticoagulation or complement inhibition specifically benefit biomarker-defined vascular-subphenotype patients? — and whether microclots are a reproducible, causal component or a partly artefactual correlate.

## Connections to Project

- Related hypotheses: `hypothesis:0001-shared-dysregulated-attractor` (vascular thromboinflammation as a candidate self-amplifying loop).
- Required data or analyses: unsupervised clustering of harmonized vascular biomarkers (complement TCC ratios, vWF/ADAMTS13, D-dimer, RHI, platelet/microclot assays) in long COVID cohorts to test for a discrete cluster; linkage of cluster membership to outcomes in stratified anticoagulant/complement-modulator trials (e.g. STIMULATE-ICP).
- Priority level: P2 — high translational payoff and biomarker support, but the decisive treatment-response test depends on trial data not yet mature.

## Related

- Topic notes: `topic:thromboinflammation-and-endothelial-dysfunction`, `topic:long-covid-immune-dysregulation`, `topic:biomarkers-and-objective-endpoints`.
- Article notes: CerviaHasler2024, Nicolai2023, Stahlberg2025.
- Methods/Datasets: serum complement/coagulation proteomics (SomaScan/Olink/MS); EndoPAT RHI; microclot/platelet functional assays; STIMULATE-ICP and complement-modulator trial outcomes.
