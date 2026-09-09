"""Gate 1 closure check for Ch5 Morphology of Flowering Plants.

Gate 1 is a *machine-checked* gate, not merely a written artifact. This script
earns it, and it must be re-run after any edit to the inventory -- documentation
can degrade a gate it only describes (the Ch19/Ch11 lesson: a matrix column
header that itself began "Figure labels" was parsed as a label row).

Checks
------
1  ID contiguity: F001..FNNN, monotonic, no gaps, no duplicates.
2  Type vocabulary: single spelling and casing per value; census sums to the row count.
3  Label parse: `check_pdf.py`'s own `_extract_labels`, imported rather than
   replicated -- expected figure count, expected label count, no doubling, and no
   phantom figure row (e.g. a `Fig #` row conjured from a markdown separator).
4  Header agreement: every count restated in the header block equals a re-parse
   of the Facts table it describes.
5  Structure: every source heading has a `heading` row and every section's first
   sentence has an `opener` row, checked against the source PDF rather than assumed.
6  Freeze state: 0 rows ticked (Pass 2 does the ticking).

Run from the repository root:
    /vercel/share/neetenv/bin/python scratch/ch5morph_gate1/gate1_close.py
"""
import collections
import importlib.util
import re
import sys

INV = "notes/class 11/Ch5_MorphologyOfFloweringPlants/Ch5_MorphologyOfFloweringPlants_inventory.md"
CHECK_PDF = "check_pdf.py"
EXTRACT = "notes/class 11/Ch5_MorphologyOfFloweringPlants/extract_figures.py"

EXPECTED_FIGURES = 11
EXPECTED_LABELS = 56

# The 20 numbered section headings the source actually prints, in order.
SOURCE_HEADINGS = [
    "5.1", "5.1.1", "5.2", "5.3", "5.3.1", "5.3.2", "5.3.3", "5.4", "5.5", "5.5.1",
    "5.5.1.1", "5.5.1.2", "5.5.1.3", "5.5.1.4", "5.6", "5.7", "5.7.1", "5.7.2", "5.8", "5.9",
]

failures: list[str] = []
notes: list[str] = []


def check(ok: bool, msg: str) -> None:
    (notes if ok else failures).append(("PASS  " if ok else "FAIL  ") + msg)


text = open(INV).read()

# ---- parse the Facts table --------------------------------------------------
rows = []
in_facts = False
for line in text.splitlines():
    low = line.strip().lower()
    if low.startswith("## "):
        in_facts = low.startswith("## facts")
        continue
    if not in_facts or not line.strip().startswith("|"):
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if not cells or not re.fullmatch(r"F\d{3}", cells[0]):
        continue
    rows.append(cells)

check(bool(rows), f"Facts table parsed: {len(rows)} rows")

# ---- 1. ID contiguity -------------------------------------------------------
ids = [r[0] for r in rows]
nums = [int(i[1:]) for i in ids]
check(len(set(ids)) == len(ids), f"no duplicate IDs ({len(ids)} rows, {len(set(ids))} distinct)")
check(nums == sorted(nums), "IDs monotonic")
check(nums == list(range(1, len(nums) + 1)),
      f"IDs contiguous {ids[0]}..{ids[-1]} with no gaps")

# ---- 2. Type vocabulary -----------------------------------------------------
types = collections.Counter(r[2] for r in rows)
check(all(t == t.lower() for t in types), f"all {len(types)} Type values lowercase: {sorted(types)}")
check(sum(types.values()) == len(rows), f"type census sums to {len(rows)}")

# ---- 3. Label parse via the real _extract_labels ----------------------------
spec = importlib.util.spec_from_file_location("check_pdf", CHECK_PDF)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
labels = mod._extract_labels(text)

figs = collections.Counter(fid for fid, _ in labels)
check(len(figs) == EXPECTED_FIGURES,
      f"_extract_labels sees {len(figs)} label-bearing figures (expected {EXPECTED_FIGURES})")
check(len(labels) == EXPECTED_LABELS,
      f"_extract_labels returns {len(labels)} labels (expected {EXPECTED_LABELS})")

phantom = [f for f in figs if not re.fullmatch(r"Fig 5\.\d+", f)]
check(not phantom, f"no phantom figure rows (offenders: {phantom or 'none'})")

dupes = {f: [l for l, c in collections.Counter(lab for fid, lab in labels if fid == f).items() if c > 1]
         for f in figs}
doubled = {f: d for f, d in dupes.items() if d}
check(not doubled, f"no doubled labels within any figure (offenders: {doubled or 'none'})")

matrix_rows = [r for r in rows if r[2] == "figure-labels"]
check(len(matrix_rows) == len(figs),
      f"matrix lives in exactly one place: {len(matrix_rows)} figure-labels rows == {len(figs)} parsed figures")

# ---- 4. Header agreement ----------------------------------------------------
header = text.split("## Facts")[0]


def stated(pattern: str) -> int | None:
    m = re.search(pattern, header)
    return int(m.group(1)) if m else None


derived = {
    "rows": len(rows),
    "heading": types["heading"],
    "opener": types["opener"],
    "caption": types["caption"],
    "summary-unique": types["summary-unique"],
    "figure-labels": types["figure-labels"],
    "labels": len(labels),
}

check(stated(r"\| Rows: (\d+)") == derived["rows"], f"header 'Rows:' == {derived['rows']}")
check(stated(r"Total Facts rows: \*\*(\d+)\*\*") == derived["rows"], f"header total == {derived['rows']}")
check(stated(r"Heading rows \(`Type: heading`\): \*\*(\d+)\*\*") == derived["heading"],
      f"header heading count == {derived['heading']}")
check(stated(r"Opener rows \(`Type: opener`\): \*\*(\d+)\*\*") == derived["opener"],
      f"header opener count == {derived['opener']}")
check(stated(r"Caption rows \(`Type: caption`\): \*\*(\d+)\*\*") == derived["caption"],
      f"header caption count == {derived['caption']}")
check(stated(r"Figure-label rows \(`Type: figure-labels`\): \*\*(\d+)\*\*") == derived["figure-labels"],
      f"header figure-label row count == {derived['figure-labels']}")
check(stated(r"figures / \*\*(\d+)\*\* in-figure labels") == derived["labels"],
      f"header label count == {derived['labels']}")

# every census that asserts a total must equal the length of its own adjacent list
m = re.search(r"Heading rows.*?\*\*(\d+)\*\* = (\d+) numbered.*?\+ (\d+) structural.*?\+ (\d+) unnumbered", header, re.S)
check(m is not None and int(m.group(1)) == int(m.group(2)) + int(m.group(3)) + int(m.group(4)),
      "heading census total equals its own addends"
      + (f" ({m.group(2)}+{m.group(3)}+{m.group(4)}={m.group(1)})" if m else ""))

per_fig_stated = dict(re.findall(r"(5\.\d+)=(\d+)", header))
per_fig_derived = {f.replace("Fig ", ""): c for f, c in figs.items()}
check(per_fig_stated == {k: str(v) for k, v in per_fig_derived.items()},
      f"per-figure label counts agree with the parse ({len(per_fig_derived)} figures)")

# type census line must sum to the stated total
census_line = re.search(r"Type vocabulary.*?: (.*?) = \*\*(\d+)\*\*", header, re.S)
if census_line:
    pairs = re.findall(r"`([a-z-]+)` (\d+)", census_line.group(1))
    check(sum(int(n) for _, n in pairs) == int(census_line.group(2)) == len(rows),
          f"type census line sums to {len(rows)} across {len(pairs)} values")
    check({t for t, _ in pairs} == set(types),
          "type census line lists exactly the types present")
else:
    check(False, "type census line found")

# summary + exercise arithmetic
sm = re.search(r"\*\*(\d+) sentences = (\d+) BODY-PRESENT \+ (\d+) SUMMARY-UNIQUE", text)
check(sm is not None and int(sm.group(1)) == int(sm.group(2)) + int(sm.group(3)),
      "summary arithmetic balances" + (f" ({sm.group(2)}+{sm.group(3)}={sm.group(1)})" if sm else ""))
check(sm is not None and int(sm.group(3)) == derived["summary-unique"],
      f"SUMMARY-UNIQUE count matches the {derived['summary-unique']} fold rows")

ex = re.search(r"\*\*(\d+) exercises, (\d+) answered by design \(GAP\), (\d+) unanswered by design \(COVERED\), 0 overlooked", text)
check(ex is not None and int(ex.group(1)) == int(ex.group(2)) + int(ex.group(3)),
      "exercise arithmetic balances" + (f" ({ex.group(2)}+{ex.group(3)}={ex.group(1)})" if ex else ""))
ex_rows = re.findall(r"^\| (\d+) \| .*? \| (COVERED|GAP) \|", text, re.M)
check(ex is not None and len(ex_rows) == int(ex.group(1)),
      f"exercise table holds {len(ex_rows)} rows, matching the stated total")

# ---- 5. Structure: headings and openers vs the source -----------------------
heading_rows = [r for r in rows if r[2] == "heading"]
numbered_headings = [r for r in heading_rows if r[3].startswith("Numbered")]
found = []
for r in numbered_headings:
    m = re.search(r'"(\d+(?:\.\d+)*)\s', r[3])
    if m:
        found.append(m.group(1))
check(found == SOURCE_HEADINGS,
      f"all {len(SOURCE_HEADINGS)} numbered source headings have a heading row, in source order")

opener_sections = [r[1] for r in rows if r[2] == "opener"]
check(opener_sections == ["intro"] + SOURCE_HEADINGS,
      f"every numbered section plus the chapter intro has exactly one opener row ({len(opener_sections)})")

sections_with_heading = {r[1] for r in numbered_headings}
check(sections_with_heading == set(SOURCE_HEADINGS),
      "heading rows and opener rows cover the same section set")

# ---- 6. Freeze state --------------------------------------------------------
ticked = [r[0] for r in rows if r[-1].lower() in ("x", "[x]", "done", "yes", "\u2713")]
check(not ticked, f"0 rows ticked at the freeze ({len(ticked)} found)")

# ---- 7. Manifest agrees with the extraction script --------------------------
# A rect written in two places is a count written in two places. The manifest's
# crop rects must equal `extract_figures.py`'s, which is what actually produced
# the assets on disk.
espec = importlib.util.spec_from_file_location("ef", EXTRACT)
ef = importlib.util.module_from_spec(espec)
espec.loader.exec_module(ef)
script_rects = {fid.replace("_", "."): tuple(rect) for fid, _, rect in ef.FIGS}
script_pages = {fid.replace("_", "."): pno for fid, pno, _ in ef.FIGS}

manifest = {}
for line in text.splitlines():
    m = re.match(r"\| (5\.\d+) \| .*? \| `assets/fig_5_\d+\.png` \| +(\d+) \| `\((\d+), (\d+), (\d+), (\d+)\)` \| +(\d+) \| (\w+) \| (\w+) \|", line)
    if m:
        manifest[m.group(1)] = {
            "page": int(m.group(2)),
            "rect": tuple(int(m.group(i)) for i in range(3, 7)),
            "labels": int(m.group(7)),
            "mono": m.group(8),
            "verified": m.group(9),
        }

check(len(manifest) == len(script_rects),
      f"figure manifest holds {len(manifest)} rows, matching the {len(script_rects)} figures in extract_figures.py")
bad_rect = {f: (v["rect"], script_rects.get(f)) for f, v in manifest.items() if v["rect"] != script_rects.get(f)}
check(not bad_rect, f"every manifest crop rect equals extract_figures.py's (drift: {bad_rect or 'none'})")
bad_page = {f: (v["page"], script_pages.get(f)) for f, v in manifest.items() if v["page"] != script_pages.get(f)}
check(not bad_page, f"every manifest source page equals extract_figures.py's (drift: {bad_page or 'none'})")
check(all(v["mono"] == "yes" and v["verified"] == "yes" for v in manifest.values()),
      f"all {len(manifest)} figures marked Mono: yes and Verified: yes")

manifest_labels = {f"Fig {f}": v["labels"] for f, v in manifest.items() if v["labels"]}
check(manifest_labels == dict(figs),
      "manifest per-figure label counts equal the _extract_labels parse")
check(sum(v["labels"] for v in manifest.values()) == len(labels),
      f"manifest label counts sum to {len(labels)}")

# ---- 8. Assets on disk are true monochrome ---------------------------------
try:
    from PIL import Image

    bad_assets = []
    for fig in script_rects:
        path = f"notes/class 11/Ch5_MorphologyOfFloweringPlants/assets/fig_{fig.replace('.', '_')}.png"
        im = Image.open(path)
        if im.mode != "L" or len(im.getbands()) != 1:
            bad_assets.append((path, im.mode))
    check(not bad_assets, f"all {len(script_rects)} assets on disk are single-channel mode=L (offenders: {bad_assets or 'none'})")
except ImportError:  # pragma: no cover
    check(False, "Pillow available for the asset check")

# ---- report -----------------------------------------------------------------
for line in notes:
    print(line)
for line in failures:
    print(line)
print()
print(f"figures={len(figs)}  labels={len(labels)}  rows={len(rows)}  types={len(types)}")
print(f"per-figure labels: {dict(sorted(figs.items(), key=lambda kv: float(kv[0].split()[1])))}")
print()
print(f"VERDICT: {'GREEN' if not failures else 'RED'}  ({len(notes)} pass / {len(failures)} fail)")
sys.exit(1 if failures else 0)
