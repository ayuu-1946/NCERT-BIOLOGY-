#!/usr/bin/env python3
"""Read every horizontal band of page ink that the line-level OCR never covered."""
import json, os, sys
import numpy as np, pymupdf
from PIL import Image
from rapidocr_onnxruntime import RapidOCR
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, "..", "..", "Chapter", "class 12",
                                   "Chapter 4 - Principles of Inheritance and Variation.pdf"))
DPI = 300; SC = DPI/72.0
def main(pages=None):
    raw = json.load(open(os.path.join(HERE, "ocr_raw.json")))
    doc = pymupdf.open(SRC); ocr = RapidOCR()
    for pno_s, rows in raw.items():
        pno = int(pno_s)
        if pages and pno not in pages: continue
        page = doc[pno-1]
        pix = page.get_pixmap(dpi=DPI, colorspace=pymupdf.csGRAY)
        a = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width)
        ink = a < 140
        mask = np.zeros_like(ink)
        for r in rows:
            y0=max(0,int((r[1]-2)*SC)); y1=min(pix.height,int((r[3]+5)*SC))
            x0=max(0,int((r[0]-2)*SC)); x1=min(pix.width,int((r[2]+2)*SC))
            mask[y0:y1, x0:x1]=True
        resid = ink & ~mask
        resid[:int(62*SC),:]=False; resid[int(758*SC):,:]=False
        prof = resid.sum(axis=1)
        bands=[]; start=None
        for y,v in enumerate(prof):
            if v>3 and start is None: start=y
            elif v<=3 and start is not None:
                if y-start>4: bands.append((start,y))
                start=None
        if start is not None: bands.append((start,len(prof)))
        print("##### page %d : %d residual bands" % (pno, len(bands)))
        for (y0,y1) in bands:
            cols = np.where(resid[y0:y1].any(axis=0))[0]
            if len(cols)==0: continue
            x0,x1 = cols.min(), cols.max()
            box = (max(0,x0/SC-3), max(0,y0/SC-3), min(612,x1/SC+3), min(820,y1/SC+3))
            tot = int(resid[y0:y1].sum())
            pix2 = page.get_pixmap(dpi=400, colorspace=pymupdf.csGRAY, clip=pymupdf.Rect(*box))
            img = Image.frombytes("L",(pix2.width,pix2.height),pix2.samples)
            big = img.resize((img.width*3,img.height*3), Image.LANCZOS)
            res,_ = ocr(np.array(big))
            toks = [t for _b,t,_s in (res or [])]
            print("  y%5.0f-%5.0f x%5.0f-%5.0f ink=%-6d %s" % (box[1],box[3],box[0],box[2],tot,
                  " | ".join(toks)[:150] or "(no text)"))
if __name__=="__main__":
    args=[a for a in sys.argv[1:] if a.isdigit()]
    main(pages=[int(a) for a in args] if args else None)
