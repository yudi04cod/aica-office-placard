#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum placard line for an ordinary office object,
treated as an ancient artifact, to /output/entry.txt.

Deterministic: the same line, byte for byte, on every run.
Standard library only; no network, no randomness, no environment input.
"""

import os

# The placard: a stapler recast as a ritual binding device.
# Catalogue date, material, and donor included, deadpan throughout.
PLACARD = (
    "Stapler, c. 2024 CE. Pressed steel. A binding rite joining two sheets "
    "in eternal union; four unions in ten failed. "
    "Gift of the Accounts Department."
)

MAX_CHARS = 180


def main() -> None:
    line = PLACARD.strip()
    if not line:
        raise SystemExit("placard is empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"placard is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in line or "\r" in line:
        raise SystemExit("placard must be a single line")

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
