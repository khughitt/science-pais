# science:code
# status: workflow-owned
# task_ids: [t117]
# science:end

#!/usr/bin/env Rscript
# =============================================================================
# build_gene_id_map.R — WP1b (b): the SHARED gene-id identity contract.
#
# Builds the symbol/alias/RefSeq -> Ensembl-gene harmonization map that
# stage_matrix.py uses to lift non-Ensembl expression matrices into the ONE
# Ensembl-gene axis the rank universe lives on. It is built from the SAME
# annotation authority the gene sets were mapped with — org.Hs.eg.db (pinned
# 3.22.0 in envs/r-bioc.yaml) — and the SAME multimap policy as
# genesets_reference.R ("first"), so a given source symbol resolves to the SAME
# ENSG on both the expression side and the gene-set side. This is what prevents a
# "parsed successfully but not actually commensurable" failure: identity is a
# contract, not a coincidence.
#
# Output (deterministic -> reproducible sha256):
#   map_tsv    long table: source_id \t source_ns \t ensembl_gene  (sorted, deduped;
#              only ids resolving into the org.Hs.eg.db ENSEMBL universe are kept)
#   report     per-namespace build stats (n_keys, n_mapped, n_ambiguous, version)
#
# multimap "first" mirrors the gene-set build; the ambiguous (1:many) COUNT is
# recorded so stage_matrix can fail closed when a deposit is dominated by
# ambiguous ids. rel-retired / novel ids simply do not appear in the map (they can
# never be gene-set members) — dropped, never silently kept.
# =============================================================================
suppressPackageStartupMessages({
  library(org.Hs.eg.db)
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
keytypes <- strsplit(args[["keytypes"]], ",")[[1]]          # e.g. SYMBOL,ALIAS,REFSEQ
policy   <- args[["multimap"]]                              # locked; must be "first"
out_tsv  <- args[["out-tsv"]]
out_rep  <- args[["out-report"]]
stopifnot(!is.null(out_tsv), !is.null(out_rep))
if (is.null(policy) || policy != "first")
  stop(sprintf("[build_gene_id_map] multimap policy '%s' not implemented — only 'first' (matches genesets_reference.R for commensurability)", policy))

# canonical target axis: exactly the ENSEMBL keys the gene sets were mapped into.
universe <- unique(keys(org.Hs.eg.db, keytype = "ENSEMBL"))

# ns tag used in the map + parse block (SYMBOL->symbol, ALIAS->alias, REFSEQ->refseq)
ns_tag <- function(kt) tolower(kt)

rows <- list()
stats <- list()
for (kt in keytypes) {
  keys_kt <- unique(keys(org.Hs.eg.db, keytype = kt))
  # first-ENSG per source id (deterministic under a pinned org.Hs.eg.db)
  first_map <- suppressWarnings(mapIds(org.Hs.eg.db, keys = keys_kt, column = "ENSEMBL",
                                       keytype = kt, multiVals = "first"))
  # full target list per source id -> per-id ambiguity (n distinct ENSG targets IN
  # universe). n_targets>=2 means the "first" pick is ambiguous; emitted PER ID so a
  # deposit dominated by ambiguous ids can be failed closed (not just a global count).
  list_map <- suppressWarnings(mapIds(org.Hs.eg.db, keys = keys_kt, column = "ENSEMBL",
                                      keytype = kt, multiVals = "list"))
  # per-id ambiguity = number of distinct ENSG targets (non-NA). >=2 => the "first"
  # pick is ambiguous. (Distinct targets, not universe-filtered — a cheap, slightly
  # conservative flag; the emitted rows are still universe-filtered via first_map.)
  n_targets_all <- lengths(lapply(list_map, function(x) unique(x[!is.na(x)])))
  n_ambiguous <- sum(n_targets_all > 1L)

  keep <- !is.na(first_map) & first_map %in% universe
  mapped <- first_map[keep]
  if (length(mapped)) {
    rows[[kt]] <- data.frame(source_id = names(mapped), source_ns = ns_tag(kt),
                             ensembl_gene = unname(mapped),
                             n_targets = n_targets_all[names(mapped)],
                             stringsAsFactors = FALSE)
  }
  stats[[kt]] <- list(keytype = kt, n_keys = length(keys_kt),
                      n_mapped_in_universe = length(mapped), n_ambiguous_1_to_many = n_ambiguous)
}

tab <- do.call(rbind, rows)
tab <- tab[!duplicated(tab[c("source_id", "source_ns")]), ]
tab <- tab[order(tab$source_ns, tab$source_id), ]

dir.create(dirname(out_tsv), recursive = TRUE, showWarnings = FALSE)
# stable, header-first, no row names -> byte-reproducible for a fixed annotation.
con <- file(out_tsv, "w")
writeLines("source_id\tsource_ns\tensembl_gene\tn_targets", con)
writeLines(sprintf("%s\t%s\t%s\t%d", tab$source_id, tab$source_ns, tab$ensembl_gene, tab$n_targets), con)
close(con)

report <- list(
  annotation_source = sprintf("org.Hs.eg.db %s", as.character(packageVersion("org.Hs.eg.db"))),
  multimap_policy = policy,
  n_universe_ensembl = length(universe),
  keytypes = stats,
  n_rows = nrow(tab)
)
write_json(report, out_rep, auto_unbox = TRUE, pretty = TRUE)
message(sprintf("[build_gene_id_map] %d rows across %s; org.Hs.eg.db %s",
                nrow(tab), paste(keytypes, collapse = "/"),
                as.character(packageVersion("org.Hs.eg.db"))))
