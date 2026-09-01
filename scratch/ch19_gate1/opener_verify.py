#!/usr/bin/env python
"""Ch19 session 1-O deliverable — machine-verifies the opener sweep.

Two properties, both derived from the source PDF rather than asserted:

  A. CONTENT ORDER. The `## Facts` table's content rows (F001..F211) must be in
     the source's own reading order, so their `Src` page numbers must be
     non-decreasing. A row out of page order means the table is not in Content
     Order (SUPREME COMMAND §5) and Pass 2 would be written from a scrambled
     spine.

  B. EVERY SECTION'S OPENER ROW IS THAT SECTION'S FIRST SENTENCE. For each of
     the 14 numbered sections, every row belonging to it is located in the
     source text stream by position; the row typed `opener` must have the
     smallest position of all that section's prose rows. This is the property
     that makes a dropped or mistyped opener detectable: it is not enough for
     the opening sentence to exist somewhere in the table (session 1-S already
     guarantees that) — it must be the row the table marks `opener`.

Run with the venv interpreter:
  /vercel/share/neetenv/bin/python scratch/ch19_gate1/opener_verify.py
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("gate1_close", HERE / "gate1_close.py")
G = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(G)

NUMBERED = ["19.1", "19.2", "19.2.1", "19.2.2", "19.2.3", "19.2.4", "19.2.5",
            "19.2.6", "19.2.7", "19.2.8", "19.2.9", "19.2.10", "19.3", "19.4"]

# Rows that are furniture rather than prose: they legitimately precede the
# opener in the source (a heading always does) or sit outside the prose stream.
NON_PROSE = {"heading", "caption", "contents"}


def main() -> int:
    rows = G.parse_facts(G.INV.read_text(encoding="utf-8"))
    content = [r for r in rows if int(r["id"][1:]) <= 211]

    print("=" * 78)
    print("A. CONTENT ORDER — Src page monotonicity over the BODY-PROSE rows")
    print("=" * 78)
    print("Two row classes legitimately break page monotonicity and are excluded,")
    print("with the excluded set printed so the exclusion is auditable:")
    print("  * FOLD rows — a numbered section carrying Src p11-p13, i.e. a")
    print("    SUMMARY-UNIQUE fact folded into its body section (1-Z) or an")
    print("    exercise label held verbatim beside the body fact it assumes")
    print("    (Rule 2). Content Order places these next to the body row they")
    print("    belong to, not on their own printed page.")
    print("  * CAPTION rows — a figure caption is placed beside the prose that")
    print("    refers to the figure, which the source itself may print a page")
    print("    earlier or later than the caption.")
    fold, caption, body = [], [], []
    for r in content:
        if r["type"] == "caption":
            caption.append(r)
        elif r["section"].startswith("19.") and r["src"].isdigit() and int(r["src"]) >= 11:
            fold.append(r)
        else:
            body.append(r)
    bad = []
    prev_id, prev_pg = None, 0
    for r in body:
        if not r["src"].isdigit():
            continue
        pg = int(r["src"])
        if pg < prev_pg:
            bad.append(f"{r['id']} (p{pg}) follows {prev_id} (p{prev_pg})")
        prev_id, prev_pg = r["id"], pg
    print()
    print(f"content rows              : {len(content)}")
    print(f"  body-prose rows checked : {len(body)}")
    print(f"  FOLD rows excluded      : {len(fold)}  "
          + ", ".join(f"{r['id']}(p{r['src']})" for r in fold))
    print(f"  caption rows excluded   : {len(caption)}  "
          + ", ".join(f"{r['id']}(p{r['src']})" for r in caption))
    print(f"out-of-order body rows    : {len(bad) or 'none'}")
    for b in bad:
        print("   " + b)

    # ---------------------------------------------------------------- corpus
    # One document-wide stream per corpus. Positions are indices into the
    # squashed (alphanumeric-only) string, so hard-wrapped hyphenation and the
    # marginal contents column cannot shift a sentence's position.
    corpora = [
        G.toks(" ".join(G.page_texts())),
        G.toks(" ".join(G.page_texts_geometric())),
    ]

    def subseq_start(hay: list[str], needle: list[str], gap_budget: int = 14) -> int | None:
        """Start index of the TIGHTEST place `needle` occurs in `hay` in order,
        tolerating a bounded number of interleaved foreign tokens.

        The bounded gap is not a convenience: NCERT prints a marginal contents
        column whose words extract *inside* the body paragraph's token stream,
        and long sentences wrap across a page break, so a contiguous search
        reports 'not found' for wording that is perfectly verbatim. This is the
        same matcher gate1_close.py uses for the verbatim audit, extended to
        return a position so rows can be ordered.

        It returns the SMALLEST-SPAN match, not the earliest one, and that
        distinction is the whole reason this function exists in this form.
        Taking the earliest start mis-ranked F170 ('Ovary is the primary female
        sex organ...') ahead of the real §19.2.10 opener F169: the token
        'Ovary' also occurs one token earlier in the heading '19.2.10 Ovary',
        so the gap budget happily skipped the entire opening sentence and
        matched from the heading. The tightest match cannot be gamed that way —
        the true occurrence has a span of len(needle), any heading-anchored
        match is strictly longer — so an apparent 'opener is not first' finding
        is a real ordering defect rather than matcher slack."""
        if not needle:
            return None
        n, best = len(hay), None
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
                span = i - start
                if best is None or span < best[0]:
                    best = (span, start)
                if span == len(needle):   # exact contiguous run; unbeatable
                    return start
        return None if best is None else best[1]

    def position(wording: str) -> int | None:
        """Earliest token position of `wording` across the two corpora."""
        needle = G.toks(wording)
        if len(needle) < 4:           # too short to locate unambiguously
            return None
        hits = [subseq_start(c, needle) for c in corpora]
        hits = [h for h in hits if h is not None]
        return min(hits) if hits else None

    print()
    print("=" * 78)
    print("B. OPENER IS THE FIRST SENTENCE OF ITS SECTION")
    print("=" * 78)
    print(f"{'section':<9} {'opener':<6} {'rank':>10}  {'located':>9}  verdict")
    failures = 0
    for sec in NUMBERED:
        secrows = [r for r in content if r["section"] == sec]
        openers = [r for r in secrows if r["type"] == "opener"]
        prose = [r for r in secrows if r["type"] not in NON_PROSE]
        located = [(position(r["wording"]), r) for r in prose]
        located = [(p, r) for p, r in located if p is not None]
        located.sort(key=lambda t: t[0])

        if len(openers) != 1:
            print(f"{sec:<9} {'--':<6} {'':>10}  {'':>9}  FAIL: {len(openers)} opener rows")
            failures += 1
            continue
        op = openers[0]
        ranks = [i for i, (_, r) in enumerate(located) if r["id"] == op["id"]]
        if not ranks:
            print(f"{sec:<9} {op['id']:<6} {'':>10}  {len(located):>9}  FAIL: opener not located in source")
            failures += 1
            continue
        rank = ranks[0]
        ok = rank == 0
        failures += 0 if ok else 1
        verdict = "ok — first" if ok else f"FAIL — {located[0][1]['id']} precedes it"
        print(f"{sec:<9} {op['id']:<6} {rank + 1:>4}/{len(located):<5}  {len(located):>9}  {verdict}")

    print()
    print(f"sections checked : {len(NUMBERED)}")
    print(f"opener rows       : {sum(1 for r in content if r['type'] == 'opener')} "
          f"({len(NUMBERED)} section-opener + 5 chapter-opener)")
    print()
    print("=" * 78)
    print("VERDICT:", "GREEN" if not (bad or failures) else "RED")
    print("=" * 78)
    return 0 if not (bad or failures) else 1


if __name__ == "__main__":
    sys.exit(main())
