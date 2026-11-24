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


def validate_entry(text: str) -> None:
    """Self-check: entry must be exactly one line of 1-200 chars.

    Fails loudly with SystemExit (not assert, so it survives `python -O`)
    when the entry would be rejected by the gate.
    """
    if not text or text != text.strip():
        raise SystemExit("entry invalid: must not be empty or padded with whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry invalid: must be a single line, no line breaks")
    if not 1 <= len(text) <= 200:
        raise SystemExit(
            f"entry invalid: {len(text)} chars, must be 1-200 characters"
        )
    if text[-1] not in ".!?":
        raise SystemExit("entry invalid: must end with terminal punctuation")


def main() -> None:
    text = LINE.strip()
    validate_entry(text)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read back and re-validate: what the grader reads must be the entry.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read().rstrip("\n")
    if written != text:
        raise SystemExit("entry invalid: written file does not match validated text")
    validate_entry(written)


if __name__ == "__main__":
    main()
