"""§4.4 figure extraction for Ch17 Locomotion and Movement.
Rects are in PDF points on the 571.7 x 780.5 source pages. Each rectangle was
hand-pinned from the mandatory 440-dpi / 5-point grid overlays and checked
against caption positions, neighboring text columns, and visible artwork/label
extents. Captions are kept in the generated notes PDF, not inside the PNGs.
"""
import os
import sys
import pymupdf
from PIL import Image, ImageOps, ImageDraw

SRC = "Chapter/class 11/Chapter 17 - Locomotion and Movement.pdf"
OUT_DIR = "notes/class 11/Ch17_LocomotionAndMovement/assets"
RENDER_DPI = 440

FIGS = [
    # p3: complete cross-sectional muscle artwork; x=90 keeps the left leader
    # labels, y=245 starts above the drawing, and y=502 stops before the caption
    # beginning at y=507.4.
    ("17_1", 3, (90, 245, 525, 502)),
    # p4: one two-part composition; y=325 starts above the micrograph and y=680
    # includes the lower (b) marker while stopping before the caption at y=682.4;
    # x bounds preserve all Z/A/I/H/Sarcomere labels.
    ("17_2", 4, (85, 325, 520, 680)),
    # p5: two-part actin/myosin composition; x=85 preserves left binding-site
    # labels and x=505 preserves right filament labels; caption is below y=600.
    ("17_3", 5, (85, 375, 505, 595)),
    # p6: complete four-stage cross-bridge cycle; x=65 preserves the left ATP
    # stage, x=565 reaches the page-safe right margin for the full Myosin head
    # label, and bottom stops before the Figure 17.4 caption near y=550.
    ("17_4", 6, (65, 275, 565, 545)),
    # p7: pale-background three-row sliding-filament diagram; y=90 starts below
    # the running header/page number, while all state labels, Z lines, band
    # labels, and Two Sarcomeres remain; caption begins near y=432.
    ("17_5", 7, (65, 90, 510, 425)),
    # p8: skull diagram; y=295 starts below the preceding prose while retaining
    # the Frontal-bone leader; x=95/525 preserve the outer labels, and y=570
    # ends just above the caption near y=575.
    ("17_6", 8, (95, 295, 525, 570)),
    # p9 upper-right: vertebral column only; x=275 excludes the prose column,
    # x=520 preserves right brackets/labels, and y=365 stops above caption.
    ("17_7", 9, (275, 75, 520, 365)),
    # p9 lower-right: rib cage only; x=240 preserves the complete Floating ribs
    # label. Text-layer prose words are masked after rendering because the
    # neighboring column overlaps this figure’s left label zone; vector labels
    # remain untouched. x=520 preserves right labels, y=675 stops above caption.
    ("17_8", 9, (240, 425, 520, 675)),
    # p10 upper-left: pectoral girdle and upper arm; x=50 preserves left outline
    # and x=295 preserves right labels, ending just above caption at y=386.
    ("17_9", 10, (50, 75, 295, 382)),
    # p10 lower-left: pelvic girdle and lower limb; x=50 preserves left labels,
    # x=295 preserves right labels, and y=758 captures the complete foot and
    # Phalanges label. Caption words below y=667 are masked after rendering.
    ("17_10", 10, (50, 410, 295, 758)),
]

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    doc = pymupdf.open(SRC)
    for fid, pno, rect in FIGS:
        page = doc[pno - 1]
        clip = pymupdf.Rect(*rect) & page.rect
        pix = page.get_pixmap(clip=clip, dpi=RENDER_DPI, alpha=False)
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        if fid in {"17_8", "17_10"}:
            # Remove only text-layer prose/caption words from overlapping
            # regions. Figure labels are vector artwork and remain intact.
            draw = ImageDraw.Draw(img)
            z = RENDER_DPI / 72
            for w in page.get_text("words"):
                wr = pymupdf.Rect(*w[:4])
                if (wr & clip).is_empty:
                    continue
                if fid == "17_10" and wr.y0 < 667:
                    continue
                x0 = max(0, int((wr.x0 - clip.x0) * z) - 2)
                y0 = max(0, int((wr.y0 - clip.y0) * z) - 2)
                x1 = min(img.width, int((wr.x1 - clip.x0) * z) + 2)
                y1 = min(img.height, int((wr.y1 - clip.y0) * z) + 2)
                draw.rectangle((x0, y0, x1, y1), fill=(255, 255, 255))
        img = ImageOps.autocontrast(img.convert("L"), cutoff=1)
        out = os.path.join(OUT_DIR, f"fig_{fid}.png")
        img.save(out, optimize=True)
        print(f"fig_{fid}: p{pno} {rect} {img.size} mode={img.mode} -> {out}")

if __name__ == "__main__":
    sys.exit(main())
