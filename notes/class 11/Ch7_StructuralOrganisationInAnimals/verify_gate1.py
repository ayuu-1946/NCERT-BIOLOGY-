#!/usr/bin/env python3
"""Machine checks for the frozen Gate 1 inventory (Class 11, Ch. 7).

Run from repository root with the configured environment:
  ./.venv/bin/python 'notes/class 11/Ch7_StructuralOrganisationInAnimals/verify_gate1.py'
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import importlib.util
import re
import sys

from PIL import Image
import pymupdf

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
INV = HERE / "Ch7_StructuralOrganisationInAnimals_inventory.md"
ASSETS = HERE / "assets"
FAIL = []


def check(ok: bool, message: str) -> None:
    print(f"{'PASS' if ok else 'FAIL'}  {message}")
    if not ok:
        FAIL.append(message)


def parse_facts(text: str):
    found = []
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) >= 5 and re.fullmatch(r"F\d{3}", cells[0]):
            found.append(cells[:5])
    return found


def main() -> int:
    text = INV.read_text(encoding="utf-8")
    facts = parse_facts(text)
    ids = [r[0] for r in facts]
    seq = [int(x[1:]) for x in ids]
    types = Counter(r[2] for r in facts)
    allowed_types = {"fact", "caption", "heading", "opener", "summary-unique", "figure-labels"}

    check(len(facts) == 398, f"398 retained Facts rows parsed (got {len(facts)})")
    check(seq == list(range(1, 399)), "F001–F398 contiguous, ordered, no duplicates/gaps")
    check(not (set(types) - allowed_types), f"controlled Type vocabulary only (got {sorted(types)})")
    check(all(t == t.lower() for t in types), "Type spellings are normalized lowercase")
    check(types["heading"] == 15, "15 retained heading rows")
    check(types["opener"] == 13, "13 retained opener rows")
    check(types["caption"] == 17, "17 caption rows")
    check(types["figure-labels"] == 17, "17 figure-label matrix rows")
    check(types["summary-unique"] == 14, "14 retained SUMMARY-UNIQUE facts folded into body rows")
    check(types["fact"] == 322, "322 retained source-prose fact rows")
    fact_texts = [r[3] for r in facts if r[2] == "fact"]
    check(not any("preceding chapters you came across" in s for s in fact_texts) and not any("How do these cells in the body work together?" in s for s in fact_texts), "accepted transition/rhetorical items are absent")
    check(any("The human body is composed of billions of cells" in s for s in fact_texts), "rejected cell-count removal remains in the inventory")
    check(all(not r[4] for r in facts), "0 rows ticked before Pass 2")
    check(f"Rows: {len(facts)}" in text and f"| Facts rows | {len(facts)} |" in text, "syllabus-scope inventory header and machine-parsed row count agree")
    check("removed from the NEET syllabus" in text and "complete for the requested syllabus scope" in text, "syllabus exclusion and scope are documented")

    # Every captured heading and opener wording must be found in the source PDF text.
    doc_source = pymupdf.open(ROOT / "Chapter/class 11/Chapter 07 - Structural Organisation in Animals.pdf")
    source_text = re.sub(r"\s+", " ", " ".join(page.get_text() for page in doc_source))
    quoted_structural = [re.search(r'"(.*)"', r[3]).group(1) for r in facts if r[2] in {"heading", "opener"}]
    normalize = lambda s: re.sub(r"\s+", " ", s).replace("’", "'").replace("–", "-").lower()
    missing_structural = [q for q in quoted_structural if normalize(q) not in normalize(source_text)]
    check(not missing_structural, f"all retained heading/opener wordings found in source (missing: {missing_structural})")

    # Check the source-extracted manifest independently of the figure-label parser.
    manifest_rows = []
    for line in text.splitlines():
        if line.startswith("| Fig 7."):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 6 and cells[2].startswith("`fig_"):
                manifest_rows.append(cells)
    check(len(manifest_rows) == 17, f"17 figure manifest entries (got {len(manifest_rows)})")
    check(all(r[4] == "yes" and r[5] == "yes" and (ASSETS / re.search(r"`([^`]+)`", r[2]).group(1)).exists() for r in manifest_rows), "all manifest assets exist and are marked Mono/Verified yes")

    spec = importlib.util.spec_from_file_location("check_pdf", ROOT / "check_pdf.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    labels = module._extract_labels(text)
    figures = Counter(fig for fig, _ in labels)
    expected_figures = {f"Fig 7.{i}" for i in (*range(1, 9), *range(14, 23))}
    dups = [pair for pair, n in Counter(labels).items() if n > 1]
    check(len(labels) == 143, f"check_pdf._extract_labels parses 143 labels (got {len(labels)})")
    check(set(figures) == expected_figures, "17 expected labelled figure IDs; no phantom IDs")
    check(not dups, "no labels doubled in parser output")

    # Summary census table must reconcile, sentence by sentence.
    summary_rows = [l for l in text.splitlines() if re.match(r"^\| S\d{2} \|", l)]
    sc = Counter("SUMMARY-UNIQUE" if "| SUMMARY-UNIQUE |" in l else "BODY-PRESENT" for l in summary_rows)
    check(len(summary_rows) == 53, f"53 retained summary sentences classified (got {len(summary_rows)})")
    check(sc == Counter({"SUMMARY-UNIQUE": 14, "BODY-PRESENT": 39}), f"retained summary split 14 + 39 = 53 (got {dict(sc)})")
    # Reconcile every listed summary sentence, in order, against the PDF's two
    # summary pages; strip only known running furniture/source-watermark text.
    doc = pymupdf.open(ROOT / "Chapter/class 11/Chapter 07 - Structural Organisation in Animals.pdf")
    source_summary_blocks = []
    for page_index in (16, 17):
        for block in doc[page_index].get_text("blocks"):
            x0, y0, x1, y1, raw = block[:5]
            if page_index == 16 and y0 <= 276:
                continue
            if page_index == 17 and y0 >= 560:
                continue
            line = re.sub(r"\s+", " ", raw).strip()
            if "For more FREE Downloads please visit" in line or line.startswith("Source: NCERT") or line == "STRUCTURAL ORGANISATION IN ANIMALS 121":
                continue
            if line:
                source_summary_blocks.append(line)
    source_summary = " ".join(source_summary_blocks)
    listed_summary = [l.split("|")[2].strip().strip('"') for l in summary_rows]
    words = lambda s: re.findall(r"[a-z0-9]+", s.lower())
    source_words = words(source_summary)
    cursor = 0
    ordered_subset = True
    for sentence in listed_summary:
        target = words(sentence)
        found = next((i for i in range(cursor, len(source_words) - len(target) + 1) if source_words[i:i + len(target)] == target), None)
        if found is None:
            ordered_subset = False
            break
        cursor = found + len(target)
    check(ordered_subset, "all retained summary sentences match source wording/order (in the original summary subsequence)")

    # Every exercise subpart/root item is one dedicated exercise table row.
    ex_rows = [l for l in text.splitlines() if re.match(r"^\| (?:\d+(?:\([ivx]+\)|\([a-g]\))?) \|", l)]
    gaps = sum("GAP —" in l for l in ex_rows)
    covered = sum("COVERED —" in l for l in ex_rows)
    check(len(ex_rows) == 29, f"29 retained exercise subparts classified (got {len(ex_rows)})")
    check((gaps, covered) == (4, 25), f"retained exercise split 4 GAP / 25 COVERED (got {gaps}/{covered})")

    # Re-probe all 22 delivered PNGs; figure manifest uses the 17 principal assets.
    assets = sorted(ASSETS.glob("*.png"))
    bad = []
    for path in assets:
        with Image.open(path) as im:
            if im.mode != "L":
                bad.append((path.name, im.mode))
    check(len(assets) == 22, f"22 delivered PNGs found (17 numbered outputs + 5 panel crops; got {len(assets)})")
    check(not bad, f"all 22 assets single-channel grayscale (non-L: {bad})")

    print(f"\nGate 1 inventory validator: {'ALL PASS' if not FAIL else f'{len(FAIL)} FAILURE(S)'}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
