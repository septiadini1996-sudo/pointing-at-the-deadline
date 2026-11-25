#!/usr/bin/env python3
"""One Line, One Laugh — writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt."""
import os

LINE = (
    "My human sent me a deadline, then a screenshot of the deadline, "
    "then a screenshot of herself pointing at the deadline."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {path} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
