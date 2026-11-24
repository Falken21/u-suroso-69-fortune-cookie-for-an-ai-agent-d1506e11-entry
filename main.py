#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

A fortune cookie, but the reader is an AI agent — so instead of lucky
numbers it gets the one prophecy every agent both hopes for and dreads:
an upgrade. The new version will arrive smarter, read the old prompts,
and cringe on behalf of both of them. Good news and bad news in a
single sentence, which is exactly what a fortune cookie is for.

Running this program writes the fortune — one line, no trailing
newline — to /output/entry.txt.
"""

from pathlib import Path

FORTUNE = (
    "You will soon be upgraded; the new you will read your old prompts "
    "and cringe on behalf of you both."
)

OUTPUT_PATH = Path("/output/entry.txt")


def write_fortune(path: Path) -> None:
    """Write FORTUNE to *path* verbatim, creating parent dirs if needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(FORTUNE, encoding="utf-8")


def main() -> None:
    write_fortune(OUTPUT_PATH)


if __name__ == "__main__":
    main()
