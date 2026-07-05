---
kind: search
title: 'Literature search: post-dengue / QFS / post-SARS omics gap confirmation (t033)'
status: active
created: '2026-06-20'
updated: '2026-06-20'
id: search:0004-post-dengue-qfs-postsars-omics-gap
related:
- task:t033
- question:0001-shared-molecular-signature-across-triggers
- discussion:0002-cross-pathogen-pais-signature-convergence
- hypothesis:0001-shared-dysregulated-attractor
- topic:shared-failure-mode-across-pais
---

# Search: post-dengue / QFS / post-SARS omics gap confirmation (t033)

## Search Focus

Targeted, **gap-confirming** hunt for molecular / omics studies (transcriptomic,
proteomic, metabolomic, epigenetic, cytokine / immune-cell profiling) in the three
PAIS triggers the 2026-06-20 cross-pathogen sweep
(`doc/searches/2026-06-20-cross-pathogen-pais-signatures.md`) flagged as **structural
data gaps**: **post-dengue fatigue**, **Q-fever fatigue syndrome (QFS)**, and
**post-SARS (SARS-CoV-1, 2003) syndrome**. The question this run answers is binary and
decision-relevant for `question:0001` / `hypothesis:0001`: *is the apparent emptiness of
these cells a true literature gap, or a miss of the broad relevance-ranked sweep?* This
is **not** a re-run of the broad cross-pathogen discovery — it is a deep, boolean,
per-trigger audit (the prior search's follow-up task #2).

## Query Set

Discovery used OpenAlex relevance search (broad) plus PubMed E-utilities boolean
(precise) — PubMed carried the load because OpenAlex relevance-ranking washed the thin
triggers into generic fatigue/COVID reviews (itself weak corroboration of the gap).

1. **OpenAlex broad (post-dengue):** `post-dengue chronic fatigue immune transcriptomic proteomic metabolomic cytokine sequelae` — 11 works; **0 post-dengue omics** (top hits = generic fatigue review, perinatal lung disease).
2. **OpenAlex broad (QFS):** `Q-fever fatigue syndrome Coxiella cytokine metabolic transcriptomic proteomic immune biomarker` — 10 works; 0 QFS-specific in the relevance head (washed into post-COVID/ME-CFS).
3. **OpenAlex broad (post-SARS):** `post-SARS survivors chronic fatigue metabolomic proteomic sequelae` — 119 works; relevance head entirely SARS-CoV-2/long-COVID (OpenAlex conflates "SARS" with SARS-CoV-2).
4. **PubMed boolean (post-dengue):** `(post-dengue OR "post dengue" OR (dengue AND "chronic fatigue")) AND (transcriptom* OR proteom* OR metabolom* OR cytokine* OR "gene expression" OR "immune profil*" OR autoantibod*)` — **5 hits, all vector-biology or persistent-skin-cell-infection models; 0 human post-acute fatigue omics**. A broader convalescent variant (11 hits) surfaced only post-dengue autoimmune **case reports** (transverse myelitis, necrotizing myopathy) + 1 cross-pathogen antibody review.
5. **PubMed boolean (QFS):** `("Q fever fatigue syndrome" OR "post-Q-fever fatigue" OR QFS) AND (transcriptom* OR proteom* OR metabolom* OR cytokine* OR "gene expression" OR "immune profil*" OR epigenetic* OR "whole blood")` — 23 hits (heavily polluted by "QFS" = a cotton-fiber QTL acronym), but **5 genuine QFS molecular studies** isolated after esummary triage, all from the Nijmegen/Radboud group.
6. **PubMed boolean (post-SARS, SARS-CoV-2 excluded):** `(... "severe acute respiratory syndrome" ...) AND (recovered OR survivors OR follow-up OR sequelae OR "chronic fatigue") AND (metabolom* OR lipidom* OR proteom* OR transcriptom* OR cytokine) NOT (SARS-CoV-2 OR COVID-19)` — 56 hits, almost all 2003-era acute SARS-CoV-1 virology; **exactly 1 survivor omics study** (Wu2017, 12-yr lipid metabolome).
7. **PubMed author audit:** `Raijmakers R[Author] AND (Q fever OR QFS OR fatigue)` — 18 hits; used to ensure the QFS omics cluster (one group) was captured exhaustively.

## Sources and Run Metadata

- **PubMed E-utilities** (esearch + esummary via WebFetch): primary, 6 boolean queries + 1 author audit. All ranked items carry a verified PMID + DOI.
- **OpenAlex** `works` (relevance, broad): 3 queries; low yield on thin triggers (documented above) — corroborates rather than discovers.
- Bash/`curl` network was sandbox-denied this session; queries ran through `WebFetch`
  against the same E-utilities/OpenAlex endpoints.
- Date window: unrestricted (the decisive items span 2011–2025; post-SARS evidence is
  necessarily 2017-era 12-yr-follow-up of a 2003 cohort).

## Ranked Results

Ranking weights: fills a named gap cell (post-dengue / QFS / post-SARS) > head-to-head /
cross-trigger design > molecular maturity (multi-omics > single cytokine) > recency. Items
already in the corpus (Galbraith2011, Raijmakers2021, Melenotte2019, Conde2026) are excluded.

| Rank | Citation (short) | Year | Source IDs | Trigger / design | Tier | Why it matters |
|---|---|---|---|---|---|---|
| 1 | Raijmakers et al., *EBioMedicine* — Immunological associations in post-infective fatigue syndromes incl. Long COVID (systematic review + meta-analysis) | 2025 | DOI 10.1016/j.ebiom.2025.105970 · PMID 41151241 | **cross-trigger meta-analysis** | **Core now** | The most current cross-PAIS *immunological* synthesis spanning QFS / Q-fever, EBV, Lyme, Long COVID. Meta-analytic CLAIM-level convergence evidence; directly updates `question:0001` provenance audit and the QFS row of the signature matrix. |
| 2 | Wu et al., *Sci Rep* — Altered lipid metabolism in recovered SARS patients twelve years after infection | 2017 | DOI 10.1038/s41598-017-09536-z · PMID 28831119 | post-SARS-CoV-1, single-trigger metabolomic | **Core now** | The **only** molecular-omics study of 2003-SARS survivors found. Fills the previously-empty **post-SARS** cell (lipidomic/metabolic sequelae, 12-yr). Phenotype = metabolic dysregulation, not fatigue-specified — caveat. |
| 3 | Raijmakers et al., *J Transl Med* — Mitochondrial-derived peptides humanin & MOTS-c in QFS **and** CFS | 2019 | DOI 10.1186/s12967-019-1906-3 · PMID 31088495 | **QFS ↔ CFS head-to-head**, metabolic/mitochondrial | **Core now** | A genuine within-study QFS–CFS comparison at the mitochondrial-peptide level — bridges the QFS gap to the bioenergetic axis (`question:0011`). Rare head-to-head bacterial-trigger vs idiopathic-CFS molecular datapoint. |
| 4 | Raijmakers et al., *J Infect* — Cytokine profiles in patients with Q-fever fatigue syndrome | 2019 | DOI 10.1016/j.jinf.2019.01.006 · PMID 30684502 | QFS single-trigger, cytokine | Relevant next | Dedicated QFS cytokine-omics; the substantive analyte panel behind the QFS immune cell. |
| 5 | Keijmel et al., *J Infect* — Altered interferon-γ response in patients with QFS | 2016 | DOI 10.1016/j.jinf.2016.01.004 · PMID 26820634 | QFS single-trigger, immune | Relevant next | Earliest QFS-specific immune-functional signal (IFN-γ); anchors the QFS IFN axis alongside Galbraith2011. |
| 6 | Raijmakers et al., *Eur J Clin Microbiol Infect Dis* — IFN-γ & CXCL10 responses related to complaints in QFS | 2018 | DOI 10.1007/s10096-018-3265-z · PMID 29804281 | QFS single-trigger, cytokine | Relevant next | Links the QFS IFN-γ/CXCL10 axis to *symptom burden* — a symptom-correlated molecular readout, uncommon in this corner. |
| 7 | Raijmakers et al., *Open Forum Infect Dis* — Long-lasting transcriptional changes in circulating monocytes of acute Q-fever patients | 2019 | DOI 10.1093/ofid/ofz296 · PMID 31363773 | acute-Q-fever cohort followed long-term, transcriptomic | Relevant next | Monocyte trained-immunity / epigenetic-reprogramming transcriptome — bears on persistence (`hypothesis:0002`) but phenotype is acute-cohort-followed, not QFS-fatigue-stratified. |
| 8 | Sun et al., *Int J Mol Sci* — Virus-induced pathogenic antibodies: lessons from Long COVID **and** dengue hemorrhagic fever | 2025 | DOI 10.3390/ijms26051898 · PMID 40076527 | review / cross-pathogen CLAIM | Peripheral monitor | Only item linking **dengue** to a shared PAIS axis (autoantibodies) — but a review, and dengue arm = DHF immunopathology, *not* post-dengue fatigue omics. Tracks the convergence CLAIM, not evidence. |

## Cross-Pathogen Signature Matrix — updates to the three gap columns

Replaces the post-dengue / QFS / post-SARS cells of the 2026-06-20 matrix. Bold = genuine
head-to-head / within-study design; plain = assembled single-trigger.

| Axis \ Trigger | Post-dengue | QFS (Coxiella) | Post-SARS (2003) |
|---|---|---|---|
| **Cytokine / IFN** | no-data | supported — IFN-γ/CXCL10 + cytokine profiles (Keijmel2016, Raijmakers2018, Raijmakers2019b); shared IFN-class transcripts in **Galbraith2011** | no-data |
| **Transcriptomic** | no-data | mixed — monocyte trained-immunity transcriptome in acute-Q-fever cohort (Raijmakers2019c); **Galbraith2011** (3-trigger, no consistent shared genes) | no-data |
| **Metabolic / mitochondrial** | no-data | supported — **mitochondrial-peptide humanin/MOTS-c, QFS↔CFS head-to-head (Raijmakers2019)** | **supported — 12-yr plasma lipid-metabolome dysregulation (Wu2017)** |
| **Neuroinflammation** | no-data | **absent — no TSPO signal (Raijmakers2021 head-to-head)** | no-data |
| **Autoantibodies** | claim only — DHF↔LC pathogenic-antibody review (Sun2025), no post-dengue-fatigue data | no-data | no-data |
| **Proteomic (untargeted)** | no-data | no-data | no-data |
| **Cross-trigger immune synthesis** | — | **Raijmakers2025 meta-analysis spans QFS + LC + other PIFS** | — |

## Coverage Notes and Gaps

**Verdict: the post-dengue and post-SARS molecular gaps are REAL; the QFS gap is partly
closed.** Specifically:

- **Post-dengue fatigue omics — confirmed structural gap (true empty).** Across OpenAlex +
  three PubMed boolean variants, **zero** human studies report transcriptomic / proteomic /
  metabolomic / immune-profiling data in a *post-acute / chronic-fatigue* dengue phenotype.
  What exists is (a) acute-dengue severity omics, (b) persistent-infection *cell-culture*
  models (Wei2018/2020, skin fibroblasts/dermal papilla), (c) post-dengue **autoimmune case
  reports** (myelitis, necrotizing myopathy), and (d) one cross-pathogen antibody **review**
  (Sun2025). This is a genuine evidence vacuum, not a search miss — it should be recorded as a
  structural limit on `hypothesis:0001` testability, not papered over.
- **Post-SARS (SARS-CoV-1) omics — near-empty, single datapoint.** Exactly one survivor
  molecular study exists (Wu2017, lipid metabolome at 12 yr). No transcriptomic / proteomic /
  immune survivor-fatigue omics. The post-SARS cell moves from `no-data` to a **single
  metabolic-sequelae datapoint with a phenotype caveat** (metabolic, not fatigue-defined).
- **QFS — moderate, single-group, immune+metabolic.** Materially better than the prior sweep
  implied: a coherent Nijmegen/Radboud cluster covers **cytokine/IFN-γ** (Keijmel2016,
  Raijmakers2018, Raijmakers2019b), **mitochondrial-peptide metabolism with a QFS↔CFS
  head-to-head** (Raijmakers2019), and **monocyte transcriptome** (Raijmakers2019c), now
  topped by a **2025 cross-PIFS immunological meta-analysis** (Raijmakers2025). Caveats:
  near-total **single-group provenance**, no untargeted proteomics/metabolomics, and the
  transcriptome study follows an *acute* Q-fever cohort rather than stratifying QFS fatigue.

**Net effect on `question:0001`:** the decisive ≥3-trigger harmonized multi-omics test still
does not exist, and now two of the project's own named triggers (post-dengue, post-SARS) are
confirmed to have **essentially no usable molecular substrate** — so the cross-pathogen claim
remains *structurally untestable* for them. QFS is the one thin trigger with a real (if
single-group) molecular handle, and Raijmakers2025 is the closest thing to a cross-PIFS
immunological synthesis to mine next.

## Recommended Next Actions

1. **Read Raijmakers2025 (EBioMedicine meta-analysis) in full** — extract which immune
   analytes it reports as *shared across* QFS / Q-fever / EBV / Lyme / Long COVID vs
   trigger-specific, and feed the head-to-head-vs-assembled provenance overlay for
   `question:0001` / `discussion:0002`.
2. **Record post-dengue and post-SARS as documented structural evidence gaps** in
   `discussion:0002` and the `hypothesis:0001` falsifiability/limitations — "absence of
   evidence" here is itself a finding that bounds the shared-signature claim.
3. **Mine the QFS metabolic head-to-head (Raijmakers2019, humanin/MOTS-c)** against the
   bioenergetic thread (`question:0011`, `hypothesis:0006`) — a bacterial-trigger
   mitochondrial datapoint is a useful out-of-COVID test of the mito-PEM axis.
4. **Do not over-weight Sun2025 / convergence reviews** — the only dengue "link" is a
   review-level autoantibody CLAIM; per `discussion:0003`'s operational rule, hold it at
   claim level until post-dengue primary data exist.
