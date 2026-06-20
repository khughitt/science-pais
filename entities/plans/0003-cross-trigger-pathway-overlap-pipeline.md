---
id: "plan:0003-cross-trigger-pathway-overlap-pipeline"
type: "plan"
title: "Pipeline design: cross-trigger pathway-overlap Snakemake workflow (t035)"
status: "active"
created: "2026-06-20"
updated: "2026-06-20"
related:
  - "plan:0002-cross-trigger-pathway-overlap-analysis-plan"
  - "pre-registration:0002-cross-trigger-pathway-overlap"
  - "hypothesis:0001-shared-dysregulated-attractor"
  - "question:0001-shared-molecular-signature-across-triggers"
  - "question:0017-deflationary-alternatives-vs-shared-pathophysiology"
  - "task:t035"
  - "task:t037"
  - "paper:Gow2009"
  - "paper:Raijmakers2019"
---

# Pipeline design: cross-trigger pathway-overlap Snakemake workflow (t035)

## Purpose

Turn the **settled** methodology of `plan:0002-cross-trigger-pathway-overlap-analysis-plan` and the
**locked** decision rule of `pre-registration:0002-cross-trigger-pathway-overlap` into a reproducible,
QA-gated Snakemake workflow that runs **raw GEO payloads → single mechanical verdict label**. This is
an *orchestration* design only: it does **not** re-decide the estimand, the primary metric, the
specificity logic, the gene-set universe, or the verdict thresholds — those are frozen upstream and are
encoded verbatim in one `config.yaml`. Guiding principle: **the pipeline is a faithful executor of the
pre-registration; every locked parameter has exactly one home (the config), and the code reads it.**

Methodological readiness is already discharged (`plan:0002`, verdict `ready-with-caveats`) and the
vehicle-admissibility gates G1/G2/G4 are **cleared** (data provisioned + hashed; MMSEQ scale =
`log_mu`; groups 10/10/10/10). G3 (gene-id harmonization) is the one remaining gate and becomes a
first-class pipeline stage here.

## Scope decomposition

**In scope:** the Snakemake DAG under `code/workflows/`; reproducible acquisition (download as a rule
with checksum verification); G3 harmonization; wired QA checkpoints (the `t037` build-fatal /
two-severity discipline); per-dataset limma → fgsea → NES rank-concordance → sample-label permutation
null → specificity → theme roll-up → DB-robustness → compartment check → mechanical verdict; a results
report feeding `q0001`/`h0001`/`q0017`.

**In scope (provenance):** a **minimal Frictionless `datapackage.json`** descriptor for the acquired
payloads (resource list + per-file SHA-256 + source URL + the locked MMSEQ/SOFT scale facts), emitted by
the acquisition rule. This is the artifact `pre-registration:0002` G1 names ("record SHA-256 per file in
the datapackage"); producing it discharges G1 literally rather than leaning on the registry note alone.

**Out of scope (deferred, with reason):**
- Formal `mixin-dataset-1.0` **commons entities** (validated, promotable dataset entities) → deferred to
  commons-promotion (the minimal `datapackage.json` above + the registry note are the interim provenance;
  project tooling does not support stub dataset entities). Note the split: the **datapackage** is in
  scope (WP1, satisfies G1); the **formal entity** is deferred — these are two different artifacts that
  the prior wording conflated.
- The `≥3-trigger` harmonized test and any absolute-scale/magnitude claim → out of scope by the
  pre-reg (exploratory ceiling; rank-only estimand).
- RMA re-normalization from GSE14577 CELs and MMSEQ `sd`-precision-weighting → **optional robustness
  rules**, not on the primary path (see Key decision 8).
- post-dengue / post-SARS triggers → no usable substrate (`q0001` gap audit).

## Architecture

```
code/
  workflows/
    Snakefile                     NEW  thin: includes rules/*.smk, defines `rule all`
    config.yaml                   NEW  SINGLE encoding of the locked pre-reg params (release pin,
                                       size filter, keyword→theme map, marker regex, B, seed,
                                       thresholds, verdict resolution order, near-zero log_mu filter
                                       τ/min_donors, U133A∪B combine rule, hallmark_coverage_warn,
                                       RNG kind + float precision for determinism)
    rules/
      acquire.smk                 NEW  download(+checksum), parse_gse14577, extract_gse130353,
                                       emit_datapackage (minimal Frictionless descriptor)
      qa.smk                      NEW  structural (build-fatal) + distribution (surfaced) checkpoints
      harmonize.smk               NEW  G3: probe/ENSG → canonical Ensembl; coverage report
      prepare.smk                 NEW  probe→gene collapse, near-zero filter, geneset prep
      enrich.smk                  NEW  limma per contrast; fgsea per (contrast × DB)
      verdict.smk                 NEW  concordance, permutation null, specificity, rollup, verdict
    envs/
      r-bioc.yaml                 NEW  conda: r-base, bioconductor-limma, -fgsea, -msigdbr,
                                       -org.Hs.eg.db, -annotationdbi, hgu133a.db, hgu133b.db
      py.yaml                     NEW  conda: python, pandas, pyarrow, numpy, scipy, pyyaml
  scripts/
    g1_acquire.py                 MODIFY  split into rule-callable modules (keep as the seed)
    parse_gse14577.py             NEW  SOFT → per-platform probe×sample matrices + metadata
    extract_gse130353.py          NEW  untar → per-donor log_mu matrix + sample_sheet (subject_status)
    emit_datapackage.py           NEW  minimal Frictionless datapackage.json (resources+SHA-256+source)
    qa_checkpoint.py              NEW  generic two-severity checkpoint (config-driven thresholds)
    harmonize_geneids.py          NEW  G3 mapping + mapped/unmapped + Hallmark-coverage
    collapse_probes.R             NEW  probe→gene median collapse; U133A∪B per patient
    prepare_genesets.R            NEW  pin MSigDB release; size filter; emit gene-set list + theme map join
    limma_de.R                    NEW  one contrast → moderated-t ranked gene list
    fgsea_enrich.R                NEW  one (rank × DB) → NES table
    permutation_null.R            NEW  paired sample-label permutation null → observed ρ + p_perm (HEAVY)
    specificity.py                NEW  S1/S2 per-set classes from QFS-vs-QS + QS-vs-HC fgsea
    theme_rollup.py               NEW  concordance-carrying sets → strict-dominance theme classes
    verdict.py                    NEW  resolution order → single label + results markdown
  notebooks/                      UNCHANGED
data/                             UNCHANGED  (gitignored payloads; processed/ holds rule outputs +
                                             datapackage.json provenance descriptor)
results/                          (DAG writes qa_report.md, verdict.json, figures, results md here)
```

**Data-flow DAG (logical):**

```
download_gse130353 ─┐
                    ├─ extract_gse130353 ─ qa_raw[130353] ─┐
(GSE130353_RAW.tar) ┘                                      │
                                                           ├─ harmonize(G3) ─ prepare ─┐
parse_gse14577 ───────────────── qa_raw[14577] ───────────┘                           │
(local family.soft.gz)                                                                 │
                                                                                       ▼
prepare_genesets (pinned MSigDB) ──────────────────────────────────────────────► limma[contrast]
                                                                                       │
                                            (5 contrasts × 3 DBs)                       ▼
                                                                                   fgsea[contrast×DB]
                                                                                       │
        ┌──────────────────────────────────────────────────────────────────────────┬─┴───────────┐
        ▼                                   ▼                                        ▼             ▼
 concordance[pair×DB]              permutation_null[pair×DB]                  specificity      compartment
 (ρ per pair×DB)                   (p_perm, paired label null, per pair×DB)   (S1/S2 classes)  (marker 50%)
 pair ∈ {primary:PI-CFS×QFS,       — C1 = primary×Hallmark (confirmatory);
         S4:PI-CFS×CFS}              Reactome/GO-BP primary = S3; S4 rows = S4 sensitivity
 DB   ∈ {Hallmark,Reactome,GO-BP}
        └──────────────┬────────────────────┴───────────────┬────────────────────┴──────────────┘
                       ▼                                     ▼
                 theme_rollup (strict-dominance) ─ db_robustness (sign-consistent ≥2 DB, per-DB ρ+p_perm)
                       └────────────────────────────► verdict (resolution order → 1 label) ─► results md
```

## Key decisions

### Key decision 1: Snakemake orchestrator, R+Python split by capability
- **Chosen approach:** Snakemake drives; DE/enrichment rules call **R/Bioconductor** (limma, fgsea,
  msigdbr, annotation `.db` packages); acquisition, QA, harmonization, specificity, roll-up, and
  verdict are **Python**.
- **Rejected alternative:** pure-R or pure-Python pipeline.
- **Reason:** limma's empirical-Bayes moderated-t and fgsea have no Python equivalent worth the
  small-n risk, while glue/QA/verdict logic is clearer and more testable in Python; Snakemake's
  `conda:` per-rule envs keep the two stacks isolated and reproducible.

### Key decision 2: permutation null as one heavy R rule, parameterized over (concordance-pair × DB)
- **Chosen approach:** `permutation_null.R` loads both prepared datasets + the pinned gene sets, draws
  `B` **paired** label permutations (GSE14577 PI-CFS/HC pool **and** GSE130353 QFS/HC pool permuted
  **independently**, seeded), reruns the full limma→fgsea→NES→ρ chain internally, and emits the null ρ
  distribution + one-sided `p_perm`. It is **parameterized by the gene-set DB and the concordance pair**,
  so Snakemake instantiates it once per `(pair × DB)` cell: pairs = {primary `PI-CFS-vs-HC × QFS-vs-HC`,
  S4 `PI-CFS-vs-HC × CFS-vs-HC`} × DBs = {Hallmark, Reactome, GO-BP}. **`(primary × Hallmark)` is the
  confirmatory C1**; the `(primary × Reactome)` and `(primary × GO-BP)` cells are the **S3** DB-sensitivity
  nulls; the S4 rows are the **S4** second-fatigue nulls — matching the pre-reg's "each sensitivity ρ
  carries its own permutation null." Parallelized with `BiocParallel`; one master seed fans out into
  per-`(pair×DB)` substreams (see Key decision 10) so each cell is independently reproducible.
- **Rejected alternative (a):** Snakemake-level fan-out of `B≥2000` jobs **per cell** — process-spawn
  overhead and scheduler thrash dwarf the per-permutation compute (seconds each); the inner loop stays
  in-process, only the `(pair×DB)` cells are Snakemake-level.
- **Rejected alternative (b):** compute the null for Hallmark only and reuse it for Reactome/GO-BP — the
  pre-reg's S3 requires an **independent ρ + null per DB** (different gene-set universe → different null);
  reuse would fabricate the sensitivity.
- **Rejected alternative (c):** gene-label shuffle — the pre-reg explicitly forbids it (does not
  preserve gene-set correlation structure; anti-conservative).
- **Reason:** the pre-reg's null *is* the full-chain re-run under permuted **sample** labels, and S3/S4
  each demand their own ρ+null; one parameterized rule over `(pair×DB)` is the faithful, efficient
  encoding (6 cells, each an in-process parallel loop).

### Key decision 3: QA checkpoints are DAG-gating sentinel rules (t037 discipline)
- **Chosen approach:** each processed substrate gets a `qa_checkpoint.py` invocation that re-reads the
  built table and writes a markdown report **plus** a tiny `*.qa.pass` sentinel. **Structural**
  failures (missing donor key, wrong group codes, unresolved gene id, row/col count mismatch) exit
  non-zero → the sentinel is not written → the DAG **halts**. **Distribution** issues (log-scale
  range, % missing, gene-universe size, batch-PC variance) are written to the report and a
  `warnings` field but are **not** build-fatal. Downstream rules depend on the **sentinel**, not the
  report.
- **Rejected alternative (a):** declare `qa_report.md` as the strict rule's output — Snakemake's
  failed-job cleanup would delete the very evidence of failure.
- **Rejected alternative (b):** a side-output counts file as the QA artifact — explicitly *does not
  satisfy* the checkpoint convention (`pipeline-qa-checkpoints.md`).
- **Reason:** matches the `t037` two-severity convention exactly; the sentinel makes structural QA a
  hard DAG dependency while keeping distribution QA informative-not-fatal.

### Key decision 4: one `config.yaml` is the sole encoding of the locked pre-reg parameters
- **Chosen approach:** the pinned MSigDB release + hash, the `15 ≤ |set| ≤ 500` filter, the
  keyword→theme regex map, the compartment-marker regex, the permutation `B` + master seed, the
  nominal-p / FDR thresholds, the verdict resolution order, **and every verdict-affecting preprocessing
  choice** — the near-zero `log_mu` filter (`τ`, min-donor count, contrast-blind scope), the U133A∪B
  dual-chip combine rule, and the G3 Hallmark-coverage warn threshold — all live in `config.yaml`, which
  cites `pre-registration:0002` as their source of truth. Scripts read them; nothing is hard-coded, and
  **nothing verdict-affecting is chosen during a run** (see Key decisions 9–10).
- **Rejected alternative:** thresholds/regexes embedded per-script.
- **Reason:** the pre-reg is the lock; a single config mirroring it prevents drift and makes any future
  change a visible, reviewable diff that must be reconciled with a pre-reg amendment.

### Key decision 5: canonical gene axis = Ensembl gene ID (G3)
- **Chosen approach:** harmonize both sides to **Ensembl gene IDs**. GSE130353 `feature_id` is already
  `ENSG` (release 68) — lift to the current Ensembl build via a static map (drop/track retired IDs).
  GSE14577 U133A/B probes → Ensembl via `hgu133a.db`/`hgu133b.db`. Symbols are display-only.
- **Rejected alternative:** harmonize on HGNC symbol.
- **Reason:** symbols are unstable and many-to-many; both inputs already resolve cleanly to Ensembl
  (G2/G4 confirmed `ENSG`), so Ensembl minimizes mapping loss. The harmonization rule emits
  mapped/unmapped fractions and **Hallmark-gene coverage**, which the QA checkpoint gates.

### Key decision 6: never merge expression across datasets (enrichment-layer comparison only)
- **Chosen approach:** the two datasets are processed on independent branches; they meet **only** at
  the NES level (concordance/permutation). No probe/gene expression matrix is ever concatenated.
- **Rejected alternative:** ComBat/batch-correct + pooled matrix.
- **Reason:** platform (microarray vs MMSEQ) × compartment (PBMC vs monocyte) confounds make a merged
  matrix indefensible; already locked in `plan:0002` (strategy-1 within-dataset → aggregate).

### Key decision 7: MSigDB via pinned `msigdbr` release, hash recorded
- **Chosen approach:** `prepare_genesets.R` pins `msigdbr` to the release in config (default
  `2024.1.Hs`), applies the size filter, and writes the gene-set list + a recorded release hash as a
  build artifact.
- **Rejected alternative:** live MSigDB download at run time.
- **Reason:** reproducibility — the overlap denominator must not drift between runs; the pin + hash
  make the universe a fixed, audited input.

### Key decision 8: GSE14577 uses deposited log2; CEL re-RMA and MMSEQ `sd`-weighting are optional rules
- **Chosen approach:** the primary path uses the deposited GSE14577 log2 intensities and unweighted
  limma on GSE130353 `log_mu`. RMA-from-CEL and `sd`-derived precision weights are **separate,
  off-primary robustness rules** toggled in config.
- **Rejected alternative:** make re-RMA / precision-weighting mandatory on the primary path.
- **Reason:** the estimand is a within-dataset GSEA **rank**, invariant to monotone normalization and
  largely insensitive to mild precision-weighting; the pre-reg bounds claims accordingly and holds
  these as optional sensitivities, so they must not gate the primary verdict.

### Key decision 9: verdict-affecting preprocessing is locked in config, by contrast-blind rule (not picked at runtime)
- **Chosen approach:** the two preprocessing choices that alter ranked gene lists — and therefore
  fgsea/NES and the verdict — are **pre-committed in `config.yaml` now**, each as a rule that is **blind
  to the contrast/group labels** so it cannot leak group differences into the ranking:
  - **Near-zero `log_mu` filter (GSE130353).** Retain gene *g* iff `#{donors : log_mu(g) > τ} ≥
    min_donors`, with `τ = -7.0` (natural-log) and `min_donors = 10`, computed on the **pooled 40-donor
    cohort, contrast-blind**. Rationale (pre-data, structural): the unexpressed mode sits at
    `log_mu ≈ −14`; `τ = −7.0` is a fixed floor well above it (`exp(−7) ≈ 9×10⁻⁴` of the expressed
    scale), and `min_donors = 10` = one full group, so a gene expressed in **any single** group survives
    (no bias toward cross-group-shared genes). A WP3/WP4 **structural-QA** check confirms the global
    `log_mu` density is bimodal with its antimode **below** `τ`; if the antimode is above `τ`, that is a
    surfaced distribution-severity warning — **not** a license to retune `τ` mid-run.
  - **U133A∪B dual-chip combine (GSE14577).** For a gene mapping from both GPL96 and GPL97, the
    per-patient value = **mean of the two platform-level median-collapsed log2 values**; single-chip
    genes pass through. The count of dual-chip genes is logged in `cohort_audit.json`.
- **Rejected alternative:** "pick `τ` from the per-gene distribution at WP4" / "decide the combine rule
  during preprocessing" — choosing a ranked-list-altering parameter *after seeing the run* is exactly the
  post-hoc latitude pre-registration exists to remove; even a group-blind marginal can drift if it is
  selected rather than pre-committed.
- **Reason:** these are the only two preprocessing knobs that move the NES ranking; fixing them as
  blind rules with concrete values keeps the verdict a function of the data alone, and any future change
  is a visible config diff requiring a pre-reg amendment.

### Key decision 10: explicit determinism contract for byte-identical `verdict.json`
- **Chosen approach:** reproducibility is engineered, not hoped for. (1) **RNG:** a single master `seed`
  in config; R uses `RNGkind("L'Ecuyer-CMRG")` with `BiocParallel` `bpparam(RNGseed=seed)` so each
  `(pair×DB)` permutation cell and each worker draws an independent, fixed substream; Python uses
  `numpy.random.default_rng(seed)`. (2) **Stable ordering:** every NES / gene-set / theme table is sorted
  by a deterministic key (gene-set name, then contrast) before any reduction or serialization; ties
  broken by name — no reliance on hash/iteration order. (3) **Fixed serialization:** `verdict.json` is
  written with sorted keys, fixed float formatting (round to a config'd decimal precision), `ensure_ascii`,
  and LF newlines; **no timestamps or host/path strings** in `verdict.json` (run-time provenance goes to a
  separate `run_metadata.json` sidecar that is *not* the determinism target).
- **Rejected alternative:** rely on a top-level `set.seed()` + default serialization — under
  `BiocParallel` the worker RNG streams are not reproducible without `L'Ecuyer-CMRG`, and unsorted
  float/dict serialization yields spurious diffs; the criterion would fail intermittently despite a valid
  analysis.
- **Reason:** the "byte-identical `verdict.json`" acceptance criterion is only meaningful if RNG streams,
  ordering, and serialization are all pinned; this names the three explicitly so the build can assert them.

## Work packages

### WP0 — Workflow skeleton + locked config + conda envs
- **Depends on:** G1/G2/G4 cleared (done).
- **Entry point:** `code/workflows/Snakefile`, `config.yaml`, `envs/*.yaml`.
- **Definition of done:** `snakemake -n` resolves a complete DAG from raw inputs to `results/verdict.json`;
  `config.yaml` contains **every** locked pre-reg parameter with an inline `# pre-registration:0002`
  provenance comment; `snakemake --lint` clean; conda envs solve.

### WP1 — Reproducible acquisition rules
- **Depends on:** WP0.
- **Entry point:** `rules/acquire.smk`, `parse_gse14577.py`, `extract_gse130353.py`, `emit_datapackage.py`.
- **Definition of done:** a `download_gse130353` rule fetches `GSE130353_RAW.tar` and **verifies it
  against the locked SHA-256** (`98e6b07b…`); GSE14577 SOFT fetch rule with its locked hash;
  `parse_gse14577` and `extract_gse130353` reproduce the WP-checked matrices + `sample_sheet.tsv`
  (keyed on `subject_status`, not filenames); `g1_acquire.py` logic is refactored into these modules
  (the one-off curl is retired in favor of the rule); an `emit_datapackage` rule writes a **minimal
  Frictionless `data/processed/datapackage.json`** (one resource per acquired payload with `path`,
  `bytes`, `hash: sha256:…`, and `sources[].path` = the GEO URL), discharging the G1 "record SHA-256 per
  file in the datapackage" requirement. The **formal `mixin-dataset-1.0` commons entity remains
  deferred** to promotion — only the datapackage descriptor is in scope here.

### WP2 — QA checkpoints (structural build-fatal + distribution surfaced)
- **Depends on:** WP1.
- **Entry point:** `rules/qa.smk`, `qa_checkpoint.py`.
- **Definition of done:** `qa_raw[GSE14577]` and `qa_raw[GSE130353]` each emit a `qa_report.md` + a
  `*.qa.pass` sentinel; structural checks (donor-unique key; required group codes
  `{HC,CFS,QFS,QS}`/`{HC,PI-CFS}`; gene-id column present; expected row/col counts) are build-fatal;
  distribution checks (log-scale min/max/median, % missing, gene-universe size) are reported as
  warnings; a deliberately corrupted fixture makes the DAG halt (test).

### WP3 — G3 gene-id harmonization
- **Depends on:** WP2.
- **Entry point:** `rules/harmonize.smk`, `harmonize_geneids.py`.
- **Definition of done:** both datasets carry a canonical `ensembl_gene_id`; the rule writes
  mapped/unmapped fractions and **Hallmark-gene coverage**. QA severity is locked to the pre-reg (G3
  requires only a **non-empty** harmonized universe + coverage **logged**): **build-fatal iff the mapped
  Hallmark set is empty**; coverage below the config'd warn threshold (`hallmark_coverage_warn = 0.90`)
  is **distribution-severity (surfaced, not fatal)**. Retired ENSG (rel68→current) are logged, not
  silently dropped.

### WP4 — Preprocessing (collapse, filter, geneset prep)
- **Depends on:** WP3.
- **Entry point:** `rules/prepare.smk`, `collapse_probes.R`, `prepare_genesets.R`.
- **Definition of done:** GSE14577 probe→gene **median collapse** with U133A∪B combined per patient
  (15 patients, not 30 arrays) using the **locked dual-chip combine rule** (Key decision 9; mean of
  platform-level collapsed log2); GSE130353 near-zero `log_mu` filter applied with the **locked
  contrast-blind rule** (`τ = −7.0`, `min_donors = 10`, pooled 40-donor cohort — Key decision 9; **values
  read from config, not chosen here**), plus the structural-QA antimode-below-`τ` confirmation; the mask
  is logged. `prepare_genesets.R` emits the pinned, size-filtered gene-set list + the joined
  keyword→theme assignment; a `cohort_audit.json` per dataset records every raw→filtered count and
  decision.

### WP5 — DE + enrichment (limma, fgsea across contrasts × DBs)
- **Depends on:** WP4.
- **Entry point:** `rules/enrich.smk`, `limma_de.R`, `fgsea_enrich.R`.
- **Definition of done:** `limma_de.R` produces moderated-t ranked gene lists for the **5 contrasts**
  (`PI-CFS-vs-HC`, `QFS-vs-HC`, `CFS-vs-HC`, `QFS-vs-QS`, `QS-vs-HC`); `fgsea_enrich.R` produces NES
  tables for each contrast × **3 DBs** (Hallmark primary; Reactome, GO-BP sensitivities) using the
  pinned sets + size filter + master seed; all parameterized, no hard-coded thresholds.

### WP6 — Concordance + permutation null (per concordance-pair × DB)
- **Depends on:** WP5.
- **Entry point:** `rules/verdict.smk` (`concordance`, `permutation_null`).
- **Definition of done:** `concordance` writes the observed Spearman ρ + NES scatter for **each
  `(pair × DB)` cell** — pairs {primary `PI-CFS-vs-HC × QFS-vs-HC`, S4 `PI-CFS-vs-HC × CFS-vs-HC`} ×
  DBs {Hallmark, Reactome, GO-BP} = 6 cells; `permutation_null.R` writes `p_perm` for each cell from the
  **paired, independent, sample-label** null (B from config; per-cell seeded substream; null histogram
  emitted). `(primary × Hallmark)` is the confirmatory **C1**; `(primary × Reactome/GO-BP)` are **S3**;
  the S4 rows are **S4**. A small-B smoke config reproduces a deterministic `p_perm` for every cell under
  the fixed seed (test). The S3 cells feed `db_robustness` (WP7); C1 + S4 feed the verdict.

### WP7 — Specificity + theme roll-up + DB-robustness + compartment
- **Depends on:** WP5 (specificity uses QFS-vs-QS, QS-vs-HC fgsea), WP6 (concordance-carrying set needs
  the primary pair; `db_robustness` needs the per-DB ρ + `p_perm` from all three `primary × DB` cells).
- **Entry point:** `rules/verdict.smk` (`specificity`, `theme_rollup`, `db_robustness`, `compartment`).
- **Definition of done:** `specificity.py` computes per-set **S1/S2** classes (same-sign-NES ∧ nominal
  fgsea p<0.05) → `fatigue-specific`/`exposure_sequela`/`unresolved`; `theme_rollup.py` applies the
  **strict-dominance** rule (`#fatigue-specific > #exposure_sequela`); `db_robustness` consumes the
  **per-DB ρ + `p_perm`** (the three `primary × DB` cells from WP6) and the per-DB theme classes, and
  enforces **sign-consistent** theme recurrence in ≥2 of {Hallmark, Reactome, GO-BP} (a theme counts only
  in DBs whose primary ρ is itself directionally consistent); `compartment` applies the locked marker
  regex to the **concordance-carrying set** (≥50% rule). Each reads its definition from config.

### WP8 — Mechanical verdict + report
- **Depends on:** WP6, WP7.
- **Entry point:** `rules/verdict.smk` (`verdict`), `verdict.py`.
- **Definition of done:** `verdict.py` walks the **locked resolution order** (model_inadequate/
  batch → null → compartment → exposure → suggestive → fragile → residual-exposure) and emits exactly
  **one** label to `results/verdict.json` + a results markdown synthesizing into `q0001`/`h0001`/
  `q0017`; the output cites the pre-reg and reproduces its decision-table semantics; a fixtures test
  exercises each label path.

## Open questions

1. **MMSEQ `log_mu` is natural-log; limma input.** Natural-log is a monotone transform → fine for the
   rank estimand, but document it and decide whether to convert to log2 for human-readable diagnostics
   only. *Lean: keep natural-log internally; convert for display.* (Display-only — does not affect the
   verdict, so not a config lock.)
2. **`org.Hs.eg.db`/annotation versions vs MSigDB release.** Pin all annotation `.db` packages in the
   conda env so probe→Ensembl and the gene-set universe come from a coherent build; record versions.
3. **Exhaustive vs Monte-Carlo permutation for the GSE14577 arm.** `C(15,8)=6435` is exhaustible but
   the ρ null is *paired* with the Monte-Carlo GSE130353 arm; default to `B=2000` paired draws, note
   the exhaustive option as a robustness toggle.

*(Resolved into locks, formerly open: the near-zero `log_mu` filter threshold and the U133A∪B combine
rule are now pre-committed in `config.yaml` under Key decision 9 — they alter the NES ranking and so
cannot be left open; see the Architecture note on `config.yaml`.)*

## Non-Goals

- Confirming a shared mechanism, or running the `≥3-trigger` test (exploratory ceiling, by pre-reg).
- Any absolute-scale / fold-magnitude claim (rank-only estimand).
- Count-based inference (DESeq2/edgeR) — inadmissible (G2: estimate is `log_mu`, not counts).
- Cross-dataset expression-matrix merge.
- Formal commons `mixin-dataset-1.0` entities (deferred to promotion). *The minimal Frictionless
  `datapackage.json` is in scope (WP1) — it is a different, lighter artifact.*
- Re-deciding any pre-registered parameter — this plan executes, it does not re-plan.

## Acceptance Criteria

- [ ] `snakemake -n` resolves the full DAG raw → `results/verdict.json`; `snakemake --lint` clean.
- [ ] `config.yaml` encodes **every** locked pre-reg parameter, each with a `# pre-registration:0002`
      provenance comment; no threshold/regex/seed is hard-coded in any script.
- [ ] Acquisition is a rule with **checksum verification** against the locked SHA-256s; the one-off
      `curl` is retired; payloads stay gitignored; a **minimal Frictionless `datapackage.json`**
      (resources + SHA-256 + source URL) is emitted, discharging G1.
- [ ] **No verdict-affecting parameter is chosen at runtime**: the near-zero `log_mu` filter
      (`τ=−7.0`, `min_donors=10`, contrast-blind), the U133A∪B combine rule, and the G3 coverage warn
      threshold are all in `config.yaml`; WP4 reads them rather than picking from the distribution.
- [ ] Every processed substrate has a **structural (build-fatal) + distribution (surfaced)** QA
      checkpoint with a `*.qa.pass` sentinel; a corrupted fixture halts the DAG; `qa_report.md` is
      never the strict rule's declared output.
- [ ] G3 harmonization emits mapped/unmapped + Hallmark coverage and gates on it.
- [ ] The permutation null is the **paired, independent, sample-label** null (not gene-shuffle), seeded
      and reproducible, and is computed **per `(concordance-pair × DB)` cell** — C1 (`primary×Hallmark`),
      S3 (`primary×{Reactome,GO-BP}`), and S4 (`PI-CFS×CFS × {3 DBs}`) each carry their own ρ + `p_perm`;
      the verdict is emitted by the **locked resolution order** as exactly one label.
- [ ] Re-running `--use-conda` from clean produces a byte-identical `verdict.json` under the fixed seed,
      via the **determinism contract** (Key decision 10): `L'Ecuyer-CMRG` substreams under `BiocParallel`,
      stable table ordering, and sorted-key/fixed-precision/timestamp-free serialization.
- [ ] A results markdown lands in `results/` and is wired to `q0001`/`h0001`/`q0017`.

## Notes on reusable infrastructure

`qa_checkpoint.py` (config-driven two-severity structural/distribution checkpoint with sentinel) and the
Snakemake `envs/` (limma+fgsea+annotation Bioconductor stack) are **`reusable: true`** — directly
liftable to any future expression reanalysis in `health-immunity` / `pan-disease`, and a candidate for
commons promotion once the workflow stabilizes.
