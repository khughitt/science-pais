---
id: question:0024-nlrp3-inflammasome-and-gasdermin-d-pyroptosis-as-a-self-amplifying-il-1
kind: question
title: "NLRP3 inflammasome and gasdermin-D pyroptosis as a self-amplifying IL-1\u03B2\
  /IL-18 loop sustaining PAIS without viremia"
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Christ2018
- cite:Saeed2014
origins:
- type: assistant
  ref: explore-ideas-mechanism
related:
- hypothesis:0019-cgas-sting-nlrp3-sterile-innate-sensing-driver
created: '2026-07-04'
updated: '2026-07-16'
added_by: explore-ideas:claude-opus-4-8:cand-mechanism-nlrp3-pyroptosis-selfamplify
lens_views:
- lens: mechanism
  rationale: "The project lists NF-\u03BAB/TNF, IL-6 and complement as active pathways\
    \ but does not name the NLRP3 \u2192 caspase-1 \u2192 IL-1\u03B2/IL-18 \u2192\
    \ gasdermin-D \u2192 pyroptotic-DAMP-release chain, which propagates without live\
    \ virus. This is partly distinct from the IL-6/NF-\u03BAB axis: NLRP3-specific\
    \ inhibitors (MCC950, colchicine) do not fully overlap JAK/TNF blockade, predicting\
    \ a pharmacologically separable effect on the neuropsychiatric cluster. Distinct\
    \ from hypothesis:0003 (which concerns the adaptive antigen/exhaustion loop).\n"
  origin_ref: explore-ideas-mechanism
---
# NLRP3 inflammasome and gasdermin-D pyroptosis as a self-amplifying IL-1β/IL-18 loop sustaining PAIS without viremia

## Summary

Does an NLRP3 → caspase-1 → IL-1β/IL-18 → gasdermin-D → pyroptotic-DAMP-release chain form a self-amplifying inflammatory loop that sustains PAIS *without* ongoing viremia? The mechanistic appeal is that NLRP3-specific inhibitors (MCC950, colchicine) do not fully overlap JAK/TNF blockade, predicting a pharmacologically separable effect. This question is homed under `topic:innate-immune-memory-trained-immunity-in-pais` as the q0024 sub-axis.

## Current Evidence

- **Grounded — NLRP3 as a functional inducer of central training.** Christ2018 (Cell) showed that Western-diet-induced central myeloid training in *Ldlr⁻/⁻* mice is **NLRP3-dependent**: *Nlrp3⁻/⁻* mice fail to develop the GMP expansion and progenitor transcriptomic reprogramming. This grounds NLRP3 as a *required upstream inducer* of a durable trained/reprogrammed myeloid state driven by a sterile stimulus — a relevant analogy for antigen-independent PAIS persistence [@Christ2018].
- **NOT grounded — a NLRP3-locus chromatin imprint in trained cells.** The often-repeated claim that trained monocytes carry elevated H3K4me3/accessibility at the NLRP3 or pro-IL-1β promoter (eliminating the need for NF-κB priming) is **not demonstrated in the primary epigenomic literature** (t112 re-sourcing, 2026-07). Christ2018's ATAC-seq opens *Tet2/Tlr4*, not NLRP3; Saeed2014's training-specific enhancer signature is metabolic/cAMP and its IL-1β result is a monocyte→macrophage differentiation finding, not a training-specific locus mark [@Saeed2014].
- **Conflicting/absent — PAIS-specific test.** The DAMP-driven positive-feedback loop (GSDMD pores → IL-1α/ATP/mtDNA/HMGB1 release → re-training / cGAS-STING re-engagement) is mechanistically coherent but has **not been tested in any PAIS system**.

## Thoughts

- Best current interpretation: NLRP3's link to durable myeloid reprogramming is real but *functional/genetic*, not a demonstrated epigenetic imprint at the sensor locus — cite it accordingly.
- Major remaining uncertainty: whether the loop operates in PAIS at all, and whether NLRP3-selective inhibition produces a separable clinical effect from JAK/TNF blockade.

## Connections to Project

- Related hypotheses: `hypothesis:0003` (immune-exhaustion feedback; the sterile self-sustaining branch), `hypothesis:0001` (shared attractor maintenance).
- Required datasets: none yet.
- Required analyses: none yet.
- Priority level: P3 (mechanistic-hypothesis maturity).

## Related

- Topic notes: `topic:innate-immune-memory-trained-immunity-in-pais` (q0024 sub-axis)
- Article notes: `paper:Christ2018`, `paper:Saeed2014`
- Methods/Datasets:
