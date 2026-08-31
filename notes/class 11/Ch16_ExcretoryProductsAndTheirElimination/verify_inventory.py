#!/usr/bin/env python3
"""Machine-verify every count and claim asserted in Ch16 INVENTORY.md.

Re-parses the source PDF and the inventory itself, then asserts they agree.
Exits non-zero on any drift, so a stale inventory can never look green.

Run:  /vercel/share/neetenv/bin/python verify_inventory.py
"""
from __future__ import annotations

import importlib.util
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent
PDF = REPO / "Chapter" / "class 11" / "Chapter 16 - Excretory Products and their Elimination.pdf"
INVENTORY = HERE / "Ch16_ExcretoryProductsAndTheirElimination_inventory.md"
ASSETS = HERE / "assets"

# ---- expected values, as claimed by INVENTORY.md -------------------------
EXP_PAGES = 12
EXP_FIGURES = 6
EXP_CAPTION_BLOCKS = 6
EXP_CALLOUTS = 7          # 16.5 is called out twice
EXP_HEADINGS = 8          # 16.1 .. 16.8
EXP_EXERCISES = 12
EXP_LABEL_TOTAL = 76
EXP_LABELS_PER_FIG = {1: 12, 2: 9, 3: 11, 4: 4, 5: 16, 6: 24}

FAILURES: list[str] = []
CHECKS = 0


def check(cond: bool, msg: str) -> None:
    global CHECKS
    CHECKS += 1
    if cond:
        print(f"  ok   {msg}")
    else:
        print(f"  FAIL {msg}")
        FAILURES.append(msg)


def main() -> int:
    import pymupdf

    if not PDF.exists():
        print(f"FATAL: source PDF missing: {PDF}")
        return 2
    if not INVENTORY.exists():
        print(f"FATAL: INVENTORY.md missing: {INVENTORY}")
        return 2

    doc = pymupdf.open(PDF)
    pages = [doc[i].get_text() for i in range(doc.page_count)]
    full = "".join(pages)
    doc.close()
    inv = INVENTORY.read_text(encoding="utf-8")

    print("[1] source structure")
    check(len(pages) == EXP_PAGES, f"pdf page count == {EXP_PAGES} (got {len(pages)})")

    caption_starts = re.findall(r"^\s*Figure\.?\s*16\.(\d)", full, re.M)
    check(
        len(caption_starts) == EXP_CAPTION_BLOCKS,
        f"caption blocks == {EXP_CAPTION_BLOCKS} (got {len(caption_starts)})",
    )
    check(
        sorted(set(caption_starts)) == [str(i) for i in range(1, EXP_FIGURES + 1)],
        f"caption numbers are contiguous 1..{EXP_FIGURES} (got {sorted(set(caption_starts))})",
    )

    callouts = re.findall(r"\(Figure\.?\s*16\.\d\)", re.sub(r"\s+", " ", full))
    check(len(callouts) == EXP_CALLOUTS, f"in-text call-outs == {EXP_CALLOUTS} (got {len(callouts)})")

    # body headings are ALLCAPS "16.N TITLE"; the p1 contents panel is title-case
    body = "".join(pages[1:])
    headings = re.findall(r"^\s*16\.(\d)\s+[A-Z][A-Z]", body, re.M)
    check(
        sorted(set(headings)) == [str(i) for i in range(1, EXP_HEADINGS + 1)],
        f"body headings 16.1..16.{EXP_HEADINGS} all present (got {sorted(set(headings))})",
    )

    ex_block = full[full.rfind("EXERCISES"):]
    ex_nums = [int(n) for n in re.findall(r"^\s*(\d{1,2})\.\s", ex_block, re.M)]
    check(
        ex_nums == list(range(1, EXP_EXERCISES + 1)),
        f"exercises numbered 1..{EXP_EXERCISES} contiguously (got {ex_nums})",
    )

    print("[2] assets on disk")
    pngs = sorted(ASSETS.glob("fig_16_*.png"))
    check(len(pngs) == EXP_FIGURES, f"asset count == {EXP_FIGURES} (got {len(pngs)})")
    for i in range(1, EXP_FIGURES + 1):
        p = ASSETS / f"fig_16_{i}.png"
        check(p.exists() and p.stat().st_size > 0, f"assets/fig_16_{i}.png exists and is non-empty")

    print("[3] inventory label matrix")
    # canonical form: Facts-table rows whose Fact column starts 'Figure labels:'
    rows = re.findall(
        r"^\|[^|]*\|\s*Fig\s*16\.(\d)\s*\|[^|]*\|\s*Figure labels:\s*(.+?)\s*\|",
        inv,
        re.M,
    )
    check(
        len(rows) == EXP_FIGURES,
        f"one 'Figure labels:' Facts row per figure (got {len(rows)} of {EXP_FIGURES})",
    )
    seen = {}
    for num, payload in rows:
        n = int(num)
        check(n not in seen, f"Fig 16.{n} label row appears exactly once")
        labels = [x.strip() for x in payload.split(";") if x.strip()]
        seen[n] = labels
        exp = EXP_LABELS_PER_FIG.get(n)
        check(
            exp is not None and len(labels) == exp,
            f"Fig 16.{n} label count == {exp} (got {len(labels)})",
        )
        dupes = sorted({l for l in labels if labels.count(l) > 1})
        check(not dupes, f"Fig 16.{n} has no duplicate labels" + (f" (got {dupes})" if dupes else ""))

    check(
        sorted(seen) == list(range(1, EXP_FIGURES + 1)),
        f"label rows cover figures 1..{EXP_FIGURES} with no phantoms (got {sorted(seen)})",
    )
    total = sum(len(v) for v in seen.values())
    check(total == EXP_LABEL_TOTAL, f"total labels == {EXP_LABEL_TOTAL} (got {total})")

    print("[4] the parser check_pdf.py actually uses")
    spec = importlib.util.spec_from_file_location("cp", REPO / "check_pdf.py")
    cp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cp)
    # _extract_labels returns a flat list[(fig_id, label)], not a dict.
    parsed = cp._extract_labels(inv)
    check(
        bool(parsed),
        "check_pdf._extract_labels() finds a non-empty matrix (guards the silent-WARN trap)",
    )
    check(
        len(parsed) == EXP_LABEL_TOTAL,
        f"check_pdf parses {EXP_LABEL_TOTAL} labels (got {len(parsed)})",
    )
    parsed_figs = sorted({fig for fig, _ in parsed})
    check(
        len(parsed_figs) == EXP_FIGURES,
        f"check_pdf parses {EXP_FIGURES} distinct figure rows, no phantoms (got {parsed_figs})",
    )

    print("[5] encoding hygiene")
    banned = {
        "\u2080", "\u2081", "\u2082", "\u2083", "\u2084", "\u2085",
        "\u2086", "\u2087", "\u2088", "\u2089",
        "\u00b2", "\u00b3", "\u00b9", "\u207a", "\u207b", "\u2074",
    }
    hits = sorted({c for c in inv if c in banned})
    check(
        not hits,
        "no Unicode sub/superscripts in inventory"
        + (f" (got {[unicodedata.name(c, repr(c)) for c in hits]})" if hits else ""),
    )
    check("\ufffd" not in inv, "no U+FFFD replacement chars in inventory")

    print("[6] caption text is source-verbatim in the BUILT pdf")
    # WHY THIS CHECK EXISTS (Gate 3(b), defect D1): check [1] above counts caption
    # BLOCKS and asserts their NUMBERS are contiguous 1..6 - it never looked at a single
    # caption's WORDS. So the chapter shipped Figure 16.3 as "... duct and tubules" while
    # NCERT draws "... duct and tubule" (singular), and 39 green checks plus a full
    # check_pdf.py run never noticed. Frozen row F167 carries the same Pass 1 eye-slip.
    # A caption is a verbatim-transcription obligation, so it gets a verbatim assertion.
    #
    # Method: pull each caption STRUCTURALLY (block-level) out of the built PDF, then
    # require it to appear contiguously in the normalized source text. Block-level
    # extraction is used because a plain "first match of Figure 16.N" regex picks up
    # in-text call-outs and the label NOTEs instead of the caption itself; containment
    # against normalized source text is used because the source's two-column caption
    # wraps into several blocks that cannot be reassembled reliably.
    built_pdf = HERE / "Ch16_ExcretoryProductsAndTheirElimination.pdf"
    if not built_pdf.exists():
        check(False, f"built pdf present for caption verification ({built_pdf.name})")
    else:
        def _norm(t: str) -> str:
            for a, b in (("\u2013", "-"), ("\u2014", "-"), ("\u2019", "'"), ("\u2018", "'")):
                t = t.replace(a, b)
            return re.sub(r"\s+", " ", t).strip()

        src_norm = _norm(full)
        bdoc = pymupdf.open(built_pdf)
        built_caps: dict[int, str] = {}
        for bpage in bdoc:
            for blk in bpage.get_text("blocks"):
                btxt = _norm(blk[4])
                m = re.match(r"^Figure\.?\s*16\.(\d)\s+(.+)$", btxt)
                if m and "labels, verbatim" not in btxt:
                    built_caps.setdefault(int(m.group(1)), m.group(2))
        bdoc.close()

        check(
            sorted(built_caps) == list(range(1, EXP_FIGURES + 1)),
            f"built pdf prints {EXP_FIGURES} figure captions (got {sorted(built_caps)})",
        )
        for n in range(1, EXP_FIGURES + 1):
            cap = built_caps.get(n, "")
            check(
                bool(cap) and cap in src_norm,
                f"Fig 16.{n} caption is source-verbatim"
                + ("" if cap and cap in src_norm else f" (printed {cap!r} is not in the source)"),
            )

    print()
    print("KNOWN FROZEN-ROW DRIFT (documented, deliberately not 'fixed'):")
    print("  F167 records the Fig 16.3 caption as '... duct and tubules'; the source draws")
    print("  '... duct and tubule'. SS7 rule 5 forbids rewording a frozen Facts row, so the")
    print("  row stands as frozen and the correction lives in the inventory's Pass 3(b)")
    print("  findings section. The BUILT pdf prints the source-verbatim caption, which is")
    print("  what check [6] above enforces.")

    print()
    if FAILURES:
        print(f"RESULT: FAIL -- {len(FAILURES)} of {CHECKS} checks failed")
        for f in FAILURES:
            print(f"  - {f}")
        return 1
    print(f"RESULT: PASS -- all {CHECKS} checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
