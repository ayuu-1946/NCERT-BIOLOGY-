"""Session 1-Z, step 8: reconstruct the SUMMARY block in true reading order and
split it into sentences, machine-counted.

Why this is not a plain get_text() call: pymupdf emits page 21's blocks in
non-visual order, so the raw page text splices the tail of section 7.5.4's body
prose (blocks at y=84..418) into the middle of the summary. Selecting by
*block* geometry fixes it cleanly:

  - page 21: the single text block that starts below the 'SUMMARY' heading
    (heading at y=440.5; the summary block is x0=52.3, y0=469.7, y1=700.5).
  - page 22: the blocks above the 'EXERCISES' heading (y=288.2), which carry
    the summary's continuation.

A first attempt selected spans by an x-band derived from the heading's own x0
(185.5) and silently dropped the summary's entire first half, producing a
spliced 8-sentence result whose sentence 1 read "Plasmodium falciparum , if not
afforded by vaccination and immunisation." That nonsense sentence is what
exposed the bug -- recorded here so the failure mode is not re-tried.

Usage: /vercel/share/neetenv/bin/python scratch/ch7_1z/summary_sentences.py
"""
import re
import pymupdf

PDF = "Chapter/class 12/Chapter 7 - Human Health and Disease.pdf"
JUNK = ("HUMAN HEALTH AND DISEASE", "BIOLOGY", "Reprint 2026-27", "SUMMARY")


def blocks(page):
    out = []
    for blk in page.get_text("dict")["blocks"]:
        if blk.get("type") != 0:
            continue
        txt = " ".join(s["text"] for line in blk["lines"] for s in line["spans"])
        out.append((blk["bbox"], txt))
    return out


def find_heading(page, word):
    hits = [b for b in blocks(page) if b[1].strip() == word]
    assert len(hits) == 1, f"expected exactly 1 {word!r} block, got {len(hits)}"
    return hits[0][0]


def main():
    doc = pymupdf.open(PDF)

    # ---- page 21: the one block below the SUMMARY heading ----
    p21 = doc[20]
    hy = find_heading(p21, "SUMMARY")[1]
    below = [b for b in blocks(p21) if b[0][1] > hy and b[1].strip()]
    # drop page furniture: the page-number tab and the reprint stamp
    below = [b for b in below
             if not any(j in b[1] for j in JUNK) and not b[1].strip().isdigit()]
    below.sort(key=lambda b: (round(b[0][1], 1), b[0][0]))
    assert len(below) == 1, (
        f"expected 1 summary block on p21, got {len(below)}: "
        + str([(b[0], b[1][:40]) for b in below])
    )
    part21 = below[0][1]
    print(f"p21 summary block bbox={tuple(round(v,1) for v in below[0][0])}")

    # ---- page 22: blocks above the EXERCISES heading ----
    p22 = doc[21]
    ey = find_heading(p22, "EXERCISES")[1]
    top = [b for b in blocks(p22) if b[0][3] <= ey and b[1].strip()]
    top = [b for b in top
           if not any(j in b[1] for j in JUNK) and not b[1].strip().isdigit()]
    top.sort(key=lambda b: (round(b[0][1], 1), b[0][0]))
    print(f"p22 pre-EXERCISES blocks: {len(top)}")
    for b in top:
        print(f"   bbox={tuple(round(v,1) for v in b[0])} | {b[1][:60]}")
    part22 = " ".join(b[1] for b in top)

    text = re.sub(r"\s+", " ", part21 + " " + part22).strip()
    # NCERT sets italic binomials as separate spans, leaving " ," artifacts
    text = re.sub(r"\s+([,.])", r"\1", text)

    print("\n---- reconstructed summary ----")
    print(text)
    print("\nchars:", len(text))

    parts = re.split(r"(?<=[.])\s+(?=[A-Z\u2018\u201c(])", text)
    parts = [p.strip() for p in parts if p.strip()]
    print("\n---- sentences ----")
    for i, s in enumerate(parts, 1):
        print(f"{i:2d}. {s}")
    print(f"\nSENTENCE COUNT: {len(parts)}")


if __name__ == "__main__":
    main()
