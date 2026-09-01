#!/usr/bin/env python
"""Ch19 Gate 1 closure auditor — machine-derives every count in the inventory
header/census, re-parses the figure-label matrix through check_pdf's own
_extract_labels, and verifies each row's verbatim wording + Src page attribution
against the source PDF.

Run with the venv interpreter:
  /vercel/share/neetenv/bin/python scratch/ch19_gate1/gate1_close.py
"""
from __future__ import annotations

import importlib.util
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

REPO = Path("/vercel/share/v0-project")
CH = REPO / "notes/class 11/Ch19_ChemicalCoordinationAndIntegration"
INV = CH / "Ch19_ChemicalCoordinationAndIntegration_inventory.md"
SRC = REPO / "Chapter/class 11/Chapter 19 - Chemical Coordination and Integration.pdf"


# ---------------------------------------------------------------- inventory parse
def parse_facts(text: str) -> list[dict]:
    rows, in_facts = [], False
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("## "):
            in_facts = s.startswith("## Facts")
            continue
        if not in_facts or not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 6 or not re.fullmatch(r"F\d{3}", cells[0]):
            continue
        rows.append(
            dict(id=cells[0], section=cells[1], type=cells[2],
                 wording=cells[3], src=cells[4], ticked=cells[5])
        )
    return rows


# ---------------------------------------------------------------- source text
def page_texts() -> list[str]:
    import pdfplumber
    with pdfplumber.open(SRC) as pdf:
        return [(p.extract_text() or "") for p in pdf.pages]


LIG = {"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl", "\ufb03": "ffi", "\ufb04": "ffl"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    for k, v in LIG.items():
        s = s.replace(k, v)
    s = (s.replace("\u2018", "'").replace("\u2019", "'")
          .replace("\u201c", '"').replace("\u201d", '"')
          .replace("\u2013", "-").replace("\u2014", "-").replace("\u2212", "-"))
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def squash(s: str) -> str:
    """Aggressive form: drop everything but alphanumerics, lowercased.

    Kills the source's hard-wrapped hyphenation and column artefacts so a row's
    wording can be located on a page regardless of line breaks."""
    return re.sub(r"[^a-z0-9]+", "", norm(s).lower())


def toks(s: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", norm(s).lower())


def subseq_at(hay: list[str], needle: list[str], gap_budget: int = 14) -> bool:
    """True if `needle` occurs in `hay` in order, tolerating a bounded number of
    interleaved foreign tokens.

    This is the correct matcher for this source: NCERT's marginal contents
    column is extracted *inside* the body paragraph's token stream, so a
    contiguous substring search reports false 'missing' for perfectly verbatim
    rows (e.g. '...need to be continuously | 19.2 Human | regulated;...').
    A bounded-gap ordered subsequence match tolerates that interleaving while
    still refusing genuinely reordered or absent wording."""
    if not needle:
        return True
    n = len(hay)
    for start in range(n):
        if hay[start] != needle[0]:
            continue
        i, gaps, j = start + 1, 0, 1
        while i < n and j < len(needle):
            if hay[i] == needle[j]:
                j += 1
                gaps = 0
            else:
                gaps += 1
                if gaps > gap_budget:
                    break
            i += 1
        if j == len(needle):
            return True
    return False


def main() -> int:
    text = INV.read_text(encoding="utf-8")
    rows = parse_facts(text)
    fails: list[str] = []

    print("=" * 78)
    print("A. ROW CENSUS (machine-derived)")
    print("=" * 78)
    ids = [r["id"] for r in rows]
    nums = [int(i[1:]) for i in ids]
    print(f"rows parsed                : {len(rows)}")
    print(f"ID range                   : {ids[0]}..{ids[-1]}")
    dupes = [i for i, n in Counter(ids).items() if n > 1]
    print(f"duplicate IDs              : {len(dupes)} {dupes or ''}")
    expected = list(range(1, len(rows) + 1))
    gaps = sorted(set(expected) - set(nums))
    extra = sorted(set(nums) - set(expected))
    print(f"gaps (vs F001..F{len(rows):03d})     : {gaps or 'none'}")
    print(f"out-of-range IDs           : {extra or 'none'}")
    print(f"monotonic                  : {nums == sorted(nums)}")
    unticked = [r["id"] for r in rows if r["ticked"] != "x"]
    print(f"ticked                     : {len(rows) - len(unticked)} / {len(rows)}")
    if dupes or gaps or extra or nums != sorted(nums):
        fails.append("ID contiguity/monotonicity")

    matrix = [r for r in rows if re.match(r"figure(\s*\([a-z]\))?(/\([a-z]\))?\s*labels",
                                          r["wording"], re.I)]
    content = [r for r in rows if r not in matrix]
    print(f"content Facts              : {len(content)}")
    print(f"figure-label matrix rows   : {len(matrix)}  ({', '.join(r['id'] for r in matrix)})")

    print()
    print("=" * 78)
    print("B. TYPE CENSUS (machine-derived)")
    print("=" * 78)
    tc = Counter(r["type"] for r in rows)
    for t, n in sorted(tc.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  {t:<12} {n:>4}")
    print(f"  {'TOTAL':<12} {sum(tc.values()):>4}")
    bad_case = [t for t in tc if t != t.lower()]
    print(f"non-lowercase Type values  : {bad_case or 'none'}")
    if bad_case:
        fails.append("Type column casing")

    print()
    print("HEADING rows:")
    heads = [r for r in rows if r["type"] == "heading"]
    numbered = [r for r in heads if re.match(r"^\d+\.\d", r["wording"])]
    unnumbered = [r for r in heads if r not in numbered]
    print(f"  total {len(heads)} = {len(numbered)} numbered + {len(unnumbered)} unnumbered")
    print(f"  numbered   : {', '.join(r['id'] for r in numbered)}")
    print(f"  unnumbered : {', '.join(r['id'] + '=' + r['wording'] for r in unnumbered)}")
    print("OPENER rows:")
    ops = [r for r in rows if r["type"] == "opener"]
    print(f"  total {len(ops)}: {', '.join(r['id'] for r in ops)}")

    print()
    print("=" * 78)
    print("C. _extract_labels RE-PARSE (check_pdf.py's own parser)")
    print("=" * 78)
    spec = importlib.util.spec_from_file_location("check_pdf", REPO / "check_pdf.py")
    cp = importlib.util.module_from_spec(spec)
    sys.modules["check_pdf"] = cp
    spec.loader.exec_module(cp)
    labels = cp._extract_labels(text)
    byfig = Counter(f for f, _ in labels)
    print(f"figures parsed : {len(byfig)}")
    print(f"labels parsed  : {len(labels)}")
    for f, n in byfig.items():
        print(f"   {f:<20} {n:>3}")
    phantom = [f for f in byfig if not re.match(r"Fig 19\.\d", f)]
    print(f"phantom rows   : {phantom or 'none'}")
    seen = Counter(labels)
    doubled = [k for k, v in seen.items() if v > 1]
    print(f"doubled labels : {doubled or 'none'}")
    if phantom or doubled:
        fails.append("_extract_labels parse")

    print()
    print("=" * 78)
    print("D. VERBATIM + Src PAGE ATTRIBUTION vs SOURCE PDF")
    print("=" * 78)
    pages = page_texts()
    ptoks = [toks(p) for p in pages]
    sq = [squash(p) for p in pages]
    print(f"source pages   : {len(pages)}")
    print(f"page char count: {[len(p) for p in pages]}")
    notfound, misattributed = [], []
    for r in content:
        w = r["wording"]
        needle_t = toks(w)
        needle_s = squash(w)
        try:
            want = int(r["src"])
        except ValueError:
            want = None
        hits = [i + 1 for i in range(len(pages))
                if (needle_s and needle_s in sq[i]) or subseq_at(ptoks[i], needle_t)]
        if not hits:
            notfound.append((r["id"], want, w[:90]))
        elif want not in hits:
            misattributed.append((r["id"], want, hits, w[:70]))
    print(f"rows whose wording was NOT found verbatim on ANY page : {len(notfound)}")
    for i, want, w in notfound:
        print(f"   {i} (Src {want}): {w}")
    print(f"rows found, but NOT on their stated Src page          : {len(misattributed)}")
    for i, want, hits, w in misattributed:
        print(f"   {i}: Src says {want}, found on {hits} :: {w}")
    if notfound or misattributed:
        fails.append("verbatim/page attribution")

    print()
    print("=" * 78)
    print("E. HEADER / CENSUS RESTATEMENTS FOUND IN THE FILE")
    print("=" * 78)
    for pat in (r"Rows: \*\*\d+\*\*", r"F001`–`F\d+", r"\| Rows \| \d+ \|",
                r"\| Content Facts \| \d+ \|", r"\| Rows ticked \| [^|]+ \|",
                r"\*\*total\*\* \| \*\*\d+\*\* \|", r"ID range \| [^|]+ \|"):
        for m in re.finditer(pat, text):
            print(f"   {m.group(0)}")

    print()
    print("=" * 78)
    print("VERDICT:", "GREEN" if not fails else "RED — " + "; ".join(fails))
    print("=" * 78)
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
