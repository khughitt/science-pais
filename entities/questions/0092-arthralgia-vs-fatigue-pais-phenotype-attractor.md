---
id: question:0092-arthralgia-vs-fatigue-pais-phenotype-attractor
kind: question
title: Do post-infectious arthralgia phenotypes and post-infectious fatigue phenotypes
  converge on the same PAIS attractor state, or represent distinct downstream failure
  modes?
status: active
ontology_terms:
- phenotype heterogeneity
- post-chikungunya chronic disease
- inflammatory arthritis
- post-infectious fatigue
- post-acute infection syndrome
- attractor state
- PAIS scope
datasets: []
source_refs:
- cite:Ramundo2025
origins:
- type: literature
  ref: paper:Ramundo2025
related:
- hypothesis:0001-shared-dysregulated-attractor
- question:0001-shared-molecular-signature-across-triggers
- question:0014-which-pais-case-definition-is-most-biologically-coherent
- paper:Ramundo2025
required_capabilities:
- data_product: data-product:gene-expression-bulk-rna
  qualifiers:
    cohort_design: case-control
created: '2026-07-26'
updated: '2026-07-26'
---

# Do post-infectious arthralgia phenotypes and post-infectious fatigue phenotypes converge on the same PAIS attractor state, or represent distinct downstream failure modes?

## Summary

Post-acute infection syndromes include both fatigue-dominant phenotypes (ME/CFS, long COVID, post-Q-fever fatigue) and arthralgia-dominant phenotypes (post-chikungunya chronic inflammatory joint disease, arthralgic PTLDS). Both pass D-003 (acute infection trigger), both involve persistent post-infectious immune dysfunction, and both appear in the in-scope list of this project. However, the molecular mechanisms driving the joint-specific failure mode (MMP8/LTF-dependent cartilage matrix biology, synovitis, ultrasound-verified arthritis) are substantially different from those driving fatigue and cognitive impairment (autonomic dysfunction, neuroinflammation, mitochondrial bioenergetics, serotonin depletion).

The question is whether these two phenotypic families represent (a) the same post-infectious immune-state displacement manifesting in different target organs depending on host/pathogen factors, or (b) distinct downstream failure modes that merely share a common early upstream cause (viral-persistence-promoting immune failure), with the downstream attractor itself being phenotype-specific.

This question was raised by reading `paper:Ramundo2025` and the scope tension flagged in `search:0002` and `discussion:0002` ("arthralgia-dominant ... caveat").

## Why It Matters

- **Scope of h0001:** If arthralgia and fatigue are the same attractor, pCHIKV-CIJD transcriptomics (Ramundo2025, Chang2024) are positive evidence for h0001. If they are distinct failure modes, arthralgia data fill a separate mechanistic cell and should not be counted as convergence support for the fatigue-attractor hypothesis. Conflating them risks making h0001 trivially true (any chronic post-infectious inflammation would "support" it).
- **Cross-trigger matrix design:** The `search:0002` cross-pathogen signature matrix lumps arthralgia and fatigue phenotypes in the same column (post-chikungunya). If the phenotypes are distinct, the matrix should split by phenotype, not just by trigger.
- **Therapeutic implication:** If shared attractor, treatments that work for fatigue-dominant PAIS (pacing, JAK inhibitors, etc.) should be piloted in pCHIKV-CIJD. If distinct, joint-specific interventions (lactoferrin, MMP modulators) are more appropriate and unlikely to address fatigue.
- **Risk if unanswered:** The project will continue to treat arthralgia-dominant PAIS as corroborating evidence for the fatigue-attractor convergence claim, overstating the strength of cross-trigger molecular evidence and broadening h0001 until "convergence" becomes unfalsifiable.

## Current Evidence

- **Supporting convergence (same attractor):**
  - Ramundo2025 (pCHIKV-CIJD) shows early immune impairment (LIFR down, neutrophil degranulation down, MHC-I down) that structurally parallels immune-failure mechanisms discussed in ME/CFS and long COVID — the shared upstream (early antiviral immune failure → viral persistence) is consistent across phenotypes.
  - PTLDS (Borrelia trigger) includes both arthralgic and fatigue manifestations; Galbraith2011 includes all three triggers in one design without phenotype-splitting, suggesting the field has implicitly treated them as one class.
  - The shared-attractor framing in h0001 explicitly allows for heterogeneous molecular configurations reaching the same macro-state — this would accommodate different organ-system expression.

- **Supporting distinct failure modes:**
  - The joint-specific mechanisms in Ramundo2025 (MMP8, LTF, collagen degradation, M13 co-expression module) have no established role in fatigue or autonomic dysfunction. These are not "the same attractor expressed differently" — they are distinct molecular programs.
  - Fatigue-dominant PAIS signature markers (serotonin depletion, NK dysfunction, mitochondrial ATP reduction, small-fiber neuropathy) have not been measured in pCHIKV-CIJD patients.
  - The 2011 Galbraith head-to-head (EBV/RRV/Q-fever) found no shared gene expression across triggers even within the fatigue-phenotype category — adding an arthralgia phenotype makes cross-trigger molecular convergence even less likely.
  - PTLDS's arthralgic manifestations may be mechanistically distinct from its fatigue manifestations; the two outcomes in PTLDS should not be treated as one.

## Thoughts

- **Best current interpretation:** The two phenotype families most likely share an early upstream mechanism (impaired antiviral immune clearing → viral persistence → sustained inflammation) but diverge at the level of which organ system bears the inflammatory burden, with the downstream molecular programs being substantially distinct. This is consistent with h0001's "heterogeneous molecular configurations" framing but argues against using arthralgia-dominant data as direct positive evidence for the fatigue-attractor specifically.
- **Major uncertainty:** We do not know whether pCHIKV-CIJD patients also have co-occurring fatigue/PEM that was simply not measured, or whether the arthritis displaces the fatigue phenotype. If a substantial fraction of pCHIKV-CIJD patients also have post-exertional malaise or significant fatigue, the phenotypes overlap more than the case definition suggests.
- **Best test:** A study that measures BOTH joint inflammation AND fatigue/PEM in the same CHIKV cohort longitudinally would resolve this; an overlap would support the same-attractor view, while clean dissociation would support distinct failure modes.

## Connections to Project

- Related hypotheses: `hypothesis:0001-shared-dysregulated-attractor` (h0001 scope); `hypothesis:0002-tissue-reservoir-antigen-fragment` (shared upstream mechanism)
- Required data or analyses: Fatigue / PEM phenotyping in pCHIKV-CIJD or arthralgic-PTLDS cohorts; cell-type-resolved transcriptomics comparing arthritis-dominant vs fatigue-dominant PAIS in matched CHIKV cohorts.
- Priority level: Medium — affects h0001 interpretation and cross-trigger matrix design, but does not block existing computational work.

## Related

- Topic notes: `topic:shared-failure-mode-across-pais`, `topic:pais-case-definition-heterogeneity`
- Article notes: `paper:Ramundo2025` (source); `paper:Chang2024` (post-chikungunya T-cell/cytokine companion); `search:0002` (cross-pathogen matrix); `discussion:0002` (scope tension item 3)
- Methods/Datasets: PRJNA1001790 (pCHIKV-CIJD whole-blood RNA-seq; lacks fatigue phenotyping)
