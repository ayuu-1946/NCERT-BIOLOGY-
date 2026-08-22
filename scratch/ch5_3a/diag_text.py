"""List every text span whose bbox exceeds the 1.5cm text frame on either side,
plus any span running past the PAPER edge (true clipping)."""
import pymupdf

CH = "/vercel/share/v0-project/notes/class 12/Ch5_MolecularBasisOfInheritance"
PDF = f"{CH}/Ch5_MolecularBasisOfInheritance.pdf"
CM = 28.3464567
LEFT, RIGHT, PW = 1.5 * CM, 595.276 - 1.5 * CM, 595.276

doc = pymupdf.open(PDF)
print(f"text frame: {LEFT:.2f} .. {RIGHT:.2f}   paper: 0 .. {PW:.2f}\n")
n = 0
for i, page in enumerate(doc, 1):
    for blk in page.get_text("dict")["blocks"]:
        if blk.get("type") != 0:
            continue
        for ln in blk["lines"]:
            for sp in ln["spans"]:
                x0, x1 = sp["bbox"][0], sp["bbox"][2]
                if x1 > RIGHT + 0.5 or x0 < LEFT - 0.5:
                    n += 1
                    clip = "  *** PAST PAPER EDGE ***" if x1 > PW else ""
                    print(f"p{i:02d}  x0={x0:7.2f} x1={x1:7.2f}  over_r={max(0,x1-RIGHT):5.2f} "
                          f"size={sp['size']:.2f} font={sp['font']}{clip}")
                    print(f"      text={sp['text']!r}")
print(f"\ntotal out-of-frame text spans: {n}")
