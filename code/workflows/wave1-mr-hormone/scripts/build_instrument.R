# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
#!/usr/bin/env Rscript
# Build one hormone-stratum MR exposure instrument (plan:0009 Task 2).
#
# Deliberate hormone-local adaptation of the plan:0007 `wave1-mr/scripts/
# build_instrument.R` (isolation convention; the frozen run-of-record is not
# edited). Same mechanics: GWAS-SSF hm_* column resolution -> keep p <
# p_threshold -> LOCAL LD-clump against the staged 1000G-EUR plink panel
# (ieugwasr::ld_clump with a local plink binary + bfile, r2/kb from config) ->
# F = (beta/se)^2. Four load-bearing changes vs plan:0007 (plan:0009 Task 2):
#
#   1. MHC exclusion is OPTIONAL (driven by presence of instrument.mhc_exclude,
#      which is absent for this hormone config: hormones are not HLA-dominated).
#   2. Per-boundary attrition is logged (F2) so a small instrument set is
#      diagnosable as biology/power vs an rsID-join/panel-mismatch artifact;
#      ld_clump's stdout/stderr is captured to a clump-log file.
#   3. Tiered gate, NO weak-abort: weak/underpowered strata are recorded as
#      quarantined (eligible_for_mr: false + reasons), never silently used, but
#      never hard-stop the run. stop() remains for TECHNICAL faults only, and
#      the zero-instrument message distinguishes its two causes (F2).
#   4. A per-stratum JSON sidecar is written next to the instrument TSV.

suppressPackageStartupMessages({
  library(data.table)
  library(ieugwasr)
  library(jsonlite)
})

args <- commandArgs(trailingOnly = TRUE)
get_arg <- function(flag) { i <- match(flag, args); if (is.na(i)) stop(paste("missing", flag)); args[[i + 1L]] }
cfg <- yaml::read_yaml(get_arg("--config"))
stratum <- get_arg("--stratum")
exposure_path <- get_arg("--exposure")
ld_prefix <- get_arg("--ld-prefix")
out_path <- get_arg("--out")
sidecar_path <- get_arg("--sidecar")
clump_log_path <- get_arg("--clump-log")

ins <- cfg$instrument
p_thr <- as.numeric(ins$p_threshold)
mhc <- ins$mhc_exclude                       # NULL for the hormone config (MHC exclusion off, edit #1)
f_min <- as.numeric(ins$f_min)
min_instruments_mr <- as.integer(ins$min_instruments_mr)
target_instruments <- as.integer(ins$target_instruments)

# --- resolve this stratum's spec from config$exposures -----------------------
specs <- cfg$exposures
match_idx <- which(vapply(specs, function(s) identical(s$name, stratum), logical(1)))
if (length(match_idx) != 1)
  stop(sprintf("build_instrument[%s]: stratum not found (or not unique) in config$exposures — HALT", stratum))
spec <- specs[[match_idx]]

# --- column resolution (SSF harmonised names vary) ---------------------------
pick <- function(dt, candidates, what) {
  hit <- candidates[candidates %in% names(dt)]
  if (length(hit) == 0) stop(sprintf("build_instrument[%s]: no column for %s (tried %s) — HALT (technical)",
                                      stratum, what, paste(candidates, collapse = ", ")))
  hit[[1]]
}

raw <- fread(exposure_path, showProgress = FALSE)
col <- list(
  rsid = pick(raw, c("hm_rsid", "rsid", "variant_id"), "rsid"),
  chr  = pick(raw, c("hm_chrom", "chromosome", "chr"), "chrom"),
  pos  = pick(raw, c("hm_pos", "base_pair_location", "position"), "pos"),
  ea   = pick(raw, c("hm_effect_allele", "effect_allele"), "effect_allele"),
  oa   = pick(raw, c("hm_other_allele", "other_allele"), "other_allele"),
  beta = pick(raw, c("hm_beta", "beta"), "beta"),
  se   = pick(raw, c("standard_error", "se"), "se"),
  eaf  = pick(raw, c("hm_effect_allele_frequency", "effect_allele_frequency"), "eaf"),
  pval = pick(raw, c("p_value", "pval", "p"), "pval")
)

# n_missing_rsid is computed from the RAW rsID column, before the completeness
# filter drops rows (F2 — the boundary must be measured pre-drop or it is
# tautologically zero).
n_rows <- nrow(raw)
raw_rsid <- raw[[col$rsid]]
n_missing_rsid <- sum(is.na(raw_rsid) | raw_rsid == "")

std <- data.table(
  SNP = raw_rsid, chr = suppressWarnings(as.integer(raw[[col$chr]])),
  pos = suppressWarnings(as.numeric(raw[[col$pos]])),
  effect_allele = toupper(as.character(raw[[col$ea]])),
  other_allele = toupper(as.character(raw[[col$oa]])),
  beta = as.numeric(raw[[col$beta]]), se = as.numeric(raw[[col$se]]),
  eaf = as.numeric(raw[[col$eaf]]), pval = as.numeric(raw[[col$pval]])
)
rm(raw); gc()

# --- completeness filter ------------------------------------------------------
std <- std[!is.na(SNP) & SNP != "" & !is.na(beta) & !is.na(se) & se > 0 & !is.na(pval)]
n_complete <- nrow(std)

# --- genome-wide significance filter ------------------------------------------
gws <- std[pval < p_thr]
n_passing_p <- nrow(gws)

# --- MHC exclusion (edit #1: optional) ----------------------------------------
if (!is.null(mhc)) {
  in_mhc <- !is.na(gws$chr) & gws$chr == as.integer(mhc$chrom) &
            !is.na(gws$pos) & gws$pos >= as.numeric(mhc$start) & gws$pos <= as.numeric(mhc$end)
  cat(sprintf("build_instrument[%s]: %d genome-wide-sig SNPs; dropping %d in MHC chr%s:%s-%s\n",
              stratum, nrow(gws), sum(in_mhc), mhc$chrom, mhc$start, mhc$end))
  gws <- gws[!in_mhc]
} else {
  cat(sprintf("build_instrument[%s]: %d genome-wide-sig SNPs; MHC exclusion off\n", stratum, nrow(gws)))
}
n_clump_input <- nrow(gws)

# --- technical fault: zero GWS variants (cause 1 of 2, F2) --------------------
if (n_passing_p == 0)
  stop(sprintf("build_instrument[%s]: zero genome-wide-significant variants — HALT (technical)", stratum))

# --- local LD clumping (plink + 1000G-EUR bfile), stdout/stderr captured -----
dir.create(dirname(clump_log_path), recursive = TRUE, showWarnings = FALSE)
plink_bin <- unname(Sys.which("plink"))
if (plink_bin == "") {
  writeLines("plink not found on PATH", clump_log_path)
  stop(sprintf("build_instrument[%s]: plink not found on PATH — HALT (technical)", stratum))
}

if (n_clump_input == 0) {
  # MHC exclusion (or upstream filtering) removed every candidate; nothing to
  # feed ld_clump. Record an empty log and fall through to the zero-instrument
  # (cause 2) stop below.
  writeLines(sprintf("build_instrument[%s]: n_clump_input=0, ld_clump not called", stratum), clump_log_path)
  clumped <- gws[0]
} else {
  clump_log_con <- file(clump_log_path, open = "wt")
  sink(clump_log_con, type = "output")
  sink(clump_log_con, type = "message")
  clumped <- tryCatch({
    ld_clump(
      dplyr::tibble(rsid = gws$SNP, pval = gws$pval, id = stratum),
      clump_kb = as.numeric(ins$clump_kb), clump_r2 = as.numeric(ins$clump_r2),
      clump_p = 1, plink_bin = plink_bin, bfile = ld_prefix
    )
  }, error = function(e) {
    sink(type = "message"); sink(type = "output"); close(clump_log_con)
    stop(sprintf("build_instrument[%s]: plink/clump call failed: %s — HALT (technical)",
                 stratum, conditionMessage(e)))
  })
  sink(type = "message")
  sink(type = "output")
  close(clump_log_con)
}

log_lines <- if (file.exists(clump_log_path)) readLines(clump_log_path, warn = FALSE) else character(0)
n_absent_in_panel <- {
  # plink/ld_clump reports SNPs absent from the reference bfile two ways: one
  # "Warning: 'rsXXXX' is not present..." line per missing SNP (whose rsID
  # itself contains digits — do NOT regex-scrape numbers from these lines) and
  # an optional aggregate "N more top variant IDs missing" summary line.
  per_snp <- sum(grepl("^Warning: '[^']+' (is )?(not present|absent)", log_lines, ignore.case = TRUE))
  extra_hits <- regmatches(log_lines, regexpr("([0-9]+)(?=\\s+more\\s+top\\s+variant)", log_lines, perl = TRUE))
  extra_hits <- extra_hits[nzchar(extra_hits)]
  extra <- if (length(extra_hits) > 0) sum(suppressWarnings(as.integer(extra_hits))) else 0L
  if (per_snp > 0 || extra > 0) per_snp + extra else NA_integer_
}

inst <- gws[SNP %in% clumped$rsid]
n_clumped <- nrow(inst)

# --- technical fault: zero instruments post-clump (cause 2 of 2, F2) ---------
if (n_passing_p > 0 && n_clumped == 0)
  stop(sprintf(
    "build_instrument[%s]: all %d genome-wide-significant variants lost in reference matching/clumping (see clump log %s) — HALT (technical)",
    stratum, n_passing_p, clump_log_path
  ))

# --- F-statistics --------------------------------------------------------------
inst[, F := (beta / se)^2]
if (!all(is.finite(inst$F)))
  stop(sprintf("build_instrument[%s]: non-finite F — HALT (technical)", stratum))

if (!is.null(mhc)) {
  if (any(inst$chr == as.integer(mhc$chrom) & inst$pos >= as.numeric(mhc$start) & inst$pos <= as.numeric(mhc$end)))
    stop(sprintf("build_instrument[%s]: an instrument lies in the excluded MHC window (should be impossible) — HALT (technical)", stratum))
}

# --- pval assertion (non-silent) before writing -------------------------------
bad_pval <- inst[pval >= p_thr]
if (nrow(bad_pval) > 0) {
  cat(sprintf("build_instrument[%s]: %d emitted instrument(s) with pval >= p_threshold (%s):\n",
              stratum, nrow(bad_pval), p_thr))
  print(bad_pval[, .(SNP, pval)])
  stop(sprintf("build_instrument[%s]: instrument with pval >= p_threshold — HALT (technical)", stratum))
}

# --- tiered gate, no weak-abort (edit #3) -------------------------------------
n_inst <- nrow(inst)
mean_F <- mean(inst$F)
min_F <- min(inst$F)
max_F <- max(inst$F)

reasons <- character(0)
if (mean_F <= f_min)             reasons <- c(reasons, "weak_mean_f")           # gate: eligible iff mean_F > f_min (F4)
if (n_inst < min_instruments_mr) reasons <- c(reasons, "too_few_instruments")
eligible <- length(reasons) == 0
quality <- if (n_inst < target_instruments) c("below_target_n") else character(0)

cat(sprintf(
  "build_instrument[%s]: n_rows=%d n_complete=%d n_missing_rsid=%d n_passing_p=%d n_clump_input=%d n_clumped=%d n_absent_in_panel=%s\n",
  stratum, n_rows, n_complete, n_missing_rsid, n_passing_p, n_clump_input, n_clumped,
  ifelse(is.na(n_absent_in_panel), "NA", n_absent_in_panel)
))
cat(sprintf(
  "build_instrument[%s]: %d independent instruments; mean F = %.2f; eligible_for_mr=%s reasons=[%s] quality=[%s]\n",
  stratum, n_inst, mean_F, eligible, paste(reasons, collapse = ","), paste(quality, collapse = ",")
))

# --- write the instrument TSV (always, given we reach here with n_inst >= 1) --
dir.create(dirname(out_path), recursive = TRUE, showWarnings = FALSE)
out_dt <- inst[, .(SNP, chr, pos, EA = effect_allele, OA = other_allele, beta, se, eaf, pval, F)]
fwrite(out_dt, out_path, sep = "\t")

# --- per-stratum JSON sidecar (edit #4) ---------------------------------------
sidecar <- list(
  stratum = stratum, accession = spec$accession,
  trait = spec$trait, sex = spec$sex,
  attrition = list(
    n_rows = n_rows, n_complete = n_complete, n_missing_rsid = n_missing_rsid,
    n_passing_p = n_passing_p, n_clump_input = n_clump_input, n_clumped = n_clumped,
    n_absent_in_panel = n_absent_in_panel
  ),
  n_genomewide_sig = n_passing_p, n_instruments = n_inst,
  mean_F = mean_F, min_F = min_F, max_F = max_F,
  clump = list(r2 = as.numeric(ins$clump_r2), kb = as.numeric(ins$clump_kb),
               panel = "1000G-EUR", by = "rsid", clump_log = clump_log_path),
  mhc_excluded = !is.null(mhc),
  eligible_for_mr = eligible, eligibility_reasons = I(reasons),
  quality_flags = I(quality), instrument_tsv = out_path
)
dir.create(dirname(sidecar_path), recursive = TRUE, showWarnings = FALSE)
writeLines(jsonlite::toJSON(sidecar, auto_unbox = TRUE, pretty = TRUE, na = "null"), sidecar_path)
cat("build_instrument: wrote", out_path, "and", sidecar_path, "\n")
