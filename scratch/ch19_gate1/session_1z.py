#!/usr/bin/env python
"""Ch19 session 1-Z — machine-derived SUMMARY sentence census, BODY-PRESENT /
SUMMARY-UNIQUE candidate screen, and exercise / sub-part census.

Run with the venv interpreter:
  /vercel/share/neetenv/bin/python scratch/ch19_gate1/session_1z.py
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

REPO = Path("/vercel/share/v0-project")
CH = REPO / "notes/class 11/Ch19_ChemicalCoordinationAndIntegration"
INV = CH / "Ch19_ChemicalCoordinationAndIntegration_inventory.md"
SRC = REPO / "Chapter/class 11/Chapter 19 - Chemical Coordination and Integration.pdf"

STOP = set("""a an the and or of in to for on by with as is are was were be been being
that this these those it its their our we you he she they them from at into than then
which who whom whose also not no nor but if so such very can may might will would
have has had do does did done more most other others some any each both all""".split())


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u2013", "-")
    return re.sub(r"\s+", " ", s).strip()


def content_words(s: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", norm(s).lower())
            if w not in STOP and len(w) > 2}


def main() -> int:
    import pdfplumber
    with pdfplumber.open(SRC) as pdf:
        pages = [(p.extract_text() or "") for p in pdf.pages]

    # ---------------------------------------------------------- SUMMARY census
    p11, p12 = pages[10], pages[11]
    s11 = p11.split("SUMMARY", 1)[1]
    s11 = s11.rsplit("Reprint", 1)[0]
    s12 = p12.split("BIOLOGY", 1)[1].rsplit("Reprint", 1)[0]
    summary = norm(s11 + " " + s12)
    # de-hyphenate wraps, then split on sentence-final period
    summary = re.sub(r"(\w)- (\w)", r"\1\2", summary)
    sents = [x.strip() for x in re.split(r"(?<=[a-z0-9)\]])\.\s+(?=[A-Z])", summary) if x.strip()]
    sents = [s if s.endswith(".") else s + "." for s in sents]

    print("=" * 78)
    print(f"A. SUMMARY SENTENCE CENSUS — {len(sents)} sentences (machine-split, pp. 11-12)")
    print("=" * 78)

    inv = INV.read_text(encoding="utf-8")
    body_rows = []
    in_facts = False
    for line in inv.splitlines():
        s = line.strip()
        if s.startswith("## "):
            in_facts = s.startswith("## Facts")
            continue
        if not in_facts or not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 6 or not re.fullmatch(r"F\d{3}", cells[0]):
            continue
        body_rows.append((cells[0], cells[4], cells[3]))

    # body-only corpus = rows whose Src page is NOT 11 or 12 (i.e. not summary rows)
    body_only = [(i, w) for i, src, w in body_rows if src not in {"11", "12"}]
    body_words = set()
    for _, w in body_only:
        body_words |= content_words(w)

    for n, s in enumerate(sents, 1):
        cw = content_words(s)
        novel = sorted(cw - body_words)
        # best-matching body row by content-word overlap
        best_id, best = "-", 0.0
        for i, w in body_only:
            bw = content_words(w)
            if not bw:
                continue
            ov = len(cw & bw) / max(1, len(cw))
            if ov > best:
                best, best_id = ov, i
        verdict = "BODY-PRESENT" if best >= 0.60 and not novel else "REVIEW"
        print(f"\nS{n:02d} [{verdict}] best body row {best_id} overlap {best:.2f}")
        print(f"     {s}")
        if novel:
            print(f"     words absent from ALL non-summary rows: {novel}")

    # ---------------------------------------------------------- exercise census
    print()
    print("=" * 78)
    print("B. EXERCISE CENSUS (p. 13)")
    print("=" * 78)
    ex = pages[12]
    ex = ex.split("EXERCISES", 1)[1].rsplit("Reprint", 1)[0]
    # split into per-question blocks so each question's own labels are counted
    parts = re.split(r"(?m)^\s*(\d)\.\s", ex)
    blocks: list[tuple[str, str]] = []
    for i in range(1, len(parts) - 1, 2):
        blocks.append((parts[i], parts[i + 1]))
    print(f"numbered questions : {len(blocks)}")

    ROMAN = ("i", "ii", "iii", "iv", "v")
    total_sub, total_opt = 0, 0
    for q, body in blocks:
        # "(s)" in "example(s)" is not an enumerator
        labels = [l for l in re.findall(r"\(([a-z]{1,4})\)", body) if l != "s"]
        # Column-II romans exist only in the match-the-following question, which is
        # the only block whose label run restarts with a roman AFTER a letter run
        letters = [l for l in labels if not (l in ROMAN and "Column" in body)]
        opts = [l for l in labels if l in ROMAN and "Column" in body]
        total_sub += len(letters)
        total_opt += len(opts)
        head = norm(body.splitlines()[0])[:58]
        print(f"  Q{q}: {len(letters):>2} sub-part(s)"
              f"{f' + {len(opts)} match-option(s)' if opts else ''}"
              f"  {letters}{opts if opts else ''}   :: {head}")
    print(f"sub-parts to ANSWER (lettered)                : {total_sub}")
    print(f"Column-II match options (roman)               : {total_opt}")
    print(f"all enumerated labels                         : {total_sub + total_opt}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
