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
amendments:
  - date: "2026-06-20"
    ratified_by: "user code review 2026-06-20 (same-day, pre-data)"
    type: "pre-data tightening (not a fresh pre-registration; criteria narrowed/specified, none loosened)"
    change: >
      Five review findings closed, all making the mechanical verdict truly mechanical or fixing
      drift — none observed any data (data-gated, nothing run): (HIGH) the QFS-vs-QS / QS-vs-HC
      specificity leg was not thresholded — now S1-positive ≡ same-sign-NES-as-QFS-vs-HC ∧ nominal
      fgsea p<0.05 in QFS-vs-QS, S2-positive ≡ same in QS-vs-HC, with mechanical per-set classes
      (fatigue-specific / exposure_sequela / unresolved-specificity) and a theme roll-up (nominal p,
      not FDR, justified by the small pre-nominated set + n=10 power floor). (HIGH) the
      keyword→theme map was named but absent — now an explicit Locked theme map (six case-insensitive
      regexes + first-match precedence) plus a locked cell-type-marker regex for compartment_confounded.
      (MED) intro said "G1–G3" while the gate defines G1–G4 — reconciled to G1–G4. (MED) the pre-reg
      said "tracked by a status:blocked task" while t035 is active — reworded to keep t035 active
      (G1–G3 are executable now; the gate is dischargeable work, not an external block). (LOW) exact
      permutation label pools now stated per contrast (PI-CFS/HC only for GSE14577; QFS/HC only for the
      primary GSE130353 arm; CFS and QS held out), preventing a "permute all four GSE130353 groups
      together" misread. Also added a locked verdict-resolution order so exactly one label is emitted
      and the p_perm<0.05-but-all-unresolved-specificity fall-through is explicit.
    rationale: >
      The first commit (30edefe) locked the primary (permutation null) and the universe pin but left
      two verdict-bearing legs — the specificity threshold and the theme map — underspecified, which
      would have left room for post-hoc calls at interpretation time. Filling them in before any data
      is observed is the entire point of pre-registration; recording it as an amendment preserves the
      audit trail that they were specified pre-data via independent review, not back-fitted.
  - date: "2026-06-20"
    ratified_by: "user code review 2026-06-20 second pass (same-day, pre-data)"
    type: "pre-data tightening (not a fresh pre-registration; criteria narrowed/specified, none loosened)"
    change: >
      Three findings + one open question from the second review pass closed (still data-gated, nothing
      run): (HIGH) the locked theme-map regexes were inside a Markdown table with escaped pipes (\\|),
      ambiguous if copied verbatim — moved to a fenced YAML block with RAW PCRE alternation and an
      explicit "compile verbatim, case-insensitive, no Markdown unescaping" instruction; the
      cell-type-marker regex likewise. (HIGH) compartment_confounded used the gene-level term
      "leading-edge" and an undefined "sets driving ρ" — replaced by a locked set-level
      *concordance-carrying set* (primary-concordant AND nominal fgsea p<0.05 in BOTH contrasts);
      the 50%-marker rule now runs on that fixed Hallmark set, and fires empty→cannot-fire. (MED)
      DB-robustness did not require cross-DB direction agreement — now a theme "recurs across ≥2 DBs"
      only if fatigue-specific in ≥2 of {Hallmark,Reactome,GO-BP} with the SAME theme-level NES sign
      (theme direction = sign of the largest-|NES| fatigue-specific concordance-carrying set).
      (OPEN Q) the mixed-theme case (one fatigue-specific set overriding exposure evidence) was made
      explicit and tightened: theme roll-up is now STRICT-DOMINANCE — fatigue-specific iff
      (#fatigue-specific sets) > (#exposure_sequela sets); a tie or exposure-majority demotes to
      exposure_sequela. Decision table + resolution order updated to reference these locked terms.
    rationale: >
      Second-pass review caught that "mechanical" was not yet fully mechanical: a copy-paste-ambiguous
      regex, a gene-level term standing in for a set-level rule, a direction-blind robustness check, and
      an under-specified mixed-theme roll-up each still left an interpretation-time judgment call. All
      four are closed pre-data, preserving the no-HARKing audit trail.
  - date: "2026-06-20"
    ratified_by: "pipeline review of plan:0003 (/science:review-pipeline) 2026-06-20 (same-day, pre-data)"
    type: "pre-data tightening (not a fresh pre-registration; verdict-affecting input-handling rules pulled into the pre-reg, none loosened)"
    change: >
      The pipeline-design review (plan:0003) surfaced that several verdict-affecting input-handling
      choices had been drafted only in the pipeline plan/config, not here — leaving the config/code to
      act as the de facto pre-registration. Pulled four such locks into this document, all decided
      pre-data (data-gated, nothing run beyond the G1/G2 scale smoke check): (1) **Near-zero expression
      filter (GSE130353)** is now a locked **contrast-blind procedure**, not a guessed constant — τ is
      the antimode of the pooled, group-blind per-gene log_mu density estimated by a fixed method, and a
      gene is retained iff log_mu > τ in ≥10 donors (one full group, so a gene expressed in any single
      group survives); if the pooled density is **not clearly bimodal**, the pipeline **HALTS** (an
      unjustified automated threshold must not be applied silently) rather than falling back to a fixed
      cut. (2) **U133A∪B dual-chip combine (GSE14577)** = mean of the two platform-level median-collapsed
      log2 values per patient; single-platform genes pass through. (3) **NA / undefined NES handling**:
      a set with NA NES in a contrast is treated as absent — excluded pairwise from ρ, cannot be
      concordance-carrying, cannot be S1/S2-positive; dropped counts reported. (4) **R↔Python intermediate
      table contract**: a fixed NES/permutation schema with explicit NA encoding, so the parse/join is
      unambiguous. This amendment **supersedes the earlier fixed τ = −7.0** that briefly appeared in the
      pipeline plan; that constant rested on an unverified bimodality assumption and is replaced by the
      procedure above.
    rationale: >
      A threshold or NA rule that lives only in config has no committed/amendment provenance and can be
      retuned once results are visible — exactly the latitude pre-registration removes. These four all
      alter the GSEA ranking or verdict eligibility, so they belong here, locked pre-data, with the
      audit trail showing they were fixed before any DE/fgsea/concordance was computed. The fixed-τ→
      procedure change is a strengthening: a contrast-blind data-adaptive rule is both outcome-blind and
      robust to the actual distribution, and the halt-if-not-bimodal guard refuses to auto-threshold a
      distribution that does not justify it.
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
> blocking check (pre-registration lock)**; the plan's remaining three checks are encoded as
> **G1–G3** below, plus a contrast/power-floor admissibility gate **G4** (so the gate defines
> **G1–G4**).

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
| `shared_suggestive` | p_perm < 0.05 **and** ≥1 **fatigue-specific theme** (strict-dominance roll-up; see *Metric Selection Rationale*) that satisfies **direction-consistent DB-robustness** (fatigue-specific with matching NES sign in ≥2 of {Hallmark, Reactome, GO-BP}) | **Moderate positive** (capped at "suggestive — needs ≥3-trigger test") | **Weakens** finite-repertoire-coincidence null |
| `fragile` | p_perm < 0.05 **and** ≥1 fatigue-specific theme, but **none** satisfies direction-consistent DB-robustness | Near-zero durable update (unstable signal) | No material update |
| `exposure_confounded` | p_perm < 0.05 **and no** primary-concordant theme is fatigue-specific, **and** ≥1 concordant theme is **exposure_sequela** (S2-positive) | **Negative** on the interpretation that convergence reflects shared *fatigue* biology | **Strengthens** ascertainment/exposure-sequela account |
| `compartment_confounded` | concordant pathways dominated by monocyte/PBMC cell-type-marker sets | Negative (artifactual convergence) | Strengthens detection-artifact account |
| `null_nonarbitrating` | p_perm ≥ 0.05 | Minimal (power/bias ceiling — cannot exclude a real shared signature) | **No** update — explicitly **not** support for the coincidence null |
| `batch_confounded` / `model_inadequate` | GSE130353 PCA batch-dominated, or limma diagnostics fail | No update (test inadmissible) | No update |

**Support** for `hypothesis:0001` therefore requires the *conjunction*: permutation-significant
concordance **AND** fatigue-specificity (QFS-vs-QS) **AND** DB-robustness. Any single leg failing
caps the verdict below `shared_suggestive`.

**Verdict resolution order (locked — exactly one label is emitted).** Labels are not mutually
exclusive by construction, so they are evaluated in this fixed priority and the **first** match is the
verdict:

1. **`model_inadequate` / `batch_confounded`** — admissibility first: if Hallmark-primary limma
   diagnostics fail or GSE130353 PCA is batch-dominated (G4), the test is inadmissible; stop.
2. **`null_nonarbitrating`** — else if **p_perm ≥ 0.05**.
3. **`compartment_confounded`** — else if **≥50% of the Hallmark concordance-carrying sets** (locked
   set-level definition above) are **compartment markers** by the locked marker regex.
4. **`exposure_confounded`** — else if **no** theme is fatigue-specific **and** ≥1 theme is
   `exposure_sequela` (strict-dominance roll-up).
5. **`shared_suggestive`** — else if ≥1 fatigue-specific theme satisfies **direction-consistent
   DB-robustness** (≥2 of {Hallmark, Reactome, GO-BP}, matching NES sign).
6. **`fragile`** — else if ≥1 fatigue-specific theme but **none** satisfies direction-consistent
   DB-robustness.
7. **`exposure_confounded` (residual)** — else (p_perm<0.05 but **all** concordant themes are
   *unresolved-specificity*: no fatigue-specific and no exposure_sequela theme). Rationale: a
   permutation-significant concordance with **no** demonstrable fatigue specificity at this n does
   **not** support `hypothesis:0001`; it is reported as specificity-unresolved and carries the same
   (negative-for-fatigue-specificity) weight, distinguished in prose by an
   `unresolved_specificity` annotation.

This ordering makes the fall-through explicit and guarantees a single mechanical label.

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
  (permute group labels *within each contrast's own two-group sample pool*, re-run the entire
  limma→GSEA→NES→ρ chain; one-sided p_perm = fraction of permuted ρ ≥ observed; **B ≥ 2000**, or
  **exhaustive** where feasible — C(15,8)=6435 is exhaustible; C(20,10)=184,756 is Monte-Carlo).
- **Exact permutation label pools (locked — to prevent "permute all groups together" misreads).**
  Each permutation relabels **only the two groups that define that contrast**; samples outside the
  contrast are **excluded from its pool**, not shuffled in:
  - **GSE14577 PI-CFS-vs-HC** — permute the **15 PI-CFS/HC** sample labels (8 vs 7); pool = C(15,8) = 6435 (exhaustible).
  - **GSE130353 QFS-vs-HC** (primary partner) — permute **only the 20 QFS+HC** labels (10 vs 10); CFS and QS samples are held out; pool = C(20,10) = 184,756 (Monte-Carlo, B ≥ 2000).
  - **S1 QFS-vs-QS** — permute only the **20 QFS+QS** labels. **S2 QS-vs-HC** — permute only the **20 QS+HC** labels. **S4 CFS-vs-HC** — permute only the **20 CFS+HC** labels.
  The primary-ρ null permutes GSE14577 (15) and GSE130353-QFS/HC (20) pools **independently** of each
  other; no GSE130353 four-group joint relabeling is performed at any point.
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
  (C5:GO:BP)** = **DB sensitivities**. The **pre-registered keyword→theme map** that collapses enriched
  sets into themes is the **Locked theme map** block below (explicit case-insensitive regexes +
  first-match precedence — not just theme names). The theme map only *assigns* each set to one theme;
  whether a theme counts toward the verdict is governed by the **concordance-carrying set**,
  **strict-dominance roll-up**, and **direction-consistent DB-robustness** definitions in the
  *Specificity metric* block (not by a loose "≥1 concordant set" rule). The theme map and the pinned
  release are locked here so the overlap denominator cannot drift post-hoc.
- **Locked input preprocessing & NA handling (pre-data, verdict-affecting — 3rd amendment).** These
  alter the GSEA ranking or verdict eligibility, so they are fixed here, not delegated to config:
  - **Near-zero expression filter (GSE130353), contrast-blind procedure — NOT a fixed constant.**
    Compute the **pooled, group-blind** per-gene summary (median `log_mu` across all 40 donors) and
    estimate the antimode of its density by a **fixed method** (Gaussian KDE, Silverman bandwidth;
    `τ` = the lowest-density point between the two highest modes — the unexpressed mode near
    `log_mu ≈ −14` and the expressed mode). **Retain gene *g* iff `#{donors : log_mu(g) > τ} ≥ 10`**
    (one full group, so a gene expressed in any single group survives — no bias toward cross-group-shared
    genes). The procedure never sees contrast/group labels. **Halt rule:** if the pooled density is
    **not clearly bimodal** (no interior antimode, or the two modes are not separated, or the antimode
    splits less than a fixed mass fraction), the pipeline **HALTS (structural)** and requires a recorded
    amendment — it must **not** silently fall back to a fixed `τ`. *(This supersedes the fixed `τ = −7.0`
    that briefly appeared in the pipeline plan; that constant assumed a bimodality not yet measured.)*
    GSE14577 array data inherits deposited log2 values; no additional near-zero filter is applied to it.
  - **U133A∪B dual-chip combine (GSE14577), locked.** After probe→Ensembl harmonization and
    within-platform median collapse, a gene present on **both** GPL96 and GPL97 takes the **mean of its
    two platform-level collapsed log2 values** per patient (15 patients, not 30 arrays); single-platform
    genes pass through unchanged. The count of dual-chip genes is logged.
  - **NA / undefined NES handling, locked.** A gene-set whose fgsea **NES is NA/undefined** in a given
    contrast (too few of its genes survive into that contrast's ranked universe) is treated as **absent**
    for every downstream rule: **excluded pairwise** from the Spearman ρ of any pair in which either
    contrast's NES is NA; **cannot** be a concordance-carrying set; **cannot** be S1- or S2-positive. The
    per-`(contrast × DB)` count of NA-dropped sets is reported. (An empty concordance-carrying set →
    `compartment_confounded` cannot fire, as already locked, and the set contributes nothing to the
    strict-dominance roll-up.)
  - **R↔Python intermediate table contract, locked.** NES tables crossing the R→Python boundary carry
    columns `{gene_set, db, contrast, NES, pval, padj, size}` (one row per `gene_set × contrast × DB`,
    **NA encoded as empty/`NA`, never `0`**); permutation outputs carry `{pair, db, rho_obs, p_perm, B}`.
    Spearman ρ and all set-level classes are computed from these columns only, so the parse, the join
    key (`gene_set` exact-match within a `db`), and the NA rule above are unambiguous.
- **Specificity metric (locked, fully thresholded): direct QFS-vs-QS presence contrast.** "Signal"
  is **not** left to interpretation. For every gene-set that is **primary-concordant** (same-sign NES
  in *both* PI-CFS-vs-HC and QFS-vs-HC), evaluate two **presence predicates** using the *same* pinned
  gene-set universe and fgsea run, against the set's QFS-vs-HC NES direction:
  - **S1-positive (fatigue presence in QFS-vs-QS)** ≡ in the **QFS-vs-QS** contrast the set has
    **same-sign NES as its QFS-vs-HC direction** **AND** **nominal fgsea p < 0.05**.
  - **S2-positive (exposure presence in QS-vs-HC)** ≡ in the **QS-vs-HC** contrast the set has
    **same-sign NES as its QFS-vs-HC direction** **AND** **nominal fgsea p < 0.05**.

  **Why nominal p, not FDR, and why a sign requirement:** these are **presence tests on a small,
  pre-nominated set** (the primary-concordant pathways), not a genome-wide screen — at n=10 vs 10 an
  FDR floor would be empty for the same power reason ORA was demoted, falsely sinking everything to
  `exposure_confounded`. The **same-sign-NES** requirement is the direction lock that a bare p-value
  lacks; nominal p<0.05 is the presence floor. (Rank-percentile and effect-size floors were considered
  and rejected as less standard than fgsea's own p; this choice is locked, not adjudicated post-hoc.)

  **Concordance-carrying set (locked, set-level — replaces the gene-level "leading-edge" term).**
  Within one DB, the **concordance-carrying sets** are the primary-concordant sets (same-sign NES in
  *both* PI-CFS-vs-HC and QFS-vs-HC) that are **nominally significant (fgsea p < 0.05) in both**
  contrasts. This is a well-defined **set list** (not a gene-level leading-edge); it is the
  denominator for the `compartment_confounded` 50%-marker rule and the substrate for theme roll-up. If
  the concordance-carrying list is empty, `compartment_confounded` cannot fire (no sets to be
  marker-dominated) and the verdict proceeds to the specificity/DB steps.

  **Per-set specificity class (mechanical):** evaluated on the **concordance-carrying sets**.
  - **fatigue-specific** ≡ **S1-positive AND NOT S2-positive** (present where fatigue differs holding
    exposure constant; *absent* in exposure-without-fatigue).
  - **exposure_sequela** ≡ **S2-positive** (present in QS-vs-HC; tracks *Coxiella* exposure) —
    regardless of S1.
  - **unresolved-specificity** ≡ neither S1-positive nor S2-positive (no presence either way at this n).

  **Theme-level NES direction (locked):** a theme's **direction** in a given DB is the **sign of the
  QFS-vs-HC NES of its fatigue-specific concordance-carrying set with the largest |NES|** (the
  representative set). This single locked rule makes the theme's sign well-defined for the cross-DB
  direction check below.

  **Theme roll-up (mechanical — dominance rule, resolves the mixed-theme case).** Within a DB, count a
  theme's concordance-carrying sets by class:
  - **fatigue-specific theme** ≡ **(# fatigue-specific sets) > (# exposure_sequela sets)** in the
    theme (fatigue evidence strictly dominates; a single spurious nominal QS-vs-HC hit cannot by
    itself sink a theme, and a single fatigue-specific hit cannot by itself rescue an
    exposure-dominated theme).
  - **exposure_sequela theme** ≡ **(# exposure_sequela sets) ≥ (# fatigue-specific sets)** and ≥1
    exposure_sequela set.
  - **unresolved theme** ≡ no fatigue-specific and no exposure_sequela set.

  This **strict-dominance** choice is the explicit answer to "can a mixed theme still carry
  `shared_suggestive`?": **only if fatigue-specific sets strictly outnumber exposure_sequela sets**
  within it — a tie or exposure-majority demotes it to `exposure_sequela`. It replaces both the prior
  "absent-in-QS-vs-HC" veto (too strict) and the prior "≥1 fatigue-specific set wins" roll-up (too
  lenient — it let one set override any amount of exposure evidence).

- **DB-robustness (locked — direction-consistent recurrence).** A fatigue-specific theme **"recurs
  across ≥2 DBs"** (the `shared_suggestive` requirement) **iff it is a fatigue-specific theme in ≥2 of
  the three DBs {Hallmark, Reactome, GO-BP} AND its theme-level NES direction (above) is the *same
  sign* in those ≥2 DBs.** A theme that is fatigue-specific in Hallmark (up) and in Reactome (down)
  does **not** satisfy robustness — opposite-direction "recurrence" is not robust biology, so the
  sign-agreement requirement is part of the lock. (The primary ρ test itself is run on Hallmark; the
  DB-robustness check re-runs the QFS-vs-HC / PI-CFS-vs-HC / QFS-vs-QS / QS-vs-HC contrasts on Reactome
  and GO-BP with the same size filter and permutation procedure, then re-derives concordance-carrying
  sets and theme classes per DB.)

### Locked theme map (keyword→theme, pre-registered)

Each gene-set is assigned to **exactly one** theme by matching its **MSigDB set name** (uppercased,
collection prefix such as `HALLMARK_` / `REACTOME_` / `GOBP_` stripped) against the regexes below,
evaluated **top-to-bottom; first match wins** (precedence is part of the lock, so a set naming both an
energy and an immune term resolves deterministically). Any set matching none falls to **other** and is
ineligible to be a "shared theme" (it can still enter the ρ rank, but cannot *carry* a verdict theme).

The regexes are given **raw** in the fenced block below — they are **PCRE/ERE alternation strings, not
Markdown**. Compile them verbatim with the **case-insensitive** flag (`re.IGNORECASE` / R
`perl=TRUE, ignore.case=TRUE`); the `|` characters are literal alternation operators and `\b` is a
word boundary. **No Markdown unescaping is involved** (the block is not a table, so pipes are not
escaped). `_` is the MSigDB word join and is matched literally.

```yaml
# keyword→theme map — first match wins, evaluated in this exact order; case-insensitive.
# Matched against the MSigDB set name, uppercased, with the collection prefix
# (HALLMARK_/REACTOME_/GOBP_/…) stripped. Strings are raw PCRE — compile verbatim.
- precedence: 1
  theme: mitochondrial/OXPHOS
  regex: 'OXIDATIVE_PHOSPHORYLATION|OXPHOS|MITOCHOND|RESPIRATORY_ELECTRON|ELECTRON_TRANSPORT|RESPIRATORY_CHAIN|\bTCA_CYCLE\b|CITRIC_ACID|ATP_SYNTH|\bCOMPLEX_I\b|FATTY_ACID_BETA_OXID'
- precedence: 2
  theme: oxidative-stress
  regex: 'REACTIVE_OXYGEN|OXIDATIVE_STRESS|\bROS\b|GLUTATHIONE|\bNRF2\b|NFE2L2|PEROXID|\bREDOX\b|SUPEROXIDE|ANTIOXIDANT|DETOXIF'
- precedence: 3
  theme: apoptosis
  regex: 'APOPTOSI|PROGRAMMED_CELL_DEATH|CASPASE|NECROPTOSI|PYROPTOSI|\bBCL2\b|INTRINSIC_APOPTOTIC|EXTRINSIC_APOPTOTIC|DEATH_RECEPTOR'
- precedence: 4
  theme: innate/IFN
  regex: 'INTERFERON|\bIFN\b|INNATE|INFLAMMAT|\bTNFA?\b|\bNFKB\b|NF_KB|TOLL|\bTLR\b|COMPLEMENT|\bIL6\b|JAK_STAT|CYTOKINE|CHEMOKINE|NEUTROPHIL|MONOCYTE|MACROPHAGE|MYELOID|INFLAMMASOME|RIG_I|NOD_LIKE'
- precedence: 5
  theme: adaptive/T-cell
  regex: '\bT_CELL|\bTCR\b|\bCD8\b|\bCD4\b|\bTH1\b|\bTH2\b|\bTH17\b|REGULATORY_T|LYMPHOCYTE|ADAPTIVE_IMMUN|ANTIGEN_PROCESS|\bMHC\b|\bHLA\b|IL2_STAT5|ALLOGRAFT_REJECTION|\bB_CELL|IMMUNOGLOBULIN|GERMINAL_CENTER'
- precedence: 6
  theme: other            # no match above — ineligible to carry a verdict theme
```

Precedence rationale (locked): the mechanistically specific energy/redox/death themes the hypothesis
predicts (1–3) outrank the broader immune themes (4–5), so a set such as
`..._APOPTOTIC_..._MITOCHONDRIAL_...` resolves to **mitochondrial/OXPHOS**, and an oxphos set
incidentally naming "inflammatory" does not leak into **innate/IFN**. The exact regex strings — not
just the theme names — are the locked artifact; changing any term is an amendment, not a runtime
choice.

**Locked cell-type-marker set (for the `compartment_confounded` check, resolution step 3).** A
gene-set is a **compartment marker** iff its prefix-stripped, uppercased name matches this raw
case-insensitive regex (same compile rules as above):

```yaml
compartment_marker_regex: 'MONOCYTE|MACROPHAGE|MYELOID|NEUTROPHIL|GRANULOCYTE|DENDRITIC|\bPBMC\b|LEUKOCYTE|MARKER_|_CELL_SURFACE|CELL_TYPE'
```

The firing rule is **set-level and fixed** (see *Concordance-carrying set*, below): `compartment_confounded`
fires when **≥50% of the concordance-carrying sets** are compartment markers by this regex. It is
evaluated **before** specificity (resolution step 3 precedes steps 4–6) because a marker-dominated
concordance is artifactual regardless of QFS-vs-QS behaviour.

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
one does. Tracked by **`task:t035`, kept `active` (not `blocked`)**: unlike a vehicle blocked on an
external event (e.g. a pending data-access application), G1–G3 are **executable now** — the data is
public, a download away — so the next action is to *discharge* the gate, not wait on it. The task flips
to `done` only once an admissible vehicle clears G1–G4 and the analysis runs.
