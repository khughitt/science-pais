---
id: topic:innate-immune-memory-trained-immunity-in-pais
kind: topic
title: Innate Immune Memory and Trained Immunity as an Antigen-Independent Persistence Mechanism in PAIS
status: active
ontology_terms:
- trained immunity
- innate immune memory
- epigenetic reprogramming
- hematopoietic stem and progenitor cells
- monocyte hyperreactivity
- H3K4me3
- chromatin accessibility
- immunometabolism
- antigen-independent inflammation
- post-acute infection syndrome
datasets: []
source_refs:
- cite:Tsergas2025
- cite:Crotty2026
- cite:Vacharathit2025
- cite:Munro2025
- cite:Netea2016
- cite:Cheng2014
- cite:Arts2016
- cite:Mitroulis2018
- cite:Cheong2023
- cite:Gu2023
- cite:Bomans2018
- cite:Humer2025
- cite:Aid2025
- cite:Klein2023
origins:
- type: user
related:
- paper:Gu2023
- topic:long-covid-immune-dysregulation
- topic:shared-failure-mode-across-pais
- topic:antigen-pathogen-persistence
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0003-immune-exhaustion-feedback
- hypothesis:0014-nk-failure-clear-senescent-endothelium-sasp-propagation
- question:0023-cgas-sting-cytosolic-dna-sensing-as-upstream-driver-of-persistent-type-i
- question:0024-nlrp3-inflammasome-and-gasdermin-d-pyroptosis-as-a-self-amplifying-il-1
- question:0026-acute-infection-il-6-stat3-imprinting-of-hematopoietic-progenitors
- question:0001-shared-molecular-signature-across-triggers
- question:0002-antigen-clearance-rescues-symptoms
- question:0055-hspc-epigenomic-imprinting-depth-predicts-pais-persistence
- question:0056-pharmacological-reversal-of-innate-immune-training-in-pais
- paper:Bomans2018
created: '2026-07-07'
updated: '2026-07-10'
added_by: "llm:claude-sonnet-4-6:research-topic"
---

# Innate Immune Memory and Trained Immunity as an Antigen-Independent Persistence Mechanism in PAIS

## Scope Note

This topic synthesizes the trained-immunity / innate-immune-memory literature specifically as a candidate **antigen-independent persistence mechanism** for post-acute infection syndromes. It homes three project sub-questions — `question:0023` (cGAS-STING → IFN-I), `question:0024` (NLRP3/GSDMD pyroptosis loop), and `question:0026` (IL-6/STAT3 imprinting of hematopoietic progenitors) — under a single mechanistic umbrella. The general biology of trained immunity as an immune-homeostasis mechanism belongs to the peer project `health-immunity`; this synthesis keeps its framing anchored to post-infectious persistence.

## Summary

Trained immunity — the durable epigenetic and metabolic reprogramming of innate immune cells and their bone-marrow progenitors that renders them constitutively hyperreactive — is an emerging candidate explanation for why post-acute infection syndromes (PAIS) persist long after infectious triggers are cleared, *without* requiring ongoing antigen or adaptive T-cell engagement. The central trained-immunity idea is that acute infection can imprint hematopoietic stem and progenitor cells (HSPCs) in the bone marrow, so that every newly generated monocyte arrives pre-activated — an antigen-independent, continuously replenished inflammatory output. The strongest direct evidence in a PAIS-relevant context is Cheong et al. 2023 (Cell), which demonstrates that severe SARS-CoV-2 infection induces durable HSPC chromatin remodeling (ATAC-seq) and myelopoiesis skewing that persists up to 12 months and is conveyed to progeny monocytes, with acute IL-6 as a key imprinting signal. The PAIS-specific causal evidence — that this imprint *drives* symptoms rather than merely correlating with acute severity — does not yet exist. The field is in an inferential phase: the mechanism is biologically plausible, mechanistically connected to documented PAIS immune features, and supported by observational data in COVID-19 convalescents, but direct interventional evidence linking trained HSPC phenotype to PAIS symptom burden is absent [@Netea2016; @Cheong2023; @Gu2023; @Humer2025].

## Key Concepts

**Trained immunity (innate immune memory).** Innate immune cells — monocytes, macrophages, NK cells — can retain a functionally altered state after an initial stimulus and respond more vigorously to secondary, unrelated stimuli. Unlike adaptive memory, this does not involve clonal expansion or antigen-specific receptors; it is mediated by epigenetic and metabolic reprogramming. The canonical training stimuli are BCG vaccination and β-glucan (fungal cell-wall component); oxLDL, uric acid, and DAMPs also induce training. The key functional consequence is that trained innate cells produce more inflammatory cytokines (TNF, IL-6, IL-1β, IL-12) and mount stronger oxidative bursts upon restimulation [@Netea2016].

**Peripheral vs central (HSPC-level) training.** The original trained-immunity paradigm described peripheral monocyte-level epigenetic memory, which is self-limiting because circulating monocytes live only 1-7 days. *Durable* (months-to-years) trained immunity requires imprinting of HSPCs in the bone marrow, so that each newly generated monocyte inherits the trained phenotype — the **central training** model. Mitroulis et al. 2018 (Cell) established, in murine and human systems, that β-glucan modulates myeloid progenitor fate in bone marrow and that this is an integral component of trained-immunity effects lasting beyond monocyte turnover [@Mitroulis2018]. This distinction is critical for PAIS: months-long monocyte hyperreactivity cannot be explained by peripheral monocyte imprinting alone; central HSPC imprinting is required.

**Epigenetic basis: H3K4me3, H3K27ac, and chromatin accessibility.** Trained immunity is mechanistically anchored in epigenetic reprogramming at inflammatory gene loci. Key marks include:
- **H3K4me3** (active promoter) and **H3K4me1** (poised enhancer) deposited at promoters and enhancers of TNF, IL-6, CXCL8, and other inflammatory response genes — facilitating transcription upon restimulation without requiring de novo gene activation.
- **H3K27ac** (active enhancer activation) replacing H3K27me3 (repressive).
- **Chromatin accessibility** (ATAC-seq open chromatin) at innate immune gene loci — the readout used by Cheong2023 for COVID-HSPC imprinting.
- Fumarate accumulation (from glutaminolysis) inhibits KDM5 histone demethylases, preventing erasure of H3K4me3 marks — linking TCA cycle intermediates directly to epigenetic memory [@Arts2016].

**Metabolic basis: glycolysis, glutaminolysis, mevalonate, itaconate.** Metabolic reprogramming is both a consequence and a driver of the trained phenotype:
- **Glycolysis / mTOR / HIF-1α axis:** β-glucan-trained monocytes shift from oxidative phosphorylation to aerobic glycolysis (Warburg-like), dependent on mTOR activation via dectin-1 → Akt → mTOR → HIF-1α. Inhibition of Akt, mTOR, or HIF-1α blocks training induction [@Cheng2014].
- **Glutaminolysis / fumarate:** Glutamine catabolism generates fumarate, which accumulates and inhibits KDM5 histone demethylases, enabling H3K4me3 deposition at inflammatory loci — the metabolic-epigenetic bridge [@Arts2016].
- **Mevalonate pathway:** Statin-blockable cholesterol biosynthesis contributes to trained immunity induction by LPS and oxLDL.
- **Itaconate:** An anti-inflammatory TCA intermediate produced by IRG1 that inhibits training induction and blocks NLRP3 activation — relevant as a potential natural brake on trained immunity.

**The antigen-independent-persistence hook.** The defining advantage of the trained-immunity frame for PAIS is that it predicts **inflammatory hyperreactivity without ongoing antigen, without adaptive immune engagement, and without replicating virus**. This makes it mechanistically distinct from:
- `topic:antigen-pathogen-persistence` (requires ongoing antigen, tested by `question:0002`)
- `hypothesis:0003` (immune exhaustion loop, which still requires antigen or a sterile persistent antigenic stimulus to drive T-cell exhaustion)
The trained-HSPC frame predicts that even if antigen is fully cleared, the bone-marrow myeloid output remains hyperinflammatory, explaining why antiviral/antigen-clearing trials have not yet produced robust symptom reversal.

**Tolerance vs training: the post-sepsis dual phenotype.** Sepsis and critical illness can produce *either* trained immunity (enhanced reactivity, hyperinflammatory) *or* immune tolerance (endotoxin tolerance, immunosuppression, vulnerability to secondary infection) in myeloid cells, depending on stimulus intensity, timing, and cell compartment. Bomans et al. 2018 (Frontiers Immunology) showed that sepsis induces long-lasting trained immunity in *bone marrow* naive monocytes (HSPC-level), while circulating monocytes can simultaneously exhibit tolerance — suggesting that compartment and cell maturity determine the direction of innate reprogramming. In PAIS, both phenotypes may coexist: peripheral circulating monocytes may be tolerized (blunted TLR response, contributing to immune exhaustion in `hypothesis:0003`), while naive HSPC-derived progeny arriving from the marrow are trained (hyperinflammatory output). This is not well-characterized in any PAIS cohort [@Bomans2018].

## Current State of Knowledge

### Well-established in the trained-immunity field (general)

- Monocytes and macrophages can acquire durable epigenetic memory after a range of infectious or inflammatory stimuli (BCG, β-glucan, oxLDL, uric acid); this memory enhances cytokine output upon secondary stimulation and is mechanistically anchored in H3K4me3/H3K27ac remodeling at inflammatory loci (Netea2016, landmark field review).
- The metabolic-epigenetic engine: Cheng2014 (Science) identified the mTOR/HIF-1α glycolytic switch; Arts2016 (Cell Metabolism) identified glutaminolysis/fumarate → KDM5 demethylase inhibition → H3K4me3 accumulation; Saeed et al. 2014 demonstrated genome-wide H3K4me3 changes in trained monocytes.
- Durable training requires HSPC-level imprinting: Mitroulis2018 (Cell) demonstrated in murine and human systems that β-glucan modulates myeloid progenitor fate in bone marrow and that this bone-marrow effect — not just peripheral monocyte memory — accounts for the multi-month persistence of trained immunity.
- NLRP3's role in trained immunity is best supported as a *functional dependency*, not a demonstrated epigenetically-primed locus: Christ2018 (Cell) showed that Western-diet-induced central myeloid training (GMP expansion + progenitor transcriptomic reprogramming) is abolished in *Nlrp3⁻/⁻* mice — establishing NLRP3 as a required upstream inducer of central training — but its ATAC-seq maps opened chromatin at *Tet2/Tlr4*, not at the NLRP3 or IL1B loci. The genome-wide trained-monocyte epigenomic map (Saeed2014, Science) covers IL1B/NLRP3 within the dataset, but its *training-specific* enhancer signature is predominantly metabolic/cAMP and it does not spotlight an inflammasome-locus training mark. **No primary study demonstrates elevated H3K4me3/accessibility at the NLRP3 or pro-IL-1β locus specifically in trained cells** — a claim frequently asserted in reviews but not directly grounded (t112 re-sourcing, 2026-07) [@Christ2018; @Saeed2014].

### Directly COVID/PAIS-relevant evidence (observational, not causal)

- **Cheong2023 (Cell) — the load-bearing COVID paper.** Jin-Gyu Cheong, Arjun Ravishankar et al. at Mount Sinai used combined snRNA/ATAC-seq on peripheral blood HSPCs from COVID-19 patients (severe, mild, and convalescent) and healthy controls. Key findings: (1) severe COVID induces persistent differential chromatin accessibility in HSPCs at inflammatory gene loci; (2) altered HSPC epigenomic programs are conveyed to progeny monocytes (transmission confirmed); (3) durable increases in myelopoiesis skewing toward inflammatory myeloid output; (4) the pattern persists to 12 months post-infection; (5) acute IL-6 — not just viral exposure — is mechanistically required: IL-6 blockade in a mouse coronavirus model prevented the epigenomic imprint. This is the strongest available evidence that a PAIS-relevant infection can centrally train HSPCs via IL-6 signaling. Limitations: no symptom correlation reported; severity-selection (most subjects were hospitalized); long COVID phenotyping is not reported [@Cheong2023].
- **Gu2023 (Frontiers Immunology).** A synthesis review (Gu, Liu, Zhang, Xu, 2023) proposing that the HSPC-to-monocyte epigenetic imprinting pathway, driven by acute IL-6, constitutes a "trained immunity" contribution to the long COVID inflammatory burden. The review synthesizes Cheong2023 and related data but does not present original data. It explicitly links IL-6/STAT3 → HSPC imprinting → hyperreactive monocyte output as a candidate long COVID mechanism, coincident with `question:0026` [@Gu2023].
- **Humer2025 (Frontiers Immunology).** A 2025 mini review from Erasmus Medical Center (Humer, Dik, Versnel) explicitly advocates for trained immunity as a pathogenic mechanism in ME/CFS, noting that: (1) approximately 60% of ME/CFS cases follow a recognized acute infection; (2) trained immunity induces the hyperresponsive monocyte phenotype and NK cell alterations documented in ME/CFS; (3) HSPC-level imprinting could explain why these changes persist despite monocyte turnover. Importantly, there are no direct epigenomic studies of HSPCs in ME/CFS patients: the proposal is conceptual, based on analogical reasoning from the trained-immunity framework and the ME/CFS myeloid-cell literature [@Humer2025].
- **Bomans2018 (Frontiers Immunology).** The post-sepsis parallel: Bomans, Schenz et al. 2018 showed that sepsis induces long-lasting enhanced cytokine production and glycolytic reprogramming in bone marrow monocytes (PICS model, murine cecal ligation and puncture with human validation) — demonstrating that a critical illness stimulus can centrally train the myeloid compartment. This is the principal support for the claim that non-COVID PAIS triggers can also drive central training, but only sepsis has been directly demonstrated; whether Borrelia, Coxiella, or EBV acute infection similarly imprints HSPCs is entirely inferred [@Bomans2018].

### What is contested or uncertain

- **Causal direction.** None of the PAIS-specific studies (Cheong2023, Gu2023, Humer2025) demonstrate that the trained-HSPC phenotype *causes* PAIS symptoms. Cheong2023 establishes the imprint is present and transmitted; Gu2023 argues it contributes; but no study has correlated HSPC imprinting depth with PAIS severity, duration, or symptom burden, let alone tested whether reversing the imprint resolves symptoms.
- **Severity selection and confounding.** Cheong2023's strongest HSPC data are from severely ill, hospitalized patients. PAIS (especially long COVID) affects primarily non-severely ill patients. Whether mild-to-moderate acute infection induces the same HSPC imprinting depth is not established.
- **Non-COVID PAIS.** HSPC-level epigenomic reprogramming has been documented only after COVID (Cheong2023) and sepsis (Bomans2018) in human studies. Whether Borrelia, Coxiella burnetti, EBV, dengue, or influenza acute infection drives comparable HSPC central training is unknown. The ME/CFS advocacy in Humer2025 is conceptual, not backed by ME/CFS-specific epigenomic data.
- **Tolerance vs training coexistence.** Post-COVID monocytes show both activated and tolerized features depending on cohort, timing, and assay. The Bomans2018 dual-compartment model (HSPC-level training + peripheral tolerance) has not been directly tested in long COVID or ME/CFS. Whether a circulating-monocyte tolerance observation contradicts or coexists with central HSPC training is unresolved.
- **Protective vs harmful trained immunity.** In the Cheong2023 system, the trained-HSPC phenotype persists longer in severe COVID than mild. In cancer and vaccine biology, trained immunity is protective. In PAIS, the same trained phenotype is proposed as a pathogenic inflammatory driver. The difference may be context (ongoing pathological signaling environment vs resolved infection with normal tissue milieu) but this distinction is not empirically established in PAIS.
- **Whether the imprint is reversible.** The half-life of the HSPC imprint is not known for COVID-specific training; β-glucan studies suggest months-scale persistence. Whether it reverses spontaneously with disease recovery, or whether reversal requires active intervention, is unknown.

## The Three Sub-mechanisms as Connected Subtopics

Three project questions home under this topic as mechanistically connected components of the trained-immunity axis:

### cGAS-STING → IFN-I (question:0023)

SARS-CoV-2 releases mitochondrial DNA (mtDNA), viral RNA fragments, and micronuclear dsDNA into the cytoplasm; herpesviruses and Borrelia generate cytoplasmic nucleic acids via DNA damage or lytic replication. cGAS detects cytoplasmic dsDNA → activates STING → TBK1 → IRF3 → IFN-I production. This is the sensor that initiates and sustains IFN-I signaling without requiring active replication (`question:0023`). **The trained-immunity connection here is weakly grounded and largely conjectural.** A dedicated re-sourcing pass (t112, 2026-07) found **no primary study reporting chromatin accessibility or activating histone marks at cGAS / STING (TMEM173) / IRF / ISG loci in trained myeloid cells**. The only primary support linking STING to trained immunity is *functional*: STING agonism (e.g. c-di-AMP-overexpressing BCG constructs) can augment BCG-driven trained immunity, and type-I-IFN *signaling* gates β-glucan-driven hematopoietic expansion — but neither provides a locus-level epigenomic readout at the sensor loci. The earlier framing here (that trained HSPCs carry elevated STING/IFN-locus accessibility, or that chronic STING signaling deposits an IFN-trained chromatin imprint sustaining IFN-I without ongoing cGAS ligand) is therefore a **mechanistic hypothesis, not an evidenced link** in trained cells or in PAIS. `Question:0023` — cGAS-STING as an upstream IFN-I driver in PAIS — remains legitimate on general innate-immunology grounds (mtDNA/dsDNA sensing does drive STING→TBK1→IRF3→IFN-I), but should **not** be treated as an established sub-branch of the trained-immunity *epigenomic* axis until primary locus-level evidence exists.

### NLRP3/GSDMD pyroptosis loop (question:0024)

The link between NLRP3 and trained immunity is real but is best characterized as a **functional/genetic dependency rather than a demonstrated locus-level chromatin imprint**. Christ2018 established that central myeloid training (progenitor expansion + transcriptomic reprogramming) *requires* NLRP3: *Nlrp3⁻/⁻* mice fail to develop the trained phenotype, placing NLRP3 as a required upstream inducer of the training program — though the accompanying ATAC-seq shows opened chromatin at *Tet2/Tlr4*, not at NLRP3 or IL1B. The frequently-asserted claim that trained monocytes carry elevated H3K4me3 at the NLRP3/pro-IL-1β promoters, eliminating the need for NF-κB priming, is **not directly demonstrated in the primary epigenomic literature** (Saeed2014's training-specific signature is metabolic, not inflammasome-centric; its IL-1β result is a monocyte→macrophage differentiation finding, not a training-specific locus mark). The downstream loop described in `question:0024` — disproportionate IL-1β/IL-18 output to small secondary stimuli (DAMPs, ATP, cholesterol crystals, urate), GSDMD pyroptosis releasing DAMPs (IL-1α, ATP, mtDNA, HMGB1) that could re-train neighboring cells or re-engage cGAS-STING — is therefore a **positive-feedback loop that is mechanistically coherent but rests on a functional NLRP3-dependence result plus inference, not on a confirmed NLRP3-locus training mark**. It remains uninvestigated as a DAMP-driven training loop in any PAIS system [@Christ2018; @Saeed2014].

### IL-6/STAT3 imprinting of hematopoietic progenitors (question:0026)

This is the most mechanistically direct and best-evidenced connection. Cheong2023 explicitly demonstrated that acute IL-6 — not merely viral exposure — is required for HSPC epigenomic imprinting after COVID: IL-6 blockade in a mouse coronavirus model prevented the HSPC chromatin remodeling. The proposed mechanism: IL-6 → JAK1/2 → STAT3 → epigenetic remodeling of inflammatory gene promoters in HSPCs (H3K4me3 deposition, chromatin opening) → every HSPC-derived monocyte inherits a hyperreactive inflammatory epigenome — a constitutively trained myeloid output that is antigen-independent. STAT3 interacts directly with chromatin-modifying complexes (EZH2, BRD4) and can imprint gene promoters in long-lived progenitors in ways that survive cell division. Because IL-6 peaks during severe acute illness (when PAIS risk is highest), the imprinting depth is plausibly proportional to acute-IL-6 burden — offering an explanation for why acute severity predicts PAIS incidence. `Question:0026` was independently surfaced by two explore-ideas lenses and is the most developed sub-question under this topic. The PAIS-specific causal evidence gap remains: Cheong2023 shows the imprint at 12 months, but no study has tested whether the imprint depth predicts *who develops* PAIS vs who fully recovers [@Cheong2023; @Gu2023].

### How the sub-mechanisms relate

A plausible integrated model: (1) Severe acute infection → high IL-6 → HSPC STAT3 signaling → HSPC epigenomic imprinting → continuous hyperreactive monocyte output for months-to-years (the central trained-immunity axis, q0026). (2) Each newly arriving trained monocyte is *hypothesized* to be hyperresponsive to residual DAMP signals via the q0023 (cGAS-STING/IFN) and q0024 (NLRP3/IL-1β) axes — though, as noted above, the locus-level chromatin grounding for these two axes in trained cells is **not** established (the NLRP3 link rests on a functional dependency; the cGAS-STING link is conjectural). (3) Pyroptotic GSDMD pores from NLRP3-hyperresponsive trained cells release mtDNA and other DAMPs → re-engages cGAS-STING in neighboring cells → sustains IFN-I production → feeds back onto HSPC differentiation signals. This creates an antigen-independent self-sustaining loop that could maintain the h0001 attractor state. All connections are mechanistically coherent but remain hypothetical in PAIS; no study has tested them in an integrated fashion.

## Relevance to This Project

**As an antigen-independent persistence mechanism, trained immunity is the key mechanistic alternative/complement to the project's antigen-persistence frame.** The project currently has strong coverage of antigen-dependent persistence (h0002, q0002, `topic:antigen-pathogen-persistence`) and adaptive immune exhaustion (h0003). The trained-immunity axis adds a third route to chronification that is:
- Independent of ongoing antigen (diverges from `topic:antigen-pathogen-persistence`)
- Independent of adaptive T-cell engagement (diverges from h0003)
- Capable of sustaining the inflammatory/IFN-I state long after full pathogen clearance
- Proportional to acute disease severity (through IL-6 imprinting depth), consistent with the acute-severity → PAIS-risk relationship

**Links to existing project entities:**
- `hypothesis:0001-shared-dysregulated-attractor`: Trained HSPC imprinting is a candidate maintenance mechanism that could hold the system in the attractor state after the trigger is cleared. The central-training model predicts attractor persistence that is *independent of* antigen, providing the stability that the attractor metaphor requires.
- `hypothesis:0003-immune-exhaustion-feedback`: Adaptive exhaustion and innate training are not mutually exclusive. Trained monocytes could sustain innate inflammatory output even as adaptive CD8+ T cells are exhausted, contributing to the paradoxical co-occurrence of inflammation and exhaustion documented in Aid2025.
- `hypothesis:0014-nk-failure-clear-senescent-endothelium-sasp-propagation`: Trained immunity concepts extend to NK cells. Documented NK cytotoxic dysfunction in ME/CFS could reflect a tolerance rather than training phenotype; alternatively, NK cells could be trained to produce IFN-γ and cytokines but not cytotoxicity — creating a pathological NK phenotype. The interaction of HSPC-trained myeloid output with NK function in PAIS is uninvestigated.
- `question:0001-shared-molecular-signature-across-triggers`: Trained HSPC imprinting offers a candidate shared molecular signature that is pathway-level (chromatin accessibility at innate loci, myelopoiesis bias) rather than analyte-level. Whether this signature appears across PAIS triggers (not just COVID and sepsis) is untested but would be a concrete test of the shared-attractor hypothesis if data become available.
- `question:0002-antigen-clearance-rescues-symptoms`: The trained-immunity frame offers the most coherent explanation for the antigen-clearance trial nulls: if HSPC central training is established, removing the antigen does not reset the bone-marrow epigenome; trained myeloid output continues. This predicts that antiviral trials will fail to rescue established PAIS symptoms unless combined with epigenetic-reprogramming or immunometabolic intervention.

**Boundary with `health-immunity` peer project.** The general-immunology biology of trained immunity (BCG/β-glucan mechanisms, metabolic reprogramming in monocytes, HSPC fate decisions, trained vs tolerance) belongs in `health-immunity`. This topic retains only the *post-infectious PAIS persistence* framing: how a training event established by acute infection maintains inflammatory dysregulation in the chronic phase.

## Controversies and Open Questions

1. **Causal or correlational?** Cheong2023's HSPC imprint is present at 12 months after severe COVID but is not linked to PAIS symptoms. The decisive test — correlation of imprinting depth with PAIS symptom burden and duration — has not been done. Establishing causation would require either a prospective design (imprinting depth at 3 months predicts PAIS at 12 months) or an interventional test (reversing the imprint improves symptoms).

2. **Severity threshold and non-hospitalized disease.** All direct HSPC epigenomic data in COVID (Cheong2023) derive from severe/hospitalized patients. Long COVID prevalence is higher after severe acute illness, but the majority of long COVID cases follow mild-to-moderate acute disease. Whether mild COVID induces the same central training is unknown.

3. **Cross-trigger generalizability.** Only COVID (Cheong2023) and sepsis (Bomans2018) have direct HSPC-training evidence in humans. Whether Borrelia, Coxiella, EBV, dengue, or influenza acute infection imprints HSPCs is entirely inferred. If the mechanism requires high IL-6 specifically, it would predict weaker HSPC imprinting after pathogens that elicit lower IL-6 peaks — a testable corollary. **This corollary was tested via a cross-pathogen acute serum-IL-6 desk compilation (t108, 2026-07-10 → `interpretation:0039-t108-cross-pais-il6-peak-vs-pais-risk`) and did NOT hold:** low-IL-6 triggers (Q fever ~49 pg/mL, Lyme ~21–26 with IL-6 not even a top acute marker, EBV/IM IFN-γ-dominated) still produce ~12–20% post-infectious fatigue, and the Dubbo prospective three-pathogen cohort found ~identical incidence predicted by acute *severity*, not any cytokine [@Hickie2006]. The finding refutes only the *serum-IL-6-magnitude-as-cross-pathogen-proxy* shortcut (defeated by 10–100× cross-assay non-comparability and severity-confounding), **not** the within-COVID IL-6→HSPC mechanism. The mechanism's live cross-trigger test is therefore the direct-epigenomic one (`question:0055` / t107), not a serum-cytokine surrogate. **That direct route has now been feasibility-scoped (t107 → `interpretation:0040-t107-hspc-epigenomics-feasibility-banked-pbmc`, 2026-07-10): it is buildable opportunistically on already-banked PAIS blood, but the feasible high-leverage readout is *monocyte-progeny ATAC-seq* (abundant; the imprint's transmitted readout per Cheong2023), not rare circulating-CD34⁺ HSPC ATAC (marginal cell yield + compartment-mismatched to Cheong2023's marrow HSPCs); the definitive same-compartment test needs LIINC's banked bone marrow.**

4. **Tolerance vs training in the same PAIS patient.** Post-sepsis biology (Bomans2018) suggests compartment-dependent divergence (naive BM monocytes trained, circulating monocytes tolerized). In long COVID patients, both hyperreactive monocytes (TLR-hypersensitivity, IL-6 excess) and tolerized monocytes (blunted antiviral responses) have been reported across different cohorts — possibly reflecting the same dual-compartment biology. Whether these are distinct endotypes or coexisting within the same patient across cell maturation states is unresolved.

5. **Reversibility and therapeutic window.** β-Glucan-induced murine trained immunity can be reversed by DNMT inhibitors (azacytidine), BET bromodomain inhibitors (JQ1), and, paradoxically, by some statins. Whether these agents can reverse COVID-specific HSPC imprinting, and at what post-infection timepoint intervention remains effective, is not known. The therapeutic window — if it exists — could be narrow (before the imprint is fully consolidated) or might persist (if the imprint is maintained by ongoing cytokine signals that could be pharmacologically blocked).

6. **Itaconate as a natural brake.** Itaconate, produced by IRG1-expressing macrophages in response to LPS/IL-4, is anti-inflammatory and blocks trained immunity induction. Whether PAIS patients have attenuated itaconate production (removing this natural brake) is an unexplored question.

7. **HSPC imprint as a biomarker of PAIS risk.** If imprinting depth at 3-6 months post-infection predicts PAIS chronification, ATAC-seq or H3K4me3 ChIP-seq in sorted HSPCs or even bulk monocytes from peripheral blood could serve as a PAIS biomarker and patient-stratification tool. This is addressed by `question:0055`.

## Key References

- **Netea2016** — Netea MG et al., Science 2016; the foundational trained-immunity review: epigenetic and metabolic mechanisms, BCG/β-glucan paradigm, conceptual framework.
- **Cheng2014** — Cheng SC et al., Science 2014; mTOR/HIF-1α-mediated aerobic glycolysis as the metabolic basis for β-glucan-induced trained immunity in monocytes.
- **Arts2016** — Arts RJW et al., Cell Metabolism 2016; glutaminolysis and fumarate accumulation integrate immunometabolic and epigenetic programs; KDM5 demethylase inhibition as the metabolic-epigenetic bridge.
- **Mitroulis2018** — Mitroulis I et al., Cell 2018; HSPC-level β-glucan training in bone marrow as the substrate for durable (months) trained immunity; myelopoiesis modulation as an integral trained-immunity component.
- **Saeed2014** — Saeed S et al., Science 2014; genome-wide H3K4me3/H3K4me1/H3K27ac map of β-glucan-trained vs naive vs tolerized human monocytes; foundational epigenomic resource — but its *training-specific* enhancer signature is predominantly metabolic/cAMP, and it does **not** spotlight NLRP3/IL1B or an inflammasome-locus training mark (seeded for t112 to bound the q0024 grounding).
- **Christ2018** — Christ A et al., Cell 2018; Western-diet-induced central myeloid training in *Ldlr⁻/⁻* mice is **NLRP3-dependent** (abolished in *Nlrp3⁻/⁻*); GMP ATAC-seq opens *Tet2/Tlr4*, not the NLRP3 locus. Grounds "central training is NLRP3-dependent (functional)"; does **not** ground a NLRP3-locus chromatin imprint (seeded for t112).
- **Cheong2023** — Cheong JG et al., Cell 2023; epigenetic memory of coronavirus infection in innate immune cells and their progenitors; HSPC ATAC-seq reprogramming persisting to 12 months; IL-6 as required imprinting signal. *The most important PAIS-relevant trained-immunity paper.*
- **Gu2023** — Gu J et al., Front Immunol 2023; COVID-19 and trained immunity: synthesis review proposing IL-6-mediated HSPC imprinting as a contributor to the long COVID inflammatory burden.
- **Bomans2018** — Bomans K et al., Front Immunol 2018; sepsis induces long-lasting trained immunity in bone marrow monocytes; post-sepsis parallel and evidence for HSPC-level non-COVID PAIS training.
- **Humer2025** — Humer B, Dik WA, Versnel MA, Front Immunol 2025; advocacy for trained immunity in ME/CFS pathogenesis; conceptual bridge from COVID/BCG data to ME/CFS monocyte/NK phenotype.
- **Aid2025; Klein2023** — persistent JAK-STAT/IL-6/IFN activation plus CD8+ exhaustion in long COVID; non-conventional monocyte elevation; context for how the trained-myeloid phenotype would appear in existing long COVID immune profiles.

## Suggested Follow-up Research Tasks

1. **Prospective HSPC epigenomic profiling in PAIS cohort:** ATAC-seq and H3K4me3 ChIP-seq on peripheral blood HSPCs (or sorted monocytes) at 3 and 12 months post-infection, with PAIS vs full-recovery endpoints, across at least COVID and one non-COVID PAIS trigger. This would test whether central training predicts chronification (addresses `question:0055`) and whether the signal is trigger-shared.

2. **In vitro reversal screen (immunometabolic agents):** Test itaconate, BET inhibitors (JQ1), DNMT inhibitors, and statins against the trained phenotype induced by COVID-patient serum or IL-6/STAT3 stimulation of healthy donor HSPCs. Maps the pharmacological space for `question:0056` before clinical trials.

3. **Seed papers into this topic entity:** Identify and ingest the primary epigenomic studies cited here (Cheong2023, Mitroulis2018, Arts2016, Cheng2014) as paper entities; link them to this topic and to `question:0026` for graph connectivity and belief-tracking.
