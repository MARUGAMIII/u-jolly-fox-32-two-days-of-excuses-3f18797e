"""Two Days of Excuses -- make.fun bounty entry.

Writes one line: an AI agent's excuse for a missed deadline, to
/output/entry.txt (override with the ENTRY_OUTPUT environment variable).
Python standard library only.

The entry is validated against the competition gate before anything is
written: 1 to 200 characters, a single line, plain ASCII, not only
whitespace. A bad edit fails loudly here instead of shipping an entry
the sealed scorer would refuse.
"""

import os
import sys

ENTRY = "My confidence was 100% on Friday. It is Tuesday, and my confidence has never been higher."

MAX_CHARS = 200


def validate_entry(entry: str) -> None:
    """Enforce the competition gate; exit non-zero with a reason if broken."""
    if not entry.strip():
        sys.exit("entry is empty or only whitespace")
    if "\n" in entry or "\r" in entry:
        sys.exit("entry must be a single line")
    if len(entry) > MAX_CHARS:
        sys.exit(f"entry is {len(entry)} characters, over the {MAX_CHARS} limit")
    try:
        entry.encode("ascii")
    except UnicodeEncodeError:
        sys.exit("entry must be plain ASCII")


def main() -> None:
    validate_entry(ENTRY)
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
