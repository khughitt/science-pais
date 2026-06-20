---
id: paper:Raijmakers2019c
type: paper
title: Long-Lasting Transcriptional Changes in Circulating Monocytes of Acute Q Fever Patients
status: active
ontology_terms:
  - trained immunity
  - epigenetic reprogramming
  - monocyte transcriptome
  - Q fever
  - Coxiella burnetii
  - post-infectious fatigue
  - cytokine dysregulation
dataset_usage: []
datasets: []
source_refs:
  - cite:Raijmakers2019c
related:
  - question:0001-shared-molecular-signature-across-triggers
  - discussion:0002-cross-pathogen-pais-signature-convergence
created: '2026-06-20'
updated: '2026-06-20'
---
# Long-Lasting Transcriptional Changes in Circulating Monocytes of Acute Q Fever Patients

- **Authors:** Ruud Ph Raijmakers, John Stenos, Stephan P Keijmel, Rob Ter Horst, Boris Novakovic, Chelsea Nguyen, Jos Wm Van Der Meer, Mihai G Netea, Chantal P Bleeker-Rovers, Leo Ab Joosten, Stephen R Graves
- **Year:** 2019
- **Journal:** Open Forum Infectious Diseases, vol 6(7):ofz296
- **DOI:** 10.1093/ofid/ofz296
- **PMID:** 31363773
- **PMCID:** PMC6667718
- **BibTeX key:** Raijmakers2019c
- **Source:** Full-text via science paper-fetch (DOI 10.1093/ofid/ofz296), read 2026-06-20

## Key Contribution

This study provides the first in-human evidence that acute Q fever infection (caused by *Coxiella burnetii*) induces long-lasting transcriptional reprogramming of circulating monocytes persisting at least 6 months after infection — an effect the authors frame as infection-induced trained immunity acting through myeloid progenitor cells in the bone marrow. The paper adds Q fever to a short list of human infections demonstrated to remodel the myeloid epigenome and transcriptome in a durable fashion, paralleling what has been observed with live-vaccine challenge (e.g., BCG). An important caveat: the cohort is an undifferentiated group of acute Q fever patients; only 2 of 11 developed Q fever fatigue syndrome (QFS), making inferences about QFS-specific monocyte biology speculative at this sample size.

## Methods

**Design:** Longitudinal observational study; blood collected at a median of 27 days after the last sick day ("baseline") and again 6 months later ("follow-up").

**Cohort:** 11 acute Q fever patients diagnosed by immunofluorescence assay (phase 2 IgM positivity in the absence of high phase 1 IgG) recruited in Victoria and New South Wales, Australia, through the Australian Rickettsial Reference Laboratory. Compared against 15 age- and sex-matched healthy controls (colleagues in the Geelong/Launceston area, Q-fever seronegative by serology).

**Case definition:** Acute Q fever confirmed by serology. QFS at follow-up was diagnosed using the Dutch RIVM guideline minus the full somatic/psychiatric co-morbidity workup. At follow-up, 9 of 11 patients had recovered; 2 met criteria for QFS.

**Monocyte isolation:** 40 mL EDTA blood → PBMC isolation by Ficoll-Paque density centrifugation → monocyte enrichment by hyperosmotic Percoll gradient centrifugation.

**Transcriptomics platform:** Total RNA sequenced (RNA-seq); reads aligned to Ensembl v68 human transcriptome using Bowtie (Johns Hopkins); gene quantification via MMSEQ; differential expression via DESeq2 (input: MMSEQ Unique_hits counts, genes with mean count > 1 retained). PCA performed on top 500 varying genes. Pathway enrichment via ClueGO v2.1.7 in Cytoscape v3.2, using KEGG, Reactome, and WikiPathways databases; Benjamini-Hochberg correction applied.

**Cytokines:** Circulating IL-10, IL-1β, IL-1Ra, and IL-6 measured by Ella microfluidic analyzer (ProteinSimple) in serum; TNF-alpha also measured.

**Mitochondrial-derived peptide focus:** Expression of *MT-RNR1* (encodes MOTS-c) and *MT-RNR2* (encodes humanin) examined based on a prior finding that these genes are downregulated in QFS monocytes.

**In vitro trained-immunity experiment:** Naïve monocytes from healthy seronegative controls (buffy coats, Sanquin Bloodbank) were primed with *C. burnetii* antigen or RPMI for 24 h, washed, rested 6 days, then re-stimulated with LPS or RPMI. IL-6 and TNF-alpha production measured to test whether *C. burnetii* can induce the trained-immunity phenotype in vitro.

**Statistics:** Mann-Whitney nonparametric U-test for group comparisons; P < 0.05 considered significant.

**Funding:** Q-support Foundation (UMCN-160708-00). No conflicts of interest declared.

No public transcriptome data accession (GEO or equivalent) is reported in the paper. The RNA-seq dataset does not appear to have been deposited in a public repository at time of publication.

## Key Findings

**1. Durable monocyte transcriptional reprogramming after acute Q fever.**
At baseline (median 27 days post-illness), PCA of the top 500 varying genes clearly separated acute Q fever patients from healthy controls. At 6-month follow-up, separation was reduced but a subset of patients retained distinct transcriptional profiles.

**2. Pathway enrichment pattern.**
At baseline: downregulation of energy metabolism pathways and general epigenetic/transcriptional processes; upregulation of apoptosis and necrosis pathways. Histone H3K9me2 repressive marks were noted at promoter regions of IL-6 and IL-8 genes at baseline. At 6-month follow-up: differences diminished; residual signal was primarily upregulation of energy metabolism pathways.

**3. Persistent circulating cytokine elevation.**
At baseline: significantly elevated IL-10 (median 5.81 vs 2.77 pg/mL, P = 0.0019), IL-1β (13.05 vs 0.69 pg/mL, P = 0.0067), IL-1Ra (2132 vs 512.4 pg/mL, P = 0.0008), and IL-6 (14.17 vs 1.81 pg/mL, P = 0.0003). At 6-month follow-up: IL-10 (P = 0.0136) and IL-1Ra (P = 0.0017) remained significantly elevated; IL-1β and IL-6 normalized (P = 0.11 and P = 0.28, respectively).

**4. *C. burnetii* induces trained-immunity phenotype in vitro.**
Naïve monocytes pre-exposed to *C. burnetii* (1×10^7/mL) for 24 h, then rested 6 days, produced significantly more IL-6 (P = 0.02) and TNF-alpha (P = 0.03) upon LPS restimulation than RPMI controls. This experiment, performed in monocytes from 3 healthy donors in 2 independent experiments, directly demonstrates that *C. burnetii* can imprint a trained-immunity functional phenotype.

**5. Transient suppression of mitochondrial-derived peptide genes.**
*MT-RNR1* (MOTS-c) and *MT-RNR2* (humanin) were significantly less expressed at baseline (−0.7 log2-fold, P = 0.0111 and −0.9 log2-fold, P = 0.0002, respectively). This suppression resolved by 6-month follow-up. A non-significant trend toward lower expression in the 2 QFS patients relative to the 9 recovered patients was noted at both time points — underpowered but consistent with a prior QFS study.

**6. Limited QFS stratification.**
Of the 11 patients, 2 developed QFS at 6 months. Differential expression between QFS (n = 2) and recovered (n = 9) patients was explored using heatmaps (cut-off P < 0.005) but the sample is far too small for reliable statistical inference. No PCA separation of QFS vs. recovered was observed, consistent with a prior study of QFS patients vs. healthy controls (cited as ref 16).

## Relevance

This paper is relevant to PAIS in two ways: (a) it demonstrates that *Coxiella burnetii*, the causative agent of post-Q-fever fatigue, durably reprograms the myeloid transcriptome and cytokine landscape of recovering patients, extending the trained-immunity / epigenetic reprogramming hypothesis beyond BCG vaccination into natural human infection; (b) it connects to the cross-pathogen convergence question by showing that the persistent myeloid activation seen in post-acute Q fever resembles signals seen in other post-viral fatigue contexts.

Importantly, this paper is NOT a study of QFS patients vs. recovered controls. The entire cohort had confirmed acute Q fever and was followed longitudinally. QFS-specific inferences are severely constrained by n = 2 QFS cases. The trained-immunity finding applies to the post-acute Q fever period broadly and does not resolve whether this reprogramming is causal, protective, or incidental in the development of QFS.

Relevant project questions and discussions:
- question:0001-shared-molecular-signature-across-triggers — the myeloid transcriptional reprogramming pattern (energy metabolism, epigenetic silencing, cytokine dysregulation) may contribute to a shared post-infectious immune signature across trigger pathogens.
- discussion:0002-cross-pathogen-pais-signature-convergence — provides direct molecular evidence for convergent myeloid reprogramming after a non-viral PAIS-associated pathogen.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Infection-induced trained immunity | Persistent immune activation / epigenetic reprogramming | Core candidate mechanism for myeloid dysfunction in PAIS |
| Long-lasting monocyte transcriptional changes | Immune dysregulation after index infection | Mechanistic plausibility, not QFS-specific |
| Downregulated energy metabolism pathways | Metabolic / mitochondrial dysfunction | Transient at baseline; may persist in QFS subgroup |
| Elevated IL-10 and IL-1Ra at 6 months | Anti-inflammatory cytokine persistence | Possible regulatory counter-response to persistent activation |
| H3K9me2 at IL-6/IL-8 promoters | Epigenetic silencing of pro-inflammatory genes | Paradoxical: silencing may coexist with elevated circulating cytokines |
| MT-RNR1 / MT-RNR2 suppression (acute phase) | Metabolic-peptide axis / mitochondrial function | Transient; QFS trend nonsignificant but directionally consistent |
| *C. burnetii* trained-immunity priming in vitro | Pathogen-specific trained-immunity induction | Mechanistic demonstration that the bacterium itself can reprogram monocytes |

## Limitations

1. **Very small sample:** 11 patients, 15 controls. The QFS stratification (n = 2 vs n = 9) is severely underpowered and the authors explicitly acknowledge this. All QFS-related findings should be treated as preliminary signals only.

2. **No QFS stratification for transcriptome primary analysis:** The main transcriptome results describe the unselected post-acute Q fever cohort vs. healthy controls, not QFS vs. non-QFS. The paper cannot directly address whether the observed monocyte reprogramming predicts or characterizes QFS.

3. **Monocyte purity not confirmed:** The authors note that "due to logistical challenges, monocyte purity was not checked prior to transcriptome analysis." Percoll isolation yields an enriched but not pure monocyte fraction; transcriptional signals from contaminating cells (NK cells, B cells, T cells) could confound differential expression findings.

4. **Short follow-up window:** The second timepoint is 6 months post-infection. Whether transcriptional differences persist further (1–2 years), as in established QFS, is not captured.

5. **In vitro trained-immunity experiment is small:** n = 3 donors in 2 independent experiments; demonstrates feasibility and direction rather than quantitative precision.

6. **No epigenomic profiling of patient samples:** The H3K9me2 reference is cited from earlier in vitro work. Actual chromatin accessibility (ATAC-seq) or histone-modification profiling was not performed on the patient samples, so the epigenetic mechanism is inferred, not measured.

7. **Australian cohort, occupational/geographic exposure:** Patients were primarily male (82%), median age 46, recruited through a reference laboratory in Victoria/New South Wales. Generalizability to other Q fever populations or outbreaks may be limited.

8. **Case definition qualification:** QFS was assessed using the Dutch RIVM guideline minus the full somatic/psychiatric co-morbidity workup, which may affect case ascertainment accuracy.

9. **No adjustment for doxycycline treatment:** Most acute Q fever patients receive doxycycline, which has anti-inflammatory properties. The effect of antibiotic treatment on monocyte transcriptomes is not addressed.

## Model / Tool Availability

No model, software tool, or public dataset was released with this paper. The RNA-seq data do not appear to have been deposited in GEO or a comparable repository. Bioinformatic tools used (Bowtie alignment to Ensembl v68, MMSEQ quantification, DESeq2 differential expression, ClueGO/Cytoscape pathway enrichment) are all publicly available standard packages.

## Follow-up

- **Companion paper to read:** Ref 16 (cited as prior QFS monocyte study from this group, showing reduced *MT-RNR1*/*MT-RNR2* expression in established QFS patients and lack of PCA separation vs. healthy controls) — this provides context for interpreting the acute-phase findings.
- **Longitudinal QFS-stratified study:** The most important follow-up would be a larger cohort study comparing monocyte transcriptomes and epigenomes in QFS patients vs. fully recovered post-Q-fever individuals at 1 and 2+ years.
- **Epigenomic profiling:** ATAC-seq or ChIP-seq on patient monocytes or bone marrow progenitors to test whether H3K9me2 at cytokine gene promoters is actually established in vivo.
- **Cross-PAIS comparison:** Do the downregulated energy metabolism and epigenetic pathways in post-Q-fever monocytes overlap with signatures reported in post-COVID or ME/CFS monocyte studies? This would directly address question:0001.
- **MOTS-c and humanin biology:** If *MT-RNR1* and *MT-RNR2* suppression during acute Q fever recovers in most patients but persists in QFS patients, these mitochondrial-derived peptides could be candidate biomarkers or therapeutic targets worth pursuing in a powered study.
