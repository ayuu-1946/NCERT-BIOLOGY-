#!/usr/bin/env python
"""Ch19 session 1-Z — classify every SUMMARY sentence BODY-PRESENT / SUMMARY-UNIQUE.

The classification itself is a judgement, so this script does not pretend to
make it. What it does is remove the two ways the judgement usually goes wrong:

  1. It enumerates the SUMMARY sentences by machine, so no sentence is
     classified that was never read and none is silently skipped. The census
     total is therefore the length of this list, not a hand tally.
  2. For each sentence it reports the best-matching Facts rows by content-word
     overlap, plus which of the sentence's own content words appear in NO Facts
     row at all. A word appearing nowhere in the body is the actual signal for
     SUMMARY-UNIQUE; a high-overlap match with zero unmatched words is the
     signal for BODY-PRESENT. The verdict column is asserted in the inventory
     against this evidence.

Run:  /vercel/share/neetenv/bin/python scratch/ch19_gate1/summary_classify.py
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

import pdfplumber

REPO = Path("/vercel/share/v0-project")
CH = REPO / "notes/class 11/Ch19_ChemicalCoordinationAndIntegration"
INV = CH / "Ch19_ChemicalCoordinationAndIntegration_inventory.md"
SRC = REPO / "Chapter/class 11/Chapter 19 - Chemical Coordination and Integration.pdf"

STOP = set("""a an the and or but of in on to for from with without as at by is are was
were be been being this that these those it its their our your his her they we you i
which who whom whose what when where while also then than so such into onto over under
between among during about very more most other others some any all both each few many
much no not only own same s t can will just should now etc e g eg ie i.e. e.g. up out
""".split())


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = (s.replace("\u2018", "'").replace("\u2019", "'")
          .replace("\u201c", '"').replace("\u201d", '"')
          .replace("\u2013", "-").replace("\u2014", "-"))
    return re.sub(r"\s+", " ", s).strip()


def words(s: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", norm(s).lower())
            if w not in STOP and len(w) > 2}


def parse_facts(text: str) -> list[dict]:
    rows, in_facts = [], False
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("## "):
            in_facts = s.startswith("## Facts")
            continue
        if not in_facts or not s.startswith("|"):
            continue
        c = [x.strip() for x in s.strip("|").split("|")]
        if len(c) < 6 or not re.fullmatch(r"F\d{3}", c[0]):
            continue
        rows.append(dict(id=c[0], section=c[1], type=c[2], wording=c[3], src=c[4]))
    return rows


def summary_sentences() -> list[str]:
    """Extract the SUMMARY block (p.11 'SUMMARY' -> p.12 end) and split to sentences."""
    with pdfplumber.open(SRC) as pdf:
        p11 = pdf.pages[10].extract_text() or ""
        p12 = pdf.pages[11].extract_text() or ""
    # p.11: everything after the 'SUMMARY' heading line
    tail = p11.split("SUMMARY", 1)[1] if "SUMMARY" in p11 else ""
    # drop running heads / reprint lines from both pages
    def clean(block: str) -> str:
        keep = [ln for ln in block.splitlines()
                if not re.match(r"^\s*(Reprint \d|\d+ BIOLOGY|CHEMICAL COORDINATION)", ln)]
        return " ".join(keep)
    block = norm(clean(tail) + " " + clean(p12))
    # the summary ends where EXERCISES would begin (p.13), so p.12 is all summary
    # split on sentence-final period followed by a capital; protect 'e.g.' etc.
    block = block.replace("e.g.,", "<EG>").replace("i.e.,", "<IE>")
    parts = re.split(r"(?<=[.])\s+(?=[A-Z(])", block)
    out = []
    for p in parts:
        p = p.replace("<EG>", "e.g.,").replace("<IE>", "i.e.,").strip()
        if len(p) > 3:
            out.append(p)
    return out


def main() -> int:
    text = INV.read_text(encoding="utf-8")
    rows = parse_facts(text)
    body = [r for r in rows
            if not re.match(r"figure(\s*\([a-z]\))?(/\([a-z]\))?\s*labels", r["wording"], re.I)]
    body_vocab: set[str] = set()
    for r in body:
        body_vocab |= words(r["wording"])

    sents = summary_sentences()
    print(f"SUMMARY sentences extracted: {len(sents)}")
    print(f"body Facts rows            : {len(body)}")
    print(f"body content-word vocab    : {len(body_vocab)}")
    print("=" * 78)

    unique_hits = []
    for n, s in enumerate(sents, 1):
        sw = words(s)
        unmatched = sorted(sw - body_vocab)
        scored = sorted(
            ((len(sw & words(r["wording"])) / max(len(sw), 1), r) for r in body),
            key=lambda t: -t[0])[:3]
        flag = "  <<< CHECK" if unmatched else ""
        print(f"\nS{n:02d} [{len(s)} ch]{flag}")
        print(f"   {s[:190]}")
        print(f"   words with NO body occurrence: {unmatched or 'none'}")
        for sc, r in scored:
            print(f"     {sc:.2f}  {r['id']} [{r['section']}] {r['wording'][:88]}")
        if unmatched:
            unique_hits.append((n, unmatched))

    print()
    print("=" * 78)
    print(f"sentences with at least one word absent from every body row: "
          f"{len(unique_hits)} / {len(sents)}")
    for n, u in unique_hits:
        print(f"   S{n:02d}: {u}")
    print("=" * 78)
    print("A sentence with NO unmatched words cannot be SUMMARY-UNIQUE on")
    print("vocabulary grounds; it may still restate a body fact in new wording,")
    print("which is BODY-PRESENT (a wording variant), not a fold.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
