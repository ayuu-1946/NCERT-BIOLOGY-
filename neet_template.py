"""
NCERT Biology -> NEET replacement notes
Shared canon module — SUPREME COMMAND PROMPT.md v6 §0.6

Every chapter script imports its page geometry, colour palette, paragraph
styles, and layout helpers from HERE instead of re-declaring them. This is
what makes drift across chapters (defects 1-3: inconsistent margins, fonts,
colours) structurally impossible: a chapter either imports the shared canon
or it fails to import at all.

FONT RULE (all chapters, no exceptions): every piece of type in every PDF is
Times New Roman. ReportLab's base-14 PDF fonts "Times-Roman" / "Times-Bold" /
"Times-Italic" / "Times-BoldItalic" ARE the Times New Roman metrics — they are
guaranteed to be present in every PDF viewer with no embedding required. No
chapter script may reference any other fontName. Use FONT_REGULAR / FONT_BOLD
/ FONT_ITALIC / FONT_BOLD_ITALIC below rather than hardcoding the strings, so a
future font change happens in exactly one place.

Usage in a chapter script:

    from neet_template import (
        PAGE_SIZE, MARGIN, TOP_MARGIN, BOTTOM_MARGIN, FRAME_WIDTH,
        DARK_GREY, MED_GREY, SOFT_GREY, ROW_ALT, NOTE_BG, GRID_LINE, INK,
        STYLES, TABLE_PADDING,
        heading, keyterm, process_flow, note, memory_aid, data_table, figure,
        motif_dna, build_pdf,
    )

    HERE = os.path.dirname(os.path.abspath(__file__))
    ASSETS = os.path.join(HERE, "assets")
    OUT_PDF = os.path.join(HERE, "ChN_Whatever.pdf")

    story = []
    ... story.append(heading("9.1", "Some Heading", level=1)) ...
    ... story.append(figure("fig1.png", "Caption text", ASSETS)) ...

    if __name__ == "__main__":
        sys.exit(build_pdf(OUT_PDF, story,
                            title="Class 12 Chapter N - ... (NEET notes)",
                            subject="NEET Biology"))

Nothing chapter-specific lives in this module: no content, no NCERT section
numbers, no per-chapter constants. Only the frozen design system (§4) and the
sanctioned helper functions that operationalise it.
"""

import math
import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                Image, KeepTogether, HRFlowable, CondPageBreak)
from reportlab.graphics.shapes import Drawing, Circle, Rect, Polygon, String, Line
from reportlab.pdfbase.pdfmetrics import stringWidth

# --------------------------------------------------------------------------------------
# 0. FONT CANON — Times New Roman everywhere, no exceptions
# --------------------------------------------------------------------------------------

FONT_REGULAR = "Times-Roman"
FONT_BOLD = "Times-Bold"
FONT_ITALIC = "Times-Italic"
FONT_BOLD_ITALIC = "Times-BoldItalic"

# --------------------------------------------------------------------------------------
# 1. CANONICAL STYLE BLOCK (§4)
# --------------------------------------------------------------------------------------

PAGE_SIZE = A4
MARGIN = 1.5 * cm
TOP_MARGIN = 1.4 * cm
BOTTOM_MARGIN = 1.4 * cm
FRAME_WIDTH = PAGE_SIZE[0] - 2 * MARGIN

DARK_GREY = HexColor("#2C2C2C")
MED_GREY = HexColor("#4A4A4A")
SOFT_GREY = HexColor("#6B6B6B")
ROW_ALT = HexColor("#F0F0F0")
NOTE_BG = HexColor("#E8E8E8")
GRID_LINE = HexColor("#AAAAAA")
INK = HexColor("#1A1A1A")

STYLES = {
    "Title": ParagraphStyle("Title", fontName=FONT_BOLD, fontSize=20, alignment=TA_CENTER,
                            leading=23, spaceAfter=2),
    "H1": ParagraphStyle("H1", fontName=FONT_BOLD, fontSize=10.5, textColor=white,
                         backColor=DARK_GREY, borderPadding=3, spaceAfter=6, leading=13),
    "H2": ParagraphStyle("H2", fontName=FONT_BOLD, fontSize=9.5, textColor=white,
                         backColor=MED_GREY, borderPadding=2, spaceAfter=5, leading=12),
    "H3": ParagraphStyle("H3", fontName=FONT_BOLD, fontSize=9, textColor=white,
                         backColor=SOFT_GREY, borderPadding=2, spaceAfter=4, leading=11.5),
    "Body": ParagraphStyle("Body", fontName=FONT_REGULAR, fontSize=10.8, leading=14.2,
                           spaceAfter=3),
    "Bullet1": ParagraphStyle("Bullet1", fontName=FONT_REGULAR, fontSize=10.8,
                              leftIndent=12, firstLineIndent=-8, leading=14.2, spaceAfter=1.5),
    "Bullet2": ParagraphStyle("Bullet2", fontName=FONT_REGULAR, fontSize=10.5,
                              leftIndent=22, firstLineIndent=-8, leading=13.8, spaceAfter=1.5),
    "Bullet3": ParagraphStyle("Bullet3", fontName=FONT_REGULAR, fontSize=10.2,
                              leftIndent=32, firstLineIndent=-8, leading=13.5, spaceAfter=1.5),
    "NoteBox": ParagraphStyle("NoteBox", fontName=FONT_ITALIC, fontSize=10.2,
                              borderPadding=6, leading=13.5),
    "Caption": ParagraphStyle("Caption", fontName=FONT_ITALIC, fontSize=9.5,
                              alignment=TA_CENTER, leading=12.5, spaceBefore=3, spaceAfter=8),
    "TableCell": ParagraphStyle("TableCell", fontName=FONT_REGULAR, fontSize=9.5, leading=12),
    "TableHead": ParagraphStyle("TableHead", fontName=FONT_BOLD, fontSize=9.5, leading=12,
                                textColor=white),
}

TABLE_PADDING = dict(top=3, bottom=3, left=4, right=4)


# --------------------------------------------------------------------------------------
# 2. HELPERS — icons/badges (§4.1), process flow (§4.2), boxes (§4.3), figures (§4.4)
# --------------------------------------------------------------------------------------

def _badge_section(label: str, size: float) -> Drawing:
    """Filled badge carrying the NCERT section number in white (§4.1).

    The badge GROWS SIDEWAYS to fit its label instead of shrinking the type.
    A fixed square forced long labels such as "9.2.1" down to ~3.4 pt, which
    printed as an unreadable smudge; §0.4 check 2 requires the badge to be
    legible at actual print size, not merely at screen zoom. The glyph height
    is therefore pinned to a >=6 pt floor and the plate is widened to suit.
    """
    fs = max(size * 0.46, 6.0)
    pad = fs * 0.42
    text_w = stringWidth(label, FONT_BOLD, fs)
    w = max(size, text_w + 2 * pad)
    h = size
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, fillColor=INK, strokeColor=INK, strokeWidth=0))
    # Optical centring: Times cap-height is ~0.66 em, so centre the cap box.
    d.add(String(w / 2, (h - fs * 0.66) / 2, label, fontName=FONT_BOLD,
                 fontSize=fs, fillColor=white, textAnchor="middle"))
    return d


def _icon_definition(size: float = 7.5) -> Drawing:
    """Filled circle — definition / key-term callout (§4.1)."""
    d = Drawing(size, size)
    d.add(Circle(size / 2, size / 2, size / 2, fillColor=INK, strokeColor=INK, strokeWidth=0))
    return d


def _icon_table(size: float = 9) -> Drawing:
    """Open (stroke-only) square — content converted to a table (§4.1)."""
    d = Drawing(size, size)
    d.add(Rect(0.5, 0.5, size - 1, size - 1, fillColor=None, strokeColor=INK, strokeWidth=0.9))
    return d


def _icon_star(size: float = 11) -> Drawing:
    """5-point outline star — MEMORY AID (§4.1)."""
    pts = []
    cx = cy = size / 2
    outer, inner = size / 2 - 0.4, (size / 2 - 0.4) * 0.42
    for i in range(10):
        ang = math.pi / 2 + i * math.pi / 5
        r = outer if i % 2 == 0 else inner
        pts += [cx + r * math.cos(ang), cy + r * math.sin(ang)]
    d = Drawing(size, size)
    d.add(Polygon(points=pts, fillColor=None, strokeColor=INK, strokeWidth=0.9))
    return d


def _icon_note(size: float = 11) -> Drawing:
    """Outline circle with a drawn '!' — NOTE (§4.1). Built from Rect + Circle, never a glyph."""
    d = Drawing(size, size)
    d.add(Circle(size / 2, size / 2, size / 2 - 0.5, fillColor=None, strokeColor=INK,
                 strokeWidth=0.9))
    d.add(Rect(size / 2 - 0.55, size * 0.36, 1.1, size * 0.33, fillColor=INK, strokeColor=INK,
              strokeWidth=0))
    d.add(Circle(size / 2, size * 0.27, 0.85, fillColor=INK, strokeColor=INK, strokeWidth=0))
    return d


def motif_dna(size: float = 42) -> Drawing:
    """Title-block decorative motif (§4 title block): a simple DNA double-helix outline.
    Decorative only — carries no facts and is deliberately a single line-art shape so it
    cannot be mistaken for a reproduced NCERT diagram."""
    d = Drawing(size, size)
    steps = 26
    left, right = [], []
    for i in range(steps + 1):
        t = i / steps
        y = t * size
        phase = t * 2 * math.pi * 1.6
        left.append((size / 2 + math.sin(phase) * size * 0.26, y))
        right.append((size / 2 - math.sin(phase) * size * 0.26, y))
    for strand in (left, right):
        flat = []
        for x, y in strand:
            flat += [x, y]
        d.add(Polygon(points=flat, fillColor=None, strokeColor=INK, strokeWidth=0.9))
    for i in range(2, steps - 1, 4):
        d.add(Line(left[i][0], left[i][1], right[i][0], right[i][1],
                   strokeColor=INK, strokeWidth=0.7))
    return d


# Vertical space a heading must have below it, or it is pushed to the next page.
# A banner is ~17pt tall; ORPHAN_GUARD_PT reserves the banner plus two lines of
# Body (10.8pt / 15.2pt leading) so a heading can never be the last thing on a
# page with its own section text starting on the next one. See heading() below.
ORPHAN_GUARD_PT = 52


def heading(number: str, text: str, level: int, has_table: bool = False):
    """Banner heading with its section-number badge (§4.1 + Heading structure).
    `number` is the NCERT section number, kept visible for traceability (§3).

    Returns a KeepTogether([CondPageBreak(ORPHAN_GUARD_PT), banner]) rather than a
    bare Table: a bare banner has nothing binding it to the text beneath it, so a
    heading landing near a page break is left stranded at the foot of the page
    while its section body starts overleaf. That is the "orphaned heading" layout
    bug §6 Pass 3(a) exists to catch, and it is a mechanical defect, so it belongs
    in the frozen template (fixed once for every chapter) and in check_pdf.py's
    automated gate (check 9) - not in a per-chapter workaround.
    """
    size = {1: 13.5, 2: 11.5, 3: 10.0}[level]
    cells = [_badge_section(number, size), Paragraph(text, STYLES[f"H{level}"])]
    widths = [1.02 * cm, None]
    if has_table:
        cells.append(_icon_table())
        widths = [1.02 * cm, FRAME_WIDTH - 1.02 * cm - 0.55 * cm, 0.55 * cm]
    t = Table([cells], colWidths=widths)
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (0, -1), 5),
        ("RIGHTPADDING", (1, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    t.hAlign = "LEFT"
    return KeepTogether([CondPageBreak(ORPHAN_GUARD_PT), t])


def keyterm(text: str):
    """A bullet marked with the filled-circle definition icon (§4.1).
    Eligibility: the term also appears in the chapter summary or in an exercise question."""
    t = Table([[_icon_definition(), Paragraph(text, STYLES["Body"])]],
              colWidths=[0.5 * cm, FRAME_WIDTH - 0.5 * cm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (0, -1), "TOP"),
        ("VALIGN", (1, 0), (1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (0, -1), 4),
        ("TOPPADDING", (0, 0), (0, -1), 4),
        ("TOPPADDING", (1, 0), (1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    t.hAlign = "LEFT"
    return t


def _step_badge(n: int, size: float = 16) -> Drawing:
    """Filled apex-up triangle badge with the white step number (§4.2).

    The digit must sit LOW, in the wide part of the triangle: the shape tapers
    towards the apex, so type placed too high is pinched by the sloping sides.
    The previous 14 pt plate rendered its number at ~6.2 pt and read as a black
    blob on paper, so the plate and its digit are both scaled up here.
    """
    label = str(n)
    fs = max(size * 0.5, 7.5) if len(label) == 1 else max(size * 0.38, 6.5)
    d = Drawing(size, size)
    d.add(Polygon(points=[0, 0, size, 0, size / 2, size],
                  fillColor=INK, strokeColor=INK, strokeWidth=0))
    d.add(String(size / 2, size * 0.12, label, fontName=FONT_BOLD,
                 fontSize=fs, fillColor=white, textAnchor="middle"))
    return d


def process_flow(steps, cyclic: bool = False) -> Table:
    """One reusable flow block (§4.2). steps = plain-text step strings (inline tags OK)."""
    rows = []
    if cyclic:
        loop = Drawing(14, 10)
        loop.add(Polygon(points=[2, 0, 12, 0, 7, 9],
                         fillColor=INK, strokeColor=INK, strokeWidth=0))
        rows.append([loop, Paragraph("<i>(cycle - last step feeds back to step 1)</i>",
                                     STYLES["Caption"])])
    for i, s in enumerate(steps, 1):
        rows.append([_step_badge(i), Paragraph(s, STYLES["Bullet1"])])
    t = Table(rows, colWidths=[0.7 * cm, FRAME_WIDTH - 0.7 * cm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEAFTER", (0, 0), (0, -1), 0.75, GRID_LINE),
        ("LEFTPADDING", (0, 0), (0, -1), 0),
        ("RIGHTPADDING", (0, 0), (0, -1), 4),
        ("LEFTPADDING", (1, 0), (1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    t.hAlign = "LEFT"
    return t


def _box(text: str, kind: str) -> Table:
    """NOTE / MEMORY AID box (§4.3). Meaning is carried by label + icon + border style,
    with NOTE_BG fill as decoration only so it survives photocopying."""
    icon = _icon_note() if kind == "NOTE" else _icon_star()
    label = "[NOTE]" if kind == "NOTE" else "[MEMORY AID - not in NCERT]"
    inner = Table([[icon, Paragraph(f"<b>{label}</b> {text}", STYLES["NoteBox"])]],
                  colWidths=[0.55 * cm, FRAME_WIDTH - 0.55 * cm - 0.5 * cm])
    inner.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (0, -1), 4),
        ("TOPPADDING", (0, 0), (0, -1), 1),
        ("TOPPADDING", (1, 0), (1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    outer = Table([[inner]], colWidths=[FRAME_WIDTH])
    style = [
        ("BACKGROUND", (0, 0), (-1, -1), NOTE_BG),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]
    if kind == "NOTE":
        # solid double-rule border: two parallel 0.5pt lines ~1.5pt apart
        style += [("BOX", (0, 0), (-1, -1), 0.5, GRID_LINE),
                  ("LINEBELOW", (0, 0), (-1, -1), 0.5, GRID_LINE),
                  ("LINEABOVE", (0, 0), (-1, -1), 0.5, GRID_LINE)]
    else:
        style += [("BOX", (0, 0), (-1, -1), 0.75, GRID_LINE, None, (3, 2))]
    outer.setStyle(TableStyle(style))
    outer.hAlign = "LEFT"
    return outer


def note(text: str) -> Table:
    return _box(text, "NOTE")


def memory_aid(text: str) -> Table:
    return _box(text, "MEMORY AID")


def data_table(rows, col_widths=None, font_size=9.5):
    """Standard table (§4 Table rules): DARK_GREY header row with white bold text,
    ROW_ALT alternating rows, 0.4pt gridlines, a 0.25pt rule under every row,
    repeatRows=1 so a data row never appears without its header."""
    body = [[Paragraph(c, STYLES["TableHead"]) for c in rows[0]]]
    for r in rows[1:]:
        body.append([Paragraph(c, STYLES["TableCell"]) for c in r])
    if col_widths:
        total = sum(col_widths)
        col_widths = [w / total * FRAME_WIDTH for w in col_widths]
    t = Table(body, colWidths=col_widths, repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), DARK_GREY),
        ("GRID", (0, 0), (-1, -1), 0.4, GRID_LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), TABLE_PADDING["top"]),
        ("BOTTOMPADDING", (0, 0), (-1, -1), TABLE_PADDING["bottom"]),
        ("LEFTPADDING", (0, 0), (-1, -1), TABLE_PADDING["left"]),
        ("RIGHTPADDING", (0, 0), (-1, -1), TABLE_PADDING["right"]),
    ]
    for i in range(1, len(body)):
        if i % 2 == 0:
            style.append(("BACKGROUND", (0, i), (-1, i), ROW_ALT))
        style.append(("LINEBELOW", (0, i), (-1, i), 0.25, GRID_LINE))
    t.setStyle(TableStyle(style))
    t.hAlign = "LEFT"
    return t


def figure(asset_name: str, caption_text: str, assets_dir: str, max_width_cm: float = 15.9):
    """Embed an extracted NCERT figure with its caption (§4.4).

    `assets_dir` is the calling chapter's own assets/ folder (each chapter keeps
    its extracted figures alongside its script), so this module stays chapter-
    agnostic while every chapter still gets identical framing/scaling rules.

    Scales to the text column preserving aspect ratio, never upscaled beyond 300 dpi
    effective resolution, sits inside a thin GRID_LINE box so it reads as part of this
    design system rather than a pasted-in foreign object, and is kept together with its
    caption across page breaks.

    Two loud failures, never silent ones:
      - a missing asset raises FileNotFoundError naming the caption that needed it;
      - an asset that is not true monochrome raises RuntimeError, so a raw or colour
        extraction cannot reach the PDF even if convert_figures_mono.py was skipped.
    """
    path = os.path.join(assets_dir, asset_name)
    if not os.path.exists(path):
        raise FileNotFoundError(f"MISSING FIGURE ASSET: {path} (required by caption: {caption_text})")
    try:
        from PIL import Image as PILImage
        with PILImage.open(path) as im:
            px_w, px_h = im.size
            mode = im.mode
    except Exception as exc:
        raise RuntimeError(f"CANNOT READ FIGURE ASSET {path}: {exc}")
    if mode != "L":
        raise RuntimeError(
            f"FIGURE NOT MONOCHROME: {asset_name} has mode {mode!r}, expected 'L'. "
            f"Run convert_figures_mono.py before building (§4.4 Step 2).")

    max_w = min(max_width_cm * cm, FRAME_WIDTH)
    natural_w = px_w / 300.0 * 2.54 * cm          # width at 300 dpi effective resolution
    width = min(max_w, natural_w)
    height = width * px_h / px_w
    img = Image(path, width=width, height=height)

    framed = Table([[img]], colWidths=[width + 10])
    framed.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.5, GRID_LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    framed.hAlign = "CENTER"
    return KeepTogether([framed, Paragraph(caption_text, STYLES["Caption"])])


def title_block(title_text: str, motif_size: float = 42):
    """Page-1 title row + rule (§4 title block): DNA motif + centred Times-Bold title,
    no separate title page. Returns a list of flowables ready to extend a story list."""
    row = Table(
        [[motif_dna(motif_size), Paragraph(title_text, STYLES["Title"])]],
        colWidths=[motif_size / 28.35 * cm + 0.1 * cm, FRAME_WIDTH - (motif_size / 28.35 * cm + 0.1 * cm)])
    row.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    row.hAlign = "LEFT"
    rule = HRFlowable(width="100%", thickness=1.1, color=DARK_GREY, spaceBefore=4, spaceAfter=8)
    return [row, rule]


# --------------------------------------------------------------------------------------
# 3. BUILD (§4: no header, no footer, no page numbers, no top/bottom rule lines —
# every page carries content only, so no onFirstPage / onLaterPages canvas callback)
# --------------------------------------------------------------------------------------

def build_pdf(out_pdf: str, story: list, title: str,
              author: str = "NCERT replacement notes", subject: str = "NEET Biology") -> int:
    """Build and write the PDF, print the output size, return 0 on success.
    Identical SimpleDocTemplate geometry for every chapter — only out_pdf/story/title vary."""
    doc = SimpleDocTemplate(
        out_pdf, pagesize=PAGE_SIZE,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=TOP_MARGIN, bottomMargin=BOTTOM_MARGIN,
        title=title, author=author, subject=subject,
    )
    doc.build(story)
    size_kb = os.path.getsize(out_pdf) / 1024
    print(f"Built {out_pdf} ({size_kb:.0f} KB)")
    return 0
