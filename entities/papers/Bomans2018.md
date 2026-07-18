---
id: paper:Bomans2018
kind: paper
title: "Sepsis Induces a Long-Lasting State of Trained Immunity in Bone Marrow Monocytes"
status: active
paper_kind: ""
ontology_terms:
- trained immunity
- innate immune memory
- bone marrow monocytes
- hematopoietic stem and progenitor cells
- granulocyte-monocyte progenitors
- myelopoiesis
- sepsis
- post-sepsis syndrome
- cecal ligation and puncture
- glycolytic reprogramming
- aerobic glycolysis
- immune tolerance
- compartmentalized innate immunity
- transcriptomic reprogramming
- post-acute infection syndrome
source_refs:
- cite:Bomans2018
related:
- topic:innate-immune-memory-trained-immunity-in-pais
- question:0026-acute-infection-il-6-stat3-imprinting-of-hematopoietic-progenitors
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0003-immune-exhaustion-feedback
created: "2026-07-18"
updated: "2026-07-18"
---

# Sepsis Induces a Long-Lasting State of Trained Immunity in Bone Marrow Monocytes

<!--
- **Authors:** Katharina Bomans, Judith Schenz, Isabella Sztwiertnia, Dominik Schaack, Markus Alexander Weigand, Florian Uhle
- **Year:** 2018
- **Journal:** Frontiers in Immunology, Vol. 9, p. 2685
- **DOI:** https://doi.org/10.3389/fimmu.2018.02685
- **PMID:** 30510555
- **PMCID:** PMC6254543
- **BibTeX key:** Bomans2018
- **Source:** Europe PMC full text (XML via science paper-fetch, read 2026-07-18)
- **Model organism note:** This is a murine study (male C57BL/6 mice, 12 weeks old, CLP model). There is NO human arm in this paper, despite the BibTeX note in references.bib saying "with human validation"; that note is inaccurate — the study is purely preclinical.
-->

## Key Contribution

This paper provides the first direct demonstration — in a clinically relevant post-sepsis mouse model assessed at three months post-insult — that sepsis durably imprints **naive bone marrow monocytes** in a trained-immunity phenotype (enhanced LPS-stimulated TNF and IL-6 production, elevated basal glycolysis, sustained transcriptomic reprogramming of 367 genes) even as peripheral blood monocytes remain systemically unaltered. The critical conceptual contribution for this project is the **dual-compartment divergence**: bone marrow naive monocytes are trained, while circulating whole-blood monocytes do not exhibit altered cytokine output to LPS challenge. This compartment-dependent finding — central (bone marrow-level) training coexisting with unchanged peripheral responsiveness — provides the first direct experimental evidence for the mechanistic model invoked in `topic:innate-immune-memory-trained-immunity-in-pais` to explain the tolerance/training paradox observed in post-infectious patients. It also establishes that HSPC-level trained immunity after severe infection is not a COVID-specific phenomenon, thereby load-bearing for the cross-trigger generalization arm of the project's shared-attractor hypothesis.

**Organism / design boundary.** Bomans2018 is a murine experimental study with no human arm. All claims about trained bone marrow monocytes, GMP expansion, glycolysis, and transcriptomic reprogramming derive from C57BL/6 mice 12 weeks after CLP. Extrapolation to human post-sepsis syndrome (PICS) or to other PAIS is supported by mechanistic analogy and consistency with β-glucan training paradigms — not by data in this paper.

## Methods

**Animal model.** Polymicrobial cecal ligation and puncture (CLP) in 12-week-old male C57BL/6 mice. CLP is the standard murine model of polymicrobial abdominal sepsis; this was a "mild" CLP approach. Overall mortality in the CLP group was 28% (4/15 animals); no sham animal died. Enhanced body-weight loss and a higher clinical score confirmed successful sepsis induction. Mice were assessed 12 weeks (3 months) after CLP or sham surgery — a timepoint the authors describe as a "clinically relevant post-ICU timeframe."

**Sample sizes.** n = 9 per group for flow cytometry, cytokine ELISA (whole blood and bone marrow monocyte stimulation), and Seahorse metabolic assays. n = 3 per group for RNA-seq (technical replication only; small cohort).

**Immune cell profiling.** Flow cytometry of spleen, whole blood, and bone marrow for monocyte subsets (CD11b+ F4/80−, Ly6C+ inflammatory, Ly6C− alternative), hematopoietic progenitor populations (LT-HSC, ST-HSC, MPP, CMP, MEP, GMP), and regulatory T cells (CD4+ CD25+ CD127dim Tregs).

**Functional training assay.** MACS-sorted bone marrow monocytes were stimulated ex vivo with LPS or saline for 24 hours; TNF and IL-6 levels measured by ELISA. Whole blood was similarly stimulated to assess the systemic compartment separately from the bone marrow compartment.

**Metabolic analysis.** Seahorse extracellular flux assay on unstimulated bone marrow monocytes: glycolytic proton efflux rate (basal glycolysis and compensatory glycolysis), mitochondrial oxygen consumption rate. Cells were analyzed in the unstimulated (resting) state — not after LPS re-stimulation.

**Transcriptomics (RNA-seq).** Whole-genome RNA-seq on naive (unstimulated) MACS-sorted bone marrow monocytes from CLP and sham mice. Differential expression threshold: linear fold change >1.5, p < 0.02. n = 3 per group. Gene ontology (GO) enrichment analysis of up- and down-regulated gene sets.

**No epigenomic profiling.** The paper explicitly acknowledges that epigenetic reprogramming — ChIP-seq, ATAC-seq, DNA methylation — was not analyzed. Epigenetics is identified as an open question for future investigation.

## Key Findings

### 1. Splenomegaly and altered splenic monocyte composition persist 3 months post-CLP

CLP mice showed markedly enlarged, heavier spleens at 12 weeks vs. sham. Splenic total monocytes (CD11b+ F4/80−) and inflammatory monocytes (Ly6C+) were significantly increased; alternative monocytes (Ly6C−) were decreased. Splenic regulatory T cells (Tregs) were also elevated, indicating a co-existing immunosuppressive component in the lymphoid compartment.

### 2. The systemic blood monocyte response is unaltered (tolerance / no systemic training)

Flow cytometry of whole blood found no significant change in total, inflammatory, or alternative monocytes in CLP survivors vs. sham. Critically, LPS-stimulated whole blood showed **no difference in TNF-α or IL-6 output** between CLP and sham. This absence of a systemic trained or tolerance phenotype in blood is the pivotal contrast with bone marrow findings.

### 3. Bone marrow myelopoiesis is durably skewed toward the granulocyte-monocyte lineage

GMP (granulocyte-monocyte progenitors: LS−K CD16/32+ CD34+) were **significantly increased** in CLP bone marrow at 12 weeks (Figure 3F). LT-HSCs were unchanged; ST-HSCs were slightly decreased; MPP/CMP/MEP showed only subtle differences. This selective GMP enrichment indicates a sustained late-stage myelopoiesis bias — consistent with the β-glucan training paradigm (Mitroulis et al. 2018) rather than the broad hematopoietic suppression observed acutely after sepsis.

### 4. Naive bone marrow monocytes exhibit the trained immunity functional phenotype (the paper's central claim)

MACS-sorted naive bone marrow monocytes from CLP mice produced significantly more TNF-α and IL-6 than sham controls after LPS stimulation (Figures 4A–B). This enhanced cytokine response in naive (never-stimulated) progeny monocytes from the bone marrow is the defining functional marker of trained immunity — the cells are pre-programmed by the septic insult to hyperrespond to a secondary stimulus.

### 5. Basal glycolysis is enhanced in bone marrow monocytes; mitochondrial function is unchanged

Seahorse analysis of unstimulated bone marrow monocytes showed **significantly elevated basal glycolysis** in CLP mice (Figure 4C–D); compensatory glycolysis (maximum glycolytic capacity) was not elevated. Mitochondrial indices (oxygen consumption) were not significantly altered. The authors note that the full aerobic glycolysis shift (Warburg) may require an LPS re-stimulation that was not performed; the cells appear glycolytically primed without full Warburg commitment at rest.

### 6. RNA-seq reveals a sustained 367-gene transcriptomic signature in trained bone marrow monocytes

367 genes were differentially expressed between CLP and sham bone marrow monocytes (73 upregulated, 294 downregulated; linear fold change >1.5, p < 0.02). PCA of these 367 genes shows clean group separation. Upregulated GO categories include "cell migration" and "response to cytokines"; downregulated categories include "positive regulation of cilium assembly" and "carbohydrate derivative metabolic process."

Key individually upregulated genes with mechanistic relevance to trained immunity:
- **MyD88** (TLR downstream adaptor → NF-κB → pro-inflammatory gene transcription): primes enhanced cytokine output to TLR ligands
- **Jak3** (JAK/STAT signaling → downstream of IL-6R among others): upregulation could amplify cytokine-mediated responses and hematopoietic development signals
- **HAL** (histidine deaminase → glutamate via urocanic acid): a source of glutamate for glutaminolysis → α-KG → TCA → fumarate accumulation, mechanistically aligned with the Arts2016 epigenetic memory pathway
- **GDA and XDH** (guanine deaminase, xanthine dehydrogenase → purine catabolism): likely compensating for excess purine synthesis from PPP restriction

Key downregulated gene:
- **RPE** (ribulose-phosphate 3-epimerase → non-oxidative PPP branch): downregulation drives PPP output toward purine synthesis for nucleotide demand in the trained-transcription state — consistent with the Arts2016 NMR finding that the non-oxidative PPP branch is inactive in trained immune cells

### 7. The dual-compartment finding: trained BM, unchanged blood

The paper's most conceptually important result for PAIS is the dissociation between (a) trained naive monocytes in bone marrow and elevated GMPs, and (b) unaltered LPS responsiveness in whole blood. The authors hypothesize that upon release from bone marrow, monocytes rapidly convert from inflammatory (Ly6C+) to alternative (Ly6C−) phenotype within one day, and the short half-life of peripheral monocytes plus potential humoral factors may "blur" the trained signal by the time cells exit the marrow into circulation. A slight increase in alternative monocytes in blood is noted (consistent with faster conversion or extended alternative-monocyte residence), but functional cytokine output is unchanged.

## Relevance

**`topic:innate-immune-memory-trained-immunity-in-pais` — the principal non-COVID PAIS parallel.** This paper is the primary empirical anchor for the claim that central (bone-marrow-level) trained immunity after severe infection is not COVID-specific: it demonstrates that a polymicrobial infection trigger (sepsis, CLP) can imprint the hematopoietic niche of the bone marrow in a durable trained state three months after the insult. Post-sepsis syndrome (PICS — post-intensive care syndrome) is a recognized PAIS variant with chronic fatigue, cognitive impairment, and functional limitation; Bomans2018 provides a direct mechanistic candidate for how the myeloid compartment could sustain inflammation in that context. Together with Cheong2023 (IL-6-driven COVID HSPC imprinting), it supports the claim in the topic that central training is a candidate cross-trigger mechanism — though only two triggers (sepsis and coronavirus) have been directly demonstrated in animal/human data to date.

**`question:0026` (IL-6/STAT3 HSPC imprinting) — non-COVID instance.** Question:0026 asks whether the IL-6/STAT3 → HSPC imprinting → hyperreactive monocyte axis generalizes beyond SARS-CoV-2. Bomans2018 shows that the downstream endpoint — trained bone marrow monocytes plus GMP expansion — occurs after polymicrobial sepsis in mice. The paper does not identify IL-6 or STAT3 as the mechanistic driver (it upregulates Jak3, which is part of JAK/STAT signaling, but does not test IL-6/STAT3 necessity). It is a cross-trigger parallel, not a mechanistic replication of the Cheong2023 IL-6 dependency. Strength of support for q0026: **functional parallel in a non-COVID trigger** (trained BM monocytes + GMP expansion), **not an IL-6/STAT3 mechanistic test** in this trigger.

**`hypothesis:0001` (shared dysregulated attractor) — cross-trigger generalization support.** The attractor hypothesis requires that distinct infection triggers can drive the same post-infectious failure mode. Bomans2018 provides non-COVID experimental evidence that a severe infectious insult can produce a durable myeloid trained phenotype in the bone marrow, offering a candidate shared mechanism that could hold the inflammatory state in an attractor-like configuration independent of the specific pathogen. This is mechanistic analogy support, not direct PAIS symptom evidence.

**`hypothesis:0003` (immune exhaustion feedback) — tolerance/training dual-compartment clarification.** The Bomans2018 dissociation between trained BM monocytes and unaltered peripheral blood cytokine response is directly relevant to the tolerance/training paradox noted in hypothesis:0003. Peripheral circulating monocytes may appear tolerized (as in post-septic immunosuppression), while simultaneously, naive monocytes arriving fresh from the bone marrow carry a trained epigenome — creating a constitutively hyperreactive myeloid output that is invisible when only blood is sampled. This compartment-dependent biology is likely to apply to other PAIS; it is currently not directly characterized in long COVID or ME/CFS patients.

**What this paper is NOT:**
- It is not a human study. The "human validation" reference in the project's BibTeX note is incorrect; all experiments are in mice.
- It does not measure epigenomic marks (no ChIP-seq, ATAC-seq, methylation); the epigenetic basis of the trained phenotype is inferred from the trained-immunity literature and from the transcriptomic changes, but is uncharacterized in this model.
- It does not link trained monocyte phenotype to any post-sepsis clinical outcome (PICS symptoms, cognitive impairment, fatigue, quality of life).
- It does not identify the mechanistic signal driving BM monocyte training after CLP (IL-6? DAMPs? microbial translocation? — speculative; not tested).
- It does not show tolerance or training in the same peripheral cell type; the whole-blood assay probes mixed circulating cells, not a pure monocyte sort from blood.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| CLP → trained naive BM monocytes (enhanced LPS-stimulated TNF, IL-6) | Non-COVID central trained immunity after infectious trigger | First demonstration in a non-COVID PAIS-relevant sepsis model |
| GMP expansion 3 months post-CLP | Durable myelopoiesis skewing toward inflammatory myeloid output | Same GMP readout as Cheong2023 and Christ2018 — a convergent structural finding |
| Enhanced basal glycolysis in unstimulated BM monocytes | Metabolic reprogramming of trained monocytes | Consistent with Warburg priming; compensatory glycolysis and mitochondrial indices unchanged at rest |
| 367-DEG transcriptomic signature (MyD88↑, Jak3↑, RPE↓) | Sustained innate-sensing and glycolytic-priming gene signature | Mechanistically consistent with trained-immunity framework; Jak3 JAK/STAT upregulation links to IL-6 signaling axis |
| BM monocytes trained, blood monocytes unaltered | Compartment-dependent tolerance/training divergence | Key conceptual contribution: explains why peripheral immune tolerance and central BM training coexist post-sepsis |
| 3-month persistence post-CLP | Antigen-independent maintenance (no ongoing septic insult at assessment) | Central training outlasts pathogen clearance in the murine CLP model |
| No epigenomic data (limitation) | Epigenetic basis inferred, not demonstrated | H3K4me3/ATAC-seq at BM monocytes post-CLP is an unmet experimental need |

## Limitations

**1. Mouse model only — no human post-sepsis data in this paper.** All results derive from male C57BL/6 mice 12 weeks after a single CLP procedure. Sex, strain, and species differences are all uncontrolled for PAIS extrapolation. The BibTeX note saying "with human validation" is inaccurate — no human subjects were studied.

**2. Small RNA-seq cohort (n = 3 per group).** The 367-gene transcriptomic signature is generated from n = 3 animals per group (no power calculation reported). With this sample size, many of the individual gene-level findings are under-powered and subject to high false-discovery risk. Replication of the transcriptomic signature in a larger cohort or an independent CLP dataset is needed before individual gene calls (MyD88, Jak3, HAL, etc.) are cited as established.

**3. No epigenomic profiling.** The central claim — that CLP induces epigenetic reprogramming in BM monocytes — is inferred from functional (enhanced cytokine output) and metabolic (glycolysis) data, and indirectly from the transcriptomic findings. ChIP-seq, ATAC-seq, or DNA methylation profiling of bone marrow monocytes from CLP mice would be required to establish the epigenetic mechanism directly and to determine which histone marks (H3K4me3, H3K27ac) are altered and at which genomic loci. The paper explicitly identifies this as a gap.

**4. No mechanistic identification of the training signal.** What drives bone marrow monocyte training after CLP is not identified. Candidate signals include: high acute IL-6 (consistent with Cheong2023); DAMPs from pyroptotic and necrotic cells; microbial translocation products (LPS, fungi); NLRP3-activating stimuli. None of these was tested in this paper. The mechanistic signal is entirely uncharacterized in the CLP model.

**5. Mild CLP model (28% mortality) — severity confound.** The authors note that "mild" CLP (25% lethality) was used. Higher bacterial burden / severity might produce different or stronger trained-immunity effects. The severity dependence of the trained BM phenotype — critical for understanding the dose-response relationship that would map to PAIS incidence — is not explored.

**6. Single timepoint (12 weeks / 3 months).** The paper assesses one timepoint post-CLP. Whether the trained phenotype is still present at 6 months, 12 months, or years post-sepsis (comparable to the 12-month HSPC imprint in Cheong2023) is not established. Whether the phenotype was already established earlier (e.g., 4–6 weeks) or represents a late-onset adaptive response is also unknown.

**7. No link to post-sepsis clinical outcomes.** The paper does not report any functional correlate between the trained BM monocyte phenotype and post-CLP morbidity, cognitive outcomes, functional status, or survival in secondary infection challenges. Whether the trained state is protective (better pathogen clearance) or harmful (inflammasome-driven organ damage, fatigue) in the post-sepsis context is not addressed.

**8. Whole-blood (not sorted-monocyte) assay for peripheral compartment.** The peripheral LPS assay uses unsorted whole blood rather than MACS-sorted blood monocytes. This means that cytokine contributions from granulocytes, NK cells, and lymphocytes are included, potentially obscuring a weaker monocyte-specific training signal in blood.

## Model / Tool Availability

No computational tools, custom software, or public data deposits are reported in this paper. The RNA-seq data (n = 3 per group) is referenced with a Supplementary File 1 (full DEG list), but a GEO accession number is not cited in the text as extracted; primary data availability requires checking the Frontiers in Immunology supplementary materials. [UNVERIFIED — GEO accession, if any, not confirmed from full-text XML]

## Follow-up

**Papers already in project or directly related:**

- `paper:Cheong2023` (Cell 2023) — the COVID parallel: IL-6-driven HSPC epigenomic imprinting after severe SARS-CoV-2 with human and mouse (MHV-1) arms, persistent to 12 months, with direct IL-6-necessity demonstration. The comparison between Cheong2023 and Bomans2018 is load-bearing for the cross-trigger generalization claim: both show GMP expansion and trained BM/HSPC output after non-COVID (CLP) and COVID (MHV-1/SARS-CoV-2) infections, but the mechanistic signal (IL-6) is demonstrated only in Cheong2023.
- `paper:Christ2018` (Cell 2018) — Western-diet-driven central myeloid training is NLRP3-dependent; GMP ATAC-seq at Tet2/Tlr4. Comparison: Christ2018 characterizes a sterile, non-infectious training model with epigenomic readout; Bomans2018 is an infectious model without epigenomics. Together they bracket the range of central-training stimuli (lipid DAMPs vs. polymicrobial sepsis) converging on GMP expansion.
- `paper:Saeed2014` (Science 2014) — genome-wide H3K4me3/H3K27ac map of β-glucan training; the epigenomic resource that Bomans2018 explicitly cites as context but does not extend to the CLP-trained monocyte setting.

**Key missing experiments:**
1. ATAC-seq and/or H3K4me3 ChIP-seq on sorted bone marrow monocytes from CLP mice at 3 and 12 months — to establish the epigenomic basis of the trained phenotype and link it to the Cheong2023/Saeed2014 chromatin landscape.
2. A mechanistic intervention: IL-6R blockade (or NLRP3 inhibition, or fungal translocation prevention) during the acute CLP phase, followed by assessment of BM monocyte training at 12 weeks — to identify the training signal.
3. Human post-sepsis cohort profiling: sorted bone marrow or circulating HSPCs from ICU survivors at 3–12 months, with ATAC-seq or H3K4me3 ChIP-seq, alongside PICS symptom burden — to translate the murine finding to human post-sepsis syndrome.
4. Correlation of trained BM monocyte phenotype with secondary infection susceptibility or post-sepsis fatigue/cognitive impairment endpoints in a longitudinal CLP cohort.
