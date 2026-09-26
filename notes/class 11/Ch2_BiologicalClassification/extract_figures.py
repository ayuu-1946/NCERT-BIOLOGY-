"""Source extraction and horizontal composition for Class 11 Biology Chapter 2.

Figure 2.4 is source-cropped from p6 using the pinned 440-dpi/5-pt-grid bounds
(320, 100, 536.5, 656) pt. The cut between halves is y=395 pt: it keeps panels
(a)/(b) and their markers together, then (c)/(d) together. The shorter lower
half is centered on white to make equal-size cells; neither crop is resampled.
Figure 2.5's three panels are independently source-cropped from p8.

All crop coordinates are PDF points on the original 576 x 784.8 pt source pages.
The script runs word-grazing, vector-overflow and 6-pt border-ink audits before
rendering at 300 dpi. Composition is pixel-pasting only.
"""
from __future__ import annotations

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
GAP_PT = 6.0

# One full pinned crop for Figure 2.4; split at the whitespace seam between (b) and (c).
FIG24_RECT = (320.0, 100.0, 536.5, 656.0)
FIG24_SPLIT_Y = 395.0
FIGS_25 = [
    ("2_5a", 8, (328.0, 235.0, 490.0, 367.0)),  # Mucor
    ("2_5b", 8, (328.0, 374.0, 490.0, 494.0)),  # Aspergillus
    ("2_5c", 8, (328.0, 499.0, 490.0, 673.0)),  # Agaricus
]
FIGS = [("2_4full", 6, FIG24_RECT)] + FIGS_25


def audit(doc: pymupdf.Document) -> None:
    """Mandatory A/B/C crop audit: word grazing, drawings overflow, border ink."""
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
        print(f"  {fid}: words_in_rect={inside}" + (f" GRAZING {cut}" if cut else " ok"))
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
            print(f"  {fid}: raster source art; no vector drawings")
            continue
        overflow = [max(0, x0 - min(xs)), max(0, y0 - min(ys)),
                    max(0, max(xs) - x1), max(0, max(ys) - y1)]
        print(f"  {fid}: overflow L{overflow[0]:.1f} T{overflow[1]:.1f} "
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
                X, Y = region.x0 + px / z, region.y0 + py / z
                if any(w.x0 - 1 <= X <= w.x1 + 1 and w.y0 - 1 <= Y <= w.y1 + 1 for w in words):
                    continue
                keep += 1
                if sample is None:
                    sample = (round(X, 1), round(Y, 1))
            if keep > 40:
                hits.append(f"{side}:{keep}px@{sample}")
        print(f"  {fid}: " + (f"EDGE-INK {hits}" if hits else "clean"))
        if hits:
            raise RuntimeError(f"Unexplained border ink for {fid}: {hits}")


def source_crop(doc: pymupdf.Document, pno: int, coords: tuple[float, float, float, float]) -> Image.Image:
    page = doc[pno - 1]
    pix = page.get_pixmap(clip=pymupdf.Rect(*coords), dpi=RENDER_DPI, alpha=False)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L")


def save_png(image: Image.Image, filename: str) -> None:
    path = OUT_DIR / filename
    image.save(path, format="PNG", dpi=(RENDER_DPI, RENDER_DPI), optimize=True)
    print(f"{filename}: {image.size} mode={image.mode} -> {path}")


def build_fig24(doc: pymupdf.Document) -> None:
    """Split a/b from c/d; make equal-size cells by white padding, then paste side by side."""
    full = source_crop(doc, 6, FIG24_RECT)
    x0, y0, _, _ = FIG24_RECT
    split = round((FIG24_SPLIT_Y - y0) * RENDER_DPI / 72)
    upper = full.crop((0, 0, full.width, split))
    lower_original = full.crop((0, split, full.width, full.height))
    cell_h = max(upper.height, lower_original.height)
    lower = Image.new("L", (full.width, cell_h), 255)
    lower_y = (cell_h - lower_original.height) // 2
    lower.paste(lower_original, (0, lower_y))
    save_png(upper, "fig_2_4_top.png")
    save_png(lower, "fig_2_4_bottom.png")

    gap = round(GAP_PT * RENDER_DPI / 72)
    composite = Image.new("L", (2 * full.width + gap, cell_h), 255)
    composite.paste(upper, (0, 0))
    composite.paste(lower, (full.width + gap, 0))
    save_png(composite, "fig_2_4.png")

    if composite.crop((0, 0, full.width, cell_h)).tobytes() != upper.tobytes():
        raise RuntimeError("Figure 2.4 top half pixels changed during composition")
    if composite.crop((full.width + gap, 0, 2 * full.width + gap, cell_h)).tobytes() != lower.tobytes():
        raise RuntimeError("Figure 2.4 bottom half pixels changed during composition")
    if upper.crop((0, 0, upper.width, upper.height)).tobytes() != full.crop((0, 0, full.width, split)).tobytes():
        raise RuntimeError("Figure 2.4 upper source pixels changed")
    if lower.crop((0, lower_y, lower.width, lower_y + lower_original.height)).tobytes() != lower_original.tobytes():
        raise RuntimeError("Figure 2.4 lower source pixels changed")
    if upper.size != lower.size:
        raise RuntimeError(f"Figure 2.4 halves must be equal-size: {upper.size} vs {lower.size}")
    print(f"Figure 2.4 split at source y={FIG24_SPLIT_Y:g} pt; equal-size cells; no resizing")


def build_fig25(doc: pymupdf.Document) -> None:
    panels: list[Image.Image] = []
    for fid, pno, coords in FIGS_25:
        panel = source_crop(doc, pno, coords)
        save_png(panel, f"fig_{fid}.png")
        panels.append(panel)
    if len({p.width for p in panels}) != 1:
        raise ValueError(f"Expected equal-width Figure 2.5 panels; got {[p.size for p in panels]}")
    gap = round(GAP_PT * RENDER_DPI / 72)
    height = max(p.height for p in panels)
    composite = Image.new("L", (sum(p.width for p in panels) + 2 * gap, height), 255)
    x = 0
    for panel in panels:
        y = (height - panel.height) // 2
        composite.paste(panel, (x, y))
        if composite.crop((x, y, x + panel.width, y + panel.height)).tobytes() != panel.tobytes():
            raise RuntimeError("Figure 2.5 composition altered panel pixels")
        x += panel.width + gap
    save_png(composite, "fig_2_5.png")


def main() -> None:
    if not SRC.is_file():
        raise FileNotFoundError(SRC)
    doc = pymupdf.open(SRC)
    audit(doc)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    build_fig24(doc)
    build_fig25(doc)


if __name__ == "__main__":
    main()
