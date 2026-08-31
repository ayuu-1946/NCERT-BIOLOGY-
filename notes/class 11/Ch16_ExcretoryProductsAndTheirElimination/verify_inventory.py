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

# ---- row-level census, as claimed by the inventory header + census sections
# Added at Gate 1 closure. The freeze shipped a hand-tallied Type census with
# six wrong values (summing to 174 against a 172-row table) and an opener count
# of 13 against 12 real rows; nothing in this file could see either, because
# checks [1]-[5] only ever looked at the source PDF, the assets and the label
# matrix. These expectations close that hole: every count restated in the
# inventory prose is now re-derived from the table and asserted here.
EXP_TOTAL_ROWS = 178
EXP_FACTS_ROWS = 172
EXP_FIRST_ID = 1
# Pass 2 is PARTIAL: only the chapter intro + SS16.1 are written, so exactly the
# rows below are ticked. Asserting the exact ID SET (not just a count) is what
# keeps this a real gate during a partial build - a row ticked outside this set
# means the script claims coverage it does not have.
EXP_TICKED_IDS = (
    [f"F{n:03d}" for n in range(1, 53)]        # title + chapter intro + 16.1
    + [f"F{n:03d}" for n in range(165, 169)]   # captions for Figures 16.1-16.4
    + [f"F{n:03d}" for n in range(173, 177)]   # label rows for Figures 16.1-16.4
)
EXP_TICKED = len(EXP_TICKED_IDS)
EXP_TYPE_COUNTS = {
    "concept": 82,
    "process": 19,
    "heading": 15,
    "number": 13,
    "definition": 12,
    "opener": 12,
    "example": 9,
    "caption": 6,
    "figure-label": 6,
    "disorder": 2,
    "list": 1,
    "question": 1,
}
# Opener IDs named by the opener census, in source order.
EXP_OPENER_IDS = [
    "F002", "F028", "F054", "F076", "F080", "F087",
    "F090", "F095", "F109", "F128", "F140", "F151",
]
EXP_ROW_RE = re.compile(r"^F\d{3}$")

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
    # NOTE: _extract_labels returns a flat list[(fig_id, label)], NOT a dict.
    # An earlier revision of this file called .values() on it, which raised
    # AttributeError and aborted the run *after* printing only ok lines - a
    # crash that reads as a pass if you only skim the tail. Keep this shape
    # assertion so the contract is checked, not assumed.
    parsed = cp._extract_labels(inv)
    check(
        isinstance(parsed, list) and all(isinstance(p, tuple) and len(p) == 2 for p in parsed),
        "check_pdf._extract_labels() returns a flat list of (fig_id, label) pairs",
    )
    check(
        bool(parsed),
        "check_pdf._extract_labels() finds a non-empty matrix (guards the silent-WARN trap)",
    )
    check(
        len(parsed) == EXP_LABEL_TOTAL,
        f"check_pdf parses {EXP_LABEL_TOTAL} labels with no doubling (got {len(parsed)})",
    )
    parsed_figs = sorted({fid for fid, _ in parsed})
    exp_figs = sorted(f"Fig 16.{i}" for i in range(1, EXP_FIGURES + 1))
    check(
        parsed_figs == exp_figs,
        f"check_pdf sees exactly figures {exp_figs} with no phantom rows (got {parsed_figs})",
    )
    for i in range(1, EXP_FIGURES + 1):
        n = len([1 for fid, _ in parsed if fid == f"Fig 16.{i}"])
        check(
            n == EXP_LABELS_PER_FIG[i],
            f"check_pdf parses {EXP_LABELS_PER_FIG[i]} labels for Fig 16.{i} (got {n})",
        )

    print("[5] row census: IDs, types, ticks (guards hand-tallied counts)")
    rows = []
    for line in inv.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) >= 5 and EXP_ROW_RE.match(cells[0]):
            rows.append(cells)

    ids = [r[0] for r in rows]
    check(len(rows) == EXP_TOTAL_ROWS, f"total F-rows == {EXP_TOTAL_ROWS} (got {len(rows)})")
    check(len(set(ids)) == len(ids), f"no duplicate row IDs (got {len(ids) - len(set(ids))} dupes)")
    nums = sorted(int(i[1:]) for i in ids)
    check(
        nums == list(range(EXP_FIRST_ID, EXP_FIRST_ID + EXP_TOTAL_ROWS)),
        f"IDs contiguous F{EXP_FIRST_ID:03d}..F{EXP_FIRST_ID + EXP_TOTAL_ROWS - 1:03d} with no gaps",
    )

    types: dict[str, int] = {}
    for r in rows:
        types[r[2]] = types.get(r[2], 0) + 1
    check(
        types == EXP_TYPE_COUNTS,
        "Type census matches a re-parse of the table"
        + (f" (got {dict(sorted(types.items()))})" if types != EXP_TYPE_COUNTS else ""),
    )
    check(
        sum(EXP_TYPE_COUNTS.values()) == EXP_TOTAL_ROWS,
        f"Type census sums to the stated total {EXP_TOTAL_ROWS} "
        f"(got {sum(EXP_TYPE_COUNTS.values())})",
    )
    check(
        EXP_TOTAL_ROWS - EXP_TYPE_COUNTS["figure-label"] == EXP_FACTS_ROWS,
        f"Facts rows == {EXP_FACTS_ROWS} once the {EXP_TYPE_COUNTS['figure-label']} "
        "figure-label rows are excluded",
    )
    lower = sorted({t for t in types if t != t.lower()})
    check(not lower, "Type column is all-lowercase (normalized vocabulary)"
          + (f" (got {lower})" if lower else ""))

    opener_ids = [r[0] for r in rows if r[2] == "opener"]
    check(
        opener_ids == EXP_OPENER_IDS,
        f"opener rows are exactly the {len(EXP_OPENER_IDS)} IDs named by the opener census "
        f"(got {opener_ids})",
    )
    heading_ids = [r[0] for r in rows if r[2] == "heading"]
    check(
        len(heading_ids) == EXP_TYPE_COUNTS["heading"],
        f"heading rows == {EXP_TYPE_COUNTS['heading']} (got {len(heading_ids)})",
    )

    ticked_ids = [r[0] for r in rows if r[-1].strip().lower() == "x"]
    check(
        len(ticked_ids) == EXP_TICKED,
        f"ticked rows == {EXP_TICKED} (partial build: intro + 16.1) (got {len(ticked_ids)})",
    )
    check(
        ticked_ids == EXP_TICKED_IDS,
        "ticked rows are exactly the intro + 16.1 + Fig 16.1-16.4 ID set"
        + (
            f" (unexpected: {sorted(set(ticked_ids) - set(EXP_TICKED_IDS))}; "
            f"missing: {sorted(set(EXP_TICKED_IDS) - set(ticked_ids))})"
            if ticked_ids != EXP_TICKED_IDS
            else ""
        ),
    )

    # every count restated in prose must equal the parsed value
    for claim, val in (
        ("Opener rows (`Type: opener`) | %d" % len(opener_ids), len(opener_ids)),
        ("Heading rows (`Type: heading`) | %d" % len(heading_ids), len(heading_ids)),
    ):
        check(claim in inv, f"header table restates the parsed count: {claim!r}")

    print("[6] verbatim fidelity of quoted rows against the source PDF")
    # Strings the inventory claims verbatim. Each must appear in BOTH the source
    # PDF text and this inventory, character for character. Added at Gate 1
    # closure after two rows shipped silently corrected to standard English:
    # F042 "along with" (source: "alongwith") and F167 "duct and tubules"
    # (source: "duct and tubule"). Count checks cannot see this defect class.
    flat = re.sub(r"\s+", " ", full)
    flat_inv = re.sub(r"\s+", " ", inv)
    verbatim = [
        "Glomerulus alongwith",                 # F042 - source typo, one word
        "duct and tubule",                      # F167 - Fig 16.3 caption, singular
        "characterestic",                       # F134
        "discorders",                           # F137
        "membrance",                            # F156
        "Columns of Bertini",                   # F036
        "counter current mechanism",             # F104
        "Atrial Natriuretic Factor",            # F124
    ]
    for s in verbatim:
        # curly apostrophes in the PDF are normalized to straight in the inventory
        src = flat.replace("\u2019", "'")
        check(s in src, f"source PDF contains {s!r}")
        check(s in flat_inv, f"inventory quotes {s!r} verbatim")

    # negative assertions: the "corrected" spellings must NOT reappear as quotes
    for bad, why in (
        ("Glomerulus along with", "F042 must not silently correct 'alongwith'"),
        ("duct and tubules", "F167 must not pluralise Fig 16.3's caption"),
    ):
        check(bad not in flat_inv, f"{why} (found {bad!r})" if bad in flat_inv else why)

    print("[7] encoding hygiene")
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
