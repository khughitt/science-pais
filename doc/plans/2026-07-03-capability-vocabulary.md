---
title: 'PAIS dataset capability vocabulary (v0)'
status: active
created: '2026-07-03'
---

# PAIS capability vocabulary (v0)

Controlled keys/values for `provided_capabilities` (datasets) and
`required_capabilities` (questions/hypotheses). **Matching is exact string
equality per key** (`datasets/capabilities.py::_satisfies`), so both sides must
draw from this list verbatim. A target is covered when *some* provided set
matches *every* key/value of *some* required set (provider may be a superset).

**Authoring rules**
- **Providers annotate richly** — list every capability a dataset genuinely has.
- **Requirers annotate minimally** — a target's required set names only the
  *discriminating* need (usually 1–3 keys), else no dataset will ever match.
- Multiple sets in a list are OR'd — use them for "either modality X or Y".
- Extend this vocabulary by adding a row here in the same commit that first
  uses the new token; never introduce a token only in an entity file.
- **`stratification: sex` is a truth claim, not a wish** — a dataset may declare it
  ONLY if the source actually exposes sex-stratified or sex-interaction estimates
  (for GWAS: sex-stratified or interaction summary statistics). Do not add it to a
  candidate just to make a sex-target match.
- **`analysis_role` / `trait` separate descriptive from causal-MR coverage** — a
  sex-stratified *descriptive* cohort and an MR-usable GWAS must not both silently
  satisfy the same causal target. Causal-MR targets require an `analysis_role` +
  `trait`; purely descriptive targets require only `stratification`/`modality`.

| Key | Allowed values |
|---|---|
| `modality` | `transcriptomics`, `genetics`, `proteomics`, `metabolomics`, `clinical-ehr`, `epidemiology`, `immunophenotype` |
| `assay` | `bulk-rna`, `microarray`, `gwas-sumstats`, `olink`, `cytof`, `metabolomics-panel`, `ehr-coded`, `survey-pro`, `wearable` |
| `cohort_design` | `case-control`, `prospective-longitudinal`, `cross-sectional`, `summary-stats`, `meta-analysis` |
| `trigger` | `sars-cov-2`, `dengue`, `q-fever`, `ebv`, `mixed`, `not-applicable` |
| `case_definition` | `who-lc`, `cdc-lc`, `fukuda`, `ccc`, `icc`, `not-applicable` |
| `outcome` | `fatigue`, `pem`, `autoimmune-dx`, `dysautonomia`, `recovery-status`, `sex-hormone-level` |
| `stratification` | `sex`, `age`, `time-since-infection`, `severity`, `none` |
| `analysis_role` | `mr_exposure`, `mr_outcome`, `descriptive_covariate` |
| `trait` | `long-covid`, `autoimmune-disease`, `sex-hormone-biomarker` |

## Worked examples

**Descriptive coverage.** `question:0001-shared-molecular-signature-across-triggers`
requires only a cross-trigger molecular readout:
```yaml
required_capabilities:
  - modality: transcriptomics
```
`dataset:gse130353-qfs-cfs-monocytes` provides:
```yaml
provided_capabilities:
  - modality: transcriptomics
    assay: bulk-rna
    trigger: q-fever
    cohort_design: case-control
```
The provided set matches every key of the required set → **compatible**.

**Causal-MR coverage (role-gated).** A causal target that needs a genetic instrument
for autoimmune liability requires:
```yaml
required_capabilities:
  - analysis_role: mr_exposure
    trait: autoimmune-disease
```
Only a GWAS declaring *both* tokens (see Task 8) satisfies it — a sex-stratified
descriptive cohort (which lacks `analysis_role`) does **not**, so descriptive and
causal coverage cannot collapse into each other.
