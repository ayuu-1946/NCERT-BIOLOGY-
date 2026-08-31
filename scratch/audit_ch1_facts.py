"""Pass-3 fact-coverage audit for Ch1 Sexual Reproduction in Flowering Plants.

For every Facts row in the frozen inventory, pull the content words out of the
"exact original wording" cell and measure how many of them actually appear in
the rendered PDF text. Rows below the threshold are printed so they can be
fixed in the generating script before any row is ticked.
"""
import re
import sys

import pymupdf

BASE = "notes/class 12/Ch1_SexualReproductionInFloweringPlants/Ch1_SexualReproductionInFloweringPlants"
INV = BASE + "_inventory.md"
PDF = BASE + ".pdf"
THRESHOLD = float(sys.argv[1]) if len(sys.argv) > 1 else 0.70

STOP = set("""a an the and or of to in on for with by from as at is are was were be been being
this that these those it its their his her they them we us you your i he she which who whom whose
not no but if then than so such also more most many much some any all both each other another
into onto over under after before during while when where why how what very can could may might
will would shall should must do does did done have has had there here own same off out up down
one two three four five six seven eight nine ten""".split())


def words(text):
    text = text.lower().replace("\u2013", " ").replace("\u2014", " ").replace("\u2019", "'")
    return [w for w in re.findall(r"[a-z']+", text) if len(w) > 2 and w not in STOP]


def stem(w):
    for suf in ("ies", "ing", "ers", "ed", "es", "s", "e"):
        if w.endswith(suf) and len(w) - len(suf) >= 4:
            return w[: -len(suf)]
    return w


doc = pymupdf.open(PDF)
pdf_raw = " ".join(p.get_text() for p in doc)
pdf_stems = {stem(w) for w in words(pdf_raw)}

rows = []
in_facts = False
for line in open(INV, encoding="utf-8"):
    line = line.rstrip("\n")
    if line.startswith("## "):
        in_facts = line.strip().lower() == "## facts"
        continue
    if not in_facts or not line.startswith("| F"):
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) < 5:
        continue
    rows.append((cells[0], cells[1], cells[2], cells[3]))

print(f"Facts rows parsed: {len(rows)}   threshold={THRESHOLD:.0%}")
weak = []
for fid, sec, typ, wording in rows:
    ws = words(wording)
    if not ws:
        continue
    missing = [w for w in ws if stem(w) not in pdf_stems]
    cov = 1 - len(missing) / len(ws)
    if cov < THRESHOLD:
        weak.append((cov, fid, sec, typ, missing, wording))

weak.sort()
print(f"\nrows below threshold: {len(weak)}\n" + "=" * 78)
for cov, fid, sec, typ, missing, wording in weak:
    print(f"{fid} [{sec} / {typ}] coverage={cov:.0%}")
    print(f"   missing: {sorted(set(missing))}")
    print(f"   wording: {wording[:200]}")
    print("-" * 78)
