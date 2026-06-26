# science:code
# status: exploratory
# task: t067
# science:end

"""Fail if the committed menopause DAG adjustment-set artifact is stale."""

from __future__ import annotations

import argparse
import difflib
import pathlib
import shutil
import subprocess
import sys


ROOT = pathlib.Path(__file__).resolve().parents[2]
DEFAULT_DERIVER = ROOT / "code" / "menopause_dag" / "derive_adjustment_sets.py"
DEFAULT_EXPECTED = ROOT / "code" / "menopause_dag" / "adjustment_sets_v2.txt"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--expected",
        type=pathlib.Path,
        default=DEFAULT_EXPECTED,
        help="Committed adjustment-set artifact to compare against.",
    )
    parser.add_argument(
        "--deriver",
        type=pathlib.Path,
        default=DEFAULT_DERIVER,
        help="Script that derives fresh adjustment-set output.",
    )
    return parser.parse_args()


def derive_output(deriver: pathlib.Path) -> str:
    uv = shutil.which("uv")
    if uv is None:
        raise RuntimeError("uv is required to run the PEP 723 DAG derivation script")
    result = subprocess.run(
        [uv, "run", str(deriver)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr or result.stdout)
    return result.stdout


def unified_diff(expected: str, derived: str) -> str:
    return "".join(
        difflib.unified_diff(
            expected.splitlines(keepends=True),
            derived.splitlines(keepends=True),
            fromfile="expected",
            tofile="derived",
        )
    )


def display_path(path: pathlib.Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def main() -> int:
    args = parse_args()
    expected_path = args.expected.resolve()
    deriver = args.deriver.resolve()

    expected = expected_path.read_text(encoding="utf-8")
    derived = derive_output(deriver)
    if expected == derived:
        print(f"fresh: {display_path(expected_path)} matches regenerated DAG adjustment sets")
        return 0

    print(f"stale: {display_path(expected_path)} differs from regenerated DAG adjustment sets", file=sys.stderr)
    print(unified_diff(expected, derived), file=sys.stderr, end="")
    return 1


if __name__ == "__main__":
    sys.exit(main())
