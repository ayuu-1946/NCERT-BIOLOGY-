"""Re-parse the frozen Ch15 inventory and assert every header count matches.

Idempotent: reads only, never writes. Run after any hand edit to the inventory.
    /vercel/share/neetenv/bin/python "notes/class 11/Ch15_BodyFluidsAndCirculation/verify_inventory.py"
"""
import collections
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
INV = HERE / "Ch15_BodyFluidsAndCirculation_inventory.md"
text = INV.read_text()

assert "F###" not in text, "unassigned F### placeholders remain"
leftovers = re.findall(r"COUNT_[A-Z0-9_]+|TYPE_[A-Z]+|LABEL_PARSE|FOLD_S\d+", text)
assert not leftovers, "unsubstituted placeholders: %s" % set(leftovers)


def rows_of(section):
    m = re.search(r"^## " + re.escape(section) + r"\s*$", text, re.M)
    assert m, "section not found: " + section
    body = re.split(r"^## ", text[m.end():], maxsplit=1, flags=re.M)[0]
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


facts, matrix = rows_of("Facts"), rows_of("Figure-label matrix")
rows = facts + matrix
ids = [r[0] for r in rows]

assert len(ids) == len(set(ids)), "duplicate IDs"
assert [int(i[1:]) for i in ids] == list(range(1, len(ids) + 1)), "IDs not contiguous"

types = collections.Counter(r[2] for r in rows)
assert all(t == t.lower() for t in types), "Type column not lowercase"

headings = [r for r in facts if r[2] == "heading"]
openers = [r for r in facts if r[2] == "opener"]
folded = [r for r in facts if r[3].startswith("FOLDED SUMMARY-UNIQUE")]
numbered = [r for r in headings if re.search(r"\b15(\.\d+)+", r[3])]
ticked = [r for r in rows if r[4].strip()]

spec = importlib.util.spec_from_file_location("check_pdf", ROOT / "check_pdf.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
labels = mod._extract_labels(text)
figs = collections.Counter(f for f, _ in labels)
phantom = [f for f in figs if not re.fullmatch(r"Fig 15\.\d", f)]
dupes = [p for p, n in collections.Counter(labels).items() if n > 1]

# ---- header claims must equal the machine parse ---------------------------
def claim(pattern):
    m = re.search(pattern, text)
    assert m, "header claim not found: " + pattern
    return int(m.group(1))


checks = {
    "facts rows": (claim(r"Facts-table rows \(`## Facts`\) \| (\d+)"), len(facts)),
    "matrix rows": (claim(r"Figure-label-matrix rows \(`## Figure-label matrix`\) \| (\d+)"), len(matrix)),
    "total rows": (claim(r"\| Total rows \| (\d+) \|"), len(rows)),
    "heading rows": (claim(r"Heading rows \(`Type: heading`\) \| (\d+)"), len(headings)),
    "opener rows": (claim(r"Opener rows \(`Type: opener`\) \| (\d+)"), len(openers)),
    "ticked rows": (claim(r"Ticked rows \| (\d+) of"), len(ticked)),
    "header Rows:": (claim(r"Rows: (\d+)"), len(rows)),
    "numbered heads": (claim(r"(\d+) numbered \+ \d+ unnumbered"), len(numbered)),
    "unnumbered heads": (claim(r"\d+ numbered \+ (\d+) unnumbered"), len(headings) - len(numbered)),
    "heading census": (claim(r"Heading census — (\d+) rows"), len(headings)),
    "opener census": (claim(r"Opener census — (\d+) rows"), len(openers)),
    "folded S-U": (claim(r"BODY-PRESENT \+ (\d+) SUMMARY-UNIQUE"), len(folded)),
}
bad = {k: v for k, v in checks.items() if v[0] != v[1]}

print("rows        : %d (facts %d + matrix %d)" % (len(rows), len(facts), len(matrix)))
print("id range    : %s -> %s, contiguous, no dupes" % (ids[0], ids[-1]))
print("headings    : %d = %d numbered + %d unnumbered" % (len(headings), len(numbered), len(headings) - len(numbered)))
print("openers     : %d  (= headings %d - 3 + 1 intro: %s)"
      % (len(openers), len(headings), len(openers) == len(headings) - 3 + 1))
print("folded S-U  : %d %s" % (len(folded), [r[0] for r in folded]))
print("ticked      : %d" % len(ticked))
print("types (%d)  : %s" % (len(types), dict(types.most_common())))
print("labels      : %d across %d figs %s"
      % (len(labels), len(figs), " / ".join("%s:%d" % (f, figs[f]) for f in sorted(figs))))
print("phantom figs: %s" % phantom)
print("dupe labels : %s" % dupes)
print("header claims mismatched: %s" % (bad or "none"))

# ---- artifact metrics, pinned WITH their extraction method ----------------
# Gate 3(b) rule 4 (fail loud, not silently-plausible): a bare "N text chars"
# claim is method-ambiguous and drifts silently. pdfplumber and pymupdf
# legitimately disagree on this PDF (31,367 vs 30,724) because they join page
# text differently, so a recorded count is only meaningful next to the reader
# that produced it. Both are asserted here; a mismatch is a real defect
# (script or assets changed), never a choice of library.
PDF = HERE / "Ch15_BodyFluidsAndCirculation.pdf"
EXPECT_PAGES, EXPECT_IMAGES = 11, 4
EXPECT_CHARS = {"pdfplumber": 31367, "pymupdf": 30724}

artifact_bad = {}
if PDF.exists():
    import pdfplumber
    import pymupdf

    with pdfplumber.open(PDF) as _p:
        got_pages = len(_p.pages)
        got_chars_plumber = len("".join((pg.extract_text() or "") for pg in _p.pages))
        got_images = sum(len(pg.images) for pg in _p.pages)
    _d = pymupdf.open(PDF)
    got_chars_mupdf = len("".join(pg.get_text() for pg in _d))
    got_portrait = all(pg.rect.width < pg.rect.height for pg in _d)
    _d.close()

    for name, got, want in (
        ("pages", got_pages, EXPECT_PAGES),
        ("images", got_images, EXPECT_IMAGES),
        ("chars/pdfplumber", got_chars_plumber, EXPECT_CHARS["pdfplumber"]),
        ("chars/pymupdf", got_chars_mupdf, EXPECT_CHARS["pymupdf"]),
    ):
        if got != want:
            artifact_bad[name] = (want, got)
    if not got_portrait:
        artifact_bad["portrait"] = (True, False)

    print("artifact    : %d pages / %d images / %d chars (pdfplumber) / %d chars (pymupdf)"
          % (got_pages, got_images, got_chars_plumber, got_chars_mupdf))
    print("artifact mismatched: %s" % (artifact_bad or "none"))
else:
    print("artifact    : PDF absent - artifact metrics not checked")

assert not phantom, "phantom figure row(s): %s" % phantom
assert not dupes, "duplicated labels: %s" % dupes
assert len(figs) == 4, "expected 4 figure rows, got %d" % len(figs)
assert not bad, "header claim mismatch: %s" % bad
assert len(openers) == len(headings) - 3 + 1, "opener census arithmetic broken"
assert not artifact_bad, "artifact metric mismatch (want, got): %s" % artifact_bad
print("\nALL CHECKS PASS")
sys.exit(0)
