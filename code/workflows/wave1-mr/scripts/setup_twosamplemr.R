# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
#!/usr/bin/env Rscript
# Install the pinned TwoSampleMR tag into the r-mr conda env's R library.
#
# plan:0007 "Reproducible execution harness": TwoSampleMR is not on conda, so it
# is installed from a pinned GitHub tag via remotes (upgrade = "never") and its
# RESOLVED version is recorded (the sentinel captures it) for run_metadata.json.
# ieugwasr and the remaining CRAN deps are pulled by remotes.
#
# STUB — not yet implemented (WP0 skeleton).

args <- commandArgs(trailingOnly = TRUE)
# expected: --repo MRCIEU/TwoSampleMR --ref <tag> --sentinel <path>
stop("setup_twosamplemr.R: STUB not implemented (plan:0007 execution harness)")
