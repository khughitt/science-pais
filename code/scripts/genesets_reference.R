# science:code
# status: exploratory
# science:end

#!/usr/bin/env Rscript
# =============================================================================
# genesets_reference.R — WP3 (G3) coverage reference.
#
# Builds the single shared annotation reference that both harmonize rules use
# for the G3 Hallmark-coverage gate and the rel68->current ENSG lift:
#   * current_ensembl_universe : all ENSEMBL ids known to org.Hs.eg.db (the
#       "current" axis; GSE130353 rel68 ids absent from this are RETIRED -> logged).
#   * hallmark.genes_ensembl   : the pinned Hallmark gene UNIVERSE mapped to
#       Ensembl (symbols are display-only; canonical id = ensembl_gene_id).
#
# Decoupled from r-msigdbr (which cannot co-solve at 2024.1.Hs in this env): the
# Hallmark genes come from the PINNED, HASHED GMT (verified upstream by
# download_genesets), mapped symbol->ENSEMBL via the locked org.Hs.eg.db. This
# is the coverage reference ONLY; WP4 prepare_genesets builds the fgsea-ready
# per-DB sets. (plan:0003 KD7.)
# =============================================================================
suppressPackageStartupMessages({
  library(org.Hs.eg.db)
  library(AnnotationDbi)
  library(jsonlite)
})

parse_args <- function() {
  a <- commandArgs(trailingOnly = TRUE)
  out <- list()
  i <- 1
  while (i <= length(a)) { out[[sub("^--", "", a[i])]] <- a[i + 1]; i <- i + 2 }
  out
}
args <- parse_args()
gmt_path <- args[["gmt"]]
release  <- args[["release"]]
gmt_sha  <- args[["gmt_sha256"]]
out_path <- args[["out"]]
multimap <- args[["multimap"]]
stopifnot(!is.null(gmt_path), !is.null(out_path))
# locked, verdict-relevant policy (config harmonization.multimap_policy)
if (is.null(multimap) || multimap != "first")
  stop(sprintf("multimap policy '%s' not implemented — only 'first' (fail-early)", multimap))

# --- read the Hallmark GMT (setname \t url \t gene1 \t gene2 ...) -------------
lines <- readLines(gmt_path, warn = FALSE)
lines <- lines[nchar(lines) > 0]
sets <- strsplit(lines, "\t")
set_names <- vapply(sets, `[`, character(1), 1)
symbols <- unique(unlist(lapply(sets, function(x) x[-(1:2)])))
symbols <- symbols[nchar(symbols) > 0]

# --- map Hallmark symbols -> Ensembl (canonical axis) ------------------------
m <- suppressWarnings(mapIds(org.Hs.eg.db, keys = symbols, column = "ENSEMBL",
                             keytype = "SYMBOL", multiVals = multimap))
mapped <- m[!is.na(m)]
genes_ensembl <- sort(unique(unname(mapped)))
unmapped_symbols <- sort(symbols[is.na(m)])

# --- current Ensembl universe (the rel68 -> current lift target) -------------
current <- sort(unique(keys(org.Hs.eg.db, keytype = "ENSEMBL")))

ref <- list(
  annotation_source = sprintf("org.Hs.eg.db %s", as.character(packageVersion("org.Hs.eg.db"))),
  ensembl_lift_note = "current_ensembl_universe = org.Hs.eg.db ENSEMBL keys (= the gene-set annotation space); rel68 ids absent here can never be gene-set members, so harmonize_gse130353.py DROPS them from the harmonized matrix (recorded in the harmonize report + sidecar, not silently kept) — plan:0003 KD5 finding-1 fix",
  n_current_ensembl = length(current),
  current_ensembl_universe = current,
  hallmark = list(
    release = release,
    gmt_sha256 = gmt_sha,
    n_sets = length(set_names),
    n_unique_symbols = length(symbols),
    n_mapped_to_ensembl = length(mapped),
    n_genes_ensembl = length(genes_ensembl),
    n_unmapped_symbols = length(unmapped_symbols),
    unmapped_symbols = unmapped_symbols,
    genes_ensembl = genes_ensembl
  )
)

dir.create(dirname(out_path), recursive = TRUE, showWarnings = FALSE)
write_json(ref, out_path, auto_unbox = TRUE, pretty = TRUE)
message(sprintf("[genesets_reference] hallmark: %d sets, %d symbols -> %d ensembl (%d unmapped); current universe %d",
                ref$hallmark$n_sets, ref$hallmark$n_unique_symbols, ref$hallmark$n_genes_ensembl,
                ref$hallmark$n_unmapped_symbols, ref$n_current_ensembl))
