"""Dump the Ch19 SOURCE pdf text page by page for the Gate 3(b) direction-2 read.

Written to a few grouped files so every page can be read in full, in order,
with its page number attached to every line of text. No summarising, no
sampling: Gate 3(b) requires the source read start to finish.
"""
import os

import pymupdf

REPO = "/vercel/share/v0-project"
SRC = os.path.join(REPO, "Chapter/class 11/Chapter 19 - Chemical Coordination and Integration.pdf")
OUT = os.path.join(REPO, "scratch/ch19_gate3b/source")
os.makedirs(OUT, exist_ok=True)

doc = pymupdf.open(SRC)
groups = [(1, 3), (4, 6), (7, 9), (10, 11), (12, 14)]
for lo, hi in groups:
    parts = []
    for pno in range(lo, hi + 1):
        page = doc[pno - 1]
        txt = page.get_text("text")
        parts.append(f"\n{'=' * 76}\n=== SOURCE PAGE {pno} ({len(txt)} chars) ===\n{'=' * 76}\n{txt}")
    path = os.path.join(OUT, f"pages_{lo:02d}_{hi:02d}.txt")
    open(path, "w", encoding="utf-8").write("".join(parts))
    print(f"wrote {path}  ({sum(len(p) for p in parts)} chars)")

print("\nper-page char counts:")
for pno in range(1, doc.page_count + 1):
    print(f"  p{pno:02d}: {len(doc[pno-1].get_text('text')):6d}")
doc.close()
