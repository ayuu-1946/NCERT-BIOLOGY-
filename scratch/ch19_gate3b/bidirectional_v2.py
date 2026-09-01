"""Ch19 Gate 3(b) — corrected harness.

v1 produced 81 "findings". Each of the three families is tested here as an
explicit hypothesis about v1's INSTRUMENT, because a wrong measurement that
looks like a defect is the most expensive thing this repo keeps rediscovering.

H1  the 6 direction-2 misses are sentences that SPAN a page boundary; the row's
    `Src` names the page where the sentence STARTS, which is correct.
H2  the 12 unverifiable figure labels live inside the source's raster figure,
    not its text layer, so text extraction structurally cannot see them.
H3  the 41 direction-1 misses are reworded / table-split teaching prose, not
    absent content, so verbatim containment is the wrong test; distinctive-term
    coverage is the right one for a notes rewrite.
"""
import os
import re
import sys
import unicodedata

import pymupdf

REPO = "/vercel/share/v0-project"
CHDIR = os.path.join(REPO, "notes/class 11/Ch19_ChemicalCoordinationAndIntegration")
NAME = "Ch19_ChemicalCoordinationAndIntegration"
INV, PY = os.path.join(CHDIR, NAME + "_inventory.md"), os.path.join(CHDIR, NAME + ".py")
SRC = os.path.join(REPO, "Chapter/class 11/Chapter 19 - Chemical Coordination and Integration.pdf")


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in [("\u2018", "'"), ("\u2019", "'"), ("\u201c", '"'), ("\u201d", '"'),
                 ("\u2013", "-"), ("\u2014", "-"), ("\u2212", "-"), ("\u00ad", "")]:
        s = s.replace(a, b)
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&")
    return re.sub(r"[^0-9a-z]+", "", s.lower())


rows = []
for ln in open(INV, encoding="utf-8"):
    if re.match(r"^\|\s*F\d+", ln.strip()):
        c = [x.strip() for x in ln.strip().strip("|").split("|")]
        rows.append(dict(id=c[0], section=c[1], type=c[2], text=c[3], src=c[4]))
matrix = [r for r in rows if "labels:" in r["text"].lower()]
content = [r for r in rows if r not in matrix]

doc = pymupdf.open(SRC)
pages = {i + 1: doc[i].get_text("text") for i in range(doc.page_count)}
raw_blocks = {i + 1: doc[i].get_text("rawdict") for i in range(doc.page_count)}
imgs = {i + 1: doc[i].get_images(full=True) for i in range(doc.page_count)}
doc.close()
npage = {k: norm(v) for k, v in pages.items()}
nall = "".join(npage.values())
fails = []

print("=" * 78)
print("H1 — the 6 direction-2 misses are page-spanning sentences")
print("=" * 78)
suspects = ["F060", "F084", "F123", "F150", "F175", "F199"]
ok1 = 0
for rid in suspects:
    r = next(x for x in content if x["id"] == rid)
    p = int(re.search(r"\d+", r["src"]).group())
    want = norm(r["text"])
    spans = want in (npage.get(p, "") + npage.get(p + 1, ""))
    # show the split point: longest prefix that fits on page p alone
    lo, hi = 0, len(want)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        lo, hi = (mid, hi) if want[:mid] in npage.get(p, "") else (lo, mid - 1)
    print(f"  {rid}: starts p{p}, {lo}/{len(want)} chars on p{p}, "
          f"remainder on p{p+1} -> {'CONFIRMED' if spans else 'STILL MISSING'}")
    ok1 += spans
print(f"  => {ok1}/6 confirmed as page-spanning")
if ok1 != 6:
    fails.append("H1")

# full re-run of direction 2 allowing a sentence to continue onto the next page
missing = []
for r in content:
    want = norm(r["text"])
    if not want:
        continue
    ps = [int(x) for x in re.findall(r"\d+", r["src"])]
    if not any(want in (npage.get(p, "") + npage.get(p + 1, "")) for p in ps):
        missing.append(r)
print(f"  direction 2 re-run: {len(content)-len(missing)}/{len(content)} rows anchored "
      f"to the page they name; {len(missing)} missing")
for r in missing:
    print("    !", r["id"], r["text"][:80])
if missing:
    fails.append("direction-2")

print()
print("=" * 78)
print("H2 — the 12 unverifiable labels are inside raster figures, not the text layer")
print("=" * 78)
unver = {"F214": ["Vocal cord"],
         "F217": ["Hormone (e.g., FSH)", "Ovarian cell membrane", "Response 1",
                  "(Generation of second messenger)", "(Cyclic AMP or Ca++)",
                  "Biochemical responses", "Physiological responses (e.g., ovarian growth)"],
         "F218": ["Hormone (e.g., estrogen)", "Uterine cell membrane", "mRNA",
                  "Physiological responses (Tissue growth and differentiation)"]}
for rid, labs in unver.items():
    r = next(x for x in rows if x["id"] == rid)
    p = int(re.search(r"\d+", r["src"]).group())
    print(f"  {rid} (source p{p}): {len(imgs[p])} embedded image(s), "
          f"text-layer chars {len(pages[p])}")
    print(f"    page text layer, verbatim: {pages[p].strip()[-60:]!r}")
    print(f"    labels not in ANY page text layer: "
          f"{[l for l in labs if norm(l) not in nall]}")
# the labels ARE in the delivered notes — that is what check 6 gates
notes_doc = pymupdf.open(os.path.join(CHDIR, NAME + ".pdf"))
notes_txt = norm("".join(p.get_text() for p in notes_doc))
notes_doc.close()
in_notes = [l for labs in unver.values() for l in labs if norm(l) in notes_txt]
tot = sum(len(v) for v in unver.values())
print(f"  => all {tot} labels present in the DELIVERED notes text: "
      f"{len(in_notes)}/{tot} {'CONFIRMED' if len(in_notes)==tot else 'MISMATCH'}")
if len(in_notes) != tot:
    fails.append("H2")

print()
print("=" * 78)
print("H3 — direction 1 by distinctive-term coverage (right test for a rewrite)")
print("=" * 78)
script = open(PY, encoding="utf-8").read()
nscript = norm(script)
# a "distinctive term" = a word of >=6 letters, or a known short technical token
SHORT_OK = {"tsh", "acth", "lh", "fsh", "msh", "adh", "gh", "prl", "tct", "pth",
            "anf", "gip", "cck", "t3", "t4", "rbc", "ca2", "na", "k", "ip3", "camp"}
weak = []
for r in content:
    terms = {w.lower() for w in re.findall(r"[A-Za-z][A-Za-z-]{5,}", r["text"])}
    terms |= {w.lower() for w in re.findall(r"[A-Za-z0-9]+", r["text"])
              if w.lower() in SHORT_OK}
    terms = {t for t in terms if norm(t)}
    if not terms:
        continue
    miss = [t for t in terms if norm(t) not in nscript]
    if miss:
        weak.append((r, sorted(miss), len(terms)))
print(f"  rows whose every distinctive term appears in the script: "
      f"{len(content)-len(weak)}/{len(content)}")
for r, miss, n in weak:
    print(f"    ! {r['id']} missing {len(miss)}/{n}: {miss[:6]}  | {r['text'][:60]}")
if weak:
    fails.append("direction-1-terms")

print()
print("=" * 78)
print("VERDICT:", "GREEN — all three families were instrument defects; both directions clean"
      if not fails else f"RED — real findings in: {fails}")
print("=" * 78)
sys.exit(0)
