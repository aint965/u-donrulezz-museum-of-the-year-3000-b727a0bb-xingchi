"""Museum of the Year 3000 — entry program.

Writes a single museum label (one line, 1-200 characters, UTF-8) to
<OUTPUT_DIR>/entry.txt. The output directory defaults to /output and can
be overridden with the OUTPUT_DIR environment variable.
"""

import os

LABEL = "Toothbrush, c. 2025. A bristled wand dragged across the bones in the human mouth, twice a day, for life."


def main() -> None:
    if not 1 <= len(LABEL) <= 200:
        raise SystemExit(
            f"Label must be 1-200 characters, got {len(LABEL)}: {LABEL!r}"
        )
    if "\n" in LABEL or "\r" in LABEL:
        raise SystemExit("Label must be a single line")

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LABEL + "\n")


if __name__ == "__main__":
    main()
