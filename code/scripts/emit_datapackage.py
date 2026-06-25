# science:code
# status: exploratory
# science:end

#!/usr/bin/env python3
"""Emit a minimal Frictionless datapackage.json for the acquired payloads (t035 WP1).

Discharges the pre-registration:0002 G1 requirement to "record SHA-256 per file
in the datapackage" LITERALLY — one Frictionless resource per acquired payload
carrying `path`, `bytes`, `hash: sha256:…`, and `sources[].path` = the GEO URL.

This is the lighter of the two provenance artifacts: the formal
`mixin-dataset-1.0` commons entity is DEFERRED to promotion (plan:0003 scope
split). Hashes are recomputed from the bytes on disk (authoritative); the
download rule is the integrity gate that put verified bytes there.

Conforms to the Frictionless Data Package descriptor spec (datapackage.org);
written as plain JSON so WP1 is not coupled to a library's inference behavior.
The `frictionless` package remains available in the env for downstream schema
validation.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from acquire_common import SOURCE_URLS, sha256_path

# Human label per acquired payload basename.
PAYLOAD_TITLES = {
    "GSE14577_family.soft.gz": "GEO GSE14577 family SOFT (U133A/B microarray, PI-CFS vs HC)",
    "GSE130353_RAW.tar": "GEO GSE130353 supplementary RAW tar (40 MMSEQ per-donor log_mu members)",
    "GSE130353_family.soft.gz": "GEO GSE130353 family SOFT (authoritative subject status / groups)",
}


def resource_for(payload: Path) -> dict:
    if not payload.exists():
        sys.exit(f"[emit_datapackage] HALT: missing acquired payload {payload}")
    name = payload.name
    url = SOURCE_URLS.get(name)
    if url is None:
        sys.exit(f"[emit_datapackage] HALT: no source URL known for {name}")
    return {
        "name": name.replace("_", "-").replace(".", "-").lower(),
        "path": str(payload).replace("\\", "/"),
        "title": PAYLOAD_TITLES.get(name, name),
        "bytes": payload.stat().st_size,
        "hash": "sha256:" + sha256_path(payload),
        "sources": [{"title": name, "path": url}],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="emit minimal Frictionless datapackage.json")
    ap.add_argument("--payload", required=True, nargs="+", type=Path,
                    help="acquired raw payload(s) to record as resources")
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    resources = [resource_for(p) for p in args.payload]
    descriptor = {
        "name": "t035-cross-trigger-acquisition",
        "title": "t035 cross-trigger pathway-overlap — acquired GEO payloads",
        "description": (
            "Provenance descriptor for the acquired raw inputs to the t035 "
            "cross-trigger pathway-overlap reanalysis (GSE14577 + GSE130353). "
            "One resource per payload with its locked SHA-256 and GEO source URL. "
            "Discharges pre-registration:0002 gate G1."
        ),
        "profile": "data-package",
        "resources": resources,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(descriptor, indent=2, sort_keys=False, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"[emit_datapackage] wrote {args.out} with {len(resources)} resources", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
