"""Pass 2 tick support for Ch18: token-coverage audit of every frozen Facts row
against the built PDF's extracted text.

This does NOT tick anything. It ranks rows by how much of their vocabulary is
missing from the PDF text so the low scorers can be read by eye before the tick
is written. Ticking without this step is exactly the "green gate that verified
nothing" failure the SUPREME COMMAND PROMPT warns about.
"""

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

import pymupdf  # noqa: E402
from check_pdf import _norm, STOPWORDS  # noqa: E402

CH = REPO / "notes" / "class 11" / "Ch18_NeuralControlAndCoordination"
PDF = CH / "Ch18_NeuralControlAndCoordination.pdf"
INV = CH / "Ch18_NeuralControlAndCoordination_inventory.md"


def facts_rows(inv_text):
    rows, in_facts = [], False
    for line in inv_text.splitlines():
        low = line.strip().lower()
        if low.startswith("## "):
            in_facts = low.startswith("## facts")
            continue
        if not in_facts or not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5 or not re.match(r"f\d{3}$", cells[0].lower()):
            continue
        rows.append(cells)
    return rows


def main():
    doc = pymupdf.open(PDF)
    hay = _norm("\n".join(p.get_text() for p in doc))
    rows = facts_rows(INV.read_text(encoding="utf-8"))
    print(f"Facts rows parsed: {len(rows)}")
    scored = []
    for rid, section, typ, wording, _ticked in rows:
        toks = [t for t in _norm(wording).split()
                if t not in STOPWORDS and len(t) > 3]
        if not toks:
            toks = _norm(wording).split()
        missing = [t for t in set(toks) if not re.search(r"\b" + re.escape(t) + r"\b", hay)]
        ratio = 1 - len(missing) / max(len(set(toks)), 1)
        scored.append((ratio, rid, section, typ, sorted(missing), wording))
    scored.sort()
    below = [s for s in scored if s[0] < 0.80]
    print(f"rows below 0.80 coverage: {len(below)}\n")
    for ratio, rid, section, typ, missing, wording in below:
        print(f"{rid} [{section}/{typ}] {ratio:.2f} missing={missing}")
        print(f"    {wording[:150]}")
    print(f"\nmean coverage: {sum(s[0] for s in scored)/len(scored):.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
