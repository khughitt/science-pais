# t117 — cross-PAIS pathway-response effective-rank estimation

Snakemake workflow for **`task:t117`** / **`plan:0010`**: learn the reproducible
effective rank *R* of the cross-trigger PAIS blood pathway-response subspace from
primary data, with dataset/condition leave-one-out stability as the primary
believability criterion.

- **Design:** `entities/plans/0010-crosspais-pathway-response-rank-estimation.md`
- **Review:** `doc/reviews/0010-crosspais-pathway-response-rank-estimation-pipeline-review.md`
- **Grounds:** `interpretation:0037` (t116 R-regime grid + the K≥3 identifiability lever)

## Status: WP1 acquisition COMPLETE; WP1b parse framework + tranches 1/(b)/(c)/(a)/(a2 tar trio) DONE; WP2–WP6 stubbed

`snakemake -n` resolves the DAG (**68 jobs** remaining after WP1 + WP1b-tranche-1).
**WP1 acquisition is implemented and run** (download + checksum + universe
build/verify); **WP1b is implemented** as a config-driven, brutally-uniform
per-deposit parser (`stage_matrix.py`) with **tranche 1 parsed + proven on real
data**; the remaining rule bodies (WP1b tranches 2–6, WP2–WP6) are fail-early stubs
(`exit 1`, no silent placeholder output) or `parse: deferred` HALTs naming their
exact blocker. `config.yaml` encodes **all** design parameters — it originates the
design; scripts hard-code nothing.

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
  > **Still deferred (need more than series metadata):** `gse226260` (2 platforms →
  > internal-id linking + platform batch), `gse267625` (within-cohort, no external
  > control → WP2 model), `gse228320` (continuous DLCO axis → `~ dlco` model),
  > `gse143549` (gene-id-blocked, deprioritized).
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
| `rank_battery` | WP3 | ≥3 rotation-invariant estimators + **t116 structural co-primary**; LODO/LOCO; **LC-out power curve** | A, B |
| `calibration_3c` | WP3 | rank battery calibrated vs t116's generative model at real K/N; **gates grid** | B |
| `artifact_adjudication` | WP4 | platform-LOO, negative-control sets, recovered-control specificity, **compartment/composition control** (WB/PBMC-only primary, drop-sorted, composition-adjusted R) | C |
| `gws_fm_specificity` | WP4b | non-infectious GWS/FM read-across (Q-D infection-specificity); note-only if no admissible deposit | D |
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
