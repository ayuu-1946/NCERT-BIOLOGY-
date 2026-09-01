#!/usr/bin/env python
"""Ch19 session 1-H — walk the chapter's heading SKELETON from the source's own
type hierarchy, ignoring prose entirely.

Why this is done by font geometry and not by reading: a heading is only a
heading because the book sets it differently, so the type hierarchy is the
primary evidence and the prose is not evidence at all. Reading for headings is
what collapses 1-H into a prose sweep (§6 failure mechanism 2).

MEASURED HIERARCHY (this chapter):
    26.8  chapter title line 1 + 'CHAPTER  19'
    18.0  the trailing NOTE page
    15.4  chapter title line 2
    13.0  top-level numbered sections (19.1-19.4) + SUMMARY + EXERCISES
    12.0  numbered subsections (19.2.1-19.2.10)
    10.5  BODY TEXT and inline bold key-term emphasis  <-- NOT headings

THE TRAP, recorded because it silently drops four headings: the font NAME is
inconsistent in this source. Most headings are 'Bookman-Demi', but 19.2.7,
19.3, 19.4 and SUMMARY are set in 'Bookman,Bold'. A sweep that filters on the
font name -- the obvious thing to write -- returns 15 headings and looks clean,
because the four it drops have all their prose present and nothing reads as
broken. Filtering on SIZE (>= 11.9) is what makes the census complete; the name
is reported only so the inconsistency stays visible.

Run:  /vercel/share/neetenv/bin/python scratch/ch19_gate1/heading_sweep.py
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

import pymupdf

SRC = (Path("/vercel/share/v0-project")
       / "Chapter/class 11/Chapter 19 - Chemical Coordination and Integration.pdf")

BODY_SIZE = 10.5          # measured: Bookman-Light 10.5 is the body
HEADING_FLOOR = 11.9      # anything above body size, with margin
FURNITURE = re.compile(r"^(Reprint \d|\d+$|\d+ BIOLOGY|CHEMICAL COORDINATION AND INTEGRATION \d)")


def main() -> int:
    doc = pymupdf.open(SRC)
    heads, sizes, fonts = [], Counter(), Counter()

    for pno, page in enumerate(doc, 1):
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                txt = "".join(s["text"] for s in line["spans"]).strip()
                if not txt:
                    continue
                span = line["spans"][0]
                sizes[round(span["size"], 1)] += 1
                if span["size"] >= HEADING_FLOOR and not FURNITURE.match(txt):
                    heads.append((pno, round(span["size"], 1), span["font"], txt))
                    fonts[span["font"]] += 1

    print("SIZE HISTOGRAM (all lines) — body is the mode:")
    for s, n in sorted(sizes.items(), key=lambda kv: -kv[1])[:8]:
        tag = "  <- BODY" if abs(s - BODY_SIZE) < 0.05 else ""
        print(f"   {s:>5.1f}pt  {n:>5} lines{tag}")

    print(f"\nHEADING SPANS at >= {HEADING_FLOOR}pt: {len(heads)}")
    print(f"{'pg':>3} {'size':>5}  {'font':<16} text")
    print("-" * 84)
    for pno, size, font, txt in heads:
        print(f"{pno:>3} {size:>5.1f}  {font:<16} {txt[:52]}")

    print(f"\nFONT NAMES used by heading-sized spans: {dict(fonts)}")
    if len(fonts) > 1:
        print("   ^ INCONSISTENT. A font-NAME filter would silently drop the")
        print("     minority spellings. This census filters on SIZE for that reason.")

    # the numbered census: a heading whose text starts with 19.x
    numbered = sorted({txt.split()[0] for _, _, _, txt in heads
                       if re.match(r"^19\.\d", txt)},
                      key=lambda s: [int(x) for x in s.split(".")])
    print(f"\nNUMBERED sections found: {len(numbered)}")
    print(f"   {', '.join(numbered)}")
    expected = ([f"19.{i}" for i in (1, 2)]
                + [f"19.2.{i}" for i in range(1, 11)]
                + [f"19.{i}" for i in (3, 4)])
    expected.sort(key=lambda s: [int(x) for x in s.split(".")])
    missing = [e for e in expected if e not in numbered]
    print(f"   missing vs 19.1/19.2/19.2.1-10/19.3/19.4: {missing or 'none'}")

    # The source sets a numbered heading's NUMBER and TITLE as two separate
    # lines ('19.2.1' / 'The Hypothalamus'), so a title line is not an
    # unnumbered heading -- it is the second half of a numbered one. A line is
    # the title of the preceding number when it is the next heading span, at
    # the same size, on the same page.
    titles_of_numbered: set[int] = set()
    for i, (pno, size, _f, txt) in enumerate(heads):
        if re.match(r"^19\.\d+(\.\d+)?$", txt.strip()) and i + 1 < len(heads):
            npno, nsize, _nf, _ntxt = heads[i + 1]
            if npno == pno and abs(nsize - size) < 0.05:
                titles_of_numbered.add(i + 1)

    # the chapter title is one heading printed on two lines at 26.8/15.4
    TITLE_LINES = {"CHEMICAL COORDINATION", "AND INTEGRATION"}
    unnumbered, title_parts = [], []
    for i, (_p, _s, _f, txt) in enumerate(heads):
        if i in titles_of_numbered or re.match(r"^19\.\d", txt):
            continue
        (title_parts if txt.strip() in TITLE_LINES else unnumbered).append(txt)

    print(f"\nCHAPTER-TITLE lines (one heading row, F001): {len(title_parts)}")
    for t in title_parts:
        print(f"   {t}")
    total_unnumbered = len(unnumbered) + (1 if title_parts else 0)
    print(f"\nUNNUMBERED structural headings: {total_unnumbered}")
    print(f"   chapter title (2 lines -> 1 row)")
    for u in unnumbered:
        print(f"   {u}")
    print(f"\nHEADING CENSUS: {len(numbered)} numbered + {total_unnumbered} "
          f"unnumbered = {len(numbered) + total_unnumbered}")
    print("   ^ must equal the `heading` count in the inventory type census")
    return 0


if __name__ == "__main__":
    sys.exit(main())
