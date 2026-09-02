#!/usr/bin/env python3
"""Pass 2 tick screen for Ch6.

For every '## Facts' row, measure whether its wording is present in the
GENERATED PDF's extracted text layer, and tick only the rows that clear the
bar. Rows below the bar are printed for a hand read - they are never ticked
automatically.

This is Pass 2 evidence only (SUPREME COMMAND SS6 Pass 3(b) hard bar): a token
score may LOCATE a suspicious row, it may never CLEAR one at Gate 3.

Run:  /vercel/share/neetenv/bin/python tick_rows.py [--write]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE / "Ch6_AnatomyOfFloweringPlants_inventory.md"
PDF = HERE / "Ch6_AnatomyOfFloweringPlants.pdf"

BAR = 0.80  # fraction of content tokens that must appear in the PDF text

STOP = {
    "a", "an", "and", "are", "as", "at", "be", "been", "by", "can", "do", "does",
    "for", "from", "has", "have", "in", "into", "is", "it", "its", "like", "may",
    "not", "of", "on", "or", "other", "our", "out", "so", "such", "than", "that",
    "the", "their", "them", "there", "these", "they", "this", "to", "up", "was",
    "were", "which", "while", "will", "with", "you", "your", "etc", "also", "both",
}


def norm(s: str) -> str:
    s = s.lower()
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2013", "-").replace("\u2014", "-")
    return re.sub(r"\s+", " ", s)


def toks(s: str) -> list[str]:
    return [t for t in re.findall(r"[a-z0-9]+", norm(s)) if t not in STOP and len(t) > 1]


def pdf_text() -> str:
    import pymupdf

    doc = pymupdf.open(PDF)
    txt = " ".join(doc[i].get_text() for i in range(doc.page_count))
    doc.close()
    txt = txt.replace("-\n", "").replace("\n", " ")
    return norm(txt)


def facts_rows(inv: str) -> list[tuple[int, str, str, str, str]]:
    out = []
    in_facts = False
    for i, line in enumerate(inv.splitlines()):
        low = line.strip().lower()
        if low.startswith("## "):
            in_facts = low.startswith("## facts")
            continue
        if not in_facts or not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or not re.match(r"^f\d{3}$", cells[0].lower()):
            continue
        out.append((i, cells[0], cells[1], cells[2], cells[3]))
    return out


def main() -> int:
    write = "--write" in sys.argv
    inv = INV.read_text(encoding="utf-8")
    full = pdf_text()
    ftoks = set(re.findall(r"[a-z0-9]+", full))

    rows = facts_rows(inv)
    scored: list[tuple[str, float, list[str], str, str]] = []
    for _, fid, sec, typ, wording in rows:
        body = re.sub(r"\((?:source|the source|note|count|qualifier|qualifiers|example|dicot|monocot)[^)]*\)",
                      " ", wording, flags=re.I)
        t = toks(body)
        if not t:
            scored.append((fid, 1.0, [], sec, typ))
            continue
        missing = [x for x in t if x not in ftoks]
        scored.append((fid, 1 - len(missing) / len(t), missing, sec, typ))

    clear = [s for s in scored if s[1] >= BAR]
    flagged = [s for s in scored if s[1] < BAR]

    print(f"rows parsed: {len(rows)}   clear (>= {BAR:.0%}): {len(clear)}   flagged: {len(flagged)}")
    print()
    if flagged:
        print("FLAGGED FOR HAND READ (not auto-ticked):")
        for fid, sc, missing, sec, typ in sorted(flagged, key=lambda x: x[1]):
            print(f"  {fid}  {sc:5.0%}  S{sec} [{typ}]  missing: {', '.join(missing[:14])}")
        print()

    if not write:
        print("(dry run - pass --write to tick the clear rows)")
        return 0

    ok = {fid for fid, sc, *_ in scored if sc >= BAR}
    lines = inv.splitlines()
    in_facts = False
    ticked = 0
    for i, line in enumerate(lines):
        low = line.strip().lower()
        if low.startswith("## "):
            in_facts = low.startswith("## facts")
            continue
        if not in_facts or not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or not re.match(r"^f\d{3}$", cells[0].lower()):
            continue
        if cells[0] in ok and cells[-1].lower() != "x":
            cells[-1] = "x"
            lines[i] = "| " + " | ".join(cells) + " |"
            ticked += 1
    INV.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"ticked {ticked} rows in {INV.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
