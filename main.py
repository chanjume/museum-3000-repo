#!/usr/bin/env python3
"""Write one museum label for the year 3000 to /output/entry.txt.

Entry (102 chars, limit 200): a deadpan curator's label for a plastic
fork — used once by the wealthy, then buried in landfill in a ritual
called "takeout". The humour is the year 3000 misreading a throwaway
object as a sacred rite of the rich, in the flat voice of a real
museum label.
"""
import os

LINE = "Plastic fork, c. 2024. Used once by the wealthy, then buried in landfill in a ritual called \"takeout.\""


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, limit 200"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars")


if __name__ == "__main__":
    main()
