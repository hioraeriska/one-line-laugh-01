#!/usr/bin/env python3
"""One-Line Laugh Sprint entry.

Writes a single original funny line about everyday life to
$MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8, 1-200 characters).
"""

import os
from pathlib import Path

LINE = "I set five alarms to wake up at seven and snoozed all of them, so technically I woke up five times and still chose sleep every single time."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"line is {len(text)} chars, must be 1-200")
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
