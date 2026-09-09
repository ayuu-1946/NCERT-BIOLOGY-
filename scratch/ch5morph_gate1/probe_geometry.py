"""Geometry probe for Ch5 figure re-pinning.

Reports, per source page, the bbox of every text line and every raster image,
plus the union bbox of vector drawings. Used ONLY to pin crop rectangles --
in-figure labels for the Gate 1 label matrix were harvested by opening each
rendered asset and reading it (SUPREME COMMAND 4.4 / GATE_1 section 3 Step 1).
"""
import re
import sys

import pymupdf

SRC = "Chapter/class 11/Chapter 05 - Morphology of Flowering Plants.pdf"


def probe(page_no: int, y0: float = 0.0, y1: float = 1000.0) -> None:
    doc = pymupdf.open(SRC)
    page = doc[page_no - 1]
    print(f"===== PDF page {page_no}  (mediabox {page.rect}) =====")

    print("--- text lines ---")
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            txt = "".join(s["text"] for s in line["spans"]).strip()
            if not txt:
                continue
            x0, ly0, x1, ly1 = (round(v, 1) for v in line["bbox"])
            if ly1 < y0 or ly0 > y1:
                continue
            tag = "CAPTION" if re.match(r"Figure\s+5\.\d+", txt) else "       "
            print(f"  {tag} ({x0:6.1f},{ly0:6.1f},{x1:6.1f},{ly1:6.1f})  {txt[:66]!r}")

    print("--- raster images ---")
    for info in page.get_image_info():
        x0, iy0, x1, iy1 = (round(v, 1) for v in info["bbox"])
        if iy1 < y0 or iy0 > y1:
            continue
        print(f"  IMG     ({x0:6.1f},{iy0:6.1f},{x1:6.1f},{iy1:6.1f})  {info['width']}x{info['height']}")

    print("--- vector drawings (union of items in band) ---")
    union = None
    for drawing in page.get_drawings():
        rect = drawing["rect"]
        if rect.y1 < y0 or rect.y0 > y1 or rect.is_empty:
            continue
        union = rect if union is None else union | rect
    print(f"  DRAW    {None if union is None else [round(v, 1) for v in union]}")


if __name__ == "__main__":
    page = int(sys.argv[1])
    lo = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
    hi = float(sys.argv[3]) if len(sys.argv) > 3 else 1000.0
    probe(page, lo, hi)
