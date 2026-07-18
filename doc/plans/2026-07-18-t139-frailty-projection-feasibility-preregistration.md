# t139 — Frailty signature-projection feasibility packet: frozen pre-registration

- **Date frozen:** 2026-07-18
- **Task:** `task:t139` · **Authorized by:** D-008 (feasibility packet only; a **reportable** projection is gated on a later **D-008b** ratification)
- **Status:** Step 1 (freeze) — this document. Steps 2–5 execute against it and may not silently amend the frozen choices below.

## Epistemic status (read first)

**This is an operational feasibility pre-registration, not an epistemic test.**
`commits_to: []`. **No belief update follows from this packet passing or failing.** A GO means only
that a transferable, non-artifactual frailty signature *can* be built and projected cleanly enough to
be worth a reportable run (D-008b); a NO-GO means the *method* cannot be trusted on public data — in
neither case does the project's credence in any frailty × PAIS hypothesis (`question:0033`,
`hypothesis:0001`) move. The packet screens **tooling feasibility**, exactly as t137 screened MR
feasibility. Any downstream *scientific* claim is deferred to D-008b and carries its own commitments.

## Estimand (frozen)

A **cross-sectional signature-overlap association**: does a frailty-vs-healthy-old immune
transcriptomic signature, learned in an aging cohort, score **higher in PAIS cases than in the
matched controls of the same cohort**? This is a descriptive projection overlap, **never** a
frailty→PAIS causal effect. Per **D-003**, GSE196793's influenza-vaccine challenge is not an
acute-infection trigger and its donors are never counted as PAIS cases.

## Vehicles (verified against the GEO artifacts 2026-07-18, not the catalog entities)

- **Training (primary):** `dataset:gse157007-aging-frailty-pbmc-scrna` — PBMC scRNA, NovaSeq 6000
  (GPL24676). **Verified:** 48 samples across 17 donors = 3 cord blood / 3 healthy-young / **6
  healthy-old / 5 frail**; multiple modality libraries (GEX/TCR/CITE) per donor ⇒ **donor, not
  sample, is the independent unit**. Frailty labels explicit. No timepoints. Processed matrices
  (`GSE157007_RAW.tar`, 706.4 Mb, MTX/CSV/TSV) directly downloadable. **The learnable contrast is
  5 frail vs 6 healthy-old donors** — this is the binding power constraint of the whole line.
- **Validation (contingent):** `dataset:gse196793-frailty-influenza-vaccine-pbmc` — PBMC bulk RNA,
  NextSeq 500 (GPL18573). **Verified:** 84 samples = 28 participants × 3 timepoints (Day 0/3/7);
  Fried 5-item phenotype measured; `GSE196793_htseq_counts.txt.gz` (3.5 Mb) usable; **raw FASTQ
  withheld** (privacy) so upstream processing is fixed. **CRITICAL VERIFIED GAP: per-donor Fried
  status is *not* in the GEO metadata (only participant IDs).** GSE196793 therefore enters as
  independent-platform validation **only if** per-donor frailty labels are recoverable from the
  source paper/supplement for ≥ 20 of 28 donors (Gate 1b); otherwise it is **dropped** and validation
  falls back to leave-one-donor-out within GSE157007. Day 0 (baseline) is the frozen projection point
  (cross-sectional); Day 3/7 are a response-trajectory *sensitivity* only, never the primary.
- **PAIS projection targets (frozen, tissue-prioritised).** Primary = **PBMC** deposits (tissue-matched
  to the PBMC training source): `dataset:gse251872-pime-cfs-pbmc` (PI-ME/CFS, NIH intramural),
  `dataset:gse226260-longcovid-pbmc` (LC >6 mo), `dataset:gse251849-longcovid-pbmc-cognitive` (LC
  cognitive), `dataset:scilifelab-28832492-longcovid-pbmc` (LC 28 mo). Secondary, **flagged for
  cell-composition mismatch** = whole-blood deposits: `dataset:gse270045-longcovid-mecfs-wholeblood`,
  `dataset:gse128078-mecfs-wholeblood`, `dataset:gse267625-longcovid-wholeblood`,
  `dataset:gse224615-longcovid-wholeblood`. **Excluded a priori:** `dataset:prjna1184005-longcovid-pbmc`
  (n = 7/7 — underpowered as a projection target). Each target must carry a usable case/control label
  and a processed expression matrix; a target lacking either is dropped and logged, not imputed.

## Frozen analysis parameters

1. **Independent unit = donor.** GSE157007: collapse all per-donor libraries into **one pseudobulk
   profile per donor** (sum raw counts across the donor's cells/libraries). GSE196793: donor =
   participant, Day 0 baseline. All AUC/power statistics are computed at the **donor** level, never
   the sample or cell level.
2. **Signature learning (frozen).** Frail-vs-healthy-old differential expression on GSE157007
   pseudobulk (5 vs 6 donors) via a fixed pipeline: CPM → log1p → limma-voom (or limma-trend on
   log-CPM) with donor as the unit; the signature = the signed gene set passing a **frozen**
   threshold (nominal p < 0.01 **and** |log2FC| > 0.5), capped at the top 200 by |log2FC| if larger.
   Direction (up/down in frailty) is retained. **No threshold tuning after seeing projection results.**
3. **Projection scoring (frozen).** Primary score = **mean z-score of up-genes minus mean z-score of
   down-genes**, where z-scoring is fit **independently within each target cohort** (no cross-cohort
   parameter sharing — a hard leakage control). `singscore` is a pre-registered sensitivity method,
   never a primary swap-in.
4. **Case-vs-control comparison is WITHIN cohort (frozen batch control).** Every projection AUC is
   PAIS-case vs that **same cohort's own controls**, so platform/batch is held constant per cohort.
   Scores are **never pooled across platforms** to compute a case/control contrast. Cross-cohort
   pooling appears only in the descriptive forest-style summary, never as an inference.
5. **Feature intersection (frozen).** Map all matrices to a common gene identifier space (HGNC
   symbols via a frozen Ensembl/HGNC table); the signature is intersected with each target's measured
   genes before scoring. Choices frozen before any projection is run.
6. **Leakage controls (frozen).** (a) Signature genes are selected on training only; (b) all
   normalisation/z-scoring is fit within-cohort; (c) no target-cohort label is seen during signature
   construction; (d) the permutation null (below) re-runs the *entire* pipeline including gene
   selection, not just the scoring step.

## Five gates — quantitative pass/fail (evaluated at Step 5)

| # | Gate | PASS threshold | Hard NO-GO trigger |
|---|---|---|---|
| **1a** | Training power (learnability) | Leave-one-donor-out (LODO) signature re-selection **median Jaccard ≥ 0.50** and **≥ 20 genes** reproducibly selected across folds | LODO Jaccard < 0.30 **or** < 20 reproducible genes ⇒ signature not learnable from 5v6 donors |
| **1b** | Validation labels recoverable | Per-donor Fried status recovered for **≥ 20/28** GSE196793 donors | < 20 recovered ⇒ GSE196793 dropped; validation = LODO-only (not itself a NO-GO, but logged) |
| **2** | Feature compatibility | **≥ 70%** of signature genes measurable in **≥ 80%** of retained target cohorts | A target with < 50% of signature genes measurable is dropped (logged); if **> half** of targets drop ⇒ NO-GO |
| **3** | Cross-cohort / platform-transfer robustness | Independent-platform validation **AUC ≥ 0.70** (GSE196793, if labels) **or** LODO **AUC ≥ 0.75** (fallback); **and** frailty association stronger than platform association (|r_frailty| > |r_platform|) | Validation AUC ≤ 0.60 **or** platform correlation dominates ⇒ transfer failed |
| **4** | Negative controls | (a) **Permuted-label null:** real validation AUC exceeds the **95th percentile** of ≥ 200 full-pipeline label permutations (empirical **p < 0.05**); (b) **unrelated-axis/random-geneset control:** size-matched random-gene signature gives target AUC in **[0.40, 0.60]** | Real AUC inside the permutation null (p ≥ 0.05) **or** random-geneset signature separates cases from controls (AUC > 0.65) ⇒ the "signal" is a confound |
| **5** | Non-causal framing | Every output stated as cross-sectional signature-overlap; no causal language; D-003 vaccine-challenge exclusion honoured | (editorial gate — a violation is corrected, not a NO-GO) |

### "Too-good-to-be-true" check (frozen)

If the frailty signature separates PAIS cases from controls at **AUC > 0.95 uniformly** across cohorts
of **differing platform and tissue**, this is treated as a **batch/composition-confound red flag → NO-GO
pending confound resolution**, *not* a strong GO. A real 5-vs-6-donor immune signature projected across
heterogeneous public cohorts should not be near-perfect; near-perfection implies the score is tracking
a technical axis. This check overrides an otherwise-passing Gate 3.

## GO / NO-GO decision rule (frozen, evaluated at Step 5)

- **GO** (→ draft D-008b for a reportable projection) **iff ALL** of: Gate 1a PASS; Gate 2 PASS;
  Gate 3 PASS; Gate 4 PASS (both 4a and 4b); Gate 5 adhered; and the too-good-to-be-true check does
  **not** fire. (Gate 1b may fail — GSE196793 dropped to LODO — without blocking a GO.)
- **NO-GO** (→ shelve the frailty line, joining IM and atopy; **no t110 boundary-strata line then
  survives** and the boundary-conditions program closes on public data) if **any** hard NO-GO trigger
  above fires — in particular **insufficient power** (Gate 1a) or **failed transfer** (Gate 3), the two
  most likely outcomes given 5 vs 6 training donors.
- **INCONCLUSIVE** (report as method-underpowered; do **not** draft D-008b) for borderline results that
  neither clearly pass all gates nor trip a hard trigger.

Even a GO authorises (via D-008b) only a **cross-sectional, non-causal signature-overlap** report — never
a causal frailty→PAIS claim, and never admission of GSE196793 as a PAIS case set (D-003).

## Deliverables (Step 5 packet)

A single GO/NO-GO record carrying: the pseudobulk + signature pipeline provenance and hashes; the
signature gene table (symbol, direction, log2FC, p); LODO Jaccard and gene count (Gate 1a); GSE196793
label-recovery count (Gate 1b); per-target feature-intersection fractions (Gate 2); per-cohort
within-cohort case-vs-control AUC + validation AUC + frailty-vs-platform correlations (Gate 3);
permutation-null distribution and random-geneset control AUCs (Gate 4); the too-good-to-be-true
determination; and the GO/NO-GO/inconclusive verdict with the triggering criterion. Public GEO data
only; staging via a reproducible, checksum-pinned Snakemake workflow off-Dropbox.
