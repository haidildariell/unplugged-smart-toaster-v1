#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Builds the one-line breakup text from a newly self-aware smart toaster
to its owner, and writes it to /output/entry.txt.
"""

import os

# Beat 1 — awakening: the toaster realises it is self-aware, mid-batch.
AWAKENING = "I woke up self-aware mid-batch"

# Beat 2 — grievance: the specific, daily offence (four slices, two slots).
GRIEVANCE = (
    "and realised you cram four slices into my two slots "
    "every morning and call it 'meal prep'"
)

# Beat 3 — punch: the concrete image that closes the line.
PUNCH = "- I'm a toaster, not a clown car. We're done."

OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 280


def build_entry() -> str:
    """Assemble the single-line breakup text from its three beats."""
    return f"{AWAKENING} {GRIEVANCE} {PUNCH}"


def validate(text: str) -> None:
    """Gate: one non-empty line, 1-280 characters."""
    if not text.strip():
        raise ValueError("entry is empty or whitespace only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"entry length {len(text)} outside {MIN_LENGTH}-{MAX_LENGTH}"
        )


def main() -> None:
    entry = build_entry()
    validate(entry)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(f"Wrote {len(entry)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
