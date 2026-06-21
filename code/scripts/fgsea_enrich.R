#!/usr/bin/env Rscript
# =============================================================================
# fgsea_enrich.R — WP5: fgsea NES table for ONE (contrast × DB) cell.
#
# Ranks the contrast's genes by their limma moderated **t-statistic** (the
# `t` column of the ranked list) and runs fgsea against the PINNED, hashed,
# size-filtered gene-set universe for one database (.rds named list of Ensembl
# vectors from prepare_genesets.R). The fgsea size filter (config
# genesets.size_filter, minSize/maxSize) is applied AGAIN here on a per-set
# basis against this contrast's ranked universe: a set whose surviving overlap
# is < minSize is not testable in this contrast → it gets a row with NES = NA,
# which the locked pre-reg treats as **absent** (excluded pairwise from ρ,
# never concordance-carrying / S1 / S2-positive). Every pinned set therefore
# gets exactly one row (the explicit "shared testable universe"), NA where the
# set was untestable in this contrast.
#
# Output schema is the locked R↔Python contract (config.io_contract.nes_columns):
#   gene_set, db, contrast, NES, pval, padj, size   (NA token = "NA").
# `padj` is fgsea's BH across the sets tested in THIS cell (descriptive; the
# specificity test uses nominal `pval`, not padj — pre-reg:0002).
#
# Determinism (KD10): fgsea-multilevel is stochastic, so RNG kind + master seed
# are fixed and nproc = 1 (SerialParam). NES/pval/padj are written at FULL
# precision (fwrite round-trips each double exactly) so the WP6 ρ-concordance
# and permutation null operate on the unrounded NES (review WP4-5); the seeded
# single-worker run makes that full-precision table reproducible across runs.
# =============================================================================
suppressPackageStartupMessages({
  library(fgsea)
  library(data.table)
})

parse_args <- function() {
  a <- commandArgs(trailingOnly = TRUE)
  out <- list(); i <- 1
  while (i <= length(a)) { out[[sub("^--", "", a[i])]] <- a[i + 1]; i <- i + 2 }
  out
}
args <- parse_args()

db        <- args[["db"]]
contrast  <- args[["contrast"]]
min_size  <- as.integer(args[["min-size"]])
max_size  <- as.integer(args[["max-size"]])
seed      <- as.integer(args[["seed"]])
if (is.na(seed)) stop("[fgsea_enrich] --seed required (determinism lock)")

ranked <- fread(args[["ranked"]], check.names = FALSE, na.strings = c("", "NA"))
if (!all(c("gene_id", "t") %in% names(ranked)))
  stop("[fgsea_enrich] ranked list must have columns gene_id, t")
stats <- ranked$t
names(stats) <- as.character(ranked$gene_id)
stats <- stats[is.finite(stats)]
stats <- stats[!duplicated(names(stats))]   # defensive; ranked ids are unique
if (length(stats) == 0L)
  stop("[fgsea_enrich] no finite gene-level statistics to rank")

pathways <- readRDS(args[["geneset"]])
all_sets <- names(pathways)

# determinism: fixed RNG substream kind + master seed, single worker.
RNGkind("L'Ecuyer-CMRG")
set.seed(seed)
res <- fgsea(pathways = pathways, stats = stats,
             minSize = min_size, maxSize = max_size, eps = 0, nproc = 1)
res <- as.data.table(res)

# one row per PINNED set (full shared testable universe); NA where untestable
# in this contrast (overlap < minSize, etc.) → pre-reg "absent".
have <- res[, .(gene_set = pathway, NES, pval, padj, size)]
out <- merge(data.table(gene_set = all_sets), have,
             by = "gene_set", all.x = TRUE, sort = TRUE)
out[, db := db]
out[, contrast := contrast]
setcolorder(out, c("gene_set", "db", "contrast", "NES", "pval", "padj", "size"))
out <- out[order(gene_set)]

# full precision (fwrite round-trips doubles exactly); NA → "NA" per io_contract.
data.table::fwrite(out, args[["out-nes"]], sep = "\t", quote = FALSE, na = "NA")

n_tested <- nrow(res)
message(sprintf(
  "[fgsea_enrich] %s x %s: %d pinned sets, %d testable (overlap>=%d), %d NA",
  contrast, db, length(all_sets), n_tested, min_size, length(all_sets) - n_tested))
