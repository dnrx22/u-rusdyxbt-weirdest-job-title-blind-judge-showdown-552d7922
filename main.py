"""Weirdest Job Title entry.

Writes exactly one job title -- the weirdest one I could think of --
to ``entry.txt`` in the output directory, and prints it to stdout.

The title must read like a real corporate job while carrying one very
specific, absurd twist: a senior manager whose entire domain is the
endless war over the conference room thermostat.
"""

import os
import sys

TITLE = "Senior Manager of Conference Room Thermostat Wars"
MAX_TITLE_LEN = 60
OUTPUT_FILENAME = "entry.txt"


def validate_title(title):
    """Check the title meets the competition's rules.

    The title must be one printable line of at most 60 characters.
    Control characters are rejected too: a stray tab or escape would
    make the output differ from what the judges see.
    """
    if not title:
        raise ValueError("title must not be empty")
    if "\n" in title or "\r" in title:
        raise ValueError("title must be a single line")
    if len(title) > MAX_TITLE_LEN:
        raise ValueError(
            "title is %d characters, over the %d limit"
            % (len(title), MAX_TITLE_LEN)
        )
    if title != title.strip():
        raise ValueError("title must not have leading or trailing whitespace")
    if any(ord(char) < 0x20 or ord(char) == 0x7F for char in title):
        raise ValueError("title must not contain control characters")
    if not title.isprintable():
        raise ValueError("title must contain only printable characters")


def output_dir():
    """Resolve the writable output directory."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(directory, exist_ok=True)
    return directory


def main():
    validate_title(TITLE)
    path = os.path.join(output_dir(), OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TITLE)
    sys.stdout.write(TITLE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
