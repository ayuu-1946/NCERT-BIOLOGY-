"""Convert extracted NCERT figure assets to true monochrome (§4.4 Step 2).

`neet_template.figure()` refuses any asset whose PIL mode is not "L", so this
script is the mandatory bridge between extraction (which may emit RGB when
colour is load-bearing during the crop/eyeball audit) and embedding (which
must be single-channel grey to satisfy check_pdf.py check 3).

Idempotent: an asset already in mode "L" is re-saved unchanged. The convert +
autocontrast pair is exactly the transform check_pdf.py check 3 expects, so
running this twice cannot drift the pixels.

Usage:
    python convert_figures_mono.py "notes/class 12/Ch1_SexualReproductionInFloweringPlants/assets"
"""

import glob
import os
import sys

from PIL import Image, ImageOps


def convert_dir(assets_dir: str) -> int:
    paths = sorted(glob.glob(os.path.join(assets_dir, "*.png")))
    if not paths:
        print(f"NO ASSETS FOUND in {assets_dir}", file=sys.stderr)
        return 1
    for p in paths:
        im = Image.open(p)
        before = im.mode
        gray = ImageOps.autocontrast(im.convert("L"), cutoff=0.5)
        gray.save(p)
        print(f"{os.path.basename(p)}: {before} -> L  {gray.size}")
    print(f"converted {len(paths)} assets in {assets_dir}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(convert_dir(sys.argv[1]))
