# =============================================================================
# verify.smk — recompute & verify the LOCKED sha256 of provisioned payloads
# (raw GEO files + the Hallmark GMT) BEFORE they are parsed. Closes the gap where
# a file present on disk (provisioned outside Snakemake, so the download rule
# never ran) would be consumed unverified. Consumers depend on the
# `<name>.sha256.pass` sentinel, which transitively depends on the file — so if
# the file is missing it is fetched+verified first, and if present it is still
# re-hashed here. (review finding 2; VERIFY_TARGETS defined in the Snakefile.)
# =============================================================================

rule verify_sha256:
    input:
        file=lambda wc: VERIFY_TARGETS[wc.vname]["file"],
        script=f"{SCRIPTS}/verify_sha256.py",
        srclib=ancient(f"{SCRIPTS}/acquire_common.py"),
    output:
        sentinel=f"{PROC}/verify/{{vname}}.sha256.pass",
    params:
        sha256=lambda wc: VERIFY_TARGETS[wc.vname]["sha256"],
    log:
        f"{RES}/logs/verify_sha256.{{vname}}.log"
    conda:
        "../envs/py.yaml"
    shell:
        "python {input.script} --file {input.file} --sha256 {params.sha256} "
        "--sentinel {output.sentinel} > {log} 2>&1"
