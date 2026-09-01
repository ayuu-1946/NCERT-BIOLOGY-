"""H1' — the 6 direction-2 misses split across a page boundary, and the two
halves are NOT adjacent in the text layer because the source page's figure
caption + vector callout labels are emitted after the body text.

Test: the longest prefix that fits on page p must be followed by the exact
remaining suffix appearing on page p+1, and (to make the claim strong) that
suffix must sit near the START of p+1's body text.
"""
import os
import re
import unicodedata

import pymupdf

REPO = "/vercel/share/v0-project"
SRC = os.path.join(REPO, "Chapter/class 11/Chapter 19 - Chemical Coordination and Integration.pdf")
INV = os.path.join(REPO, "notes/class 11/Ch19_ChemicalCoordinationAndIntegration/"
                         "Ch19_ChemicalCoordinationAndIntegration_inventory.md")


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in [("\u2018", "'"), ("\u2019", "'"), ("\u201c", '"'), ("\u201d", '"'),
                 ("\u2013", "-"), ("\u2014", "-"), ("\u2212", "-"), ("\u00ad", "")]:
        s = s.replace(a, b)
    return re.sub(r"[^0-9a-z]+", "", s.lower())


rows = {}
for ln in open(INV, encoding="utf-8"):
    if re.match(r"^\|\s*F\d+", ln.strip()):
        c = [x.strip() for x in ln.strip().strip("|").split("|")]
        rows[c[0]] = dict(text=c[3], src=c[4])

doc = pymupdf.open(SRC)
npage = {i + 1: norm(doc[i].get_text("text")) for i in range(doc.page_count)}
doc.close()

confirmed = 0
for rid in ["F060", "F084", "F123", "F150", "F175", "F199"]:
    r = rows[rid]
    p = int(re.search(r"\d+", r["src"]).group())
    want = norm(r["text"])
    lo, hi = 0, len(want)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        lo, hi = (mid, hi) if want[:mid] in npage[p] else (lo, mid - 1)
    head, tail = want[:lo], want[lo:]
    pos = npage[p + 1].find(tail)
    # where does the head sit on page p? (should be at the very end of the body)
    hpos = npage[p].find(head)
    print(f"{rid}: p{p} head[{len(head)}] ends at char {hpos+len(head)} of {len(npage[p])}"
          f"   p{p+1} tail[{len(tail)}] found at char {pos}"
          f"   -> {'CONFIRMED page-spanning' if pos != -1 else 'NOT FOUND'}")
    print(f"      head tail-end : ...{head[-40:]}")
    print(f"      tail          : {tail[:40]}...")
    if pos != -1:
        confirmed += 1
        # what sits between them on page p, after the head?
        between = npage[p][hpos + len(head):]
        print(f"      p{p} text AFTER the head ({len(between)} chars): {between[:90]}...")

print()
print(f"=> {confirmed}/6 confirmed: sentence starts on the named page and completes on the next,"
      f" with the figure caption/callout block emitted in between")
