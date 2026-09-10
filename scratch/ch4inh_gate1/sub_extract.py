#!/usr/bin/env python3
"""Extract every standalone sub-baseline glyph (subscript digit) in the chapter.

A subscript digit is its own connected component sitting entirely below the
line's baseline; the descender of g/p/q/y is not, because it is attached to its
letter body above the baseline.  Commas/full stops are far too small to pass
the height filter.  Candidates are kept only inside the OCR line box, so the
next line's ascenders are never picked up.
"""
import json, os, sys
import numpy as np, pymupdf
from scipy import ndimage

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, "..", "..", "Chapter", "class 12",
                                   "Chapter 4 - Principles of Inheritance and Variation.pdf"))
DPI = 400
SC = DPI / 72.0


def line_components(page, r, padx=4.0, padtop=3.0, padbot=10.0):
    x0, y0, x1, y1 = r[0], r[1], r[2], r[3]
    clip = pymupdf.Rect(max(0, x0 - padx), max(0, y0 - padtop), x1 + padx, y1 + padbot)
    pix = page.get_pixmap(dpi=DPI, colorspace=pymupdf.csGRAY, clip=clip)
    a = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width)
    ink = a < 140
    lab, n = ndimage.label(ink, structure=np.ones((3, 3)))
    objs = ndimage.find_objects(lab)
    comps = []
    for i, sl in enumerate(objs, start=1):
        comps.append(dict(x0=sl[1].start, x1=sl[1].stop, y0=sl[0].start, y1=sl[0].stop,
                          w=sl[1].stop - sl[1].start, h=sl[0].stop - sl[0].start,
                          arr=(lab[sl] == i).astype(np.uint8)))
    comps.sort(key=lambda c: c["x0"])
    # geometry in crop pixels
    box_top = int((y0 - (y0 - padtop)) * SC)
    box_bot = int((y1 - (y0 - padtop)) * SC)
    return comps, box_top, box_bot, x0 - padx, y0 - padtop


def baseline_of(comps, box_top, box_bot):
    cand = [c for c in comps if c["y0"] >= box_top - 4 and c["y1"] <= box_bot + 4 and c["h"] >= 8]
    if not cand:
        return None, None
    hs = sorted(c["h"] for c in cand)
    cap = hs[int(len(hs) * 0.85)] if len(hs) > 3 else max(hs)
    tall = [c for c in cand if c["h"] >= 0.62 * cap]
    if not tall:
        return None, cap
    return int(np.median([c["y1"] for c in tall])), cap


def main():
    raw = json.load(open(os.path.join(HERE, "ocr_raw.json")))
    doc = pymupdf.open(SRC)
    out = []
    for pno_s, rows in raw.items():
        pno = int(pno_s)
        page = doc[pno - 1]
        for idx, r in enumerate(rows):
            if "F," not in r[4] and "F." not in r[4]:
                continue
            comps, box_top, box_bot, cx0, cy0 = line_components(page, r)
            base, cap = baseline_of(comps, box_top, box_bot)
            if base is None:
                out.append(dict(page=pno, line=idx, text=r[4], err="no baseline"))
                continue
            subs = [c for c in comps
                    if c["y0"] > base + 1 and c["y0"] <= box_bot + 2
                    and 0.30 * cap <= c["h"] <= 0.95 * cap
                    and c["w"] <= 1.4 * c["h"]]
            out.append(dict(page=pno, line=idx, text=r[4], nfound=len(subs),
                            expected=r[4].count("F,") + r[4].count("F."),
                            base=base, cap=cap, box_bot=box_bot,
                            glyphs=[dict(x=c["x0"], y0=c["y0"], y1=c["y1"], w=c["w"], h=c["h"],
                                         art="\n".join("".join("#" if v else "." for v in row)
                                                       for row in c["arr"]))
                                    for c in subs]))
    json.dump(out, open(os.path.join(HERE, "sub_candidates.json"), "w"), indent=1)
    ok = sum(1 for o in out if o.get("nfound") == o.get("expected"))
    print("lines:", len(out), "count-matching:", ok)
    for o in out:
        flag = "OK " if o.get("nfound") == o.get("expected") else "!! "
        print("%sp%02d L%-3d n=%d exp=%d  %s" %
              (flag, o["page"], o["line"], o.get("nfound", -1), o.get("expected", -1), o["text"][:60]))


if __name__ == "__main__":
    main()
