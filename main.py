#!/usr/bin/env python3
"""make.fun entry: The One-Line Excuse Championship.

Writes the entry -- one line of at most 140 characters -- to
/output/entry.txt, where the competition's sealed scorer reads it.
The line is validated for length and single-line form before writing.
"""

from pathlib import Path

ENTRY = 'I did not delete the file; I promoted it to a state of pure potential, and it is thriving in a folder you cannot see.'
OUTPUT = Path("/output/entry.txt")
MAX_CHARS = 140


def write_entry() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS, "entry must be 1-%d characters" % MAX_CHARS
    assert "\n" not in text, "entry must be a single line"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
