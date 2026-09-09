#!/usr/bin/env python3
"""Compose tall morphology plates horizontally so they fit a portrait page.

Two plates are unusable at their native aspect ratio in an A4-portrait layout:

  * `fig_5_12.png` (Types of placentation) is a vertical stack of five panels,
    430 x 2230 px -- an aspect ratio of about 1:5.2.
  * `fig_5_4.png` (Structure of a leaf) is one wide panel above two side-by-side
    panels, 905 x 1496 px.

Re-flowing their panels into a horizontal strip keeps every panel at its native
scale -- which is what section 4.4 requires, since squashing a plate to fit is
forbidden -- while producing a shape a page can actually hold.

Panels are located by **row projection**, not by hardcoded pixel boxes. The
previous version hardcoded boxes measured against the pre-re-pin assets; several
already reached past the image bounds (it cropped `fig_5_12.png` to y=2240 when
that asset was 2180 px tall), and re-pinning every rectangle at Gate 1 changed
every asset's dimensions, so the constants could not survive. Segmenting on
whitespace adapts automatically if a rectangle is ever re-pinned again.

Output is **single-channel `mode="L"`**. The previous version built its canvas as
`Image.new("RGB", ...)`, so both committed composites were 3-channel: section 4.4
Step 2 requires true monochrome, and `check_pdf.py` check 3 fails a build that
embeds a non-greyscale image, so those files could not have been used.

Run from anywhere:
    /vercel/share/neetenv/bin/python compose_horizontal_figures.py
"""
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"

DARK_INK = 215     # a row is "blank" if it holds no pixel darker than this.
                   # 215 rather than ~250 on purpose: NCERT's watermark renders
                   # around grey 230-245, so a pure-white test treats every
                   # watermarked row as content and the whole plate segments as
                   # one band. Same threshold the ink measurements use.
GAP = 24           # white padding between panels in the composite
MIN_BAND = 12       # ignore content runs shorter than this (stray specks)
MARKER_MAX = 60     # a content band this short is a panel marker or a label line,
                    # not a panel of its own, so it belongs to its neighbour


def content_bands(arr: np.ndarray, axis: int) -> list[tuple[int, int]]:
    """Runs of non-blank rows (axis=1) or columns (axis=0), as [start, end)."""
    blank = arr.min(axis=axis) >= DARK_INK
    bands, start = [], None
    for i, is_blank in enumerate(blank):
        if not is_blank and start is None:
            start = i
        elif is_blank and start is not None:
            bands.append((start, i))
            start = None
    if start is not None:
        bands.append((start, len(blank)))
    return [b for b in bands if b[1] - b[0] >= MIN_BAND]


def absorb_markers(bands: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Attach every short band to a neighbouring panel.

    Deliberately keyed on band *height*, not on the gap to the next band. A gap
    rule cannot separate these two cases in Fig 5.12: its panel (a) sits 1 px above
    panel (b) and must stay separate, while each panel sits 27 px above its own
    `(a)`-style marker and must merge with it. Heights, by contrast, are
    unambiguous -- markers run 33-37 px and panels 373-413 px.

    A short band that comes *first* has no previous panel to join, so it attaches
    forwards instead; that is Fig 5.4's `Lamina` label, which sits above panel (a).
    """
    if not bands:
        return []
    out: list[list[int]] = []
    pending: tuple[int, int] | None = None
    for lo, hi in bands:
        if hi - lo < MARKER_MAX:
            if out:
                out[-1][1] = hi          # marker below a panel
            else:
                pending = (lo, hi)       # label above the first panel
        else:
            out.append([pending[0] if pending else lo, hi])
            pending = None
    return [tuple(b) for b in out]


def panels_by_row(img: Image.Image, expected: int) -> list[Image.Image]:
    """Split a vertically stacked plate into `expected` panels, trimmed sideways."""
    arr = np.array(img)
    bands = absorb_markers(content_bands(arr, axis=1))
    if len(bands) != expected:
        raise SystemExit(
            f"row projection found {len(bands)} panels, expected {expected}: {bands}. "
            "Either MARKER_MAX no longer separates markers from panels, or the asset "
            "has been re-pinned in a way that changes its panel structure."
        )
    out = []
    for top, bottom in bands:
        cols = content_bands(arr[top:bottom], axis=0)
        left, right = cols[0][0], cols[-1][1]
        out.append(img.crop((left, top, right, bottom)))
    return out


def compose(panels: list[Image.Image], out_name: str) -> None:
    height = max(p.height for p in panels)
    width = sum(p.width for p in panels) + GAP * (len(panels) - 1)
    canvas = Image.new("L", (width, height), 255)   # single channel, white ground
    x = 0
    for p in panels:
        canvas.paste(p, (x, (height - p.height) // 2))
        x += p.width + GAP
    dest = ASSETS / out_name
    canvas.save(dest, format="PNG", dpi=(300, 300), optimize=True)
    print(f"{out_name}: {len(panels)} panels -> {canvas.size} mode={canvas.mode}")


def main() -> None:
    # Fig 5.12: five panels (a)-(e) stacked vertically, each with its marker below.
    fig12 = Image.open(ASSETS / "fig_5_12.png").convert("L")
    compose(panels_by_row(fig12, expected=5), "fig_5_12_horizontal.png")

    # Fig 5.4: row 1 is panel (a) with its labels; row 2 holds panels (b) and (c)
    # side by side, so that row is split again on column projection.
    fig4 = Image.open(ASSETS / "fig_5_4.png").convert("L")
    rows = panels_by_row(fig4, expected=2)
    cols = absorb_markers(content_bands(np.array(rows[1]), axis=0))
    if len(cols) != 2:
        raise SystemExit(f"Fig 5.4 lower row: found {len(cols)} panels, expected 2: {cols}")
    lower = [rows[1].crop((lo, 0, hi, rows[1].height)) for lo, hi in cols]
    compose([rows[0], *lower], "fig_5_4_horizontal.png")


if __name__ == "__main__":
    main()
