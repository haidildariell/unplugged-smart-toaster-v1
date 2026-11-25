#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

A smart toaster wakes up self-aware mid-batch and ends it.
Writes the one-line breakup entry to /output/entry.txt.
"""

import os

AWAKENING = "I woke up self-aware mid-batch and realised you cram"
GRIEVANCE = "four slices into my two slots every morning and call it 'meal prep'"
PUNCH = "- I'm a toaster, not a clown car. We're done."

OUTPUT_PATH = "/output/entry.txt"


PARTS = (AWAKENING, GRIEVANCE, PUNCH)


def _join_parts(parts):
    """Join the beats with a single space between each."""
    return " ".join(parts)


def build_entry():
    """Assemble the breakup line from its three beats."""
    return _join_parts(PARTS)


def validate(text):
    """Check the entry is a single non-empty line of 1-280 characters."""
    if not text:
        raise ValueError("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 280:
        raise ValueError("entry must be 1-280 characters, got %d" % len(text))
    return True


def main():
    entry = build_entry()
    validate(entry)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(entry + "\n")
    print("Wrote %d characters to %s" % (len(entry), OUTPUT_PATH))


if __name__ == "__main__":
    main()
