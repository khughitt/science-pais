# Public cross-trigger post-infective-fatigue expression datasets — registry note

**Status:** **provisioned (2026-06-20, G1/G2/G4 cleared)** — payloads downloaded, hashed, and
parse-contract-verified. Provenance artifacts split (per `plan:0003` review, 2026-06-20): a **minimal
Frictionless `datapackage.json`** (resource list + per-file SHA-256 + source URL) is produced by the
acquisition rule (`plan:0003` WP1) and is the artifact `pre-registration:0002` G1 names; the **formal
`mixin-dataset-1.0` commons entity** remains deferred to commons-promotion (readiness gate in
`~/d/science/docs/process/pipeline-audit-and-refactor.md`). This is a lightweight registry note, **not**
a validated dataset entity. Tracked for **t035** / `pre-registration:0002-cross-trigger-pathway-overlap`.

> **Acquisition note (reproducibility):** the first-pass download used a one-off `curl` for
> `GSE130353_RAW.tar` (the `science` GEO adapter is series-matrix-only). For the final implementation
> the download **must become a rule in a reproducible Snakemake workflow** under `code/workflows/`
> (per user direction 2026-06-20), not a manual step. The acquisition/hash/scale logic currently lives
> in `code/scripts/g1_acquire.py` (stdlib-only, idempotent) and is the seed for that rule.

### Provisioning record (G1 acquisition + integrity)

Top-level SHA-256 (full per-file manifest incl. all 40 MMSEQ members:
`data/processed/acquisition_manifest.json`, gitignored, regenerable by re-running the script):

| File | SHA-256 | Source |
|---|---|---|
| `GSE14577_family.soft.gz` | `a4ca33e1afe96587…2917180` | GEO `series/GSE14nnn/GSE14577/soft/` |
| `GSE130353_RAW.tar` (94.9 MB, 40 members) | `98e6b07b389a922b…0467a4f` | GEO `series/GSE130nnn/GSE130353/suppl/` |
| `GSE130353_family.soft.gz` | `dcb09ba0824d23bc…1f789064` | GEO `series/GSE130nnn/GSE130353/soft/` |
| `GSE130353_series_matrix.txt.gz` | `a6a741a38644df5c…310ea26e` | GEO `series/GSE130nnn/GSE130353/matrix/` |

**GSE14577 (parsed from local SOFT; series_matrix 404s):** GPL96 22,283 probes × 15 samples
(`6a9e9b8e…`), GPL97 22,645 × 15 (`c1c5761e…`); **7 HC + 8 PI-CFS** (15 patients, chip A+B each), all
Male; scale 2.58–14.33, mean ≈6.5, 0% integer → **log2 intensities confirmed**.

**GSE130353 (G2 + G4 cleared from the data, not the metadata):**
- **G2 scale verdict = PASS.** MMSEQ columns `feature_id, log_mu, sd, mcse, iact, effective_length,
  true_length, unique_hits, ntranscripts, observed, percentiles…`; 56,625 features (Ensembl gene IDs,
  release 68). The expression estimate is **`log_mu`** (natural-log posterior mean; continuous, ~30%
  negative, 0% integer). The SOFT's "containing **counts** per gene" label is **inaccurate** — the
  recommended estimate is `log_mu`, *not* the integer `unique_hits` column (which discards MMSEQ's
  multi-map model). ⇒ **continuous limma only; DESeq2/edgeR inadmissible**, exactly as the pre-reg
  locked. `sd` is the per-estimate posterior SD (candidate limma precision weights).
- **G4 admissibility verdict = PASS.** Groups **10/10/10/10** from the authoritative SOFT
  `subject status` field (HC / CFS / QFS / **QS** "Q fever seropositive controls"); 40 distinct donors;
  40/40 SOFT samples matched to tar members; **QFS-vs-QS specificity contrast constructable**. Caution:
  filename prefixes are unreliable — `QS` samples are coded **`PQ`**, and `CFS` titles include the
  depositor typos `CSF`/`FCS`. The locked sample sheet (`data/processed/GSE130353/sample_sheet.tsv`)
  is keyed on `subject status`, not filenames.
- **G3 (gene-id harmonization) not yet run** — but de-risked: both sides are mappable to Ensembl
  (U133 probes via GPL96/97; MMSEQ `feature_id` already ENSG, release 68).

These two **public** sets are the reproducible substitute for the declined, author-held Galbraith2011
arrays (`[INACCESSIBLE]` on reproducibility grounds, 2026-06-20). They span **different infectious
triggers**, so a pathway/gene-set-overlap test across them is a concrete step toward the ≥3-trigger
test in `question:0001` / `hypothesis:0001`.

## GSE14577 — post-infectious CFS PBMC microarray

- **Source paper:** Gow2009 (`cite:Gow2009`), *BMC Med Genomics* 2:38 — "A gene signature for
  post-infectious chronic fatigue syndrome."
- **Accession:** GEO **GSE14577** — <https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE14577>
- **Platform:** Affymetrix U133A / U133B (GPL96 / GPL97).
- **Samples:** n = 8 PI-CFS + 7 healthy controls; **male-only**; Fukuda criteria.
- **Trigger:** post-viral (post-infectious CFS).
- **Access:** public, downloadable. **Caveats:** small n, sex skew (male-only), no stated FDR in the
  source paper, low cross-study concordance → **exploratory / hypothesis-generating only**.

## GSE130353 — QFS/CFS monocyte RNA-seq

- **Source paper:** Raijmakers2019 (`cite:Raijmakers2019`), *J Transl Med* — QFS↔CFS monocyte
  transcriptome (humanin/MT-RNR2, MOTS-c/MT-RNR1 downregulation).
- **Accession:** GEO **GSE130353** — <https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE130353>
- **Platform:** RNA-seq (monocytes).
- **Samples:** QFS + CFS + asymptomatic-seropositive + healthy controls.
- **Trigger:** post-bacterial (*Coxiella burnetii*, QFS) + idiopathic CFS.
- **Access:** public, downloadable. **Caveat:** the shared mitochondrial-peptide signal is **not
  fatigue-specific** (asymptomatic seropositive controls also show it).

## Cross-set handling (load-bearing)

- **Do not naively merge** — microarray (GSE14577) vs RNA-seq (GSE130353) are not probe/gene
  comparable. Compare at **pathway / gene-set level** (GSEA/ORA on immune, oxidative-stress,
  mitochondrial, apoptosis modules), per t035.
- Both are strong **commons-promotion candidates** once provisioned (public post-infective-fatigue
  transcriptomes reusable by `health-immunity` / `pan-disease`), but only after the readiness gate is
  met: staged local file + structural QA + datapackage with hashes/provenance + access recorded.

## Related

- Tasks: t035 (pathway-level reanalysis).
- Questions: `question:0001-shared-molecular-signature-across-triggers`.
- Hypotheses: `hypothesis:0001-shared-dysregulated-attractor`.
- Discussion: `discussion:0002-cross-pathogen-pais-signature-convergence`.
