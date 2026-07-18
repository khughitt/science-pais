---
id: question:0029-tissue-resolved-spatial-multi-omics-and-molecular-imaging-to-localize
kind: question
title: Tissue-resolved spatial multi-omics and molecular imaging to localize post-infectious
  immune activity beyond blood
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Peluso2023
origins:
- type: assistant
  ref: explore-ideas-methodology
related:
- question:0001-shared-molecular-signature-across-triggers
- hypothesis:0002-tissue-reservoir-antigen-fragment
- theme:0003-demonstrability-ceiling-cross-pathogen-design
created: '2026-07-04'
updated: '2026-07-18'
added_by: explore-ideas:claude-opus-4-8:cand-methodology-tissue-spatial-multiomics-pais
lens_views:
- lens: methodology
  rationale: "Blood-centric profiling cannot resolve where persistent activation resides.\
    \ Three mechanisms the project tracks \u2014 antigen/fragment persistence (hypothesis:0002),\
    \ small-fiber neuropathy, gut dysbiosis \u2014 have plausible tissue seats requiring\
    \ spatial resolution. PET with T-cell-activation tracers has been applied at single-pathogen\
    \ level; extending spatial + imaging methods across triggers with matched blood\
    \ controls would resolve the tissue-to-blood surrogate gap. Serves question:0001\
    \ and hypothesis:0002.\n"
  origin_ref: explore-ideas-methodology
---
# Tissue-resolved spatial multi-omics and molecular imaging to localize post-infectious immune activity beyond blood

## Summary

Spatial transcriptomics/proteomics and molecular imaging (e.g. [18F]F-AraG PET of activated T cells)
applied to PAIS-relevant **non-blood** tissues — gut lamina propria, dorsal root ganglion, skeletal
muscle, bone marrow — to localize persistent immune activation, antigen-fragment deposition, or
transcriptional dysregulation that is absent or attenuated in matched blood, and to test whether such
tissue signatures differ across triggers or symptom subphenotypes. The question is a direct probe of
whether blood-centric profiling (the project's dominant data channel) is a faithful surrogate for where
PAIS pathology actually resides.

## Why It Matters

- **Decision it affects:** how much weight blood-based biomarkers deserve, and whether `hypothesis:0002`
  (tissue-reservoir antigen/fragment persistence) has a spatial seat that blood cannot see.
- **Serves** `question:0001` by testing whether a shared cross-trigger signature exists at the tissue
  level rather than in blood.
- **Risk if unanswered:** the project may under- or over-read blood signals decoupled from tissue
  pathology (small-fibre neuropathy, gut dysbiosis, marrow imprinting all have plausible tissue seats).

## Current Evidence

- **The tissue-resolved paradigm is established at single-pathogen scale.** Peluso2023 ([18F]F-AraG
  whole-body PET, n=24) found elevated activated-T-cell tracer uptake up to ~2.5 years post-COVID across
  brain stem, spinal cord, bone marrow, lymphoid tissue, cardiopulmonary tissue and gut wall, with gut
  viral-RNA persistence — demonstrating tissue-based activation invisible to routine blood assays. This
  is the anchor the question proposes to extend cross-trigger with matched blood controls.
- **Gap:** no cross-trigger spatial multi-omics/imaging exists; PAIS spatial transcriptomics/proteomics
  of DRG/muscle/marrow is essentially absent, and the tissue-to-blood surrogate gap is unquantified.

## Thoughts

- **Best current interpretation:** this is the highest-resolution but **least tractable** vehicle in
  `theme:0003` — the demonstrability ceiling here is *tissue access* (DRG, marrow, gut biopsy are
  invasive and rarely banked cross-trigger), not analysis. [18F]F-AraG is also a T-cell-activation
  tracer of limited specificity, and the evidence is single-cohort, single-trigger, imaging-only.
- **Major remaining uncertainty:** whether tissue signatures are shared across triggers (supporting
  `hypothesis:0001`/`hypothesis:0002`) or trigger-specific, and whether any accessible tissue (e.g.
  skin-biopsy small-fibre, or banked marrow from `question:0055` / `pre-registration:0006`) can serve as
  a cross-trigger readout without new invasive sampling.
- **Priority:** P3 — conceptually pivotal for the blood-surrogate question but access-bound; best
  advanced opportunistically via already-banked tissue rather than as a standalone prospective imaging
  study.

## Connections to Project

- Related hypotheses: `hypothesis:0002` (tissue-reservoir antigen/fragment — the mechanism this would
  localize).
- Related questions / theme: `question:0001`; `theme:0003` (named vehicle).
- Required datasets: cross-trigger paired tissue+blood specimens with spatial-omics/imaging (none
  project-held; access is the constraint).
- Required analyses: spatial DE / tissue-vs-blood contrast; cross-trigger signature comparison.
- Priority level: P3 (access-bound).

## Related

- Topic notes: `theme:0003-demonstrability-ceiling-cross-pathogen-design`.
- Article notes: `cite:Peluso2023`.
- Methods/Datasets: `pre-registration:0006` (banked-marrow HSPC ATAC as an accessible tissue readout).
