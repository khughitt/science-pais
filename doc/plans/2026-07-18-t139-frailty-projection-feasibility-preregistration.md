# t139 — Frailty signature-projection feasibility packet: frozen pre-registration

- **Date frozen:** 2026-07-18
- **Task:** `task:t139` · **Authorized by:** D-008 (feasibility packet only; a **reportable** projection is gated on a later **D-008b** ratification)
- **Status:** Step 1 (freeze), **re-frozen after Amendment 1**, then **re-frozen after Amendment 2** (pre-target training-side gate added). Steps 2–5 execute against it and may not silently amend the frozen choices below.

## Amendment 1 (pre-execution, 2026-07-18)

Recorded **before any of Steps 2–5 ran** — no data was touched between the original freeze and this
amendment, so it introduces no outcome-dependent researcher degrees of freedom; it *removes* four.
The affected inline text below has been reconciled and tagged `[A1]`.

1. **Training pseudobulk uses the scRNA gene-expression libraries only.** GSE157007 records GEX, TCR
   V(D)J, and cell-surface-protein (CITE) as **separate modalities/files**; only the `_scRNA` GEX
   matrices are summed into the donor pseudobulk. VDJ and protein libraries are excluded — pooling
   them would contaminate the count space. (Affects Vehicles → Training and Frozen parameter 1.)
2. **One exact DE pipeline, no `or`.** `voom` consumes raw counts/`DGEList`; `limma-trend` consumes
   logCPM — the original "voom **or** limma-trend" left an outcome-dependent choice. Frozen to a single
   **limma-voom-on-raw-pseudobulk-counts** pipeline (Frozen parameter 2). The prior `CPM → log1p`
   pre-step is dropped because `voom` performs log-CPM with precision weights internally.
3. **Unrecoverable GSE196793 labels ⇒ INCONCLUSIVE, not GO.** D-008 requires the signature to survive
   **scRNA→bulk platform transfer**; a scRNA-only leave-one-donor-out (LODO) result is single-platform
   and cannot discharge that requirement. The original "LODO AUC ≥ 0.75 fallback" GO path is **removed**.
   If GSE196793 per-donor Fried labels are not recovered (Gate 1b fails) **and** no substitute genuine
   *bulk* frailty-labelled transfer cohort is specified by a further amendment, the packet verdict is
   **INCONCLUSIVE** (no D-008b) — LODO remains only as the Gate 1a learnability check. (Affects Gates 1b, 3;
   GO/NO-GO rule.)
4. **Operationalised the three under-defined quantities** (Gates 1a, 3, 4b) — `r_platform`, the Jaccard
   denominator + reproducibility frequency, and the random-control *distribution* + across-cohort
   aggregation — are now given exact frozen definitions in-line.

## Amendment 2 (pre-target, 2026-07-18): batch-adjusted learnability gate

Recorded **after Step 2 but before any target/PAIS label is opened** (Step 3 held). Step 2 surfaced a
**submission-batch ↔ contrast confound** in the training cohort itself: all **5 frail + 3 of 6
healthy-old** donors are the **F0xx** submission (GSM4750xxx); the other **3 healthy-old** are the later
**OH** submission (GSM5684xxx), which is also systematically deeper (~12k vs 2.5–8k cells/donor). So the
frozen frail-vs-old contrast is **partly a between-submission contrast**, and this is a *training-side*
validity threat that the frozen Gates 3–4 **cannot** detect:

- **Gate 3b** (target-local `r_platform`) diagnoses *target-side* composition/depth artifacts — it does
  **not** diagnose a signature that is *already* submission-batch-driven at training time.
- **Gate 4a** label permutations, if drawn **unrestricted**, permute frailty labels *across* the two
  submission batches and so **destroy the batch block structure** — an **exchangeability violation** that
  makes the null too easy to beat and would spuriously "confirm" a batch signal.
- A submission-batch-derived **inflammatory** signature can be **biologically coherent** (IL6/CSF up) and
  can still **transfer** to PAIS cohorts (which are themselves inflammatory). Face validity and transfer
  therefore **do not** rule the confound out.

This amendment **adds one pre-target gate and tightens Gate 4a's null**; both *remove* researcher degrees
of freedom (they constrain the null and add a stopping condition) rather than adding outcome-dependent
choices. **Within D-008 — no new scope decision.** No PAIS/target label is inspected at Step 2b.

1. **Refit with `~ submission + frailty`.** Re-run the frozen Frozen-parameter-2 pipeline adding the
   submission batch as a covariate. Because OH is old-only, the **frailty coefficient is identified chiefly
   by the within-F0xx 5-frail-vs-3-old contrast** (OH donors load on the submission term, contributing no
   frailty variation). The design is full-rank (F0xx carries both arms) and stays full-rank under any single
   donor drop.
2. **Adjusted LODO + comparison to the frozen primary.** Repeat the Gate-1a leave-one-donor-out check
   under the adjusted model, and compare the adjusted **signed** signature to the **frozen primary**
   signature — both judged against the **existing Gate-1a Jaccard / gene-count thresholds** (median
   pairwise Jaccard ≥ 0.50 clears, < 0.30 NO-GO; ≥ 20 shared/reproducible genes).
3. **Within-submission-batch permutations (Gate 4a exchangeability correction).** Gate 4a's label
   permutations are **restricted to within submission batch**: frail/old labels are permuted only among the
   **8 F0xx donors**; the **3 OH donors are old-only and contribute no frailty-label permutation**. The
   frozen across-cohort aggregation is unchanged. (Applied when Gate 4 runs at Step 5.)
4. **Decision rule.** **Failure** of batch-adjusted learnability is a **NO-GO** (the primary signature was
   substantially submission-driven, not a frailty signal); a **borderline** adjusted result is
   **INCONCLUSIVE**; only a **clear pass** lets Step 3 proceed. Until Gate 1a-adj passes, the attractive
   cytokine panel (CSF3/IL6/CSF2/IRG1/…) is **non-adjudicating face validity — not evidence**.

Gate **1a-adj** is evaluated at a new **Step 2b** (pre-target), and its NO-GO **halts the packet before
Step 3**. It is recorded in the gates table, operational definitions, and GO/NO-GO rule below.

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
  (`GSE157007_RAW.tar`, 706.4 Mb, MTX/CSV/TSV) directly downloadable. **`[A1]` Only the scRNA
  gene-expression (`_scRNA` GEX) matrices are used for pseudobulk** — the TCR V(D)J and cell-surface
  protein (CITE) libraries are separate GEO modalities and are excluded. **The learnable contrast is
  5 frail vs 6 healthy-old donors** — this is the binding power constraint of the whole line.
- **Validation (contingent):** `dataset:gse196793-frailty-influenza-vaccine-pbmc` — PBMC bulk RNA,
  NextSeq 500 (GPL18573). **Verified:** 84 samples = 28 participants × 3 timepoints (Day 0/3/7);
  Fried 5-item phenotype measured; `GSE196793_htseq_counts.txt.gz` (3.5 Mb) usable; **raw FASTQ
  withheld** (privacy) so upstream processing is fixed. **CRITICAL VERIFIED GAP: per-donor Fried
  status is *not* in the GEO metadata (only participant IDs).** GSE196793 therefore enters as
  the independent-platform (scRNA→bulk) transfer validation **only if** per-donor frailty labels are
  recoverable from the source paper/supplement for ≥ 20 of 28 donors (Gate 1b); otherwise it is
  **dropped**, and — `[A1]` because LODO within GSE157007 is single-platform and cannot demonstrate
  transfer — the packet is **INCONCLUSIVE** unless a substitute genuine *bulk* frailty-labelled cohort
  is added by amendment. Day 0 (baseline) is the frozen projection point (cross-sectional); Day 3/7 are
  a response-trajectory *sensitivity* only, never the primary.
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

1. **Independent unit = donor.** GSE157007: `[A1]` sum **raw scRNA GEX counts across the donor's
   cells** (GEX libraries only; VDJ/CITE excluded) into **one pseudobulk count profile per donor**.
   GSE196793: donor = participant, Day 0 baseline. All AUC/power statistics are computed at the
   **donor** level, never the sample or cell level.
2. **Signature learning (frozen, single pipeline — `[A1]` no alternatives).** From the donor-level
   pseudobulk **raw count** matrix (scRNA GEX only): `filterByExpr(group = frailty)` (defaults) →
   `DGEList` → `calcNormFactors(method = "TMM")` → `voom` (no `sample.weights`) → `lmFit(~ frailty)` →
   `eBayes` → `topTable`. **limma-voom on raw counts is the sole DE method**; limma-trend/logCPM and the
   prior `CPM → log1p` pre-step are removed (voom performs weighted log-CPM internally). The signature =
   the signed gene set passing a **frozen** threshold (nominal p < 0.01 **and** |log2FC| > 0.5), capped
   at the top 200 by |log2FC| if larger; direction (up/down in frailty) retained. Nominal (not adjusted)
   p is deliberate — this is a **screening** signature at 5 vs 6 donors, and its reproducibility is
   adjudicated by the Gate 1a LODO check, not by FDR. **No threshold tuning after seeing projection results.**
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
| **1a** | Training power (learnability) | LODO signature re-selection **median pairwise Jaccard ≥ 0.50** and **≥ 20 genes** at selection-frequency **≥ 0.8** (def. below) | LODO Jaccard < 0.30 **or** < 20 reproducible genes ⇒ signature not learnable from 5v6 donors |
| **1a-adj** | `[A2]` Batch-adjusted learnability (**pre-target, Step 2b**) | Under `~ submission + frailty`: adjusted LODO **median pairwise Jaccard ≥ 0.50** and **≥ 20** reproducible genes, **and** the adjusted signed signature overlaps the frozen primary at **signed Jaccard ≥ 0.50** with **≥ 20 shared** signed genes (def. below) | Adjusted LODO Jaccard < 0.30 / < 20 reproducible genes, **or** signed overlap with primary < 0.30 ⇒ the primary signature was **submission-batch-driven** ⇒ **NO-GO (halts packet before Step 3)** |
| **1b** | Validation labels recoverable | Per-donor Fried status recovered for **≥ 20/28** GSE196793 donors | `[A1]` < 20 recovered **and** no substitute bulk transfer cohort ⇒ **INCONCLUSIVE** (LODO cannot stand in for bulk transfer; no D-008b) |
| **2** | Feature compatibility | **≥ 70%** of signature genes measurable in **≥ 80%** of retained target cohorts | A target with < 50% of signature genes measurable is dropped (logged); if **> half** of targets drop ⇒ NO-GO |
| **3** | Cross-cohort / platform-transfer robustness | `[A1]` **3a** bulk-transfer validation **AUC ≥ 0.70** (GSE196793 frail-vs-nonfrail — the scRNA→bulk demonstration; **no LODO fallback**); **and 3b** composition/technical check `r_frailty > r_platform` (def. below) in a **majority** of retained PBMC targets | 3a AUC ≤ 0.60 **or** 3b fails (technical axis dominates) ⇒ transfer failed |
| **4** | Negative controls | `[A1]` (a) **permuted-label null:** real 3a AUC > **95th pct** of ≥ 200 full-pipeline label permutations (**p < 0.05**), `[A2]` **permutations restricted to within submission batch** (def. below); (b) **matched-random-set null:** real aggregate AUC > **95th pct** of a **distribution of N = 1000** size- and expression-matched random signatures (def. below) | Real AUC inside the label null (p ≥ 0.05) **or** inside the random-set null (p ≥ 0.05) ⇒ the "signal" is a confound |
| **5** | Non-causal framing | Every output stated as cross-sectional signature-overlap; no causal language; D-003 vaccine-challenge exclusion honoured | (editorial gate — a violation is corrected, not a NO-GO) |

### Operational definitions (Amendment 1, frozen)

- **Gate 1a — LODO Jaccard + frequency.** Leave-one-donor-out over all **11** training donors (5 frail
  + 6 healthy-old) ⇒ 11 fold-signatures, each re-derived by the *full* Frozen-parameter-2 pipeline.
  **Median pairwise Jaccard** = median of `|Aᵢ∩Aⱼ| / |Aᵢ∪Aⱼ|` over all C(11,2)=55 fold pairs (union
  denominator). **Selection frequency** of a gene = fraction of the 11 folds whose signature contains it;
  "reproducible" = frequency **≥ 0.8** (≥ 9/11 folds). Gate 1a needs median pairwise Jaccard ≥ 0.50 **and**
  ≥ 20 genes at frequency ≥ 0.8.
- **Gate 1a-adj — batch-adjusted learnability (`[A2]`, Step 2b).** `submission` ∈ {F0xx, OH} is assigned
  per donor from its GEO submission block (F0xx = GSM4750xxx / 5 frail + 3 healthy-old; OH = GSM5684xxx /
  3 healthy-old), asserted at run time (HALT on drift). The frozen DE pipeline is refit with
  `design = model.matrix(~ submission + frailty)` (ref levels: submission = F0xx, frailty = healthy-old),
  the frailty coefficient extracted, and the signature re-derived under the **identical** frozen thresholds
  + cap. **Adjusted LODO** repeats the 11-fold leave-one-donor-out under this adjusted model (median
  pairwise Jaccard over C(11,2)=55 fold pairs, union denominator; reproducible = frequency ≥ 0.8) — reusing
  the Gate-1a thresholds. **Signed-overlap-to-primary** = Jaccard of the adjusted vs frozen-primary
  signature counting a gene shared **only if present in both with the same direction**; also reported: the
  raw (unsigned) Jaccard, the shared-gene count, and the direction-concordance among shared genes. Gate
  1a-adj **clears** iff adjusted LODO Jaccard ≥ 0.50 **and** ≥ 20 reproducible genes **and** signed overlap
  ≥ 0.50 **and** ≥ 20 shared signed genes; **trips NO-GO** iff adjusted LODO Jaccard < 0.30, or < 20
  reproducible genes, or signed overlap < 0.30; anything between is **borderline ⇒ INCONCLUSIVE**.
- **Gate 4a — within-submission-batch label permutation (`[A2]`).** The ≥ 200 label permutations of Gate 4a
  are drawn **within submission batch**: the frail/old labels are permuted only among the **8 F0xx donors**
  (5 frail + 3 old); the **3 OH donors keep their old label** (old-only batch ⇒ no frailty-label swap). This
  preserves the batch block structure so the null reflects the true (batch-restricted) exchangeability. The
  full pipeline (incl. gene selection) is re-run per permutation; the frozen across-cohort aggregation is
  unchanged.
- **Gate 3b — `r_frailty` and `r_platform`.** Within each retained PBMC target cohort: `r_frailty` =
  |point-biserial correlation| between the donor projection score and case/control status; `r_platform`
  = the **maximum** |Pearson correlation| between the projection score and each frozen technical/composition
  axis — (i) log₁₀ total counts (library size/depth), (ii) estimated granulocyte/neutrophil fraction,
  (iii) estimated lymphocyte fraction (fractions from a frozen marker-based deconvolution restricted to
  major lineages). 3b passes for a cohort iff `r_frailty > r_platform`, and overall iff that holds in a
  majority of retained PBMC targets.
- **Gate 4b — matched-random-set null + frozen aggregation.** Draw **N = 1000** random gene sets, each
  matched to the real signature on **size** and **mean-pseudobulk-expression decile** (controls the
  expression-level confound). The **frozen across-cohort aggregate** = unweighted mean of within-cohort
  case-vs-control AUC across the **retained PRIMARY (PBMC) targets only** (whole-blood secondary never
  pooled into inference). Compare the real signature's aggregate to the 1000-set null of aggregates; PASS
  requires real > 95th percentile **and** the null median in [0.45, 0.55] (sanity).

### "Too-good-to-be-true" check (frozen)

If the frailty signature separates PAIS cases from controls at **AUC > 0.95 uniformly** across cohorts
of **differing platform and tissue**, this is treated as a **batch/composition-confound red flag → NO-GO
pending confound resolution**, *not* a strong GO. A real 5-vs-6-donor immune signature projected across
heterogeneous public cohorts should not be near-perfect; near-perfection implies the score is tracking
a technical axis. This check overrides an otherwise-passing Gate 3.

## GO / NO-GO decision rule (frozen, evaluated at Step 5)

- **`[A2]` Gate 1a-adj is a pre-target precondition.** It is evaluated at **Step 2b, before any target
  label is opened**. If it trips NO-GO the packet **stops there** — Steps 3–5 do not run. If it is
  borderline the packet is **INCONCLUSIVE** and Steps 3–5 do not run. Only a clear pass clears Step 3.
- **GO** (→ draft D-008b for a reportable projection) **iff ALL** of: Gate 1a PASS; **`[A2]` Gate 1a-adj
  PASS**; **a genuine bulk transfer validation exists** (Gate 1b PASS, or a substitute bulk
  frailty-labelled cohort added by amendment); Gate 2 PASS; Gate 3 PASS (both 3a and 3b); Gate 4 PASS
  (both 4a and 4b); Gate 5 adhered; and the too-good-to-be-true check does **not** fire.
- **NO-GO** (→ shelve the frailty line, joining IM and atopy; **no t110 boundary-strata line then
  survives** and the boundary-conditions program closes on public data) if **any** hard NO-GO trigger
  above fires — in particular `[A2]` **batch-driven signature** (Gate 1a-adj), **insufficient power**
  (Gate 1a), or **failed transfer** (Gate 3a AUC ≤ 0.60 / Gate 3b technical dominance), the most likely
  outcomes given 5 vs 6 training donors partly split across two submissions.
- **INCONCLUSIVE** (report as method-undemonstrated; do **not** draft D-008b) when transfer cannot be
  *tested* rather than being tested-and-failed: **`[A1]` Gate 1b fails and no substitute bulk cohort is
  specified** (scRNA-only LODO cannot discharge D-008's scRNA→bulk transfer requirement), **`[A2]` a
  borderline Gate 1a-adj result**, or for other borderline results that neither clearly pass all gates nor
  trip a hard NO-GO trigger.

Even a GO authorises (via D-008b) only a **cross-sectional, non-causal signature-overlap** report — never
a causal frailty→PAIS claim, and never admission of GSE196793 as a PAIS case set (D-003).

## Deliverables (Step 5 packet)

A single GO/NO-GO record carrying: the pseudobulk + signature pipeline provenance and hashes; the
signature gene table (symbol, direction, log2FC, p); LODO Jaccard and gene count (Gate 1a); `[A2]` the
batch-adjusted (`~ submission + frailty`) signature, its adjusted-LODO Jaccard/gene count, and its
signed-overlap-to-primary (Gate 1a-adj verdict, Step 2b); GSE196793
label-recovery count (Gate 1b); per-target feature-intersection fractions (Gate 2); per-cohort
within-cohort case-vs-control AUC + bulk-transfer validation AUC (3a) + per-cohort `r_frailty`/`r_platform`
(3b); the label-permutation null (4a) and the N=1000 matched-random-set null of aggregate AUC (4b); the too-good-to-be-true
determination; and the GO/NO-GO/inconclusive verdict with the triggering criterion. Public GEO data
only; staging via a reproducible, checksum-pinned Snakemake workflow off-Dropbox.
