---
id: paper:Saeed2014
kind: paper
title: "Epigenetic programming of monocyte-to-macrophage differentiation and trained innate immunity"
status: active
paper_kind: ""
ontology_terms:
- epigenetic reprogramming
- trained immunity
- innate immune memory
- H3K4me3
- H3K4me1
- H3K27ac
- ChIP-seq
- monocyte-to-macrophage differentiation
- beta-glucan
- endotoxin tolerance
- LPS tolerance
- enhancer landscape
- cAMP signaling
- metabolic reprogramming
- inflammasome
- NF-kB
source_refs:
- cite:Saeed2014
related:
- topic:innate-immune-memory-trained-immunity-in-pais
- question:0024-nlrp3-inflammasome-and-gasdermin-d-pyroptosis-as-a-self-amplifying-il-1
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0003-immune-exhaustion-feedback
created: "2026-07-07"
updated: "2026-07-07"
---

# Epigenetic programming of monocyte-to-macrophage differentiation and trained innate immunity

<!--
- **Authors:** Sadia Saeed, Jessica Quintin, Hindrik H. D. Kerstens, Nagesha A. Rao, Ali Aghajanirefah, Filomena Matarese, Shih-Chin Cheng, Jacqueline Ratter, Kim Berentsen, Martijn A. van der Ent, Nilofar Sharifi, Eva M. Janssen-Megens, Menno Ter Huurne, Amit Mandoli, Tom van Schaik, Aylwin Ng, Frances Burden, Kate Downes, Mattia Frontini, Vinod Kumar, Evangelos J. Giamarellos-Bourboulis, Willem H. Ouwehand, Jos W. M. van der Meer, Leo A. B. Joosten, Cisca Wijmenga, Joost H. A. Martens, Ramnik J. Xavier, Colin Logie, Mihai G. Netea, Hendrik G. Stunnenberg (corresponding)
- **Year:** 2014
- **Journal:** Science, Vol. 345, Issue 6204, p. 1251086
- **DOI:** https://doi.org/10.1126/science.1251086
- **PMID:** 25258085
- **PMCID:** PMC4242194
- **BibTeX key:** Saeed2014
- **Source:** web (PMC full text via pmc.ncbi.nlm.nih.gov, read 2026-07-07)
-->

## Key Contribution

The foundational genome-wide epigenomic map of human monocyte-to-macrophage differentiation and β-glucan-induced trained immunity. Saeed et al. profiled four primary cell states — monocytes (Mo), naive macrophages (Mf), LPS-tolerized macrophages (LPS-Mf), and β-glucan-trained macrophages (BG-Mf) — using ChIP-seq for H3K4me3 (active promoters), H3K4me1 (distal/enhancer regions), and H3K27ac (active regulatory elements), combined with DNase I hypersensitive sites and RNA-seq. The central finding is that β-glucan training establishes a broad, training-exclusive epigenetic signature — 3,069 distal regulatory elements newly marked by H3K27ac in BG-Mf vs. only ~500 in LPS-Mf — revealing a complex training-specific network of enhancers and promoters. Transcription factor motif analysis links this training-specific enhancer landscape primarily to **cAMP signaling (bZIP/ATF/CREB family)** and metabolic reprogramming rather than to classical NF-κB-driven inflammatory programs. The paper serves as a genome-wide resource for human monocyte/macrophage epigenomics; it does not present a clinical or post-infectious study.

**PAIS relevance disclaimer.** This is an in-vitro and ex-vivo study of canonical trained immunity using β-glucan as training stimulus in primary human monocytes from healthy donors. The link to post-acute infection syndromes is entirely by mechanistic analogy: if acute infection can train monocytes/HSPCs by similar epigenetic mechanisms, this map characterizes the epigenomic landscape those trained cells inhabit. No PAIS-specific evidence is present in this paper.

## Methods

**Cell types and donors.** Primary CD14+ monocytes isolated from peripheral blood of 3–6 healthy human donors (number varied by experiment). Differentiated in vitro into four states: monocytes (Mo, day 0), naive macrophages (Mf, day 6), LPS-tolerized macrophages (LPS-Mf, LPS stimulation on day 0 followed by 6-day culture), and β-glucan-trained macrophages (BG-Mf, 24h β-glucan priming on day 0, washout, 5-day culture in serum-enriched medium).

**Epigenomic assays.** Genome-wide ChIP-seq for three histone marks:
- **H3K4me3** — marks active gene promoters; 17% of peaks are dynamic across conditions.
- **H3K4me1** — marks distal regulatory elements (poised/active enhancers); 10% of peaks are dynamic.
- **H3K27ac** — marks active regulatory elements (enhancers + promoters); 19% of peaks are dynamic.

Additionally, DNase I hypersensitive site (DHS) mapping to identify open chromatin; paired RNA-seq for transcriptome profiling. Epigenomic clusters were defined as ACp (acetylated promoters) and ACe (acetylated distal/enhancer elements), numbered by cell-state specificity (e.g., ACe1 = β-glucan training-exclusive).

**Expression modules.** Polytomous analysis identified six gene co-expression modules (M1–M6) with differential expression patterns across cell states, linked to epigenomic clusters via gene-locus overlap.

**Transcription factor motif analysis.** TF motifs enriched in DHS sites at cell-type-specific epigenetic loci, identifying differentiation-stage- and treatment-specific TF repertoires.

**Functional validation.** cAMP pathway importance for trained immunity confirmed with adenylate cyclase inhibitors and PKA inhibitors (attenuated training-induced cytokine production); in vivo mouse *Candida albicans* survival experiments with cAMP pathway manipulation (Figure 5).

## Key Findings

### Scope of epigenomic dynamism across differentiation and training

Dynamic epigenomic marks across all four cell states span 17% of H3K4me3 peaks, 10% of H3K4me1 blocks, and 19% of H3K27ac peaks. At promoters specifically, H3K27 acetylation decreases at 1,240 promoters and increases at 1,307 promoters across conditions.

### β-glucan training installs a quantitatively larger and qualitatively distinct enhancer signature than LPS tolerance

The training-specific ACe1 cluster comprises **3,069 distal regulatory elements** that gain H3K27ac exclusively in BG-Mf — the most extensive treatment-specific response observed. By contrast, LPS-tolerized cells gain H3K27ac at only ~500 distal elements. In total, 40.3% of all dynamic distal elements and 17% of all dynamic promoters gain H3K27ac exclusively in β-glucan-trained cells. This marks training as a qualitatively different epigenomic state from both naive differentiation and tolerance.

### H3K4me1 as epigenetic memory mark (latent enhancers)

Distal elements that lose H3K27ac activation across conditions retain their H3K4me1 mark, supporting a "latent enhancer" model in which H3K4me1 provides an epigenetic memory function preserving enhancer accessibility across macrophage states for potential reactivation. H3K4me3 shows less condition-specific dynamism than H3K27ac ("largely constant at promoters that display dynamic H3K27 acetylation"), making H3K27ac the more informative mark for training-specific regulatory changes.

### Training-specific enhancers are enriched in metabolic and cAMP pathway loci, not primarily inflammatory loci

Gene modules enriched in the training-specific ACe1 enhancers are primarily metabolic: Module M2 and M4 genes include **glycolysis enzyme pyruvate dehydrogenase (DLAT)** and TCA cycle enzyme malate dehydrogenase (MDH1), consistent with the Warburg-like aerobic glycolysis shift established by Cheng2014. The dominant TF motifs in ACe1 are **bZIP family members (ATF1, ATF7, CREB3, JDP2)** and the glucocorticoid receptor (NR3C1), linking training-specific enhancer activation to cAMP-responsive rather than NF-κB-driven regulation. By contrast, LPS-tolerized ACe5 elements are enriched for NF-κB and REL motifs — the inverse signature. **The paper does not report H3K4me3 or H3K27ac changes specifically at TNF, IL6, IL1B, CXCL8, or NLRP3 gene loci as highlighted training-specific findings; no locus-level ChIP-seq tracks at inflammatory cytokine or inflammasome genes are displayed.**

### Transcription factor repertoire switches during differentiation

Figure 4 documents coordinated TF switches during monocyte-to-macrophage differentiation, including a dramatic increase in **LXRα** (NR1H3) in trained cells and reduction of PPARG (NR1C3) in LPS-Mf but maintenance in BG-Mf — linking trained macrophage identity to nuclear receptor programs distinct from tolerized cells.

### Inflammasome pathway: differentiation-level modulation, not training-specific epigenetic priming

Figure 1H ("Modulation of the inflammasome and NF-κB pathways during monocyte-to-macrophage differentiation") displays gene expression changes across cell states. Key finding: during naive macrophage differentiation, NF-κB subunits (REL, RELA, RELB, NFκB1, NFκB2) are all downregulated >2-fold. **This is a differentiation-level analysis, not a comparison of trained vs. naive macrophages at inflammatory loci.** Figure 1I (Western blot) shows that in vitro-differentiated macrophages, unlike monocytes, show no caspase-1 activation and lack the capacity to secrete active IL-1β upon LPS stimulation; pro-IL-1β (proIL-1β) levels are demonstrated. The IL-1β/IL1B analysis is protein-level (Western blot) and reflects the differentiation state rather than epigenomic marks at the IL1B locus. **No dedicated H3K4me3/H3K27ac ChIP-seq tracks at the IL1B gene locus are presented.**

### cAMP signaling is functionally required for trained immunity induction

Inhibitors of adenylate cyclase and PKA significantly impair training-induced cytokine production in vitro (Figure 5), and cAMP pathway manipulation affects mouse survival after *Candida albicans* challenge — establishing cAMP as mechanistically required for β-glucan-trained immunity and linking the bZIP/ATF/CREB motif enrichment in ACe1 enhancers to a functional pathway.

### Precision statement: NLRP3 and IL1B locus coverage

| Claim | Accurate characterization |
|---|---|
| Paper provides genome-wide H3K4me3/H3K27ac map covering all gene loci | **Yes** — the map covers all annotated loci including NLRP3 and IL1B within the genome-wide dataset |
| Training installs H3K27ac at inflammatory promoters/enhancers broadly | **Indirectly** — the 3,069 ACe1 elements are genome-wide and likely include some inflammatory genes, but the paper's own analysis spotlights metabolic/cAMP enrichments, not inflammatory loci |
| Inflammasome pathway analyzed (Figure 1H/1I) | **Yes, but at the expression/protein level during differentiation**, not as training-specific epigenomic tracks |
| IL1B locus shown with a dedicated ChIP-seq track | **No** — proIL-1β shown by Western blot (Figure 1I); no ChIP-seq locus view at IL1B |
| NLRP3 locus shown with a dedicated ChIP-seq track | **No** — NLRP3 appears only as part of pathway-level module analysis; no locus-level ChIP-seq visualization |
| Only locus-level tracks displayed | CELSR1 and CD300E (Figure 1E) as representative differentiation examples; no inflammatory gene tracks shown |

## Relevance

**`topic:innate-immune-memory-trained-immunity-in-pais` — foundational epigenomic resource.** This paper provides the genome-wide histone-mark map that established trained immunity as an epigenomically defined state. The topic cites it (alongside Arts2016 and Netea2016) as anchoring the "H3K4me3/H3K27ac at inflammatory loci" claim. The precision caveat needed for PAIS-specific use: this paper's training-specific enhancer signature (ACe1) is enriched in metabolic and cAMP pathway loci; the claim that "training installs H3K4me3/H3K27ac specifically at NLRP3 or IL1B loci" is not directly demonstrated here and derives from the broader trained-immunity literature.

**`question:0024` (NLRP3 inflammasome/pyroptosis loop) — partial, with strong caveat.** The paper documents decreased inflammasome activity in differentiating macrophages (Figure 1H/1I) and provides the epigenomic landscape of trained monocytes. However, it does **not** demonstrate training-specific H3K4me3 or H3K27ac at the NLRP3 locus — this connection (primed NLRP3 via epigenetic marks in trained cells) is derived from the broader field and is not directly supported by a locus-level track in this paper. Cite as general epigenomic context for training, not as direct NLRP3-locus evidence.

**`hypothesis:0001` (shared dysregulated attractor) — indirect mechanistic context.** The trained-immunity frame positions this paper as part of the epigenetic-reprogramming-of-innate-immunity substrate that could maintain PAIS as an antigen-independent attractor. Connection is inferential.

**`hypothesis:0003` (immune exhaustion feedback) — epigenomic complement.** The tolerance-vs-training dichotomy demonstrated here (distinct epigenomic signatures) is mechanistically relevant to whether PAIS involves a training or tolerance state in myeloid cells — a distinction with opposite functional consequences (hyperreactivity vs. immunosuppression).

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| β-glucan-trained macrophages (BG-Mf) | Trained innate immunity / epigenetic reprogramming | Canonical training stimulus; PAIS-relevant by analogy, not by direct evidence |
| ACe1 cluster (3,069 training-specific H3K27ac distal elements) | Training-specific enhancer landscape | Enriched in metabolic/cAMP loci, not primarily inflammatory cytokine loci |
| LPS tolerance vs β-glucan training epigenomic divergence | Tolerance/training dual phenotype (h0003, Bomans2018) | Tolerance = fewer H3K27ac elements, NF-κB motif enriched; training = broader H3K27ac, bZIP/CREB motif enriched |
| H3K4me1 latent enhancers | Epigenetic memory substrate | H3K4me1 persists after H3K27ac loss — "poised" for reactivation |
| Inflammasome/IL-1β downregulation during differentiation (Figure 1H/1I) | Macrophage maturation phenotype | Differentiation-level change; not a training-specific epigenomic mark at IL1B or NLRP3 |
| cAMP/bZIP TF motif enrichment in trained enhancers | Immunometabolic reprogramming in training | Connects to glycolytic/mTOR switch (Cheng2014) at the regulatory-element level |

## Limitations

**1. In vitro and ex vivo system — no in vivo post-infectious validation.** The four cell states (Mo, Mf, LPS-Mf, BG-Mf) are differentiated in vitro from peripheral blood monocytes of healthy donors. Whether post-infectious epigenomic reprogramming in vivo generates similar H3K4me3/H3K27ac patterns to β-glucan-trained cells is not established by this paper.

**2. Training-specific epigenomic enrichments are metabolic, not primarily inflammatory.** The paper's analysis of training-specific ACe1 enhancers highlights metabolic (glycolysis, TCA cycle) and cAMP-responsive loci rather than classical inflammatory cytokine or inflammasome gene loci. The widely-cited "trained immunity installs activating marks at inflammatory promoters" claim is not specifically demonstrated at the IL1B, NLRP3, TNF, or IL6 loci in this paper; it extrapolates from the genome-wide resource and from other trained-immunity studies. This distinction matters for accurately citing Saeed2014 as an anchor for inflammasome-pathway epigenetic priming.

**3. Donor variability — small N per condition.** 3–6 healthy human donors per experiment; no demographic or genetic characterization of donors. Training-response heterogeneity across individuals is not analyzed.

**4. β-glucan as training stimulus — relevance to post-infectious PAIS.** β-glucan (a fungal cell-wall component) is the canonical experimental training stimulus but is not a natural post-infectious signal in most PAIS-defining infections (COVID-19, Borrelia, EBV, Coxiella). The epigenomic signature described here is β-glucan-specific; whether SARS-CoV-2 spike protein, Borrelia lipoproteins, or EBV viral antigens induce the same enhancer landscape is not established by this paper.

**5. No PAIS or post-infectious clinical data.** This is a basic mechanistic epigenomics study. It provides no evidence about whether trained immunity occurs in PAIS patients, contributes to symptoms, or differs by trigger.

**6. Inflammasome/NF-κB analysis is differentiation-level, not training-level.** The decreased inflammasome activity (Figure 1H/1I) describes naive macrophage differentiation, not a comparison between trained and naive macrophages. This is a frequent misread of the paper.

## Model / Tool Availability

**Data.** Genome-wide ChIP-seq (H3K4me3, H3K4me1, H3K27ac), DHS, and RNA-seq data deposited at NCBI GEO; accession number not confirmed from full text review. [UNVERIFIED — accession number should be retrieved from GEO directly if data reanalysis is planned.]

**No new software tools released.** Standard ChIP-seq pipelines; DHS-seq motif analysis.

## Follow-up

**Papers already in project or closely related:**

- `paper:Cheong2023` (Cell 2023) — the most direct PAIS-relevant extension: durable HSPC chromatin remodeling after severe COVID-19, with IL-6 as the imprinting signal; uses ATAC-seq rather than ChIP-seq but anchors the central-training model Saeed2014 provided epigenomic context for.
- Arts2016 (Cell Metabolism) — the metabolic-epigenetic bridge: glutaminolysis → fumarate → KDM5 demethylase inhibition → H3K4me3 at training loci; directly extends the Saeed2014 epigenomic map with a mechanistic explanation.
- Cheng2014 (Science) — mTOR/HIF-1α glycolytic reprogramming required for β-glucan training induction; connects to the metabolic loci enriched in Saeed2014's ACe1 enhancer cluster.
- Netea2016 — field review anchoring trained immunity as a distinct immunological memory class, citing Saeed2014 as the core epigenomic evidence.
- Mitroulis2018 (Cell) — β-glucan-induced HSPC training in bone marrow; the central (not just peripheral) training model that requires the Saeed2014 monocyte-level map as its downstream readout.

**Questions this paper bears on:**

1. **`question:0024` (NLRP3/inflammasome loop) — locus-specificity gap.** For the claim that "trained immunity epigenetically primes the NLRP3 locus," Saeed2014 provides context but not direct evidence. A genome-wide map that specifically demonstrates H3K4me3 gain at NLRP3 and IL1B loci in trained monocytes would be needed to directly ground this claim; later studies in the trained-immunity field may have done this (check Novakovic2016 in Immunity for BCG training data, or Foster2007 for tolerance-specific H3K4me3 at TNF).

2. **Differentiation vs. training epigenomics distinction.** The paper is the primary source for both the monocyte-to-macrophage differentiation map AND the β-glucan training map; these are distinct biological comparisons and should be cited separately when the claim is about one vs. the other.
