---
id: question:0076-ip10-cxcl10-omicron-persistence-antigen-vs-sterile
kind: question
title: Is persistent IP-10/CXCL10 elevation after mild Omicron breakthrough driven
  by residual antigen or sterile innate sensing?
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Vacharathit2025
related:
- hypothesis:0019-cgas-sting-nlrp3-sterile-innate-sensing-driver
- hypothesis:0001-shared-dysregulated-attractor
created: '2026-07-10'
updated: '2026-07-10'
---

# Is persistent IP-10/CXCL10 elevation after mild Omicron breakthrough driven by residual antigen or sterile innate sensing?

## Summary

Vacharathit 2025 (cite:Vacharathit2025) documents persistent IP-10/CXCL10 elevation (7–10× above pre-pandemic baseline) in mild, vaccinated Omicron breakthrough cases for up to 6–8 months post-infection — a pattern not seen after earlier SARS-CoV-2 variant waves. This question asks whether that sustained IP-10/CXCL10 output reflects ongoing antigen stimulation (residual SARS-CoV-2 RNA, protein, or fragments driving IFN-γ/IFN-I and IP-10 production) or a sterile self-sustaining innate sensing loop (cGAS-STING or NLRP3 engaged by host-derived DAMPs — mitochondrial DNA, HMGB1 — independent of replicating virus). The distinction matters because these two mechanisms predict different intervention targets and different clinical trajectories.

## Why It Matters

- **Intervention target:** Antigen-driven IP-10 would be addressed by antiviral agents (e.g., extended Paxlovid, vaccines), while sterile-sensing-driven IP-10 would require sensor-selective agents (STING antagonists, NLRP3 inhibitors such as colchicine/MCC950) — directly relevant to `hypothesis:0019`.
- **Prognosis and biomarker interpretation:** If IP-10 reflects sterile sustained innate activation, it may flag a sub-clinical immune-state displacement with long-term risk of autoimmune conversion (linking to `hypothesis:0009`); if it reflects antigen clearance kinetics, it may resolve naturally without intervention.
- **Risk if unanswered:** IP-10 monitoring in mild Omicron cases cannot be usefully interpreted for clinical or research decisions until the mechanism is defined; conflating the two pathways risks targeting the wrong node.

## Current Evidence

- **Supporting sterile innate sensing:** IP-10 elevation persists well beyond expected antigen clearance in mild cases (6–8 months), dissociated from clinical symptoms and from Long COVID scores in Vacharathit 2025; this temporal dissociation is more consistent with a self-amplifying sterile loop than ongoing viral replication. Domizio 2022 shows SARS-CoV-2 induces endothelial cGAS-STING activation by mitochondrial DNA — sterile-sensor precedent in acute COVID (acute, not PAIS context). BNT162b2 vaccination (mRNA) triggers an IL-15–IFN-γ–IP-10 innate signature within 24–48 h (Bergamaschi 2021); mRNA-vaccinated Omicron breakthrough patients had lower Long COVID scores in Vacharathit 2025, suggesting the mRNA-primed innate state may modulate IP-10 kinetics.
- **Supporting antigen-driven:** Prior longitudinal studies show SARS-CoV-2 nucleocapsid RNA and/or antigen can persist in gut, lymph nodes, and plasma for months in a subset of individuals even after mild COVID (relevant to `hypothesis:0002-tissue-reservoir-antigen-fragment`). If antigen persists, it can sustain IFN-γ output from specific T cells, directly inducing IP-10 in bystander cells. Vacharathit 2025 did not measure viral antigen or RNA persistence, leaving this route unexcluded.
- **Against a clear signal:** The Vacharathit cohort is small (n=30 Omicron), data are confidential, and IP-10 levels did not statistically correlate with Long COVID scores — a mild but relevant constraint suggesting IP-10 elevation may not fully track clinical disease burden, complicating mechanistic inference.

## Thoughts

- **Best current interpretation:** The temporal profile (7–10× baseline at 6–8 months in mild, largely symptom-resolved individuals) favors a sterile sensing component — but antigen persistence and vaccine-mediated innate priming are not excluded and may co-operate. The most parsimonious reading is that mRNA vaccination upregulates an IL-15–IFN-γ–IP-10 innate axis that prolongs IP-10 expression even after antigen clearance; whether this is beneficial (adaptive resolution) or creates a sub-clinical risk state is unknown.
- **Major uncertainty:** No study has yet measured cGAMP, phospho-TBK1/IRF3, cleaved gasdermin-D, or SARS-CoV-2 antigen/RNA persistence simultaneously with IP-10 in the same mild Omicron breakthrough cohort. Until such data exist, the antigen-driven vs. sterile-sensing distinction cannot be empirically adjudicated.

## Connections to Project

- Related hypotheses: `hypothesis:0019-cgas-sting-nlrp3-sterile-innate-sensing-driver` (primary); `hypothesis:0001-shared-dysregulated-attractor` (IP-10 as sub-clinical displacement marker); `hypothesis:0002-tissue-reservoir-antigen-fragment` (antigen-driven alternative); `hypothesis:0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune`
- Required data or analyses: Co-measurement of (i) SARS-CoV-2 spike/nucleocapsid antigen or RNA in plasma/stool; (ii) cGAMP, phospho-TBK1, or ISG scores; (iii) IP-10 longitudinally — in the same mild Omicron breakthrough cohort. A sensor-selective intervention trial (STING antagonist or colchicine) with IP-10 as a pharmacodynamic endpoint would be most decisive.
- Priority level: Medium-high — IP-10 is one of the most actionable candidate PAIS biomarkers and the mechanism question gates whether antiviral or innate-resolution treatment strategies are appropriate.

## Related

- Topic notes: `topic:innate-immune-memory-trained-immunity-in-pais`
- Article notes: `paper:Vacharathit2025`; Domizio 2022 (cGAS-STING in acute COVID endothelium); Bergamaschi 2021 (mRNA vaccine IP-10 innate axis)
- Methods/Datasets: Would require a longitudinal mild-COVID cohort with stored plasma and consent for antigen and nucleic-acid assays; co-assay of IP-10 and cGAMP feasible from the same Luminex run.
