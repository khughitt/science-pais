# science:code
# status: workflow-owned
# task_ids: [t117]
# science:end

#!/usr/bin/env Rscript
# =============================================================================
# harmonize_microarray.R — WP1b tranche (c): single-platform probe -> Ensembl.
#
# Maps a microarray probe x sample table onto the canonical ensembl_gene_id axis
# via the platform's LOCKED Bioconductor annotation .db package (e.g. GPL570 ->
# hgu133plus2.db), pinned in envs/r-bioc.yaml. multimap "first" mirrors
# genesets_reference.R / build_gene_id_map.R (commensurability by construction).
# Emits the [platform, probe, ensembl_gene_id, <sample cols...>] shape that
# collapse_probes.R consumes for the probe->gene median collapse. Unmapped probes
# are KEPT with an empty ensembl_gene_id and LOGGED (collapse_probes drops them,
# counted) — never silently discarded here.
#
# NOTE: the platform annotation .db (hgu133*.db) is DISTINCT from the org.Hs.eg.db
# symbol/RefSeq map (tranche b) — microarray identity is probe-based, so it needs
# the probe->gene package, not the symbol map. Single-platform only (one .db); the
# dual-chip U133A∪B combine (GSE14577) stays in the bespoke harmonize_gse14577.R.
# =============================================================================
suppressPackageStartupMessages({
  library(AnnotationDbi)
  library(jsonlite)
})

parse_args <- function() {
  a <- commandArgs(trailingOnly = TRUE)
  out <- list(); i <- 1
  while (i <= length(a)) { out[[sub("^--", "", a[i])]] <- a[i + 1]; i <- i + 2 }
  out
}
args <- parse_args()
db_pkg   <- args[["db"]]         # e.g. hgu133plus2.db
platform <- args[["platform"]]   # e.g. GPL570 (label carried into the collapse input)
multimap <- args[["multimap"]]   # locked; must be "first"
if (is.null(multimap) || multimap != "first")
  stop(sprintf("[harmonize_microarray] multimap policy '%s' not implemented — only 'first'", multimap))
if (is.null(db_pkg) || is.null(platform))
  stop("[harmonize_microarray] --db and --platform are required")
suppressPackageStartupMessages(library(db_pkg, character.only = TRUE))
db <- get(db_pkg)

# probe x sample (env has no R.utils, so fread .gz via `gzip -dc`; keep col names)
m <- read.delim(gzfile(args[["probe-expr"]]), check.names = FALSE, stringsAsFactors = FALSE)
probes <- as.character(m[[1]])
sample_cols <- colnames(m)[-1]

ens <- suppressWarnings(mapIds(db, keys = probes, column = "ENSEMBL",
                               keytype = "PROBEID", multiVals = multimap))
ens[is.na(ens)] <- ""

harm <- data.frame(platform = platform, probe = probes, ensembl_gene_id = unname(ens),
                   check.names = FALSE, stringsAsFactors = FALSE)
harm <- cbind(harm, m[, sample_cols, drop = FALSE])

n_probes <- nrow(harm)
mapped_mask <- harm$ensembl_gene_id != ""
mapped_ens <- unique(harm$ensembl_gene_id[mapped_mask])
failures <- character(0)
if (n_probes == 0 || length(mapped_ens) == 0)
  failures <- c(failures, "harmonized universe is empty")

report <- list(
  platform = platform,
  annotation_source = sprintf("%s %s", db_pkg, as.character(packageVersion(db_pkg))),
  multimap_policy = multimap,
  n_probes_total = n_probes,
  n_probes_mapped = sum(mapped_mask),
  n_probes_unmapped = sum(!mapped_mask),
  frac_probes_mapped = round(mean(mapped_mask), 6),
  n_unique_ensembl_mapped = length(mapped_ens),
  structural_failures = as.list(failures),
  verdict = if (length(failures) == 0) "PASS" else "FAIL (structural)"
)

dir.create(dirname(args[["out-harmonized"]]), recursive = TRUE, showWarnings = FALSE)
# deterministic gzip (`gzip -n`: no name/mtime) so re-runs are byte-identical (KD10).
con <- pipe(sprintf("gzip -n > %s", shQuote(args[["out-harmonized"]])), "w")
write.table(harm, con, sep = "\t", quote = FALSE, row.names = FALSE)
close(con)
write_json(report, args[["out-report"]], auto_unbox = TRUE, pretty = TRUE)

if (length(failures) > 0) {
  for (f in failures) message(sprintf("[harmonize_microarray] STRUCTURAL FAIL %s", f))
  message(sprintf("[harmonize_microarray] HALT: see %s", args[["out-report"]]))
  quit(status = 1)
}
message(sprintf("[harmonize_microarray] PASS %s/%s: %d probes, %d mapped -> %d ensembl",
                platform, db_pkg, n_probes, sum(mapped_mask), length(mapped_ens)))
