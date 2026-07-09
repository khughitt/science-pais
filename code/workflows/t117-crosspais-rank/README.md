# t117 — cross-PAIS pathway-response effective-rank estimation

Snakemake workflow for **`task:t117`** / **`plan:0010`**: learn the reproducible
effective rank *R* of the cross-trigger PAIS blood pathway-response subspace from
primary data, with dataset/condition leave-one-out stability as the primary
believability criterion.

- **Design:** `entities/plans/0010-crosspais-pathway-response-rank-estimation.md`
- **Review:** `doc/reviews/0010-crosspais-pathway-response-rank-estimation-pipeline-review.md`
- **Grounds:** `interpretation:0037` (t116 R-regime grid + the K≥3 identifiability lever)

## Status: WP1 + WP1b (11 deposits PASS) + WP2 (matrices) + WP3 (rank battery + Stage-3c calibration) + WP4 (artifact + compartment adjudication) + WP4b (non-infectious FM/GWI specificity) DONE; WP5/WP6 stubbed

**WP4b done (2026-07-09).** Discovery sweep (Open Question #4) found **admissible public
non-infectious deposits** (NOT the note-only branch): fibromyalgia `GSE221921` (flagship) +
`GSE67311`, GWI `E-MEXP-2069` + `GSE286345`, IEI `GSE182503`; **PACVS has none public** (note-only
gap). `gws_fm_specificity.py` builds the PAIS shared subspace U_ref from the strict matrix (same
standardize + leading-r left-singular-vector construction as the WP4 recovered-control prong — the
`read_nes`/`projection_fraction` primitives are imported verbatim) and projects the non-infectious
column onto it. The flagship `GSE221921` (96 FM / 93 HC, PBMC NovaSeq, "log of normalized TPM" →
`log2_intensity`, symbol map 86%) rides the **same** stage→DE→fgsea path via a `matrix: specificity`
tag that is **absent from `MATRIX_COMPOSITION` and the adjudication extras** — so it enters no rank
matrix and no artifact control; it meets the PAIS matrix only at the NES level, then is projected.
**Result — `exploratory_flagship`, `partially_recovered_indeterminate`:** the FM column recovers
**0.045** of its variance in the strict PAIS rank-2 subspace. "Above chance" rests on an **empirical
row-permutation null** (permute the FM column across pathways, reproject; null mean 0.0025, p95 0.0074,
**empirical p=0.0005** over 2000 draws — the analytic r/P floor is reported for orientation only, not as
calibrated specificity). The replication ceiling is the **trigger-INDEPENDENT leave-one-*trigger*-out**
projection (not column-LOO, which would let a held-out long-COVID column reuse the other LC columns), and
that ceiling is averaged **per-trigger, not per-column** — with 5 of 7 strict columns being SARS-CoV-2,
column-weighting understates the ceiling (0.16) versus the per-trigger mean (**0.24**): FM sits at
**0.185× the trigger-weighted trigger-LOO mean**. Neither cleanly **infection-specific** (well above its
permutation null) nor a full **generic-sickness manifold** (well below a trigger-held-out PAIS trigger).
Caveat sharpened by trigger-LOO: that ceiling is **heterogeneous (per-trigger 0.11 SARS-CoV-2 / 0.27
PI-ME/CFS / 0.35 Lyme; per-column 0.02–0.35) with the LC-out projections low** — the PAIS subspace is
**not even trigger-general within PAIS** (coheres with the Stage-3c FAIL / LOO-fragility), so FM is read
against a weak, non-trigger-general baseline. That baseline is also **under-identified**: with 3 strict
triggers, each leave-one-trigger-out reference is built from only 2 triggers, below the K≥3 floor
(`trigger_loo_identifiability_pass: false`). The queued replication panel (`GSE67311` WB-microarray, `E-MEXP-2069` GWI-microarray,
`GSE286345` GWI-RNA-seq pending a GWI/FM co-carry check) + the reverse projection (needs ≥2 non-infectious
columns) are recorded, not built. **Infra:** `acquire_payload` now emits the `origin.json` provenance
sidecar `stage_matrix` requires (previously written only during the WP1 run), so a fresh acquire of any
deposit stages reproducibly. Run:
`snakemake … --use-conda -- results/t117-crosspais-rank/specificity/gws_fm.json`.

**WP4 done (2026-07-08).** `artifact_adjudication.py` reuses the WP3 battery **verbatim**
(imports `rank_battery` + `rank_estimators`) and runs the artifact + compartment
battery before any biological reading of R, **holding every stratum/drop to the same
K≥3 identifiability rule as the LODO/LOCO folds**. **Result —
`artifact_controls_pass = false` / `interpretation_status = limited_or_nonarbitrating`
for both matrices** (the available controls are underpowered/incomplete; they neither
rescue nor refute the low-rank): (i) **Compartment invariance NOT established** — only
the PBMC stratum clears K≥3 (strict PBMC R=2; WB 1-trigger non-identifiable), so a
composition-shift rival can be neither confirmed nor refuted (underpowered, **not**
evidence of entanglement). (ii) **Drop-sorted:** pooling the sorted QFS stratum keeps
strict R=2 but **rotates the leading subspace 26.7° (> 20° cutoff)** → the on-data
justification for the G1 sorted exclusion. (iii) **Platform-LOO:** strict is
**single-platform → untestable**; sensitivity drop-microarray R=3 survives
(identifiable), drop-rnaseq is **non-identifiable** (2 triggers < K=3) → invariance
`partial`. (iv) **Recovered-control specificity (conservative):** the naive-defined
shared subspace is **weakly present in case-vs-recovered** (projection 0.09 < 0.30) —
this supports only "not strongly present," **not** a "case-vs-healthy/infection-history
axis" claim. **No artifact floor was subtracted:** the only null applied is the
parallel-analysis per-column-permuted null — a **`random_structure_null_floor`, NOT an
artifact floor** (it controls random cross-column structure only). Set-based negative
controls, CIBERSORTx-LM22 composition adjustment, and acute-decoy specificity (both
decoys, both matrices) are **note-only deferred** with their blockers. The R point
estimate (strict 2 / sensitivity 3) is the random-structure-null-adjusted R_primary,
**not** a clean adjudicated estimate. This coheres with the structural heterogeneity
(mean≈0, high SD) and the Stage-3c FAIL. Run:
`snakemake … --use-conda -- results/t117-crosspais-rank/artifact/{strict,sensitivity}.adjudicated.json`.

**WP3 done (2026-07-08).** `rank_battery.py` (+ shared `rank_estimators.py`) runs three
rotation-invariant estimators (Horn parallel analysis [primary, bootstrap CI],
Owen-Perry bi-cross-validation SVD, split-half subspace stability) + the t116 structural
co-primary (off-diagonal Spearman-concordance SD) + pre-locked LODO/LOCO + a first-class
LC-out contrast-count power/CI curve + compartment-stratified R. `calibration_3c.py`
calibrates the battery against t116's own generative model at the real K/per-column-N
(three arms: α=0 self-check, strong-signal positive control, operating-point matched).
**Descriptive result:** strict R=2 (CI[2,2]), sensitivity R=3 (CI[3,4]) — both LOW-rank
but LC-inclusive and LOO-fragile; strict LC-out is **non-identifiable** (2 triggers),
sensitivity LC-out **FAILs** → hypothesis-grade, not q0050-grade. The structural
co-primary (mean ρ≈0, SD 0.25–0.27) is **heterogeneous** (finite-repertoire-like), NOT a
single-attractor signature — it **diverges** from the SVD low-rank reading (reported, not
reconciled). **Stage-3c FAILS fail-closed, on two INDEPENDENT grounds** (both recorded
additively): (1) on a clean α=0 signal the battery only weakly recovers R=2 (R̂≈1, CI
coverage 0.54 — under-covered) and does not recover R=4 → the SVD→t116-grid bridge is not
licensed at the corpus width K=7/10; (2) the real concordance is at the sampling floor →
no rank identifiable at the operating point. `calibration.pass=false`, **no grid verdict**
(gates WP6). This demonstrates, on data, the plan's low-power ceiling.

**WP1 acquisition** (download + checksum + universe build/verify) and **WP1b**
(config-driven brutally-uniform per-deposit parse via `stage_matrix.py`, 11 deposits
PASS) are implemented and run. **WP2 is DONE (2026-07-08):** scale-aware DE
(`de_ranklist.R`: voom for counts/estimated_counts, log2 for fpkm/cpm, direct for
log_mu/log2_intensity) → `fgsea_enrich.R` (reused verbatim) → `assemble_matrix.py`,
producing **strict (1153 gene_sets × 7 built cols of 9)** and **sensitivity (1153 ×
10, nested)** pathway × contrast matrices. Deferred columns (`gse267625`,
`gse143549`) are recorded as `omitted_columns`, never silently dropped; the
same-tissue LC NES-comparability **best-pair screen** on the enriched subset gives WB
`concordant` (ρ=0.50) and PBMC `best_pair_only` (ρ=0.42, with `gse251849` discordant
→ carried to WP3 `wp3_loo_candidates`). The remaining rule bodies (WP4–WP6) are fail-early stubs (`exit 1`, no
silent placeholder output). `config.yaml` encodes **all** design parameters — it
originates the design; scripts hard-code nothing.

**WP2 done (2026-07-08):**
- **Scale-aware DE** (`code/scripts/de_ranklist.R`, t117-owned): ONE ranking
  statistic (limma moderated-t) across all 5 corpus scales so NES stays
  commensurable (review Finding F, executable). `counts`/`estimated_counts` →
  `limma::voom` (library-size logCPM + weights; no edgeR/TMM, so the NES-sensitive
  r-bioc env isn't re-solved); `fpkm`/`cpm` → `log2(x+1)`; `log_mu`/`log2_intensity`
  → direct. Per-contrast `de_models` extensions applied: `~ platform + group`
  (gse251872), `duplicateCorrelation(twin_pair)` (gse16059), longitudinal
  `collapse_to: subject` (gse226260, gse128078).
- **NES-comparability + power finding:** the all-set Spearman is diluted to ~0 by
  the ~700 near-zero-NES pathways; on the enriched subset the powered same-tissue LC
  pairs concord (PBMC best pair 0.42, WB 0.50). This is a **best-pair screen** — the
  underpowered `gse251849` (0 BH<0.05) concords with neither PBMC sibling and is a
  `wp3_loo_candidate`. Per-deposit marginal power is uneven (6081…0 BH<0.05; 5
  deposits at 0) — the deposit-level face of the WP1 LC-out low-power ceiling, carried
  to WP3.
- Run: `snakemake -s code/workflows/t117-crosspais-rank/Snakefile --use-conda
  --conda-prefix /data/snakemake/conda -- data/processed/t117/matrix/{strict,sensitivity}.pathway_by_contrast.tsv`

**WP1b done (2026-07-08):**
- **WP0 semantic wiring confirmed/completed** — sensitivity matrix nested (`strict`
  + ME/CFS additions via `MATRIX_COMPOSITION`); `calibration_3c` depends on the real
  assembled matrix/grouping/structural stats; per-contrast DE specs explicit in
  `de_models`, each now declaring the exact `covariates` its sample sheet must carry.
- **Uniform contract** (`code/scripts/stage_matrix.py`, config `parse:`) — every
  deposit emits `expr.gene.tsv.gz` + `sample_sheet.tsv` + `clean.qa.pass` +
  `stage_matrix.qa.json` (the per-deposit ingest contract; review Finding F).
- **Tranche 1 proven** — `gse251849_lc` (62710 Ensembl × 23) + `scilifelab_lc`
  (60669 × 110) parse to PASS; both are salmon/RSEM `estimated_counts` (continuous,
  limma-only). **Gap surfaced:** most GEO deposits' case/control lives in
  series-matrix/SOFT metadata not yet staged → their `parse:` block is
  `status: deferred` naming the exact blocker (metadata payload / harmonization map).
- **Tranche (b) — shared gene-id identity contract** (`build_gene_id_map.R`,
  config `harmonization:`) — symbol/alias/RefSeq → Ensembl from the **same**
  org.Hs.eg.db (3.22.0) + `first` policy as the gene sets, so identity is
  commensurable by construction. `stage_matrix.py` **fails closed** on any of:
  map-rate < `min_map_rate` (0.60), wrong-namespace fraction, or mostly-ambiguous
  map (per-id `n_targets` ≥ 2 fraction > `max_ambiguous_mapped_frac`) ⇒ contrast
  **ineligible**, not a thin matrix. Proven: `gse270045` symbol 83% ✓,
  `gse128078` RefSeq 90% ✓ (but isoform-FPKM→gene sum is only approximate →
  sensitivity-only), `gse143549` gene_name 56% → fails closed. **b·pin DONE:** the
  canonical map is built by the pinned org.Hs.eg.db **3.22.0** r-bioc env
  (`--use-conda`), is **deterministic** (identical sha256 on rebuild), and its
  `map_sha256` (`d07f65bd…`) is committed in config + re-verified before use — so
  non-Ensembl parsing is now **reproducibly consumable**. (b) resolves gene-id
  only; `gse270045`/`gse128078` still need group metadata, and `gse143549` is still
  gene-id-blocked (a cleaner symbol source, not group, unlocks it).
- **Tranche (c) — microarray handlers DONE** (`parse_series_matrix.py`,
  `harmonize_microarray.R`, config `microarray:` + `parse.*.handler: prebuilt`) —
  microarray probe→gene needs the **platform** annotation `.db` (not the tranche-b
  symbol map), so it can't live in the pure-Python `stage_matrix`. Architecture:
  dedicated rules run the **parse→harmonize→collapse** chain as upstream producers,
  and a new **`prebuilt`** `stage_matrix` handler ADOPTS the resulting gene matrix +
  inline group into the uniform contract (stage_matrix stays the SOLE producer of
  `expr.gene.tsv.gz`). Both microarray deposits carry group **inline** → both **PASS**:
  `gse14577` (t035 chain reused verbatim; hgu133a/b.db) → **18371 genes × 15 patients
  (8 PI-CFS / 7 HC)**; `gse16059` (GPL570; **hgu133plus2.db** added to the pinned
  r-bioc env, annotation-only/NES-neutral) → **20338 genes × 76 samples (32 CFS / 44
  unaffected; 12 ICF excluded)**, `twin_pair` block covariate carried. The per-sample
  **`tar` trio** (`gse130353`/`gse251872`/`gse63085`) is **tranche (a2), not (c)** —
  handler code alone can't PASS them; they need a group-metadata payload first (now DONE).
  > **Repro note:** `envs/r-bioc.conda-lock.yml` postdates the hgu133plus2.db add and
  > needs a `conda-lock` regen (tool absent this session); the pinned `=3.13.0` in
  > `r-bioc.yaml` is the source of truth until then.
- **Tranche (a) — series-matrix group metadata (partial)** (`parse_geo_metadata.py`,
  config `parse.*.metadata_payload` + `group_source.mode: sheet`) — several RNA-seq
  deposits carry case/control ONLY in the series-matrix `!Sample_*` header (not the expr
  columns). Architecture: the series matrix is added as a **second acquisition payload**
  (pinned sha256, hash-stable across fetches), `parse_geo_metadata` parses its header into
  `series_metadata.samples.tsv`, and `stage_matrix`'s `sheet` group_source **joins it to
  the expr columns** and applies the deposit's `level_map`/`group_regex` (raw condition ->
  arm). Two group-blocked deposits now **PASS**:
  `gse270045` (**19 LC / 17 healthy**; join expr cols = `sample_id`, group = title-regex
  "Healthy Control"/"Long Covid" — no disease-state characteristic exists; symbol map 83%)
  and `gse128078` (**55 / 44 samples = 14 ME/CFS vs 11 control subjects**; join = title,
  group = `disease_state`, subject+timepoint covariates carried for the WP2 timepoint
  collapse; RefSeq map 90%; SENSITIVITY-ONLY per the FPKM caveat). **Data finding:**
  `gse270045`'s `_LC_counts` file is a MISNOMER — it is fractional EM/pseudo-alignment
  gene counts (values 1e-8..5e4, library-size-varying column sums), so `estimated_counts`'
  scale check now tests the real invariant (non-negative + count magnitude), not an
  integer-fraction proxy that wrongly rejects heavily-fractional EM matrices
  (tranche-1 `gse251849`/`scilifelab` re-verified unchanged).
- **Tranche (a-rest) — deposits needing MORE than series metadata DONE** (2026-07-08).
  Investigation corrected the catalog's premises (Explicit > Defensive); 2 now **PASS**,
  1 stays deferred with a sharpened blocker:
  `gse226260` (LC, PBMC) — **CATALOG CORRECTED**: the combined expr matrix is
  **single-platform** (all 228 cols GPL24676; the catalogued "2-platform batch" made the
  `~ platform + group` model degenerate) and mixes the PASC cohort with a **disjoint
  142-sample acute-severity cohort** (dropped). Group + subject/timepoint from the family
  SOFT (`parse_geo_soft`; 2-platform → plain series-matrix 404s), join = `title`. Staged
  **PASC vs NOPASC → 24203 ENSG × 86 (72 / 14 = 28 vs 8 subjects)**, de_model `~ group`
  (no platform term), subject+timepoint carried for the WP2 collapse; control =
  infected-nonPASC-convalescent (small arm). `gse228320` (LC, WB) — **CATALOG
  CORRECTED**: titles carry a **binary control/sequela** label (not continuous-only), so
  staged as **control vs sequela → 60683 ENSG × 50 (18 / 32)** on the stock `~ group`;
  continuous DLCO carried in the sheet for a later severity-axis sensitivity. The expr id
  `MC1_N` is embedded in the free-text title, handled by a new optional
  **`sample_col_regex`** join-key extractor (leaves the original column intact so the same
  title still yields the group).
  > **Still deferred (sharpened):** `gse267625` — deposited metadata has **no
  > case/control or symptom label** (only subject `AA*`/`VV*` prefix + timepoint,
  > all WT/untreated); the within-cohort contrast needs the **paper** to define it, not a
  > metadata-only prefix guess. `gse143549` — gene-id-blocked (56% < 0.60), deprioritized.
- **Tranche (a2) — per-sample `tar` trio DONE** (`parse_tar` in `stage_matrix.py` +
  `parse_geo_soft.py`, config `handler: tar`). Each RAW.tar member is one sample: its
  `(member_gene_col, member_value_col)` — name OR positional index — becomes that
  sample's column, keyed by `sample_id_regex` on the member basename; duplicate gene ids
  WITHIN a member collapse under `member_agg` before the cross-deposit Ensembl collapse.
  Group is NOT in the tar — it comes from a metadata sheet (`series_matrix` via
  `parse_geo_metadata` OR `soft` via the new `parse_geo_soft`, selected by
  `metadata_format`) joined by the GSM the member filename carries. All three **PASS**:
  `gse130353` (post-Q-fever fatigue, monocytes; MMSEQ `log_mu`) → **56625 × 20 (10 QFS
  case / 10 QS infected-recovered control)**, group from SOFT `subject status` via
  parenthetical-code regex `\(QFS\)`/`\(QS\)` (HC + CFS drop; `Fatigue Syndrom` alone
  would mis-match both QFS and CFS), 0 NaN cells, scale `log_mu` PASS (limma-only);
  `gse63085` (Lyme/PTLDS, cufflinks FPKM; 97 PBMC members) → **20214 × 42 (29 Lyme-V5
  case / 13 control)**, arm+visit selected by the series-matrix `time` characteristic
  (`\(V5\)` = 6-mo post-treatment → case, `^control$` → control; Lyme V1/V2 drop),
  symbol map 86%; `gse251872` (PI-ME/CFS PBMC; 27 members, 2 seq platforms) → **18369 ×
  27 (12 case / 15 control)**, value column named per-sample (`S###`) → positional
  index 2, series-matrix URL 404s so group comes from the family SOFT title
  (`, HV,`/`PI-ME/CFS`), `platform` batch covariate carried for `~ platform + group`.
  > **Fail-closed guardrails (review):** duplicate metadata join keys HALT (last-write
  > ambiguity); covariate completeness gates on `notna()` (a `NaN`→`"nan"` string no
  > longer counts as present); ragged GEO characteristic rows HALT (no silent
  > provenance loss).
  > **Arm-partition guard (project-review #1):** a declared contrast arm that matches
  > **0 samples** HALTs, naming the dead selector — a too-loose sibling pattern that
  > empties the other arm via first-match-wins (the QFS/CFS substring trap) is refused
  > at group-resolution time, not surfaced later as a silent mis-label. Per-**arm**
  > (not per-selector) so multi-selector arms (`gse251849` control = `^Control` ∪
  > `^Convalescent`) are fine. `NaN`/blank join keys are dropped as non-joinable
  > (recorded), not mis-flagged as ambiguous duplicates (fixes a false HALT on the
  > 6 blank `SampleName` rows of the `scilifelab` companion sheet). Each deposit's
  > per-selector capture counts are recorded in `stage_matrix.qa.json`
  > (`samples.group_resolution`).

**Cross-deposit QA reconciliation (project-review #3):** `reconcile_qa` rolls every ready
deposit's `stage_matrix.qa.json` into ONE sheet
(`results/…/reconciliation/stage_matrix.reconciliation.{tsv,json}`) so the heterogeneity
that matters **before** the rank step is reviewable at a glance: mixed expression scales,
mixed gene-id namespaces, arm balance, covariate coverage, gene-count spread, plus a
`warnings` list (scale-verdict, soft-low map rate, incomplete covariates, thin arms, scale
caveats). It flags `scale_heterogeneity` explicitly — the rank pipeline pools deposits only
at the NES level, so >1 expression scale is admissible **only if** each deposit's DE
contrast absorbs its own scale; the sheet surfaces that assumption rather than hiding it.
Standalone QA target (not in `rule all`):
`snakemake -s code/workflows/t117-crosspais-rank/Snakefile reconcile_qa`.

> **Naming:** `dataset:msigdb-2024-1-hs-hallmark-reactome-rank-universe` is the
> **rank universe** — the Hallmark ∪ Reactome subset **derived from** the broader
> clean base (`dataset:msigdb-2024-1-hs-mapped-pais-gene-set-universe`, which also
> carries GO:BP). It is *not* "the full PAIS gene-set universe"; keep the distinction
> so pathway-coverage claims are read against the rank universe, not the clean base.

**WP1 done (2026-07-08):**
- **Pinned + checksummed acquisition** — every GEO/FigShare deposit's raw payload
  downloaded + verified against a **LOCKED sha256** (`config.acquisition`, reusing
  `code/scripts/fetch_url.py`; empty hash or mismatch ⇒ HALT). 14 deposits staged.
- **Single pinned universe materialized** — Hallmark ∪ Reactome (1153 sets, 15–500;
  GO:BP dropped per the universe decision), built by `code/scripts/combine_universe.R`
  from the two hash-locked clean-base `.rds` and **re-verified** (`verify_universe`).
  sha256 `2a782ac5…9b07b` is reproducible on rebuild →
  `dataset:msigdb-2024-1-hs-hallmark-reactome-rank-universe`.
- **Salmon path WIRED** — the SRA-only CHIKV decoy (`PRJNA1001790`) quantification
  chain (transcriptome → index → per-run quant → tximport gene matrix) resolves in
  the DAG (`config.salmon`, env `../envs/salmon.yaml`); the heavy index build +
  FASTQ retrieval + quant + the day-21 run/group split are **deferred to WP1b**
  (reference hash HALT-guarded until first verified fetch).

```bash
# dry-run — resolves the DAG (68 jobs remaining after WP1 + WP1b tranche 1)
uv run --frozen snakemake -s code/workflows/t117-crosspais-rank/Snakefile -n all
# WP1 acquisition + universe (implemented rules; runs in the current env)
uv run --frozen snakemake -s code/workflows/t117-crosspais-rank/Snakefile -j4 \
  data/processed/t117/genesets/universe.qa.pass \
  $(python - <<'PY'
import yaml; c=yaml.safe_load(open("code/workflows/t117-crosspais-rank/config.yaml"))
print(" ".join(f"data/raw/t117/{a}/staged.ok" for a in c["acquisition"]))
PY
)
```

Shared conda envs are **reused** from `code/workflows/envs/` (`r-bioc.yaml`, the
plan:0003 limma+fgsea Bioconductor stack; `py.yaml` for fetch/verify) via `../envs/…`;
the Stage-2 DE→enrichment reuses `code/scripts/fgsea_enrich.R` verbatim and
`limma_de.R` for `~ group` contrasts only (see the `de_models` model contract).

## DAG / work-package map

| Stage (rule) | WP | Deliverable | Review finding wired in |
|---|---|---|---|
| `acquire_payload` · `acquire_deposit` · `build_universe` · `verify_universe` · salmon chain | WP1 ✅ | pinned+checksummed staging (done); single universe built+verified; SRA `quantify: salmon` wired | — |
| `stage_matrix` (GEO) · `salmon_gene_matrix` (SRA) | WP1b ✅ framework + tranche 1 | config-driven per-deposit parse → uniform expr + sheet + `clean.qa.pass` + `stage_matrix.qa.json`; `matrix` handler proven (gse251849, scilifelab); microarray/tar/salmon + deferred-metadata deposits named with exact blocker | F |
| `limma_de` · `fgsea_enrich` · `assemble_matrix` | WP2 | pathway × contrast matrix over the one pinned universe; per-deposit ingest + NES-comparability | F |
| `rank_battery` | WP3 ✅ | ≥3 rotation-invariant estimators + **t116 structural co-primary**; LODO/LOCO; **LC-out power curve**; compartment-stratified R (done) | A, B, C |
| `calibration_3c` | WP3 ✅ | rank battery calibrated vs t116's generative model at real K/N (3-arm); **FAILS fail-closed → no grid** (done) | B |
| `artifact_adjudication` | WP4 ✅ | platform-LOO, negative-control sets, recovered-control specificity, **compartment/composition control** (compartment-stratified R, drop-sorted, composition-adjust deferred); reuses the WP3 battery verbatim (done) | C |
| `gws_fm_specificity` | WP4b ✅ | non-infectious FM/GWI read-across (Q-D infection-specificity): projects the PAIS subspace onto a non-infectious column; flagship GSE221921 built, panel queued (done) | D |
| `grid_placement` | WP6 | t116 R-regime placement **only if `calibration.pass`** | A, B |
| `datapackage` | WP6 | manifest: matrix + R estimates + stability profiles | G |

## Corpus (config `contrasts`, WP1-verified 2026-07-08)

- **strict-primary** (WB/PBMC, documented trigger, ≥4 wk floor): **9 columns** —
  6 long-COVID + PI-ME/CFS + Ebola + Lyme (one contrast per deposit as configured;
  WP2 may split some LC deposits into within-deposit subgroup contrasts). **4
  documented triggers** after the Finding-C compartment split (LC, PI-ME/CFS,
  Ebola, Lyme).
- **stratum** (sorted, Finding C): QFS `GSE130353` — a **single column**, so it has
  **no own rank**; held as a separate compartment stratum for the drop-sorted
  comparison + as a projection target, **never pooled** into the primary matrix.
- **sensitivity** (probable-PI ME/CFS, unknown per-subject onset): `GSE128078`,
  `GSE16059` (twins), `GSE14577`. The sensitivity **rank matrix is NESTED** — the 9
  strict columns **plus** these 3 ME/CFS additions (12 columns), not an
  ME/CFS-only matrix (`MATRIX_COMPOSITION` in the Snakefile).
- **decoy** (acute-infection specificity layer): `GSE68310` (influenza),
  `PRJNA1001790` (CHIKV).
- **excluded** (G4 blockers): `GSE224615` (DEG summary only), `PRJNA1184005`
  (SRA-only, unverifiable split).

## Provisional ceiling (do not cite as settled)

WP1 surfaced a **calibration-contingent** low-power ceiling: with the WB/PBMC
primary at 4 triggers, the long-COVID-out fold retains exactly 3 triggers (the
t116 K=3 identifiability floor) — **admissible but low-power**, not
"non-identifiable" (review Finding A). Whether it becomes a citable negative result
is gated on `calibration_3c` + the WP3 LC-out power curve. `results/…` is gitignored
(regenerable); the committed reproducibility contract is this workflow.
