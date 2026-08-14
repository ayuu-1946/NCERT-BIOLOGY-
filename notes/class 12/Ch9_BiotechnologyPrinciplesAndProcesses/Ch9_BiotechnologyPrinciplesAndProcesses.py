"""
NCERT Biology -> NEET replacement notes
Class 12, Chapter 9 : Biotechnology : Principles and Processes

Source  : Chapter/class 12/Chapter 9 - Biotechnology Principles and Processes.pdf
Built to: SUPREME COMMAND PROMPT.md v5 (full-replacement edition, print-hardened B&W figures)

Run from the repository root:
    python3 "notes/class 12/Ch9_BiotechnologyPrinciplesAndProcesses/Ch9_BiotechnologyPrinciplesAndProcesses.py"

Figures: every asset in assets/ has already been clip-extracted at 300 dpi and pushed
through convert_figures_mono.py (PIL convert("L") + autocontrast). figure() re-asserts
mode == "L" at build time, so a raw or colour asset cannot silently reach the PDF (§4.4).

Structure of this file:
  1. Canonical style block (§4)
  2. The sanctioned helpers: process_flow() (§4.2), figure() (§4.4), boxes/headings (§4.1/§4.3)
  3. One linear sequence of story.append(...) calls in Content Order (§5),
     each block commented with its NCERT section number for fast auditing.
"""

import math
import os
import sys

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                Image, KeepTogether, HRFlowable)
from reportlab.graphics.shapes import Drawing, Circle, Rect, Polygon, String, Line
from reportlab.pdfbase.pdfmetrics import stringWidth

# --------------------------------------------------------------------------------------
# 1. CANONICAL STYLE BLOCK (§4)
# --------------------------------------------------------------------------------------

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch9_BiotechnologyPrinciplesAndProcesses.pdf")

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
    "Title": ParagraphStyle("Title", fontName="Times-Bold", fontSize=20, alignment=TA_CENTER,
                            leading=23, spaceAfter=2),
    "H1": ParagraphStyle("H1", fontName="Times-Bold", fontSize=10.5, textColor=white,
                         backColor=DARK_GREY, borderPadding=3, spaceAfter=6, leading=13),
    "H2": ParagraphStyle("H2", fontName="Times-Bold", fontSize=9.5, textColor=white,
                         backColor=MED_GREY, borderPadding=2, spaceAfter=5, leading=12),
    "H3": ParagraphStyle("H3", fontName="Times-Bold", fontSize=9, textColor=white,
                         backColor=SOFT_GREY, borderPadding=2, spaceAfter=4, leading=11.5),
    "Body": ParagraphStyle("Body", fontName="Times-Roman", fontSize=10.8, leading=14.2,
                           spaceAfter=3),
    "Bullet1": ParagraphStyle("Bullet1", fontName="Times-Roman", fontSize=10.8,
                              leftIndent=12, firstLineIndent=-8, leading=14.2, spaceAfter=1.5),
    "Bullet2": ParagraphStyle("Bullet2", fontName="Times-Roman", fontSize=10.5,
                              leftIndent=22, firstLineIndent=-8, leading=13.8, spaceAfter=1.5),
    "Bullet3": ParagraphStyle("Bullet3", fontName="Times-Roman", fontSize=10.2,
                              leftIndent=32, firstLineIndent=-8, leading=13.5, spaceAfter=1.5),
    "NoteBox": ParagraphStyle("NoteBox", fontName="Times-Italic", fontSize=10.2,
                              borderPadding=6, leading=13.5),
    "Caption": ParagraphStyle("Caption", fontName="Times-Italic", fontSize=9.5,
                              alignment=TA_CENTER, leading=12.5, spaceBefore=3, spaceAfter=8),
    "TableCell": ParagraphStyle("TableCell", fontName="Times-Roman", fontSize=9.5, leading=12),
    "TableHead": ParagraphStyle("TableHead", fontName="Times-Bold", fontSize=9.5, leading=12,
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
    text_w = stringWidth(label, "Times-Bold", fs)
    w = max(size, text_w + 2 * pad)
    h = size
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, fillColor=INK, strokeColor=INK, strokeWidth=0))
    # Optical centring: Times cap-height is ~0.66 em, so centre the cap box.
    d.add(String(w / 2, (h - fs * 0.66) / 2, label, fontName="Times-Bold",
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


def _motif_dna(size: float = 42) -> Drawing:
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


def heading(number: str, text: str, level: int, has_table: bool = False):
    """Banner heading with its section-number badge (§4.1 + Heading structure).
    `number` is the NCERT section number, kept visible for traceability (§3)."""
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
    return t


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
    d.add(String(size / 2, size * 0.12, label, fontName="Times-Bold",
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


def figure(asset_name: str, caption_text: str, max_width_cm: float = 15.9):
    """Embed an extracted NCERT figure with its caption (§4.4).

    Scales to the text column preserving aspect ratio, never upscaled beyond 300 dpi
    effective resolution, sits inside a thin GRID_LINE box so it reads as part of this
    design system rather than a pasted-in foreign object, and is kept together with its
    caption across page breaks.

    Two loud failures, never silent ones:
      - a missing asset raises FileNotFoundError naming the caption that needed it;
      - an asset that is not true monochrome raises RuntimeError, so a raw or colour
        extraction cannot reach the PDF even if convert_figures_mono.py was skipped.
    """
    path = os.path.join(ASSETS, asset_name)
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


# --------------------------------------------------------------------------------------
# 3. STORY — Content Order (§5)
# --------------------------------------------------------------------------------------

story = []

# ---- Title block (page 1, no separate title page) ----
_title_row = Table(
    [[_motif_dna(42), Paragraph("Biotechnology : Principles and Processes", STYLES["Title"])]],
    colWidths=[1.55 * cm, FRAME_WIDTH - 1.55 * cm])
_title_row.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ("TOPPADDING", (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
]))
_title_row.hAlign = "LEFT"
story.append(_title_row)
story.append(HRFlowable(width="100%", thickness=1.1, color=DARK_GREY,
                        spaceBefore=4, spaceAfter=8))

# ---- Unit 9 introduction (unit opener page) ----
story.append(KeepTogether([
    heading("U9", "UNIT 9 - BIOTECHNOLOGY : WHY THIS UNIT EXISTS", 1),
    Paragraph(
        "Since <b>Rene Descartes</b> - the seventeenth-century French philosopher, mathematician "
        "and biologist - all human knowledge, and especially the natural sciences, has been "
        "directed towards technologies that add to the creature comforts of human lives and add "
        "value to human life. The whole approach to understanding natural phenomena thus became "
        "<b>anthropocentric</b>. Physics and chemistry gave rise to engineering, technologies and "
        "industries which all worked for human comfort and welfare; the major utility of the "
        "biological world is as a source of food.", STYLES["Body"]),
]))
story.append(Paragraph(
    "<b>Biotechnology</b> is the twentieth century off-shoot of modern biology. It changed our "
    "daily life because its products brought qualitative improvement in health and food "
    "production. This unit covers the basic principles underlying biotechnological processes "
    "(Chapter 9) and some of their applications (Chapter 10, Biotechnology and Its Applications).",
    STYLES["Body"]))
story.append(Spacer(1, 4))

# ---- Scientist profile box: Herbert Boyer (chapter opener page) ----
# TEXT ONLY - the source page carries a headshot, which is deliberately not embedded.
# A likeness carries no testable fact, and §4.4's hard no on photographs of people is not
# waived by monochrome conversion. Name, dates and achievements carry everything examinable.
_boyer_text = [
    Paragraph("<b>HERBERT BOYER (1936 - )</b>", STYLES["Body"]),
    Paragraph(
        "Born <b>1936</b>, brought up in a corner of western Pennsylvania where railroads and "
        "mines were the destiny of most young men. Completed graduate work at the University of "
        "Pittsburgh in <b>1963</b>, followed by <b>three years</b> of post-graduate studies at "
        "Yale. In <b>1966</b> he took over assistant professorship at the University of "
        "California at San Francisco.", STYLES["Body"]),
    Paragraph(
        "By <b>1969</b> he had performed studies on a couple of <b>restriction enzymes</b> of the "
        "<i>E. coli</i> bacterium with especially useful properties: these enzymes can cut DNA "
        "strands in a particular fashion, leaving what became known as <b>sticky ends</b> on the "
        "strands. These clipped ends made pasting together pieces of DNA a precise exercise.",
        STYLES["Body"]),
    Paragraph(
        "That discovery led to a rich and rewarding conversation in Hawaii with a Stanford "
        "scientist, <b>Stanley Cohen</b>. Cohen had been studying small ringlets of DNA called "
        "<b>plasmids</b>, which float about freely in the cytoplasm of certain bacterial cells and "
        "replicate independently from the coding strand of DNA; he had developed a method of "
        "removing these plasmids from the cell and then reinserting them in other cells. "
        "Combining this with DNA splicing let Boyer and Cohen recombine segments of DNA in "
        "desired configurations and insert the DNA into bacterial cells, which could then act as "
        "manufacturing plants for specific proteins. This breakthrough was the basis upon which "
        "the discipline of biotechnology was founded.", STYLES["Body"]),
]
_boyer = Table([[_icon_definition(), _boyer_text]],
               colWidths=[0.55 * cm, FRAME_WIDTH - 0.55 * cm])
_boyer.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOX", (0, 0), (-1, -1), 0.5, GRID_LINE),
    ("LEFTPADDING", (0, 0), (-1, -1), 5),
    ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
]))
_boyer.hAlign = "LEFT"
story.append(_boyer)
story.append(Spacer(1, 6))

# ---- 9.0 Chapter introduction: what biotechnology means ----
story.append(heading("9", "WHAT BIOTECHNOLOGY MEANS", 1))
story.append(keyterm(
    "<b>Biotechnology</b> deals with the techniques of using live organisms, or enzymes from "
    "organisms, to produce products and processes useful to humans. Taken together with the "
    "chapter summary, it also covers the <b>large scale production and marketing</b> of products "
    "and processes using live organisms, <b>cells</b> or enzymes."))
story.append(Paragraph(
    "In that broad sense, making <b>curd, bread or wine</b> - all microbe-mediated processes - "
    "could also be thought of as a form of biotechnology. However, the word is used in a "
    "<b>restricted sense</b> today: it refers to those processes which use <b>genetically "
    "modified organisms</b> to achieve the same on a <b>larger scale</b>. Further, many other "
    "processes and techniques are also included under biotechnology - for example <b><i>in "
    "vitro</i> fertilisation</b> leading to a 'test-tube' baby, synthesising a gene and using it, "
    "developing a <b>DNA vaccine</b>, or correcting a defective gene: all of these are part of "
    "biotechnology.", STYLES["Body"]))
story.append(keyterm(
    "The <b>European Federation of Biotechnology (EFB)</b> definition deliberately encompasses "
    "both the traditional view and modern molecular biotechnology: <i>'The integration of natural "
    "science and organisms, cells, parts thereof, and molecular analogues for products and "
    "services'</i>."))
story.append(Spacer(1, 3))

# ---- 9.1 Principles of Biotechnology ----
story.append(heading("9.1", "PRINCIPLES OF BIOTECHNOLOGY", 1, has_table=True))
story.append(Paragraph(
    "Among many techniques, <b>two core techniques</b> enabled the birth of modern biotechnology.",
    STYLES["Body"]))
story.append(data_table([
    ["Core technique", "What it is"],
    ["<b>(i) Genetic engineering</b>",
     "Techniques to alter the chemistry of genetic material (<b>DNA and RNA</b>), to introduce "
     "these into host organisms, and thus change the <b>phenotype</b> of the host organism."],
    ["<b>(ii) Bioprocess engineering</b>",
     "Maintenance of <b>sterile</b> (microbial contamination-free) ambience in chemical "
     "engineering processes, to enable growth of <b>only the desired</b> microbe / eukaryotic "
     "cell in large quantities for the manufacture of biotechnological products like "
     "antibiotics, vaccines, enzymes, etc."],
], col_widths=[1.05, 3.1]))
story.append(Spacer(1, 5))

# ---- 9.1 (cont.) Why genetic engineering was needed: the limits of hybridisation ----
story.append(heading("9.1", "Why genetic engineering was needed", 2, has_table=True))
story.append(Paragraph(
    "Sexual reproduction provides opportunities for variations and for the formulation of unique "
    "combinations of genetic setup, <b>some of which may be beneficial</b> to the organism as "
    "well as to the population.", STYLES["Body"]))
story.append(data_table([
    ["Mode of reproduction", "What it does to genetic information"],
    ["Asexual reproduction", "<b>Preserves</b> the genetic information."],
    ["Sexual reproduction", "<b>Permits variation.</b>"],
], col_widths=[1.2, 3.0]))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "Traditional <b>hybridisation</b> procedures used in plant and animal breeding <b>very often "
    "lead to inclusion and multiplication of undesirable genes</b> along with the desired genes. "
    "The techniques of genetic engineering - which include creation of <b>recombinant DNA</b>, use "
    "of <b>gene cloning</b> and <b>gene transfer</b> - overcome this limitation and allow us to "
    "isolate and introduce <b>only one or a set of desirable genes</b> without introducing "
    "undesirable genes into the target organism.", STYLES["Body"]))
story.append(Spacer(1, 3))

# ---- 9.1 (cont.) The fate of alien DNA and the origin of replication ----
story.append(heading("9.1", "Fate of an alien piece of DNA: the origin of replication", 2))
story.append(Paragraph(
    "What happens to a piece of DNA that is somehow transferred into an alien organism? "
    "<b>Most likely</b>, this piece of DNA would <b>not</b> be able to multiply itself in the "
    "progeny cells of the organism. But when it gets <b>integrated into the genome</b> of the "
    "recipient, it <b>may</b> multiply and be inherited along with the host DNA - because the "
    "alien piece of DNA has become part of a chromosome, which has the ability to replicate.",
    STYLES["Body"]))
story.append(keyterm(
    "In a chromosome there is a specific DNA sequence called the <b>origin of replication</b>, "
    "which is responsible for <b>initiating replication</b>. Therefore, for the multiplication of "
    "any alien piece of DNA in an organism, it needs to be a part of a chromosome(s) which has "
    "this specific sequence. An alien DNA is thus <b>linked with the origin of replication</b> so "
    "that it can replicate and multiply itself in the host organism."))
story.append(keyterm(
    "This can also be called <b>cloning</b>: making <b>multiple identical copies</b> of any "
    "template DNA."))
story.append(Spacer(1, 3))

# ---- 9.1 (cont.) The first recombinant DNA (1972) ----
story.append(heading("9.1", "The first artificial recombinant DNA molecule (1972)", 3))
story.append(Paragraph(
    "The construction of the first recombinant DNA emerged from the possibility of linking a gene "
    "encoding <b>antibiotic resistance</b> with a <b>native plasmid</b> (autonomously replicating "
    "circular extra-chromosomal DNA) of <i>Salmonella typhimurium</i>. <b>Stanley Cohen</b> and "
    "<b>Herbert Boyer</b> accomplished this in <b>1972</b>.", STYLES["Body"]))
story.append(process_flow([
    "Isolate the <b>antibiotic resistance gene</b> by cutting out a piece of DNA from a plasmid "
    "which was responsible for conferring antibiotic resistance. Cutting DNA at specific "
    "locations became possible with the discovery of the so-called <b>'molecular scissors'</b> - "
    "<b>restriction enzymes</b>.",
    "Link the cut piece of DNA with the <b>plasmid DNA</b>. These plasmid DNA act as "
    "<b>vectors</b> to transfer the piece of DNA attached to them - just as a mosquito acts as an "
    "insect vector to transfer the malarial parasite into the human body.",
    "Join the ends with the enzyme <b>DNA ligase</b>, which acts on cut DNA molecules and joins "
    "their ends. This makes a new combination of circular autonomously replicating DNA created "
    "<i>in vitro</i>, known as <b>recombinant DNA</b>.",
    "Transfer this DNA into <i>Escherichia coli</i>, a bacterium closely related to "
    "<i>Salmonella</i>. It could replicate using the new host's <b>DNA polymerase</b> enzyme and "
    "make multiple copies. This ability to multiply copies of the antibiotic resistance gene in "
    "<i>E. coli</i> was called <b>cloning of the antibiotic resistance gene in <i>E. coli</i></b>.",
]))
story.append(Spacer(1, 4))
story.append(KeepTogether([
    heading("9.1", "The three basic steps in genetically modifying an organism", 3),
    process_flow([
        "<b>Identification of DNA</b> with desirable genes.",
        "<b>Introduction</b> of the identified DNA into the host.",
        "<b>Maintenance</b> of introduced DNA in the host, and <b>transfer of the DNA to its "
        "progeny</b>.",
    ]),
]))
story.append(Spacer(1, 4))
story.append(memory_aid(
    "The whole chapter is one sentence: <b>CUT - PASTE - CARRY - COPY - HARVEST</b>. "
    "Cut (restriction enzyme), paste (ligase), carry (vector into a competent host), copy "
    "(origin of replication / PCR), harvest (bioreactor then downstream processing)."))
story.append(Spacer(1, 4))

# ---- 9.2 Tools of Recombinant DNA Technology ----
story.append(heading("9.2", "TOOLS OF RECOMBINANT DNA TECHNOLOGY", 1))
story.append(Paragraph(
    "Genetic engineering (recombinant DNA technology) can be accomplished <b>only</b> if we have "
    "the key tools. There are <b>five</b>: <b>restriction enzymes</b>, <b>polymerase enzymes</b>, "
    "<b>ligases</b>, <b>vectors</b> and the <b>host organism</b>.", STYLES["Body"]))
story.append(Spacer(1, 3))

# ---- 9.2.1 Restriction Enzymes ----
story.append(heading("9.2.1", "Restriction Enzymes", 2, has_table=True))
story.append(Paragraph(
    "The discovery ran in two stages, five years apart.", STYLES["Body"]))
story.append(data_table([
    ["Year", "What was found", "Significance"],
    ["<b>1963</b>",
     "The <b>two enzymes</b> responsible for restricting the growth of <b>bacteriophage</b> in "
     "<i>Escherichia coli</i> were isolated. One <b>added methyl groups</b> to DNA; the other "
     "<b>cut</b> DNA.",
     "The cutting enzyme was called <b>restriction endonuclease</b>."],
    ["<b>Five years later</b> (i.e. after 1963)",
     "The <b>first</b> restriction endonuclease - <b>Hind II</b> - whose functioning depended on a "
     "specific DNA nucleotide sequence, was isolated and characterised.",
     "Hind II always cuts DNA at a particular point by recognising a specific sequence of "
     "<b>six base pairs</b>. That sequence is its <b>recognition sequence</b>."],
    ["<b>Today</b>",
     "More than <b>900</b> restriction enzymes are known, isolated from over <b>230 strains</b> of "
     "bacteria.",
     "Each recognises a <b>different</b> recognition sequence."],
], col_widths=[1.5, 3.4, 3.1]))
story.append(Spacer(1, 4))

story.append(heading("9.2.1", "How restriction enzymes are named", 3, has_table=True))
story.append(Paragraph(
    "The name is not arbitrary - every part of <b>EcoRI</b> is readable:", STYLES["Body"]))
story.append(data_table([
    ["Part of the name", "Where it comes from", "In <b>EcoRI</b>"],
    ["<b>First letter</b>", "The <b>genus</b> of the prokaryotic cell it was isolated from",
     "<b>E</b> = <i>Escherichia</i>"],
    ["<b>Second two letters</b>", "The <b>species</b>", "<b>co</b> = <i>coli</i>"],
    ["<b>Following letter(s)</b>", "The name of the <b>strain</b>",
     "<b>R</b> = from strain <b>RY 13</b>"],
    ["<b>Roman number</b>",
     "The <b>order</b> in which the enzymes were isolated from that strain of bacteria",
     "<b>I</b> = the first isolated"],
], col_widths=[1.7, 4.3, 2.0]))
story.append(Spacer(1, 4))

story.append(heading("9.2.1", "Where restriction enzymes sit among the nucleases", 3,
                     has_table=True))
story.append(Paragraph(
    "Restriction enzymes belong to a larger class of enzymes called <b>nucleases</b>. These are of "
    "<b>two</b> kinds.", STYLES["Body"]))
story.append(data_table([
    ["Kind of nuclease", "Where it cuts"],
    ["<b>Exonucleases</b>", "Remove nucleotides <b>from the ends</b> of the DNA."],
    ["<b>Endonucleases</b>", "Make cuts at <b>specific positions within</b> the DNA."],
], col_widths=[2.2, 5.8]))
story.append(Spacer(1, 4))

story.append(heading("9.2.1", "How a restriction endonuclease works", 3))
story.append(process_flow([
    "<b>Inspect</b> - each restriction endonuclease functions by 'inspecting' the length of a DNA "
    "sequence.",
    "<b>Bind</b> - once it finds its specific <b>recognition sequence</b>, it binds to the DNA.",
    "<b>Cut</b> - it cuts <b>each of the two strands</b> of the double helix at specific points in "
    "their <b>sugar-phosphate backbones</b>.",
]))
story.append(Spacer(1, 3))
story.append(keyterm(
    "Each restriction endonuclease recognises a specific <b>palindromic nucleotide sequence</b> in "
    "the DNA. A palindrome is a group of letters that forms the same word read both forward and "
    "backward, e.g. <b>'MALAYALAM'</b>. But note the difference: in a word-palindrome the same "
    "word is read in both directions, whereas <b>the palindrome in DNA is a sequence of base "
    "pairs that reads the same on the two strands when the orientation of reading is kept the "
    "same</b>."))
story.append(Paragraph(
    "For example, the following sequence reads the same on the two strands in the "
    "<b>5' to 3'</b> direction - and this is also true if read in the <b>3' to 5'</b> direction:",
    STYLES["Body"]))
story.append(data_table([
    ["Strand", "Sequence"],
    ["<b>5'</b> ---", "<b>G A A T T C</b> --- <b>3'</b>"],
    ["<b>3'</b> ---", "<b>C T T A A G</b> --- <b>5'</b>"],
], col_widths=[1.6, 6.4]))
story.append(Spacer(1, 4))

story.append(heading("9.2.1", "Sticky ends - why the cut is off-centre", 3))
story.append(Paragraph(
    "Restriction enzymes cut the strand of DNA <b>a little away from the centre</b> of the "
    "palindrome sites, but <b>between the same two bases on the opposite strands</b>. This leaves "
    "<b>single stranded portions at the ends</b> - overhanging stretches called <b>sticky ends</b> "
    "on each strand.", STYLES["Body"]))
story.append(keyterm(
    "They are named <b>sticky</b> because they form <b>hydrogen bonds</b> with their complementary "
    "cut counterparts. This stickiness of the ends facilitates the action of the enzyme "
    "<b>DNA ligase</b>."))
story.append(Paragraph(
    "Restriction endonucleases are therefore used in genetic engineering to form "
    "<b>'recombinant' molecules of DNA</b>, which are composed of DNA <b>from different "
    "sources/genomes</b>. When cut by the <b>same</b> restriction enzyme, the resultant DNA "
    "fragments have the <b>same kind of sticky ends</b>, and these can be joined together "
    "(end-to-end) using DNA ligases.", STYLES["Body"]))
story.append(note(
    "Normally, <b>unless one cuts the vector and the source DNA with the same restriction "
    "enzyme</b>, the recombinant vector molecule <b>cannot</b> be created."))
story.append(Spacer(1, 4))
story.append(figure(
    "fig_9_1.png",
    "<b>Fig. 9.1</b> - Steps in formation of recombinant DNA by action of restriction "
    "endonuclease enzyme - EcoRI. The enzyme cuts both DNA strands at the same site, cutting "
    "between bases G and A only where the sequence GAATTC is present, so that the vector DNA and "
    "the foreign DNA both end in matching sticky ends and can join to give recombinant DNA. "
    "<i>The original is colour-coded; here the vector DNA is the outline strand and the foreign "
    "DNA the solid black strand.</i>",
    max_width_cm=14.5))

story.append(heading("9.2.1", "Separation and isolation of DNA fragments", 3))
story.append(Paragraph(
    "Cutting DNA with restriction endonucleases results in <b>fragments</b> of DNA. These "
    "fragments are separated by a technique known as <b>gel electrophoresis</b>.", STYLES["Body"]))
story.append(process_flow([
    "<b>Move them in a field</b> - since DNA fragments are <b>negatively charged</b> molecules, "
    "they are separated by forcing them to move <b>towards the anode</b> under an electric field "
    "through a medium/matrix.",
    "<b>Sieve them by size</b> - the most commonly used matrix nowadays is <b>agarose</b>, a "
    "<b>natural polymer extracted from sea weeds</b>. The fragments separate (resolve) according "
    "to their size through the <b>sieving effect</b> provided by the agarose gel. Hence the "
    "<b>smaller the fragment size, the farther it moves</b>.",
    "<b>Stain and view</b> - the separated fragments can be visualised <b>only after staining</b> "
    "the DNA with <b>ethidium bromide</b> followed by exposure to <b>UV radiation</b>. You cannot "
    "see pure DNA fragments in visible light without staining. You then see <b>bright orange "
    "coloured bands</b> of DNA.",
    "<b>Cut out and elute</b> - the separated bands of DNA are cut out from the agarose gel and "
    "extracted from the gel piece. This step is known as <b>elution</b>.",
]))
story.append(Paragraph(
    "The DNA fragments purified in this way are used in constructing recombinant DNA by joining "
    "them with <b>cloning vectors</b>.", STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(figure(
    "fig_9_3.png",
    "<b>Fig. 9.3</b> - A typical agarose gel electrophoresis showing migration of <b>undigested</b> "
    "DNA (lane 1) and <b>digested</b> sets of DNA fragments (lanes 2 to 4). The largest fragments "
    "stay nearest the wells and the smallest travel farthest.",
    max_width_cm=13.0))
story.append(memory_aid(
    "Gel electrophoresis in one line: <b>negative DNA runs to the positive anode, small runs "
    "fast</b>. Then <b>stain (ethidium bromide) - shine (UV) - see (orange bands) - snip "
    "(elution)</b>."))
story.append(Spacer(1, 4))

# ---- 9.2.2 Cloning Vectors ----
story.append(heading("9.2.2", "Cloning Vectors", 2, has_table=True))
story.append(Paragraph(
    "<b>Plasmids</b> and <b>bacteriophages</b> have the ability to replicate within bacterial "
    "cells <b>independent of the control of chromosomal DNA</b>. That independence is what makes "
    "them useful as vectors.", STYLES["Body"]))
story.append(data_table([
    ["Vector", "Copy number within the bacterial cell"],
    ["<b>Bacteriophages</b>",
     "Because of their <b>high number per cell</b>, they have <b>very high copy numbers</b> of "
     "their genome within the bacterial cells."],
    ["<b>Plasmids</b>",
     "Some may have only <b>one or two</b> copies per cell, whereas others may have "
     "<b>15-100</b> copies per cell. Their numbers can go even <b>higher</b>."],
], col_widths=[2.0, 6.0]))
story.append(Paragraph(
    "So if we can link an alien piece of DNA with bacteriophage or plasmid DNA, we can multiply "
    "its numbers <b>equal to the copy number</b> of the plasmid or bacteriophage.", STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "Vectors used at present are <b>engineered</b> in such a way that they help (a) <b>easy linking "
    "of foreign DNA</b> and (b) <b>selection of recombinants from non-recombinants</b>. Four "
    "engineered features do this work.", STYLES["Body"]))
story.append(Spacer(1, 3))

story.append(heading("9.2.2", "Feature 1 - Origin of replication (ori)", 3))
story.append(keyterm(
    "<b>Origin of replication (ori)</b> is a sequence <b>from where replication starts</b>, and any "
    "piece of DNA when linked to this sequence can be made to <b>replicate within the host "
    "cells</b>. This sequence is <b>also responsible for controlling the copy number</b> of the "
    "linked DNA."))
story.append(note(
    "Practical consequence: if one wants to recover <b>many copies</b> of the target DNA, it should "
    "be cloned in a vector <b>whose origin supports high copy number</b>."))
story.append(Spacer(1, 3))

story.append(heading("9.2.2", "Feature 2 - Selectable marker", 3))
story.append(keyterm(
    "In addition to 'ori', the vector requires a <b>selectable marker</b>, which helps in "
    "<b>identifying and eliminating non-transformants</b> and <b>selectively permitting the growth "
    "of the transformants</b>."))
story.append(keyterm(
    "<b>Transformation</b> is a procedure through which a piece of DNA is <b>introduced in a host "
    "bacterium</b>."))
story.append(Paragraph(
    "Normally the genes encoding <b>resistance to antibiotics</b> such as <b>ampicillin</b>, "
    "<b>chloramphenicol</b>, <b>tetracycline</b> or <b>kanamycin</b> are considered useful "
    "selectable markers for <i>E. coli</i>. This works because <b>normal <i>E. coli</i> cells do "
    "not carry resistance against any of these antibiotics</b>.", STYLES["Body"]))
story.append(Spacer(1, 3))

story.append(heading("9.2.2", "Feature 3 - Cloning sites", 3))
story.append(Paragraph(
    "In order to link the alien DNA, the vector needs to have <b>very few, preferably single</b>, "
    "recognition sites for the commonly used restriction enzymes. Presence of <b>more than one</b> "
    "recognition site within the vector will generate <b>several fragments</b>, which will "
    "complicate the gene cloning.", STYLES["Body"]))
story.append(Paragraph(
    "The ligation of alien DNA is carried out at a restriction site present in <b>one of the two "
    "antibiotic resistance genes</b>. For example, you can ligate a foreign DNA at the "
    "<b>BamH I site of the tetracycline resistance gene</b> in the vector <b>pBR322</b>. The "
    "recombinant plasmids will <b>lose tetracycline resistance</b> due to insertion of foreign "
    "DNA, but can still be selected out from non-recombinant ones by <b>plating the transformants "
    "on ampicillin containing medium</b>.", STYLES["Body"]))
story.append(process_flow([
    "Plate the transformants on <b>ampicillin</b> containing medium.",
    "Transfer the transformants growing on ampicillin medium onto a medium containing "
    "<b>tetracycline</b>.",
    "Read the result: the <b>recombinants will grow in ampicillin</b> containing medium but "
    "<b>not on tetracycline</b>. The <b>non-recombinants will grow on the medium containing both "
    "the antibiotics</b>.",
]))
story.append(Paragraph(
    "In this case <b>one</b> antibiotic resistance gene helps in <b>selecting the transformants</b>, "
    "whereas the <b>other</b> antibiotic resistance gene gets <b>'inactivated due to insertion'</b> "
    "of alien DNA and helps in <b>selection of recombinants</b>.", STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(figure(
    "fig_9_4.png",
    "<b>Fig. 9.4</b> - <i>E. coli</i> cloning vector <b>pBR322</b> showing restriction sites "
    "(Hind III, EcoR I, BamH I, Sal I, Pvu II, Pst I, Cla I), <b>ori</b>, and the antibiotic "
    "resistance genes <b>amp<super>R</super></b> and <b>tet<super>R</super></b>. <b>rop</b> codes "
    "for the proteins involved in the replication of the plasmid. <i>The original distinguishes "
    "the amp<super>R</super>, tet<super>R</super>, ori and rop arcs by colour; in this monochrome "
    "print each region is identified by its printed label, and the arcs are separated by the "
    "boundary lines at the restriction sites.</i>",
    max_width_cm=11.5))

story.append(heading("9.2.2", "A better marker - insertional inactivation with a colour readout",
                     3))
story.append(Paragraph(
    "Selection of recombinants due to inactivation of antibiotics is a <b>cumbersome</b> procedure, "
    "because it requires <b>simultaneous plating on two plates having different antibiotics</b>. "
    "Therefore alternative selectable markers have been developed which differentiate recombinants "
    "from non-recombinants on the basis of their <b>ability to produce colour in the presence of a "
    "chromogenic substrate</b>.", STYLES["Body"]))
story.append(process_flow([
    "A recombinant DNA is inserted <b>within the coding sequence of an enzyme, "
    "beta-galactosidase</b>.",
    "This results in <b>inactivation of the gene</b> for synthesis of this enzyme - referred to as "
    "<b>insertional inactivation</b>.",
    "Read the colour on a <b>chromogenic substrate</b>: <b>blue coloured colonies</b> mean the "
    "plasmid in the bacteria <b>does not have an insert</b>; colonies that <b>do not produce any "
    "colour</b> have suffered insertional inactivation of the beta-galactosidase gene and are "
    "<b>identified as recombinant colonies</b>.",
]))
story.append(Spacer(1, 3))

story.append(heading("9.2.2", "Vectors for cloning genes in plants and animals", 3, has_table=True))
story.append(Paragraph(
    "Here biotechnologists borrowed from natural pathogens, which have always transferred genes "
    "into eukaryotic hosts.", STYLES["Body"]))
story.append(data_table([
    ["Natural agent", "What it does in nature", "How it was turned into a vector"],
    ["<b><i>Agrobacterium tumifaciens</i></b>, a pathogen of several <b>dicot</b> plants",
     "Delivers a piece of DNA known as <b>'T-DNA'</b> to <b>transform normal plant cells into a "
     "tumor</b>, and directs these tumor cells to <b>produce the chemicals required by the "
     "pathogen</b>.",
     "Its <b>tumor inducing (Ti) plasmid</b> has been modified into a cloning vector which is "
     "<b>no more pathogenic</b> to the plants but is still able to use the mechanisms to deliver "
     "genes of our interest into a variety of plants."],
    ["<b>Retroviruses</b> in animals",
     "Have the ability to <b>transform normal cells into cancerous cells</b>.",
     "Have also been <b>disarmed</b> and are now used to deliver desirable genes into "
     "<b>animal cells</b>."],
], col_widths=[1.9, 3.1, 3.0]))
story.append(Paragraph(
    "Once a gene or a DNA fragment has been ligated into a suitable vector, it is transferred into "
    "a <b>bacterial, plant or animal host</b>, where it multiplies.", STYLES["Body"]))
story.append(Spacer(1, 4))

# ---- 9.2.3 Competent Host (For Transformation with Recombinant DNA) ----
story.append(heading("9.2.3", "Competent Host (for transformation with recombinant DNA)", 2))
story.append(Paragraph(
    "The obstacle is chemical: since <b>DNA is a hydrophilic molecule, it cannot pass through cell "
    "membranes</b>. So the host has to be forced to take it up.", STYLES["Body"]))
story.append(process_flow([
    "<b>Make the cells competent</b> - in order to force bacteria to take up the plasmid, the "
    "bacterial cells must first be made <b>'competent'</b> to take up DNA. This is done by treating "
    "them with a <b>specific concentration of a divalent cation, such as calcium</b>, which "
    "<b>increases the efficiency with which DNA enters the bacterium through pores in its cell "
    "wall</b>.",
    "<b>Incubate on ice</b> with the recombinant DNA.",
    "<b>Heat shock</b> - place them briefly at <b>42 degrees C</b>.",
    "<b>Return to ice</b> - this enables the bacteria to <b>take up the recombinant DNA</b>.",
]))
story.append(Spacer(1, 3))
story.append(heading("9.2.3", "Three other ways to get DNA into a cell", 3, has_table=True))
story.append(data_table([
    ["Method", "How it works", "Suited to"],
    ["<b>Micro-injection</b>",
     "Recombinant DNA is <b>directly injected into the nucleus</b>.",
     "<b>Animal</b> cells"],
    ["<b>Biolistics</b> or <b>gene gun</b>",
     "Cells are <b>bombarded with high velocity micro-particles of gold or tungsten coated with "
     "DNA</b>.",
     "<b>Plants</b>"],
    ["<b>'Disarmed pathogen' vectors</b>",
     "When allowed to <b>infect the cell</b>, they <b>transfer the recombinant DNA into the "
     "host</b>.",
     "Plant and animal cells"],
], col_widths=[2.0, 4.4, 1.6]))
story.append(memory_aid(
    "Four doors into a cell: <b>C - M - G - P</b>. <b>C</b>alcium-competent heat shock (bacteria), "
    "<b>M</b>icro-injection (animal), <b>G</b>ene gun / biolistics (plant), "
    "<b>P</b>athogen disarmed (both)."))
story.append(Spacer(1, 4))

# ---- 9.3 Processes of Recombinant DNA Technology ----
story.append(heading("9.3", "PROCESSES OF RECOMBINANT DNA TECHNOLOGY", 1))
story.append(Paragraph(
    "Recombinant DNA technology involves several steps in a <b>specific sequence</b>. The whole "
    "chapter's machinery is now assembled in order.", STYLES["Body"]))
story.append(process_flow([
    "<b>Isolation</b> of DNA.",
    "<b>Fragmentation</b> of DNA by restriction endonucleases.",
    "<b>Isolation of a desired DNA fragment.</b>",
    "<b>Ligation</b> of the DNA fragment into a vector.",
    "<b>Transferring</b> the recombinant DNA into the host.",
    "<b>Culturing</b> the host cells in a medium at large scale.",
    "<b>Extraction</b> of the desired product.",
]))
story.append(Spacer(1, 3))
story.append(figure(
    "fig_9_2.png",
    "<b>Fig. 9.2</b> - Diagrammatic representation of recombinant DNA technology: the <b>same "
    "restriction enzyme</b> cuts both foreign DNA and vector DNA (plasmid) at a specific point, "
    "<b>ligases join</b> the foreign DNA to the plasmid to give the <b>recombinant DNA "
    "molecule</b>, <b>transformation</b> carries it into <i>E. coli</i> (the cloning host), and "
    "the cells then <b>divide</b> - each daughter cell carrying the recombinant DNA.",
    max_width_cm=12.5))

# ---- 9.3.1 Isolation of the Genetic Material (DNA) ----
story.append(heading("9.3.1", "Isolation of the Genetic Material (DNA)", 2))
story.append(Paragraph(
    "Recall that <b>nucleic acid is the genetic material of all organisms without exception</b>, and "
    "in the majority of organisms this is <b>deoxyribonucleic acid (DNA)</b>. In order to cut the "
    "DNA with restriction enzymes, it needs to be in <b>pure form, free from other "
    "macro-molecules</b>.", STYLES["Body"]))
story.append(process_flow([
    "<b>Break the cell open</b> - since the DNA is enclosed within the membranes, the cell must be "
    "broken open to release DNA along with other macromolecules such as <b>RNA, proteins, "
    "polysaccharides and also lipids</b>. This is done by treating the bacterial cells / plant or "
    "animal tissue with enzymes: <b>lysozyme</b> (bacteria), <b>cellulase</b> (plant cells), "
    "<b>chitinase</b> (fungus).",
    "<b>Free the DNA from its protein packing</b> - genes are located on long molecules of DNA "
    "<b>interwined with proteins such as histones</b>.",
    "<b>Strip away RNA and protein</b> - the <b>RNA</b> can be removed by treatment with "
    "<b>ribonuclease</b>, whereas <b>proteins</b> can be removed by treatment with "
    "<b>protease</b>. Other molecules can be removed by appropriate treatments.",
    "<b>Precipitate the DNA</b> - purified DNA ultimately precipitates out after the addition of "
    "<b>chilled ethanol</b>. This can be seen as a <b>collection of fine threads in the "
    "suspension</b>.",
]))
story.append(Spacer(1, 3))
story.append(figure(
    "fig_9_5.png",
    "<b>Fig. 9.5</b> - DNA that separates out can be removed by <b>spooling</b>. The precipitated "
    "DNA appears as a collection of fine threads in the suspension.",
    max_width_cm=7.0))

# ---- 9.3.2 Cutting of DNA at Specific Locations ----
story.append(heading("9.3.2", "Cutting of DNA at Specific Locations", 2))
story.append(process_flow([
    "<b>Digest</b> - restriction enzyme digestions are performed by <b>incubating purified DNA "
    "molecules with the restriction enzyme</b>, at the <b>optimal conditions for that specific "
    "enzyme</b>.",
    "<b>Check the progress</b> - <b>agarose gel electrophoresis</b> is employed to check the "
    "progression of a restriction enzyme digestion. DNA is a <b>negatively charged</b> molecule, "
    "hence it moves <b>towards the positive electrode (anode)</b>.",
    "<b>Repeat with the vector</b> - the process is repeated with the <b>vector DNA</b> also.",
    "<b>Mix and ligate</b> - after having cut the source DNA as well as the vector DNA with a "
    "<b>specific restriction enzyme</b>, the cut out <b>'gene of interest'</b> from the source DNA "
    "and the <b>cut vector with space</b> are mixed and <b>ligase is added</b>. This results in the "
    "preparation of <b>recombinant DNA</b>.",
]))
story.append(Spacer(1, 4))

# ---- 9.3.3 Amplification of Gene of Interest Using PCR ----
story.append(heading("9.3.3", "Amplification of Gene of Interest Using PCR", 2))
story.append(keyterm(
    "<b>PCR</b> stands for <b>Polymerase Chain Reaction</b>. In this reaction, multiple copies of "
    "the gene (or DNA) of interest are synthesised <b>in vitro</b> using <b>two sets of "
    "primers</b> - small chemically synthesised <b>oligonucleotides</b> that are complementary to "
    "the regions of DNA - and the enzyme <b>DNA polymerase</b>."))
story.append(Paragraph(
    "The enzyme <b>extends the primers</b> using the <b>nucleotides provided in the reaction</b> "
    "and the <b>genomic DNA as template</b>. If the process of replication of DNA is repeated many "
    "times, the segment of DNA can be amplified to approximately <b>a billion times</b>, i.e. "
    "<b>1 billion copies</b> are made.", STYLES["Body"]))
story.append(process_flow([
    "<b>Denaturation</b> - the double stranded DNA is separated by <b>heat</b>.",
    "<b>Primer annealing</b> - the <b>two sets of primers</b> bind to their complementary regions.",
    "<b>Extension of primers</b> - <b>DNA polymerase (Taq polymerase) + deoxynucleotides</b> extend "
    "the primers.",
], cyclic=True))
story.append(note(
    "The enzyme used is a <b>thermostable DNA polymerase</b> isolated from the bacterium "
    "<b><i>Thermus aquaticus</i></b>, which <b>remains active during the high temperature induced "
    "denaturation</b> of double stranded DNA. That heat-stability is precisely why the cycle can be "
    "repeated without adding fresh enzyme."))
story.append(Paragraph(
    "The amplified fragment, if desired, can now be used to <b>ligate with a vector for further "
    "cloning</b>.", STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(figure(
    "fig_9_6.png",
    "<b>Fig. 9.6</b> - Polymerase chain reaction (PCR). Each cycle has three steps: "
    "(i) <b>Denaturation</b>; (ii) <b>Primer annealing</b>; and (iii) <b>Extension of primers</b>. "
    "Run for <b>30 cycles</b>, the region to be amplified is <b>amplified about 1 billion "
    "times</b>. <i>The shaded blocks mark the region being amplified; the outline blocks are the "
    "flanking DNA that is not.</i>",
    max_width_cm=12.5))
story.append(memory_aid(
    "PCR = <b>D - A - E</b>, thirty times over: <b>D</b>enature (heat splits the strands), "
    "<b>A</b>nneal (primers land), <b>E</b>xtend (Taq builds). Heat is the reason "
    "<i>Thermus aquaticus</i> is in the tube at all."))
story.append(Spacer(1, 4))

# ---- 9.3.4 Insertion of Recombinant DNA into the Host Cell/Organism ----
story.append(heading("9.3.4", "Insertion of Recombinant DNA into the Host Cell / Organism", 2))
story.append(Paragraph(
    "Recipient cells, after making them <b>'competent'</b> to receive, take up DNA present in their "
    "surroundings. The selection then does the sorting for us.", STYLES["Body"]))
story.append(process_flow([
    "Transfer a recombinant DNA bearing a gene for <b>resistance to an antibiotic</b> (e.g. "
    "<b>ampicillin</b>) into <i>E. coli</i> cells - the host cells become <b>ampicillin-resistant "
    "cells</b>.",
    "<b>Spread</b> the transformed cells on <b>agar plates containing ampicillin</b>.",
    "Read the plate: <b>only transformants will grow</b>; <b>untransformed recipient cells will "
    "die</b>.",
]))
story.append(keyterm(
    "The ampicillin resistance gene in this case is called a <b>selectable marker</b>."))
story.append(Spacer(1, 4))

# ---- 9.3.5 Obtaining the Foreign Gene Product ----
story.append(heading("9.3.5", "Obtaining the Foreign Gene Product", 2, has_table=True))
story.append(Paragraph(
    "When you insert a piece of alien DNA into a cloning vector and transfer it into a bacterial, "
    "plant or animal cell, <b>the alien DNA gets multiplied</b>. But in almost all recombinant "
    "technologies the <b>ultimate aim is to produce a desirable protein</b>. Hence there is a need "
    "for the recombinant DNA to be <b>expressed</b> - the foreign gene gets expressed under "
    "<b>appropriate conditions</b>.", STYLES["Body"]))
story.append(keyterm(
    "If any protein encoding gene is expressed in a <b>heterologous host</b>, it is called a "
    "<b>recombinant protein</b>."))
story.append(heading("9.3.5", "From small scale to large scale", 3, has_table=True))
story.append(data_table([
    ["Scale", "How it is run", "What it yields"],
    ["<b>Small scale</b> (laboratory)",
     "The cells harbouring cloned genes of interest may be grown on a <b>small scale in the "
     "laboratory</b>. The cultures may be used for <b>extracting the desired protein</b> and then "
     "<b>purifying it</b> by using different <b>separation techniques</b>.",
     "<b>Small volume cultures cannot yield appreciable quantities</b> of products."],
    ["<b>Continuous culture system</b>",
     "The <b>used medium is drained out from one side while fresh medium is added from the "
     "other</b>, to maintain the cells in their <b>physiologically most active log / exponential "
     "phase</b>.",
     "Produces a <b>larger biomass</b>, leading to <b>higher yields of desired protein</b>."],
    ["<b>Bioreactors</b>",
     "Large volumes of <b>100-1000 litres</b> of culture can be processed.",
     "The industrial scale needed once small volumes proved insufficient."],
], col_widths=[1.9, 3.6, 2.5]))
story.append(Spacer(1, 3))
story.append(keyterm(
    "<b>Bioreactors</b> can be thought of as <b>vessels in which raw materials are biologically "
    "converted into specific products, individual enzymes, etc., using microbial, plant, animal or "
    "human cells</b>. A bioreactor provides the <b>optimal conditions</b> for achieving the desired "
    "product by providing optimum growth conditions - <b>temperature, pH, substrate, salts, "
    "vitamins, oxygen</b>."))
story.append(Paragraph(
    "The <b>most commonly used bioreactors are of stirring type</b>. A <b>stirred-tank reactor</b> "
    "is usually <b>cylindrical</b> or with a <b>curved base</b> to facilitate the <b>mixing of the "
    "reactor contents</b>. The <b>stirrer</b> facilitates <b>even mixing and oxygen availability</b> "
    "throughout the bioreactor. Alternatively, <b>air can be bubbled through</b> the reactor.",
    STYLES["Body"]))
story.append(heading("9.3.5", "What a stirred-tank bioreactor must have", 3, has_table=True))
story.append(data_table([
    ["System", "Its job", "The part that does it"],
    ["<b>Agitator system</b>", "Even mixing of the reactor contents.",
     "A <b>motor</b> on top driving a <b>flat bladed impeller</b> down in the "
     "<b>culture broth</b>."],
    ["<b>Oxygen delivery system</b>", "Oxygen availability throughout the bioreactor.",
     "A <b>sterile air</b> inlet."],
    ["<b>Foam control system</b>", "Controls the foam that agitation throws up.",
     "A <b>foam breaker</b>, mounted on the same shaft above the broth."],
    ["<b>Temperature control system</b>", "Holds the optimum temperature.",
     "A <b>jacket / coil</b> around the vessel; <b>steam</b> is also piped in for "
     "<b>sterilisation</b>."],
    ["<b>pH control system</b>", "Holds the optimum pH.",
     "An <b>acid</b> line and a <b>base</b> line into the vessel."],
    ["<b>Sampling ports</b>",
     "So that <b>small volumes of the culture can be withdrawn periodically</b>.",
     "A <b>sampling port</b> in the vessel wall."],
], col_widths=[2.1, 3.0, 2.9]))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "In the <b>sparged stirred-tank</b> variant, <b>sterile air is sparged</b> (blown in as fine "
    "bubbles) from the base. This gives an <b>increased surface area for oxygen transfer</b> plus "
    "<b>gas entrainment</b>, because the <b>bubbles dramatically increase the oxygen transfer "
    "area</b>.", STYLES["Body"]))
story.append(Spacer(1, 3))
story.append(figure(
    "fig_9_7.png",
    "<b>Fig. 9.7</b> - (a) Simple <b>stirred-tank bioreactor</b>, showing the motor, foam breaker, "
    "flat bladed impeller, culture broth, sterile air inlet, acid/base line for pH control and "
    "steam for sterilisation; (b) <b>Sparged stirred-tank bioreactor</b> through which sterile air "
    "bubbles are sparged - giving <b>increased surface area for oxygen transfer</b> and <b>gas "
    "entrainment</b>, because the <b>bubbles dramatically increase the oxygen transfer area</b>.",
    max_width_cm=15.5))

# ---- 9.3.6 Downstream Processing ----
story.append(heading("9.3.6", "Downstream Processing", 2))
story.append(Paragraph(
    "After completion of the <b>biosynthetic stage</b>, the product has to be subjected to a "
    "<b>series of processes</b> before it is ready for marketing as a finished product.",
    STYLES["Body"]))
story.append(keyterm(
    "The processes include <b>separation and purification</b>, which are collectively referred to "
    "as <b>downstream processing</b>."))
story.append(process_flow([
    "<b>Separation and purification</b> of the product.",
    "<b>Formulation</b> - the product has to be formulated with <b>suitable preservatives</b>.",
    "<b>Clinical trials</b> - such formulation has to undergo <b>thorough clinical trials</b> as in "
    "the case of drugs.",
    "<b>Quality control</b> - <b>strict quality control testing for each product</b> is also "
    "required.",
]))
story.append(note(
    "The <b>downstream processing and quality control testing vary from product to product</b> - "
    "there is no single fixed protocol to memorise here."))
story.append(Spacer(1, 4))

# ---- Quick Recap (the NCERT summary, every clause traced back to the body) ----
story.append(heading("R", "QUICK RECAP", 1))
story.append(process_flow([
    "<b>Biotechnology</b> deals with <b>large scale production and marketing</b> of products and "
    "processes using <b>live organisms, cells or enzymes</b>.",
    "Modern biotechnology using <b>genetically modified organisms</b> was made possible only when "
    "man learnt to <b>alter the chemistry of DNA</b> and <b>construct recombinant DNA</b>. This key "
    "process is called <b>recombinant DNA technology</b> or <b>genetic engineering</b>.",
    "The process involves the use of <b>restriction endonucleases</b>, <b>DNA ligase</b>, and "
    "<b>appropriate plasmid or viral vectors</b> to <b>isolate and ferry the foreign DNA</b> into "
    "host organisms.",
    "Then comes <b>expression of the foreign gene</b>, <b>purification of the gene product</b> "
    "(i.e. the functional protein), and finally <b>making a suitable formulation for "
    "marketing</b>.",
    "<b>Large scale production involves use of bioreactors.</b>",
]))
story.append(Spacer(1, 4))

# ---- Appendix: what the NCERT exercises assume ----
# Rule 5 applies here too: where the chapter supplies no fact, this appendix says so instead of
# inventing one. Nothing outside the source chapter is added.
story.append(heading("A", "APPENDIX - WHAT THE NCERT EXERCISES ASSUME", 1, has_table=True))
story.append(Paragraph(
    "Every exercise question is either answerable from the sections above, or it is not answerable "
    "from this chapter at all. Both cases are stated plainly - no outside facts have been "
    "introduced to paper over a gap.", STYLES["Body"]))
story.append(data_table([
    ["Exercise asks about", "Status", "Where it is covered / why it is not"],
    ["<b>Recombinant proteins used in medical practice</b> (list of 10)",
     "<b>Beyond this chapter</b>",
     "The chapter <b>defines</b> a recombinant protein (9.3.5) but supplies <b>no list</b>. The "
     "exercise directs you to an internet search, so no list is invented here."],
    ["<b>Restriction enzyme</b>, its substrate DNA, cut site and product",
     "<b>Covered</b>",
     "9.2.1 (mechanism, palindromes, sticky ends) and <b>Fig. 9.1</b>."],
    ["<b>Relative molecular size</b> of enzymes vs DNA",
     "<b>Beyond this chapter</b>",
     "The chapter gives <b>no molecular sizes</b>. It is a reasoning exercise; no figure has been "
     "invented to fill it."],
    ["<b>Molar concentration of human DNA</b> in a human cell",
     "<b>Beyond this chapter</b>",
     "No data given anywhere in the chapter; the exercise itself says <b>'Consult your "
     "teacher'</b>."],
    ["Do <b>eukaryotic cells</b> have restriction endonucleases?",
     "<b>Reason from the chapter</b>",
     "9.2.1 states the enzymes were isolated <b>from bacteria</b> (over 230 strains) and that "
     "their natural role is <b>restricting bacteriophage growth</b> - reason from those two facts "
     "only."],
    ["Advantages of <b>stirred tank bioreactors over shake flasks</b>",
     "<b>Covered</b>",
     "9.3.5 - the <b>100-1000 litre</b> volume plus the six control systems (agitator, oxygen, "
     "foam, temperature, pH, sampling ports)."],
    ["<b>Palindromic DNA sequences</b>",
     "<b>Covered</b>",
     "9.2.1 - the definition, the MALAYALAM analogy, and the <b>GAATTC / CTTAAG</b> pair."],
    ["<b>Meiosis stage</b> at which a recombinant DNA is made",
     "<b>Beyond this chapter</b>",
     "Recombination / crossing over is <b>not covered</b> here; it belongs to the inheritance "
     "chapters."],
    ["A <b>reporter enzyme</b> to monitor transformation alongside a selectable marker",
     "<b>Covered</b>",
     "9.2.2 - the <b>beta-galactosidase</b> insertional-inactivation and chromogenic-substrate "
     "colour readout is exactly this."],
    ["<b>ori</b>; bioreactors; downstream processing; PCR; restriction enzymes; chitinase; "
     "plasmid vs chromosomal DNA; RNA vs DNA; exonuclease vs endonuclease",
     "<b>All covered</b>",
     "9.1 and 9.2.2 (ori), 9.3.5 (bioreactors), 9.3.6 (downstream), 9.3.3 (PCR), 9.2.1 "
     "(restriction enzymes, exo vs endo), 9.3.1 (chitinase, nucleic acid), 9.1 / 9.2.2 "
     "(plasmid)."],
], col_widths=[2.4, 1.4, 4.2]))
story.append(Spacer(1, 4))
story.append(note(
    "<b>Source problems noted during extraction.</b> Page-number artifacts bleed into the extracted "
    "text of the source PDF (e.g. \"others may have 168 15-100 copies per cell\" on page 8, and "
    "\"117722\" on page 12). Checked against the rendered page images: the true values are "
    "<b>15-100 copies per cell</b> and page number <b>172</b>. No content is missing. The "
    "unit-opening page also interleaves the Unit 9 introduction with the chapter-list sidebar, so "
    "that text was reconstructed from the rendered page image."))


# --------------------------------------------------------------------------------------
# 4. BUILD
# --------------------------------------------------------------------------------------
# Spec section 4: no header, no footer, no page numbers, and no rule lines at the top or
# bottom of the page. Every page therefore carries content only -- there is deliberately
# no onFirstPage / onLaterPages canvas callback.

def main():
    doc = SimpleDocTemplate(
        OUT_PDF, pagesize=PAGE_SIZE,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=TOP_MARGIN, bottomMargin=BOTTOM_MARGIN,
        title="Class 12 Chapter 9 - Biotechnology : Principles and Processes (NEET notes)",
        author="NCERT replacement notes", subject="NEET Biology",
    )
    doc.build(story)
    size_kb = os.path.getsize(OUT_PDF) / 1024
    print(f"Built {OUT_PDF} ({size_kb:.0f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
