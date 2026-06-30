---
id: topic:long-covid-immune-dysregulation
type: topic
title: Long COVID Immune Dysregulation and Inflammatory Signatures
status: active
ontology_terms:
- long COVID
- immune dysregulation
- inflammation
- complement
- interferon
- T cell exhaustion
- proteomics
- biomarkers
datasets: []
related:
- topic:shared-failure-mode-across-pais
- topic:antigen-pathogen-persistence
- topic:pediatric-long-covid-and-misc
- immunity:research-question:immune-homeostasis-and-dysregulation
source_refs:
- cite:Klein2023
- cite:Aid2025
- cite:Talla2023
- cite:Ryan2022
- cite:CerviaHasler2024
- cite:Cruz2025
- cite:Ganesh2022
- cite:Patrascu2025
- cite:Truong2025
created: '2026-06-11'
updated: '2026-06-26'
---
# Long COVID Immune Dysregulation and Inflammatory Signatures

## Summary

Long COVID (PASC) is the most deeply profiled PAIS, and multi-omic immune studies now provide the strongest molecular evidence in the field that post-infectious illness is a state of *failed immune resolution* rather than ongoing acute infection. Across independent cohorts, long COVID is marked by persistent activation of antiviral/inflammatory pathways (type I/II IFN, JAK-STAT, IL-6, complement, NF-kB/TNF) alongside markers of immune exhaustion, with no detectable replicating virus in blood (Aid2025, Talla2023, CerviaHasler2024, Klein2023). Several signatures discriminate case status with high accuracy (Klein2023 LASSO AUC 0.94; CerviaHasler2024 and Talla2023 biomarker AUROCs 0.74-0.87). The evidence strongly supports immune dysregulation as a defining feature; what is contested is whether any single axis is the *driver* versus a marker, whether distinct inflammatory subtypes require different therapy, and whether these signatures generalize to non-COVID PAIS [@Aid2025; @Talla2023; @CerviaHasler2024; @Klein2023].

## Key Concepts

**Persistent inflammatory pathway activation without circulating virus.** Aid2025 (two cohorts, discovery n=142, validation n=38) shows JAK-STAT, IL-6, IFN, and complement pathways remain active beyond 180 days with no detectable circulating virus, paired with CD8+ T-cell exhaustion — supporting a chronic-dysregulation model and motivating a JAK1-inhibitor trial. This reframes IL-6/JAK-STAT as a candidate proximal driver, not just a marker [@Aid2025].

**Inflammatory endotypes.** Long COVID is not immunologically monolithic. Talla2023 (Olink, n=55, validated in INCOV) identifies two persistent inflammatory subgroups (~65% of PASC) — one type II IFN/NF-kB/TNF-dominant, one neutrophil-activation/NETosis-dominant — and a three-protein panel (CCL7, CD40LG, S100A12) separating inflammatory from non-inflammatory PASC. The remaining ~35% non-inflammatory subgroup is mechanistically distinct and underexplored [@Talla2023].

**Complement and thromboinflammation.** CerviaHasler2024 (>6,500 proteins, 268 longitudinal samples) defines active long COVID by a terminal complement complex imbalance (elevated C5bC6, decreased soluble C7, indicating membrane insertion) plus thromboinflammation (high vWF, low ADAMTS13, monocyte-platelet aggregates) and classical-complement activation linked to anti-CMV/EBV IgG. The C5bC6/C7 and vWF/ADAMTS13 ratios are top machine-learning biomarkers [@CerviaHasler2024].

**Blunted type I interferon and platelet/megakaryocyte signature.** Ryan2022 (longitudinal, ~130 immune subpopulations) finds broad perturbation in all convalescents to ~6 months, but a *specific* long-COVID-referral signature at 24 weeks: IFN-I suppression (MX1, OAS3, OASL), platelet/megakaryocyte transcriptional downregulation, and elevated S100B — instantiating divergent, incomplete recovery [@Ryan2022].

**Neuroendocrine and herpesvirus axes.** Klein2023 (MY-LC, n=275) reports markedly reduced cortisol (single strongest LC predictor), elevated non-conventional monocytes, exaggerated anti-spike humoral responses, and EBV-reactivation markers — connecting immune dysregulation to HPA-axis failure [@Klein2023].

**Persistent IL-6 and central sensitization.** Ganesh2022 (Mayo, n=108) documents IL-6 elevation in 61% at ~5 months (more common in women), often discordant with CRP/ESR, framing post-COVID syndrome as a central-sensitization condition [@Ganesh2022].

**Organ-stratified biomarkers and distinct trajectories.** Patrascu2025 organizes 20 biomarkers by organ system (NfL/GFAP, KL-6/SP-D, I-FABP/zonulin, CRP/IL-6/D-dimer/suPAR/NETs), offering a multi-axis phenotyping framework. Cruz2025 (n=113) shows post-COVID pulmonary sequelae and systemic long COVID are *biologically distinct* trajectories sharing only a core antiviral residue (IFN-γ, IL-8, MCP-4) [@Patrascu2025; @Cruz2025].

**MIS-C recovery contrast.** Truong2025/MUSIC anchors the pediatric hyperinflammatory comparator: MIS-C
can present with severe cardiac/inflammatory involvement, but most measured cardiac and global health
outcomes normalize or return near baseline by 6 months. This makes MIS-C useful for immune-resolution
biology while cautioning against pooling it with chronic long COVID.

## Current State of Knowledge

### What the evidence supports

- Long COVID involves persistent, multi-pathway immune activation (IFN, JAK-STAT/IL-6, complement, NF-kB/TNF, neutrophil/NETosis) detectable months post-infection across independent cohorts, with no replicating virus in blood (Aid2025, Talla2023, CerviaHasler2024, Klein2023).
- The signatures are discriminating enough to build high-AUC classifiers (Klein2023, CerviaHasler2024, Talla2023), supporting a real, reproducible biological state.
- Long COVID is heterogeneous: at least two inflammatory endotypes plus a sizeable non-inflammatory subgroup (Talla2023), and pulmonary vs systemic trajectories diverge within the same trigger (Cruz2025).
- MIS-C is immune-mediated and post-infectious but has a different time course from chronic PASC in most
  children (Truong2025).

### What is contested or unresolved

- **Driver vs marker.** Whether IL-6/JAK-STAT (Aid2025), complement (CerviaHasler2024), or IFN-I suppression (Ryan2022) is causal, and which is upstream, is not established; the JAK1-inhibitor trial (NCT06597396) is a direct test for one axis.
- **Cortisol mechanism.** Klein2023's low cortisol without compensatory ACTH could be primary HPA defect, peripheral metabolism, or secondary to inflammation; single-timepoint sampling cannot resolve it.
- **Generalizability.** All these signatures were derived in COVID-19; whether the IL-6, complement, IFN-I-suppression, or three-protein panels mark a *shared* PAIS state (ME/CFS, PTLDS) is untested and central to the project.

### Tensions between papers

Ryan2022 reports IFN-I *suppression* at 6 months as the long-COVID-specific signal, whereas Aid2025 and Talla2023 emphasize persistent IFN/inflammatory *activation* — likely reconcilable by timing, compartment (blood transcriptome vs plasma proteome), and endotype, but currently an unresolved apparent contradiction. Cruz2025 cautions that even within one pathogen the "long COVID immune signature" is not unitary.

## Controversies and Open Questions

- Is the JAK-STAT/IL-6 axis a proximal driver whose inhibition resolves symptoms, or a downstream marker (Aid2025)?
- Do the inflammatory endotypes (Talla2023) map onto antigen-persistence vs autoimmune upstream mechanisms, predicting antiviral vs immunomodulatory responsiveness?
- Why does MIS-C often resolve after severe hyperinflammation while chronic PASC persists in a smaller
  subset?
- Which cell type sustains the chronic IL-6/JAK-STAT signal — single-cell resolution is needed (Aid2025)?
- Do these blood signatures track symptom severity and recovery, i.e. can any serve as a validated surrogate endpoint (a gap flagged in Peluso2024b)?

## Relevance to This Project

This topic supplies the molecular substrate for the project's "failed immune homeostasis" frame and is the best-characterized instance of the shared-failure-mode question (`topic:shared-failure-mode-across-pais`). The persistent-activation-without-virus finding (Aid2025) and the antiviral residue shared across trajectories (Cruz2025) link to `topic:antigen-pathogen-persistence` and to hypotheses `0001` (self-sustaining attractor) and `0003` (immune-exhaustion feedback). It connects to the peer owner `immunity:research-question:immune-homeostasis-and-dysregulation` for the general biology of non-resolving inflammation.

## Key References

- Aid2025 — persistent JAK-STAT/IL-6/IFN/complement + CD8 exhaustion >180d, no circulating virus; therapeutic-target validation.
- Talla2023 — two inflammatory PASC endotypes; CCL7/CD40LG/S100A12 panel.
- CerviaHasler2024 — terminal complement imbalance + thromboinflammation; C5bC6/C7 and vWF/ADAMTS13 ratios.
- Ryan2022 — IFN-I suppression + platelet/megakaryocyte downregulation as a 24-week long-COVID-referral signature.
- Klein2023 — multi-omic LC signature (low cortisol, non-conventional monocytes, EBV); AUC 0.94.
- Cruz2025; Ganesh2022; Patrascu2025 — distinct trajectories, persistent IL-6, organ-stratified biomarker framework.
- Truong2025 — MIS-C as pediatric hyperinflammatory recovery contrast.
