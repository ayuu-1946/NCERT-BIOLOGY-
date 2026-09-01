"""Gate 3(b) DIRECTION 2 instrument: source -> inventory, page by page.

This script does NO judging. It only lays the two documents side by side so the
walk can be done by reading:

  LEFT  : every sentence of the NCERT source page, numbered.
  RIGHT : every frozen inventory row whose Source column cites that page.

The verdict for each source sentence ("which row carries this?" / "no row =
UNINVENTORIED") is made by me reading the pair, per the hard bar in the SUPREME
COMMAND: no automated comparison may clear a row.

The inventory's Source column is what makes this possible - it cites page
numbers, so the two documents can be aligned without guessing.
"""
import os
import re

import pymupdf

REPO = "/vercel/share/v0-project"
CH = os.path.join(REPO, "notes/class 11/Ch19_ChemicalCoordinationAndIntegration")
NAME = "Ch19_ChemicalCoordinationAndIntegration"
SRC = os.path.join(REPO, "Chapter/class 11/Chapter 19 - Chemical Coordination and Integration.pdf")
INV = os.path.join(CH, NAME + "_inventory.md")
OUT = os.path.join(REPO, "scratch/ch19_gate3b")

# The source PDF's sheet order vs the printed page numbers the inventory cites.
# Derived, not assumed: printed page numbers are read off the source text layer.


def source_pages():
    doc = pymupdf.open(SRC)
    pages = [p.get_text() for p in doc]
    doc.close()
    return pages


def sentences(txt):
    # Keep headings/labels as their own units: split on blank lines and on
    # sentence enders, but never inside "e.g.," / "Figure 19.1" / "19.2.1".
    txt = re.sub(r"[ \t]+", " ", txt)
    chunks = []
    for para in txt.split("\n"):
        para = para.strip()
        if not para:
            continue
        chunks.append(para)
    # rejoin wrapped lines, then sentence-split
    joined = " ".join(chunks)
    joined = re.sub(r"\s+", " ", joined)
    parts = re.split(r"(?<![A-Z])(?<!e\.g)(?<!i\.e)(?<!etc)(?<!\d)\.(?=\s+[A-Z0-9(])", joined)
    return [p.strip(" .") for p in parts if p.strip(" .")]


def inventory_by_page():
    by = {}
    for line in open(INV, encoding="utf-8"):
        m = re.match(r"^\|\s*(F\d+[a-z]?)\s*\|([^|]*)\|([^|]*)\|(.*)\|([^|]*)\|([^|]*)\|\s*$", line)
        if not m:
            continue
        fid, sec, typ, wording, src, tick = (x.strip() for x in m.groups())
        for pg in re.findall(r"\d+", src):
            by.setdefault(pg, []).append((fid, sec, typ, wording, src))
    return by


def main():
    pages = source_pages()
    inv = inventory_by_page()
    print("inventory rows grouped by cited source page:")
    for pg in sorted(inv, key=int):
        print(f"  p{pg}: {len(inv[pg])} rows")

    # ALIGNMENT KEY, derived not assumed: the inventory's Source column cites
    # p1..p14, and the source PDF has exactly 14 sheets whose printed folios are
    # 239..251. So the citations are SHEET indices, not printed folios. Keying on
    # the printed folio silently produced "0 rows" for all 14 sheets - a loud
    # failure that caught the mistake, which is why the count is printed below.
    for i, txt in enumerate(pages, 1):
        printed = str(i)
        folio = re.findall(r"^\s*(\d{2,3})\s*$", txt, re.M)
        sents = sentences(txt)
        rows = inv.get(printed, [])
        path = os.path.join(OUT, f"pair_sheet{i:02d}.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"===== SOURCE SHEET {i}  (printed page number detected: {printed}) =====\n")
            f.write(f"--- {len(sents)} SOURCE SENTENCES ---\n")
            for j, s in enumerate(sents, 1):
                f.write(f"S{j:03d}. {s}\n")
            f.write(f"\n--- {len(rows)} INVENTORY ROWS CITING p{printed} ---\n")
            for fid, sec, typ, wording, src in rows:
                f.write(f"[{fid}] ({sec} · {typ} · src {src})\n     {wording}\n")
        print(f"  sheet {i:02d} -> printed p{printed}: {len(sents)} sentences, {len(rows)} rows -> {os.path.basename(path)}")


if __name__ == "__main__":
    main()
