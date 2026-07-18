# t139 — Step 2 result: GSE157007 staging, pseudobulk, frailty signature

- **Date:** 2026-07-18
- **Task:** `task:t139` · **Scope:** D-008 feasibility packet, **Step 2 only**
- **Pre-registration:** `doc/plans/2026-07-18-t139-frailty-projection-feasibility-preregistration.md` (re-frozen after Amendment 1)
- **Workflow:** `code/workflows/t139-frailty/` (run: `snakemake -s …/Snakefile --use-conda -c1 step2`)

**This is NOT a GO/NO-GO packet.** Step 2 builds the training signature and its
provenance only. No PAIS projection, no target-cohort labels, and no packet
verdict were touched — those are Steps 3–5.

## Inputs staged + checksum-locked (config.yaml)

| role | source | file | sha256 (first 16) | note |
|---|---|---|---|---|
| donor metadata | GSE157007 | `GSE157007_series_matrix.txt.gz` | `321be57f4a0f823c` | 5 frail + 6 healthy-old GEX donors (asserted at parse) |
| expression | GSE157007 | `GSE157007_RAW.tar` (740,761,600 B) | `79efc3456e24ae48` | 10x triplets; both submissions are MatrixMarket content |
| deconv panel (Gate 3b) | MCPcounter | `mcpcounter_genes.txt` | `408f6c5d02c8f9bd` | Neutrophils + T/CD8/NK/B/cytotoxic lineages |
| gene map (Gate 2) | org.Hs.eg.db 3.22.0 | `ensembl_symbol_map.tsv` | `a908bdd55fab72a6` | generated deterministically (47,792 pairs) |

Fetches ran through Snakemake (ad-hoc shell egress is sandbox-blocked). The two
projection-time references (panel, gene map) are pinned **now** so they cannot
drift before Step 3.

## Donor pseudobulk (GEX only [A1], donor = unit)

11 donors, raw scRNA GEX counts summed across cells; aligned on the **33,694**
Ensembl genes common to all donors. Cells/donor 2,529–12,796; total counts
17.4M–60.3M.

- **Frail (5):** F002, F004, F006, F007, F008 — 2,529–8,232 cells.
- **Healthy-old (6):** F020, F021, F023 (F0xx submission) + OH14, OH15, OH17 (OH submission) — 6,477–12,796 cells.

## Signature (frozen limma-voom pipeline; edgeR 4.8.2 / limma 3.66.0)

`filterByExpr(group)` kept **15,003** genes → TMM → voom → `lmFit(~group)` → eBayes
→ topTable(coef = frail-vs-old). Signature = nominal p < 0.01 & |log2FC| > 0.5,
capped at 200 → **200 genes (184 up / 16 down in frail)**.

Top up-in-frail genes are a coherent **innate-inflammation / inflammaging** panel:
**CSF3, IL6, IRG1/ACOD1, CSF2, F3, IFNB1, RHCG** — face-valid for a frailty
contrast (IL6-up is textbook), i.e. the signal is not obviously pure technical noise.

## Gate 1a (learnability) — DIAGNOSTIC only

Leave-one-donor-out over all 11 donors (full pipeline re-fit per fold):
- **median pairwise Jaccard = 0.639** (threshold ≥ 0.50; NO-GO < 0.30)
- **137 reproducible genes** at selection-frequency ≥ 0.8 (threshold ≥ 20)
- → **clears** the Gate-1a bar as a training-side diagnostic.

The signature is stable to dropping any single donor. This is *not* the packet
verdict; it only says the signature is learnable from 5 vs 6 donors.

## Caveats carried into Steps 3–5 (recorded in provenance)

1. **Submission-batch ↔ contrast confound (load-bearing for Gate 3):** all 5 frail
   + 3 of 6 healthy-old are the F0xx submission (GSM4750xxx); the other 3
   healthy-old are the later OH submission (GSM5684xxx). So frail-vs-old is partly
   a between-submission contrast. The OH donors also have systematically more cells
   (~12k vs 2.5–8k). This is precisely what the Step-3 **negative-control** and
   **batch/transfer** gates must rule out before any signal is believed.
2. **Strong up-skew (184/16) + cap hit** — many genes cleared the threshold; the
   permutation-label and matched-random-set nulls (Gate 4) will test whether the
   projection separation exceeds what this skew produces by chance.
3. **Direction is retained** (up/down in frail) so the signed projection score is
   defined for Step 3.

## Reproducibility

Pinned URLs + locked sha256 (record-or-verify; mismatch HALTs). Env
`envs/r-sc.yaml` (Bioc 3.22/R 4.5; limma + org.Hs.eg.db pinned) with a generated
`envs/r-sc.conda-lock.yml` for byte-level repro. Outputs:
`results/t139-frailty-feasibility/{signature.tsv, signature_provenance.json, gate1a_lodo.json}`.
