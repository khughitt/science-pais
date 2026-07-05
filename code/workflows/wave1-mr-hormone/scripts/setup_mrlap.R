# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
#!/usr/bin/env Rscript
# Install MRlap + GenomicSEM (both GitHub-only, no CRAN release) at PINNED
# commits into the r-mrlap conda env, plus their transitive engine
# TwoSampleMR/ieugwasr, and HARD-FAIL unless the resolved commit SHAs AND
# package versions match config (plan:0009 Task 4, MRlap overlap-corrected MR).
#
# Deliberate mirror of `setup_twosamplemr.R` (isolation convention within this
# workflow). MRlap `Imports` TwoSampleMR + ieugwasr and calls
# `TwoSampleMR::mr_ivw()` / `mr_egger_regression()` inside `run_MR` — so the
# corrected arm can drift with those unpinned even when MRlap's SHA is fixed.
# Pinning + asserting all four closes that: the correction-machinery
# reproducibility gate for the whole corrected arm.

args <- commandArgs(trailingOnly = TRUE)
get_arg <- function(flag, default = NULL) {
  i <- match(flag, args)
  if (is.na(i) || i == length(args)) return(default)
  args[[i + 1L]]
}

config_path <- get_arg("--config")
sentinel <- get_arg("--sentinel")
if (is.null(config_path) || is.null(sentinel))
  stop("setup_mrlap.R: --config and --sentinel are required")

cfg <- yaml::read_yaml(config_path)

# --- install in dependency order --------------------------------------------
# 1. TwoSampleMR @ pinned tag (transitive engine MRlap calls; pulls ieugwasr
#    from CRAN via `dependencies = TRUE` — install it explicitly first so the
#    resolved ieugwasr version is captured even if already present).
if (!requireNamespace("ieugwasr", quietly = TRUE)) {
  remotes::install_cran("ieugwasr", upgrade = "never")
}
remotes::install_github(
  paste0(cfg$mrlap_env$twosamplemr_repo, "@", cfg$mrlap_env$twosamplemr_ref),
  upgrade = "never", dependencies = TRUE
)

# 2. GenomicSEM @ pinned commit (MRlap's internal cross-trait LDSC engine).
remotes::install_github(
  paste0(cfg$mrlap_env$genomicsem_repo, "@", cfg$mrlap_env$genomicsem_ref),
  upgrade = "never"
)

# 3. MRlap @ pinned commit.
remotes::install_github(
  paste0(cfg$mrlap_env$mrlap_repo, "@", cfg$mrlap_env$mrlap_ref),
  upgrade = "never"
)

suppressPackageStartupMessages({
  library(TwoSampleMR)
  library(ieugwasr)
  library(GenomicSEM)
  library(MRlap)
})

# --- commit-SHA assert (hard-fail) -------------------------------------------
for (pkg in c("GenomicSEM", "MRlap")) {
  sha  <- utils::packageDescription(pkg)$GithubSHA1
  want <- if (pkg == "MRlap") cfg$mrlap_env$mrlap_ref else cfg$mrlap_env$genomicsem_ref
  if (is.null(sha) || substr(sha, 1, 40) != substr(want, 1, 40))
    stop(sprintf("setup_mrlap: %s GithubSHA1 %s != pinned %s — HALT", pkg, sha, want))
}

# --- transitive-engine version assert (hard-fail) ----------------------------
for (pv in list(c("TwoSampleMR", cfg$mrlap_env$twosamplemr_version_expected),
                c("ieugwasr",   cfg$mrlap_env$ieugwasr_version_expected))) {
  got <- as.character(utils::packageVersion(pv[[1]]))
  if (got != pv[[2]])
    stop(sprintf("setup_mrlap: %s %s != pinned %s — HALT", pv[[1]], got, pv[[2]]))
}

# --- sentinel -----------------------------------------------------------------
mrlap_sha <- utils::packageDescription("MRlap")$GithubSHA1
genomicsem_sha <- utils::packageDescription("GenomicSEM")$GithubSHA1
twosamplemr_version <- as.character(utils::packageVersion("TwoSampleMR"))
ieugwasr_version <- as.character(utils::packageVersion("ieugwasr"))

installed_pkgs <- c("MRlap", "GenomicSEM", "TwoSampleMR", "ieugwasr")
sessionInfo_pkgs <- setNames(
  lapply(installed_pkgs, function(p) as.character(utils::packageVersion(p))),
  installed_pkgs
)

sentinel_data <- list(
  mrlap_sha = mrlap_sha,
  genomicsem_sha = genomicsem_sha,
  mrlap_ref_expected = cfg$mrlap_env$mrlap_ref,
  genomicsem_ref_expected = cfg$mrlap_env$genomicsem_ref,
  twosamplemr_version = twosamplemr_version,
  twosamplemr_version_expected = cfg$mrlap_env$twosamplemr_version_expected,
  ieugwasr_version = ieugwasr_version,
  ieugwasr_version_expected = cfg$mrlap_env$ieugwasr_version_expected,
  sha_and_version_assert_pass = TRUE,
  r_version = as.character(getRversion()),
  sessionInfo_pkgs = sessionInfo_pkgs,
  installed_at_note = format(Sys.time(), tz = "UTC", usetz = TRUE)
)

dir.create(dirname(sentinel), recursive = TRUE, showWarnings = FALSE)
writeLines(jsonlite::toJSON(sentinel_data, auto_unbox = TRUE, pretty = TRUE), sentinel)
cat("setup_mrlap: MRlap", mrlap_sha, "GenomicSEM", genomicsem_sha,
    "TwoSampleMR", twosamplemr_version, "ieugwasr", ieugwasr_version,
    "(SHA+version-assert PASS)\n")
