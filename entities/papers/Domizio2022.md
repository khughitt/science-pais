---
id: paper:Domizio2022
kind: paper
title: The cGAS-STING pathway drives type I IFN immunopathology in COVID-19
status: active
paper_kind: ""
ontology_terms:
- cGAS-STING
- type I interferon
- innate immunity
- COVID-19 immunopathology
- endothelial dysfunction
- mitochondrial DNA
- macrophage
- endothelial cell
- lung-on-chip
- STING inhibition
dataset_usage: []
source_refs:
- cite:Domizio2022
related:
- question:0023-cgas-sting-cytosolic-dna-sensing-as-upstream-driver-of-persistent-type-i
- hypothesis:0003-immune-exhaustion-feedback
created: '2026-07-07'
updated: '2026-07-07'
---
# The cGAS-STING pathway drives type I IFN immunopathology in COVID-19

- **Authors:** Jeremy Di Domizio, Muhammet F. Gulen, Fanny Saidoune, Vivek V. Thacker, Ahmad Yatim, Kunal Sharma, Théo Nass, Emmanuella Guenova, Martin Schaller, Curdin Conrad, Christine Goepfert, Laurence de Leval, Christophe von Garnier, Sabina Berezowska, Anaëlle Dubois, Michel Gilliet, Andrea Ablasser
- **Year:** 2022
- **Journal:** Nature, vol. 603, no. 7899, pp. 145–151
- **DOI:** 10.1038/s41586-022-04421-w
- **PMID:** 35045565
- **PMCID:** PMC8891013
- **BibTeX key:** Domizio2022
- **Source:** Europe PMC XML (full text)

## Key Contribution

This paper establishes the cGAS-STING pathway as a critical driver of aberrant type I IFN responses in severe/acute COVID-19. Using human tissue samples (skin and post-mortem lung), a lung-on-chip model, and K18-hACE2 transgenic mice, the study demonstrates that SARS-CoV-2 infection triggers mitochondrial damage in endothelial cells, causing mtDNA release into the cytosol that activates cGAS-STING, while macrophages respond to DNA from engulfed dying endothelial cells via the same pathway. Pharmacological STING inhibition (H-151) reduced lung inflammation and improved survival in mice without affecting viral replication, showing that STING drives immunopathology independently of antiviral clearance.

**Important scope boundary:** this is an acute/severe COVID-19 immunopathology study — all human samples came from hospitalized patients or post-mortem lung, and the mouse model recapitulates fatal severe disease. The paper does not study long COVID or post-acute sequelae. Its relevance to persistent IFN-I in PAIS is inferential: it grounds the mechanism by which SARS-CoV-2 acutely engages the cGAS-STING axis, but does not show this pathway persists after viral clearance or drives PAIS chronicity.

## Methods

**Human tissue.**
- COVID-19 skin biopsies: 10 consecutive patients with moderate-to-severe COVID-19 and associated skin manifestations, hospitalized at CHUV (Lausanne) from March 2020; all PCR+ for SARS-CoV-2. Compared against skin from inflammatory skin disease controls (CLE n=11, psoriasis n=21, atopic dermatitis n=16, lichen planus n=5) and healthy donors (n=4–9 depending on readout).
- Post-mortem lung: 8 patients who died from COVID-19; analysed by DAD stage (early: <10 days from onset; late: >14 days from onset, fibrotic).

**Lung-on-chip (LoC) model.** Three-cell and two-cell component chips mimicking the alveolar-capillary interface: human primary alveolar epithelial cells (apical), human lung microvascular endothelial cells (basolateral), and M-CSF-differentiated primary macrophages. Chips infected with SARS-CoV-2 via the apical channel (400–600 PFU). Treated with STING inhibitor H-151 (1 µM) or VDAC1 oligomerization inhibitor VBIT-4 (1 µM) through the vascular channel. mtDNA depletion: endothelial cells pre-treated with 2′,3′-dideoxycytidine (ddC) to generate ρ⁰ cells. STING and MAVS knockdown via shRNA lentiviral transduction of endothelial and epithelial cells separately.

**Proteomics.** Mass spectrometry of cytosolic fractions of LoC endothelial cells at 3 days post-infection (dpi) and time course; TMT labelling; Proteome Discoverer v2.4. Identified enrichment of mitochondria-associated proteins (GO terms: thermogenesis, oxidative phosphorylation).

**Volumetric electron microscopy.** In-situ ultrastructural imaging of LoC endothelial cell mitochondria; surface-area-to-volume ratio of cristae in uninfected (n=45) vs infected (n=43) mitochondria.

**Mouse model.** Female K18-hACE2 transgenic mice (C57BL/6J background, 12–16 weeks); intranasal SARS-CoV-2 (1×10⁴ PFU). H-151 regimen: (a) prophylactic — daily i.p. 750 nmol H-151 starting 16 h before infection, euthanised at 3 or 6 dpi; (b) therapeutic — H-151 starting at 2 dpi. Outcomes: lung histopathology (% inflamed area), RT-qPCR for IFNβ, ISGs, cytokines, and chemokines; Western blot for p-p65 and p-STAT1; plaque assay for viral replication; body weight; survival (Mantel-Cox analysis; n=15 per arm in survival experiment).

**Key assays in tissue.** Immunofluorescence confocal microscopy (p-STING, CD163, CD31, IFNβ, cleaved caspase-3, cytosolic DNA foci); cGAMP ELISA on skin lysates; RNA-FISH for IFNB1 mRNA; Nanostring nCounter Human Immunology V2 panel (600 targets) on skin biopsies; ex-vivo skin explant culture ± H-151 with Nanostring readout of ISGs (IFI35, IRF7, MX1).

## Key Findings

### 1. Type I IFN signature in COVID-19 skin resembles cutaneous lupus, not other inflammatory skin diseases

Transcriptome profiling of COVID-19 skin lesions (n=10) clustered with CLE samples, distinct from psoriasis, atopic dermatitis, and lichen planus. COVID-19 profiles additionally showed marked upregulation of macrophage genes (CD163, MARCO, CD209, CLEC5A, MRC1, CCL2, CXCL2) and pro-inflammatory cytokines (TNF, IL6, IL1B, IL1A) not seen in CLE — suggesting a macrophage-dominated, IFN-high state with added inflammatory features. IFNβ expression co-localised with CD163+ macrophages surrounding injured vessels (most consistent across all COVID-19 samples), and also with CD31+ endothelial cells (with higher inter-sample variability). Levels of cleaved caspase-3 (endothelial cell death marker) correlated significantly with IFNβ intensity across COVID-19 skin samples.

### 2. cGAS-STING is activated in perivascular macrophages and endothelial cells in COVID-19 tissue

In COVID-19 skin:
- Cytosolic DNA foci accumulated inside IFNβ-producing CD163+ macrophages (not in healthy skin); macrophages also contained engulfed cleaved caspase-3 fragments, consistent with phagocytosis of dying endothelial cells.
- cGAMP levels were elevated in COVID-19 skin lysates vs. healthy skin (ELISA direct measurement of cGAS second messenger).
- Phosphorylated STING (p-STING) was detected in perivascular CD163+ macrophages and in CD31+ endothelial cells in COVID-19 lesions; absent in healthy controls.
- Ex-vivo skin explant culture: H-151 (STING inhibitor) strongly reduced ISG expression (IFI35, IRF7, MX1) in COVID-19 explants but not healthy skin.

In post-mortem COVID-19 lung:
- p-STING was detected in macrophages and endothelial cells in lungs with early DAD (death <10 days from onset, extensive hyaline membrane formation), but NOT in late DAD (death >14 days, fibrotic changes).
- Type I IFN signature (MxA expression) was similarly restricted to early DAD lungs.
- Conclusion: cGAS-STING and IFN-I are active during the acute immunopathological phase of lung injury, not the fibrotic remodelling phase.

### 3. Endothelial STING activation is driven specifically by mitochondrial DNA (mtDNA) release

In the LoC model, SARS-CoV-2 infection of the epithelial layer triggered robust IFNβ production by endothelial cells (not epithelial cells). This response was:
- Completely abolished by H-151 perfused through the vascular channel.
- Unaffected by MAVS knockdown in endothelial cells (ruling out RIG-I-like RNA sensing as the primary driver).
- Dependent on STING in endothelial cells (shRNA knockdown of STING abolished cell death and reduced IFN; STING knockdown in epithelium did not affect endothelial viability).

Mechanistic evidence for mtDNA as the cGAS ligand in endothelial cells:
- Cytosolic proteomics at 3 dpi showed enrichment of mitochondrial proteins (GO: thermogenesis, oxidative phosphorylation) — a molecular signature of mitochondrial stress.
- Volumetric electron microscopy: endothelial cell mitochondria in infected LoCs showed disrupted cristae, swollen appearance, and significantly reduced surface-area-to-volume ratio vs. uninfected controls.
- mtDNA depletion (ρ⁰ cells via ddC treatment) significantly reduced IFNβ production in endothelial cells after SARS-CoV-2 infection.
- VBIT-4 (blocks VDAC1 oligomerization, which is required for mtDNA fragment passage into the cytosol during mitochondrial stress) decreased IFNβ production in infected endothelial cells.

The authors conclude: **SARS-CoV-2 causes mitochondrial dysfunction in endothelial cells → damaged mitochondria release mtDNA into the cytosol via VDAC1 → cytosolic mtDNA activates cGAS → cGAS produces cGAMP → STING activation → IFNβ production and endothelial cell death.** This is a cell-intrinsic mode of cGAS activation in endothelial cells.

For macrophages, the mode is distinct: macrophages phagocytose dying endothelial cells and their cGAS responds to DNA from engulfed cells. The paper documents cytosolic DNA foci in macrophages (confocal imaging) and engulfed cleaved caspase-3 fragments, but does not characterize the DNA type (mtDNA vs. nuclear/genomic) driving macrophage cGAS activation.

### 4. STING drives immunopathology in vivo; STING inhibition is protective

In K18-hACE2 mice:

**Prophylactic H-151 (starting 16 h before infection):**
- At 6 dpi: significantly reduced lung inflammatory infiltration (H&E), reduced TUNEL+ dying cells, reduced mRNA levels of Ifnb1, ISGs (Gbp2, Irf5, Irf8), pro-inflammatory cytokines (Il6, Tnfrsf12a), chemokines (Ccl2, Ccl3, Ccl12, Cxcl9), and lung injury markers (F3, Retnla).
- Reduced NF-κB (p-p65) and type I IFN (p-STAT1) signalling in lung lysates at 6 dpi.
- At 3 dpi: no difference in inflammation between H-151 and vehicle (confirming STING drives the late-phase pathology, not early-phase).
- Attenuated body weight loss vs. vehicle controls.
- Viral replication was not significantly different between H-151 and vehicle at either time point.

**Therapeutic H-151 (starting 2 dpi, when viral loads are maximal):**
- Reduced lung pathology and type I IFN/cytokine levels.
- Protected mice from weight loss.
- Improved survival (Mantel-Cox; n=15/arm): STING inhibition starting during peak viremia still conferred survival benefit.

### 5. Two parallel cell-type-specific modes of cGAS-STING activation

The discussion explicitly frames a two-cell architecture:
- **Endothelial cells:** cell-autonomous cGAS activation by mtDNA released from infected/damaged mitochondria → IFNβ production + endothelial cell death.
- **Macrophages:** cell-extrinsic cGAS activation by DNA from engulfed dying endothelial cells → focused on IFNβ induction.

Both routes converge on STING-dependent type I IFN production and constitute the pathological late-phase response (distinct from the early rapid IFN response triggered by RNA sensing via TLR3/7/RIG-I).

## Relevance

This paper grounds the claim in `question:0023-cgas-sting-cytosolic-dna-sensing-as-upstream-driver-of-persistent-type-i` that SARS-CoV-2 engages the cGAS-STING axis and drives type I IFN through cytosolic DNA sensing. Specifically:

- The mtDNA-release claim in q0023 is **supported and precise for endothelial cells**. The ddC (ρ⁰) depletion and VBIT-4 (VDAC1 inhibition) experiments provide mechanistic proof. The claim should be stated as: SARS-CoV-2 provokes mitochondrial dysfunction in endothelial cells, causing mtDNA to pass into the cytosol via VDAC1 and engage cGAS.
- For macrophages, the cGAS ligand is DNA from engulfed dying (endothelial) cells — the DNA species is not characterized as specifically mtDNA in that context. q0023 should not state mtDNA as the macrophage cGAS ligand; "cell-derived DNA" is more precise there.
- STING inhibition is protective **in acute severe COVID-19 disease**, with no effect on viral replication — validating STING as a pathology driver independent of antiviral function.

**Boundary with PAIS relevance:** This paper studies only acute, severe/fatal COVID-19. The cGAS-STING→IFN-I axis is engaged during active tissue destruction (early DAD phase) and the protective effect of STING inhibition is demonstrated acutely. Whether this pathway remains active post-resolution — sustaining the low-level IFN signature seen in long COVID months after viral clearance — is not addressed here. That extrapolation (q0023's core question) remains an open inferential step. Several indirect lines suggest the pathway could persist (ongoing mtDNA damage, EBV reactivation, viral remnants) but none are established by this study.

Relevant to `hypothesis:0003-immune-exhaustion-feedback` (sterile self-sustaining stimulus branch): this paper provides the molecular basis for how SARS-CoV-2 tissue damage could seed a cycle in which endothelial injury activates innate IFN-I, which further drives inflammation and endothelial damage — a feedforward loop that could in principle be sustained without ongoing viral replication.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| mtDNA release via VDAC1 in endothelial cells | Sterile self-sustaining stimulus (`hypothesis:0003`) | Cell-intrinsic, replication-independent once mitochondria are disrupted |
| Macrophage cGAS activation by engulfed cell DNA | Innate immune activation by dying-cell DAMPs | Extrinsic pathway; DNA type unspecified |
| cGAS-STING → IFN-I late-phase only | Dissociated IFN/inflammatory state in PAIS | Acute: early phase = RNA sensing; late phase = DNA/STING. Parallel to PAIS where elevated IFN-I is not tied to active replication |
| H-151 STING inhibitor protective in mice | Potential PAIS therapeutic target (q0023) | Proof-of-concept in acute model; PAIS-specific trials do not yet exist |
| Two-cell (endothelial + macrophage) cGAS architecture | Endothelial dysfunction + innate activation convergence | Supports multi-cell-type substrate for chronic IFN-I signal |
| STING active only in early DAD, not fibrotic late DAD | Stage-specific immunopathology | Pathway may be self-limiting in resolution; persistence in PAIS is an open question |

## Limitations

- **Scope is acute severe/fatal COVID-19 only.** All human data come from hospitalized patients (skin) or post-mortem lungs (early DAD). There are no long COVID follow-up outcomes, no subacute or convalescent samples, and no PAIS cohort. The extrapolation that cGAS-STING drives persistent IFN-I in long COVID is the researchers' implication, not a finding in this paper.
- **Mouse model is a highly artificial severe disease.** K18-hACE2 mice with 10⁴ PFU intranasal inoculation are a model of severe/fatal disease, not the mild-to-moderate illness that typically precedes long COVID. H-151 dose and route (daily i.p.) may not translate directly to human therapeutic regimens.
- **Human sample sizes are small.** Skin: n=10 COVID-19 patients; lung: n=4 per DAD group. The lung p-STING finding is based on only four early-DAD samples; replication in larger cohorts has not been shown.
- **LoC model limitations.** The lung-on-chip system enables mechanistic dissection not possible in primary human tissue, but it uses commercially sourced cell lines and does not replicate the full in-vivo inflammatory milieu (no circulating immune cells, no lymphocyte compartment, no systemic signals).
- **DNA type in macrophages not characterized.** The paper demonstrates cytosolic DNA foci in macrophages but does not use mtDNA-specific probes, ρ⁰ macrophages, or VBIT-4 experiments in macrophages. Whether macrophage cGAS is stimulated by mtDNA or nuclear/genomic DNA from engulfed dying cells is unresolved.
- **VBIT-4 and ddC are not specific STING/cGAS inhibitors.** ddC depletes mtDNA and has broader metabolic effects; VBIT-4 blocks VDAC1 oligomerization which affects multiple mitochondrial processes beyond mtDNA release. The specificity of these results for the mtDNA→cGAS route is supported but indirect.
- **No direct measurement of cGAS-STING in macrophages separately from endothelial cells in vivo.** The p-STING staining is done on tissue sections and attributes signal to cell types by co-staining markers (CD163, CD31); cross-contamination between cell types in dense tissue sections cannot be fully excluded.
- **Pre-Omicron, early-pandemic isolate.** The SARS-CoV-2 strain used (SARS-CoV2/Switzerland/GE9586/2020) is an ancestral isolate. Immune evasion strategies of later variants may differ.
- **No test in non-COVID-19 PAIS.** The paper is entirely COVID-19-focused. Whether mtDNA-driven cGAS-STING activation occurs in ME/CFS, PTLDS, or other PAIS after different infectious triggers is unstudied.

## Model / Tool Availability

No model, software, or dataset released for community reuse. H-151 is a commercially available small-molecule STING inhibitor (used at 1 µM in LoC assays, 750 nmol i.p. daily in mice). VBIT-4 is a commercially available VDAC1 oligomerization inhibitor (1 µM in LoC).

## Follow-up

- Seed q0023 with this as the primary reference grounding acute cGAS-STING engagement. The `[MISSING_CITATION]` tags in q0023 for "SARS-CoV-2 releases mtDNA that engages this axis" are now resolved by `cite:Domizio2022`.
- The question of whether macrophage cGAS is activated by mtDNA specifically (vs. nuclear/genomic DNA from dying cells) warrants a targeted search — this paper does not settle it; cell-free DNA fractionation studies may.
- Seek studies of cGAS-STING in long COVID samples (peripheral blood mononuclear cells, circulating pDCs, endothelial biopsies) to test whether STING remains activated post-viral clearance — the PAIS-relevance gap not addressed here.
- STING inhibitors (H-151, diABZI antagonists) and cGAS inhibitors (RU.521, G140) are entering early clinical development for systemic autoinflammatory disease; monitor for any PAIS or long COVID trials.
- Compare findings to other viral triggers of mtDNA-driven cGAS-STING (EBV, dengue) to assess whether the mechanism generalises across PAIS triggers — relevant to the cross-trigger hypothesis in `hypothesis:0003`.
