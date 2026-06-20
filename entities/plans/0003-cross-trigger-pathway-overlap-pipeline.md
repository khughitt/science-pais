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

**Out of scope (deferred, with reason):**
- Formal `mixin-dataset-1.0` entities + Frictionless datapackages → deferred to commons-promotion
  (the registry note + the G1 SHA-256 manifest are the interim provenance; tooling does not support
  stub dataset entities in this project).
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
                                       thresholds, verdict resolution order)
    rules/
      acquire.smk                 NEW  download(+checksum), parse_gse14577, extract_gse130353
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
data/                             UNCHANGED  (gitignored payloads; processed/ holds rule outputs)
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
 concordance_primary               permutation_null                          specificity      compartment
 (ρ, Hallmark)                     (p_perm, paired label null)               (S1/S2 classes)   (marker 50%)
        └──────────────┬────────────────────┴───────────────┬────────────────────┴──────────────┘
                       ▼                                     ▼
                 theme_rollup (strict-dominance) ─ db_robustness (sign-consistent ≥2 DB)
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

### Key decision 2: permutation null as one heavy R rule with an internal loop
- **Chosen approach:** `permutation_null.R` loads both prepared datasets + the pinned gene sets, draws
  `B` **paired** label permutations (GSE14577 PI-CFS/HC pool **and** GSE130353 QFS/HC pool permuted
  **independently**, seeded), reruns the full limma→fgsea→NES→ρ chain internally, and emits the null ρ
  distribution + one-sided `p_perm`. Parallelized with `BiocParallel`.
- **Rejected alternative (a):** Snakemake-level fan-out of `B≥2000` jobs — process-spawn overhead and
  scheduler thrash dwarf the per-permutation compute (seconds each).
- **Rejected alternative (b):** gene-label shuffle — the pre-reg explicitly forbids it (does not
  preserve gene-set correlation structure; anti-conservative).
- **Reason:** the pre-reg's null *is* the full-chain re-run under permuted **sample** labels; one
  process with an inner parallel loop is the faithful, efficient encoding.

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
  nominal-p / FDR thresholds, and the verdict resolution order all live in `config.yaml`, which cites
  `pre-registration:0002` as their source of truth. Scripts read them; nothing is hard-coded.
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

## Work packages

### WP0 — Workflow skeleton + locked config + conda envs
- **Depends on:** G1/G2/G4 cleared (done).
- **Entry point:** `code/workflows/Snakefile`, `config.yaml`, `envs/*.yaml`.
- **Definition of done:** `snakemake -n` resolves a complete DAG from raw inputs to `results/verdict.json`;
  `config.yaml` contains **every** locked pre-reg parameter with an inline `# pre-registration:0002`
  provenance comment; `snakemake --lint` clean; conda envs solve.

### WP1 — Reproducible acquisition rules
- **Depends on:** WP0.
- **Entry point:** `rules/acquire.smk`, `parse_gse14577.py`, `extract_gse130353.py`.
- **Definition of done:** a `download_gse130353` rule fetches `GSE130353_RAW.tar` and **verifies it
  against the locked SHA-256** (`98e6b07b…`); GSE14577 SOFT fetch rule with its locked hash;
  `parse_gse14577` and `extract_gse130353` reproduce the WP-checked matrices + `sample_sheet.tsv`
  (keyed on `subject_status`, not filenames); `g1_acquire.py` logic is refactored into these modules
  (the one-off curl is retired in favor of the rule).

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
  mapped/unmapped fractions and **Hallmark-gene coverage**; a QA checkpoint gates on a configured
  minimum coverage (distribution-severity if low, structural if the mapped set is empty); retired
  ENSG (rel68→current) are logged, not silently dropped.

### WP4 — Preprocessing (collapse, filter, geneset prep)
- **Depends on:** WP3.
- **Entry point:** `rules/prepare.smk`, `collapse_probes.R`, `prepare_genesets.R`.
- **Definition of done:** GSE14577 probe→gene **median collapse** with U133A∪B combined per patient
  (15 patients, not 30 arrays); GSE130353 near-zero `log_mu` filter applied on the **full cohort**
  (symmetric across groups; mask logged); `prepare_genesets.R` emits the pinned, size-filtered gene-set
  list + the joined keyword→theme assignment; a `cohort_audit.json` per dataset records every raw→
  filtered count and decision.

### WP5 — DE + enrichment (limma, fgsea across contrasts × DBs)
- **Depends on:** WP4.
- **Entry point:** `rules/enrich.smk`, `limma_de.R`, `fgsea_enrich.R`.
- **Definition of done:** `limma_de.R` produces moderated-t ranked gene lists for the **5 contrasts**
  (`PI-CFS-vs-HC`, `QFS-vs-HC`, `CFS-vs-HC`, `QFS-vs-QS`, `QS-vs-HC`); `fgsea_enrich.R` produces NES
  tables for each contrast × **3 DBs** (Hallmark primary; Reactome, GO-BP sensitivities) using the
  pinned sets + size filter + master seed; all parameterized, no hard-coded thresholds.

### WP6 — Concordance + permutation null
- **Depends on:** WP5.
- **Entry point:** `rules/verdict.smk` (`concordance_primary`, `permutation_null`).
- **Definition of done:** `concordance_primary` writes the observed Spearman ρ (PI-CFS-vs-HC ×
  QFS-vs-HC over Hallmark) + the NES scatter; `permutation_null.R` writes `p_perm` from the **paired,
  independent, sample-label** null (B from config; seed fixed; null histogram emitted); a small-B smoke
  config reproduces a deterministic `p_perm` under a fixed seed (test).

### WP7 — Specificity + theme roll-up + DB-robustness + compartment
- **Depends on:** WP5 (specificity uses QFS-vs-QS, QS-vs-HC fgsea), WP6 (concordance-carrying set needs
  the primary pair).
- **Entry point:** `rules/verdict.smk` (`specificity`, `theme_rollup`, `db_robustness`, `compartment`).
- **Definition of done:** `specificity.py` computes per-set **S1/S2** classes (same-sign-NES ∧ nominal
  fgsea p<0.05) → `fatigue-specific`/`exposure_sequela`/`unresolved`; `theme_rollup.py` applies the
  **strict-dominance** rule (`#fatigue-specific > #exposure_sequela`); `db_robustness` enforces
  **sign-consistent** recurrence in ≥2 of {Hallmark, Reactome, GO-BP}; `compartment` applies the locked
  marker regex to the **concordance-carrying set** (≥50% rule). Each reads its definition from config.

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
   only. *Lean: keep natural-log internally; convert for display.*
2. **Near-zero `log_mu` filter threshold.** Unexpressed genes sit near `log_mu ≈ −14`. Set a config
   threshold (e.g. retain genes with `log_mu > t` in ≥N donors) and run it symmetrically. *Needs a
   value; pick from the per-gene `log_mu` distribution at WP4, record in `cohort_audit.json`.*
3. **U133A∪B overlap genes.** Some genes appear on both chips; define the combine rule (per-patient
   mean of platform-level collapsed values vs treat-as-separate). *Lean: mean of the two platform
   values per patient; flag count of dual-chip genes.*
4. **`org.Hs.eg.db`/annotation versions vs MSigDB release.** Pin all annotation `.db` packages in the
   conda env so probe→Ensembl and the gene-set universe come from a coherent build; record versions.
5. **Exhaustive vs Monte-Carlo permutation for the GSE14577 arm.** `C(15,8)=6435` is exhaustible but
   the ρ null is *paired* with the Monte-Carlo GSE130353 arm; default to `B=2000` paired draws, note
   the exhaustive option as a robustness toggle.

## Non-Goals

- Confirming a shared mechanism, or running the `≥3-trigger` test (exploratory ceiling, by pre-reg).
- Any absolute-scale / fold-magnitude claim (rank-only estimand).
- Count-based inference (DESeq2/edgeR) — inadmissible (G2: estimate is `log_mu`, not counts).
- Cross-dataset expression-matrix merge.
- Commons `mixin-dataset` entities / datapackages (deferred to promotion).
- Re-deciding any pre-registered parameter — this plan executes, it does not re-plan.

## Acceptance Criteria

- [ ] `snakemake -n` resolves the full DAG raw → `results/verdict.json`; `snakemake --lint` clean.
- [ ] `config.yaml` encodes **every** locked pre-reg parameter, each with a `# pre-registration:0002`
      provenance comment; no threshold/regex/seed is hard-coded in any script.
- [ ] Acquisition is a rule with **checksum verification** against the locked SHA-256s; the one-off
      `curl` is retired; payloads stay gitignored.
- [ ] Every processed substrate has a **structural (build-fatal) + distribution (surfaced)** QA
      checkpoint with a `*.qa.pass` sentinel; a corrupted fixture halts the DAG; `qa_report.md` is
      never the strict rule's declared output.
- [ ] G3 harmonization emits mapped/unmapped + Hallmark coverage and gates on it.
- [ ] The permutation null is the **paired, independent, sample-label** null (not gene-shuffle), seeded
      and reproducible; the verdict is emitted by the **locked resolution order** as exactly one label.
- [ ] Re-running `--use-conda` from clean produces a byte-identical `verdict.json` under the fixed seed.
- [ ] A results markdown lands in `results/` and is wired to `q0001`/`h0001`/`q0017`.

## Notes on reusable infrastructure

`qa_checkpoint.py` (config-driven two-severity structural/distribution checkpoint with sentinel) and the
Snakemake `envs/` (limma+fgsea+annotation Bioconductor stack) are **`reusable: true`** — directly
liftable to any future expression reanalysis in `health-immunity` / `pan-disease`, and a candidate for
commons promotion once the workflow stabilizes.
