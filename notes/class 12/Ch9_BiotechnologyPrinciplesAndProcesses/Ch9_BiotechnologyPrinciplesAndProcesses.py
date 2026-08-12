"""
NCERT Biology -> NEET replacement notes
Class 12, Chapter 9 : Biotechnology : Principles and Processes

Source  : Chapter/class 12/Chapter 9 - Biotechnology Principles and Processes.pdf
Built to: SUPREME COMMAND PROMPT.md v4 (full-replacement edition, original NCERT figures)

Run from the repository root:
    .venv/bin/python "notes/class 12/Ch9_BiotechnologyPrinciplesAndProcesses/Ch9_BiotechnologyPrinciplesAndProcesses.py"

Structure of this file:
  1. Canonical style block (§4)
  2. The three sanctioned helpers: process_flow() (§4.2), figure() (§4.4), boxes/headings (§4.1/§4.3)
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
    """Filled square badge with the NCERT section number in white (§4.1)."""
    d = Drawing(size, size)
    d.add(Rect(0, 0, size, size, fillColor=INK, strokeColor=INK, strokeWidth=0))
    fs = size * 0.46 if len(label) <= 3 else size * 0.34
    d.add(String(size / 2, size * 0.5 - fs * 0.36, label, fontName="Times-Bold",
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


def _step_badge(n: int, size: float = 14) -> Drawing:
    """Filled triangle badge with white step number (§4.2)."""
    d = Drawing(size, size)
    d.add(Polygon(points=[0, 0, size, 0, size / 2, size],
                  fillColor=INK, strokeColor=INK, strokeWidth=0))
    d.add(String(size / 2, size * 0.16, str(n), fontName="Times-Bold",
                 fontSize=size * 0.44, fillColor=white, textAnchor="middle"))
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
    effective resolution, and kept together with its caption across page breaks.
    A missing asset raises a loud, named error - the figure is never silently skipped."""
    path = os.path.join(ASSETS, asset_name)
    if not os.path.exists(path):
        raise FileNotFoundError(f"MISSING FIGURE ASSET: {path} (required by caption: {caption_text})")
    try:
        from PIL import Image as PILImage
        with PILImage.open(path) as im:
            px_w, px_h = im.size
    except Exception as exc:
        raise RuntimeError(f"CANNOT READ FIGURE ASSET {path}: {exc}")

    max_w = min(max_width_cm * cm, FRAME_WIDTH)
    natural_w = px_w / 300.0 * 2.54 * cm          # width at 300 dpi effective resolution
    width = min(max_w, natural_w)
    height = width * px_h / px_w
    img = Image(path, width=width, height=height)
    img.hAlign = "CENTER"
    return KeepTogether([img, Paragraph(caption_text, STYLES["Caption"])])


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
_boyer = Table([[Image(os.path.join(ASSETS, "fig_boyer.png"), width=2.6 * cm, height=3.88 * cm),
                 _boyer_text]],
               colWidths=[2.9 * cm, FRAME_WIDTH - 2.9 * cm])
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
