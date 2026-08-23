"""Session 1-Z helper: locate the frozen Facts rows that support each
exercise-gap term, so the 'Explained where' column points at real row IDs
rather than at a remembered impression.

Usage:  /vercel/share/neetenv/bin/python scratch/ch7_1z/find_rows.py
"""
import re
import sys
import os

INV = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "notes", "class 12", "Ch7_HumanHealthAndDisease",
    "Ch7_HumanHealthAndDisease_inventory.md",
)

ROW = re.compile(r"^\|\s*(F\d{3})\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*(.*?)\s*\|\s*([^|]*?)\s*\|\s*$")

TERMS = [
    "MALT",
    "cell-mediated immunity",
    "CMI",
    "NACO",
    "primary lymphoid",
    "secondary lymphoid",
    "metastasis",
    "Recombinant DNA",
    "hepatitis B",
    "public hygiene",
    "Acquired Immuno",
    "immuno-deficiency",
    "amoebiasis",
    "ascariasis",
    "pneumonia",
    "innate immunity",
    "acquired immunity",
    "active immunity",
    "passive immunity",
    "typhoid",
    "water",
]


def rows():
    out = []
    with open(INV, encoding="utf-8") as fh:
        for line in fh:
            m = ROW.match(line.rstrip("\n"))
            if m:
                out.append(m.groups())
    return out


def main():
    all_rows = rows()
    print(f"parsed {len(all_rows)} table rows from inventory\n")
    for term in TERMS:
        hits = [r for r in all_rows if term.lower() in r[3].lower()]
        ids = " ".join(h[0] for h in hits)
        print(f"{term:26s} {len(hits):3d}  {ids}")


if __name__ == "__main__":
    sys.exit(main())
