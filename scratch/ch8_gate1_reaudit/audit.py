"""
Independent Gate 1 re-derivation for Class 12 Ch8 — Microbes in Human Welfare.

Rule 1 of the Gate 1 Closure & Handoff Rules: a predecessor's findings are claims
to re-derive, not results to apply. This script trusts nothing written in the
inventory header, the census sections, the Gate 1 checklist, or the status
documents. It re-parses the frozen table and reports DERIVED vs CLAIMED.

Run with the venv interpreter:
    /vercel/share/neetenv/bin/python scratch/ch8_gate1_reaudit/audit.py
"""

import os
import re
import sys
from collections import Counter

REPO = "/vercel/share/v0-project"
sys.path.insert(0, REPO)

from check_pdf import _extract_labels  # the real parser, not a reimplementation

CH = os.path.join(REPO, "notes/class 12/Ch8_MicrobesInHumanWelfare")
INV = os.path.join(CH, "Ch8_MicrobesInHumanWelfare_inventory.md")
ASSETS = os.path.join(CH, "assets")

text = open(INV, encoding="utf-8").read()
lines = text.splitlines()

fails, warns = [], []


def check(label, derived, claimed):
    ok = derived == claimed
    print(f"  [{'OK ' if ok else 'FAIL'}] {label}: derived={derived!r} claimed={claimed!r}")
    if not ok:
        fails.append(f"{label}: derived {derived!r} != claimed {claimed!r}")


def assert_(label, cond, detail=""):
    print(f"  [{'OK ' if cond else 'FAIL'}] {label}{(' — ' + detail) if detail else ''}")
    if not cond:
        fails.append(f"{label}: {detail}")


# ---------------------------------------------------------------------------
# 0. Section boundaries, so each table is parsed from its own region only.
# ---------------------------------------------------------------------------
def section_span(heading):
    start = None
    for i, ln in enumerate(lines):
        if ln.strip() == heading:
            start = i
            break
    if start is None:
        raise SystemExit(f"section not found: {heading}")
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("## "):
            return start, j
    return start, len(lines)


def rows_in(a, b):
    """Real table data rows: pipe rows with >=5 cells, skipping header/separator."""
    out = []
    for ln in lines[a:b]:
        s = ln.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 5:
            continue
        if set(cells[0]) <= set("-: ") or cells[0] in ("ID",):
            continue
        out.append(cells)
    return out


facts_a, facts_b = section_span("## Facts")
mat_a, mat_b = section_span("## Figure-label matrix")
sum_a, sum_b = section_span("## Summary classification")
gap_a, gap_b = section_span("## Exercise-gap terms")
man_a, man_b = section_span("## Figure manifest")

facts = rows_in(facts_a, facts_b)
matrix = rows_in(mat_a, mat_b)

print("\n=== 1. Row counts and ID integrity ===")
check("Facts-table rows", len(facts), 200)
check("Figure-label-matrix rows", len(matrix), 9)
check("Total rows", len(facts) + len(matrix), 209)

ids = [r[0] for r in facts] + [r[0] for r in matrix]
assert_("no duplicate IDs", len(ids) == len(set(ids)),
        f"{[i for i, n in Counter(ids).items() if n > 1]}")

base = sorted(int(i[1:]) for i in ids if re.fullmatch(r"F\d+", i))
suffixed = sorted(i for i in ids if not re.fullmatch(r"F\d+", i))
expected = list(range(1, 208))
assert_("F001..F207 contiguous, no gaps", base == expected,
        f"missing={sorted(set(expected) - set(base))} extra={sorted(set(base) - set(expected))}")
check("suffixed Pass 3 rows", suffixed, ["F055a", "F085a"])

print("\n=== 2. Type vocabulary and per-type census ===")
types = Counter(r[2] for r in facts)
mtypes = Counter(r[2] for r in matrix)
declared_vocab = {"heading", "opener", "caption", "term", "number",
                  "name", "fact", "question", "crossref", "label"}
seen = set(types) | set(mtypes)
assert_("Type values all inside declared normalized vocabulary",
        seen <= declared_vocab, f"unexpected={sorted(seen - declared_vocab)}")
assert_("Type values all lowercase (no casing split)",
        all(t == t.lower() for t in seen), f"non-lowercase={sorted(t for t in seen if t != t.lower())}")
check("type census (Facts table)", dict(sorted(types.items())),
      {"caption": 8, "crossref": 6, "fact": 97, "heading": 15, "name": 29,
       "number": 5, "opener": 14, "question": 7, "term": 19})
check("matrix rows all Type=label", dict(mtypes), {"label": 9})
check("heading rows", types["heading"], 15)
check("opener rows", types["opener"], 14)
check("caption rows", types["caption"], 8)

print("\n=== 3. check_pdf.py _extract_labels (the machine-checked criterion) ===")
labels = _extract_labels(text)
figs = sorted({f for f, _ in labels})
check("individual labels parsed", len(labels), 17)
check("parsed figure rows", len(figs), 5)
assert_("no doubled labels", len(labels) == len(set(labels)),
        f"{[x for x, n in Counter(labels).items() if n > 1]}")
assert_("no phantom 'Fig #' / separator figure row",
        not any(f in ("Fig #", "", "?") or set(f) <= set("-: ") for f in figs), f"{figs}")
per_fig = Counter(f for f, _ in labels)
check("per-figure label distribution", dict(sorted(per_fig.items())),
      {"Fig 8.1": 2, "Fig 8.2 (a)": 6, "Fig 8.2 (c)": 1, "Fig 8.3": 1, "Fig 8.8": 7})
unlabelled = [r[0] for r in matrix if not re.match(r"figure(\s*\([a-z]\))?\s*labels", r[3], re.I)]
check("rows invisible to parser by design", unlabelled,
      ["F203", "F204", "F205", "F206"])

print("\n=== 4. Ticks ===")
unticked = [r[0] for r in facts + matrix if r[4].strip().lower() != "x"]
check("unticked rows", len(unticked), 0)

print("\n=== 5. Summary classification and exercise gaps ===")
srows = [r for r in rows_in(sum_a, sum_b)] + [
    [c.strip() for c in ln.strip().strip("|").split("|")]
    for ln in lines[sum_a:sum_b]
    if ln.strip().startswith("|") and len([c for c in ln.strip().strip("|").split("|")]) == 3
    and not set(ln.strip().strip("|").split("|")[0].strip()) <= set("-: ")
    and ln.strip().strip("|").split("|")[0].strip() != "Summary sentence"
]
summary = [r for r in srows if len(r) == 3]
check("summary sentences classified", len(summary), 18)
su = [r for r in summary if "SUMMARY-UNIQUE" in r[1]]
bp = [r for r in summary if r[1].strip() == "BODY-PRESENT"]
check("SUMMARY-UNIQUE", len(su), 2)
check("BODY-PRESENT", len(bp), 16)
folded = sorted(re.findall(r"F\d+", " ".join(r[2] for r in su)))
check("SUMMARY-UNIQUE folded into body rows", folded, ["F195", "F196"])
assert_("every folded ID exists as a real row", all(f in ids for f in folded))

gaps = [r for r in [
    [c.strip() for c in ln.strip().strip("|").split("|")]
    for ln in lines[gap_a:gap_b] if ln.strip().startswith("|")
] if len(r) == 2 and not set(r[0]) <= set("-: ") and not r[0].startswith("Term/fact")]
check("exercise-gap terms", len(gaps), 4)
assert_("every exercise-gap term has a planned home", all(r[1] for r in gaps))

print("\n=== 6. Figure manifest vs assets on disk ===")
# The manifest section also contains the 1-F "Rects" sub-table, so the manifest
# table is bounded at the first "### " sub-heading and shaped by its own 6 columns.
man_end = next((i for i in range(man_a, man_b) if lines[i].startswith("### ")), man_b)
man = [r for r in [
    [c.strip() for c in ln.strip().strip("|").split("|")]
    for ln in lines[man_a:man_end] if ln.strip().startswith("|")
] if len(r) == 6 and not set(r[0]) <= set("-: ") and r[0] != "Fig #"]
check("manifest rows", len(man), 9)
assert_("every manifest row marks Mono: yes and Verified: yes",
        all(r[4].lower() == "yes" and r[5].lower() == "yes" for r in man),
        str([r[0] for r in man if not (r[4].lower() == "yes" and r[5].lower() == "yes")]))
on_disk = sorted(f for f in os.listdir(ASSETS) if f.lower().endswith(".png"))
check("PNG assets on disk", len(on_disk), 9)
manifest_files = sorted(re.sub(r"^assets/", "", c.strip("`")) for c in (r[2] for r in man))
check("manifest asset files == files on disk", manifest_files, on_disk)

try:
    from PIL import Image
    modes = {f: Image.open(os.path.join(ASSETS, f)).mode for f in on_disk}
    bad = {f: m for f, m in modes.items() if m != "L"}
    assert_("every asset single-channel grayscale (PIL mode L)", not bad, str(bad))
except ImportError:
    warns.append("Pillow unavailable — asset mode not verified")

print("\n=== 7. Census sections must be derivable from their own lists ===")
census = "\n".join(lines[391:446])
h_numbered = re.findall(r"`(F\d+)` 8\.", census.split("Unnumbered")[0])
h_unnum = re.findall(r"`(F\d+)`", census.split("Unnumbered (6):")[1].split("The three")[0])
check("heading census: numbered IDs listed", len(h_numbered), 9)
check("heading census: unnumbered IDs listed", len(h_unnum), 6)
check("heading census total = list length = type census", len(h_numbered) + len(h_unnum), types["heading"])
real_headings = {r[0] for r in facts if r[2] == "heading"}
assert_("every heading census ID is a real Type:heading row",
        set(h_numbered + h_unnum) == real_headings,
        f"census-only={sorted(set(h_numbered+h_unnum)-real_headings)} rows-only={sorted(real_headings-set(h_numbered+h_unnum))}")

opener_block = census.split("**14 opener rows**")[1].split("That is 14")[0]
o_ids = re.findall(r"`(F\d+)`", opener_block)
check("opener census: IDs listed", len(o_ids), 14)
check("opener census total = list length = type census", len(o_ids), types["opener"])
real_openers = {r[0] for r in facts if r[2] == "opener"}
assert_("every opener census ID is a real Type:opener row",
        set(o_ids) == real_openers,
        f"census-only={sorted(set(o_ids)-real_openers)} rows-only={sorted(real_openers-set(o_ids))}")

print("\n=== 8. Pass 1 five-session evidence ===")
tracker = open(os.path.join(CH, "Ch8_TRACKER.md"), encoding="utf-8").read()
for sess in ("1-S", "1-H", "1-O", "1-F", "1-Z"):
    assert_(f"session {sess} recorded in Ch8_TRACKER.md", sess in tracker)

print("\n=== 9. Cross-document agreement (Gate 3(b) rule 2) ===")
status = open(os.path.join(REPO, "CHAPTER_STATUS.md"), encoding="utf-8").read()
trk = open(os.path.join(REPO, "CHAPTER_TRACKER.md"), encoding="utf-8").read()
derived_marks = {
    "209": len(facts) + len(matrix),
    "200": len(facts),
    "17 labels": len(labels),
    "15 headings": types["heading"],
    "14 openers": types["opener"],
    "9 assets": len(on_disk),
}
for doc_name, doc in (("CHAPTER_STATUS.md", status), ("CHAPTER_TRACKER.md", trk)):
    seg = "\n".join(l for l in doc.splitlines() if re.search(r"microbes", l, re.I))
    for token, val in (("209", 209), ("200", 200)):
        if token in seg:
            assert_(f"{doc_name} restates {token} consistently with derivation",
                    val in (len(facts) + len(matrix), len(facts)))

print("\n=== 10. Stale-claim sweep (live assertions only) ===")
for pat in (r"Gate 1 OPEN", r"GATE 1 NOT MET", r"Gate 1 not met"):
    hits = [(i + 1, l) for i, l in enumerate(lines) if re.search(pat, l, re.I)]
    assert_(f"no live '{pat}' claim in Ch8 inventory", not hits, str(hits[:3]))
prev = [(i + 1, l[:90]) for i, l in enumerate(lines)
        if re.search(r"\b198 rows\b", l) and not re.search(r"previous|was |wrong|At Gate 1", l)]
assert_("no live stale '198 rows' assertion (quoted history allowed)", not prev, str(prev))

print("\n" + "=" * 72)
if fails:
    print(f"GATE 1 RE-DERIVATION: {len(fails)} FAIL(S)")
    for f in fails:
        print("  - " + f)
else:
    print("GATE 1 RE-DERIVATION: GREEN — every claimed count reproduced from the file itself.")
for w in warns:
    print("  warn: " + w)
print("=" * 72)
sys.exit(1 if fails else 0)
