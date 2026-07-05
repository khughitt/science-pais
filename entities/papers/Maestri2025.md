---
id: paper:Maestri2025
kind: paper
title: "Systems Immunology of Long Covid: Insights from the STOP-PASC Clinical Trial"
status: active
ontology_terms:
- plasma proteomics
- Olink Explore HT
- post-exertional malaise
- patient-reported outcomes
- proportional odds logistic regression
- nirmatrelvir/ritonavir
- long COVID signature
- autoantibody
- microclots
- IL1RL1
- IL1R2
- leptin
dataset_usage: []
datasets: []
source_refs:
- cite:Maestri2025
related:
- question:0015-does-pem-requirement-improve-cross-study-comparability
- proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode
- topic:biomarkers-and-objective-endpoints
- topic:mecfs-long-covid-convergence
created: '2026-06-23'
updated: '2026-06-23'
---
# Systems Immunology of Long Covid: Insights from the STOP-PASC Clinical Trial

<!--
- **Authors:** Evan Maestri, Woo Joo Kwon, Hong Zheng, Tyler Prestwood, Haley Hedlin, Jane W. Liang, Holly McCann, Blake Shaw, Lu Tian, Ben Jones, Rufei Lu, Graham Wiley, Emily Haraguchi, Oliver Wirz, Jumana Afaghani, Brandon Lam, Dlovan F. D. Mahmood, Nicole A. Phillips, Martha M. S. Sim, Jeremy P. Wood, James R. Heath, Scott D. Boyd, Joel Guthridge, Upinder Singh, Hector Bonilla, Prasanna Jagannathan, P. J. Utz, Linda N. Geng, Purvesh Khatri
- **Year:** 2025 (preprint)
- **Journal:** medRxiv preprint (not peer-reviewed as of mid-2026)
- **DOI/URL:** https://doi.org/10.64898/2025.12.04.25341650
- **BibTeX key:** Maestri2025
- **Source:** medRxiv full-text HTML (v1, posted 2025-12-05)
-->

## Key Contribution

Systems-immunology companion analysis to the STOP-PASC randomized trial of nirmatrelvir/ritonavir
(NMV/r) in long COVID (LC). Comprehensive immune profiling of **152 trial participants** — plasma
proteomics (Olink® Explore HT 5400 panel), autoantigen arrays, viral serology, and microclot assays
at baseline, day 15, and week 10 — plus a meta-analysis of nine independent LC Olink cohorts
(n = 590 samples). Two results matter for this project: (1) a battery of **negative** mechanistic
findings (no widespread autoantibody, EBV-reactivation, or microclot differences between LC
participants, pre-pandemic controls, and non-LC individuals); and (2) an **exploratory
protein-vs-patient-reported-outcome (PRO) association** map in which **post-exertional malaise (PEM)
has a symptom-resolved proteomic signature distinct from fatigue, dyspnea, and cardiovascular
symptoms** — IL1RL1 and IL1R2 negatively associated with PEM, whereas leptin/coagulation factors
track fatigue/heart. The PRO models are **univariate per symptom and not adjusted for overall illness
severity**, so they are the closest public approach to — but do not constitute — the decisive
severity-adjusted PEM-stratified molecular test (`question:0015`, `task:t044`).

## Methods

**Study design:** Systems-immunology analysis nested in the STOP-PASC RCT (NMV/r vs placebo/ritonavir
in adults with LC; the parent trial showed no PRO benefit of NMV/r, consistent with the PAX LC trial).

**Cohort:** 152 STOP-PASC LC participants; biosamples + symptom surveys at baseline, day 15, week 10
(follow-up to 15 weeks).

**Assays:** Olink® Explore HT (5400-plex plasma proteomics); autoantigen microarrays; SARS-CoV-2 and
EBV serology (MSD + microbead platforms); microclot assay.

**Within-group differential proteomics (treatment effect):** linear mixed-effects (limma) models
adjusting for plate (fixed effect) and accounting for repeated measures; p-values Bonferroni-corrected.

**Protein/serology vs PRO associations (the analysis relevant to t044):** **proportional odds logistic
regression** fit to the **ordinal Likert severity (0 none / 1 mild / 2 moderate / 3 severe)** of each
of seven baseline symptoms — fatigue, brain fog, dyspnea, body aches, heart, stomach, **and an
additional post-exertional-malaise symptom**. **Each protein × symptom model was adjusted only for
batch plate** — there was **no covariate adjustment for overall illness/fatigue severity, age, sex, or
BMI**, and each symptom was modeled separately (no joint/mutually-adjusted model). Jonckheere-Terpstra
trend tests used for serology-vs-severity trends. FDR by Benjamini-Hochberg unless otherwise specified.

**Meta-analysis:** nine independent LC Olink cohorts; per-protein Hedges' adjusted *g*; BH-FDR;
"Long COVID Signature" (LCS) = 60 proteins differentially regulated in the same direction across
cohorts (FDR < 5%, effect size > 0.5, measured in ≥ 3 cohorts).

## Key Findings

### Treatment effect (NMV/r)
- Day 15 vs baseline: **94 significant proteins** in the NMV/r arm vs **9** in placebo/ritonavir
  (Bonferroni-adjusted P ≤ 0.05); changes **normalized by week 10**, primarily affecting
  myeloid/monocyte, lysosome, and complement-activation pathways. Transient pharmacodynamic signal
  without durable PRO benefit.

### Negative mechanistic findings
- **No widespread differences** in autoantibody profiles, EBV reactivation, or microclotting between
  STOP-PASC LC participants, pre-pandemic controls, and individuals without LC. (Counterweight to
  autoimmunity/microclot mechanistic narratives in this cohort.)
- Cardiovascular symptom severity was **negatively** associated with baseline anti-SARS-CoV-2 antibody
  levels (more robust humoral response → fewer CV manifestations).

### Protein–PRO associations (relevant to PEM / q0015)
- **1327 proteins** associated with increasing/decreasing severity of ≥ 1 PRO; **110 proteins** showed
  consistent trends across **≥ 3 PROs** (a shared cross-symptom severity axis).
- **Symptom-resolved exemplars:** leptin (LEP), coagulation factor VII (F7), and factor XII (F12)
  **positively** associated with **fatigue and heart/cardiovascular** symptoms; CD38 **negatively**
  with **dyspnea**; **IL1RL1 (ST2 / IL-33 receptor) and IL1R2 negatively with post-exertional
  malaise**. IL1RL1/IL1R2 are soluble decoy IL-1-family receptors (anti-inflammatory regulators) — a
  PEM-associated signal distinct from the leptin/coagulation fatigue signature.
- Authors' framing: PRO severity "aligns with meaningful underlying inflammatory signaling," but the
  study **cannot infer direction** (whether immune features drive PROs or result from them).

### Meta-analysis
- A conserved **60-protein LCS** across nine cohorts, indicating multi-compartment immune activation
  (monocyte/myeloid emphasis) despite clinical/technical heterogeneity.

## Relevance

Directly addresses `task:t044` route (a): convert STOP-PASC's protein-vs-PEM-severity regression into a
**severity-adjusted** PEM-stratified molecular contrast (the decisive `question:0015` test — does a
PEM-associated molecular signal survive adjustment for overall illness/fatigue severity?).

The paper supplies the **closest public dataset** to that test but does **not** itself run it: its
PEM associations are **univariate per-symptom proportional-odds regressions adjusted only for batch
plate**. Because the seven symptoms are positively intercorrelated and modeled separately, a protein
"associated with PEM" is **not separated from the shared severity axis** (the 110-protein cross-PRO
set is exactly that shared axis). The decisive severity-adjusted refit would need the **individual-level
protein × multi-symptom-severity matrix**, which is gated — "Olink data … available upon publication";
the analysis GitHub repo (`Khatri-Lab/STOP_PASC_biomarkers`) did not yet exist as of 2026-06.

What the data *do* support is a **weak discriminant-pattern increment**: PEM has a symptom-resolved
proteomic association profile (↓IL1RL1/IL1R2) distinct from fatigue (↑LEP), dyspnea (↓CD38), and
cardiovascular symptoms — consistent with a PEM-specific molecular correlate at the **blood-proteome**
endpoint within a single trigger (long COVID), complementing `proposition:0011`'s cross-trigger,
muscle-/whole-body endpoint-specificity argument.

## Project Framework Mapping

- **question:0015** (does PEM-requirement improve cross-study comparability?) — the decisive
  severity-vs-PEM molecular test **remains unrun**; STOP-PASC is the nearest public data but is
  univariate. Weak suggestive support that PEM carries a partly-distinct blood-protein signature.
- **proposition:0011** (objective PEM correlates are trigger-/endpoint-specific) — extends the
  "PEM-specific, not one shared signal" reading to the **within-long-COVID blood proteome** (a new
  endpoint), held at **weak** because univariate/unadjusted.
- **hypothesis:0001** (shared dysregulated attractor) — the negative autoantibody/EBV/microclot panel
  and the cross-PRO 110-protein severity axis both bear on the "shared inflammatory state" framing;
  neither confirms a single shared PEM-specific lesion.
- **hypothesis:0003** (immune-exhaustion feedback) — IL-1-family decoy-receptor signal and monocyte/
  myeloid LCS are adjacent but not directly tested here.

## Limitations

- **No severity adjustment** in the PRO models (batch-plate only); symptoms modeled univariately, so
  PEM-specific vs general-severity protein effects are **not separable** — the precise confound
  `question:0015` targets.
- PEM measured as a **single ordinal Likert item**, not a validated PEM instrument (DSQ-PEM) or
  provocation/CPET; ascertainment is self-report at baseline.
- **Cross-sectional** associations; authors explicitly disclaim causal direction.
- Cohort is a **treatment-trial population** (selected for an antiviral RCT), which may not represent
  the broader LC population; no PEM-negative-matched-for-severity comparison arm.
- Individual-level data **not yet released** (upon-publication); preprint, not peer-reviewed as of
  mid-2026. Multiple-testing across 5400 proteins × 7 symptoms; exemplar proteins reported without
  per-protein effect sizes/CIs in the main text.

## Model / Tool Availability

- Code: `https://github.com/Khatri-Lab/STOP_PASC_biomarkers` (stated "upon publication"; **404 / not
  yet created** as of 2026-06). Olink HT QC code: `https://github.com/guthridge-informatics/Olink_HT`.
- Data: Olink, autoantibody/viral arrays, MSD serology "available upon publication"; additional data
  from lead contact on request.

## Follow-up

### Immediate reads
- Tracks `interpretation:0004` (t025) follow-up and `interpretation:0007` (t044 verdict).

### Open questions raised
- If/when individual-level STOP-PASC data is released, re-fit the PEM proportional-odds model with an
  overall-severity covariate (e.g., summed non-PEM symptom score or a fatigue composite) to run the
  decisive `question:0015` test — reopen `task:t044` route (a) at that point.
- Are IL1RL1/IL1R2 (soluble IL-1/IL-33 decoy receptors) reproducibly PEM-associated across cohorts,
  and do they survive severity adjustment? (Candidate PEM-specific marker if so.)
