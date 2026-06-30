---
id: "evidence-line:0033-aid2025-lc-female-inflammatory-amplification-within-recovered-null"
type: "evidence-line"
title: "Aid2025 female-amplified inflammatory-pathway enrichment in long COVID with a within-recovered sex-null — strongest available interaction control"
status: "active"
stance: "supports"
target: "proposition:0013-immune-domain-partial-hormone-mediated-objective-exception"
source: "paper:Aid2025"
strength: "moderate"
independence: "independent"
independence_group: "aid2025-multiomic-lc-cohorts"
evidence_role: "direct_test"
evidence_type: "literature_evidence"
identification_strength: "observational"
related:
  - "proposition:0013-immune-domain-partial-hormone-mediated-objective-exception"
  - "question:0007-mechanism-of-female-predominance-in-pais"
  - "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
source_refs:
  - "paper:Aid2025"
created: "2026-06-23"
updated: "2026-06-23"
---

# Evidence Line: Aid2025 — female-amplified inflammation in LC with a within-recovered sex-null

## What this line shows

Aid2025 (multi-omic profiling across two cohorts, n≈142+38) is the **strongest available interaction control**
for `proposition:0013`. In the **within-sex case-control** direction, long-COVID females show
stronger inflammatory-pathway enrichment (JAK-STAT / IL-6 / IFN / complement) than recovered females,
exceeding the corresponding male contrast — and, critically, the analysis reports **no significant
sex difference within the recovered (CC) control group**. The within-recovered null is the control
that argues against a simple carried-through baseline female-immune skew in this cohort, but it is
not powered to exclude every baseline-carry explanation. The endpoints are lab-assayed
(RNA-seq / proteomics) and applied symmetrically to both
sexes, satisfying the ascertainment-symmetry requirement [@Aid2025].

## Why it is independent

Two multi-omic cohorts under its own `independence_group: aid2025-multiomic-lc-cohorts`,
methodologically and by-cohort distinct from the directly-measured-cytokine line
(`evidence-line:0034`, Shahbaz cohort) and the MY-LC signature line (`evidence-line:0035`,
Silva2024).

## Caveats / scope

`direct_test`, **moderate** — bounded by: (1) the sex stratification is a **secondary analysis**
(female-LC n≈29 / recovered-F n≈14), and the authors themselves flag the need for confirmation in
larger studies; (2) the readout is **pathway enrichment**, not a single validated assay; (3)
cross-sectional, so reverse causation (chronic inflammation → HPG suppression) is unresolved; (4) it
supports a female *amplification* reading for inflammation but does not, on its own, adjudicate whether
the operative variable is categorical sex or testosterone level — that bound comes from
`evidence-line:0035`.
