"""§4.4 Step 2 - convert every extracted NCERT figure to TRUE MONOCHROME.

Run once, in place, over assets/. The raw color extraction is an intermediate,
never a deliverable, so each file is replaced by its converted version.

autocontrast is not optional polish: a figure that used hue to separate two
elements (two DNA strands, vector vs insert DNA) can collapse to near-identical
greys under a flat convert("L"), and autocontrast stretches the tonal range back
out so the distinction survives a photocopier.
"""

import glob
import os

from PIL import Image, ImageOps

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")


def is_colored(path, tol=12, samples=40):
    """True if any sampled pixel has real color separation between channels."""
    with Image.open(path) as im:
        if im.mode == "L":
            return False
        rgb = im.convert("RGB")
        w, h = rgb.size
        for x in range(0, w, max(1, w // samples)):
            for y in range(0, h, max(1, h // samples)):
                r, g, b = rgb.getpixel((x, y))
                if abs(r - g) > tol or abs(g - b) > tol or abs(r - b) > tol:
                    return True
    return False


def convert(path):
    before_mode = Image.open(path).mode
    before_colored = is_colored(path)

    img = Image.open(path)
    # Flatten transparency onto white first, or alpha becomes black smear in "L".
    if img.mode in ("RGBA", "LA", "P"):
        img = img.convert("RGBA")
        flat = Image.new("RGBA", img.size, (255, 255, 255, 255))
        flat.paste(img, (0, 0), img)
        img = flat
    img = img.convert("L")                      # true greyscale, one channel
    img = ImageOps.autocontrast(img, cutoff=1)  # recover contrast lost with hue
    img.save(path, optimize=True)

    after = Image.open(path)
    return before_mode, before_colored, after.mode, is_colored(path)


def main():
    files = sorted(glob.glob(os.path.join(ASSETS, "*.png")))
    if not files:
        raise SystemExit("NO FIGURE ASSETS FOUND - nothing to convert.")

    print(f"{'file':<16} {'before':<8} {'was color':<10} {'after':<7} {'still color'}")
    print("-" * 60)
    failures = []
    for path in files:
        bm, bc, am, ac = convert(path)
        name = os.path.basename(path)
        print(f"{name:<16} {bm:<8} {str(bc):<10} {am:<7} {ac}")
        if am != "L" or ac:
            failures.append(name)

    print("-" * 60)
    if failures:
        raise SystemExit(f"CONVERSION FAILED for: {', '.join(failures)}")
    print(f"All {len(files)} figures verified mode=='L' and color-free.")


if __name__ == "__main__":
    main()
