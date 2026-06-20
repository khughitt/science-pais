#!/usr/bin/env Rscript
# =============================================================================
# harmonize_gse14577.R — WP3 (G3): U133 probes -> canonical ensembl_gene_id.
#
# Maps Affymetrix probes to Ensembl via the locked annotation .db packages
# (GPL96 -> hgu133a.db, GPL97 -> hgu133b.db) and stacks both platforms into ONE
# tidy table on the shared PATIENT axis (chip-A/B GSM columns are relabelled to
# patient_key so WP4 can combine U133A∪B per patient). Probe->gene collapse is
# NOT done here — that is WP4. Unmapped probes are KEPT with an empty
# ensembl_gene_id and LOGGED (never silently dropped).
#
# G3 gate (pre-reg:0002): non-empty harmonized universe + Hallmark coverage.
# Two severities (t037): build-fatal iff the harmonized universe OR the mapped-
# Hallmark intersection is empty (sentinel withheld -> DAG halts); coverage <
# warn threshold is a surfaced warning only.
# =============================================================================
suppressPackageStartupMessages({
  library(hgu133a.db)
  library(hgu133b.db)
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
coverage_warn <- as.numeric(args[["coverage-warn"]])
multimap <- args[["multimap"]]
# locked, verdict-relevant policy (config harmonization.multimap_policy)
if (is.null(multimap) || multimap != "first")
  stop(sprintf("multimap policy '%s' not implemented — only 'first' (fail-early)", multimap))

read_matrix <- function(path) {
  read.delim(gzfile(path), check.names = FALSE, stringsAsFactors = FALSE)
}

# accession -> patient_key (shared axis across the two chips)
meta <- read.delim(args[["meta"]], check.names = FALSE, stringsAsFactors = FALSE)
acc2patient <- setNames(meta$patient_key, meta$accession)
patient_order <- sort(unique(meta$patient_key))

harmonize_platform <- function(path, db, platform) {
  m <- read_matrix(path)
  probes <- m[[1]]
  gsm_cols <- colnames(m)[-1]
  ens <- suppressWarnings(mapIds(db, keys = probes, column = "ENSEMBL",
                                 keytype = "PROBEID", multiVals = multimap))
  ens[is.na(ens)] <- ""
  # relabel GSM value columns -> patient_key, ordered by patient_order
  vals <- m[, gsm_cols, drop = FALSE]
  colnames(vals) <- acc2patient[gsm_cols]
  vals <- vals[, patient_order, drop = FALSE]
  out <- data.frame(platform = platform, probe = probes, ensembl_gene_id = unname(ens),
                    check.names = FALSE, stringsAsFactors = FALSE)
  cbind(out, vals)
}

a <- harmonize_platform(args[["gpl96"]], hgu133a.db, "GPL96")
b <- harmonize_platform(args[["gpl97"]], hgu133b.db, "GPL97")
harm <- rbind(a, b)

# --- mapped/unmapped fractions + Hallmark coverage ---------------------------
ref <- fromJSON(args[["reference"]])
hallmark_ens <- unique(ref$hallmark$genes_ensembl)

n_probes <- nrow(harm)
mapped_mask <- harm$ensembl_gene_id != ""
mapped_ens <- unique(harm$ensembl_gene_id[mapped_mask])
covered <- intersect(hallmark_ens, mapped_ens)
coverage <- if (length(hallmark_ens) > 0) length(covered) / length(hallmark_ens) else 0

failures <- character(0); warnings <- character(0)
if (n_probes == 0 || length(mapped_ens) == 0) failures <- c(failures, "harmonized universe is empty")
if (length(hallmark_ens) > 0 && length(covered) == 0)
  failures <- c(failures, "mapped-Hallmark intersection is empty")
if (coverage < coverage_warn)
  warnings <- c(warnings, sprintf("Hallmark coverage %.3f < warn threshold %.3f", coverage, coverage_warn))

report <- list(
  dataset = "GSE14577",
  canonical_axis = "ensembl_gene_id",
  annotation_source = sprintf("hgu133a.db %s / hgu133b.db %s",
                              as.character(packageVersion("hgu133a.db")),
                              as.character(packageVersion("hgu133b.db"))),
  n_probes_total = n_probes,
  n_probes_mapped = sum(mapped_mask),
  n_probes_unmapped = sum(!mapped_mask),
  frac_probes_mapped = round(mean(mapped_mask), 6),
  n_unique_ensembl_mapped = length(mapped_ens),
  hallmark_coverage = list(
    n_hallmark_ensembl = length(hallmark_ens),
    n_covered = length(covered),
    coverage_fraction = round(coverage, 6),
    warn_threshold = coverage_warn
  ),
  structural_failures = as.list(failures),
  distribution_warnings = as.list(warnings),
  verdict = if (length(failures) == 0) "PASS" else "FAIL (structural)"
)

dir.create(dirname(args[["out-harmonized"]]), recursive = TRUE, showWarnings = FALSE)
# deterministic gzip: `gzip -n` strips the original name + mtime from the header,
# so re-runs are byte-identical (matches the mtime=0 Python writers; KD10).
con <- pipe(sprintf("gzip -n > %s", shQuote(args[["out-harmonized"]])), "w")
write.table(harm, con, sep = "\t", quote = FALSE, row.names = FALSE)
close(con)
write_json(report, args[["out-report"]], auto_unbox = TRUE, pretty = TRUE)

for (w in warnings) message(sprintf("[harmonize_gse14577] WARN %s", w))
if (length(failures) > 0) {
  for (f in failures) message(sprintf("[harmonize_gse14577] STRUCTURAL FAIL %s", f))
  message(sprintf("[harmonize_gse14577] HALT: sentinel withheld. See %s", args[["out-report"]]))
  quit(status = 1)
}
writeLines(sprintf("PASS GSE14577: %d probes (%d mapped) -> %d ensembl; Hallmark coverage %.3f (%d warning(s)).",
                   n_probes, sum(mapped_mask), length(mapped_ens), coverage, length(warnings)),
           args[["sentinel"]])
message(sprintf("[harmonize_gse14577] PASS %d probes, %d mapped -> %d ensembl; hallmark_cov=%.3f",
                n_probes, sum(mapped_mask), length(mapped_ens), coverage))
