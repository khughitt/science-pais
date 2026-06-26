# science:code
# status: exploratory
# science:end

#!/usr/bin/env Rscript
# =============================================================================
# qa_genesets.R — clean-base QA for the t035 prepared gene-set universe.
#
# Structural failures are build-fatal: the *.qa.pass sentinel is withheld and
# the DAG stops. Distribution-only issues are surfaced in the report. Reports
# are timestamp-free so repeated runs remain diff-stable.
# =============================================================================

parse_args <- function() {
  a <- commandArgs(trailingOnly = TRUE)
  out <- list()
  i <- 1
  while (i <= length(a)) {
    key <- sub("^--", "", a[i])
    out[[key]] <- a[i + 1]
    i <- i + 2
  }
  out
}

csplit <- function(x) strsplit(x, ",", fixed = TRUE)[[1]]

read_kv <- function(path) {
  rows <- read.delim(path, header = FALSE, sep = "\t", stringsAsFactors = FALSE)
  setNames(rows[[2]], rows[[1]])
}

append_report <- function(lines, title, items, pass_line) {
  lines <- c(lines, "", title, "")
  if (length(items)) {
    c(lines, paste0("- ", items))
  } else {
    c(lines, paste0("- ", pass_line))
  }
}

args <- parse_args()
dbs <- csplit(args[["dbs"]])
rds_paths <- csplit(args[["rds"]])
expected_sha <- csplit(args[["expected-sha256s"]])
min_size <- as.integer(args[["min-size"]])
max_size <- as.integer(args[["max-size"]])
report <- args[["report"]]
sentinel <- args[["sentinel"]]

if (length(dbs) != length(rds_paths) || length(dbs) != length(expected_sha)) {
  stop("--dbs, --rds, and --expected-sha256s must have the same length")
}

failures <- character(0)
warnings <- character(0)
facts <- list()
all_sets <- data.frame(db = character(), gene_set = character(), size = integer())

for (i in seq_along(dbs)) {
  db <- dbs[i]
  sets <- readRDS(rds_paths[i])
  if (!is.list(sets)) {
    failures <- c(failures, sprintf("%s: RDS is %s, expected named list", db, paste(class(sets), collapse = "/")))
    next
  }
  if (is.null(names(sets)) || any(!nzchar(names(sets)))) {
    failures <- c(failures, sprintf("%s: all retained sets must be named", db))
  }
  dup <- names(sets)[duplicated(names(sets))]
  if (length(dup)) {
    failures <- c(failures, sprintf("%s: duplicate gene_set names: %s", db, paste(head(unique(dup), 5), collapse = ", ")))
  }

  sizes <- vapply(sets, length, integer(1))
  if (any(sizes < min_size | sizes > max_size)) {
    bad <- names(sets)[sizes < min_size | sizes > max_size]
    failures <- c(failures, sprintf("%s: %d set(s) outside size filter [%d,%d]: %s",
                                    db, length(bad), min_size, max_size, paste(head(bad, 5), collapse = ", ")))
  }
  empty <- names(sets)[sizes == 0L]
  if (length(empty)) {
    failures <- c(failures, sprintf("%s: empty retained set(s): %s", db, paste(head(empty, 5), collapse = ", ")))
  }

  bad_ids <- unique(unlist(lapply(sets, function(x) x[!grepl("^ENSG[0-9]+$", x)]), use.names = FALSE))
  if (length(bad_ids)) {
    failures <- c(failures, sprintf("%s: non-Ensembl member id(s): %s", db, paste(head(bad_ids, 5), collapse = ", ")))
  }

  facts[[db]] <- list(n_sets = length(sets),
                      min_size = if (length(sizes)) min(sizes) else NA_integer_,
                      max_size = if (length(sizes)) max(sizes) else NA_integer_)
  all_sets <- rbind(all_sets, data.frame(db = db, gene_set = names(sets), size = sizes, stringsAsFactors = FALSE))
}

theme_map <- read.delim(args[["theme-map"]], sep = "\t", stringsAsFactors = FALSE)
required_cols <- c("db", "gene_set", "theme", "size")
missing_cols <- setdiff(required_cols, names(theme_map))
if (length(missing_cols)) {
  failures <- c(failures, sprintf("theme_map missing required column(s): %s", paste(missing_cols, collapse = ", ")))
} else {
  key <- paste(all_sets$db, all_sets$gene_set, sep = "\t")
  theme_key <- paste(theme_map$db, theme_map$gene_set, sep = "\t")
  missing_theme <- all_sets$gene_set[!key %in% theme_key]
  extra_theme <- theme_map$gene_set[!theme_key %in% key]
  dup_theme <- theme_key[duplicated(theme_key)]
  if (length(missing_theme)) {
    failures <- c(failures, sprintf("theme_map lacks %d retained set(s): %s",
                                    length(missing_theme), paste(head(missing_theme, 5), collapse = ", ")))
  }
  if (length(extra_theme)) {
    failures <- c(failures, sprintf("theme_map contains %d non-retained set(s): %s",
                                    length(extra_theme), paste(head(extra_theme, 5), collapse = ", ")))
  }
  if (length(dup_theme)) {
    failures <- c(failures, sprintf("theme_map duplicate db/gene_set keys: %s",
                                    paste(head(unique(dup_theme), 5), collapse = ", ")))
  }
  merged <- merge(all_sets, theme_map, by = c("db", "gene_set"), suffixes = c("_rds", "_theme"))
  bad_size <- merged[merged$size_rds != merged$size_theme, ]
  if (nrow(bad_size)) {
    failures <- c(failures, sprintf("theme_map size mismatch for %d retained set(s): %s",
                                    nrow(bad_size), paste(head(bad_size$gene_set, 5), collapse = ", ")))
  }
}

release <- read_kv(args[["release-hash"]])
if (!identical(release[["msigdb_release"]], args[["expected-release"]])) {
  failures <- c(failures, sprintf("msigdb_release %s != expected %s",
                                  release[["msigdb_release"]], args[["expected-release"]]))
}
if (!identical(release[["size_filter"]], sprintf("%d-%d", min_size, max_size))) {
  failures <- c(failures, sprintf("size_filter %s != expected %d-%d",
                                  release[["size_filter"]], min_size, max_size))
}
for (i in seq_along(dbs)) {
  key <- paste0(dbs[i], "_sha256")
  if (!identical(release[[key]], expected_sha[i])) {
    failures <- c(failures, sprintf("%s %s != expected %s", key, release[[key]], expected_sha[i]))
  }
}

verdict <- if (length(failures)) "FAIL (structural)" else "PASS"
report_lines <- c(
  "# Clean gene-set QA report",
  "",
  sprintf("**Verdict:** %s  ", verdict),
  sprintf("**Structural failures:** %d  ", length(failures)),
  sprintf("**Distribution warnings:** %d", length(warnings))
)
report_lines <- append_report(report_lines, "## Structural checks (build-fatal)", failures, "all structural checks passed")
report_lines <- append_report(report_lines, "## Distribution checks (surfaced, not fatal)", warnings, "no distribution warnings")
report_lines <- c(report_lines, "", "## Observed facts", "", "```json")
report_lines <- c(report_lines, jsonlite::toJSON(facts, pretty = TRUE, auto_unbox = TRUE), "```", "")
dir.create(dirname(report), recursive = TRUE, showWarnings = FALSE)
writeLines(report_lines, report)

if (length(failures)) {
  for (f in failures) message("[qa:genesets] STRUCTURAL FAIL ", f)
  message("[qa:genesets] HALT: ", length(failures), " structural failure(s); sentinel withheld. See ", report)
  quit(status = 1)
}

dir.create(dirname(sentinel), recursive = TRUE, showWarnings = FALSE)
writeLines(sprintf("PASS gene-set clean universe: %d DBs, %d retained sets. See %s",
                   length(dbs), nrow(all_sets), report),
           sentinel)
message(sprintf("[qa:genesets] PASS -> %s", sentinel))
