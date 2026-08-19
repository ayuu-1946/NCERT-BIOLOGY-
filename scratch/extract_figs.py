"""§4.4 figure extraction for Ch9 Biotechnology: Principles and Processes.
Figures are vector/composite, so clip-rect render at 300 dpi is used throughout.
Rects are in PDF points (page is 568.8 x 777.6)."""
import os
import pymupdf

SRC = "Chapter/class 12/Chapter 9 - Biotechnology Principles and Processes.pdf"
OUT = "notes/class 12/Ch9_BiotechnologyPrinciplesAndProcesses/assets"
os.makedirs(OUT, exist_ok=True)

# (asset name, 0-based page index, clip rect x0,y0,x1,y1)
FIGS = [
    ("fig_9_1.png",    5, (130, 258, 545, 575)),     # Action of restriction enzyme -> recombinant DNA
    ("fig_9_2.png",    6, (40, 340, 400, 690)),      # Diagrammatic representation of rDNA technology
    ("fig_9_3.png",    7, (75, 295, 345, 435)),      # Agarose gel electrophoresis
    ("fig_9_4.png",    8, (285, 325, 545, 500)),     # pBR322 cloning vector
    ("fig_9_5.png",   10, (370, 297, 515, 570)),     # DNA spooling (two photographs)
    ("fig_9_6.png",   11, (85, 315, 545, 672)),      # PCR
    ("fig_9_7.png",   13, (60, 270, 525, 480)),      # (a) simple and (b) sparged stirred-tank bioreactor
]

doc = pymupdf.open(SRC)

# Herbert Boyer portrait: extract the embedded image object (xref 7 on page 2) directly,
# which is exact and avoids any surrounding-text bleed from a clip crop.
try:
    pix = pymupdf.Pixmap(doc, 7)
    if pix.n > 3:
        pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
    pix.save(os.path.join(OUT, "fig_boyer.png"))
    print(f"fig_boyer.png: page 2 embedded xref 7  {pix.width}x{pix.height}px")
except Exception as exc:
    raise RuntimeError(f"FIGURE EXTRACTION FAILED for fig_boyer.png (page 2, xref 7): {exc}")

for name, pno, (x0, y0, x1, y1) in FIGS:
    try:
        page = doc[pno]
        pix = page.get_pixmap(clip=pymupdf.Rect(x0, y0, x1, y1), dpi=300)
        path = os.path.join(OUT, name)
        pix.save(path)
        print(f"{name}: page {pno+1}  {pix.width}x{pix.height}px  -> {path}")
    except Exception as exc:
        raise RuntimeError(f"FIGURE EXTRACTION FAILED for {name} on page {pno+1}: {exc}")
doc.close()
