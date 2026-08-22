"""Pass 3(a) page renderer for Ch5 — renders EVERY page twice:
  - view/pNN.png       : 150 dpi greyscale-ish view render for layout inspection
  - bw/pNN_bw.png      : 300 dpi (true print DPI) converted to 1-bit B&W threshold
Also reports per-page geometry + ink-extent so overflow past the frame is machine-visible.
"""
import os
import pymupdf
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
CH = "/vercel/share/v0-project/notes/class 12/Ch5_MolecularBasisOfInheritance"
PDF = os.path.join(CH, "Ch5_MolecularBasisOfInheritance.pdf")

VIEW = os.path.join(HERE, "view")
BW = os.path.join(HERE, "bw")
os.makedirs(VIEW, exist_ok=True)
os.makedirs(BW, exist_ok=True)

# frame per neet_template / §4: A4, margins 1.5cm L/R, 1.4cm top/bottom
CM = 28.3464567
MARGIN = 1.5 * CM
TOPM = 1.4 * CM
BOTM = 1.4 * CM

doc = pymupdf.open(PDF)
print(f"pages={len(doc)}")
rows = []
for i, page in enumerate(doc, 1):
    r = page.rect
    # 150 dpi view render
    page.get_pixmap(dpi=150).save(os.path.join(VIEW, f"p{i:02d}.png"))
    # 300 dpi print render -> 1-bit threshold
    pm = page.get_pixmap(dpi=300)
    img = Image.frombytes("RGB", (pm.width, pm.height), pm.samples).convert("L")
    img.point(lambda v: 255 if v > 128 else 0, mode="1").save(
        os.path.join(BW, f"p{i:02d}_bw.png")
    )

    # ink extent: union of all drawing + text + image bboxes, clipped to page
    xs0, ys0, xs1, ys1 = [], [], [], []

    def acc(b):
        b = pymupdf.Rect(b)
        if b.is_empty or b.is_infinite:
            return
        b = b & r
        if b.is_empty:
            return
        xs0.append(b.x0); ys0.append(b.y0); xs1.append(b.x1); ys1.append(b.y1)

    for blk in page.get_text("dict")["blocks"]:
        acc(blk["bbox"])
    for d in page.get_drawings():
        acc(d["rect"])
    for im in page.get_images(full=True):
        for br in page.get_image_rects(im[0]):
            acc(br)

    if xs0:
        x0, y0, x1, y1 = min(xs0), min(ys0), max(xs1), max(ys1)
    else:
        x0 = y0 = x1 = y1 = 0.0

    over_l = max(0.0, MARGIN - x0)
    over_r = max(0.0, x1 - (r.width - MARGIN))
    over_t = max(0.0, TOPM - y0)
    over_b = max(0.0, y1 - (r.height - BOTM))
    flag = "OVERFLOW" if max(over_l, over_r, over_t, over_b) > 1.0 else "ok"
    rows.append((i, x0, y0, x1, y1, over_l, over_r, over_t, over_b, flag))

print(f"{'pg':>3} {'x0':>7} {'y0':>7} {'x1':>7} {'y1':>7} {'ovL':>6} {'ovR':>6} {'ovT':>6} {'ovB':>6}  flag")
for t in rows:
    print(
        f"{t[0]:>3} {t[1]:7.1f} {t[2]:7.1f} {t[3]:7.1f} {t[4]:7.1f} "
        f"{t[5]:6.2f} {t[6]:6.2f} {t[7]:6.2f} {t[8]:6.2f}  {t[9]}"
    )
bad = [t[0] for t in rows if t[9] != "ok"]
print("\nOVERFLOW pages:", bad if bad else "none")
print(f"frame: x {MARGIN:.1f}..{595.276 - MARGIN:.1f}  y {TOPM:.1f}..{841.89 - BOTM:.1f}")
