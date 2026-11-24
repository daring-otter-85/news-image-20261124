#!/usr/bin/env python3
"""Front-page poster entry for the 24 November 2026 news-image bounty.

The poster itself lives in the repository as ``entry.png``.  This
script is only the delivery step: it places an exact copy of that
file at ``/output/entry.png`` so the grader can pick it up.

Nothing here touches the network and nothing is random, so two runs
produce byte-identical output.
"""

import shutil
import sys
from pathlib import Path

POSTER = Path(__file__).resolve().parent / "entry.png"
DESTINATION = Path("entry.png")


def output_dir() -> Path:
    """Where the graded image goes.

    The grading sandbox provides ``/output``; when trying the entry
    out on a laptop, ``MAKEFUN_OUTPUT_DIR`` points it somewhere else
    instead (for example ``MAKEFUN_OUTPUT_DIR=out``).
    """
    import os

    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> int:
    if not POSTER.is_file():
        print(f"poster missing: {POSTER}", file=sys.stderr)
        return 1
    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / DESTINATION
    shutil.copyfile(POSTER, target)
    print(f"wrote {target} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
