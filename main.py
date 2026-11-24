#!/usr/bin/env python3
"""news-image-20261124 entry.

Copies the bundled newspaper front-page poster (entry.png) to
/output/entry.png. No network, no randomness: the output bytes are
identical on every run.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    if not os.path.isfile(src):
        raise SystemExit("missing bundled poster: %s" % src)
    # The grader runs with /output writable; locally MAKEFUN_OUTPUT_DIR
    # stands in for it (e.g. MAKEFUN_OUTPUT_DIR=out python3 main.py).
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))


if __name__ == "__main__":
    main()
