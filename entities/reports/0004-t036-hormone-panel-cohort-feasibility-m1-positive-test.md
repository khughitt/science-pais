---
id: "report:0004-t036-hormone-panel-cohort-feasibility-m1-positive-test"
type: "report"
title: "t036 dataset-feasibility: hormone-panel triangulation cohorts for the M1 positive test of h0005"
status: "proposed"
source_refs:
  - task:t036
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - discussion:0001-menopause-timing-pais-rival-models
  - proposition:0002-reproductive-stage-transition-modifies-immune-regulatory-pathways
related:
  - question:0013-reproductive-stage-failed-immune-recovery-after-infection
  - question:0007-mechanism-of-female-predominance-in-pais
  - proposition:0003-infection-pais-perturbs-the-reproductive-axis-and-menopausal-timing
  - pre-registration:0001-menopause-pais-total-effect
  - task:t028
  - task:t038
  - task:t039
  - task:t040
  - paper:Silva2024
  - paper:Shahbaz2025
created: "2026-06-21"
updated: "2026-06-21"
---

# t036 dataset-feasibility: hormone-panel triangulation cohorts for the M1 positive test

## Scope and question

`task:t036` records a **load-bearing asymmetry** from the 2026-06-20 audit: the committed UK Biobank
design (`pre-registration:0001`) can **refute** `hypothesis:0005` (a powered, sensitivity-robust null
is a real downward update) but **cannot confirm** it. M1's unique positive signature — *a residual
reproductive-stage→failed-recovery association that survives flexible-age and U-proxy adjustment **and**
is at least partly **mediated by directly-measured sex hormones acting through immune / endothelial /
autonomic markers*** (`discussion:0001` §M1) — is exactly what UKB cannot measure: oestradiol is
floor-censored at 175 pmol/L, FSH/AMH are absent, and immune/endothelial markers are sparse at
infection.

This report is the **dataset-feasibility search** t036 calls for (literature/scoping grade, in scope
pre-seed-stage; the analysis itself remains post-seed-stage per `specs/scope-boundaries.md`). It scores
each candidate cohort against the M1 positive-test requirements and recommends a sequencing. It does
**not** provision data, stand up dataset entities, or gate `task:t028`.

### M1 positive-test requirements (the scoring rubric)

A vehicle for the positive test needs, jointly:

1. **Directly-measured sex-hormone panel** spanning the menopausal transition — oestradiol
   (uncensored), total/free testosterone, FSH, LH, AMH, SHBG. (FSH/AMH *stage* the transition;
   oestradiol/testosterone are the proposed mediators.)
2. **Hormone-responsive mediators** — immune (cytokines, type-I-IFN, lymphocyte subsets,
   autoantibodies), endothelial/thromboinflammatory, and autonomic measures — to test the *mediation*
   path, which is M1's only positive signature.
3. **Reproductive staging** — menopausal status, age at menopause, surgical menopause, HRT use.
4. **Post-acute-infection / PAIS phenotyping** — a failed-recovery outcome, ideally **PEM-stratifiable**.
5. **Longitudinal design with a pre-infection baseline** — within-person hormone/marker trajectories
   from *before* infection through recovery, the design that breaks the **reverse-causation ambiguity**
   `proposition:0003` (P← rival) exploits. The cross-sectional clinical cohorts that motivate t036
   (`paper:Silva2024`, `paper:Shahbaz2025`) cannot do this.
6. **Accessible / reproducible** — consistent with the project's reproducible-from-accessible-data norm
   (the t033 decision to decline private Galbraith arrays and pivot to public datasets).

## Headline finding

**No off-the-shelf vehicle for the M1 positive test exists in the candidate set.** Every candidate
fails ≥1 requirement that cannot be satisfied from already-collected data. More importantly, the
failures are **structurally anti-correlated**, not incidental:

> **The pre-infection-baseline requirement (R5) and the hormone-panel requirement (R1) are
> anti-correlated across the available cohort landscape.** The only cohorts with a genuine
> pre-infection baseline are general-population biobanks (All of Us, Lifelines, Generation Scotland) —
> and those either measured **no** sex steroids (Lifelines, GS) or only **opportunistic** EHR-lab
> hormones (All of Us). Every cohort *purpose-built* for long COVID with deep mediators (RECOVER,
> IMPACC) enrols **after** infection, so none can break the P3 reverse-causation ambiguity.

This is the deep reason M1's positive test is *hard*, not merely unfunded — and it is the
methodological justification for `proposition:0002` remaining **single-line fragile** and for keeping
the refute-only UKB design as the committed primary. A clean positive test requires *manufacturing* the
missing arm: either assaying sex steroids on banked biospecimens in a post-infection cohort (loses R5),
or finding adequate opportunistic hormone coverage in a pre-infection biobank (loses R2 systematic
mediators).

## Per-cohort assessment

Ratings: STRONG / PARTIAL / WEAK / ABSENT per axis; "could be assayed from biobank" is distinguished
from "already measured" throughout.

| Cohort | R1 hormones | R2 mediators | R3 repro staging | R4 PAIS/PEM | R5 pre-infection baseline | R6 access |
|---|---|---|---|---|---|---|
| **RECOVER-Adult** | PARTIAL (AMH measured; E2/T/FSH/LH/SHBG assayable from Mayo biobank) | **STRONG** (immune + endothelial Tier-1 + autonomic Tier-1/3) | PARTIAL | **STRONG (PEM-weighted index)** | **WEAK (enrols ≥3 mo post-infection)** | WEAK (ancillary-study + external funding gated) |
| **All of Us** | PARTIAL (uncensored EHR labs; coverage UNKNOWN/sparse) | PARTIAL (Fitbit HRV strong; immune/endothelial = crude EHR labs only) | **STRONG** (survey + EHR, ~396k women) | PARTIAL (large U09.9/COPE *substrate*, but **no PEM** and no biologically coherent PAIS phenotype) | **PARTIAL (pre-pandemic enrol + EHR backfill)** | PARTIAL (free but DURA/in-cloud, no export) |
| **IMPACC** | WEAK (no panel; relative-abundance androgen metabolites only) | STRONG-immune (multi-omic) / thin endothelial / ABSENT autonomic | ABSENT | PARTIAL (PRO clusters; no PEM; hospitalized skew) | WEAK (enrols at hospital admission; no pre-infection) | PARTIAL data (ImmPort/dbGaP) / WEAK biospecimens |
| **Lifelines** | ABSENT (female sex hormones not assayed; male-only VESPER testosterone) | PARTIAL (GlycA/NMR proxy; ECG; no cytokine panel) | PARTIAL (questionnaire; unverified) | STRONG-symptom / WEAK-biological (no PEM) | STRONG-phenotype / ABSENT-biomarker re-measure | PARTIAL (enclave, fees, no export) |
| **Gen. Scotland** | ABSENT (zero sex steroids; baseline chem = 6 analytes) | STRONG (DNAm-CRP, protein/cytokine EpiScores) | PARTIAL (questionnaire + linkage) | PARTIAL (CovidLife + NHS linkage; no PEM) | **PARTIAL design / FATAL staleness (markers measured 2006–2011, ~9–15 yr pre-infection)** | PARTIAL (Safe Haven, no export) |

### Tier 1 — best, but bespoke: RECOVER-Adult

The strongest single vehicle, and the only candidate that can plausibly carry the *primary* positive
test. **AMH is already in the protocol** (Tier 2, added v3.0) — the one staging analyte UKB lacks.
**PEM is the second-highest-weighted symptom** in the validated Thaweethai 2023 PASC index (~87% of
PASC-positive participants), so the in-scope PEM-stratified failed-recovery outcome is best-in-class.
Mediators span all three families: Tier-1 D-dimer/troponin/NT-proBNP/ECG (endothelial/thrombo-
inflammatory) and Tier-1 10-min active stand + Tier-3 tilt-table/catecholamine (autonomic), plus a
12-task-force pathobiology program (cytokines, autoantibodies, antigen persistence) on banked
serum/plasma/PBMC at Mayo. The full **estradiol/T/FSH/LH/SHBG panel is assayable de novo** from that
biorepository.

**Two decisive limitations.** (1) Enrolment starts ≥3 months post-infection → **no within-person
pre-infection hormone baseline**; reverse causation is only *partially* addressable via the
uninfected-control arm + post-infection trajectory, not a clean pre-exposure anchor. (2) The hormone
exposure **does not yet exist** and must be generated via an **ancillary-study proposal (ASOC) with
independently secured external funding** — application-gated, multi-month, and not freely
reproducible-from-public-data.

### Tier 2 — only candidate that can break reverse causation: All of Us

Uniquely pairs (a) **uncensored** sex hormones — real EHR clinical labs, no UKB 175 pmol/L ceiling, no
missing-FSH/AMH-by-design — with (b) **pre-pandemic enrolment + EHR backfill** (potential within-person
pre→post-infection trajectories) and (c) **strong dual-source reproductive staging** (survey + EHR,
~396k women characterized) and (d) a genuine autonomic stream (Fitbit RMSSD HRV). On paper this is the
only cohort that could address P3.

**The catch is sparsity, not censoring.** Hormones and immune/endothelial markers are *opportunistic*
EHR labs — ordered for clinical reasons (fertility, amenorrhea, HRT monitoring), so coverage is
non-random and likely thin in exactly the peri-/post-menopausal women of interest, with
selection-into-measurement as a mediation confounder. There is **no systematic cytokine/IFN/auto-
antibody panel** and **no documented PEM** capture. Feasibility hinges on per-analyte coverage counts
**that can only be resolved by querying the Researcher Workbench Data Browser** — an empirical
precondition, not answerable from public docs.

### Tier 3 — secondary corroboration only: IMPACC

The deepest **longitudinal immune multi-omics** of any candidate (serial transcriptomics, Olink,
proteomics, metabolomics, CyTOF, autoantibody/VirScan across acute→12-mo convalescent), and it already
reports a **sex-linked, androgen-metabolite long-COVID signal** (DHEA-S, androsterone-sulfate, etc.
*lower* in long COVID) that is **compatible with M1's steroid-axis / mediator predictions**. This is a
**steroid-axis / mediator-compatible** corroboration, *not* direction-confirming: with no sex-hormone
panel (only relative-abundance metabolites, not quantitative E2/FSH/AMH), **no reproductive/menopausal
data**, **no pre-infection baseline**, hospitalized-severity skew (steroids confounded by critical
illness), no PEM, and no autonomic measures, IMPACC can neither establish the hormone→recovery
*direction* nor resolve reverse causation. **Verdict: a mediator-compatible secondary analysis**, not a
primary M1 vehicle —
but its processed data are obtainable (ImmPort SDY1760 / dbGaP phs002686) **without new assays**, making
it the cheapest, most reproducible near-term triangulation.

### Tier 4 — ruled out as M1 vehicles: Lifelines, Generation Scotland

Both have a best-in-class *phenotyping* strength but a disqualifying *exposure* gap:

- **Lifelines** — outstanding within-person long-COVID **symptom** design (Ballering 2022, *Lancet*,
  n=76,422, participants-as-own-control with pre-pandemic baseline), but **essentially no measured
  female sex hormones** (only male-only VESPER testosterone) and the CORONA follow-up collected **no
  new biomaterials**. The entire hormone→mediator chain would be de-novo assays on a single-timepoint
  pre-pandemic serum aliquot.
- **Generation Scotland** — outstanding **methylation-derived** immune/inflammation proxy layer
  (DNAm-CRP, GrimAge/protein/cytokine EpiScores) and rich NHS COVID linkage, but baseline biochemistry
  was **six standard analytes with zero sex steroids** (worse than UKB), and all biomarkers were
  measured **once in 2006–2011, ~9–15 years before any 2020+ infection** — a **staleness gap that is
  fatal for a menopause-transition mediation analysis** (baseline reproductive stage is frequently not
  the stage at infection).

Retain both only as **long-COVID symptom-design references**, not as hormone-mediation vehicles.

## Disposition and recommended sequencing

1. **t036 closed; superseded by three path-specific follow-ups.** The dataset-feasibility *search* was
   t036's deliverable and is complete. Because t036 was framed as *acquisition* of All of Us / Lifelines
   / Generation Scotland — two of which (Lifelines, GS) this report **rules out** as M1 vehicles —
   leaving it open would point future work at discarded targets. It is therefore closed and replaced by
   the three surviving paths as separately-tracked tasks (different readiness levels, so not one task):
   **`task:t038`** (IMPACC), **`task:t039`** (All of Us coverage query), **`task:t040`** (RECOVER
   ancillary). The positive test itself remains post-seed-stage.
2. **No dataset entities created.** Per scope, the dataset-entity lifecycle is for analysis
   provisioning (t028-style), which remains post-seed-stage. This report is the durable artifact.
3. **Recommended order of pursuit** (cheapest/most-reproducible first):
   - **(a) IMPACC open-data secondary corroboration → `task:t038`** — test whether the *existing*
     steroid-axis (relative-abundance androgen metabolites) and immune/metabolic mediator structure is
     **compatible with** M1's predictions, using ImmPort/dbGaP data with **no new assays**. This is a
     **mediator-compatible** corroboration, *not* direction-confirming: IMPACC has no quantitative
     hormone panel, no reproductive staging, no pre-infection baseline, and a hospitalized skew, so it
     can neither establish the hormone→recovery *direction* nor resolve reverse causation. The
     literature-synthesis portion is in scope now; a fresh multi-omic re-analysis is post-seed-stage.
   - **(b) All of Us Workbench coverage query → `task:t039`** — a *scoping* query (feasibility-grade)
     for per-analyte oestradiol/FSH/AMH coverage and repeat-measure counts in long-COVID-affected
     peri-/post-menopausal women. This is the empirical gate that decides whether All of Us can ever be
     the reverse-causation-breaking vehicle. Cheap; resolves the single biggest UNKNOWN. (Access-gated:
     needs a signed DURA / Workbench account.)
   - **(c) RECOVER ancillary biospecimen study → `task:t040`** — the eventual *primary* positive test
     (assay the sex-steroid panel on banked serum, exploit AMH + PEM-stratified outcome + deep
     mediators). Post-seed-stage, funding- and committee-gated; the highest-quality but highest-cost path.
4. **This does not change `proposition:0002`'s fragility.** The report **explains** it: because no
   accessible cohort jointly satisfies R1+R2+R5, the core mechanism leg cannot yet be independently
   corroborated from existing data, and the single-line-fragile flag is an honest reflection of the
   cohort landscape, not a fixable bookkeeping artifact. The earliest realistic move is path (a)
   (IMPACC) — and even that is only *mediator-compatible*, not direction-confirming; a *causally clean*
   corroboration awaits path (b) or (c).

## What would change this verdict

- A new or extended cohort that **re-measures** sex hormones + immune/endothelial markers during a
  **pre→post-infection** window in the same women (the one design absent everywhere here).
- An All of Us Workbench query showing **adequate, non-selectively-ordered** oestradiol/FSH coverage in
  the target stratum (would promote All of Us from Tier 2 to a viable reverse-causation-breaking
  vehicle).
- A RECOVER pathobiology sub-study that has **already assayed sex steroids** on banked serum (would
  remove the funding-gated assay step; flagged as an unresolved UNKNOWN in the RECOVER scoping —
  supplemental analyte tables were not fully readable).

## Sources

Per-cohort scoping was conducted 2026-06-21 against official program documentation, data
dictionaries/catalogues, and cohort-profile / design papers. Key anchors:

- **RECOVER-Adult:** Horwitz/Thaweethai et al. protocol (medRxiv 2023.05.26.23290475 / PMC10289397);
  Thaweethai et al. *JAMA* 2023 PASC index (PMID 37278994); RECOVER biospecimen/ancillary-study pages
  (recovercovid.org/data, /studies/ancillary).
- **All of Us:** Researcher Workbench + data-tiers documentation (researchallofus.org); OMOP
  `measurement` labs; menopause descriptive paper (medRxiv 2026.04.17.26351129); COPE survey
  (PMC10505411); Fitbit/WEAR HRV (PMC12264798).
- **IMPACC:** design paper (PMC8713959); long-COVID multi-omics / androgen-metabolite paper
  (`paper:Gabernet2025`; PMC12582403; *J. Clin. Invest.* 2025;135(21):e193698; DOI 10.1172/JCI193698 —
  **corrected**: the originally-cited Nat. Commun. s41467-023-44090-5 is `paper:Ozonoff2024`, the
  PRO-phenotype paper, not the androgen-metabolite result; see `report:0005`); ImmPort SDY1760 / dbGaP
  phs002686.
- **Lifelines:** IJE Cohort Profile Update (PMC9558073); Ballering et al. *Lancet* 2022 (PMID 35934007);
  VESPER subcohort (wiki.lifelines.nl); data catalogue (data-catalogue.lifelines.nl).
- **Generation Scotland:** researcher data pages (genscot.ed.ac.uk); 2024 GS update (PMC11340249);
  protein EpiScores (PMC8880990); CovidLife (PMC10884595); record-linkage (PMC10929504).
