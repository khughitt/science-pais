---
id: question:0023-cgas-sting-cytosolic-dna-sensing-as-upstream-driver-of-persistent-type-i
kind: question
title: cGAS-STING cytosolic DNA sensing as upstream driver of persistent type I IFN
  in PAIS
status: active
ontology_terms: []
datasets: []
source_refs: []
origins:
- type: assistant
  ref: explore-ideas-mechanism
related: []
created: '2026-07-04'
updated: '2026-07-05'
added_by: explore-ideas:claude-opus-4-8:cand-mechanism-cgas-sting-ifni-driver
lens_views:
- lens: mechanism
  rationale: "The project names persistent IFN-I/JAK-STAT as downstream outputs but\
    \ does not name the innate sensor that initiates and sustains the signal. cGAS\
    \ detects cytoplasmic dsDNA and drives STING\u2192TBK1\u2192IRF3\u2192IFN-I independently\
    \ of active replication; SARS-CoV-2 releases mtDNA that activates it. Naming cGAS-STING\
    \ makes the loop pharmacologically actionable (STING antagonists/cGAS inhibitors)\
    \ without globally suppressing antiviral immunity, and it is also engaged by EBV\
    \ reactivation and Borrelia-induced DNA damage \u2014 a candidate shared cross-trigger\
    \ step. Sharpens the \"what drives IFN-I\" gap left open by question:0006.\n"
  origin_ref: explore-ideas-mechanism
---
# cGAS-STING cytosolic DNA sensing as upstream driver of persistent type I IFN in PAIS

## Summary

Is cytosolic-DNA sensing via cGAS → STING → TBK1 → IRF3 the innate sensor that initiates and *sustains* the persistent type-I IFN signature in PAIS — without requiring active viral replication? Naming this sensor would make the loop pharmacologically actionable (STING antagonists / cGAS inhibitors) without globally suppressing antiviral immunity. It is also engaged by EBV reactivation and Borrelia-induced DNA damage — a candidate shared cross-trigger step.

## Current Evidence

- **Legitimate on general innate-immunology grounds.** mtDNA / micronuclear dsDNA / viral nucleic-acid fragments do activate cGAS-STING → IFN-I independent of replication; SARS-CoV-2 is reported to release mtDNA that engages this axis. The question stands on its own as an "upstream driver of persistent IFN-I" candidate.
- **Trained-immunity locus grounding was sought and NOT found (t112, 2026-07).** A dedicated literature pass found **no primary study reporting chromatin accessibility or activating histone marks at cGAS / STING (TMEM173) / IRF / ISG loci in trained myeloid cells**. The only primary STING↔trained-immunity link is *functional* (STING agonism, e.g. c-di-AMP-overexpressing BCG, augments training; type-I-IFN signaling gates β-glucan-driven hematopoietic expansion) — no locus-level epigenomic readout at the sensor loci exists.
- **Consequence:** the earlier framing that trained HSPCs carry elevated STING/IFN-locus accessibility, or that a chronic-STING chromatin imprint sustains IFN-I without ongoing ligand, is a **hypothesis, not an evidenced link**. This sub-branch has been *severed* from the trained-immunity epigenomic axis in `topic:innate-immune-memory-trained-immunity-in-pais` pending primary locus-level evidence.

## Thoughts

- Best current interpretation: keep q0023 as a general-immunology IFN-I-driver question; do **not** present it as an established trained-immunity epigenomic sub-mechanism.
- Major remaining uncertainty: whether cGAS-STING is upstream (seeding signal) or downstream (trained-cell output) of any myeloid reprogramming in PAIS — untested.

## Connections to Project

- Related hypotheses: `hypothesis:0003` (sterile self-sustaining stimulus branch), `question:0006` (JAK-STAT/IFN driver-vs-marker).
- Required datasets: none yet.
- Required analyses: none yet.
- Priority level: P3.

## Related

- Topic notes: `topic:innate-immune-memory-trained-immunity-in-pais` (q0023 sub-axis, grounding severed)
- Article notes:
- Methods/Datasets:
