# science:code
# status: exploratory
# science:end

#!/usr/bin/env Rscript
# =============================================================================
# prepare_genesets.R — WP4: pinned, size-filtered gene-set universe + theme map.
#
# For EACH database (Hallmark primary; Reactome, GO:BP sensitivities) reads the
# PINNED, HASHED 2024.1.Hs GMT (symbols), maps symbols→Ensembl with the LOCKED
# multimap policy (config harmonization.multimap_policy = "first", applied
# identically to the harmonize step), de-duplicates Ensembl ids within each set,
# applies the LOCKED fgsea size filter (config genesets.size_filter min/max on the
# Ensembl-mapped set size), and writes per-DB .rds (named list of Ensembl vectors).
#
# The release is ASSERTED by hash: each GMT's on-disk sha256 (recomputed here via
# sha256sum) must equal the LOCKED config hash, and is recorded in
# msigdb_release_hash.txt so the overlap denominator cannot drift post-hoc.
#
# theme_map.tsv joins every retained set → its theme via the LOCKED keyword→theme
# regexes (theme_spec.json, sourced verbatim from config / pre-reg:0002), compiled
# PCRE case-insensitive, first-match-wins by precedence, matched against the set
# name uppercased with the collection prefix (HALLMARK_/REACTOME_/GOBP_) stripped.
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
csplit <- function(x) strsplit(x, ",", fixed = TRUE)[[1]]

gmts    <- csplit(args[["gmts"]])
dbs     <- csplit(args[["dbs"]])
sha_cfg <- csplit(args[["sha256s"]])
out_rds <- csplit(args[["out-rds"]])
release <- args[["release"]]
min_size <- as.integer(args[["min-size"]])
max_size <- as.integer(args[["max-size"]])
id_space <- args[["id-space"]]
multimap <- args[["multimap"]]
if (is.null(multimap) || multimap != "first")
  stop(sprintf("multimap policy '%s' not implemented — only 'first' (fail-early)", multimap))
if (!identical(id_space, "symbols"))
  stop(sprintf("gmt_id_space '%s' not implemented — only 'symbols' (fail-early)", id_space))
stopifnot(length(gmts) == length(dbs),
          length(gmts) == length(sha_cfg),
          length(gmts) == length(out_rds))

# locked theme map (verbatim from config via emit_theme_spec.py) ---------------
spec   <- fromJSON(args[["theme-spec"]], simplifyDataFrame = FALSE)
themes <- spec$theme_map                       # already precedence-ordered
strip_prefix <- function(name) sub("^(HALLMARK|REACTOME|GOBP)_", "", toupper(name))
assign_theme <- function(name) {
  key <- strip_prefix(name)
  for (t in themes)
    if (grepl(t$regex, key, perl = TRUE, ignore.case = TRUE)) return(t$theme)
  "other"                                      # precedence-6 catch-all also matches
}

sha256_of <- function(path) sub("\\s.*$", "", system2("sha256sum", shQuote(path), stdout = TRUE))

read_gmt <- function(path) {
  lines <- readLines(path, warn = FALSE)
  lines <- lines[nzchar(lines)]
  parts <- strsplit(lines, "\t", fixed = TRUE)
  setNames(lapply(parts, function(p) p[-(1:2)]),   # drop set name + description
           vapply(parts, `[`, character(1), 1))
}

theme_rows <- list()
release_lines <- c(sprintf("msigdb_release\t%s", release),
                   sprintf("id_space\t%s", id_space),
                   sprintf("multimap_policy\t%s", multimap),
                   sprintf("size_filter\t%d-%d", min_size, max_size))
summary_lines <- character(0)

for (k in seq_along(gmts)) {
  db <- dbs[k]
  observed_sha <- sha256_of(gmts[k])
  if (!identical(observed_sha, sha_cfg[k]))
    stop(sprintf("[prepare_genesets] %s GMT sha256 mismatch: on-disk %s != locked %s",
                 db, observed_sha, sha_cfg[k]))
  release_lines <- c(release_lines, sprintf("%s_sha256\t%s", db, observed_sha))

  sets_sym <- read_gmt(gmts[k])
  # symbols → Ensembl (locked multimap=first): build ONE map over all distinct
  # symbols in the DB, then index per set. multiVals="first" is a pure per-key
  # function, so this is identical to a per-set mapIds but ~1000x fewer calls.
  all_syms <- unique(unlist(sets_sym, use.names = FALSE))
  sym2ens <- suppressMessages(suppressWarnings(
    mapIds(org.Hs.eg.db, keys = all_syms, column = "ENSEMBL",
           keytype = "SYMBOL", multiVals = multimap)))
  sets_ens <- lapply(sets_sym, function(syms) {
    ens <- sym2ens[unique(syms)]
    unique(ens[!is.na(ens) & nzchar(ens)])
  })
  sizes <- vapply(sets_ens, length, integer(1))
  keep  <- sizes >= min_size & sizes <= max_size
  sets_keep <- sets_ens[keep]
  saveRDS(sets_keep, out_rds[k])

  for (nm in names(sets_keep))
    theme_rows[[length(theme_rows) + 1L]] <- data.frame(
      db = db, gene_set = nm, theme = assign_theme(nm),
      size = length(sets_keep[[nm]]), stringsAsFactors = FALSE)

  summary_lines <- c(summary_lines, sprintf(
    "%s: %d sets in GMT -> %d pass size filter [%d,%d] (Ensembl-mapped)",
    db, length(sets_sym), length(sets_keep), min_size, max_size))
}

theme_map <- do.call(rbind, theme_rows)
theme_map <- theme_map[order(theme_map$db, theme_map$gene_set), ]
write.table(theme_map, args[["out-theme-map"]], sep = "\t",
            quote = FALSE, row.names = FALSE)
writeLines(release_lines, args[["out-release-hash"]])

for (s in summary_lines) message(sprintf("[prepare_genesets] %s", s))
message(sprintf("[prepare_genesets] PASS: %d DBs, %d total retained sets, release %s asserted by hash",
                length(gmts), nrow(theme_map), release))
