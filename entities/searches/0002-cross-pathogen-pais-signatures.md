---
kind: search
title: 'Literature search: cross-pathogen PAIS molecular signatures (t001)'
status: active
created: '2026-06-20'
updated: '2026-06-20'
id: search:0002-cross-pathogen-pais-signatures
related:
- task:t001
- hypothesis:0001-shared-dysregulated-attractor
- question:0001-shared-molecular-signature-across-triggers
- topic:shared-failure-mode-across-pais
- topic:mecfs-long-covid-convergence
---

# Search: cross-pathogen PAIS molecular signatures (t001)

## Search Focus

Assemble immune / proteomic / transcriptomic / metabolomic signatures **across multiple
post-infectious triggers** (long COVID, ME/CFS incl. post-EBV, PTLDS, post-dengue,
post-Q-fever, post-SARS / post-Ebola / post-chikungunya) to test whether they converge
on a **shared dysregulated state** (`hypothesis:0001-shared-dysregulated-attractor`,
`question:0001-shared-molecular-signature-across-triggers`) or remain **trigger-specific**.

The load-bearing deliverable is the **Cross-Pathogen Signature Matrix** (below): candidate
shared axes x triggers, each cell scored `supported / mixed / absent / no-data` with a
1-line evidence note + citekey. The decisive epistemic question is whether convergence is
demonstrated by **head-to-head** studies (>=2 triggers in one design) or merely **asserted
by assembling separate single-disease studies** -- the central risk for `hypothesis:0001`.

## Query Set

1. **Broad conceptual (OpenAlex):** `post-acute infection syndrome shared immune signature long COVID ME/CFS convergence` -- 111 works.
2. **Mechanism / cross-pathogen (OpenAlex):** `cross-pathogen post-infectious fatigue proteomic transcriptomic EBV dengue Q-fever Lyme signature` -- 3 works (too narrow; surfaced Trautmann2025).
3. **Methods / multi-omics (OpenAlex):** `multi-omics proteomic metabolomic comparison post-infectious syndrome long COVID ME/CFS shared biomarker` -- 50 works.
4. **Alternative / trigger-specific counter-evidence (OpenAlex):** `trigger-specific heterogeneity distinct mechanisms post-acute sequelae long COVID subphenotype not shared` -- 43 works.
5. **Shared-axis: autoantibody / complement / microclot (OpenAlex):** `GPCR autoantibodies functional dysautonomia long COVID ME/CFS post-infectious complement microclots shared` -- 12 works.
6. **Thin-trigger coverage (PubMed E-utilities):** PTLDS molecular signatures (25), arbovirus/QFS/Ebola post-infectious omics (25), QFS+post-infectious cross-comparison (162 / 25).

## Sources and Run Metadata

- **OpenAlex** `works` (broad discovery): 6 queries, primary source. Candidate counts above.
- **PubMed** E-utilities (esearch + esummary via Bash curl): 3 queries, used specifically to
  audit the thin triggers (PTLDS / dengue / QFS / Ebola / chikungunya) the conceptual queries miss.
- No WebSearch fallback was needed; all ranked items have a verified DOI or PMID.
- Date window: last ~15 years + seminal (the decisive head-to-head cross-trigger transcriptomic
  study, Galbraith2011 / Dubbo cohort, is 2011 and is included as seminal).

## Ranked Results

Ranking weights: relevance to `question:0001` (is it cross-trigger and molecular?) >
evidence strength (head-to-head > single-trigger > review) > recency > novelty/contradiction
value > reproducibility (cohort size, replication).

| Rank | Citation (short) | Year | Source IDs | Comparison | Tier | Why it matters |
|---|---|---|---|---|---|---|
| 1 | Galbraith et al., *J Infect Dis* -- PBMC gene expression in postinfective fatigue across 3 triggers | 2011 | DOI 10.1093/infdis/jir612 - PMID 21964398 | **head-to-head** (EBV, RRV, Q-fever) | **Core now** | The single most decisive *existing* test: same design, 3 triggers, Dubbo cohort. Directly probes whether a shared transcriptomic signature exists. Seminal for `question:0001`. |
| 2 | de Sa et al., *Cell* -- causal link: autoantibodies -> LC neuro symptoms | 2026 | DOI 10.1016/j.cell.2026.04.042 - PMID 42208499 | single-trigger, **causal** (IgG transfer) | **Core now** | Raises the autoantibody axis from association to causation -- but only for SARS-CoV-2. A shared-axis CLAIM with single-trigger EVIDENCE. |
| 3 | Liu et al., *Brain Behav Immun Health* -- IgG from post-infectious & post-COVID ME/CFS disrupts cellular energetics | 2026 | DOI 10.1016/j.bbih.2026.101187 - PMID 41704659 | **cross-onset** (classic + post-COVID ME/CFS) | **Core now** | Functional convergence: IgG from two onset types both impair energetics -- links autoantibody + mitochondrial axes across triggers. |
| 4 | Patterson et al., *Sci Rep* -- ML differentiates long COVID from chronic Lyme by cytokine hubs | 2024 | DOI 10.1038/s41598-024-70929-y - PMID 39187577 | **head-to-head** (SARS-CoV-2, Borrelia) | **Core now** | Head-to-head, but the result is *separation* -- a trigger-specific counterpoint inside an overlapping cytokine space. Key contradiction. |
| 5 | Walitt et al., *Nat Commun* -- deep phenotyping of post-infectious ME/CFS | 2024 | DOI 10.1038/s41467-024-45107-3 | single-trigger deep multi-omics | **Core now** | The richest single-cohort molecular reference (NIH intramural) to align cross-trigger panels against. |
| 6 | Raijmakers et al., *Neurol Neuroimmunol Neuroinflamm* -- no neuroinflammation in QFS or ME/CFS (TSPO PET) | 2021 | DOI 10.1212/NXI.0000000000001113 | **head-to-head** (Q-fever, ME/CFS) | **Core now** | A shared *negative* finding across triggers; disciplines the neuroinflammation axis. |
| 7 | Girgis et al., *Front Immunol* -- aberrant T-cell phenotypes in PTLDS | 2025 | DOI 10.3389/fimmu.2025.1607619 - PMID 40703523 | single-trigger | **Core now** | Fills the PTLDS T-cell-exhaustion/activation cell; parallels ME/CFS (Iu2024) and LC. |
| 8 | Broderick et al., *J Transl Med* -- cytokine networks in post-mononucleosis CFS | 2012 | DOI 10.1186/1479-5876-10-191 | single-trigger longitudinal | **Core now** | Molecular anchor for the classic post-EBV ME/CFS arm. |
| 9 | Ramundo et al., *Sci Rep* -- post-chikungunya chronic-disease transcriptomics | 2025 | DOI 10.1038/s41598-025-86761-x - PMID 40000671 | single-trigger | **Core now** | Fills an arbovirus transcriptomic cell (phenotype = arthritis, not fatigue -- caveat). |
| 10 | Sanford et al., *medRxiv* -- metabolic basis of post-Ebola sequelae | 2026 | DOI 10.64898/2026.01.02.25343095 - PMID 41542679 | single-trigger | **Core now** | Rare post-Ebola metabolomic signature. PREPRINT -- low maturity. |
| 11 | Watton et al., *J Transl Med* -- unified mechanistic model of chronic post-infectious diseases | 2026 | DOI 10.1186/s12967-026-08319-3 - PMID 42174604 | synthesis/review | **Core now** | Recent convergence CLAIM, peer to Komaroff2023/2025, Trautmann2025. Track for over-claim. |
| 12 | Nilsson et al., *PLoS One* -- serum/CSF protein biomarkers in PTLDS (n=158) | 2022 | DOI 10.1371/journal.pone.0276407 - PMID 36327322 | single-trigger | Relevant next | PTLDS proteomic candidate panel. |
| 13 | Clarke et al., *Cell Rep Med* -- gene-set predictor for PTLDS | 2022 | DOI 10.1016/j.xcrm.2022.100816 - PMID 36384094 | single-trigger | Relevant next | PTLDS transcriptomic predictor; alignable to ME/CFS/LC. |
| 14 | Iu et al., *PNAS* -- CD8+ T-cell exhaustion transcriptional program in ME/CFS | 2024 | DOI 10.1073/pnas.2415119121 | single-trigger | Relevant next | ME/CFS anchor for the T-cell-exhaustion axis. |
| 15 | Apostolou et al., *Front Immunol* -- latent-virus reactivation fingerprint in post-COVID ME/CFS | 2022 | DOI 10.3389/fimmu.2022.949787 | head-to-head (SARS-CoV-2, ME/CFS) | Relevant next | Herpesvirus-reactivation axis across onset types. |
| 16 | Chang et al., *PLoS One* -- cytokine/T-cell responses in post-chikungunya arthritis | 2024 | DOI 10.1371/journal.pone.0302573 - PMID 38507338 | single-trigger | Relevant next | Arbovirus cytokine/T-cell (arthritis phenotype caveat). |
| 17 | Melenotte et al., *Med Mal Infect* -- post-bacterial (Q-fever) CFS is not latent infection | 2019 | DOI 10.1016/j.medmal.2019.01.006 | single-trigger | Peripheral monitor | Bears on antigen-persistence seed (hyp:0002) for QFS. |
| 18 | Nunes et al., *Cell Death Dis* -- virus-induced endothelial senescence in ME/CFS + LC | 2026 | DOI 10.1038/s41419-025-08162-2 | synthesis/review | Peripheral monitor | Endothelial/microclot convergence CLAIM (review-level). |
| 19 | Chowdhury et al., *Sci Rep* -- distinct plasma proteome 3mo post-COVID irrespective of LC | 2026 | DOI 10.1038/s41598-026-46180-y | single-trigger | Peripheral monitor | Counter-evidence: proteome shift not LC-specific -- cautions PAIS-specificity claims. |
| 20 | Arron et al., *Front Immunol* -- ME/CFS biology review | 2024 | DOI 10.3389/fimmu.2024.1386607 | review | Peripheral monitor | Background catalog of ME/CFS shared axes. |

(Discovery surfaced `~280` candidates across queries; the bulk are single-disease LC or ME/CFS
mechanism reviews already represented in the corpus. The records above are the load-bearing,
*cross-trigger-informative* items not already captured.)

## Cross-Pathogen Signature Matrix

Rows = candidate shared axes. Columns = triggers. Cell value =
`supported` / `mixed` / `absent` / `no-data`, with a 1-line evidence note + citekey.
**Bold** cell text marks a finding that comes from a genuine *head-to-head* design;
plain text marks a cell populated from a *separate single-trigger* study (assembled
convergence, not demonstrated convergence).

| Axis \ Trigger | Long COVID | ME/CFS (post-EBV/idiopathic) | PTLDS (Borrelia) | Post-dengue | QFS (Coxiella) |
|---|---|---|---|---|---|
| **T-cell exhaustion/activation** | supported -- CD8 exhaustion, T-cell dysregulation (Klein2023, Cruz2025) | supported -- CD8 exhaustion transcriptional program (Iu2024; Walitt2024) | supported -- aberrant T-cell phenotypes (Girgis2025) | no-data | no-data |
| **Cytokine pattern (IL-1/IL-6/TNF, IFN)** | supported -- inflammatory subset, IFN/NF-kB (Talla2023) | supported -- post-EBV cytokine networks (Broderick2012) | mixed -- **distinguishable cytokine hubs vs LC** (Patterson2024 head-to-head) | no-data | **mixed -- shared IFN-class transcripts across EBV/RRV/Q-fever postinfective fatigue (Galbraith2011)** |
| **IFN signature (transcriptomic)** | supported (Talla2023) | supported (Walitt2024) | mixed (Clarke2022 gene-set) | no-data | **mixed -- Galbraith2011 tests 3 triggers incl. Q-fever** |
| **Complement activation** | supported -- complement dysregulation (Cervia-Hasler2024, Cruz2025) | no-data | no-data | no-data | no-data |
| **EBV/herpesvirus reactivation** | supported (Klein2023; Apostolou2022) | supported -- EBV-driven onset arm (Hanson2023; Apostolou2022) | no-data | no-data | absent-by-design -- trigger is bacterial (Melenotte2019) |
| **Autoantibodies (incl. GPCR/functional)** | supported -- **causal IgG->neuro (deSa2026)**; functional AAbs | supported -- **IgG impairs energetics (Liu2026, incl. post-COVID ME/CFS)** | no-data (Q-fever has AAb reports but not PTLDS-specific) | no-data | no-data |
| **Microclots / thromboinflammation / endothelial** | supported (Nicolai2023; Kell/Nunes2026 review) | mixed -- endothelial-senescence hypothesis (Nunes2026, review) | no-data | no-data | no-data |
| **Tryptophan-kynurenine / serotonin** | supported -- serotonin depletion, kynurenine shift (corpus) | mixed (metabolomic shifts; Che2025) | no-data | no-data | no-data |
| **Mitochondrial / metabolic** | supported (Molnar2024 review) | supported -- innate-immune/metabolic (Che2025, Walitt2024); **IgG disrupts energetics (Liu2026)** | no-data | no-data | no-data |
| **Neuroinflammation** | mixed (imaging mixed) | **absent -- no TSPO signal (Raijmakers2021 head-to-head)** | no-data | no-data | **absent -- no TSPO signal (Raijmakers2021 head-to-head)** |
| **Metabolomic (untargeted)** | supported | supported (Walitt2024; Che2025) | no-data | no-data | no-data |
| **Inflammation/transcriptome (other infections)** | n/a | n/a | mixed (Clarke2022) | **no molecular omics found -- only fatigue/depression epidemiology (Conde2026)** | n/a |
| **Post-chikungunya (arbovirus add-on)** | -- | -- | -- | supported transcriptomic + cytokine (Ramundo2025, Chang2024) -- *arthritis phenotype, not fatigue* | -- |
| **Post-Ebola (add-on)** | -- | -- | -- | metabolomic signature (Sanford2026, preprint) | -- |

**Reading the matrix:** the upper-left block (Long COVID + ME/CFS) is densely `supported`
across nearly every axis -- but almost all of those cells are populated from *separate
single-trigger* studies, not head-to-head designs. The genuinely head-to-head cells are
few and concentrate in: (1) Galbraith2011 (transcriptomic IFN-class, EBV/RRV/Q-fever);
(2) Raijmakers2021 (neuroinflammation, shared *negative*); (3) Patterson2024 (cytokine,
which *separates* LC from chronic Lyme); (4) Liu2026 / Apostolou2022 (cross-onset within
the ME/CFS umbrella). PTLDS is now moderately covered; **post-dengue and QFS have no
direct molecular-omics cells** (dengue = epidemiology only; QFS = only inside Galbraith2011
and the negative Raijmakers2021). Post-SARS has no molecular signature data at all.

## Convergence: CLAIM vs EVIDENCE

- **CLAIMS of convergence** (review/synthesis level, not head-to-head data): Komaroff2023,
  Komaroff2025, Trautmann2025, Watton2026, Nunes2026. These assemble single-disease findings
  into a shared-mechanism narrative -- exactly the epistemic move `question:0001` flags as
  insufficient on its own.
- **EVIDENCE of convergence (head-to-head)**: Galbraith2011 (partial -- some shared transcripts
  across 3 triggers), Liu2026 / Apostolou2022 (cross-onset within ME/CFS), Raijmakers2021
  (shared *negative*). 
- **EVIDENCE of divergence (head-to-head)**: Patterson2024 (LC vs chronic Lyme separate by
  cytokine hubs), and within-COVID Cruz2025 / Chowdhury2026 (proteome shift not LC-specific).

The honest current state: **convergence is robust at the level of biological *domains*
(immune activation, T-cell exhaustion, metabolic/mitochondrial) but the molecular cells that
prove it are overwhelmingly assembled from separate single-trigger studies. The few real
head-to-head tests are split** -- one partial-shared (Galbraith2011), one shared-negative
(Raijmakers2021), and one that *separates* triggers (Patterson2024). No study runs harmonized
multi-omics across >=3 fatigue-phenotype triggers with full-recovery controls. The decisive
test for `hypothesis:0001` does not yet exist.

## Coverage Audit (by trigger)

| Trigger | Coverage | Gap note |
|---|---|---|
| Long COVID / PASC | Rich | Many axes; mostly single-trigger though. |
| ME/CFS (post-EBV/idiopathic) | Rich | Strong, incl. cross-onset (Liu2026, Apostolou2022). |
| PTLDS (Borrelia) | Moderate (was thin) | Now: T-cell (Girgis2025), proteomic (Nilsson2022), transcriptomic (Clarke2022), head-to-head vs LC (Patterson2024). |
| **Post-dengue** | **Thin / GAP** | Only fatigue/depression epidemiology (Conde2026). **No proteomic/transcriptomic/metabolomic omics found.** |
| **QFS (Coxiella)** | Thin-moderate / GAP | Inside Galbraith2011 (transcriptomic) and Raijmakers2021 (negative neuroimaging); Morroy2016 epidemiology. **No dedicated QFS multi-omics.** |
| **Post-SARS (2003)** | **Thin / GAP** | No molecular signature surfaced beyond historical/clinical reviews. |
| Post-Ebola | Thin-but-present | Sanford2026 metabolomic *preprint* only. |
| Post-chikungunya | Moderate | Ramundo2025, Chang2024 -- but **arthritis phenotype**, weak match to the fatigue-PAIS frame; relevance caveat. |

## Suggested Follow-up Tasks

1. **Acquire & read Galbraith2011 in full** -- it is the closest existing head-to-head
   cross-trigger transcriptomic test; extract whether shared vs trigger-specific genes
   dominate, and whether raw data (GEO) are reusable for `question:0001`.
2. **Targeted hunt for post-dengue and QFS molecular omics** (likely a true literature gap to
   record, not just a search miss) -- if confirmed empty, document as a structural evidence gap
   limiting `hypothesis:0001` testability.
3. **Build an axis x trigger "evidence-provenance" overlay** distinguishing head-to-head cells
   from assembled cells across the *whole* corpus, feeding `question:0001` and `hypothesis:0001`
   falsifiability.
4. **Read Patterson2024 critically** -- a head-to-head that *separates* LC from chronic Lyme is
   the strongest accessible disputing datapoint; assess ML-overfitting/cohort confounds.
5. **Reconcile post-chikungunya arthritis phenotype** with the fatigue-PAIS frame in
   `specs/scope-boundaries.md` -- decide whether arbovirus chronic-arthritis data are in-scope.
