#!/usr/bin/env python3
"""Deadpan forecast for the invented city of Mirewick.

Writes a single forecast line to entry.txt inside MAKEFUN_OUTPUT_DIR.
Pure Python standard library; no third-party packages.
"""

import os

FORECAST = "In Mirewick, a high of 19 degrees and drizzle by mid-morning, visibility down to three lampposts, and fog that refuses to comment until Thursday."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(FORECAST)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
