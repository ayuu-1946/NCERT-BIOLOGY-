#!/usr/bin/env python3
"""Compose selected morphology figures horizontally, without captions.

Run from this chapter directory or from anywhere:
    python3 compose_horizontal_figures.py
"""
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"


def stack(src_name, out_name, boxes):
    image = Image.open(ASSETS / src_name).convert("RGB")
    panels = [image.crop(box) for box in boxes]
    max_height = max(panel.height for panel in panels)
    gap = 24
    canvas = Image.new(
        "RGB",
        (sum(panel.width for panel in panels) + gap * (len(panels) - 1), max_height),
        "white",
    )
    x = 0
    for panel in panels:
        y = (max_height - panel.height) // 2
        canvas.paste(panel, (x, y))
        x += panel.width + gap
    output = ASSETS / out_name
    canvas.save(output, format="PNG", optimize=True)
    print(f"{output}: {canvas.size}")


if __name__ == "__main__":
    stack(
        "fig_5_12.png",
        "fig_5_12_horizontal.png",
        [
            (35, 55, 560, 490),
            (25, 492, 570, 930),
            (25, 930, 570, 1400),
            (25, 1400, 570, 1900),
            (65, 1900, 525, 2240),
        ],
    )
    stack(
        "fig_5_4.png",
        "fig_5_4_horizontal.png",
        [
            (35, 25, 930, 610),
            (70, 620, 485, 1418),
            (500, 575, 972, 1418),
        ],
    )
