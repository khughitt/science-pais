---
id: paper:Raijmakers2019
kind: paper
title: A possible role for mitochondrial-derived peptides humanin and MOTS-c in patients
  with Q fever fatigue syndrome and chronic fatigue syndrome
status: active
ontology_terms:
  - Q-fever fatigue syndrome
  - chronic fatigue syndrome
  - mitochondrial-derived peptides
  - humanin
  - MOTS-c
  - bioenergetics
  - monocyte transcriptomics
  - RNA sequencing
dataset_usage: []
datasets: []
source_refs:
  - cite:Raijmakers2019
related:
  - question:0001-shared-molecular-signature-across-triggers
  - question:0011-mitochondrial-basis-of-pem
  - discussion:0002-cross-pathogen-pais-signature-convergence
  - hypothesis:0001-shared-dysregulated-attractor
created: '2026-06-20'
updated: '2026-06-20'
---
# A possible role for mitochondrial-derived peptides humanin and MOTS-c in patients with Q fever fatigue syndrome and chronic fatigue syndrome

- **Authors:** Ruud P. H. Raijmakers, Anne F. M. Jansen, Stephan P. Keijmel, Rob ter Horst, Megan E. Roerink, Boris Novakovic, Leo A. B. Joosten, Jos W. M. van der Meer, Mihai G. Netea, Chantal P. Bleeker-Rovers
- **Year:** 2019
- **Journal:** Journal of Translational Medicine, vol. 17, p. 157
- **DOI:** 10.1186/s12967-019-1906-3
- **PMID:** 31088495
- **PMCID:** PMC6518812
- **BibTeX key:** Raijmakers2019
- **Source:** Full-text via science paper-fetch (DOI 10.1186/s12967-019-1906-3), read 2026-06-20

## Key Contribution

This paper provides the first within-study, head-to-head monocyte transcriptomic comparison of Q fever fatigue syndrome (QFS) and chronic fatigue syndrome (CFS), revealing that the mitochondrial ribosomal RNA genes MT-RNR1 (encoding MOTS-c) and MT-RNR2 (encoding humanin) are strongly and significantly downregulated in both conditions relative to healthy controls, at comparable magnitudes. The functional finding is a parallel reduction in LPS-stimulated humanin protein production in both QFS and CFS patients (and, to a lesser extent, asymptomatic Q fever seropositive controls), supporting the hypothesis that mitochondrial-derived peptide dysregulation is a shared feature of post-infectious fatigue syndromes regardless of the triggering pathogen (bacterial vs idiopathic).

## Methods

**Design:** Cross-sectional, case-control study with four matched groups (n = 10 per group for RNA-seq; note: the Methods section states CFS n = 11 at enrollment but the RNA-seq analysis used n = 10 per group, consistent with the abstract and Table 1).

**Groups:**
- QFS patients (n = 10): diagnosed at the Radboud Expert Center for Q Fever per Dutch national QFS guidelines; fatigue ≥ 6 months post-acute Q fever, CIS fatigue subscale ≥ 35, SIP-8 ≥ 450; chronic Q fever excluded; Q fever IgG seropositivity confirmed.
- CFS patients (n = 10): diagnosed at Radboud's Expert Center for Chronic Fatigue per CDC (Fukuda 1994) criteria, augmented by CIS ≥ 35 and SIP-8 ≥ 450; Q fever seronegative.
- Asymptomatic Q fever seropositive controls (n = 10): seropositive (IgG phase I or II ≥ 1:16, phase I < 512) ≥ 5 years after the 2007–2011 Dutch Q fever outbreak; no fatigue complaints.
- Healthy controls (n = 10): Q fever seronegative colleagues from the same institution with no fatigue.

All groups were age- (±5 years) and sex-matched. Median ages were comparable across groups (43–54 years). Median symptom duration: QFS 78 months (IQR 62–87), CFS 110 months (IQR 31–253), not significantly different.

**Transcriptomics:** Monocytes were isolated from PBMCs by Percoll density gradient from unstimulated whole blood. RNA was extracted with mirVana kit; RNA-seq performed (GEO: GSE130353). Reads aligned with GSNAP; expression quantified with MMSEQ; differential expression analysed with DESeq2. PCA performed on top 500 varying genes. Pathway enrichment via ClueGO (KEGG, Reactome, WikiPathways) with Benjamini-Hochberg correction; genes with P < 0.01 and ≥ 2-fold change used as input.

**Protein assays:** PBMCs were stimulated with 10 ng/mL LPS for 24 h; supernatants assayed for humanin and MOTS-c by ELISA (MyBioSource). Circulating (unstimulated plasma) humanin and MOTS-c were also measured (no between-group differences found in circulation).

**Statistics:** Mann-Whitney and Kruskal-Wallis for non-parametric group comparisons; significance threshold P < 0.05.

## Key Findings

**Transcriptomics — MT-RNR1 and MT-RNR2 downregulation (positive finding, highly significant):**

Both MDP-coding genes were the most consistently and significantly downregulated genes in patient groups vs healthy controls, and were the standout signal from the full transcriptome analysis:

| Gene | Group vs healthy controls | log2 fold change | P value |
|---|---|---|---|
| MT-RNR2 (humanin) | CFS | −5.2 | 3.49 × 10^−11 |
| MT-RNR1 (MOTS-c) | CFS | −4.4 | 2.71 × 10^−9 |
| MT-RNR2 (humanin) | QFS | −4.8 | 2.19 × 10^−9 |
| MT-RNR1 (MOTS-c) | QFS | −4.9 | 4.69 × 10^−8 |
| MT-RNR2 (humanin) | Q fever seropositive controls | −3.7 | 1.78 × 10^−6 |
| MT-RNR1 (MOTS-c) | Q fever seropositive controls | −3.2 | 1.12 × 10^−5 |

The magnitude of downregulation was statistically similar between QFS and CFS (both ~4.4–5.2 log2 FC), and greater than that seen in asymptomatic seropositive controls (~3.2–3.7 log2 FC). No significant direct QFS vs CFS difference in MT-RNR1/MT-RNR2 expression was reported.

**Humanin protein (positive finding, P = 0.05):**

LPS-stimulated humanin production was reduced in all three non-healthy-control groups vs healthy controls (P = 0.05 overall; Kruskal-Wallis):
- Healthy controls: 395 pg/mL (IQR 372–409)
- QFS patients: 371 pg/mL (IQR 325–384)
- CFS patients: 364 pg/mL (IQR 316–387)
- Q fever seropositive controls: 354 pg/mL (IQR 292–393)

The reduction was modest in absolute terms (~6–10% vs healthy) but statistically significant at P = 0.05. QFS and CFS values were nearly identical. Circulating (unstimulated) humanin did not differ between groups.

**MOTS-c protein (null finding):**

Despite MT-RNR1 being significantly downregulated at the transcript level in all groups, LPS-stimulated MOTS-c protein levels were at or near the lower detection limit (~2.47 pg/mL) and showed no significant between-group difference. Authors attribute this to possible constitutive extracellular production that is regulated through mechanisms independent of the LPS-stimulation paradigm.

**Overall transcriptome (largely null):**

PCA of the top 500 varying genes found no between-group separation; the only variation was explained by sex. Pathway enrichment at P ≤ 1 × 10^−5 yielded no results. At P ≤ 0.01, some mitochondrial pathway alterations were noted (supplementary data) but no clear immunological activation signal. The overall monocyte transcriptome is not grossly different between QFS, CFS, and healthy controls.

**QFS-specific signal:**

ALAS2 (delta-aminolevulinate synthase 2; heme synthesis) was upregulated in QFS vs both healthy controls and Q fever seropositive controls but not distinguishing QFS from CFS. This may relate to the elevated ferritin commonly observed in QFS patients.

## Relevance

This paper directly addresses `question:0011-mitochondrial-basis-of-pem` by providing monocyte-level transcriptomic and proteomic evidence for mitochondrial signaling peptide downregulation in chronic fatigue syndromes. The key result — that QFS (a post-bacterial PAIS) and CFS (idiopathic/heterogeneous) share an essentially identical MT-RNR1/MT-RNR2 downregulation signature in circulating monocytes — is one of the most direct cross-trigger molecular comparisons in the PAIS literature and is relevant to `discussion:0002-cross-pathogen-pais-signature-convergence`.

Humanin is anti-apoptotic, cytoprotective, and anti-inflammatory (signals via CNTFR/WSX-1/gp130 — the IL-6 receptor complex — activating JAK/STAT, AKT, and ERK). MOTS-c activates AMPK and regulates insulin resistance, metabolic homeostasis, and muscle metabolism. Reduced expression of both peptides supports a hypometabolic / bioenergetic failure model for fatigue (`hypothesis:0001-shared-dysregulated-attractor`) and provides a molecular bridgehead between the mitochondrial dysfunction thread and the immune-activation thread (via humanin's role in IL-6 axis signaling and neuroinflammation).

The finding that asymptomatic Q fever seropositive controls also show MT-RNR1/MT-RNR2 downregulation (albeit less severe) raises the possibility that acute Coxiella burnetii infection itself — rather than the chronic fatigue state per se — initiates this epigenetic or regulatory change, with the clinical fatigue syndrome emerging only in a subset who have additional co-factors. This complicates fatigue-causal interpretation.

The shared humanin reduction in QFS and CFS is relevant to `question:0001-shared-molecular-signature-across-triggers`, offering a bioenergetic-peptide candidate that crosses from post-bacterial to idiopathic fatigue.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Mitochondrial-derived peptides (humanin, MOTS-c) | Metabolic/mitochondrial dysfunction mechanism | MDPs as a specific measurable candidate within the broader mitochondrial failure hypothesis |
| MT-RNR1/MT-RNR2 downregulation in monocytes | Immune-cell bioenergetic impairment | The finding is in monocytes, not muscle or neurons — tissue generalizability unconfirmed |
| QFS vs CFS head-to-head | Cross-trigger comparison | Bacterial-trigger (Coxiella) vs idiopathic/heterogeneous trigger; matched design |
| Asymptomatic Q fever seropositives showing intermediate MDP-gene reduction | Exposure effect vs syndrome effect | Raises question of whether mito-peptide reduction is a direct infection sequela or specific to symptomatic fatigue |
| Hypometabolic state hypothesis | Shared dysregulated attractor (hypothesis:0001) | Authors explicitly reference the Naviaux hypometabolic model for CFS |
| Humanin / IL-6 receptor axis / neuroinflammation | Immune activation + neuroinflammation threads | Mechanistic link between bioenergetics and inflammation candidates |

## Limitations

1. **Very small sample size (n = 10 per group).** The effect sizes for MT-RNR1/MT-RNR2 are extremely large (log2 FC ~4–5, P < 10^−8), which is partly reassuring, but the humanin ELISA result (P = 0.05) and the MOTS-c null result should both be interpreted cautiously given N = 10.

2. **Unstimulated monocytes only for RNA-seq.** The PCA found no between-group separation at the full transcriptome level and only very limited pathway enrichment. The authors acknowledge that stimulated monocytes might reveal more. The overall transcriptome picture is essentially null, with MT-RNR1/MT-RNR2 being exceptional standout signals.

3. **CFS case definition is Fukuda (CDC 1994),** which is the broadest and least specific ME/CFS case definition. The Canadian Consensus Criteria or International Consensus Criteria would have selected a more homogeneous group with defined post-exertional malaise. Some enrolled CFS patients may not have PEM-defined ME/CFS.

4. **QFS diagnostic criteria** rely on the Dutch national guidelines and Q fever seropositivity; the study was conducted in a specialist center after the large Dutch 2007–2011 outbreak, which may limit generalizability to other Q fever-endemic contexts.

5. **MOTS-c ELISA near detection limit.** The assay produced signals at ~2.47 pg/mL (at or below the kit's stated detection range), so the null MOTS-c protein result may be a technical artifact of assay sensitivity rather than a true biological null. The mRNA downregulation for MT-RNR1 is real; the protein conclusion is uncertain.

6. **Asymptomatic seropositive controls reduce causal specificity.** The fact that healthy, asymptomatic Q fever seropositive individuals also show reduced MT-RNR1/MT-RNR2 means the mito-peptide reduction is not unique to the fatigue syndrome — it may be a post-Coxiella exposure effect. The authors speculate epigenetic remodeling from acute infection persisting long-term, but this is not demonstrated (cited as Raijmakers 2018, unpublished data).

7. **Cross-sectional design.** No pre-infection baselines; cannot establish whether MT-RNR1/MT-RNR2 downregulation precedes, follows, or co-occurs with the fatigue syndrome.

8. **Humanin ELISA measured in LPS-stimulated PBMCs, not monocytes.** The RNA-seq was performed on purified monocytes; the peptide ELISA was on PBMCs (a mixed population). This is a methodological inconsistency. Circulating (unstimulated) humanin did not differ between groups.

9. **No direct test of whether humanin or MOTS-c reduction causes fatigue or other symptoms.** The paper is correlational; functional studies are needed.

## Model / Tool Availability

Raw RNA-seq data are deposited at Gene Expression Omnibus under accession **GSE130353**. No analysis code or model is separately released. Assays used: mirVana RNA isolation, GSNAP alignment (non-default parameters), MMSEQ quantification, DESeq2 differential expression, ClueGO pathway analysis in Cytoscape, MyBioSource humanin and MOTS-c ELISA kits.

## Follow-up

- **Replicate in larger QFS and ME/CFS cohorts** with more stringent ME/CFS case definitions (CCC or ICC) and pre- vs post-infection samples to establish temporality.
- **Check GEO GSE130353** for the full monocyte transcriptome dataset; the broader gene list and pathway data may yield additional PAIS-relevant signals beyond MT-RNR1/MT-RNR2.
- **Stimulated monocyte transcriptomics:** The paper itself recommends following up with LPS- or antigen-stimulated monocyte RNA-seq. Unstimulated cells may be too quiescent to reveal immune-activation differences.
- **MOTS-c protein:** Repeat with a higher-sensitivity assay (e.g., mass spectrometry-based quantification) or in plasma rather than PBMC supernatant.
- **Epigenetic angle:** If MT-RNR1/MT-RNR2 reduction in asymptomatic seropositives reflects epigenetic remodeling by Coxiella, this would be worth testing via ATAC-seq or bisulfite sequencing on monocytes; compare with long-COVID monocyte epigenetics studies.
- **Humanin / IL-6 axis:** Test whether low humanin production correlates with elevated IL-6 or IL-6 receptor signaling in the same cohort; the gp130 connection could link this to the IL-6 dysregulation seen in QFS.
- **ALAS2 in QFS:** Follow up the heme-synthesis / ferritin signal as a potentially QFS-specific biomarker.
- Connects to: papers on ME/CFS mitochondrial dysfunction (Tomas et al. 2017 on PBMC mitochondrial function), Naviaux et al. hypometabolic model (Metabolomics 2016), and any long-COVID bioenergetics studies.
