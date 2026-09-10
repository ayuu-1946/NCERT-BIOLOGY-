#!/usr/bin/env python3
"""Render every page of the chapter PDF as a PNG image for Pass 3(a)."""
import os
import pymupdf

PDF = "/home/user/NCERT-BIOLOGY-/notes/class 12/Ch4_PrinciplesOfInheritanceAndVariation/Ch4_PrinciplesOfInheritanceAndVariation.pdf"
OUT = "/home/user/NCERT-BIOLOGY-/scratch/ch4inh_pass2/pages"
os.makedirs(OUT, exist_ok=True)

doc = pymupdf.open(PDF)
print(f"Rendering {doc.page_count} pages at 150 dpi...")
for i, page in enumerate(doc, 1):
    pix = page.get_pixmap(dpi=150)
    out_path = os.path.join(OUT, f"p{i:02d}.png")
    pix.save(out_path)
    print(f"  p{i:02d} -> {out_path} ({pix.width}x{pix.height})")
doc.close()
print(f"Done. {len(os.listdir(OUT))} page images in {OUT}")
