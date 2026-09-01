"""Ch19 Gate 3(b) — re-derive every claimed number from disk.

Per Gate 1 Closure rule 1: a handoff's findings are claims to re-derive, not
results to apply. Nothing here is read from CHAPTER_STATUS.md or the tracker;
everything is parsed off the inventory, the script and the committed PDF.
"""
import hashlib
import importlib.util
import os
import re
import sys
from collections import Counter

REPO = "/vercel/share/v0-project"
CH = os.path.join(REPO, "notes/class 11/Ch19_ChemicalCoordinationAndIntegration")
INV = os.path.join(CH, "Ch19_ChemicalCoordinationAndIntegration_inventory.md")
PY = os.path.join(CH, "Ch19_ChemicalCoordinationAndIntegration.py")
PDF = os.path.join(CH, "Ch19_ChemicalCoordinationAndIntegration.pdf")
SRC = os.path.join(REPO, "Chapter/class 11/Chapter 19 - Chemical Coordination and Integration.pdf")

fails = []


def check(label, ok, detail=""):
    print(("  OK   " if ok else "  FAIL ") + label + ("  " + detail if detail else ""))
    if not ok:
        fails.append(label)


print("=" * 78)
print("1. INVENTORY ROWS")
print("=" * 78)
inv_text = open(INV, encoding="utf-8").read()
lines = inv_text.splitlines()

# Facts table rows: | Fnnn | section | type | wording | ticked |
row_re = re.compile(r"^\|\s*(F\d+[a-z]?)\s*\|")
rows = []
for ln in lines:
    m = row_re.match(ln.strip())
    if m:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        rows.append(cells)
print(f"  parsed Facts rows: {len(rows)}")
ids = [r[0] for r in rows]
check("218 rows", len(rows) == 218, f"got {len(rows)}")
check("no duplicate IDs", len(set(ids)) == len(ids), f"{len(ids)-len(set(ids))} dupes")
nums = [int(re.sub(r"\D", "", i)) for i in ids]
check("contiguous F001..F218", nums == list(range(1, len(nums) + 1)),
      f"first gap at {next((i for i, (a, b) in enumerate(zip(nums, range(1, len(nums)+1))) if a != b), None)}")
check("IDs monotonic", all(b > a for a, b in zip(nums, nums[1:])))

ticked = [r for r in rows if r[-1].lower().strip() in ("x", "[x]")]
check("all rows ticked", len(ticked) == len(rows), f"{len(ticked)}/{len(rows)}")

types = Counter(r[2] for r in rows)
print("  Type census:", dict(sorted(types.items())))
check("Type values all lowercase", all(t == t.lower() for t in types), str([t for t in types if t != t.lower()]))
check("census sums to row count", sum(types.values()) == len(rows))
matrix_rows = [r for r in rows
               if re.match(r"figure(\s*\([a-z]\))?\s*labels", r[3], re.I)]
print(f"  figure-label matrix rows: {len(matrix_rows)}  content Facts: {len(rows)-len(matrix_rows)}")

print()
print("=" * 78)
print("2. REAL _extract_labels FROM check_pdf.py (never reimplemented)")
print("=" * 78)
spec = importlib.util.spec_from_file_location("check_pdf", os.path.join(REPO, "check_pdf.py"))
cp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cp)
# NOTE: _extract_labels takes the inventory TEXT, not a path. Passing the path
# returns [] silently — a green-looking empty result. That is exactly the
# "documented trap is not a fired trap" hazard, so the call is asserted below.
labels = cp._extract_labels(inv_text)          # list[(fig_id, label)]
per_fig = Counter(fid for fid, _ in labels)
total = len(labels)
print(f"  label-bearing figures: {len(per_fig)}  labels: {total}")
print("  per figure:", dict(per_fig))
check("7 label-bearing figures", len(per_fig) == 7, f"got {len(per_fig)}")
check("38 labels", total == 38, f"got {total}")
check("no phantom 'Fig #' row", not any(k.strip().lower() in ("fig #", "fig#") for k in per_fig))
pair_dupes = [p for p, n in Counter(labels).items() if n > 1]
check("no doubled (figure,label) pairs", not pair_dupes, str(pair_dupes[:3]))
check("matrix row count == label-bearing figures", len(matrix_rows) == len(per_fig),
      f"{len(matrix_rows)} rows vs {len(per_fig)} figures")

print()
print("=" * 78)
print("3. SCRIPT SHAPE")
print("=" * 78)
py = open(PY, encoding="utf-8").read()
blocks = re.findall(r"^# ---- (.+?) ----", py, re.M)
print(f"  block markers ({len(blocks)}): {blocks}")
check("18 block markers", len(blocks) == 18, f"got {len(blocks)}")
check("0 ParagraphStyle re-declared", py.count("ParagraphStyle") == 0, str(py.count("ParagraphStyle")))
check("0 fontName re-declared", py.count("fontName") == 0, str(py.count("fontName")))
print(f"  figure() calls: {len(re.findall(r'^story.append\(figure\(|figure\(\"fig_', py, re.M))}")
print(f"  asset refs: {sorted(set(re.findall(r'fig_19_[0-9a-z]+', py)))}")

print()
print("=" * 78)
print("4. COMMITTED PDF")
print("=" * 78)
import pymupdf
doc = pymupdf.open(PDF)
sizes = {(round(p.rect.width), round(p.rect.height)) for p in doc}
text = "".join(p.get_text() for p in doc)
nimg = sum(len(p.get_images(full=True)) for p in doc)
sha = hashlib.sha256(text.encode()).hexdigest()[:16]
print(f"  pages: {doc.page_count}  page sizes: {sizes}  images: {nimg}")
print(f"  extracted chars: {len(text)}  text SHA-256[:16]: {sha}")
check("14 pages", doc.page_count == 14, str(doc.page_count))
check("all A4 upright", sizes == {(595, 842)}, str(sizes))
check("7 embedded images", nimg == 7, str(nimg))
doc.close()

# The Gate 2 record claims 31,137 chars / SHA 08d68d03f8d3c05f. pymupdf gives a
# different number, so measure the OTHER extractor too before calling it drift:
# a char count is meaningless without naming the extractor that produced it.
import pdfplumber
with pdfplumber.open(PDF) as pl:
    pl_text = "".join((p.extract_text() or "") for p in pl.pages)
pl_sha = hashlib.sha256(pl_text.encode()).hexdigest()[:16]
print(f"  pdfplumber chars: {len(pl_text)}  SHA[:16]: {pl_sha}")
print(f"  pymupdf    chars: {len(text)}  SHA[:16]: {sha}")
recorded_hit = 31137 in (len(text), len(pl_text)) or "08d68d03f8d3c05f" in (sha, pl_sha)
check("recorded 31,137 / SHA 08d68d03f8d3c05f reproduced by SOME extractor",
      recorded_hit, "neither pymupdf nor pdfplumber reproduces it")

print()
print("=" * 78)
print("5. SOURCE PDF")
print("=" * 78)
sdoc = pymupdf.open(SRC)
print(f"  source pages: {sdoc.page_count}")
words = sum(len(p.get_text("words")) for p in sdoc)
print(f"  source words in text layer: {words}")
check("14 source pages", sdoc.page_count == 14, str(sdoc.page_count))
sdoc.close()

print()
print("=" * 78)
print("VERDICT:", "GREEN — every re-derived number matches disk" if not fails else f"RED — {len(fails)} mismatch(es)")
print("=" * 78)
for f in fails:
    print("  -", f)
sys.exit(1 if fails else 0)
