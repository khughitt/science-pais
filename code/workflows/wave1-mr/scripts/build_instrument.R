# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
#!/usr/bin/env Rscript
# Build the SLE exposure instrument for the Wave-1 MR pilot (plan:0007 Task 2).
#
# GWAS-SSF hm_* -> fields; keep p < p_threshold; DROP extended MHC (chr6:25-34Mb);
# LD-clump LOCALLY against the staged 1000G-EUR plink panel (ieugwasr::ld_clump
# with a local plink binary + bfile, r2/kb from config); F = (beta/se)^2. Halt if
# mean F < f_min or any surviving instrument is in the MHC window.

suppressPackageStartupMessages({
  library(data.table)
  library(ieugwasr)
})

args <- commandArgs(trailingOnly = TRUE)
get_arg <- function(flag) { i <- match(flag, args); if (is.na(i)) stop(paste("missing", flag)); args[[i + 1L]] }
cfg <- yaml::read_yaml(get_arg("--config"))
exposure_path <- get_arg("--exposure")
ld_prefix <- get_arg("--ld-prefix")
out_path <- get_arg("--out")

ins <- cfg$instrument
p_thr <- as.numeric(ins$p_threshold)
mhc <- ins$mhc_exclude

# --- column resolution (SSF harmonised names vary) ---------------------------
pick <- function(dt, candidates, what) {
  hit <- candidates[candidates %in% names(dt)]
  if (length(hit) == 0) stop(sprintf("build_instrument: no column for %s (tried %s)",
                                      what, paste(candidates, collapse = ", ")))
  hit[[1]]
}

dt <- fread(exposure_path, showProgress = FALSE)
col <- list(
  rsid = pick(dt, c("hm_rsid", "rsid", "variant_id"), "rsid"),
  chr  = pick(dt, c("hm_chrom", "chromosome", "chr"), "chrom"),
  pos  = pick(dt, c("hm_pos", "base_pair_location", "position"), "pos"),
  ea   = pick(dt, c("hm_effect_allele", "effect_allele"), "effect_allele"),
  oa   = pick(dt, c("hm_other_allele", "other_allele"), "other_allele"),
  beta = pick(dt, c("hm_beta", "beta"), "beta"),
  se   = pick(dt, c("standard_error", "se"), "se"),
  eaf  = pick(dt, c("hm_effect_allele_frequency", "effect_allele_frequency"), "eaf"),
  pval = pick(dt, c("p_value", "pval", "p"), "pval")
)

std <- data.table(
  SNP = dt[[col$rsid]], chr = suppressWarnings(as.integer(dt[[col$chr]])),
  pos = suppressWarnings(as.numeric(dt[[col$pos]])),
  effect_allele = toupper(as.character(dt[[col$ea]])),
  other_allele = toupper(as.character(dt[[col$oa]])),
  beta = as.numeric(dt[[col$beta]]), se = as.numeric(dt[[col$se]]),
  eaf = as.numeric(dt[[col$eaf]]), pval = as.numeric(dt[[col$pval]])
)
rm(dt); gc()

# --- filter: genome-wide significant, complete, non-MHC ----------------------
std <- std[!is.na(SNP) & SNP != "" & !is.na(beta) & !is.na(se) & se > 0 & !is.na(pval)]
std <- std[pval < p_thr]
in_mhc <- !is.na(std$chr) & std$chr == as.integer(mhc$chrom) &
          !is.na(std$pos) & std$pos >= as.numeric(mhc$start) & std$pos <= as.numeric(mhc$end)
cat(sprintf("build_instrument: %d genome-wide-sig SNPs; dropping %d in MHC chr%s:%s-%s\n",
            nrow(std), sum(in_mhc), mhc$chrom, mhc$start, mhc$end))
std <- std[!in_mhc]
if (nrow(std) == 0) stop("build_instrument: no SNPs survive p-filter + MHC exclusion")

# --- local LD clumping (plink + 1000G-EUR bfile) -----------------------------
plink_bin <- unname(Sys.which("plink"))
if (plink_bin == "") stop("build_instrument: plink not found on PATH")
clumped <- ld_clump(
  dplyr::tibble(rsid = std$SNP, pval = std$pval, id = "sle"),
  clump_kb = as.numeric(ins$clump_kb), clump_r2 = as.numeric(ins$clump_r2),
  clump_p = 1, plink_bin = plink_bin, bfile = ld_prefix
)
inst <- std[SNP %in% clumped$rsid]

# --- F-statistics + weak-instrument floor ------------------------------------
inst[, F := (beta / se)^2]
mean_F <- mean(inst$F)
cat(sprintf("build_instrument: %d independent instruments; mean F = %.1f\n", nrow(inst), mean_F))
if (any(inst$chr == as.integer(mhc$chrom) & inst$pos >= as.numeric(mhc$start) & inst$pos <= as.numeric(mhc$end)))
  stop("build_instrument: an instrument lies in the excluded MHC window (should be impossible)")
if (mean_F < as.numeric(ins$f_min))
  stop(sprintf("build_instrument: mean F %.1f < floor %s (weak instruments) — HALT", mean_F, ins$f_min))

dir.create(dirname(out_path), recursive = TRUE, showWarnings = FALSE)
fwrite(inst, out_path, sep = "\t")
cat("build_instrument: wrote", out_path, "\n")
