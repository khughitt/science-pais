---
id: paper:Schmitz2026
type: paper
title: "Autonomic dysfunction and vasoregulation in long COVID-19 are linked to anti-GPCR autoantibodies"
status: active
paper_kind: ""
ontology_terms:
- anti-GPCR autoantibody
- long COVID
- post-COVID syndrome
- dysautonomia
- heart rate variability
- vasoregulation
- blood pressure
- CXCR3
- angiotensin II receptor
- beta-adrenergic receptor
- muscarinic acetylcholine receptor
- CellTrend ELISA
- B-cell receptor repertoire
- T-cell receptor repertoire
- post-acute infection syndrome
dataset_usage: []
datasets: []
source_refs:
- cite:Schmitz2026
related:
- question:0009-functional-autoantibodies-drive-dysautonomia
- hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
- proposition:0016-pais-sfn-autoimmune-causation
- proposition:0018-pais-sfn-anti-gpcr-autoantibody-pathogenicity
- topic:post-infectious-dysautonomia-and-autoimmunity
created: "2026-06-24"
updated: "2026-06-24"
---
# Autonomic dysfunction and vasoregulation in long COVID-19 are linked to anti-GPCR autoantibodies

- **Authors:** Boris Schmitz, René Garbsch, Hendrik Schäfer, Christian Bär, Shambhabi Chatterjee, Gabriela Riemekasten, Kai Schulze-Forster, Harald Heidecke, Christoph Schultheiß, Mascha Binder, Frank C. Mooren
- **Year:** 2026 (published online November 20, 2025)
- **Journal:** Journal of Allergy and Clinical Immunology
- **Volume/Pages:** 157(3):722–738.e7
- **DOI:** 10.1016/j.jaci.2025.10.034
- **PMID:** 41274384
- **BibTeX key:** Schmitz2026
- **Source:** PubMed/NCBI abstract metadata for PMID 41274384, supplemented by Crossref metadata. Assay platform is inferred from Schulze-Forster/Heidecke affiliation and conflict-of-interest statement (CellTrend GmbH, Luckenwalde) — the CellTrend binding ELISA has been the platform in this paper family. Full-text methods extraction is still required to confirm assay details, cohort n, case definition, and exact per-receptor statistics.

## Key Contribution

This study is the **primary long-COVID-specific evidence anchor** for the project's anti-GPCR autoantibody / dysautonomia thread (`question:0009`). It characterizes IgG autoantibodies against multiple GPCRs — angiotensin II receptors (AT1R, AT2R), beta-adrenergic receptors (β1-AR, β2-AR), muscarinic acetylcholine receptors (M1, M3), and CXCR3 — in post-COVID syndrome (PCS) patients with documented heart rate variability (HRV) alterations, and correlates these autoantibodies with blood pressure dysregulation on 24-hour ambulatory monitoring and exercise stress testing. A novel addition beyond prior work is (1) inclusion of CXCR3 as a target, (2) direct in vitro testing of whether patient-derived autoantibodies affect cardiomyocyte electromechanics, and (3) profiling of B-cell and T-cell receptor repertoires to look for immunogenetic imprints of autoimmunity. The in vitro test was negative (no cardiomyocyte beat-frequency or amplitude effect), and the BCR/TCR metrics were indistinguishable from healthy controls — qualifying and contextualizing the autoantibody–autonomic correlations.

## Methods

### Cohort and Case Definition

- **Long-COVID cohort (PCS):** Patients with post-COVID-19 syndrome and documented alterations in autonomic nervous system function assessed by heart rate variability. Exact n is not reported in the PubMed abstract; full text is required.
- **Controls:** (a) Patients with COVID-19 after recovery from severe or moderate acute disease; (b) prepandemic healthy individuals. Exact n per control group is not reported in the PubMed abstract.
- **PCS case definition:** Not specified in the PubMed abstract. WHO 2021 or a different center-specific threshold cannot be adjudicated from abstract-level extraction.
- **Time since infection:** Not specified in the PubMed abstract.
- **Recruitment site and period:** Inferred from affiliations — University of Witten/Herdecke and DRV Clinic Königsfeld (Schmitz/Mooren group), Hannover Medical School / Fraunhofer (Bär/Chatterjee), UKSH Lübeck (Riemekasten), CellTrend GmbH (Schulze-Forster/Heidecke), University Hospital Basel (Schultheiß/Binder). Multi-site German consortium with CellTrend as the autoantibody assay provider.

### Assay — Binding ELISA (CellTrend Platform)

**BINDING ELISA, not a functional/receptor-activation bioassay.** The involvement of Kai Schulze-Forster and Harald Heidecke (both affiliated with CellTrend GmbH, Luckenwalde, Germany, and disclosed as CellTrend cofounders) strongly indicates that the CellTrend binding platform was used — the same assay family used by Loebel2016 and Stein2025. Full-text methods extraction is still required to confirm the exact assay version. This platform detects IgG binding to recombinant GPCR antigens on an ELISA-based cell surface assay. It does NOT measure receptor activation, G-protein coupling, or downstream cAMP/IP3 signaling. Whether the detected autoantibodies are agonist, antagonist, or functionally neutral is not resolved by this assay type — this is the central assay limitation for the `question:0009` causal claim.

### GPCRs Screened

The abstract explicitly names four autoantibody classes associated with HRV alterations:

| Receptor | Abbreviation used |
|---|---|
| Angiotensin II receptor type 1 | AT1R |
| Angiotensin II receptor type 2 | AT2R |
| β1-adrenergic receptor | β1-AR |
| β2-adrenergic receptor | β2-AR |
| Muscarinic acetylcholine receptor M1 | M1-AChR |
| Muscarinic acetylcholine receptor M3 | M3-AChR |
| C-X-C motif chemokine receptor 3 | CXCR3 |

Note: CXCR3 is **not a canonical autonomic GPCR** — it is a chemokine receptor expressed on T cells and endothelium. Its inclusion as a target linked to vascular dysregulation is a novel finding of this study beyond the classical adrenergic/muscarinic panel.

### Autonomic and Cardiovascular Measures

- **Primary autonomic measure:** Heart rate variability (HRV) — mode of analysis (time domain, frequency domain, or non-linear; standardized vs. resting recording duration) is not specified in the PubMed abstract.
- **Blood pressure:** 24-hour ambulatory blood pressure monitoring (24h ABPM) yielding 24-hour mean arterial pressure (MAP) and exercise stress test blood pressure (exercise BP response).
- No tilt-table testing or formal POTS diagnosis criteria are mentioned in the PubMed abstract.
- No microvascular or retinal vasoregulation readout is mentioned in the PubMed abstract; the abstracted vasoregulation measures are 24-hour MAP and exercise stress-test blood pressure.

### Adaptive Immune Repertoire

Adaptive immune receptor repertoire sequencing (AIRR-seq) of peripheral B-cell receptors (BCR) and T-cell receptors (TCR) — looking for clonality, diversity, and somatic hypermutation (SHM) metrics as proxies for antigen-driven germinal center reactions. TCR-β variable gene (TRBV) usage also analyzed.

### In Vitro Functional Test

Human-induced pluripotent stem cell-derived cardiomyocytes (hiPSC-CMs) exposed to patient-derived autoantibodies — measuring beat frequency and contraction amplitude. This tests direct electromechanical coupling effects of the autoantibodies on cardiomyocytes.

## Key Findings

### Anti-GPCR Autoantibodies and HRV

Autoantibodies against AT1R, AT2R, β1-AR, β2-AR, M1-AChR, and M3-AChR, and CXCR3 (CXCR3ab) were **associated with HRV alterations** in PCS patients. Exact per-receptor seropositivity rates, effect sizes (OR, Spearman rho, or regression coefficients), and p-values are not reported in the PubMed abstract; full-text extraction is required.

### CXCR3ab and 24-hour Mean Arterial Pressure

- **Elevated CXCR3ab levels were linked to higher 24-hour mean arterial pressure** — i.e. a titer ↔ vasoregulation correlation for a chemokine receptor. Quantitative effect size and significance are not reported in the PubMed abstract.
- This is the most novel vascular finding: a chemokine receptor autoantibody correlated with ambulatory BP load, suggesting CXCR3 on vascular endothelium or smooth muscle could be an additional autoantibody target in long-COVID vasoregulation beyond the classical adrenergic/RAS axis.

### M1-AChR and CXCR3ab — Stress-Test Blood Pressure

- Patients with **elevated M1-AChR antibodies and elevated CXCR3ab** showed **higher blood pressure during exercise stress tests**, suggesting an exaggerated sympathetic/vascular response linked to the combined autoantibody profile. This is an additive or interaction effect of two different receptor antibodies on sympathetically-driven BP; effect size and p-value are not reported in the PubMed abstract.

### BCR/TCR Repertoire — No Autoimmune Imprint

- **Clonality and diversity** of peripheral BCR were **similar to healthy controls** — no oligoclonal expansion typical of antigen-driven plasmablast responses.
- **Somatic hypermutation (SHM) level** — the proxy for antigen experience and germinal center activity — was **equal to healthy controls**. This is a negative finding: the autoantibodies are not associated with the canonical germinal-center-driven somatically hypermutated class-switched IgG seen in classic autoimmune disease.
- **TRBV gene usage** showed **no correlation** with AAB levels.

This BCR/TCR result argues that the GPCR-binding autoantibodies in PCS are **not** the product of a conventional germinal-center-driven autoimmune cascade and do not carry an antigen-experience signature. They may instead be (a) natural/innate IgG antibodies with pre-existing reactivity upregulated during inflammation, (b) extrafollicular B-cell products (which bypass somatic hypermutation), or (c) cross-reactive antibodies elicited by SARS-CoV-2 antigen with molecular mimicry but without classical SHM accumulation.

### In Vitro — No Direct Cardiomyocyte Effect

Patient-derived AABs showed **no effect on beat frequency and amplitude** of hiPSC-CM contraction. This means the detected autoantibodies, at the concentrations tested, do not directly dysregulate cardiomyocyte electromechanics in vitro. This result does not rule out in vivo autonomic or vascular effects mediated via nerve terminals, adrenal signaling, or endothelial GPCR — but it closes the simplest direct cardiomyocyte-binding mechanism.

### Summary of Key Findings Table

| Finding | Direction | Quantified? | Notes |
|---|---|---|---|
| AT1/AT2, β1/β2-AR, M1/M3-AChR, CXCR3ab correlate with HRV alterations | Positive association | Effect sizes not in abstract | Primary HRV result |
| CXCR3ab ↔ 24h MAP | Positive (higher MAP) | Magnitude not in abstract | Novel chemokine-receptor vascular link |
| M1-AChR + CXCR3ab ↔ stress-test BP | Positive (higher BP) | Magnitude not in abstract | Additive/interaction effect |
| BCR clonality / diversity vs healthy controls | No difference | Reported as equal | Negative; no germinal center imprint |
| SHM level vs healthy controls | No difference | Reported as equal | Negative; no antigen-experience signature |
| TRBV gene usage vs AAB levels | No correlation | Reported as absent | Negative |
| hiPSC-CM beat frequency/amplitude with patient AABs | No effect | Reported as null | Direct cardiomyocyte target excluded |

## Relevance

This paper is the **central long-COVID evidence anchor** for `question:0009-functional-autoantibodies-drive-dysautonomia`. It advances the GPCR autoantibody field in three ways beyond the ME/CFS-focused `Loebel2016`:

1. **Long-COVID specificity:** Directly tests the anti-GPCR autoantibody hypothesis in a PCS cohort with objective autonomic (HRV) and vascular (ambulatory BP, stress-test BP) endpoints — providing the long-COVID arm that `question:0009` explicitly asks about.

2. **Extended receptor panel:** Adds CXCR3 as a new vascular-linked target beyond the classical adrenergic/muscarinic/RAS panel. CXCR3 on endothelium is biologically plausible as a vasotonus modulator; this opens a new mechanistic thread.

3. **BCR/TCR negative result:** The absence of a germinal-center imprint constrains the mechanistic model: if these autoantibodies are real and functional, their generation bypasses classical affinity maturation. This is an important constraint for any autoimmunity hypothesis requiring antigen-driven, class-switched, somatically hypermutated autoantibodies as the effector.

**Relevance to `proposition:0018-pais-sfn-anti-gpcr-autoantibody-pathogenicity`:** This paper provides new associational evidence (titer ↔ HRV, titer ↔ BP) — the cross-sectional correlation arm. It does **not** provide passive-transfer, skin-biopsy, or fiber-damage evidence. The fundamental gap between "autoantibodies correlate with autonomic function" and "autoantibodies cause the small-fiber structural lesion" remains completely open.

**Relevance to `hypothesis:0007`:** Strengthens the autoantibody ↔ autonomic-function link (the functional arm), but adds nothing to the structural/SFN lesion arm (P1/P2 in hypothesis:0007). The paper asks whether anti-GPCR AABs modulate cardiac rhythm and vascular tone — which they do associationally — not whether they damage small fibers or cause IENFD reduction.

## Project Framework Mapping

| Paper Concept | Project Entity | Notes |
|---|---|---|
| Post-COVID syndrome (PCS) with HRV alteration as inclusion criterion | `question:0009-functional-autoantibodies-drive-dysautonomia` | Long-COVID arm of the autoantibody-dysautonomia question |
| AT1/AT2, β1/β2, M1/M3, CXCR3 binding IgG | `proposition:0018-pais-sfn-anti-gpcr-autoantibody-pathogenicity` | Cross-sectional associational evidence (binding ELISA, not functional) |
| HRV alteration correlated with anti-GPCR AABs | `proposition:0018` | The load-bearing titer↔autonomic link; binding assay limits causal inference |
| CXCR3ab ↔ 24h MAP | `topic:post-infectious-dysautonomia-and-autoimmunity` | Novel vascular target; extends the project's GPCR panel beyond adrenergic/muscarinic |
| BCR no germinal-center imprint | `hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate` (constraining) | If autoantibodies are real effectors, they bypass classical SHM maturation — consistent with extrafollicular B-cell or natural-antibody models |
| hiPSC-CM null result | Cardiomyocyte-direct mechanism excluded | The autonomic effect is via nerve/vessel GPCR, not direct cardiomyocyte binding |
| BCR/TCR repertoire metrics (AIRR-seq) | `proposition:0016-pais-sfn-autoimmune-causation` (negative indirect) | No canonical autoimmune B-cell expansion detected — weakens classical autoimmune framing but does not exclude all immune-mediated routes |
| CellTrend ELISA (inferred binding assay) | Assay limitation for `question:0009` | Binding ≠ functional; the assay gap is shared across the entire GPCR autoantibody thread from Loebel2016 onward |

### Gap: Anti-GPCR Antibodies vs. Small-Fiber Structural Lesion

This paper does **not** connect anti-GPCR antibodies to the small-fiber structural lesion (`proposition:0014`, `proposition:0015`). There is no skin-biopsy IENFD data, no QSART, no autonomic reflex screen, and no SFN diagnosis. The paper addresses the autonomic-function arm (HRV, BP) only. This preserves — and explicitly exemplifies — the gap that `proposition:0018`'s "Caveats" section describes: the leap from "autoantibodies modulate autonomic function" to "autoantibodies damage or ablate small fibers" is entirely unsupported by this study and by the current corpus.

## Limitations

1. **Binding ELISA, not a functional assay.** The CellTrend-linked assay detects receptor-binding IgG but does not measure agonism, antagonism, or downstream signaling. Whether the detected autoantibodies are functionally active (agonist/antagonist at the receptor) remains unresolved. This is the principal limitation for the `question:0009` causal claim — correlations between a binding titer and an autonomic measure do not demonstrate that the antibody is driving the autonomic phenotype.

2. **Cross-sectional design; no causal test.** No passive transfer, no antibody depletion/immunoadsorption, no before/after intervention data. The titer ↔ HRV / BP correlations are associational only. Reverse causation (autonomic dysregulation → immune activation → autoantibody production) cannot be excluded.

3. **Cohort n and composition are UNVERIFIED.** The abstract does not report exact group sizes, sex distribution, age, time since infection, or severity of acute illness. These covariates are all known to confound anti-GPCR autoantibody seroprevalence and HRV measures.

4. **PCS case definition unspecified in abstract.** Whether WHO 2021 or a more restrictive definition was applied (e.g. requiring POTS or objective HRV alteration above a threshold) is not extractable from the PubMed abstract. The HRV-alteration inclusion criterion self-selects a dysautonomia-enriched cohort, which inflates the apparent autoantibody-autonomic correlation compared to unselected PCS cohorts.

5. **Seropositivity rates unspecified in abstract.** Per-receptor seropositive fractions in the PCS group vs. each control group are not reportable from the abstract. Whether the "association with HRV" means a seropositive vs. seronegative split, a continuous titer correlation, or a regression-adjusted model requires full-text extraction.

6. **No small-fiber neuropathy or skin-biopsy data.** The paper does not test whether anti-GPCR autoantibody positivity correlates with IENFD reduction, QSART abnormality, or any structural peripheral nerve measure. The gap between "autoantibodies modulate autonomic function" and "autoantibodies damage small fibers" (`proposition:0018` central weakness) is not addressed.

7. **No POTS diagnosis by formal criteria in abstract.** Tilt-table testing and head-up tilt (HUT)-confirmed POTS are not mentioned in the abstract. HRV and stress-test BP are used, but formal orthostatic intolerance measurement requires full-text extraction.

8. **BCR/TCR SHM null finding — alternative interpretations.** The absence of elevated SHM might mean the autoantibodies are not antigen-selected — but could also reflect insufficient power to detect modest germinal center involvement, or measurement of peripheral blood BCR that may not reflect relevant tissue compartments (lymph nodes, bone marrow). The null result constrains but does not definitively exclude antigen-driven autoimmunity.

9. **Conflict of interest note.** Harald Heidecke and Kai Schulze-Forster are affiliated with CellTrend GmbH, which produces the anti-GPCR autoantibody ELISA platform. This is a structural conflict of interest that should be weighed when interpreting titer-based findings from this platform.

10. **CXCR3 is not a canonical autonomic GPCR.** The inclusion of CXCR3 in a panel of "autonomic GPCR autoantibodies" is conceptually non-standard. CXCR3 mediates T-cell trafficking and has endothelial expression; whether CXCR3 autoantibodies drive vasoregulation via direct receptor binding on endothelium or via indirect immune effects is not established. This finding requires independent replication.

## Model / Tool Availability

No model, tool, or computational artifact is released in the PubMed abstract. The anti-GPCR autoantibody assay is CellTrend-linked from author affiliations and the conflict-of-interest statement, but exact assay version/catalog requires full-text methods extraction. AIRR-seq data and bioinformatic analysis pipeline availability are not mentioned in the abstract; supplementary data deposit status remains unextracted.

## Follow-up

- **CRITICAL: Obtain full text** to extract: (a) cohort n per group; (b) PCS case definition; (c) time since infection; (d) sex distribution; (e) per-receptor seropositivity rates and HRV correlation statistics with effect sizes and p-values; (f) whether the "vasoregulation" in the title refers to retinal microvascular or capillaroscopy data not mentioned in abstract; (g) exact assay method (confirm CellTrend binding ELISA vs. functional cell-based assay).

- **`question:0009` gap:** This paper advances the long-COVID arm of the autoantibody–dysautonomia correlation but does not close the causal gap. The decisive next steps remain: (1) functional receptor-activation assay on the same samples; (2) passive-transfer or antibody-depletion design with autonomic endpoints.

- **CXCR3ab thread:** The CXCR3 ↔ MAP finding is novel and unexplored in PAIS. Track whether CXCR3 autoantibodies appear in ME/CFS or PTLDS cohorts. Consider whether CXCR3 endothelial expression explains the vascular component of long-COVID independently of the adrenergic/RAS axis — connects to `topic:thromboinflammation-and-endothelial-dysfunction`.

- **BCR/TCR null result implications:** The absence of germinal center imprint challenges the "classical autoimmunity" model but is consistent with extrafollicular B-cell activation (seen in acute COVID-19 and other viral diseases). Consider how this constrains `proposition:0016-pais-sfn-autoimmune-causation` mechanistically — immune-mediation of the lesion could occur through T-cell-dependent or innate-like routes that do not require high-SHM autoantibodies.

- **Contrast with Stein2025:** `paper:Stein2025` used β2-AR autoantibody-positive selection as enrollment criterion for immunoadsorption — a quasi-interventional approach. Schmitz2026 is broader (cross-sectional, multi-receptor, adds CXCR3, adds BCR/TCR profiling) but lacks the interventional arm. These two papers together constitute the strongest current evidence for `proposition:0018` and are the immediate context for `task:t006`.

- **Cross-reference to `paper:Loebel2016`:** Loebel2016 established the β2-AR/M3/M4 seroprevalence in ME/CFS with the same CellTrend ELISA platform. Schmitz2026 extends the panel to long COVID, adds AT1/AT2, M1, and CXCR3, and adds BCR/TCR profiling. The two papers together span ME/CFS (Loebel) and long COVID (Schmitz) arms — the cross-trigger comparison that `question:0009` requires is becoming possible but has not been formally conducted with a head-to-head design.
