---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse221921-fibromyalgia-pbmc
kind: dataset
title: GSE221921 — Fibromyalgia PBMC transcriptome (non-infectious specificity, WP4b)
status: candidate
created: '2026-07-09'
updated: '2026-07-09'
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
  verification_method: retrieved
  last_reviewed: "2026-07-09"
  verified_by: "agent (t117 WP4b)"
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE221921
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: "Per-sample expression staged from GSE221921_RAW.tar (189 members, one per sample; sha256 79ff6dc…), group from the series-matrix disease-state characteristic. Pinned+checksummed acquisition + uniform parse both RUN 2026-07-09 (config acquisition.GSE221921 + parse.GSE221921). SRA raw reads (PRJNA916731) + processed xlsx are alternative sources not staged."
accessions:
- GSE221921
- PRJNA916731
ontology_terms:
- fibromyalgia
- non-infectious
- pbmc
- rna-seq
- specificity-control
provided_capabilities:
  - modality: transcriptomics
    assay: bulk-rna
    trigger: non-infectious-fibromyalgia
    cohort_design: case-control
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0017-deflationary-alternatives-vs-shared-pathophysiology
- hypothesis:0001-shared-dysregulated-attractor
---

# GSE221921 — Fibromyalgia PBMC transcriptome (non-infectious specificity, WP4b)

**Candidate dataset for `task:t117`** (`status: candidate`). Full-download-verified against
the public GEO record + staged bytes on 2026-07-09 (t117 WP4b discovery sweep + flagship build).

## What it is

Fibromyalgia (FM) **PBMC bulk RNA-seq** — the D-003-designated **non-infectious** stress-test for
`hypothesis:0001` (the shared dysregulated attractor). Series "Identification of unique genomic
signatures in patients with fibromyalgia and chronic pain" (Sci Rep 2024, s41598-024-53874-8;
BioProject PRJNA916731). Confirmed design: **96 fibromyalgia vs 93 matched healthy controls**,
whole-blood-derived PBMC, Illumina NovaSeq 6000 (GPL24676), single platform.

Per-sample matrix confirmed downloadable and staged: `GSE221921_RAW.tar` carries 189 per-sample
member files (`GSM…_Sample_NNN.txt.gz`), each a `gene`(symbol) × one-sample column. GEO documents
the value scale as **"Log of normalized transcripts per million"** (StringTie TPM → TMM-normalized →
logged) — a continuous already-log scale (t117 `expression_scale: log2_intensity`, limma-direct; a
counts/CPM treatment would double-transform). Case/control labels live in the series-matrix
`disease state` characteristic (`… (FMA)` vs `Healthy … (CONTROL)`; note the depositor's
"Fibromylagia" misspelling — matched by the parenthetical code, not the word).

## Corpus role (t117 WP4b)

- **Matrix:** `specificity` — a **SEPARATE non-infectious specificity column, NEVER pooled** into the
  strict/sensitivity rank matrices (the `specificity` tag is absent from `MATRIX_COMPOSITION` and the
  adjudication extras). It rides the **same** uniform DE→enrichment over the **same** pinned
  Hallmark∪Reactome universe as the primary corpus, then is **projected onto the learned PAIS
  subspace** (`gws_fm_specificity.py`) for the t116 Q-D infection-specificity read-across: is the PAIS
  shared subspace equally recovered by a non-infectious illness (→ generic-sickness manifold) or not
  (→ infection-specific attractor)?
- **build_now flagship:** deliberately PBMC + RNA-seq to match the PAIS strict stratum that IS
  identifiable (WP3/WP4: only the PBMC stratum clears K≥3). The rest of the admissible non-infectious
  panel (`gse67311` WB microarray FM, `emexp2069` GWI microarray, `gse286345` GWI RNA-seq, `gse182503`
  IEI microarray) is **queued replication**, not built this pass.

## Access / caveats

Public (`GSE221921`), per-sample RAW.tar staged + hash-locked (t117 WP4b, 2026-07-09). Caveats:
(1) the projection target — the PAIS subspace — is itself **weakly identified** (Stage-3c FAIL,
LOO-fragile), so the WP4b readout is **`exploratory_flagship`, not `validated_specificity`**;
(2) FM is strongly female-biased and the cohort carries a sex imbalance — **sex is carried into the
staged sample sheet as a QA-ledger covariate (`covariate_cols: [sex]`) but left unmodeled** (`~ group`),
matching the primary corpus's default treatment for NES-comparability; (3) symbol→Ensembl harmonization via the pinned org.Hs.eg.db map (some
non-coding/novel symbols drop); (4) FM is a chronic widespread-pain syndrome — a **non-infectious**
comparator, not a PAIS case (never counted as an in-scope post-acute case).
