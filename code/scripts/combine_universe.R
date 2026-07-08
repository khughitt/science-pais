# science:code
# status: workflow-owned
# task_ids: [t117]
# science:end

#!/usr/bin/env Rscript
# =============================================================================
# combine_universe.R — WP1 (t117): materialize the SINGLE pinned gene-set
# universe for the cross-PAIS rank estimand from the plan:0003 mapped clean base.
#
# The plan:0003 clean base is stored as THREE per-DB .rds (Hallmark, Reactome,
# GO:BP — named lists of Ensembl vectors, size-filtered 15-500, hash-locked in
# msigdb_release_hash.txt). t117 needs ONE combined universe. Per the universe
# decision (2026-07-08), that universe = Hallmark ∪ Reactome (the plan:0003
# primary + the high-resolution curated pathway DB), dropping GO:BP's redundant
# ontology so highly-correlated ontology rows cannot inflate apparent low-rank
# structure (the shared-artifact confound the artifact battery guards against).
#
# DETERMINISM (so the pinned sha256 is reproducible by anyone re-running):
#   * inputs are the hash-locked per-DB .rds (asserted against config hashes);
#   * set names are unique across DBs (HALLMARK_/REACTOME_ prefixes) — union by
#     name is collision-free; ties would fail-early;
#   * sets are ordered by name (stable), member ids sorted within each set;
#   * saved with compress = FALSE (no gzip mtime) + serialization version 3, so
#     the on-disk bytes — and thus the sha256 — are a pure function of the inputs.
# Base R only (readRDS/saveRDS) — no Bioconductor deps.
# =============================================================================

parse_args <- function() {
  a <- commandArgs(trailingOnly = TRUE)
  out <- list(); i <- 1
  while (i <= length(a)) { out[[sub("^--", "", a[i])]] <- a[i + 1]; i <- i + 2 }
  out
}
args <- parse_args()
csplit <- function(x) strsplit(x, ",", fixed = TRUE)[[1]]

in_rds  <- csplit(args[["in-rds"]])       # e.g. hallmark.rds,reactome.rds
dbs     <- csplit(args[["dbs"]])          # e.g. hallmark,reactome
sha_cfg <- csplit(args[["sha256s"]])      # locked per-DB GMT-derived .rds hashes
out_rds <- args[["out-rds"]]
stopifnot(length(in_rds) == length(dbs), length(in_rds) == length(sha_cfg))

sha256_of <- function(path) sub("\\s.*$", "", system2("sha256sum", shQuote(path), stdout = TRUE))

universe <- list()
summary_lines <- character(0)
for (k in seq_along(in_rds)) {
  observed <- sha256_of(in_rds[k])
  if (!identical(observed, sha_cfg[k]))
    stop(sprintf("[combine_universe] %s .rds sha256 mismatch: on-disk %s != locked %s",
                 dbs[k], observed, sha_cfg[k]))
  sets <- readRDS(in_rds[k])
  # sort member ids within each set (stable membership regardless of source order)
  sets <- lapply(sets, function(v) sort(unique(as.character(v))))
  clash <- intersect(names(universe), names(sets))
  if (length(clash) > 0L)
    stop(sprintf("[combine_universe] set-name collision across DBs: %s",
                 paste(head(clash, 5), collapse = ", ")))
  universe <- c(universe, sets)
  summary_lines <- c(summary_lines, sprintf("%s: %d sets", dbs[k], length(sets)))
}

# stable order by set name → reproducible serialization
universe <- universe[order(names(universe))]

dir.create(dirname(out_rds), recursive = TRUE, showWarnings = FALSE)
# compress=FALSE removes gzip's nondeterministic mtime header; version=3 is the
# stable R serialization format (R >= 3.5). Bytes are a pure fn of the inputs.
saveRDS(universe, out_rds, compress = FALSE, version = 3)

for (s in summary_lines) message(sprintf("[combine_universe] %s", s))
message(sprintf("[combine_universe] PASS: %d sets -> %s (compress=FALSE, v3)",
                length(universe), out_rds))
