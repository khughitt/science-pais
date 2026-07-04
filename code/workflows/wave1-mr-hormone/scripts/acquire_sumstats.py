# science:code
# status: workflow-owned
# task_ids: [t089]
# science:end
"""Acquire the plan:0009 harmonised GWAS-SSF sumstats (Arm-B hormone pilot).

plan:0009 Task 1. Generalises the plan:0007 single-pair acquire to a LIST of
exposures (the six Ruth SHBG/testosterone strata) plus the HGI outcome. Each
harmonised deposit uses a different `*.h.tsv.gz` filename, so we resolve the file
from each harmonised directory listing rather than construct it. Download,
SHA-256, stream row count, record build → one manifest. For the outcome we also
pull the sibling `*-meta.yaml` so the case/control N is staged for MRlap total-N
injection (plan:0009 Task 4 / KD-scale). Fail loud on any failure.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import re
import sys
import urllib.request
from pathlib import Path

import yaml

_UA = {"User-Agent": "wave1-mr-hormone/plan-0009 (research; contact via repo)"}


def _get(url: str, timeout: int = 120) -> bytes:
    req = urllib.request.Request(url, headers=_UA)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def _resolve_in_dir(harmonised_dir: str, pattern: str) -> str:
    """Return the absolute URL of the single href matching `pattern` in a dir listing."""
    html = _get(harmonised_dir).decode("utf-8", errors="replace")
    hits = sorted({h for h in re.findall(rf'href="([^"]+{pattern})"', html)})
    if len(hits) != 1:
        raise SystemExit(
            f"acquire: expected exactly one *{pattern} in {harmonised_dir}, found {hits}"
        )
    href = hits[0]
    return href if href.startswith("http") else harmonised_dir.rstrip("/") + "/" + href


def resolve_harmonised_file(harmonised_dir: str) -> str:
    # the data file is `*.h.tsv.gz` but NOT `*.h.tsv.gz-meta.yaml`
    html = _get(harmonised_dir).decode("utf-8", errors="replace")
    hits = sorted({
        h for h in re.findall(r'href="([^"]+\.h\.tsv\.gz)"', html)
        if not h.endswith("-meta.yaml")
    })
    if len(hits) != 1:
        raise SystemExit(
            f"acquire: expected exactly one *.h.tsv.gz in {harmonised_dir}, found {hits}"
        )
    href = hits[0]
    return href if href.startswith("http") else harmonised_dir.rstrip("/") + "/" + href


def download(url: str, dest: Path) -> str:
    """Stream-download to dest; return SHA-256 hex."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    h = hashlib.sha256()
    req = urllib.request.Request(url, headers=_UA)
    with urllib.request.urlopen(req, timeout=600) as resp, open(dest, "wb") as fh:
        while chunk := resp.read(1 << 20):
            fh.write(chunk)
            h.update(chunk)
    return h.hexdigest()


def count_rows(path: Path) -> int:
    """Data rows (excluding header), streamed — never loads the file into memory."""
    n = 0
    with gzip.open(path, "rt") as fh:
        for _ in fh:
            n += 1
    return max(0, n - 1)


def acquire_one(spec: dict, dest: Path) -> dict:
    url = resolve_harmonised_file(spec["harmonised_dir"])
    sha = download(url, dest)
    rec = {
        "accession": spec["accession"],
        "name": spec["name"],
        "source_url": url,
        "local_path": str(dest),
        "sha256": sha,
        "n_rows": count_rows(dest),
        "build": spec["build"],
    }
    for k in ("trait", "sex"):
        if k in spec:
            rec[k] = spec[k]
    return rec


def extract_total_n(meta: object) -> dict:
    """Construct the outcome TOTAL sample size from a parsed GWAS-SSF meta mapping.

    Pure (no I/O), so it is unit-testable against a staged -meta.yaml. MRlap's
    observed-scale overlap correction needs the study TOTAL N (case + control),
    not a case/control split (plan:0009 Task 4 / KD-scale). GWAS-SSF meta files
    carry per-cohort entries under a nested `samples:` list, each with a
    `sample_size` (the cohort case+control total); the study total is their sum.
    Top-level keys are a fallback for other schemas.

    HARD-STOP if no total N can be constructed — Task 4 must receive a
    machine-checked total from this manifest, not fall back to a prose value.

    Note: in this HGI release `samples[*].sample_size` is the per-cohort TOTAL
    only (a `case_control_study` flag is present, but no `n_cases`/`n_controls`),
    so a case/control split is NOT available from the meta and must not be implied.
    """
    if not isinstance(meta, dict):
        raise SystemExit("acquire: outcome -meta.yaml is not a mapping; cannot construct total N — HALT")

    # Nested per-cohort samples[*].sample_size (each a case+control total).
    components = []
    for s in meta.get("samples", []) or []:
        if isinstance(s, dict) and "sample_size" in s:
            anc = s.get("sample_ancestry_category") or s.get("sample_ancestry") or ["unspecified"]
            components.append({
                "ancestry": anc[0] if isinstance(anc, list) and anc else str(anc),
                "sample_size": int(s["sample_size"]),
                "case_control_study": bool(s.get("case_control_study", False)),
            })
    nested_total = sum(c["sample_size"] for c in components) if components else None

    # Fallback: top-level sample-size-ish keys (older/other GWAS-SSF schemas).
    top_fields = {
        k: v for k, v in meta.items()
        if re.search(r"(sample_size|n_cas|n_con|ncase|ncontrol)", str(k), re.I)
    }
    total = nested_total
    if total is None and isinstance(top_fields.get("sample_size"), int):
        total = int(top_fields["sample_size"])
    if total is None:
        raise SystemExit(
            "acquire: could not construct outcome total N from -meta.yaml "
            "(no nested samples[*].sample_size and no top-level sample_size) — HALT"
        )

    return {
        "sample_size_total": total,
        "sample_size_policy": "total_observed_n",
        "sample_size_components": components,
        "case_control_split_available": False,
        "case_control_note": (
            "GWAS-SSF -meta.yaml carries per-cohort TOTAL sample_size only "
            "(case_control_study flag, no n_cases/n_controls); MRlap needs total "
            "observed N, not the split — a case/control breakdown is NOT available here."
        ),
        "top_level_sample_size_fields": top_fields,
    }


def capture_meta_n(harmonised_dir: str, dest: Path) -> dict:
    """Fetch the sibling *-meta.yaml, persist it, and construct the total N."""
    try:
        url = _resolve_in_dir(harmonised_dir, r"\.h\.tsv\.gz-meta\.yaml")
    except SystemExit as e:
        raise SystemExit(
            f"acquire: outcome -meta.yaml not resolved ({e}); cannot construct total N — HALT"
        )
    raw = _get(url)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(raw)
    meta = yaml.safe_load(raw.decode("utf-8", errors="replace")) or {}
    return {"meta_yaml": str(dest), "source_url": url, **extract_total_n(meta)}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    p.add_argument("--out-dir", required=True, help="dir for {name}.{accession}.h.tsv.gz")
    p.add_argument("--manifest", required=True)
    a = p.parse_args()
    cfg = yaml.safe_load(Path(a.config).read_text())
    out_dir = Path(a.out_dir)

    exposures = []
    for spec in cfg["exposures"]:
        dest = out_dir / f"{spec['name']}.{spec['accession']}.h.tsv.gz"
        exposures.append(acquire_one(spec, dest))
        m = exposures[-1]
        sys.stderr.write(f"acquire: exposure {m['name']} {m['accession']} rows={m['n_rows']} sha256={m['sha256'][:12]}…\n")

    ospec = cfg["outcome"]
    odest = out_dir / f"{ospec['name']}.{ospec['accession']}.h.tsv.gz"
    outcome = acquire_one(ospec, odest)
    outcome["meta"] = capture_meta_n(
        ospec["harmonised_dir"],
        out_dir / f"{ospec['name']}.{ospec['accession']}.h.tsv.gz-meta.yaml",
    )
    sys.stderr.write(f"acquire: outcome {outcome['name']} {outcome['accession']} rows={outcome['n_rows']} sha256={outcome['sha256'][:12]}…\n")

    manifest = {"exposures": exposures, "outcome": outcome}
    Path(a.manifest).parent.mkdir(parents=True, exist_ok=True)
    Path(a.manifest).write_text(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
