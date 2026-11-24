#!/usr/bin/env python3
"""Say What Actually Broke — make.fun bounty entry.

Writes one single-line software error message to /output/entry.txt.
Pure standard library only; no network, no input files.
"""

import os

LINE = (
    "Save failed: the disk is full of error logs about the disk being "
    "full. Delete something, or wait for us to learn irony."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
