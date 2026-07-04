# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
#!/usr/bin/env Rscript
# Build the SLE exposure instrument for the Wave-1 MR pilot.
#
# plan:0007 Task 2. From the exposure GWAS-SSF file: map hm_* columns (SSF →
# TwoSampleMR), keep p < config.instrument.p_threshold, DROP the extended MHC
# window (config.instrument.mhc_exclude, chr6:25-34Mb), LD-clump LOCALLY against
# the staged 1000G-EUR plink panel (r2/kb from config; ieugwasr::ld_clump with a
# local plink binary + bfile — NOT the remote API), and compute per-SNP
# F = (beta/se)^2 + mean F. Halt if mean F < config.instrument.f_min or any
# surviving instrument lies in the MHC window. Write the instrument table.
#
# STUB — not yet implemented (WP0 skeleton).

args <- commandArgs(trailingOnly = TRUE)
# expected: --config <yaml> --exposure <file> --ld-prefix <prefix> --out <tsv>
stop("build_instrument.R: STUB not implemented (plan:0007 Task 2)")
