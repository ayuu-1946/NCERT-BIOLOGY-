#!/usr/bin/env python3
"""
check_pdf.py — automated pre-flight gate for NCERT->NEET replacement PDFs.

This is the machine-checkable half of the SUPREME COMMAND PROMPT (v6) workflow.
It turns the mechanical defects that used to be re-discovered by eye every chapter
(footer strips, illegible badges, colour images, banned glyphs, figure labels that
never made it into running text, an inventory row left unticked) into a single
green/red gate, so the human verification pass can spend its budget on genuine
content drift instead.

It checks the *rendered PDF* plus the two sibling deliverables (the frozen
inventory and the generating script), discovered by the §0.5 naming convention.

Checks (each independently pass/fail, collected into one verdict):
  1. FOOTER/HEADER BAND   — no text drawn inside the top/bottom margin bands
                            (banned footer / running header / page number).  [defect 1]
  2. TINY TEXT / BADGES   — no rendered text glyph below the legibility floor;
                            badge & step-flow digits are real text spans, so a
                            badge that collapsed to ~3.4pt is caught here.     [defects 2,3]
  3. GRAYSCALE IMAGES     — every embedded image is true monochrome
                            (colorspace GRAY, or sampled pixels R==G==B).      [§4.4/§7]
  4. NO PERSON PHOTO      — heuristic: a manifest row that looks like a
                            portrait/photo must NOT be embedded.               [§5 item 3]
  5. BANNED GLYPHS        — no Unicode arrows / sub-super scripts / Greek /
                            emoji in the text stream.                          [§4 tech rules]
  6. FIGURE-LABEL COVERAGE— every in-figure label recorded in the inventory
                            also appears in the PDF running text.              [defects 5,6]
  7. INVENTORY TICKED     — every Facts row in the inventory is ticked.        [§6 step 9]
  8. PAGE GEOMETRY        — pages are A4 portrait.                             [§4]
  9. ORPHANED HEADINGS    — no banner heading is left stranded as the last thing
                            on its page with its section body starting overleaf.
                            Found by eye on Ch11 *after* Gate 3 was declared PASS,
                            so it is now gated instead of re-hunted every chapter.

Usage:
    python3 check_pdf.py "notes/class 12/Ch9_BiotechnologyPrinciplesAndProcesses"
    python3 check_pdf.py --pdf a.pdf --inventory a_inventory.md --script a.py
    python3 check_pdf.py <folder> --json        # machine-readable report
    python3 check_pdf.py <folder> --strict       # WARN counts as failure too

Exit code 0 = clean gate, 1 = at least one FAIL (or WARN under --strict), 2 = usage/setup error.
"""

from __future__ import annotations

import argparse
import difflib
import glob
import json
import os
import re
import sys
import unicodedata

# ---- tolerant imports so a missing lib reports cleanly instead of a traceback ----
try:
    import pymupdf as fitz  # modern import name; avoids the legacy `import fitz` deprecation warning
except Exception:  # pragma: no cover
    try:
        import fitz  # fallback for older pymupdf builds
    except Exception as exc:
        print("SETUP ERROR: pymupdf is required:  pip install --break-system-packages pymupdf")
        print(f"  import error: {exc}")
        sys.exit(2)

try:
    from PIL import Image
    import io
except Exception as exc:  # pragma: no cover
    print("SETUP ERROR: Pillow is required:  pip install --break-system-packages Pillow")
    print(f"  import error: {exc}")
    sys.exit(2)


# =====================================================================================
# Config — thresholds mirror the v6 spec §4 / §0.4.  A4 @ 72pt/inch, margins from §4.
# =====================================================================================

A4_W, A4_H = 595.276, 841.890          # A4 portrait in PDF points
SIDE_MARGIN = 1.5 * 28.3465            # 1.5 cm
TB_MARGIN = 1.4 * 28.3465              # 1.4 cm  (top / bottom band height)

BAND_TOL = 1.5                          # pts a span may poke into the band before it counts
TINY_FAIL_PT = 5.0                      # < this = illegible -> FAIL (badge smudge was ~3.4pt)
TINY_WARN_PT = 6.0                      # [FAIL_PT, this) = review -> WARN; the 6pt badge floor passes
GEOM_TOL = 3.0                          # pts of slack on page size

# label coverage: token-overlap ratio bands
LABEL_COVERED = 0.999                   # exact normalized substring
LABEL_PARTIAL = 0.60                    # >= this ratio of significant tokens present -> WARN
STOPWORDS = {
    "the", "a", "an", "of", "to", "in", "on", "at", "and", "or", "is", "are", "be",
    "by", "for", "as", "with", "that", "this", "these", "those", "it", "its", "into",
    "from", "only", "when", "which", "both", "same", "can", "has", "have", "cut", "cuts",
}

# banned Unicode families (spec §4 ReportLab strict technical rules)
ARROWS = "\u2190\u2191\u2192\u2193\u2194\u2195\u21cc\u21d0\u21d2\u21cb\u27f6\u2b0e\u2b0f"
GREEK = "".join(chr(c) for c in range(0x0391, 0x03CA))  # Alpha..omega block
SUBSUP = "".join(chr(c) for c in range(0x2070, 0x209D))  # super/subscript block


# =====================================================================================
# result plumbing
# =====================================================================================

class Check:
    def __init__(self, name: str):
        self.name = name
        self.status = "PASS"          # PASS | WARN | FAIL | SKIP
        self.detail: list[str] = []

    def fail(self, msg: str):
        self.status = "FAIL"
        self.detail.append(msg)

    def warn(self, msg: str):
        if self.status != "FAIL":
            self.status = "WARN"
        self.detail.append(msg)

    def note(self, msg: str):
        self.detail.append(msg)

    def skip(self, msg: str):
        self.status = "SKIP"
        self.detail.append(msg)

    def to_dict(self):
        return {"check": self.name, "status": self.status, "detail": self.detail}


def _norm(s: str) -> str:
    """lowercase, strip accents, collapse every non-alphanumeric run to one space."""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return s.strip()


# =====================================================================================
# deliverable discovery (§0.5 naming convention)
# =====================================================================================

def discover(args) -> tuple[str, str | None, str | None]:
    if args.pdf:
        return args.pdf, args.inventory, args.script
    folder = args.folder
    if not folder or not os.path.isdir(folder):
        print(f"SETUP ERROR: not a folder: {folder!r}")
        sys.exit(2)
    pdfs = [p for p in glob.glob(os.path.join(folder, "*.pdf"))]
    if not pdfs:
        print(f"SETUP ERROR: no .pdf found in {folder!r}")
        sys.exit(2)
    # prefer the one whose name matches the folder / has a sibling _inventory.md
    pdf = sorted(pdfs, key=lambda p: len(os.path.basename(p)))[0]
    stem = os.path.splitext(pdf)[0]
    inv = f"{stem}_inventory.md"
    inv = inv if os.path.exists(inv) else (glob.glob(os.path.join(folder, "*_inventory.md")) or [None])[0]
    scr = f"{stem}.py"
    scr = scr if os.path.exists(scr) else (glob.glob(os.path.join(folder, "*.py")) or [None])[0]
    return pdf, inv, scr


# =====================================================================================
# per-page text harvesting (spans with size + bbox) — one pass, reused by many checks
# =====================================================================================

def harvest(doc) -> tuple[list[dict], str]:
    """Return (spans, full_text). Each span: {page, text, size, x0, y0, x1, y1}."""
    spans: list[dict] = []
    chunks: list[str] = []
    for pno, page in enumerate(doc, 1):
        chunks.append(page.get_text("text") or "")
        d = page.get_text("dict")
        for block in d.get("blocks", []):
            for line in block.get("lines", []):
                for sp in line.get("spans", []):
                    t = sp.get("text", "")
                    if not t.strip():
                        continue
                    x0, y0, x1, y1 = sp.get("bbox", (0, 0, 0, 0))
                    spans.append({"page": pno, "text": t, "size": round(sp.get("size", 0), 2),
                                  "x0": x0, "y0": y0, "x1": x1, "y1": y1,
                                  "color": sp.get("color", 0)})
    return spans, "\n".join(chunks)


# =====================================================================================
# CHECK 1 — footer / header band
# =====================================================================================

def check_bands(doc, spans) -> Check:
    c = Check("1. Footer/header band (no page numbers / running header)")
    for page in doc:
        ph = page.rect.height
        break
    else:
        ph = A4_H
    hits = []
    for sp in spans:
        ph = A4_H  # all pages A4; geometry check enforces this separately
        in_bottom = sp["y0"] >= (ph - TB_MARGIN + BAND_TOL)
        in_top = sp["y1"] <= (TB_MARGIN - BAND_TOL)
        if in_bottom or in_top:
            where = "bottom" if in_bottom else "top"
            hits.append(f"p{sp['page']} [{where} band] {sp['size']}pt: {sp['text'][:60]!r}")
    if hits:
        c.fail(f"{len(hits)} text span(s) inside the forbidden margin band:")
        for h in hits[:15]:
            c.note("  " + h)
        if len(hits) > 15:
            c.note(f"  ... and {len(hits) - 15} more")
    else:
        c.note("No text in top/bottom margin bands. Content fills the frame only.")
    return c


# =====================================================================================
# CHECK 2 — tiny text / badge & step-digit legibility
# =====================================================================================

def check_tiny(spans) -> Check:
    c = Check("2. Legibility floor (badges / step digits / any micro-text)")
    fails, warns = [], []
    smallest = None
    for sp in spans:
        sz = sp["size"]
        if smallest is None or sz < smallest:
            smallest = sz
        if sz < TINY_FAIL_PT:
            fails.append(f"p{sp['page']} {sz}pt: {sp['text'][:40]!r}")
        elif sz < TINY_WARN_PT:
            warns.append(f"p{sp['page']} {sz}pt: {sp['text'][:40]!r}")
    c.note(f"Smallest rendered text: {smallest}pt (FAIL<{TINY_FAIL_PT}, WARN<{TINY_WARN_PT}).")
    if fails:
        c.fail(f"{len(fails)} span(s) below the {TINY_FAIL_PT}pt legibility floor "
               f"(badge/step-digit smudge or micro-text):")
        for h in fails[:12]:
            c.note("  " + h)
    if warns:
        c.warn(f"{len(warns)} span(s) in the {TINY_FAIL_PT}-{TINY_WARN_PT}pt review band "
               f"(often subscripts; confirm badge digits are not here):")
        for h in warns[:8]:
            c.note("  " + h)
    return c


# =====================================================================================
# CHECK 3 — grayscale-only images  (and collect embedded images for check 4)
# =====================================================================================

def _image_is_gray(doc, xref) -> tuple[bool, str]:
    info = doc.extract_image(xref)
    cs = info.get("colorspace")
    if cs == 1:
        return True, "GRAY"
    # colorspace >1 (RGB/CMYK): still could be neutral if every pixel R==G==B; sample it.
    try:
        im = Image.open(io.BytesIO(info["image"]))
        if im.mode in ("L", "1", "LA"):
            return True, im.mode
        rgb = im.convert("RGB")
        w, h = rgb.size
        step = max(1, (w * h) // 4000)   # sample ~4k pixels
        px = list(rgb.getdata())[::step]
        neutral = all(abs(r - g) <= 4 and abs(g - b) <= 4 for r, g, b in px)
        name = {3: "RGB", 4: "CMYK"}.get(cs, str(cs))
        return neutral, name + ("(neutral)" if neutral else "(colour)")
    except Exception as exc:
        return False, f"unreadable({exc})"


def check_gray(doc) -> tuple[Check, list[tuple[int, int, int, int]]]:
    c = Check("3. Grayscale-only images (no colour channels)")
    seen = []
    total = 0
    for pno in range(doc.page_count):
        for img in doc.get_page_images(pno):
            xref = img[0]
            total += 1
            gray, name = _image_is_gray(doc, xref)
            info = doc.extract_image(xref)
            seen.append((pno + 1, xref, info.get("width", 0), info.get("height", 0)))
            if not gray:
                c.fail(f"p{pno+1} xref {xref}: {name} — carries real colour; re-run §4.4 convert('L').")
    if total == 0:
        c.warn("No embedded images found — a full chapter should embed its NCERT figures.")
    elif c.status == "PASS":
        c.note(f"All {total} embedded image(s) are monochrome.")
    return c, seen


# =====================================================================================
# CHECK 4 — no photograph of a person (heuristic, manifest-driven)
# =====================================================================================

PORTRAIT_HINTS = ("portrait", "photo", "photograph", "headshot", "profile")

def check_no_person(inv_text: str | None, embedded_imgs) -> Check:
    c = Check("4. No person photograph embedded (scientist profile is text-only)")
    if not inv_text:
        c.skip("No inventory file — cannot cross-check the figure manifest.")
        return c
    # find manifest rows that look like a person portrait
    suspects = []
    for line in inv_text.splitlines():
        low = line.lower()
        if line.strip().startswith("|") and any(h in low for h in PORTRAIT_HINTS):
            # pull the asset filename if present
            m = re.search(r"(fig[\w./-]*\.png|assets/[\w./-]+\.png)", line, re.I)
            suspects.append((line.strip(), m.group(1) if m else None))
    if not suspects:
        c.note("No portrait/photo row in the figure manifest.")
        return c
    for row, asset in suspects:
        # Was this asset actually embedded? We can't map xref->filename directly,
        # so we warn loudly and require the human to confirm it is text-only.
        c.warn("Manifest lists a portrait/photo — confirm it is NOT embedded (must be text-only):")
        c.note("  " + row[:120])
        if asset:
            path_exists = os.path.exists(asset) or os.path.exists(os.path.join(os.getcwd(), asset))
            if path_exists:
                c.warn(f"  asset file {asset} exists on disk — it must not be passed to figure().")
    return c


# =====================================================================================
# CHECK 5 — banned Unicode glyphs
# =====================================================================================

def check_glyphs(full_text: str) -> Check:
    c = Check("5. Banned glyphs (Unicode arrows / sub-super / Greek / emoji)")
    families = {
        "arrow": set(ARROWS),
        "sub/superscript": set(SUBSUP) | set("\u00b2\u00b3\u00b9\u00bd\u00bc\u00be"),
        "Greek": set(GREEK),
    }
    found: dict[str, set] = {}
    for ch in full_text:
        code = ord(ch)
        for fam, members in families.items():
            if ch in members:
                found.setdefault(fam, set()).add(ch)
        # emoji / pictographs / dingbats / arrows-supplement
        if (0x1F000 <= code <= 0x1FAFF) or (0x2600 <= code <= 0x27BF) or (0x2B00 <= code <= 0x2BFF):
            found.setdefault("emoji/pictograph", set()).add(ch)
    if found:
        for fam, chars in found.items():
            shown = " ".join(sorted(chars))
            c.fail(f"{fam}: {shown}  (use <sub>/<super> tags, spell out Greek, ASCII arrows)")
    else:
        c.note("No banned Unicode arrows, sub/superscripts, Greek letters, or emoji.")
    return c


# =====================================================================================
# CHECK 6 — figure-label coverage (every in-figure label also in running text)
# =====================================================================================

def _extract_labels(inv_text: str) -> list[tuple[str, str]]:
    """Return [(fig_id, label_text)] from inventory rows whose wording begins
    with 'Figure labels' (or 'Figure (x) labels'). Labels are the quoted strings."""
    out = []
    for line in inv_text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        fig_id = cells[1] if len(cells) > 1 else "?"
        wording = cells[3]
        if re.match(r"figure(\s*\([a-z]\))?\s*labels", wording, re.I):
            quoted = re.findall(r'"([^"]+)"', wording)
            # also handle labels separated by ; without quotes
            if not quoted:
                body = re.sub(r"^figure(\s*\([a-z]\))?\s*labels\s*:?", "", wording, flags=re.I)
                quoted = [p.strip() for p in body.split(";") if p.strip()]
            for lab in quoted:
                out.append((fig_id, lab))
    return out


def _coverage_ratio(label: str, hay_norm: str, hay_tokens: set[str]) -> tuple[float, bool]:
    ln = _norm(label)
    if not ln:
        return 1.0, True
    if ln in hay_norm:
        return 1.0, True
    toks = [t for t in ln.split() if t not in STOPWORDS and len(t) > 1]
    if not toks:
        toks = ln.split()
    if not toks:
        return 1.0, True
    present = 0
    for t in toks:
        if re.search(r"\b" + re.escape(t) + r"\b", hay_norm):
            present += 1
        elif len(t) >= 4 and difflib.get_close_matches(t, hay_tokens, n=1, cutoff=0.84):
            # spelling variant (e.g. NCERT source typo "braker" vs text "breaker")
            present += 1
    return present / len(toks), False


def check_labels(inv_text: str | None, full_text: str) -> Check:
    c = Check("6. Figure-label coverage (labels present in running text)")
    if not inv_text:
        c.skip("No inventory file — cannot audit figure-label coverage.")
        return c
    labels = _extract_labels(inv_text)
    if not labels:
        c.warn("No 'Figure labels:' rows found in inventory — labels may not be catalogued. "
               "v6 §6 requires a per-figure label row.")
        return c
    hay = _norm(full_text)
    hay_tokens = set(hay.split())
    missing, partial, covered = [], [], 0
    for fig_id, lab in labels:
        ratio, exact = _coverage_ratio(lab, hay, hay_tokens)
        if exact or ratio >= LABEL_COVERED:
            covered += 1
        elif ratio >= LABEL_PARTIAL:
            partial.append((fig_id, lab, ratio))
        else:
            missing.append((fig_id, lab, ratio))
    c.note(f"{covered}/{len(labels)} labels fully in text; "
           f"{len(partial)} partial; {len(missing)} missing.")
    for fig_id, lab, r in missing:
        c.fail(f"{fig_id}: label not in running text ({int(r*100)}% tokens): {lab[:70]!r}")
    for fig_id, lab, r in partial:
        c.warn(f"{fig_id}: only {int(r*100)}% of tokens found — confirm by read: {lab[:70]!r}")
    return c


# =====================================================================================
# CHECK 7 — inventory fully ticked
# =====================================================================================

def check_ticked(inv_text: str | None) -> Check:
    c = Check("7. Frozen inventory fully ticked (every fact written)")
    if not inv_text:
        c.skip("No inventory file to check.")
        return c
    unticked = []
    total = 0
    in_facts = False
    for line in inv_text.splitlines():
        low = line.strip().lower()
        if low.startswith("## "):
            in_facts = low.startswith("## facts")
            continue
        if not in_facts or not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or not re.match(r"[a-z]?\d{2,}", cells[0].lower()):
            continue  # header/separator row
        total += 1
        ticked = cells[-1].lower()
        if ticked not in ("x", "[x]", "done", "yes", "\u2713"):
            unticked.append(cells[0])
    if total == 0:
        c.warn("No Facts rows parsed — check the inventory '## Facts' table format.")
    elif unticked:
        c.fail(f"{len(unticked)}/{total} inventory rows are NOT ticked: {', '.join(unticked[:20])}"
               + (" ..." if len(unticked) > 20 else ""))
    else:
        c.note(f"All {total} Facts rows ticked.")
    return c


# =====================================================================================
# CHECK 8 — page geometry (A4 portrait)
# =====================================================================================

def check_geometry(doc) -> Check:
    c = Check("8. Page geometry (A4 portrait)")
    bad = []
    for pno, page in enumerate(doc, 1):
        w, h = page.rect.width, page.rect.height
        if abs(w - A4_W) > GEOM_TOL or abs(h - A4_H) > GEOM_TOL:
            bad.append(f"p{pno}: {w:.0f}x{h:.0f}pt")
    if bad:
        c.fail(f"{len(bad)} page(s) are not A4 portrait: " + "; ".join(bad[:8]))
    else:
        c.note(f"All {doc.page_count} pages are A4 portrait ({A4_W:.0f}x{A4_H:.0f}pt).")
    return c


# =====================================================================================
# CHECK 9 — orphaned heading (a banner heading is the last thing on its page)
# =====================================================================================

# Banner headings are white bold text on a dark/mid-grey banner; body text, captions
# and table cells are all INK/black. White is therefore a reliable, style-independent
# marker for "drawn on a filled badge or banner". Two things are white: banner
# headings, and process_flow() step digits. A step digit always has its step text
# sitting to the RIGHT on the same visual line, whereas a banner heading's row spans
# the frame and has nothing beside it - that is what _is_banner() below separates.
WHITE = 0xFFFFFF


def _is_banner(sp: dict, page_spans: list[dict]) -> bool:
    """True for a banner-heading span, False for a process_flow step-badge digit."""
    for other in page_spans:
        if other is sp or other.get("color") == WHITE:
            continue
        # vertically overlapping (same visual line) and starting to the right
        if other["x0"] >= sp["x1"] - 0.5 and other["y0"] < sp["y1"] and other["y1"] > sp["y0"]:
            return False
    return True


def check_orphan_headings(doc, spans) -> Check:
    """A heading must be followed by content on the SAME page.

    This is the "orphaned heading" layout bug §6 Pass 3(a) lists but nothing
    enforced: a heading that lands near a page break is left stranded at the foot
    of the page while its own section text starts overleaf. It was rediscovered by
    eye on Ch11 (Organisms and Populations) *after* a Pass 3(a) record had claimed
    every page inspected and Gate 3 had been declared PASS - exactly the "human
    pass wasted its budget on a mechanical defect" failure v6 exists to prevent.
    `neet_template.heading()` now guards against it structurally with a
    CondPageBreak; this check is the gate that keeps it from silently regressing.
    """
    c = Check("9. Orphaned headings (heading not left stranded at page foot)")
    by_page: dict[int, list[dict]] = {}
    for sp in spans:
        by_page.setdefault(sp["page"], []).append(sp)

    bad = []
    heading_total = 0
    for pno in sorted(by_page):
        page_spans = by_page[pno]
        headings = [s for s in page_spans
                    if s.get("color") == WHITE and _is_banner(s, page_spans)]
        heading_total += len({round(s["y1"], 1) for s in headings})
        if not headings:
            continue
        # the lowest heading baseline on this page
        low_head = max(s["y1"] for s in headings)
        # is there any non-heading (body) text below it on the same page?
        below = [s for s in page_spans
                 if s.get("color") != WHITE and s["y0"] > low_head - 1.0]
        if not below:
            label = " / ".join(dict.fromkeys(
                s["text"].strip() for s in headings if abs(s["y1"] - low_head) < 6.0))
            bad.append(f"p{pno}: {label!r} is the last content on the page")

    if bad:
        c.fail(f"{len(bad)} orphaned heading(s) - the section body starts on the next page: "
               + "; ".join(bad[:8]))
        c.note("Fix: heading() reserves ORPHAN_GUARD_PT via CondPageBreak; if this fires, "
               "that guard was bypassed or is too small for the following flowable.")
    else:
        c.note(f"No orphaned headings; {heading_total} banner heading(s) all followed by "
               f"content on their own page.")
    return c


# =====================================================================================
# main
# =====================================================================================

def main() -> int:
    ap = argparse.ArgumentParser(description="Automated pre-flight gate for NEET replacement PDFs.")
    ap.add_argument("folder", nargs="?", help="chapter folder (auto-discovers pdf/inventory/script)")
    ap.add_argument("--pdf", help="explicit PDF path")
    ap.add_argument("--inventory", help="explicit inventory .md path")
    ap.add_argument("--script", help="explicit generator .py path (reserved for future static checks)")
    ap.add_argument("--json", action="store_true", help="emit JSON report")
    ap.add_argument("--strict", action="store_true", help="treat WARN as failure")
    args = ap.parse_args()

    if not args.folder and not args.pdf:
        ap.print_help()
        return 2

    pdf_path, inv_path, scr_path = discover(args)
    if not os.path.exists(pdf_path):
        print(f"SETUP ERROR: PDF not found: {pdf_path}")
        return 2

    inv_text = None
    if inv_path and os.path.exists(inv_path):
        with open(inv_path, encoding="utf-8") as f:
            inv_text = f.read()

    doc = fitz.open(pdf_path)
    spans, full_text = harvest(doc)

    checks: list[Check] = []
    checks.append(check_geometry(doc))
    checks.append(check_bands(doc, spans))
    checks.append(check_tiny(spans))
    gray_check, embedded = check_gray(doc)
    checks.append(gray_check)
    checks.append(check_no_person(inv_text, embedded))
    checks.append(check_glyphs(full_text))
    checks.append(check_labels(inv_text, full_text))
    checks.append(check_ticked(inv_text))
    checks.append(check_orphan_headings(doc, spans))

    # order the report by check number embedded in the name
    checks.sort(key=lambda c: c.name)

    n_fail = sum(1 for c in checks if c.status == "FAIL")
    n_warn = sum(1 for c in checks if c.status == "WARN")
    verdict = "FAIL" if n_fail else ("WARN" if n_warn else "PASS")

    if args.json:
        print(json.dumps({
            "pdf": pdf_path, "inventory": inv_path, "script": scr_path,
            "pages": doc.page_count, "verdict": verdict,
            "fail": n_fail, "warn": n_warn,
            "checks": [c.to_dict() for c in checks],
        }, indent=2))
    else:
        print("=" * 78)
        print(f"check_pdf.py — {os.path.basename(pdf_path)}  ({doc.page_count} pages)")
        print(f"inventory: {os.path.basename(inv_path) if inv_path else '(none)'}")
        print("=" * 78)
        icon = {"PASS": "PASS", "WARN": "WARN", "FAIL": "FAIL", "SKIP": "SKIP"}
        for c in checks:
            print(f"\n[{icon[c.status]}] {c.name}")
            for d in c.detail:
                print(f"       {d}")
        print("\n" + "=" * 78)
        print(f"VERDICT: {verdict}   ({n_fail} fail, {n_warn} warn)")
        print("=" * 78)

    doc.close()
    if n_fail or (args.strict and n_warn):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
