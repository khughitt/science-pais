# Pipeline audit synthesis - post-acute-infection

Audit date: 2026-06-26. Scope: workflow code and computational substrates, not new scientific analysis.

## Prioritized refactor backlog

| Rank | Axis | Item | Chains affected | Effort | Task |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | Add clean-base QA checkpoints over prepared gene matrices and mapped gene-set universe. | `t035-gse14577-expression`, `t035-gse130353-expression`, `t035-msigdb-genesets` | medium | t062 |
| 2 | 1/2 | Add downstream analysis/result QA plus an explicit workflow QA target. | `t035-pathway-overlap-analysis` | medium | t063 |
| 3 | 3 | Emit a `results/datapackage.json` manifest for t035 output resources. | `t035-pathway-overlap-analysis` | small/medium | t064 |
| 4 | 3 | Formalize clean-base dataset descriptors and commons-readiness for reusable t035 substrates. | GSE14577, GSE130353, mapped MSigDB universe | medium | t065 |
| 5 | 1 | Add workflow-run provenance entities so `science qa-audit` can inspect t035. | `t035-pathway-overlap-analysis` | small | t066 |
| 6 | 1/2 | Add freshness check for the menopause DAG adjustment-set derivation. | `menopause-dag-adjustment-sets` | small | t067 |
| 7 | 2 | Add lightweight code-to-task comment back-links for t035 workflow files and scripts. | t035 workflow code | small/mechanical | t068 |

## Recurring anti-patterns

- **Transform-side sidecars substituting for checkpoint QA.** Several scripts emit useful sidecars (`cohort_audit.json`, `diag.json`, `run_metadata.json`), but only raw QA and near-zero bimodality have separate sentinel/report behavior. The next improvement is to convert key sidecar expectations into explicit checkpoint rules.
- **Consumer contracts are enforced locally but not reported globally.** Scripts fail early on many schema and vocabulary problems, yet no single QA surface records the complete contract across DE, NES, permutation, specificity, rollup, and verdict outputs.
- **Portability stops at raw-payload provenance.** `data/processed/datapackage.json` records acquired raw inputs; the reusable clean-base outputs and final result bundle do not yet have formal descriptors.
- **Process audit is disconnected from computational runs.** `science qa-audit` cannot inspect this project because there are no authored workflow-run entities.
- **Code provenance is mostly plan-to-code, not code-to-plan.** Plans and tasks refer to the workflow, but workflow files do not yet carry sanctioned task comment back-links.

## Convention nominations (upstream candidates)

| Candidate check | Kind (data-QA / analysis-result-QA / workflow-DAG) | Evidence (chains / bugs caught) | Proposed home |
| --- | --- | --- | --- |
| A reusable gene-expression clean-base QA program for gene-by-sample matrices plus sample sheets. | data-QA | t035 needs the same shape for GSE14577 and GSE130353 after preparation: unique genes, sample-key match, finite-value policy, no all-NA rows, group-count preservation. | `~/d/science/docs/conventions/` or `science_qa` modality pack |
| A gene-set universe QA program for GMT/RDS resources and theme maps. | data-QA | t035 prepared MSigDB universe needs checks for release/hash, size-filter compliance, duplicate set names, non-empty mapped sets, and complete theme assignment. | `science_qa` modality pack |
| A result-bundle QA pattern for pathway-overlap pipelines. | analysis-result-QA | t035 has repeated contracts across `de`, `fgsea`, `concordance`, `perm`, `specificity`, `rollup`, and `verdict`. | `~/d/science/docs/conventions/` after local implementation proves useful |
| A documented workaround for Snakemake cache placement under restricted sandboxes. | workflow-DAG | Dry-run/lint failed until `XDG_CACHE_HOME=/tmp/pais-snakemake-cache` moved Snakemake's runtime source cache to a writable root. | `~/d/science/docs/process/` or agent guidance |

## Commons promotion candidates

| Dataset | Entity exists? | Promoted? | Blocking prerequisites |
| --- | --- | --- | --- |
| GSE14577 prepared gene-expression clean base | No formal clean-base entity; lightweight registry note exists in `doc/datasets/2026-06-20-public-cross-trigger-geo-sets.md` | No | t062 clean-base QA; t065 dataset descriptor/access/license/provenance; commons dry-run |
| GSE130353 prepared gene-expression clean base | No formal clean-base entity; lightweight registry note exists | No | t062 clean-base QA; t065 dataset descriptor/access/license/provenance; commons dry-run |
| Mapped MSigDB 2024.1.Hs gene-set universe used by t035 | No | No | t062 gene-set QA; t065 decide whether local mapped universe is promotable vs merely regenerable from public MSigDB |
| t035 project-specific DE/fgsea/verdict outputs | Not applicable | No | Should not be promoted as clean base data; describe in `results/datapackage.json` via t064 |

## Verification observations

- Snakemake dry-run resolves the t035 DAG when `XDG_CACHE_HOME` is writable: 60 jobs, terminal target `results/verdict.json`, `results/results.md`, `data/processed/datapackage.json`.
- Initial Snakemake dry-run/lint failed only because the default runtime cache path is read-only in this sandbox. With `XDG_CACHE_HOME=/tmp/pais-snakemake-cache`, DAG discovery proceeds.
- Snakemake `--lint` returns one advisory on `rules/common.smk` being a mixed helper file. Current disposition: leave as false-positive/noise because it is already the common helper include that the lint message recommends.
- `science qa-audit --json` cannot run here because `entities/workflow-runs` is absent. This is a process-auditability gap, not a data result issue.
