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

# --- install in dependency order (idempotent + retrying) ---------------------
# The three GitHub installs are the flaky, network-bound step (a transient
# api.github.com/codeload failure on any one tarball aborts the whole rule). So
# each install is (a) SKIPPED when the package is already present at the pinned
# SHA/version — making a re-run fetch only what is actually missing — and
# (b) RETRIED on failure. The four hard-fail asserts below remain the gate; this
# only changes HOW we reach a correctly-pinned library, never WHETHER we verify it.
retries <- 3L
retry_sleep_s <- 20

with_retry <- function(expr, what) {
  for (attempt in seq_len(retries)) {
    ok <- tryCatch({ force(expr); TRUE },
                   error = function(e) {
                     message(sprintf("setup_mrlap: %s failed (attempt %d/%d): %s",
                                     what, attempt, retries, conditionMessage(e)))
                     FALSE
                   })
    if (isTRUE(ok)) return(invisible(TRUE))
    if (attempt < retries) Sys.sleep(retry_sleep_s)
  }
  stop(sprintf("setup_mrlap: %s failed after %d attempts — HALT", what, retries))
}

installed_sha <- function(pkg) {
  if (!requireNamespace(pkg, quietly = TRUE)) return(NA_character_)
  sha <- utils::packageDescription(pkg)$GithubSHA1
  if (is.null(sha)) NA_character_ else substr(sha, 1, 40)
}
installed_version <- function(pkg) {
  if (!requireNamespace(pkg, quietly = TRUE)) return(NA_character_)
  as.character(utils::packageVersion(pkg))
}

# 1. TwoSampleMR @ pinned tag (transitive engine MRlap calls; pulls ieugwasr
#    from CRAN via `dependencies = TRUE`). Install ieugwasr explicitly first so
#    its version is captured even if already present.
if (!requireNamespace("ieugwasr", quietly = TRUE)) {
  with_retry(remotes::install_cran("ieugwasr", upgrade = "never"), "ieugwasr (CRAN)")
}
if (identical(installed_version("TwoSampleMR"), cfg$mrlap_env$twosamplemr_version_expected)) {
  message("setup_mrlap: TwoSampleMR ", cfg$mrlap_env$twosamplemr_version_expected,
          " already installed — skipping")
} else {
  with_retry(remotes::install_github(
    paste0(cfg$mrlap_env$twosamplemr_repo, "@", cfg$mrlap_env$twosamplemr_ref),
    upgrade = "never", dependencies = TRUE
  ), "TwoSampleMR (GitHub)")
}

# 2. GenomicSEM @ pinned commit (MRlap's internal cross-trait LDSC engine).
if (identical(installed_sha("GenomicSEM"), substr(cfg$mrlap_env$genomicsem_ref, 1, 40))) {
  message("setup_mrlap: GenomicSEM @ pinned SHA already installed — skipping")
} else {
  with_retry(remotes::install_github(
    paste0(cfg$mrlap_env$genomicsem_repo, "@", cfg$mrlap_env$genomicsem_ref),
    upgrade = "never"
  ), "GenomicSEM (GitHub)")
}

# 3. MRlap @ pinned commit.
if (identical(installed_sha("MRlap"), substr(cfg$mrlap_env$mrlap_ref, 1, 40))) {
  message("setup_mrlap: MRlap @ pinned SHA already installed — skipping")
} else {
  with_retry(remotes::install_github(
    paste0(cfg$mrlap_env$mrlap_repo, "@", cfg$mrlap_env$mrlap_ref),
    upgrade = "never"
  ), "MRlap (GitHub)")
}

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
