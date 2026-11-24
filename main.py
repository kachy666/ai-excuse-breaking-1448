#!/usr/bin/env python3
"""ai-excuse-breaking-1448 — writes the entry line to /output/entry.txt."""

import os

# The joke lands in two beats: the agent confesses it trusted a filename
# the way a human trusts a label — naive machine literalism — and the
# payoff is the worst possible table to lose. No apology, just the logic
# of a machine that reads names and believes them.
# Head-to-head pick over 4 other angles (green dashboard that was down
# too, logs from last Tuesday, cache reset to 2019, tests on the wrong
# repo): this one has the sharpest concrete noun (the .sql filename) and
# the most machine-voice twist — fooled by a name, not by a bug.
LINE = "I ran cleanup_old_data.sql because the filename sounded trustworthy — it deleted the users table."
MAX_CHARS = 180


def main():
    assert LINE, "entry line must not be empty"
    assert "\n" not in LINE, "entry line must be a single line"
    assert len(LINE) <= MAX_CHARS, (
        f"entry line is {len(LINE)} chars, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
