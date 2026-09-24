"""Gate 1 sessions 1-H / 1-O re-derivation for Ch1 (v2).

The source scan HAS a text layer, so the independent re-derivation is:
  (a) list every bold span that reads like a heading (page + size + font),
      so the 26 inventory heading rows can be compared against the source;
  (b) for each inventory heading row and opener row, confirm the quoted
      wording exists in the source text (whitespace-normalised) —
      a row whose text cannot be found in the source is a red flag.
"""
import os
import re

import pymupdf

ROOT = "/home/user/NCERT-BIOLOGY-"
SRC = os.path.join(ROOT, "Chapter/class 12/Chapter 1 - Sexual Reproduction in Flowering Plants.pdf")
INV = os.path.join(ROOT, "notes/class 12/Ch1_SexualReproductionInFloweringPlants/Ch1_SexualReproductionInFloweringPlants_inventory.md")

doc = pymupdf.open(SRC)

# ---------- (a) bold heading-like spans ----------
print("=== A) bold spans (potential headings), by page ===")
for i, page in enumerate(doc, 1):
    d = page.get_text("dict")
    for b in d["blocks"]:
        if b.get("type") != 0:
            continue
        for l in b["lines"]:
            line_txt = "".join(s["text"] for s in l["spans"])
            line_stripped = line_txt.strip()
            if not line_stripped or len(line_stripped) > 100:
                continue
            for s in l["spans"]:
                fl = s["flags"]
                if not (fl & 16):  # not bold
                    continue
                t = s["text"].strip()
                if not t:
                    continue
                # skip running header 'BIOLOGY'
                if t.upper() in ("BIOLOGY",):
                    continue
                print(f"p{i:2d} sz={s['size']:.1f} {s['font']:24s} | {line_stripped[:90]}")

# ---------- (b) inventory rows vs source text ----------
raw = "\n".join(p.get_text() for p in doc)
def norm(s):
    s = s.replace("\u2013", "-").replace("\u2014", "-").replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = re.sub(r"-\s*\n\s*", "", s)     # de-hyphenate across line breaks
    s = re.sub(r"\s+", " ", s)
    return s.lower()

SRC_N = norm(raw)

inv = open(INV, encoding="utf-8").read()
lines = inv.splitlines()
in_facts = False
rows = []
for ln in lines:
    if ln.startswith("## Facts"):
        in_facts = True
        continue
    if in_facts and ln.startswith("## "):
        break
    if in_facts and ln.strip().startswith("|"):
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) >= 5 and cells[0].startswith("F"):
            rows.append(cells)

def quoted_fragments(wording):
    """First quoted fragment = the part the row claims verbatim from NCERT."""
    m = re.match(r'^"([^"]+)"', wording.strip())
    if m:
        return [m.group(1)]
    return [wording.strip().strip('"')]

print("\n=== B) heading rows vs source ===")
missing = []
for r in rows:
    if r[2] != "heading":
        continue
    frag = quoted_fragments(r[3])[0]
    f = norm(frag)
    # strip the section number prefix for matching (numbers may have spaces)
    ok = f in SRC_N or re.sub(r"^\d+(\.\d+)*\s+", "", f) in SRC_N
    if not ok:
        missing.append((r[0], frag[:80]))
    print(f"{r[0]}: {'FOUND' if ok else 'MISSING!'}  {frag[:70]}")

print("\n=== C) opener rows vs source (full quoted sentence) ===")
miss_o = []
for r in rows:
    if r[2] != "opener":
        continue
    frags = re.findall(r'"([^"]+)"', r[3])
    # verify the longest quoted fragment
    if frags:
        frag = max(frags, key=len)
    else:
        frag = r[3].strip()
    f = norm(frag)
    # tolerate ellipses: split on '...' and require each piece
    pieces = [norm(p) for p in frag.split("...") if norm(p)]
    ok = all(p in SRC_N for p in pieces)
    if not ok:
        miss_o.append((r[0], frag[:80]))
    print(f"{r[0]}: {'FOUND' if ok else 'MISSING!'}  {frag[:70]}")

print()
print(f"heading rows missing from source: {len(missing)}")
for m in missing:
    print("   ", m)
print(f"opener rows missing from source: {len(miss_o)}")
for m in miss_o:
    print("   ", m)
