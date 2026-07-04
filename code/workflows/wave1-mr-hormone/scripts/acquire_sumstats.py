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


def capture_meta_n(harmonised_dir: str, dest: Path) -> dict:
    """Pull the sibling *-meta.yaml (small) and extract any sample-size fields.

    GWAS-SSF meta files vary; we record whatever sample-size-ish keys are present
    rather than assume a schema. Non-fatal: absence is logged, not a hard stop
    (N can also be read from the outcome dataset entity / DF4 release notes).
    """
    try:
        url = _resolve_in_dir(harmonised_dir, r"\.h\.tsv\.gz-meta\.yaml")
    except SystemExit as e:
        return {"meta_yaml": None, "note": f"no -meta.yaml resolved ({e})"}
    raw = _get(url)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(raw)
    n_fields: dict = {}
    try:
        meta = yaml.safe_load(raw.decode("utf-8", errors="replace")) or {}
        for k, v in (meta.items() if isinstance(meta, dict) else []):
            if re.search(r"(sample_size|n_cas|n_con|ncase|ncontrol|number.*sample)", str(k), re.I):
                n_fields[k] = v
    except Exception as e:  # noqa: BLE001 - meta parsing is best-effort
        n_fields = {"parse_error": str(e)}
    return {"meta_yaml": str(dest), "source_url": url, "sample_size_fields": n_fields}


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
