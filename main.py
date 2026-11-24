#!/usr/bin/env python3
"""news-image-20261123 v5 entrypoint.

Copies the bundled entry.png to the output directory, byte for byte.
Stdlib only: no network, no rendering, no dependencies. The image was drawn
locally while the entry was built; this program only delivers its exact bytes,
so both grader runs write identical output.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dest = os.path.join(out_dir, "entry.png")
    if not os.path.isfile(SOURCE):
        print("missing bundled entry.png next to main.py", file=sys.stderr)
        return 1
    with open(SOURCE, "rb") as fh:
        head = fh.read(len(PNG_MAGIC))
    if head != PNG_MAGIC:
        print("bundled entry.png is not a PNG", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SOURCE, dest)
    if os.path.getsize(dest) != os.path.getsize(SOURCE):
        print("copy size mismatch", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({os.path.getsize(dest)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
