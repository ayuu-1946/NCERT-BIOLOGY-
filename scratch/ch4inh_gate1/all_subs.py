#!/usr/bin/env python3
"""Find EVERY subscript-like glyph below a line's baseline in the whole chapter."""
import json, os, sys
import numpy as np, pymupdf
from scipy import ndimage
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import f_digits as F
raw = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ocr_raw.json")))
doc = pymupdf.open(F.SRC)
out=[]
for pno_s, rows in raw.items():
    pno=int(pno_s); page=doc[pno-1]
    for idx, r in enumerate(rows):
        ink, box_top, box_bot = F.line_image(page, r)
        base, cap = F.baseline_cap(ink, box_top, box_bot)
        if base is None or cap is None: continue
        H,W = ink.shape
        band = ink[base+1: min(H, base+int(0.62*cap)), :]
        if band.size==0: continue
        lab,n = ndimage.label(band, structure=np.ones((3,3)))
        for i, sl in enumerate(ndimage.find_objects(lab), start=1):
            arr=(lab[sl]==i).astype(np.uint8)
            h=sl[0].stop-sl[0].start; w=sl[1].stop-sl[1].start
            if h < 0.35*cap or h > 0.95*cap: continue
            if w > 1.6*h or w < 0.15*h: continue
            if arr.sum() < 0.18*h*w: continue
            out.append(dict(page=pno, line=idx, x=int(sl[1].start), w=w, h=h,
                            text=r[4], art="\n".join("".join("#" if v else "." for v in row) for row in arr)))
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "all_subs.json"),"w"), indent=1)
print("glyphs found:", len(out))
def norm(rows, N=20):
    a=np.array([[1 if c=="#" else 0 for c in r] for r in rows], dtype=float)
    h,w=a.shape; canvas=np.zeros((N,N))
    sh=min(N,h); sw=min(N,max(1,int(round(w*N/max(h,w)))))
    a2=np.array([[a[int(i*h/sh), int(j*w/sw)] for j in range(sw)] for i in range(sh)])
    y0=(N-sh)//2; x0=(N-sw)//2; canvas[y0:y0+sh, x0:x0+sw]=a2
    return canvas
mats=[norm(g["art"].splitlines()) for g in out]
clusters=[]
for i,m in enumerate(mats):
    for c in clusters:
        if np.abs(m-mats[c[0]]).mean() < 0.14:
            c[1].append(i); break
    else:
        clusters.append((i,[i]))
print("clusters:", len(clusters))
for ri, mem in sorted(clusters, key=lambda c:-len(c[1])):
    g=out[ri]
    print("=== size %d  exemplar p%d L%d x=%d  line=%r" % (len(mem), g["page"], g["line"], g["x"], g["text"][:60]))
    for row in g["art"].splitlines(): print("    "+row)
    print("    members:", " ".join("p%d/L%d" % (out[i]["page"], out[i]["line"]) for i in mem))
