import pymupdf, collections, os
PDF="notes/class 11/Ch19_ChemicalCoordinationAndIntegration/Ch19_ChemicalCoordinationAndIntegration.pdf"
d=pymupdf.open(PDF)
print("pages:",len(d))
tot_chars=0; tot_img=0
for i,p in enumerate(d,1):
    txt=p.get_text()
    tot_chars+=len(txt)
    imgs=p.get_images(full=True); tot_img+=len(imgs)
    # gather drawing rect count
    dr=p.get_drawings()
    sizes=collections.Counter()
    for b in p.get_text("dict")["blocks"]:
        if b["type"]!=0: continue
        for l in b["lines"]:
            for s in l["spans"]:
                sizes[(round(s["size"],1), s["font"])]+=len(s["text"])
    notes = txt.count("[NOTE]"); ma = txt.count("[MEMORY AID")
    heads = [l for l in txt.split("\n") if l.strip().startswith(("19.","Figure"))][:0]
    print(f"p{i:02d}: chars={len(txt):5d} imgs={len(imgs)} drawings={len(dr):4d} NOTE={notes} MEMAID={ma} rect={p.rect.width:.0f}x{p.rect.height:.0f}")
print("TOTAL chars",tot_chars,"images",tot_img)
