# Public cross-trigger post-infective-fatigue expression datasets — registry note

**Status:** candidate datasets, not yet provisioned. This is a lightweight registry note, **not** a
validated dataset entity. Formal `mixin-dataset-1.0` entities + Frictionless datapackages are deferred
until the data is downloaded under a workflow run (see the commons-readiness gate in
`~/d/science/docs/process/pipeline-audit-and-refactor.md`). Tracked for **t035**.

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
