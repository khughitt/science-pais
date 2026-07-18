#!/usr/bin/env Rscript
# science:code
# status: workflow-owned
# task_ids: [t139]
# science:end
#
# Generate the pinned Ensembl-gene-id <-> HGNC-symbol map DETERMINISTICALLY from
# the env-pinned bioconductor-org.Hs.eg.db (== version is fixed in envs/r-sc.yaml),
# so the map's provenance is a package version, not a flaky download. The emitted
# TSV is sorted (stable byte order) and then hashed + locked into config.yaml
# (refs.gene_map.sha256). Consumed at PROJECTION time (Step 3+); pinned now.

suppressPackageStartupMessages({
  library(org.Hs.eg.db)
  library(AnnotationDbi)
  library(jsonlite)
})

args <- commandArgs(trailingOnly = TRUE)
out <- args[which(args == "--out") + 1]
prov <- args[which(args == "--provenance") + 1]

keys <- keys(org.Hs.eg.db, keytype = "ENSEMBL")
df <- AnnotationDbi::select(org.Hs.eg.db, keys = keys,
                            columns = c("ENSEMBL", "SYMBOL"),
                            keytype = "ENSEMBL")
df <- df[!is.na(df$ENSEMBL) & !is.na(df$SYMBOL), c("ENSEMBL", "SYMBOL")]
df <- unique(df)
# Deterministic order → stable hash across runs of the same pinned package.
df <- df[order(df$ENSEMBL, df$SYMBOL), ]

dir.create(dirname(out), recursive = TRUE, showWarnings = FALSE)
write.table(df, out, sep = "\t", quote = FALSE, row.names = FALSE)

writeLines(toJSON(list(
  source_pkg = "org.Hs.eg.db",
  pkg_version = as.character(packageVersion("org.Hs.eg.db")),
  n_pairs = nrow(df),
  n_ensembl = length(unique(df$ENSEMBL)),
  n_symbol = length(unique(df$SYMBOL)),
  out = out
), auto_unbox = TRUE, pretty = TRUE), prov)

cat(sprintf("[genemap] wrote %d Ensembl<->symbol pairs from org.Hs.eg.db %s\n",
            nrow(df), as.character(packageVersion("org.Hs.eg.db"))))
