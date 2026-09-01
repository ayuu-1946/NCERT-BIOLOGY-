#!/usr/bin/env python3
"""Machine-verify every count and claim asserted in the Ch18 Pass 1 frozen inventory.

Re-parses the source PDF, the assets on disk, and the inventory itself, then asserts
they agree. Exits non-zero on any drift, so a stale inventory can never look green.

Run:  /vercel/share/neetenv/bin/python verify_inventory.py
"""
from __future__ import annotations

import importlib.util
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent
PDF = REPO / "Chapter" / "class 11" / "Chapter 18 - Neural Control and Coordination.pdf"
INVENTORY = HERE / "Ch18_NeuralControlAndCoordination_inventory.md"
ASSETS = HERE / "assets"

# ---- expected values, exactly as claimed by the inventory -----------------
EXP_PAGES = 9
EXP_FIGURES = 4
EXP_CAPTION_BLOCKS = 4
EXP_CALLOUTS = 6              # 18.2 and 18.4 are each called out twice
EXP_FIGURE_MENTIONS = 10      # 6 call-outs + 4 caption heads
EXP_NUM_HEADINGS = 4          # 18.1 .. 18.4
EXP_SUB_HEADINGS = ["18.3.1", "18.3.2", "18.4.1", "18.4.2", "18.4.3"]
EXP_EXERCISES = 10
EXP_FACT_ROWS = 131           # F001-F131
EXP_LABEL_ROWS = 4            # F132-F135
EXP_TOTAL_ROWS = 135
EXP_LABEL_TOTAL = 35
EXP_LABELS_PER_FIG = {1: 10, 2: 3, 3: 9, 4: 13}
EXP_TYPES = {
    "concept": 55,
    "definition": 21,
    "process": 20,
    "heading": 12,
    "opener": 10,
    "caption": 4,
    "example": 4,
    "prompt": 3,
    "number": 2,
}
EXP_HEADING_IDS = [
    "F001", "F013", "F019", "F029", "F046", "F072",
    "F089", "F096", "F114", "F118", "F126", "F127",
]
EXP_OPENER_IDS = [
    "F002", "F014", "F020", "F030", "F047", "F073",
    "F090", "F097", "F115", "F119",
]
EXP_SUMMARY_SENTENCES = 18
EXP_SUMMARY_UNIQUE = 4
EXP_BODY_PRESENT = 14
# assets: (w, h) as asserted in the manifest section
EXP_ASSET_SIZES = {1: (1284, 2250), 2: (2201, 1272), 3: (2054, 1498), 4: (2751, 1663)}
# source-verbatim captions (note 'sagital' - the source's spelling, deliberately kept)
EXP_CAPTIONS = {
    1: "Structure of a neuron",
    2: "Diagrammatic representation of impulse conduction through an axon (at points A and B)",
    3: "Diagram showing axon terminal and synapse",
    4: "Diagram showing sagital section of the human brain",
}

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


def _norm(t: str) -> str:
    for a, b in (("\u2013", "-"), ("\u2014", "-"), ("\u2019", "'"), ("\u2018", "'")):
        t = t.replace(a, b)
    return re.sub(r"\s+", " ", t).strip()


def _rows(inv: str) -> list[list[str]]:
    """Every markdown table row of the two ID-bearing tables, as cell lists."""
    out = []
    for line in inv.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) >= 5 and re.fullmatch(r"F\d{3}", cells[0]):
            out.append(cells)
    return out


def main() -> int:
    import pymupdf
    from PIL import Image

    if not PDF.exists():
        print(f"FATAL: source PDF missing: {PDF}")
        return 2
    if not INVENTORY.exists():
        print(f"FATAL: inventory missing: {INVENTORY}")
        return 2

    doc = pymupdf.open(PDF)
    pages = [doc[i].get_text() for i in range(doc.page_count)]
    doc.close()
    full = "".join(pages)
    flat = _norm(full)
    inv = INVENTORY.read_text(encoding="utf-8")
    rows = _rows(inv)

    print("[1] source structure")
    check(len(pages) == EXP_PAGES, f"pdf page count == {EXP_PAGES} (got {len(pages)})")

    caption_starts = re.findall(r"^\s*Figure\.?\s*18\.(\d)\s", full, re.M)
    check(
        len(caption_starts) == EXP_CAPTION_BLOCKS,
        f"caption blocks == {EXP_CAPTION_BLOCKS} (got {len(caption_starts)})",
    )
    check(
        sorted(set(caption_starts)) == [str(i) for i in range(1, EXP_FIGURES + 1)],
        f"caption numbers contiguous 1..{EXP_FIGURES} (got {sorted(set(caption_starts))})",
    )

    callouts = re.findall(r"\(Figure\.?\s*18\.\d", flat)
    check(len(callouts) == EXP_CALLOUTS, f"in-text call-outs == {EXP_CALLOUTS} (got {len(callouts)})")
    mentions = re.findall(r"Figure\.?\s*18\.\d", flat)
    check(
        len(mentions) == EXP_FIGURE_MENTIONS,
        f"total 'Figure 18.N' mentions == {EXP_FIGURE_MENTIONS} (got {len(mentions)})",
    )

    body = "".join(pages[1:])
    heads = re.findall(r"^\s*18\.(\d)\s*\n?\s*[A-Z]", body, re.M)
    check(
        sorted(set(heads)) == [str(i) for i in range(1, EXP_NUM_HEADINGS + 1)],
        f"body headings 18.1..18.{EXP_NUM_HEADINGS} all present (got {sorted(set(heads))})",
    )
    for sub in EXP_SUB_HEADINGS:
        check(sub in flat, f"sub-heading {sub} present in source")

    ex_block = full[full.rfind("EXERCISES"):]
    ex_nums = [int(n) for n in re.findall(r"^\s*(\d{1,2})\.\s", ex_block, re.M)]
    check(
        ex_nums == list(range(1, EXP_EXERCISES + 1)),
        f"exercises numbered 1..{EXP_EXERCISES} contiguously (got {ex_nums})",
    )
    # the documented source defect: exercise 10 is lettered (a),(b),(f)
    q10 = ex_block[ex_block.rfind("10."):]
    letters = re.findall(r"\(([a-f])\)", q10)
    check(
        letters == ["a", "b", "f"],
        f"exercise 10 lettering is the documented (a),(b),(f) skip (got {letters})",
    )

    print("[2] figure census: no unnumbered plate on figure-free pages")
    # figures live on extracted pp. 3-6 (1-indexed). Every other page must contain
    # no 'Figure 18.' caption head, which is what the census claim rests on.
    for i, txt in enumerate(pages, start=1):
        has_cap = bool(re.search(r"^\s*Figure\.?\s*18\.\d\s", txt, re.M))
        if i in (3, 4, 5, 6):
            check(has_cap, f"page {i} carries its numbered figure caption")
        else:
            check(not has_cap, f"page {i} carries no figure caption (figure-free)")

    print("[3] assets on disk")
    pngs = sorted(ASSETS.glob("fig_18_*.png"))
    check(len(pngs) == EXP_FIGURES, f"asset count == {EXP_FIGURES} (got {len(pngs)})")
    for i in range(1, EXP_FIGURES + 1):
        p = ASSETS / f"fig_18_{i}.png"
        if not (p.exists() and p.stat().st_size > 0):
            check(False, f"assets/fig_18_{i}.png exists and is non-empty")
            continue
        with Image.open(p) as im:
            check(im.mode == "L", f"fig_18_{i}.png is monochrome (mode=L, got {im.mode})")
            check(
                im.size == EXP_ASSET_SIZES[i],
                f"fig_18_{i}.png size == {EXP_ASSET_SIZES[i]} (got {im.size})",
            )

    print("[4] inventory row structure and type census")
    ids = [r[0] for r in rows]
    check(
        ids == [f"F{n:03d}" for n in range(1, EXP_TOTAL_ROWS + 1)],
        f"row IDs are contiguous F001..F{EXP_TOTAL_ROWS:03d} with no gap or dupe",
    )
    fact_rows = [r for r in rows if r[2] != "figure-label"]
    label_rows = [r for r in rows if r[2] == "figure-label"]
    check(len(fact_rows) == EXP_FACT_ROWS, f"Facts rows == {EXP_FACT_ROWS} (got {len(fact_rows)})")
    check(len(label_rows) == EXP_LABEL_ROWS, f"label rows == {EXP_LABEL_ROWS} (got {len(label_rows)})")
    check(
        [r[0] for r in label_rows] == [f"F{n:03d}" for n in range(132, 136)],
        "label rows occupy the tail of the ID space (F132-F135)",
    )

    types = Counter(r[2] for r in fact_rows)
    check(dict(types) == EXP_TYPES, f"type census matches the inventory (got {dict(types)})")
    check(
        sum(EXP_TYPES.values()) == EXP_FACT_ROWS,
        "claimed per-type counts sum to the claimed Facts-row total",
    )

    heading_ids = [r[0] for r in fact_rows if r[2] == "heading"]
    check(heading_ids == EXP_HEADING_IDS, f"heading census IDs match (got {heading_ids})")
    opener_ids = [r[0] for r in fact_rows if r[2] == "opener"]
    check(opener_ids == EXP_OPENER_IDS, f"opener census IDs match (got {opener_ids})")

    # every Facts row unticked at Gate 1; every preserved label row ticked
    check(
        all(r[4] == "" for r in fact_rows),
        "every Facts row is unticked at Gate 1 freeze",
    )
    check(
        all(r[4] == "x" for r in label_rows),
        "every preserved 1-F label row keeps its 'x'",
    )

    print("[5] captions are source-verbatim")
    cap_rows = {r[1]: r[3] for r in fact_rows if r[2] == "caption"}
    for i in range(1, EXP_FIGURES + 1):
        row = cap_rows.get(f"Fig 18.{i}", "")
        expect = f"Figure 18.{i} {EXP_CAPTIONS[i]}"
        check(row == expect, f"Fig 18.{i} caption row == {expect!r} (got {row!r})")
        check(
            _norm(EXP_CAPTIONS[i]) in flat,
            f"Fig 18.{i} caption text appears verbatim in the source",
        )
    # the documented divergence: the frozen 1-F manifest keeps the normalised spelling
    check(
        "sagittal section of the human brain" in inv and "sagital section of the human brain" in inv,
        "both spellings present: frozen manifest 'sagittal' + source-verbatim row 'sagital'",
    )

    print("[6] label matrix")
    matrix = {}
    for r in label_rows:
        m = re.fullmatch(r"Fig 18\.(\d)", r[1])
        check(bool(m), f"label row {r[0]} has a well-formed Section cell (got {r[1]!r})")
        if not m:
            continue
        n = int(m.group(1))
        check(n not in matrix, f"Fig 18.{n} label row appears exactly once")
        payload = re.sub(r"^Figure labels:\s*", "", r[3])
        labels = re.findall(r'"([^"]+)"', payload)
        matrix[n] = labels
        check(
            len(labels) == EXP_LABELS_PER_FIG[n],
            f"Fig 18.{n} label count == {EXP_LABELS_PER_FIG[n]} (got {len(labels)})",
        )
        dupes = sorted({l for l in labels if labels.count(l) > 1})
        check(not dupes, f"Fig 18.{n} has no duplicate labels" + (f" (got {dupes})" if dupes else ""))
    check(
        sorted(matrix) == list(range(1, EXP_FIGURES + 1)),
        f"label rows cover figures 1..{EXP_FIGURES} with no phantoms (got {sorted(matrix)})",
    )
    total = sum(len(v) for v in matrix.values())
    check(total == EXP_LABEL_TOTAL, f"total labels == {EXP_LABEL_TOTAL} (got {total})")
    check(
        inv.count("Figure labels:") == EXP_LABEL_ROWS,
        f"the matrix exists in exactly one place ({EXP_LABEL_ROWS} 'Figure labels:' rows, "
        f"got {inv.count('Figure labels:')})",
    )

    print("[7] the parser check_pdf.py actually uses")
    spec = importlib.util.spec_from_file_location("cp", REPO / "check_pdf.py")
    cp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cp)
    parsed = cp._extract_labels(inv)
    check(bool(parsed), "check_pdf._extract_labels() finds a non-empty matrix (guards the silent-WARN trap)")
    check(len(parsed) == EXP_LABEL_TOTAL, f"check_pdf parses {EXP_LABEL_TOTAL} labels (got {len(parsed)})")
    parsed_figs = sorted({fig for fig, _ in parsed})
    check(
        len(parsed_figs) == EXP_FIGURES,
        f"check_pdf parses {EXP_FIGURES} distinct figure rows, no phantoms (got {parsed_figs})",
    )

    print("[8] summary + exercise-gap sweeps")
    sum_tbl = inv[inv.find("## Summary classification"):inv.find("## Exercise-gap terms")]
    sum_rows = [l for l in sum_tbl.splitlines() if re.match(r"^\|\s*\d{1,2}\s*\|", l)]
    check(
        len(sum_rows) == EXP_SUMMARY_SENTENCES,
        f"summary table has {EXP_SUMMARY_SENTENCES} classified sentences (got {len(sum_rows)})",
    )
    uniq = sum(1 for l in sum_rows if "SUMMARY-UNIQUE" in l)
    present = sum(1 for l in sum_rows if "BODY-PRESENT" in l)
    check(uniq == EXP_SUMMARY_UNIQUE, f"SUMMARY-UNIQUE count == {EXP_SUMMARY_UNIQUE} (got {uniq})")
    check(present == EXP_BODY_PRESENT, f"BODY-PRESENT count == {EXP_BODY_PRESENT} (got {present})")
    check(
        uniq + present == EXP_SUMMARY_SENTENCES,
        "every summary sentence is classified exactly one way",
    )
    check(
        all("fold into" in l for l in sum_rows if "SUMMARY-UNIQUE" in l),
        "every SUMMARY-UNIQUE sentence names the section it folds into",
    )
    # every summary sentence quoted in the table must exist in the source
    sum_block = full[full.find("SUMMARY"):full.rfind("EXERCISES")]
    sum_norm = _norm(sum_block)
    for l in sum_rows:
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        sent = _norm(cells[1])
        check(sent in sum_norm, f"summary sentence is source-verbatim: {sent[:60]!r}")

    gap_tbl = inv[inv.find("## Exercise-gap terms"):inv.find("## Figure manifest")]
    gap_rows = [l for l in gap_tbl.splitlines() if l.startswith("|") and "GAP" in l]
    check(len(gap_rows) == 5, f"5 exercise gaps recorded (got {len(gap_rows)})")
    check(
        all(cells := [c for c in gap_rows]) and all(l.strip().strip("|").split("|")[-1].strip() for l in gap_rows),
        "every recorded gap names a destination section",
    )

    print("[9] encoding hygiene")
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

    print("[10] documented source typos are still transcribed verbatim")
    for typo, where in (("passess", "F116"), ("sagital", "F131"), ("Schwan cell", "F132")):
        check(typo in inv, f"{where} preserves the source's {typo!r}")
        if typo != "Schwan cell":  # artwork label, not in the text layer
            check(typo in flat, f"{typo!r} really is what the source prints")
    check("spiral cord" in inv and "spiral cord" in flat, "SUMMARY's 'spiral cord' recorded verbatim")

    print()
    print("GATE 1 SCOPE NOTE: this chapter has no Pass 2 rewrite and no built PDF yet, so")
    print("running-text label coverage and built-PDF caption checks are out of scope here.")
    print("They belong to Gate 2/3 and are enforced by check_pdf.py once the manuscript exists.")

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
