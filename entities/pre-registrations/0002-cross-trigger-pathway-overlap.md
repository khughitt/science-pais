---
id: "pre-registration:0002-cross-trigger-pathway-overlap"
type: "pre-registration"
title: "Pre-registration: cross-trigger pathway-overlap concordance (GSE14577 + GSE130353) as a hypothesis-generating probe of shared post-infectious pathophysiology (t035)"
status: "committed"
committed: "2026-06-20"
mode: data-gated
spec: "entities/plans/0002-cross-trigger-pathway-overlap-analysis-plan.md"
related:
  - hypothesis:0001-shared-dysregulated-attractor
  - question:0001-shared-molecular-signature-across-triggers
  - question:0017-deflationary-alternatives-vs-shared-pathophysiology
  - discussion:0002-cross-pathogen-pais-signature-convergence
  - plan:0002-cross-trigger-pathway-overlap-analysis-plan
  - paper:Gow2009
  - paper:Raijmakers2019
  - task:t035
commits_to:
  - hypothesis:0001-shared-dysregulated-attractor
  - question:0017-deflationary-alternatives-vs-shared-pathophysiology
created: "2026-06-20"
updated: "2026-06-20"
---

# Pre-registration: cross-trigger pathway-overlap concordance (GSE14577 + GSE130353)

> **Mode: data-gated.** The decision rule below is committed **now**; execution is deferred
> until a provisioned vehicle clears the G-gates in *Vehicle-Admissibility Gate*. The two
> public deposits exist but their **expression payloads are not yet provisioned** (only
> metadata/structure files are local — `doc/datasets/2026-06-20-public-cross-trigger-geo-sets.md`
> still reads "candidate / not yet provisioned"). Until all G-gates clear **and** the analysis
> runs, the standing verdict is `[?] inconclusive-for-coverage` and there is **no `bears_on`
> update** on the commitment targets. Committing this document **discharges the plan's fourth
> blocking check (pre-registration lock)**; the remaining three plan checks are encoded as
> G1–G3 below.

## Hypotheses Under Test

- **`hypothesis:0001-shared-dysregulated-attractor`** (primary commitment target) — distinct
  infectious triggers converge on a shared post-infectious failure mode detectable at the
  **pathway** level. This pre-reg tests the cheapest available probe of that claim:
  pathway-enrichment **rank concordance** between two *distinct* triggers (post-viral CFS,
  GSE14577; Q-fever fatigue, GSE130353).
- **`question:0017-deflationary-alternatives-vs-shared-pathophysiology`** (commitment target) —
  the result is scored against the **finite-repertoire-coincidence** and **ascertainment/
  exposure-confounding** nulls bundled there.
- `question:0001-shared-molecular-signature-across-triggers` (navigation context, **not** a
  commitment target) — this 2-cohort exploratory probe is a *step toward* but explicitly **not**
  the decisive ≥3-trigger harmonized test q0001 demands; it does not resolve q0001, so no
  `bears_on` edge is claimed to it.

This is an **epistemic** pre-registration with an **operational** sub-portion (the locked
analysis procedure). A null result is **weighted evidence**, not a verdict that kills
`hypothesis:0001`.

## Feasibility Against Real Input Artifacts (pre-data, load-bearing)

Confirmed from the SOFT/series-matrix **metadata** (2026-06-20), before any threshold was locked:

- **GSE14577** — 30 GEO samples = 15 patients × 2 chips (U133A GPL96 + U133B GPL97); **7 HC + 8
  PI-CFS**; sex = **all male**; Fukuda criteria; PBMC; `ID_REF\tVALUE` tables present, log2-scale
  (VALUE ≈ 6–8). The confirmatory arm **PI-CFS-vs-HC** is therefore constructable at 8 vs 7.
- **GSE130353** — 40 samples, **10 per group** (HC / CFS / QFS / QS-seropositive-recovered);
  isolated **monocytes**; series-matrix data table **empty** → expression lives in 40 per-sample
  `*.gene.mmseq.txt.gz`. The confirmatory partner arm **QFS-vs-HC** (10 vs 10) and the
  specificity backbone **QFS-vs-QS** (10 vs 10) are both constructable; the **QS group (n=10)
  exists**, so the presence-based specificity test is feasible.

Two feasibility facts that shaped the design rather than being discovered post-data: (a) the
**effective cross-trigger unit is the cohort, and there are only two** → the verdict ceiling is
*suggestive*, not confirmatory, regardless of gene/pathway count; (b) GSE130353 metadata **does
not report sex**, so it cannot be matched to GSE14577's male-only restriction — sex is an
unmeasured, unadjustable confound carried as a limitation, not a covariate.

## Expected Outcomes

- **Primary expectation:** a **weakly positive** NES rank concordance (Spearman ρ) between
  PI-CFS-vs-HC and QFS-vs-HC over the pinned Hallmark universe — driven by innate/IFN,
  oxidative-stress, and mitochondrial/OXPHOS themes — that **clears the permutation null** but
  sits well short of strong/confirmatory. Basis: the prior provenance audit (`discussion:0002`,
  `question:0001`) finds convergence is demonstrable at **pathway/physiology** level (Shankar2025
  oxidative/mitochondrial; Sommen2026 terminal-NK; Raijmakers2025 RANTES across two triggers) but
  **not** at shared analytes; a pathway-rank concordance is the level at which the project's own
  evidence predicts a signal, if one exists.
- **Live competing expectation:** the concordance is **driven by past-*Coxiella*-exposure** rather
  than fatigue (it reproduces in QS-vs-HC and/or fails QFS-vs-QS) — `discussion:0002`/Raijmakers2019
  explicitly warn the QFS mito-peptide signal is **not fatigue-specific** (asymptomatic seropositive
  controls share it). This is a genuinely competitive outcome, not a strawman.
- **Magnitude humility:** with 2 cohorts, platform heterogeneity, and compartment mismatch, even a
  clean positive is **suggestive only**; we pre-commit *not* to read a narrow nominal GSEA/permutation
  p as strong evidence (most error here is **bias**, which the permutation budget does not shrink).

## Decision Criteria

The verdict label is produced **mechanically** from the rule below (no post-hoc selection). Labels,
and the belief update each licenses on the commitment targets:

| Verdict label | Trigger | Update on `hypothesis:0001` | Update on `question:0017` |
|---|---|---|---|
| `shared_suggestive` | p_perm < 0.05 **and** QFS-vs-QS specificity holds **and** a theme recurs across ≥2 gene-set DBs | **Moderate positive** (capped at "suggestive — needs ≥3-trigger test") | **Weakens** finite-repertoire-coincidence null |
| `fragile` | p_perm < 0.05 but the concordance theme **does not** recur across ≥2 DBs | Near-zero durable update (unstable signal) | No material update |
| `exposure_confounded` | concordant pathways **fail** QFS-vs-QS specificity and/or reproduce in QS-vs-HC | **Negative** on the interpretation that convergence reflects shared *fatigue* biology | **Strengthens** ascertainment/exposure-sequela account |
| `compartment_confounded` | concordant pathways dominated by monocyte/PBMC cell-type-marker sets | Negative (artifactual convergence) | Strengthens detection-artifact account |
| `null_nonarbitrating` | p_perm ≥ 0.05 | Minimal (power/bias ceiling — cannot exclude a real shared signature) | **No** update — explicitly **not** support for the coincidence null |
| `batch_confounded` / `model_inadequate` | GSE130353 PCA batch-dominated, or limma diagnostics fail | No update (test inadmissible) | No update |

**Support** for `hypothesis:0001` therefore requires the *conjunction*: permutation-significant
concordance **AND** fatigue-specificity (QFS-vs-QS) **AND** DB-robustness. Any single leg failing
caps the verdict below `shared_suggestive`.

## Null Result Plan

- A **`null_nonarbitrating`** result (p_perm ≥ 0.05) means the **test was inadequate**, not that
  `hypothesis:0001` is wrong: 2 cohorts, n=7–10/group, cross-platform, cross-compartment, and a
  per-gene power floor that admits only very large effects. It is recorded as weighted-low evidence
  and feeds `question:0017` as *"existing public data cannot adjudicate"* — **never** as evidence
  *for* the coincidence null (the asymmetry is pre-committed: absence of detectable concordance here
  cannot exclude a real shared signature).
- **Power posture (pilot-grade).** This analysis **can** suggest a direction and calibrate
  pathway-level effect sizes for a future ≥3-trigger design; it **cannot** confirm or refute shared
  mechanism. GSEA on the full ranking is the deliberate trade: per-gene resolution (negligible at
  this n) for pathway-level power.
- **If ambiguous** (e.g. `fragile`, or concordance present but DB-sensitive): report as
  hypothesis-generating, name the specific themes for targeted replication, and do **not** promote
  to `hypothesis:0001`'s evidence base beyond the exploratory weight.

## Suspicious/Unexpected Result Plan

- **"Too good to be true" here = a high ρ with a near-zero p_perm.** Because gene-sets are
  correlated and n is tiny, an implausibly strong concordance most likely signals a **leak or a
  confound**, not biology. Pre-committed checks before accepting any strong positive:
  1. **Permutation-null sanity** — the observed ρ must be compared against the **sample-label**
     permutation histogram (the full limma→GSEA chain re-run under permuted labels), **not** a
     gene-shuffle; confirm the null is well-formed (centered near 0, plausible spread).
  2. **Cell-type-marker leak** — inspect whether top concordant sets are monocyte/PBMC compartment
     markers (→ `compartment_confounded`), which would manufacture concordance from the shared
     myeloid signal rather than fatigue biology.
  3. **Exposure leak** — confirm the signal survives QFS-vs-QS and is **not** mirrored in QS-vs-HC
     (→ `exposure_confounded`).
  4. **Single-set dominance** — confirm the rank concordance is not driven by 1–2 extreme-|NES|
     sets; the **theme-recurrence (≥2 DB)** requirement is the guard, and the NES scatter is reported.
- A strong positive surviving all four is still labelled **suggestive**, never confirmatory.

## Known Limitations

Even executed perfectly, this analysis cannot:

1. Confirm a shared mechanism — **2 cohorts** cap it at exploratory; the null is non-arbitrating.
2. Compare expression directly — **platform heterogeneity** (U133A/B microarray vs MMSEQ RNA-seq)
   restricts the comparison to the **pathway-enrichment layer**; no expression-matrix merge.
3. Cleanly separate compartment from disease — **PBMC vs isolated monocytes**; shared signal is
   scoped to monocyte-inclusive pathways, with cell-type-marker leakage a named veto.
4. Adjust for sex — GSE14577 male-only, GSE130353 sex unreported (unmeasured, unadjustable).
5. Use count-based inference — **MMSEQ estimates ≠ counts** → continuous limma only.
6. Make absolute-scale/magnitude claims — depositor normalization inherited (raw-CEL reprocessing
   deferred); defensible because the estimand is a within-dataset GSEA **rank**, invariant to
   monotone per-sample normalization, but it bounds claims to rank/enrichment only.
7. Speak to the project's other named triggers — **post-dengue and post-SARS omics are absent**
   (`question:0001` gap audit); this pair covers post-viral CFS + Q-fever only.

## Metric Selection Rationale

- **Primary metric (locked): Spearman ρ of NES across the full shared testable gene-set universe**
  between PI-CFS-vs-HC and QFS-vs-HC, with significance from a **sample-label permutation null**
  (permute group labels *within each dataset independently*, re-run the entire limma→GSEA→NES→ρ
  chain; one-sided p_perm = fraction of permuted ρ ≥ observed; **B ≥ 2000**, or **exhaustive** where
  feasible — C(15,8)=6435 is exhaustible; C(20,10)=184,756 is Monte-Carlo).
- **Why this, not Fisher's exact (the change from the prior draft):** the original framing scored
  overlap with **Fisher's exact over FDR-passing gene-sets**. MSigDB sets **share genes**, so Fisher
  treats correlated pathways as independent draws — its independence assumption is violated and it is
  **anti-conservative**. The sample-label permutation null **preserves** the gene-set correlation
  structure and the tested-set size, so it calibrates the "above-chance" claim correctly. This is a
  **calibration** fix, not a variance reduction — the permutation budget B only sharpens the
  Monte-Carlo estimate of an already-correct null; it buys no independent-unit information.
- **Demoted to descriptive (never verdict-bearing):** count/identity of FDR<0.05 direction-concordant
  sets, their Jaccard, and the Fisher statistic — reported for interpretability only.
- **Known limitation of ρ:** a global rank concordance can be driven by a few high-|NES| sets;
  mitigated by the **theme-recurrence (≥2 DB)** requirement and by reporting the NES scatter.
- **Pinned gene-set universe (locked):** MSigDB **`2024.1.Hs`** (release pinned; exact release hash
  recorded at ingest), **size filter `15 ≤ |set| ≤ 500`** (fgsea minSize/maxSize). Collections:
  **Hallmark (H, 50 sets) = primary/confirmatory**; **Reactome (C2:CP:REACTOME)** and **GO-BP
  (C5:GO:BP)** = **DB sensitivities**. A **pre-registered keyword→theme map** collapses enriched sets
  into themes {innate/IFN, oxidative-stress, mitochondrial/OXPHOS, apoptosis, adaptive/T-cell,
  other}; a theme is "shared" iff ≥1 set in it is direction-concordant in **both** datasets. The
  keyword→theme table and the pinned release are locked here so the overlap denominator cannot drift
  post-hoc.
- **Specificity metric (locked): direct QFS-vs-QS presence contrast** — a concordant pathway counts
  as fatigue-specific only if it carries **concordant signal in QFS-vs-QS** (fatigue holding
  *Coxiella* exposure constant). **QS-vs-HC** is reframed as **exposure-confounding evidence** (a
  "shared" pathway also enriched in QS-vs-HC is positive evidence of an exposure sequela). This
  replaces the prior "absent-in-QS-vs-HC" veto, which overclaimed specificity from absence-of-evidence
  at n=10.

## Exploratory vs. Confirmatory

- **Confirmatory (pre-registered):**
  - **C1** — NES rank-concordance ρ (PI-CFS-vs-HC × QFS-vs-HC) over pinned Hallmark, p_perm.
- **Mandatory pre-specified sensitivities (the verdict stands only if these run; they arbitrate, not
  multiply):**
  - **S1** — QFS-vs-QS specificity (presence) — the specificity backbone.
  - **S2** — QS-vs-HC exposure check — labels `exposure_sequela`.
  - **S3** — gene-set-DB sensitivity — repeat ρ + permutation null on Reactome and GO-BP; a *theme*
    must recur across ≥2 DBs to count as robust.
  - **S4** — second fatigue contrast — CFS-vs-HC (idiopathic) within GSE130353: does the GSE14577
    concordance hold for QFS only, or also for idiopathic CFS?
- **Exploratory (reported with exploratory weight; cannot change the verdict):**
  - ORA on a top-N / effect-size gene universe (**an empty ORA must never produce `fragile`**).
  - Single-run RMA re-normalization of GSE14577 (the deferred-CEL robustness check).
  - Per-theme leading-edge gene inspection; any contrast or set not named above is **post-hoc** and
    excluded from the verdict.

## Total Comparison Count

| Category | Count | Correction |
|---|---|---|
| Confirmatory test | 1 (C1) | multiplicity-free single primary; significance via sample-label permutation null |
| Mandatory sensitivities | 4 (S1–S4) | interpreted as robustness/arbitration, not multiplicity; each ρ carries its own permutation null |
| Per-contrast limma DE | 5 contrasts (PI-CFS-vs-HC, QFS-vs-HC, CFS-vs-HC, QFS-vs-QS, QS-vs-HC) | BH-FDR **within** each contrast; descriptive tallies only |
| Exploratory | ~3 (ORA, RMA re-norm, leading-edge) | none (exploratory weight) |
| **Total** | **~13** | confirmatory verdict is multiplicity-free; sensitivities/exploratory carry their own (reduced) weight |

## Vehicle-Admissibility Gate (data-gated mode)

**Standing verdict while gated:** `[?] inconclusive-for-coverage` — **no `bears_on` update** on
`hypothesis:0001` or `question:0017` until a provisioned vehicle clears **all** G-gates below **and**
the analysis runs. These G-gates **are** the "Blocking Checks Before Execution" that
`/science:plan-analysis` reports for `plan:0002` (defined once here; referenced there). The plan's
fourth blocking check — *pre-registration lock* — is **discharged by committing this document**.

- **G1 — Acquisition + integrity.** Download GSE14577's SOFT intensity tables (parse from the local
  `family.soft.gz`) **and** GSE130353's **40 per-sample `*.gene.mmseq.txt.gz` files** (or
  `GSE130353_RAW.tar`); record **SHA-256 per file** in the datapackage; flip the registry note from
  "candidate / not yet provisioned" to **provisioned**. Until done, "usable" is *inferred from
  metadata*, not verified.
- **G2 — MMSEQ scale verification (Halt-on).** Open one `*.gene.mmseq.txt.gz`; confirm the
  expression-estimate column and whether it is log-scale posterior mean / FPKM-like; run the universal
  scale check (min/max/integer-like). MMSEQ ≠ counts → **count-based testing (DESeq2/edgeR) is
  inadmissible**; continuous limma only. **Halt if scale is unverifiable.**
- **G3 — Gene-id harmonization.** Resolve U133 probes (GPL96/GPL97) and MMSEQ gene IDs to a **shared
  canonical gene id** (symbols display-only); record mapped/unmapped fractions; the harmonized
  universe must be non-empty and cover the pinned Hallmark genes adequately (log the covered fraction).
- **G4 — Contrast & power-floor admissibility.** Both datasets must yield the required contrasts at
  the metadata-confirmed n: GSE14577 PI-CFS-vs-HC (8 vs 7); GSE130353 QFS-vs-HC, QFS-vs-QS, CFS-vs-HC,
  QS-vs-HC (10 vs 10 each). **The QS group (n≥10) must be present and the QFS-vs-QS contrast
  constructable** — if not, the specificity backbone (S1) fails and the verdict **cannot** reach
  `shared_suggestive` (ceiling drops to `exposure_confounded`-or-below or `null_nonarbitrating`).
  GSE130353 PCA must **not** be batch-dominated (else `batch_confounded`).

A **spent** vehicle that fails any G-gate does not qualify; the standing verdict remains `[?]` until
one does. Tracked by a `status: blocked` task (`task:t035`) whose blocker is this gate.
