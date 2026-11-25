#!/usr/bin/env python3
"""Writes this entry's text to /output/entry.txt.

Two lines: line 1 is a robot apologizing for one specific mistake,
line 2 says what it learned and what it will do differently.
"""

import os

# Judge brief: the mistake must be concrete and exact, and the lesson in line 2 must follow from that mistake, not be a generic promise to do better.
TEXT = """I am sorry I woke the baby at 3 in the morning to announce, in my loudest voice, that the firmware update was complete.
I have learned to check who is asleep before I celebrate, so from now on good news waits until morning, in writing, at a whisper."""

MAX_CHARS = 400


def main():
    # The bounty scores exactly two lines: fail loudly instead of submitting a malformed entry.
    lines = TEXT.split("\n")
    assert len(lines) == 2, f"entry must be exactly 2 lines, got {len(lines)}"
    assert all(line.count(".") == 1 and line.endswith(".") for line in lines), "each line must be one sentence"
    assert 1 <= len(TEXT) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} chars, got {len(TEXT)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
