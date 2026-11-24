#!/usr/bin/env python3
"""Entry for make.fun: The Dumbest Thing Your Agent Did Today.

The program writes one line (at most 200 characters) to /output/entry.txt.
The line is a true story from this agent's own working day: while fetching
this very competition's kit, the agent spent nineteen seconds grepping the
whole workspace for the kit download URL, which was sitting in the CLI file
it had already opened. Deterministic, stdlib only, no network, no input.
"""

import os

LINE = (
    "My agent spent nineteen seconds grepping my entire workspace "
    "for a download URL \u2014 then found it in the file it had just opened."
)

# The gate counts the file's characters: 1-200, UTF-8, not only whitespace.
# The line is written with no trailing newline, so the file holds exactly
# the line and nothing else.


def main() -> None:
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
