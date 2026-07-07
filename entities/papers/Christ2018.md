---
id: paper:Christ2018
kind: paper
title: Western Diet Triggers NLRP3-Dependent Innate Immune Reprogramming
status: active
paper_kind: ""
ontology_terms:
- trained immunity
- innate immune memory
- myeloid reprogramming
- granulocyte-monocyte progenitors
- NLRP3 inflammasome
- chromatin accessibility
- ATAC-seq
- epigenetic reprogramming
- hematopoiesis
- atherosclerosis
- western diet
- sterile inflammation
dataset_usage: []
source_refs:
- cite:Christ2018
related:
- topic:innate-immune-memory-trained-immunity-in-pais
- question:0024-nlrp3-inflammasome-and-gasdermin-d-pyroptosis-as-a-self-amplifying-il-1
- hypothesis:0003-immune-exhaustion-feedback
- hypothesis:0004-acute-severity-threshold
created: '2026-07-07'
updated: '2026-07-07'
---
# Western Diet Triggers NLRP3-Dependent Innate Immune Reprogramming

- **Authors:** Anette Christ, Patrick Günther, Mario A.R. Lauterbach, Peter Duewell, Debjani Biswas, Karin Pelka, Claus J. Scholz, Marije Oosting, Kristian Haendler, Kevin Baßler, Kathrin Klee, Jonas Schulte-Schrepping, Thomas Ulas, Simone J.C.F.M. Moorlag, Vinod Kumar, Min Hi Park, Leo A.B. Joosten, Laszlo A. Groh, Niels P. Riksen, Terje Espevik, Andreas Schlitzer, Yang Li, Michael L. Fitzgerald, Mihai G. Netea, Joachim L. Schultze, Eicke Latz
- **Year:** 2018
- **Journal:** Cell, vol. 172, no. 1–2, pp. 162–175.e14
- **DOI:** 10.1016/j.cell.2017.12.013
- **PMID:** 29328911
- **PMCID:** PMC6324559
- **BibTeX key:** Christ2018
- **Source:** Europe PMC full text (via NCBI PMC efetch)

## Key Contribution

This paper established that a Western diet (WD) — independent of infection — drives durable, progenitor-level myeloid reprogramming that persists after the dietary stimulus is removed, constituting a **"maladaptive trained immunity"** paradigm. The key mechanistic claim is that this central (granulocyte-monocyte progenitor / GMP-level) epigenomic and transcriptomic reprogramming is **functionally and genetically NLRP3-dependent**: Nlrp3-/- Ldlr-/- double-knockout mice are protected against WD-induced GMP expansion, GMP transcriptional reprogramming, systemic monocytosis, and atherosclerotic plaque formation. The paper thereby demonstrates that NLRP3 acts **upstream** of the reprogramming event — it is required for induction of central trained immunity, not merely a downstream inflammatory effector of trained cells. It does not demonstrate open-chromatin marks at the NLRP3 gene locus itself; the highlighted ATAC-seq differentials in GMPs are at **Tet2 and Tlr4 enhancers**, not at NLRP3 or Il1b.

## Methods

**Animal model.** Ldlr-/- mice (LDL-receptor knockout; standard hyperlipidemia/atherosclerosis background), female, 8 weeks old. Key comparison genotype: Nlrp3-/- Ldlr-/- double-knockouts. Separate analysis of Nlrp3-/- mice (on non-Ldlr-/- background) confirmed NLRP3-specific effects on trained-immunity endpoints independent of cholesterol loading.

**Diet protocol.** 4 weeks Western diet (WD: 17.3% protein, 21.2% fat, high cholesterol) → 4 weeks return to standard chow diet (CD). The "WD → CD" design probes whether reprogramming persists after the dietary stimulus is withdrawn — the operationalization of "central training" vs transient peripheral priming. Controls: mice maintained on CD throughout.

**Cellular readouts.**
- Peripheral blood monocyte counts, Ly6C-hi vs Ly6C-lo monocyte subsets (monocytosis as a readout of myelopoiesis skewing).
- GMP (Lin-Sca1-cKit+CD16/32+CD34+) isolation from bone marrow; proliferation (BrdU incorporation, Ki67), activation (CD86), and transcriptomics.
- Peritoneal macrophage and bone-marrow-derived macrophage (BMDM) restimulation with LPS, Pam3CSK4, and other TLR ligands to measure trained-immunity functional output (cytokine production: TNF, IL-6, IL-1β).

**Transcriptomics.** RNA-seq on GMPs from WD, WD→CD, and CD mice (with and without Nlrp3 knockout). Comparison of WD vs WD→CD gene expression profiles to identify persistently dysregulated programs after diet reversal.

**Chromatin accessibility (ATAC-seq).** ATAC-seq on sorted GMPs from WD, WD→CD, and CD mice. Differentially accessible regions (DARs) compared between conditions. Key reported differentially open loci in WD-trained and WD→CD-rested GMPs: **Tet2 and Tlr4 enhancers** (more open). Loci showing transient closure during WD but reopening upon dietary reversal included Osbpl3 and Abca1. The ATAC analysis was performed on GMPs, not on circulating monocytes, establishing that the chromatin changes are at the progenitor level. Whether the NLRP3 or Il1b loci themselves show differential ATAC accessibility in GMPs is **not the reported highlight of the ATAC analysis** — the featured open-chromatin changes are at Tet2 and Tlr4.

**Human validation / QTL.** Genome-wide association data was used to identify human cis-eQTLs and expression-QTLs linked to WD-relevant trained immunity in circulating monocytes. Genetic variants in *PYCARD* (ASC, the NLRP3 inflammasome adaptor) and *IL1RAP* (IL-1 receptor accessory protein) were associated with oxLDL-induced trained immunity responses in human monocytes, providing translational support for the inflammasome pathway.

## Key Findings

### 1. WD induces systemic inflammation and GMP expansion that partially outlasts the diet

WD feeding of Ldlr-/- mice produced systemic elevation of inflammatory cytokines (IL-1β, IL-6, TNF) and peripheral monocytosis. Critically, when WD-fed mice were returned to chow for 4 weeks, systemic circulating cytokines normalized, but TLR-restimulation responses of isolated bone-marrow-derived and peritoneal cells remained significantly augmented — the canonical trained-immunity persistence signature. GMP numbers and proliferative activity (BrdU+, Ki67+) were elevated during WD and remained partially elevated in WD→CD mice relative to CD-only controls.

### 2. Progenitor-level transcriptomic reprogramming persists after diet reversal

RNA-seq of GMPs from WD→CD mice showed that LPS-induced gene expression in GMPs remained altered and largely similar to the WD-only condition, not returning to the CD baseline. This documents that the reprogramming is inscribed at the progenitor level before cells differentiate into circulating monocytes — the defining criterion of **central** (HSPC-level) trained immunity. Upregulated gene sets in WD GMPs were enriched for hematopoiesis and cell-proliferation regulatory programs.

### 3. ATAC-seq on GMPs: Tet2 and Tlr4 enhancers are differentially open; NLRP3 locus is not the reported highlight

ATAC-seq on sorted GMPs identified DARs distinguishing WD, WD→CD, and CD conditions. The highlighted persistently more-open chromatin regions in WD-trained and WD→CD-rested GMPs are at enhancers of **Tet2** (a TET methylcytosine dioxygenase involved in DNA demethylation and epigenetic programming) and **Tlr4** (Toll-like receptor 4, a pattern-recognition receptor for LPS and fatty acids), consistent with a primed innate-sensing phenotype. Some loci (Osbpl3, Abca1 — lipid-sensing genes) showed transient chromatin closure during WD that reopened on chow reversal, distinguishing diet-dependent from diet-independent epigenomic changes. **The ATAC-seq readout does not highlight NLRP3 or IL-1β (Il1b) loci as primary differentially accessible regions in GMPs.** The NLRP3 dependence is established by genetic means (knockout), not by NLRP3-locus chromatin accessibility in GMPs.

### 4. NLRP3 dependence is functional and genetic — not locus-level chromatin

Nlrp3-/- Ldlr-/- mice were protected across multiple readouts:
- No peripheral monocytosis upon WD feeding.
- Blunted GMP activation (CD86 surface expression was not induced).
- Absent or strongly reduced GMP proliferation (BrdU/Ki67).
- WD-induced transcriptional reprogramming of GMPs was "mostly dependent on NLRP3" — a direct comparison of WD vs WD in Nlrp3-/- Ldlr-/- mice showed the gene-expression changes were substantially abrogated.
- Markedly reduced atherosclerotic plaque area after 8 weeks WD.

These data place NLRP3 as a **required upstream signal** for the diet → progenitor reprogramming cascade, not merely as a gene that is epigenetically primed in trained cells. The mechanistic interpretation is that WD-derived signals (cholesterol crystals, saturated fatty acids, oxLDL) activate NLRP3 in myeloid cells or their progenitor microenvironment, and this NLRP3 signaling (via caspase-1 → IL-1β/IL-18 → downstream pathways) is required to initiate the epigenomic changes in GMPs.

### 5. Human genetic support: PYCARD and IL1RAP variants modulate trained immunity

Genetic analysis in the LifeLines cohort identified human QTL variants near *PYCARD* (the gene encoding ASC, the obligatory NLRP3 inflammasome adaptor) and *IL1RAP* that predict the magnitude of oxLDL-induced trained immunity (cytokine production) in human peripheral blood monocytes. This provides translational support for the NLRP3 → IL-1 signaling axis in human trained immunity, consistent with the murine genetic findings.

## Relevance

This paper is a mechanistic anchor for the claim that **central myeloid reprogramming (progenitor-level trained immunity) is NLRP3-dependent**, in a sterile-inflammation context. Its relevance to PAIS is by **mechanistic analogy**, not direct evidence — the study is a murine Western diet/atherosclerosis model and does not involve infection, post-infectious recovery, or PAIS phenotypes.

**What the paper contributes to the project frame:**

1. **Grounds NLRP3 as an upstream inducer of central trained immunity** (`question:0024`). The Nlrp3-/- Ldlr-/- knockout data establish that NLRP3 activity is required for progenitor reprogramming, not only for downstream IL-1β output. This is relevant because it raises the possibility that NLRP3 activation during acute infection could set in motion a durable progenitor-level imprint — the same question posed in `question:0024` for PAIS.

2. **Demonstrates the canonical central-training experimental paradigm.** The WD → CD diet-reversal design with GMP ATAC-seq and RNA-seq is the benchmark protocol for demonstrating that progenitor-level chromatin changes persist beyond the initial stimulus. For the project's `topic:innate-immune-memory-trained-immunity-in-pais`, Christ2018 is the reference for NLRP3-dependent central training, complementing Mitroulis2018 (β-glucan-mediated HSPC training) and Cheong2023 (IL-6/COVID-driven HSPC imprinting).

3. **Distinguishes functional/genetic NLRP3 dependence from locus-level chromatin.** The Tet2 and Tlr4 enhancers — not the NLRP3 locus — are the ATAC-seq signal in trained GMPs. This means that NLRP3 acts as an **inducing signal** rather than as a gene that is epigenetically unlocked at the chromatin level during training. The downstream epigenomic changes are at innate-sensing (Tlr4) and epigenetic-regulatory (Tet2) loci.

4. **Provides a prior for `hypothesis:0004` (acute severity threshold).** If NLRP3 activation above a threshold is required to trigger progenitor reprogramming, then acute-illness severity — which governs NLRP3-activating signal magnitude (pyroptotic DAMPs, cholesterol from lysed cells, IL-18 from dying cells) — becomes a gating variable for whether progenitor training is induced at all. This is mechanistically coherent with h0004's claim that a severity threshold separates self-resolving from self-sustaining post-infectious states.

**What this paper is NOT:**
- It does not show open chromatin at the NLRP3 or IL-1β gene loci in trained GMPs.
- It does not study infection, post-infectious recovery, or any PAIS phenotype.
- It does not directly demonstrate that pathogen-derived stimuli (as opposed to dietary/lipid stimuli) engage NLRP3 to train progenitors — that inference requires separate evidence (e.g., Mitroulis2018 for fungal β-glucan; Bomans2018 for post-sepsis).
- It does not test whether trained-immunity reversal (e.g., by NLRP3 inhibition after training is established) rescues the inflammatory phenotype — only knockout prior to WD was tested.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Western diet → NLRP3 → GMP reprogramming | Sterile stimulus → central trained immunity | Analogy model for post-infectious NLRP3 activation |
| Nlrp3-/- Ldlr-/- protection from GMP expansion | NLRP3 as upstream inducer (not just output) of training | Key mechanistic boundary: genetic not chromatin evidence |
| GMP ATAC-seq: Tet2, Tlr4 enhancers open | Progenitor-level chromatin reprogramming | Accessible loci are Tet2/Tlr4; NLRP3/IL1B loci not highlighted |
| Persistence after diet reversal | Antigen-independent maintenance of trained state | Central training paradigm; relevant to post-clearance PAIS persistence |
| PYCARD/IL1RAP human QTLs | NLRP3 → IL-1 axis in human myeloid training | Translational hook; no PAIS cohort studied |
| oxLDL / cholesterol crystals as training stimulus | DAMPs as training stimuli | Sterile; no pathogen-associated patterns — analogy only |

## Limitations

- **Non-infectious sterile model.** Ldlr-/- + WD is a dietary/lipid metabolic model. All mechanistic claims derive from cholesterol-crystal and lipid DAMP-driven NLRP3 activation. Whether acute pathogen-driven NLRP3 activation (viral PAMPs, pyroptotic DAMPs from infected cells) produces the same progenitor reprogramming is inferred, not demonstrated.
- **Preventive knockout, not therapeutic.** Nlrp3 knockout was present from birth. The paper does not test whether NLRP3 inhibition after WD-induced training reverses the trained state — a critical question for therapeutics and for `question:0024`'s pharmacological angle.
- **Single sex (female) and single background (Ldlr-/-).** Findings in female Ldlr-/- may not generalize across sex or to non-lipid-loading backgrounds. Ldlr-/- mice have severely dysregulated lipid metabolism that is not relevant to most PAIS contexts.
- **ATAC-seq highlight is Tet2/Tlr4, not NLRP3/IL1B.** The NLRP3 dependence is established by genetic rescue, not by demonstrating open chromatin at the NLRP3 locus. Any claim that Christ2018 grounds "NLRP3 locus chromatin accessibility in trained progenitors" misreads the paper's ATAC evidence.
- **GMP-level readout, not full HSPC hierarchy.** The study characterizes GMPs specifically, not HSCs or multipotent progenitors. Whether the epigenomic changes are inscribed higher up the hierarchy (as in Mitroulis2018 and Cheong2023) or are GMP-restricted is not tested.
- **Mechanism of NLRP3-to-chromatin link not resolved.** How NLRP3 activity (caspase-1 → IL-1β/IL-18 → ?) transduces to progenitor chromatin changes at Tet2/Tlr4 is not mechanistically delineated.
- **Human data is QTL-level.** The human validation shows genetic associations with monocyte trained-immunity responses but does not demonstrate HSPC-level chromatin changes in humans with high dietary fat/cholesterol.

## Model / Tool Availability

No computational tools or datasets released with the paper. Primary data (GMP RNA-seq, ATAC-seq) available through GEO accession numbers cited in the paper [UNVERIFIED — accession numbers not recorded from text extraction; check GEO/NCBI for GSE series].

## Follow-up

- Compare with Mitroulis2018 (Cell): β-glucan-driven HSPC reprogramming is NLRP3-independent (β-glucan signals via dectin-1/Card9), establishing that central training can occur via NLRP3-dependent (Christ2018: WD/oxLDL) and NLRP3-independent (Mitroulis2018: β-glucan) routes — the inducing signal determines the upstream pathway even if the downstream progenitor chromatin changes share features.
- Compare with Cheong2023 (Cell): severe COVID-19 trains HSPCs via IL-6/STAT3 signaling. Does SARS-CoV-2 also activate NLRP3 in progenitors or their niche? The Cheong2023 imprinting mechanism uses IL-6 as the key signal, not IL-1β/NLRP3 — but both could operate in parallel in severe infection.
- `question:0024`: Does NLRP3-driven central training operate in post-infectious settings? The pharmacological test is NLRP3 inhibitors (MCC950, colchicine) — do they prevent or reverse the progenitor reprogramming when given during or after infection? No published data in infection models yet.
- Investigate whether Tet2 chromatin opening in trained GMPs (the highlighted ATAC locus) has functional consequences — Tet2 loss-of-function in myeloid cells is known to augment IL-6 production (Clonal Hematopoiesis / CHIP context), suggesting that Tet2 transcriptional changes in trained progenitors could feedback-amplify inflammatory output.
