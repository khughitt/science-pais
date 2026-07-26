---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse157007-aging-frailty-pbmc-scrna
kind: dataset
title: GSE157007 — Single-cell immune landscape of aging and frailty (PBMC scRNA-seq + TCR)
status: candidate
provided_capabilities:
- data_product: data-product:gene-expression-single-cell
  qualifiers:
    cohort_design: case-control
    stratification: frailty
    trigger: not-applicable
created: "2026-07-17"
updated: "2026-07-17"
origin: external
dataset_class: deposit
source_class: observational
tier: evaluate-next
license: unknown
access:
  level: public
  availability: available
  verified: true
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE157007
  verification_method: landing-confirmed
  last_reviewed: '2026-07-17'
  verified_by: agent (verify-access)
accessions: []
source_refs:
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE157007
ontology_terms:
- frailty
- immunosenescence
- scrna-seq
related:
- question:0033-frailty-and-pre-frailty-as-an-independent-pais-boundary-condition-with
identity_context:
  taxon: 9606
  assembly:
    label: UNKNOWN
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# GSE157007 — Single-cell immune landscape of aging and frailty (PBMC scRNA-seq + TCR)

**Candidate dataset.** `status: candidate` — catalogued but not yet acquired.

## What it is

Single-cell atlas of PBMC across the lifespan: 48 samples / 17 donors (3 cord blood,
3 healthy young, 6 healthy old, **5 frail**), with paired scRNA, TCR V(D)J and cell-surface protein
barcoding; ~114,467 cells. NovaSeq 6000.

## Why it fits

Supplies the **frail-vs-healthy-old baseline immune reference** that PAIS cohorts lack.
Its intended use for `question:0033` is signature projection: learn a frailty signature here, then
score it across the project's existing long-COVID / ME-CFS deposits. That is the only route to a
frailty × PAIS contrast that does not require a DUA, and it matches the project's established
preference for signatures re-computed from primary data over published tables.

## Access / caveats

**Public.** GEO landing page confirmed 2026-07-17; 706.4 Mb archive (TAR of CSV/MTX/TSV) plus SRA.

**Caveats.**
- **No infection arm.** Frailty baseline only — it cannot test the boundary-condition claim by
  itself, only supply the signature.
- 17 donors, 5 frail: small, and frailty ascertainment is by the source study's definition.
- Projection across platforms (scRNA → bulk long-COVID deposits) carries its own transfer
  assumptions that must be stated wherever it is used.

**Scope (D-005 / D-008).** The frailty signature-projection line was ruled a **new-modality**
computational line requiring its own D-005 decision (distinct from the D-005/D-006 MR vehicle and
D-007's atopy MR). Taken up as **D-008 (2026-07-18)**: the **feasibility packet only** is authorised
— learn a frailty signature from this deposit (and/or `dataset:gse196793-frailty-influenza-vaccine-pbmc`)
and project it onto the project's public long-COVID / ME-CFS transcriptomic deposits, on public GEO
data only. A **reportable** frailty×PAIS projection is **not** authorised; it is gated on a follow-up
ratification (**D-008b**) once the packet clears five pre-registered gates: (1) training power +
frailty labels (the 5-frail/17-donor n is a hard power question), (2) feature compatibility across
training/target platforms, (3) cross-cohort validation + batch/platform robustness (the dominant
failure mode), (4) negative-control projections, (5) explicit non-causal framing. Full reasoning:
`core/decisions.md` → D-008.

## Access verification log

- 2026-07-17 (agent (verify-access)): GEO landing page confirmed public 2026-07-17: 48 samples / 17 donors (3 cord blood, 3 young, 6 healthy old, 5 frail), scRNA + TCR + CITE, NovaSeq 6000, 706.4Mb TAR + SRA. Frail-vs-healthy-old baseline reference; NO infection arm -- signature source only.
