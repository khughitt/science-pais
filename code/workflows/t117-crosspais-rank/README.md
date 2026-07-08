# t117 — cross-PAIS pathway-response effective-rank estimation

Snakemake workflow for **`task:t117`** / **`plan:0010`**: learn the reproducible
effective rank *R* of the cross-trigger PAIS blood pathway-response subspace from
primary data, with dataset/condition leave-one-out stability as the primary
believability criterion.

- **Design:** `entities/plans/0010-crosspais-pathway-response-rank-estimation.md`
- **Review:** `doc/reviews/0010-crosspais-pathway-response-rank-estimation-pipeline-review.md`
- **Grounds:** `interpretation:0037` (t116 R-regime grid + the K≥3 identifiability lever)

## Status: WP1 acquisition COMPLETE; WP1b+ parse/analysis stubbed

`snakemake -n` resolves the complete **75-job** DAG. **WP1 acquisition is
implemented and run** (download + checksum + universe build/verify); the remaining
rule bodies (WP1b per-deposit parse, WP2–WP6) are fail-early stubs (`exit 1`, no
silent placeholder output) until their work package implements them. `config.yaml`
encodes **all** design parameters — it originates the design; scripts hard-code
nothing.

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
# dry-run — resolves the DAG (75 jobs)
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
| `stage_matrix` (GEO) · `salmon_gene_matrix` (SRA) | WP1b | per-deposit parse of the verified raw payload → uniform gene matrix | F |
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
