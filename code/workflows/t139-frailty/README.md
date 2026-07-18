# t139 — frailty signature-projection feasibility packet (workflow)

Isolated Snakemake pipeline for **`task:t139`** / **D-008**. This directory
implements **Step 2 only** of the frozen pre-registration:

- **Frozen spec:** `doc/plans/2026-07-18-t139-frailty-projection-feasibility-preregistration.md`
  (re-frozen after Amendment 1)
- **Scope decision:** `core/decisions.md` → **D-008** (feasibility packet only;
  reportable projection gated on a later **D-008b**)

## Step-2 scope (this workflow, as run)

Checksum-pinned **GSE157007 scRNA-GEX** staging → donor mapping → donor
pseudobulk → **frail-vs-healthy-old** limma-voom signature (+ Gate-1a LODO
diagnostic + provenance). Two references are **pinned now as hashed inputs**
though they are consumed at projection time (Step 3+): the MCPcounter
deconvolution panel (Gate 3b) and the org.Hs.eg.db-derived gene map (Gate 2).

**Explicitly NOT in Step 2:** no PAIS projection, no target-cohort label
inspection, and **no GO/NO-GO verdict** (that is Step 5). The Gate-1a LODO figure
is reported as a diagnostic, not a decision.

## Run

Network fetches go through Snakemake (ad-hoc shell egress is sandbox-blocked):

```bash
uv run --frozen --group pipeline snakemake \
  -s code/workflows/t139-frailty/Snakefile --use-conda -c1 step2
```

Targets: `step2` builds signature + provenance + LODO + the two pinned refs.

## Verified inputs (checksums locked in config.yaml)

| role | accession / source | file | note |
|---|---|---|---|
| donor metadata | GSE157007 | `GSE157007_series_matrix.txt.gz` | 5 frail + 6 healthy-old GEX donors (asserted) |
| expression | GSE157007 | `GSE157007_RAW.tar` (706 MB) | 10x triplets; **F0xx = `_matrix.tsv.gz`, OH = `_matrix.mtx.gz`** |
| deconv panel (Gate 3b) | MCPcounter (Becht 2016) | `mcpcounter_genes.txt` | Neutrophils + T/CD8/NK/B/cytotoxic lineages |
| gene map (Gate 2) | org.Hs.eg.db 3.22.0 | `ensembl_symbol_map.tsv` | generated deterministically from the env-pinned package |

## Known data nuances (recorded in provenance)

- **Donor is the unit** — 48 GEO samples = 17 donors × {GEX, VDJ, CITE}
  modalities; only `_scRNA` GEX libraries feed pseudobulk [A1].
- **Format ↔ contrast confound:** all 5 frail + 3 old donors are the F0xx TSV
  submission; the other 3 old are the later OH MTX submission. This partial
  batch/format structure is carried into the Step-3 transfer/batch gates.
- Donors are aligned on the **intersection** of Ensembl gene ids present in
  every donor's features (the drop is logged).
