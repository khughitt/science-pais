# t117 — cross-PAIS pathway-response effective-rank estimation

Snakemake workflow for **`task:t117`** / **`plan:0010`**: learn the reproducible
effective rank *R* of the cross-trigger PAIS blood pathway-response subspace from
primary data, with dataset/condition leave-one-out stability as the primary
believability criterion.

- **Design:** `entities/plans/0010-crosspais-pathway-response-rank-estimation.md`
- **Review:** `doc/reviews/0010-crosspais-pathway-response-rank-estimation-pipeline-review.md`
- **Grounds:** `interpretation:0037` (t116 R-regime grid + the K≥3 identifiability lever)

## Status: WP0 skeleton

Rule I/O is **fully wired** so `snakemake -n` resolves the complete DAG
(acquire → `results/…/grid` + `datapackage.json`). Every rule **body** is a
fail-early stub (`exit 1`, no silent placeholder output) until its work package
implements it. `config.yaml` already encodes **all** design parameters — it
originates the design; scripts hard-code nothing.

```bash
# dry-run — resolves the DAG without any staged data (73 jobs)
uv run --frozen snakemake -s code/workflows/t117-crosspais-rank/Snakefile -n all
```

Shared conda envs are **reused** from `code/workflows/envs/` (`r-bioc.yaml`, the
plan:0003 limma+fgsea Bioconductor stack) via `../envs/…`; the Stage-2 DE→enrichment
reuses `code/scripts/{limma_de.R,fgsea_enrich.R}` verbatim.

## DAG / work-package map

| Stage (rule) | WP | Deliverable | Review finding wired in |
|---|---|---|---|
| `acquire_deposit` · `stage_matrix` · `stage_universe` | WP1 | pinned+checksummed staging; SRA `quantify: salmon` | — |
| `limma_de` · `fgsea_enrich` · `assemble_matrix` | WP2 | pathway × contrast matrix over the one pinned universe; per-deposit ingest + NES-comparability | F |
| `rank_battery` | WP3 | ≥3 rotation-invariant estimators + **t116 structural co-primary**; LODO/LOCO; **LC-out power curve** | A, B |
| `calibration_3c` | WP3 | rank battery calibrated vs t116's generative model at real K/N; **gates grid** | B |
| `artifact_adjudication` | WP4 | platform-LOO, negative-control sets, recovered-control specificity, **compartment/composition control** (WB/PBMC-only primary, drop-sorted, composition-adjusted R) | C |
| `gws_fm_specificity` | WP4b | non-infectious GWS/FM read-across (Q-D infection-specificity); note-only if no admissible deposit | D |
| `grid_placement` | WP6 | t116 R-regime placement **only if `calibration.pass`** | A, B |
| `datapackage` | WP6 | manifest: matrix + R estimates + stability profiles | G |

## Corpus (config `contrasts`, WP1-verified 2026-07-08)

- **strict-primary** (WB/PBMC, documented trigger, ≥4 wk floor): 9 columns —
  8 long-COVID + PI-ME/CFS, plus Ebola/Lyme single-trigger. 4 documented triggers
  after the Finding-C compartment split (LC, PI-ME/CFS, Ebola, Lyme).
- **stratum** (sorted, Finding C): QFS `GSE130353` — compartment-stratified R only,
  never pooled into the primary matrix.
- **sensitivity** (probable-PI ME/CFS, unknown per-subject onset): `GSE128078`,
  `GSE16059` (twins), `GSE14577`.
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
