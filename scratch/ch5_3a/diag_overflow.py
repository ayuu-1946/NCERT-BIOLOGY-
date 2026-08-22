"""Identify exactly WHICH objects sit right of the 552.8pt frame edge."""
import pymupdf, collections

CH = "/vercel/share/v0-project/notes/class 12/Ch5_MolecularBasisOfInheritance"
PDF = f"{CH}/Ch5_MolecularBasisOfInheritance.pdf"
CM = 28.3464567
RIGHT = 595.276 - 1.5 * CM  # 552.8

doc = pymupdf.open(PDF)
kinds = collections.Counter()
samples = []
for i, page in enumerate(doc, 1):
    # text spans past the edge?
    for blk in page.get_text("dict")["blocks"]:
        if blk.get("type") == 0:
            for ln in blk["lines"]:
                for sp in ln["spans"]:
                    if sp["bbox"][2] > RIGHT + 0.5:
                        kinds["text"] += 1
                        if len(samples) < 12:
                            samples.append((i, "text", round(sp["bbox"][2], 2), sp["text"][:60]))
    # drawings past the edge?
    for d in page.get_drawings():
        if d["rect"].x1 > RIGHT + 0.5:
            kinds[f"draw:{d['type']}"] += 1
            if len(samples) < 12:
                samples.append((i, f"draw:{d['type']}", round(d["rect"].x1, 2),
                                f"x0={d['rect'].x0:.1f} y0={d['rect'].y0:.1f} y1={d['rect'].y1:.1f} "
                                f"fill={d.get('fill')} stroke={d.get('color')} w={d.get('width')}"))
    # images past the edge?
    for im in page.get_images(full=True):
        for br in page.get_image_rects(im[0]):
            if br.x1 > RIGHT + 0.5:
                kinds["image"] += 1
                if len(samples) < 12:
                    samples.append((i, "image", round(br.x1, 2), ""))

print("offending object kinds:", dict(kinds))
print()
for s in samples:
    print(s)

# what is the widest text span anywhere, and widest drawing
mx_t = mx_d = 0
for page in doc:
    for blk in page.get_text("dict")["blocks"]:
        if blk.get("type") == 0:
            for ln in blk["lines"]:
                for sp in ln["spans"]:
                    mx_t = max(mx_t, sp["bbox"][2])
    for d in page.get_drawings():
        mx_d = max(mx_d, d["rect"].x1)
print(f"\nmax text x1 = {mx_t:.2f}   max drawing x1 = {mx_d:.2f}   frame right = {RIGHT:.2f}")
print(f"page width = 595.28 ; distance from drawing edge to paper edge = {595.276 - mx_d:.2f}pt")
