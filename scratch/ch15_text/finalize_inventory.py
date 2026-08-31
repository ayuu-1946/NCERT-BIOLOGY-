"""Assign contiguous IDs to the Ch15 inventory and derive every header count by
re-parsing the finished table (SUPREME COMMAND PROMPT v6, section 6 step 10).

Run:  /vercel/share/neetenv/bin/python scratch/ch15_text/finalize_inventory.py
"""
import collections
import importlib.util
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
INV = ROOT / "notes/class 11/Ch15_BodyFluidsAndCirculation/Ch15_BodyFluidsAndCirculation_inventory.md"

text = INV.read_text()

# ---- 1. assign IDs sequentially in file order -------------------------------
counter = [0]


def _next(_m):
    counter[0] += 1
    return "F%03d" % counter[0]


text = re.sub(r"F###", _next, text)
total = counter[0]

# ---- 2. re-parse the finished tables ---------------------------------------
def rows_of(section: str):
    """Return the pipe-delimited data rows of a named '## section'."""
    m = re.search(r"^## " + re.escape(section) + r"\s*$", text, re.M)
    assert m, "section not found: " + section
    body = text[m.end():]
    body = re.split(r"^## ", body, maxsplit=1, flags=re.M)[0]
    out = []
    for line in body.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 4 or not re.fullmatch(r"F\d{3}", cells[0]):
            continue
        out.append(cells)
    return out


facts = rows_of("Facts")
matrix = rows_of("Figure-label matrix")

ids = [r[0] for r in facts + matrix]
assert len(ids) == len(set(ids)), "duplicate IDs"
nums = [int(i[1:]) for i in ids]
assert nums == list(range(1, len(nums) + 1)), "IDs not contiguous/monotonic"
assert len(ids) == total, "unassigned F### placeholders remain"

types = collections.Counter(r[2] for r in facts + matrix)
assert all(t == t.lower() for t in types), "Type column not lowercase"

heading_rows = [r for r in facts if r[2] == "heading"]
opener_rows = [r for r in facts if r[2] == "opener"]
folded_rows = [r for r in facts if r[3].startswith("FOLDED SUMMARY-UNIQUE")]
numbered = [r for r in heading_rows if re.search(r"\b15(\.\d+)+", r[3])]
unnumbered = [r for r in heading_rows if r not in numbered]
ticked = [r for r in facts + matrix if r[4].strip()]

# ---- 3. check_pdf.py's own _extract_labels --------------------------------
spec = importlib.util.spec_from_file_location("check_pdf", ROOT / "check_pdf.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
labels = mod._extract_labels(text)
figs = collections.Counter(f for f, _ in labels)
dupes = [p for p, n in collections.Counter(labels).items() if n > 1]
phantom = [f for f in figs if not re.fullmatch(r"Fig 15\.\d", f)]
label_parse = ("%d labels across %d figure rows (%s), no doubling, no phantom row"
               % (len(labels), len(figs),
                  " / ".join("%s: %d" % (f, figs[f]) for f in sorted(figs))))

# ---- 4. substitute every derived count ------------------------------------
fold_ids = {}
for r in folded_rows:
    m = re.search(r"summary sentence (S\d+)\)", r[3])
    fold_ids["FOLD_" + m.group(1)] = r[0]

subs = {
    "COUNT_TOTAL": str(total),
    "COUNT_FACTS": str(len(facts)),
    "COUNT_MATRIX": str(len(matrix)),
    "COUNT_RANGE": "`%s`-`%s`" % (ids[0], ids[-1]),
    "COUNT_HEAD_NUM": str(len(numbered)),
    "COUNT_HEAD_UNNUM": str(len(unnumbered)),
    "COUNT_HEADING": str(len(heading_rows)),
    "COUNT_OPENER": str(len(opener_rows)),
    "COUNT_1S": str(len(facts) - len(heading_rows) - len(opener_rows) - len(folded_rows)),
    "COUNT_1Z": str(len(folded_rows)),
    "TYPE_CENSUS": " · ".join("`%s` %d" % (t, n) for t, n in types.most_common()) + " = %d" % total,
    "TYPE_COUNT": str(len(types)),
    "LABEL_PARSE": label_parse,
    **fold_ids,
}
for k in sorted(subs, key=len, reverse=True):
    text = text.replace(k, subs[k])

leftovers = re.findall(r"COUNT_[A-Z0-9_]+|TYPE_[A-Z]+|LABEL_PARSE|FOLD_S\d+", text)
assert not leftovers, "unsubstituted placeholders: %s" % set(leftovers)

INV.write_text(text)

print("rows total        :", total)
print("  facts table     :", len(facts))
print("  matrix table    :", len(matrix))
print("ID range          :", ids[0], "->", ids[-1], "(contiguous, no dupes)")
print("heading rows      :", len(heading_rows), "=", len(numbered), "numbered +",
      len(unnumbered), "unnumbered")
print("opener rows       :", len(opener_rows))
print("folded S-U rows   :", len(folded_rows), [r[0] for r in folded_rows])
print("ticked rows       :", len(ticked))
print("type census       :", dict(types.most_common()))
print("label parse       :", label_parse)
print("duplicate labels  :", dupes)
print("phantom fig rows  :", phantom)
print("openers == headings-2+1 :", len(opener_rows) == len(heading_rows) - 2 + 1)
sys.exit(0)
