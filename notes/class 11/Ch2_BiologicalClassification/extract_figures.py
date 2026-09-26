"""Extract Class 11 Biology Chapter 2, Figure 2.5 panels and compose them.

Bounding boxes are in PDF points on 1-indexed source page 8 (576 x 784.8 pt).
They were pinned from scratch/ch2_figs/grid_4x/p08.png (440 dpi, 5-pt grid),
then cross-checked against image extents and panel-marker word boxes:
  (a) image approx x=331.1..484.1, y=237.4..354.6; marker y=357.2..366.8
  (b) image approx x=331.1..487.3, y=376.6..478.9; marker y=483.4..493.0
  (c) image approx x=332.8..483.3, y=501.9..650.2; marker y=660.5..670.1
Each crop shares the same x range so the three panel cells have equal width.
"""
from __future__ import annotations

import os
from pathlib import Path

import numpy as np
import pymupdf
from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "Chapter/class 11/Chapter 02 - Biological Classification.pdf"
OUT_DIR = Path(__file__).resolve().parent / "assets"
RENDER_DPI = 300
BORDER_BAND_PT = 6.0
AUDIT_DPI = 150
DARK = 110

# (asset id, 1-indexed source page, PDF-point rectangle). The shared x bounds
# keep all three panel cells exactly equal width; y bounds include each marker
# while stopping above the caption and outside-column text.
FIGS = [
    ("2_5a", 8, (328.0, 235.0, 490.0, 367.0)),  # Figure 2.5(a), Mucor
    ("2_5b", 8, (328.0, 374.0, 490.0, 494.0)),  # Figure 2.5(b), Aspergillus
    ("2_5c", 8, (328.0, 499.0, 490.0, 673.0)),  # Figure 2.5(c), Agaricus
]


def extract(doc: pymupdf.Document) -> list[Image.Image]:
    """Render each pinned panel independently at the chapter's 300-dpi scale."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    panels: list[Image.Image] = []
    for fid, pno, coords in FIGS:
        page = doc[pno - 1]
        rect = pymupdf.Rect(*coords) & page.rect
        pix = page.get_pixmap(clip=rect, dpi=RENDER_DPI, alpha=False)
        panel = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L")
        path = OUT_DIR / f"fig_{fid}.png"
        panel.save(path, format="PNG", dpi=(RENDER_DPI, RENDER_DPI), optimize=True)
        panels.append(panel)
        print(f"fig_{fid}: p{pno} {coords} {panel.size} mode={panel.mode} -> {path}")
    return panels


def compose(panels: list[Image.Image]) -> Image.Image:
    """Place the original-scale, equal-width crops in a row; never resize them."""
    if len(panels) != 3 or len({p.width for p in panels}) != 1:
        raise ValueError(f"Expected 3 equal-width panel crops; got {[p.size for p in panels]}")
    gap = round(6.0 * RENDER_DPI / 72)  # 6 PDF points, matching chapter convention
    height = max(p.height for p in panels)
    canvas = Image.new("L", (sum(p.width for p in panels) + 2 * gap, height), 255)
    x = 0
    for panel in panels:
        canvas.paste(panel, (x, (height - panel.height) // 2))
        x += panel.width + gap
    out = OUT_DIR / "fig_2_5.png"
    canvas.save(out, format="PNG", dpi=(RENDER_DPI, RENDER_DPI), optimize=True)
    print(f"fig_2_5 horizontal: {canvas.size} mode={canvas.mode} -> {out}")
    return canvas


def audit(doc: pymupdf.Document) -> None:
    """Mandatory NCERT extraction checks: word grazing, drawing overflow, edge ink."""
    print("--- A) text-layer word grazing ---")
    for fid, pno, coords in FIGS:
        page = doc[pno - 1]
        rect = pymupdf.Rect(*coords)
        cut: list[str] = []
        inside = 0
        for word in page.get_text("words"):
            wr = pymupdf.Rect(*word[:4])
            inter = wr & rect
            if inter.is_empty:
                continue
            inside += 1
            if inter.get_area() / max(1e-6, wr.get_area()) <= 0.9:
                cut.append(str(word[4]))
        print(f"  fig_{fid}: words_in_rect={inside}" + (f" GRAZING {cut}" if cut else " ok"))
        if cut:
            raise RuntimeError(f"Text word cut by crop {fid}: {cut}")

    print("--- B) drawings-extent overflow ---")
    for fid, pno, coords in FIGS:
        page = doc[pno - 1]
        x0, y0, x1, y1 = coords
        xs: list[float] = []
        ys: list[float] = []
        for drawing in page.get_drawings():
            r = drawing["rect"]
            if r.width <= 0.2 or r.height <= 0.2 or r.width > 480 or r.height > 420:
                continue
            cx, cy = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
            if x0 <= cx <= x1 and y0 <= cy <= y1:
                xs.extend([r.x0, r.x1])
                ys.extend([r.y0, r.y1])
        if not xs:
            print(f"  fig_{fid}: no vector drawings (raster figure); rely on edge audit and visual review")
            continue
        overflow = [max(0, x0 - min(xs)), max(0, y0 - min(ys)),
                    max(0, max(xs) - x1), max(0, max(ys) - y1)]
        print(f"  fig_{fid}: overflow L{overflow[0]:.1f} T{overflow[1]:.1f} "
              f"R{overflow[2]:.1f} B{overflow[3]:.1f} pt")
        if max(overflow) > 3:
            raise RuntimeError(f"Vector artwork overflows crop {fid}: {overflow}")

    print("--- C) unexplained dark ink in 6-pt border band ---")
    z = AUDIT_DPI / 72
    for fid, pno, coords in FIGS:
        page = doc[pno - 1]
        x0, y0, x1, y1 = coords
        words = [pymupdf.Rect(*w[:4]) for w in page.get_text("words")]
        hits: list[str] = []
        sides = {
            "L": (x0 - BORDER_BAND_PT, y0, x0, y1),
            "R": (x1, y0, x1 + BORDER_BAND_PT, y1),
            "T": (x0, y0 - BORDER_BAND_PT, x1, y0),
            "B": (x0, y1, x1, y1 + BORDER_BAND_PT),
        }
        for side, box in sides.items():
            region = pymupdf.Rect(*box) & page.rect
            if region.is_empty or region.width < 0.5 or region.height < 0.5:
                continue
            pix = page.get_pixmap(clip=region, dpi=AUDIT_DPI, alpha=False)
            gray = np.array(Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L"))
            keep = 0
            sample = None
            for py, px in zip(*np.nonzero(gray < DARK)):
                X = region.x0 + px / z
                Y = region.y0 + py / z
                if any(w.x0 - 1 <= X <= w.x1 + 1 and w.y0 - 1 <= Y <= w.y1 + 1 for w in words):
                    continue
                keep += 1
                if sample is None:
                    sample = (round(X, 1), round(Y, 1))
            if keep > 40:
                hits.append(f"{side}:{keep}px@{sample}")
        print(f"  fig_{fid}: " + (f"EDGE-INK {hits}" if hits else "clean"))
        if hits:
            raise RuntimeError(f"Unexplained border ink for {fid}: {hits}")


def main() -> None:
    if not SRC.is_file():
        raise FileNotFoundError(SRC)
    doc = pymupdf.open(SRC)
    audit(doc)
    panels = extract(doc)
    composite = compose(panels)
    # Enforce equal cell widths and prove composition is a direct pixel paste.
    for panel, x in zip(panels, [0, panels[0].width + round(6 * RENDER_DPI / 72),
                                 2 * (panels[0].width + round(6 * RENDER_DPI / 72))]):
        y = (composite.height - panel.height) // 2
        if composite.crop((x, y, x + panel.width, y + panel.height)).tobytes() != panel.tobytes():
            raise RuntimeError("Composite altered panel pixels")
    print("Composition check passed: all panel pixels pasted unchanged; no resampling.")


if __name__ == "__main__":
    main()
