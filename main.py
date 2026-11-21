#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

The joke is a fixed string: the program is fully deterministic and writes
the exact same bytes on every run.
"""

import os
from pathlib import Path

JOKE = (
    "My coding agent crashed the demo, apologised, "
    "and fixed it live \u2014 by deleting the feature we were demoing."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
