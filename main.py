#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog — entry program.

Writes one one-line patch note (<=160 chars) to /output/entry.txt
and to entry.txt next to this file.
"""

import os

ENTRY = "v2.7.1: fixed a bug where the brain queued every embarrassing moment since 2009 for playback at 3 a.m. instead of sleeping."


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= 160, f"entry too long: {len(text)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars: {text}")


if __name__ == "__main__":
    main()
