#!/usr/bin/env python3
"""Session 1-S helper — turn the raw OCR boxes into readable, ordered page text.

The scanned chapter has no text layer, so `ocr_raw.json` (RapidOCR boxes in PDF
point space) is the only access to the source.  Raw boxes come out in
y-then-x order, which interleaves a paragraph with the figure labels floating
beside it.  This script:

  1. clusters boxes into spatial blocks (a block = a paragraph, a table, a
     figure's label cluster, a heading),
  2. orders blocks by (y, x) and the boxes inside a block by (y, x),
  3. repairs RapidOCR's collapsed word spacing with `fix_spacing.fix_line`,
  4. writes `pages/pNN.txt` (one per source page) and `source_text_v1.txt`,
     both annotated with block ids and coordinates so any line can be traced
     back to a place on the page.

Re-run: /tmp/neetenv/bin/python scratch/ch4inh_gate1/build_text.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fix_spacing as FS  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(HERE, "pages")
Y_GAP = 5.0      # pt: vertical gap that still counts as the same block
X_GAP = 22.0     # pt: horizontal gap that still counts as the same block
MIN_OVERLAP = 0.35


def load():
    d = json.load(open(os.path.join(HERE, "ocr_raw.json")))
    return [(int(p), r) for p, rows in d.items() for r in rows]


def y_overlap(a, b):
    lo = max(a[1], b[1])
    hi = min(a[3], b[3])
    if hi <= lo:
        return False
    small = min(a[3] - a[1], b[3] - b[1])
    return (hi - lo) >= MIN_OVERLAP * small


def x_gap(a, b):
    if a[2] >= b[0] and b[2] >= a[0]:
        return -1.0
    return b[0] - a[2] if b[0] > a[2] else a[0] - b[2]


def cluster(rows):
    """Union-find clustering of boxes on the same page."""
    n = len(rows)
    parent = list(range(n))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(i, j):
        ri, rj = find(i), find(j)
        if ri != rj:
            parent[rj] = ri

    for i in range(n):
        for j in range(i + 1, n):
            a, b = rows[i], rows[j]
            if abs(a[1] - b[1]) > 60 and abs(a[3] - b[3]) > 60:
                continue
            vgap = max(b[1] - a[3], a[1] - b[3])
            if vgap <= Y_GAP and -1.0 <= x_gap(a, b) <= X_GAP:
                if y_overlap(a, b) or vgap <= 0 or True:
                    union(i, j)
    groups = {}
    for i in range(n):
        groups.setdefault(find(i), []).append(i)
    blocks = []
    for _, idxs in groups.items():
        idxs.sort(key=lambda i: (round(rows[i][1], 1), rows[i][0]))
        blocks.append([rows[i] for i in idxs])
    blocks.sort(key=lambda bl: (round(min(r[1] for r in bl), 1), min(r[0] for r in bl)))
    return blocks


def main():
    entries = load()
    lex = FS.build_corpus_lexicon([r[4] for _, r in entries])
    for _ in range(2):
        lex |= FS.build_corpus_lexicon(
            [FS.fix_line(r[4], lex)[0] for _, r in entries])
    lex |= FS.DOMAIN

    os.makedirs(PAGES, exist_ok=True)
    allout = []
    flags = []
    for pno in range(1, 29):
        rows = [r for p, r in entries if p == pno]
        if not rows:
            continue
        blocks = cluster(rows)
        lines = []
        lines.append("########## SOURCE PAGE %d ##########" % pno)
        for bi, bl in enumerate(blocks):
            x0 = min(r[0] for r in bl)
            x1 = max(r[2] for r in bl)
            y0 = min(r[1] for r in bl)
            y1 = max(r[3] for r in bl)
            lines.append("")
            lines.append("[p%02d.B%02d  x %.0f-%.0f  y %.0f-%.0f]" % (pno, bi, x0, x1, y0, y1))
            for r in bl:
                fixed, rep, flag = FS.fix_line(r[4], lex)
                if flag:
                    flags.append((pno, bi, flag))
                lines.append("   %s" % fixed)
        txt = "\n".join(lines)
        open(os.path.join(PAGES, "p%02d.txt" % pno), "w").write(txt + "\n")
        allout.append(txt)
    open(os.path.join(HERE, "source_text_v1.txt"), "w").write("\n".join(allout) + "\n")
    print("pages written:", len(allout))
    print("\n=== TOKENS THE SEGMENTER COULD NOT SPLIT (manual review) ===")
    for pno, bi, fl in flags:
        print("p%02d.B%02d: %s" % (pno, bi, " ".join(fl)))


if __name__ == "__main__":
    main()
