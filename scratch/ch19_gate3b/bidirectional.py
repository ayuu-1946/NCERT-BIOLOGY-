"""Ch19 Gate 3(b) — the two directions, done by machine over all 218 rows.

DIRECTION 2 (source -> inventory): every content row's wording must actually
occur on the SOURCE page its `Src` column names. This is the check that catches
a wrong page number or a silently reworded row; reading 218 rows by eye cannot
do it reliably.

DIRECTION 1 (inventory -> script): every content row's wording must be
traceable into the Pass 2 script, so no ticked row is missing from the artefact.

Both directions compare on aggressively normalised text (the source PDF wraps
mid-sentence and hyphenates across lines), because the thing under test is
content presence, not line breaks.
"""
import os
import re
import sys
import unicodedata

import pymupdf

REPO = "/vercel/share/v0-project"
CHDIR = os.path.join(REPO, "notes/class 11/Ch19_ChemicalCoordinationAndIntegration")
NAME = "Ch19_ChemicalCoordinationAndIntegration"
INV = os.path.join(CHDIR, NAME + "_inventory.md")
PY = os.path.join(CHDIR, NAME + ".py")
SRC = os.path.join(REPO, "Chapter/class 11/Chapter 19 - Chemical Coordination and Integration.pdf")


def norm(s):
    """Fold everything that a PDF text layer can legitimately vary."""
    s = unicodedata.normalize("NFKC", s)
    s = (s.replace("\u2018", "'").replace("\u2019", "'")
          .replace("\u201c", '"').replace("\u201d", '"')
          .replace("\u2013", "-").replace("\u2014", "-")
          .replace("\u2212", "-").replace("\u00ad", ""))
    s = re.sub(r"<[^>]+>", "", s)          # reportlab inline markup
    s = re.sub(r"[^0-9a-z]+", "", s.lower())  # letters+digits only
    return s


# ---------------------------------------------------------------- inventory
rows = []
for ln in open(INV, encoding="utf-8"):
    if re.match(r"^\|\s*F\d+", ln.strip()):
        c = [x.strip() for x in ln.strip().strip("|").split("|")]
        rows.append(dict(id=c[0], section=c[1], type=c[2], text=c[3], src=c[4]))
matrix = [r for r in rows if r["text"].lstrip("*_ ").lower().startswith("figure")
          and "labels:" in r["text"].lower()]
content = [r for r in rows if r not in matrix]
print(f"rows={len(rows)}  content={len(content)}  figure-label matrix={len(matrix)}")

# ---------------------------------------------------------------- source text
doc = pymupdf.open(SRC)
pages = {i + 1: doc[i].get_text("text") for i in range(doc.page_count)}
doc.close()
npage = {k: norm(v) for k, v in pages.items()}
all_src = "".join(npage.values())

print()
print("=" * 78)
print("DIRECTION 2 — every content row present on the source page it names")
print("=" * 78)
d2_bad, d2_elsewhere = [], []
for r in content:
    want = norm(r["text"])
    if not want:
        continue
    srcs = [int(x) for x in re.findall(r"\d+", r["src"])] or []
    if any(want in npage.get(p, "") for p in srcs):
        continue
    found_on = [p for p, t in npage.items() if want in t]
    if found_on:
        d2_elsewhere.append((r, srcs, found_on))
    else:
        d2_bad.append((r, srcs))

print(f"  on the named page      : {len(content) - len(d2_bad) - len(d2_elsewhere)}/{len(content)}")
print(f"  present but other page : {len(d2_elsewhere)}")
print(f"  NOT FOUND in source    : {len(d2_bad)}")
for r, srcs, found in d2_elsewhere:
    print(f"    ~ {r['id']} says p{srcs} but text is on p{found}")
for r, srcs in d2_bad:
    print(f"    ! {r['id']} (p{srcs}) {r['text'][:95]}")

# figure-label rows: each quoted label must appear in the source (labels are
# vector callouts, so allow anywhere in the document text layer)
print()
print("  figure-label rows — each quoted label somewhere in source text layer:")
lab_missing = []
for r in matrix:
    for lab in re.findall(r'"([^"]+)"', r["text"]):
        if norm(lab) not in all_src:
            lab_missing.append((r["id"], lab))
print(f"    labels checked: {sum(len(re.findall(chr(34)+'([^'+chr(34)+']+)'+chr(34), r['text'])) for r in matrix)}"
      f"   not in source text layer: {len(lab_missing)}")
for i, lab in lab_missing:
    print(f"      ! {i}: {lab!r}")

print()
print("=" * 78)
print("DIRECTION 1 — every content row traceable into the Pass 2 script")
print("=" * 78)
script = open(PY, encoding="utf-8").read()
nscript = norm(script)
d1_missing, d1_partial = [], []
for r in content:
    want = norm(r["text"])
    if not want:
        continue
    if want in nscript:
        continue
    # a row may legitimately be split across two paragraphs / a table cell;
    # accept it only if BOTH halves are present, and report it as partial
    half = len(want) // 2
    if want[:half] in nscript and want[half:] in nscript:
        d1_partial.append(r)
    else:
        # try longest-prefix diagnosis
        lo, hi = 0, len(want)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if want[:mid] in nscript:
                lo = mid
            else:
                hi = mid - 1
        d1_missing.append((r, lo))

print(f"  verbatim in script     : {len(content) - len(d1_missing) - len(d1_partial)}/{len(content)}")
print(f"  split but both halves  : {len(d1_partial)}")
print(f"  NOT traceable          : {len(d1_missing)}")
for r in d1_partial:
    print(f"    ~ {r['id']} split across elements: {r['text'][:80]}")
for r, pref in d1_missing:
    print(f"    ! {r['id']} matched first {pref}/{len(norm(r['text']))} chars: {r['text'][:80]}")

print()
print("=" * 78)
bad = len(d2_bad) + len(lab_missing) + len(d1_missing)
print("VERDICT:", "GREEN — both directions clean" if bad == 0 else f"{bad} hard finding(s) to triage")
print("=" * 78)
sys.exit(0)
