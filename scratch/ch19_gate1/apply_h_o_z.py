#!/usr/bin/env python
"""Apply Ch19 Pass-1 sessions 1-H / 1-O / 1-Z to the working inventory.

Deterministic, idempotent-by-inspection transform:
  1-O  reclassify the 14 section-opening sentences to Type: opener, and the 4
       marginal contents-column entries from opener -> contents (they are not
       section openers; counting them as such inflates the opener census by 4 —
       the Ch13 'a structural finding is not a row' failure in another dress).
  1-O  correct F068's Src page 11 -> 12 (its sentence is printed on p. 12).
  1-Z  fold the 3 SUMMARY-UNIQUE facts that had no row, in Content Order.
  then renumber F001..FNNN contiguously and rewrite every cross-reference
  elsewhere in the file through the old->new map.

Run with the venv interpreter:
  /vercel/share/neetenv/bin/python scratch/ch19_gate1/apply_h_o_z.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

INV = Path("/vercel/share/v0-project/notes/class 11/"
           "Ch19_ChemicalCoordinationAndIntegration/"
           "Ch19_ChemicalCoordinationAndIntegration_inventory.md")

# --- 1-O: the 14 section-opening sentences (old IDs) -------------------------
SECTION_OPENERS = ["F013", "F022", "F029", "F039", "F071", "F077", "F097",
                   "F106", "F114", "F138", "F157", "F168", "F180", "F191"]
# --- 1-O: marginal contents column, NOT section openers ----------------------
CONTENTS_ROWS = ["F008", "F009", "F010", "F011"]
# --- 1-O: page-attribution correction ---------------------------------------
SRC_FIX = {"F068": "12"}

# --- 1-Z: SUMMARY-UNIQUE folds, inserted AFTER the given old ID -------------
FOLDS = [
    ("F124", "19.2.7", "process",
     "These hormones increase alertness, pupilary dilation, piloerection, "
     "sweating, heart beat, strength of heart contraction, rate of respiration, "
     "glycogenolysis, lipolysis, proteolysis.", "12"),
    ("F177", "19.2.10", "concept",
     "Progesterone plays a major role in the maintenance of pregnancy as well "
     "as in mammary gland development and lactation.", "12"),
    ("F188", "19.3", "process",
     "These hormones regulate the secretion of digestive juices and help in "
     "digestion.", "12"),
]

ROW_RE = re.compile(r"^\|\s*(F\d{3})\s*\|")


def main() -> int:
    lines = INV.read_text(encoding="utf-8").splitlines()

    # locate the Facts table body
    start = end = None
    for i, ln in enumerate(lines):
        if ln.strip().startswith("## Facts"):
            start = i
        elif start is not None and ln.strip().startswith("## ") and i > start:
            end = i
            break
    assert start is not None and end is not None, "Facts table not found"

    body, other_idx = [], []
    for i in range(start, end):
        if ROW_RE.match(lines[i].strip()):
            body.append(lines[i])
        else:
            other_idx.append(i)

    def cells(row: str) -> list[str]:
        return [c.strip() for c in row.strip().strip("|").split("|")]

    # ---- 1-O edits -------------------------------------------------------
    out = []
    for row in body:
        c = cells(row)
        rid = c[0]
        if rid in SECTION_OPENERS:
            c[2] = "opener"
        elif rid in CONTENTS_ROWS:
            c[2] = "contents"
        if rid in SRC_FIX:
            c[4] = SRC_FIX[rid]
        out.append(c)

    # ---- 1-Z folds -------------------------------------------------------
    folded = []
    for c in out:
        folded.append(c)
        for after, sec, typ, wording, src in FOLDS:
            if c[0] == after:
                folded.append(["<NEW>", sec, typ, wording, src, "x"])
    assert len(folded) == len(out) + len(FOLDS), "a fold anchor was not found"

    # ---- renumber --------------------------------------------------------
    id_map: dict[str, str] = {}
    for n, c in enumerate(folded, 1):
        new = f"F{n:03d}"
        if c[0] != "<NEW>":
            id_map[c[0]] = new
        c[0] = new

    rendered = ["| " + " | ".join(c) + " |" for c in folded]

    # ---- reassemble the file --------------------------------------------
    new_lines = lines[:start]
    emitted = False
    for i in range(start, end):
        if ROW_RE.match(lines[i].strip()):
            # the table grew, so emit the whole rendered block at the first row
            # position and drop the originals rather than pairing 1:1
            if not emitted:
                new_lines += rendered
                emitted = True
        else:
            new_lines.append(lines[i])
    assert emitted, "no Facts rows found to replace"
    tail_start = len(new_lines)
    new_lines += lines[end:]

    # ---- rewrite cross-references OUTSIDE the Facts table ---------------
    changed = [c for c in id_map.items() if c[0] != c[1]]
    changed.sort(key=lambda kv: -int(kv[0][1:]))  # descending: no clobbering

    def remap(text: str) -> str:
        def sub(m: re.Match) -> str:
            return id_map.get(m.group(0), m.group(0))
        return re.sub(r"F\d{3}", sub, text)

    for i in list(range(0, start)) + list(range(tail_start, len(new_lines))):
        new_lines[i] = remap(new_lines[i])

    INV.write_text("\n".join(new_lines) + "\n", encoding="utf-8")

    print(f"rows before        : {len(body)}")
    print(f"rows after         : {len(rendered)}")
    print(f"folds inserted     : {len(FOLDS)}")
    print(f"IDs that shifted   : {len(changed)}")
    print("ID map (shifted only, ascending):")
    for old, new in sorted(changed, key=lambda kv: int(kv[0][1:])):
        print(f"   {old} -> {new}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
