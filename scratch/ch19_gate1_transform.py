#!/usr/bin/env python3
"""
Ch19 Gate 1 finaliser (session 1-Z + schema fix).

Does four machine-verifiable things to the working inventory so it can be frozen:

  1. SCHEMA FIX. The working file used columns
        | ID | Section | Src | Type | Exact original wording | Ticked |
     which puts the wording in cell[4]. check_pdf._extract_labels reads the
     wording from cell[3], so it parsed ZERO labels (check 6 would be blind).
     We reorder to the canonical-compatible layout
        | ID | Section | Type | Exact original wording | Src | Ticked |
     -> wording is cell[3] (parser works) and the tick stays last (check 7 works),
     while the valuable Src page is preserved as cell[4].

  2. 1-Z FOLDS. Insert the 6 SUMMARY-UNIQUE facts found in the p.11-12 SUMMARY,
     each interleaved into the body section it belongs to.

  3. RENUMBER. Content facts become F001..F(n) in Content Order; the 7 figure-label
     rows keep their tail position and are renumbered after the content block.
     Every old->new ID change is applied to the prose OUTSIDE the table too.

  4. RECOUNT. Row total, ID range, per-Type census are all machine-derived and
     printed, never hand-tallied.

Writes <inventory>.new.md; does NOT touch the original until reviewed.
"""
import re, sys, io
from collections import Counter

INV = "notes/class 11/Ch19_ChemicalCoordinationAndIntegration/Ch19_ChemicalCoordinationAndIntegration_inventory.md"
OUT = "notes/class 11/Ch19_ChemicalCoordinationAndIntegration/Ch19_ChemicalCoordinationAndIntegration_inventory.new.md"

src = open(INV, encoding="utf-8").read()
lines = src.split("\n")

# ---- locate the Facts table (header row that starts "| ID | Section | Src |") ----
hdr_i = None
for i, ln in enumerate(lines):
    if ln.strip().startswith("| ID | Section | Src | Type"):
        hdr_i = i
        break
assert hdr_i is not None, "Facts header row not found"
sep_i = hdr_i + 1
assert set(lines[sep_i].strip()) <= set("|-: "), f"expected separator at {sep_i}: {lines[sep_i]!r}"

# data rows run until the first non-'|' line
end_i = sep_i + 1
rows = []
while end_i < len(lines) and lines[end_i].strip().startswith("|"):
    cells = [c.strip() for c in lines[end_i].strip().strip("|").split("|")]
    assert len(cells) == 6, f"row {end_i} has {len(cells)} cells: {lines[end_i]!r}"
    rows.append(cells)  # [ID, Section, Src, Type, wording, Ticked]
    end_i += 1

print(f"Parsed {len(rows)} data rows (F{rows[0][0]}..{rows[-1][0]})")

# ---- current (pre-fix) type census, straight from the table ----
cur_types = Counter(r[3] for r in rows)
print("CURRENT type census:", dict(cur_types), "sum:", sum(cur_types.values()))

# split content vs label rows by wording prefix
def is_label_row(r):
    return re.match(r"figure(\s*\([a-z]\))?\s*labels", r[4], re.I) is not None

content = [r for r in rows if not is_label_row(r)]
labels  = [r for r in rows if is_label_row(r)]
print(f"content rows: {len(content)}  label rows: {len(labels)}")

# ---- the 6 SUMMARY-UNIQUE folds (session 1-Z), each as [Section, Src, Type, wording] ----
# inserted immediately AFTER the given anchor original-ID.
FOLDS = [
    ("F040", ["19.2.2", "11", "number",
        "Pars distalis produces six trophic hormones."]),
    ("F083", ["19.2.4", "12", "concept",
        "The thyroid gland hormones play an important role in the regulation of the "
        "basal metabolic rate, development and maturation of the central neural system, "
        "erythropoiesis, metabolism of carbohydrates, proteins and fats, menstrual cycle."]),
    ("F084", ["19.2.4", "12", "concept",
        "Another thyroid hormone, i.e., thyrocalcitonin regulates calcium levels in our "
        "blood by decreasing it."]),
    ("F122", ["19.2.7", "12", "process",
        "Glucocorticoids stimulate gluconeogenesis, lipolysis, proteolysis, erythropoiesis, "
        "cardio-vascular system, blood pressure, and glomerular filtration rate and inhibit "
        "inflammatory reactions by suppressing the immune response."]),
    ("F142", ["19.2.8", "12", "concept",
        "Insulin deficiency and/or insulin resistance result in a disease called diabetes "
        "mellitus."]),
    ("F153", ["19.2.9", "12", "concept",
        "The testis secretes androgens, which stimulate the development, maturation and "
        "functions of the male accessory sex organs, appearance of the male secondary sex "
        "characters, spermatogenesis, male sexual behaviour, anabolic pathways and "
        "erythropoiesis."]),
]
fold_by_anchor = {}
for anchor, payload in FOLDS:
    fold_by_anchor.setdefault(anchor, []).append(payload)

# ---- build new content order with folds interleaved ----
new_content = []
for r in content:
    new_content.append(r)
    if r[0] in fold_by_anchor:
        for payload in fold_by_anchor[r[0]]:
            sec, srcpg, typ, wording = payload
            new_content.append(["__NEW__", sec, srcpg, typ, wording, "x"])

new_order = new_content + labels  # labels stay at the tail

# ---- assign contiguous IDs, build old->new map ----
old2new = {}
for idx, r in enumerate(new_order, 1):
    nid = f"F{idx:03d}"
    if r[0] != "__NEW__":
        old2new[r[0]] = nid
    r[0] = nid

n_total = len(new_order)
n_content = len(new_content)
n_labels = len(labels)
print(f"NEW total rows: {n_total}  (content {n_content} + labels {n_labels})")
# report where each fold landed (by matching exact wording)
fold_wordings = {p[3] for _, p in FOLDS}
for r in new_order:
    if r[4] in fold_wordings:
        print(f"  FOLD -> {r[0]} [{r[1]} | Src {r[2]} | {r[3]}] {r[4][:52]}...")

# ---- emit new Facts table (canonical-compatible column order) ----
tbl = []
tbl.append("| ID | Section | Type | Exact original wording | Src | Ticked |")
tbl.append("|---|---|---|------------------------|---:|--------|")
for r in new_order:
    _id, sec, srcpg, typ, wording, tick = r
    tbl.append(f"| {_id} | {sec} | {typ} | {wording} | {srcpg} | {tick} |")
new_table = "\n".join(tbl)

# ---- new type census (machine) ----
new_types = Counter(r[3] for r in new_order)
print("NEW type census:", dict(new_types), "sum:", sum(new_types.values()))

# ---- reassemble file: prose-before + new table + prose-after, with ID remap on prose ----
before = "\n".join(lines[:hdr_i])
after = "\n".join(lines[end_i:])

def remap_ids(text):
    return re.sub(r"F\d{3}", lambda m: old2new.get(m.group(0), m.group(0)), text)

before = remap_ids(before)
after = remap_ids(after)

new_file = before + "\n" + new_table + "\n" + after

open(OUT, "w", encoding="utf-8").write(new_file)
print(f"\nWROTE {OUT}")

# ---- self-validate with check_pdf._extract_labels ----
sys.path.insert(0, ".")
import check_pdf
parsed = check_pdf._extract_labels(new_file)
figs = Counter(f for f, _ in parsed)
print("\n_extract_labels on NEW file:")
print("  label rows / figures:", len(figs), "->", dict(figs))
print("  total labels:", len(parsed))
# contiguity + dup check
ids = [r[0] for r in new_order]
assert ids == [f"F{i:03d}" for i in range(1, n_total + 1)], "IDs not contiguous!"
assert len(set(ids)) == len(ids), "duplicate IDs!"
print("  contiguous F001..F%03d, no gaps, no dups: OK" % n_total)
# phantom check: no figure id equal to 'Fig #' or containing dashes
assert "Fig #" not in figs and "#" not in "".join(figs), "phantom Fig # row!"
print("  no phantom 'Fig #' rows: OK")
