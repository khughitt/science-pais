---
id: paper:EatonFitch2024
kind: paper
title: Immune exhaustion in ME/CFS and long COVID
status: active
ontology_terms:
- ME/CFS
- long COVID
- immune exhaustion
- PBMC transcriptomics
- NanoString
- type I interferon signaling
- type II interferon signaling
- cytokine signaling
- antigen presentation
- Tregs
- exhausted CD8 cells
dataset_usage: []
datasets: []
source_refs:
- cite:EatonFitch2024
related:
- question:0006-jak-stat-il6-driver-vs-marker
- hypothesis:0003-immune-exhaustion-feedback
- proposition:0036-non-covid-pais-partially-recapitulate-ifn-cytokine-exhaustion-axis
- topic:long-covid-immune-dysregulation
- topic:mecfs-long-covid-convergence
- topic:shared-failure-mode-across-pais
created: '2026-06-26'
updated: '2026-06-26'
---
# Immune exhaustion in ME/CFS and long COVID

- **Authors:** Natalie Eaton-Fitch, Penny Rudd, Teagan Er, Livia Hool, Lara Herrero, Sonya Marshall-Gradisnik
- **Year:** 2024
- **Journal:** JCI Insight, 9(20):e183810
- **DOI:** 10.1172/jci.insight.183810
- **BibTeX key:** EatonFitch2024
- **Source:** JCI Insight XML/HTML, read 2026-06-26.

## Key Contribution

This pilot study concurrently profiled immune-exhaustion gene expression in PBMCs from ME/CFS
participants (n=14), long-COVID participants (n=15), and healthy controls (n=18) using the NanoString
nCounter Immune Exhaustion panel. The paper is useful because it measures both diseases under the same
assay rather than inferring ME/CFS/LC convergence across separate platforms.

The central result is **partial recurrence, not identity**. Both ME/CFS and long COVID show immune-
exhaustion/pathway abnormalities involving IFN, cytokine, CTLA4, NF-kB, and complement signaling, with
Treg/exhausted-CD8 signals, but the differential genes and top canonical pathways are not the same.

## Methods

Participants with ME/CFS were screened by Fukuda, Canadian Consensus Criteria, and International
Consensus Criteria, and were included if they fulfilled CCC and/or ICC plus physician diagnosis. Long-COVID
participants fulfilled the WHO post-COVID-19 condition definition. Healthy controls reported no chronic
diagnosis.

PBMCs were isolated from EDTA blood, frozen, and used for RNA extraction. Gene expression was measured with
the NanoString nCounter Immune Exhaustion panel, which covers 785 genes related to T-cell, B-cell, and NK
cell exhaustion. Differential expression used Rosalind Bio with housekeeping-gene normalization; reported
filters were fold-change >1.5 or < -1.5 and p < 0.05. Ingenuity Pathway Analysis was used for canonical
pathway and network interpretation. Data are available as GEO GSE275334.

## Key Findings

**Cohort comparability.** The study included 18 healthy controls, 14 ME/CFS participants, and 15
long-COVID participants. Age, sex, and education were not significantly different. BMI differed, with
lower BMI in controls than in long COVID.

**Long COVID differential expression.** Twenty-nine genes differed from healthy controls: 15 upregulated
and 14 downregulated. Strongly downregulated genes included HLA-DQA1 and HLA-DQB1; KIR2DL5A/B was the
largest upregulated gene.

**ME/CFS differential expression.** Fourteen genes differed from healthy controls: 5 upregulated and 9
downregulated. Downregulated genes included IFNA4/7/10/17/21, IGHG1, and IFNA6; CEACAM3 was the largest
upregulated gene. The authors interpret the ME/CFS pattern as IFN-signaling and immunoglobulin
downregulation consistent with immune suppression/exhaustion.

**Overlapping pathway themes.** Gene-set analysis identified overlap between long COVID and ME/CFS in
chemokine signaling, type I and II IFN, IL signaling, CTLA4 signaling, NF-kB signaling, and complement.
The discussion explicitly frames these overlaps as shared immune-exhaustion/pathway dysregulation across
the two syndromes.

**Cell-type inference.** Gene-expression-derived cell abundance analyses implicated exhausted CD8 cells
and Tregs in ME/CFS, and Treg differences in both ME/CFS and long COVID.

## Relevance

**question:0006.** This is a direct same-assay ME/CFS/long-COVID comparison for the cross-PAIS half of
q0006. It supports the weak claim that non-COVID PAIS can partially recapitulate the inflammatory/IFN/
exhaustion axis seen in long COVID, but it does not establish the full Aid2025 state. It does not measure
JAK-STAT/IL-6 pathway activity as a primary readout, does not run IFN-I stimulation assays, and does not
test pathway inhibition.

**hypothesis:0003.** The paper is compatible with h0003's immune-exhaustion loop, especially the
co-occurrence of IFN/cytokine pathway dysregulation and exhaustion markers. It should not promote h0003:
sample size is small, identification is observational, and the causal driver claim remains gated on the
JAK1-inhibitor pre-registration.

## Limitations

- Small pilot cohorts (ME/CFS n=14, LC n=15, HC n=18) limit precision and subgroup analysis.
- PBMC-only transcriptomics cannot localize tissue or myeloid sources of persistent inflammatory tone.
- The NanoString panel is exhaustion-focused, so it is not an unbiased immune transcriptome.
- The result is cross-sectional and observational; it does not distinguish upstream driver from marker.
- The overlapping pathways are broad; disease-specific gene/pathway differences remain substantial.
- Patent conflicts are disclosed for related diagnostic applications.

## Model / Tool Availability

NanoString RNA data are available through GEO accession **GSE275334**. Supplemental data files are linked
from the JCI Insight article.

## Follow-up

- Reanalyze GSE275334 with a pre-specified Hallmark IL6-JAK-STAT3, IFN-alpha, IFN-gamma, and exhaustion
  score set to quantify how much of the Aid2025 LC signature recurs in ME/CFS.
- Compare the NanoString result with Che2025's exercise-provoked ME/CFS immune-exhaustion signal and
  Keijmel2016's Coxiella-stimulated QFS IFN-gamma signal.
- Do not use this study for q0006's driver-vs-marker leg; it supplies pathway recurrence only.
