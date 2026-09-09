#!/usr/bin/env python3
"""Create caption-free copies of every extracted morphology figure.

The original assets are preserved. Each output is cropped only at a documented
horizontal grid line; panel labels and in-figure callouts remain intact.
"""
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"
OUT = ASSETS / "caption_free"
OUT.mkdir(exist_ok=True)

# (left, top, right, bottom), in source-pixel coordinates.
# None means the extracted asset has no printed caption region.
CROPS = {
    "fig_5_1.png": None,
    "fig_5_2.png": None,
    "fig_5_3.png": (0, 0, 980, 900),
    "fig_5_4.png": None,
    "fig_5_5.png": (0, 0, 918, 720),
    "fig_5_6.png": None,
    "fig_5_7.png": None,
    "fig_5_8.png": (0, 0, 951, 570),
    "fig_5_9.png": None,
    "fig_5_10.png": None,
    "fig_5_11.png": None,
    "fig_5_12.png": (0, 0, 592, 2240),
    "fig_5_13.png": (0, 0, 1322, 620),
    "fig_5_14.png": None,
    "fig_5_15.png": (0, 0, 1721, 850),
    "fig_5_16.png": (0, 0, 751, 900),
    "fig_5_17.png": None,
}

for name, box in CROPS.items():
    src = ASSETS / name
    image = Image.open(src).convert("L")
    output = image if box is None else image.crop(box)
    dest = OUT / name
    output.save(dest, format="PNG", optimize=True)
    print(f"{name}: {image.size} -> {output.size}")
