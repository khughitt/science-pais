---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse251849-longcovid-pbmc-cognitive
kind: dataset
title: GSE251849 — Long COVID PBMC (cognitive phenotype)
status: candidate
created: "2026-07-07"
updated: "2026-07-07"
consumed_by:
- plan:0010-crosspais-pathway-response-rank-estimation
origin: external
dataset_class: deposit
source_class: observational
tier: evaluate-next
license: unknown
access:
  level: public
  availability: available
  verified: true
  verification_method: landing-confirmed
  last_reviewed: '2026-07-08'
  verified_by: agent (t117 WP1)
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE251849
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: GEO processed per-sample counts file GSE251849_Counts.txt.gz (+ series matrix) publicly downloadable; staging to disk deferred to workflow execution
accessions:
- GSE251849
ontology_terms:
- long-covid
- sars-cov-2
- pbmc
- rna-seq
provided_capabilities:
- data_product: data-product:gene-expression-bulk-rna
  qualifiers:
    cohort_design: case-control
    trigger: sars-cov-2
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0001-shared-molecular-signature-across-triggers
- hypothesis:0001-shared-dysregulated-attractor
---

# GSE251849 — Long COVID PBMC (cognitive phenotype)

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: evaluate-next`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

Long COVID with a cognitive/brain-fog phenotype, **PBMC bulk RNA-seq** (record title: "Blood–brain barrier disruption and sustained systemic inflammation in individuals with long COVID-associated cognitive impairment"). Confirmed against the GEO record (2026-07-08): tissue **PBMC**; assay **bulk RNA-seq** on **GPL24676 (Illumina NovaSeq 6000)**. **23 samples**, four groups: unaffected controls (7), recovered post-COVID (5), Long COVID without brain fog (6), Long COVID with brain fog (5) — i.e. **≈11 Long COVID vs 12 controls** (7 healthy-naive + 5 infected-recovered), matching the claimed split. Case-vs-control contrast exists at sample level but n per subgroup is small (5–7). Time post-infection at sampling **[UNVERIFIED] — not stated in record**.

## Corpus role (t117)

- **Matrix:** strict-primary
- **onset_certainty:** documented
- **Conditional/LOO flag:** small N — LOO-drop candidate.

## Access / caveats

Public accession (`GSE251849`); per-sample expression matrix **confirmed downloadable** (`GSE251849_Counts.txt.gz` processed counts + series matrix) — verified in t117 WP1 (2026-07-08).
