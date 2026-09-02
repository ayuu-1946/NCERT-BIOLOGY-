"""
NCERT Class 11 Biology, Chapter 12 - Respiration in Plants
NEET replacement notes -> A4 print-ready PDF.

Built under SUPREME COMMAND PROMPT.md v6, Pass 2: written linearly from the
frozen 164-row inventory (Ch12_RespirationInPlants_inventory.md, F001-F164),
importing the repo-level frozen style module `neet_template.py` (v6 SS0.6).
No style, geometry, colour or font is re-declared here.

Block markers `# ---- N.N ----` mark every NCERT section so a Pass 3 flag can be
found and fixed in one contiguous block. Inventory row IDs are named in the
comments so any fact can be traced back to its frozen row.

Operator-directed layout decisions for this build (recorded in
figure_layout_decisions.md, never in the PDF - Rule 6):

  * COMPACT TALL FIGURES. Four of the six assets are portrait plates; at the
    default max_width_cm=15.9 Fig 12.1 (AR 0.556) and Fig 12.4 (AR 0.595) would
    render 27-29 cm tall - taller than the 24.9 cm text column - and even at
    their 300 dpi natural widths (8.54 / 9.75 cm) they cost 15-16 cm of height
    while leaving ~8 cm of column empty beside them. Every tall plate therefore
    renders below its natural width. All moves are DOWNWARD, so the no-upscale
    cap in neet_template.figure() is untouched and effective print resolution
    RISES in every case.

  * FIG 12.1 IS SIZED TO FILL ITS OWN PAGE (operator instruction, this revision).
    It was previously paired with Fig 12.2 in one side-by-side row; that pairing
    spent the spare column but forced BOTH plates onto the page after SS12.2 and
    squeezed the glycolysis chart - the most examined diagram in the chapter -
    down to 6.6 cm. Unpaired, Fig 12.1 is HEIGHT-limited rather than width-
    limited: 17.69 cm is free below the pyruvate-fate table, the full-column
    caption costs 2.65 cm and the frame padding 0.35 cm, leaving 14.4 cm of
    picture, which at AR 0.556 is 8.0 cm wide. That is still inside the 8.54 cm
    natural width, so the chart grows to fill the page with NO upscaling. Its
    NCERT source is a 150 dpi raster, so 8.0 cm is also near the point where
    more display width would stop buying real detail.

  * PAIRED PANELS WHERE THE FIGURES ARE ADJACENT. Where a compact width leaves a
    column half empty and the neighbouring figure belongs to the same section,
    that space is spent rather than left blank:
      - Fig 12.4 (ETS) + Fig 12.5 (ATP synthesis) sit side by side inside
        SS12.4.2, the single section that covers both.
    Figures 12.1, 12.2, 12.3 and 12.6 stand alone: 12.1 fills its page as above,
    12.2 keeps its place at the pyruvate branch point and is centred at 11.0 cm
    (below its 12.68 cm 300 dpi natural width after the PR #192 high-DPI
    re-render, so no upscaling), 12.3 has no same-section neighbour, and 12.6
    is a landscape plate (AR 1.288) that already uses the full width.

  * SS12.4 PAGE BREAK + FIG 12.2 / FIG 12.3 RESIZE (operator instruction, this
    revision). SS12.4 previously started at the foot of page 4 (heading + intro
    + step 1) with its process-flow split across the page turn; an explicit
    PageBreak now opens the whole SS12.4 block on page 5. The space vacated on
    page 4 is spent enlarging Fig 12.2 from 8.65 cm to 11.0 cm - sized so all of
    SS12.3 still completes on page 4 with no overflow. Fig 12.3 is reduced from
    9.0 cm to 8.2 cm so the SS12.4.2 oxygen-role sentence ("...oxygen acts as
    the final hydrogen acceptor") completes on the same page as Fig 12.3 instead
    of stranding its final line on the following page. Page count is unchanged
    at 10.

  * SS12.5 PAGE BREAK + FIG 12.4 ENLARGEMENT (operator instruction, this revision).
    SS12.5 previously began at the foot of page 7 directly under the Fig 12.4 /
    Fig 12.5 plate: only the section banner and its opening paragraph fitted
    there, while the assumptions list, the NOTE and the balance sheet carried
    over to page 8. An explicit PageBreak now opens the whole SS12.5 block on
    page 8. The ~2.4 cm of column height vacated on page 7 is spent enlarging
    Fig 12.4 from 7.0 cm to 8.4 cm (picture 11.77 -> 14.12 cm tall), still inside
    its 9.75 cm natural width, so the move is DOWNWARD-only and no upscaling
    occurs. Fig 12.5 is left at its 7.6 cm request on purpose: its 300 dpi
    natural width is just 6.67 cm, so _panel() already clamps it there and any
    larger number would only push it past 300 dpi without changing the render.
    The pair therefore grows on the 12.4 side alone, and the row still measures
    ~16.1 cm inside the 18 cm column. Page count is unchanged at 10 and pages
    9-10 are pixel-identical to the previous build.

  * EXERCISES. The Pass 1 exercise-gap scan found ZERO gaps: all 12 exercises are
    answered by the body. Per Rule 2 step 4 and SS5 item 9 the chapter therefore
    ends at the Quick Recap with no "Terms used in the exercises" appendix and no
    exercise section at all. Read as: 12 exercises, 0 answered by design (GAP),
    12 unanswered by design (COVERED), 0 overlooked. F164 (the source's
    "Exercises" structural heading) consequently has no reader-facing block; that
    is the rule working, not a dropped row - see figure_layout_decisions.md SS4.

Every in-figure label of all six figures is carried in running text or in the
figure's own caption tour (SS4.4 Step 4, check_pdf.py check 6).

Source: Chapter/class 11/Chapter 12 - Respiration in Plants.pdf
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# sys.path bootstrap: walk up until we find the repo-level neet_template.py (SS0.6)
_probe = HERE
while _probe != os.path.dirname(_probe):
    if os.path.exists(os.path.join(_probe, "neet_template.py")):
        sys.path.insert(0, _probe)
        break
    _probe = os.path.dirname(_probe)

from neet_template import (  # noqa: E402
    STYLES, FRAME_WIDTH, GRID_LINE,
    heading, keyterm, process_flow, note, memory_aid, data_table, title_block, build_pdf,
)
from neet_template import figure as _shared_figure  # noqa: E402
from reportlab.platypus import (  # noqa: E402
    Paragraph, Spacer, Image, Table, TableStyle, KeepTogether, PageBreak,
)
from reportlab.lib.units import cm  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch12_RespirationInPlants.pdf")

# Inline chemical formulae - <sub>/<super> tags only, never Unicode (SS4 technical rules)
O2 = "O<sub>2</sub>"
CO2 = "CO<sub>2</sub>"
H2O = "H<sub>2</sub>O"
HP = "H<super>+</super>"
NADp = "NAD<super>+</super>"
NADH = "NADH + H<super>+</super>"
FADp = "FAD<super>+</super>"
FADH2 = "FADH<sub>2</sub>"


def figure(asset_name, caption_text, max_width_cm=15.9):
    """Chapter-local binding of the shared figure() helper (SS0.6)."""
    return _shared_figure(asset_name, caption_text, ASSETS, max_width_cm=max_width_cm)


def _panel(asset_name, caption_text, width_cm):
    """One framed figure panel + its own caption, as a single-column Table.

    Used only to place two adjacent figures side by side (see the module
    docstring). Framing (0.5pt GRID_LINE box, 5pt padding), the monochrome guard
    and the 300 dpi no-upscale cap are exactly the rules neet_template.figure()
    applies - nothing style-level is invented here.
    """
    path = os.path.join(ASSETS, asset_name)
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"MISSING FIGURE ASSET: {path} (required by caption: {caption_text})")
    try:
        from PIL import Image as PILImage
        with PILImage.open(path) as im:
            px_w, px_h = im.size
            mode = im.mode
    except Exception as exc:
        raise RuntimeError(f"CANNOT READ FIGURE ASSET {path}: {exc}")
    if mode != "L":
        raise RuntimeError(
            f"FIGURE NOT MONOCHROME: {asset_name} has mode {mode!r}, expected 'L'.")

    natural_w = px_w / 300.0 * 2.54 * cm       # width at 300 dpi effective resolution
    width = min(width_cm * cm, natural_w)      # never upscale past 300 dpi
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

    col = Table([[framed], [Paragraph(caption_text, STYLES["Caption"])]],
                colWidths=[width + 12])
    col.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return col, width + 12


def figure_pair(left, right, gutter=6):
    """Two figure panels side by side, each with its own caption, kept together.

    `left` / `right` are (asset_name, caption_text, width_cm) triples, so the two
    panels may carry different widths - a tall plate can be shrunk hard while its
    square neighbour keeps a readable size, and together they fill the column.
    """
    lcol, lw = _panel(*left)
    rcol, rw = _panel(*right)
    row = Table([[lcol, rcol]], colWidths=[lw, rw])
    row.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (0, -1), gutter),
        ("RIGHTPADDING", (1, 0), (1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    row.hAlign = "CENTER"
    return KeepTogether([row])


def body(text):
    return Paragraph(text, STYLES["Body"])


def b1(text):
    return Paragraph("&bull; " + text, STYLES["Bullet1"])


def b2(text):
    return Paragraph("- " + text, STYLES["Bullet2"])


def gap(h=4):
    return Spacer(1, h)


story = []

# ======================================================================================
# ---- Title block (SS5 item 1) ---- F001
# ======================================================================================
story.extend(title_block("Respiration in Plants"))

# ======================================================================================
# ---- Introduction (unnumbered opener section) ---- F002-F017
# ======================================================================================
story.append(heading("12", "Food, Oxidation and the ATP Currency", 1))
story.append(body(
    "<b>All living organisms need energy</b> for carrying out daily life activities, be it "
    "<b>absorption, transport, movement, reproduction</b> or even <b>breathing</b>. All the "
    "energy required for <b>'life' processes</b> is obtained by <b>oxidation of some "
    "macromolecules that we call 'food'</b>."))
story.append(b1(
    "<b>Green plants and cyanobacteria</b> can <b>prepare their own food</b>: by "
    f"<b>photosynthesis</b> they <b>trap light energy</b> and convert it into <b>chemical "
    "energy</b> stored in the <b>bonds of carbohydrates</b> like <b>glucose, sucrose and "
    "starch</b>."))
story.append(b1(
    "In green plants too, <b>not all cells, tissues and organs photosynthesise</b> - "
    "<b>only cells containing chloroplasts</b>, that are <b>most often located in the "
    "superficial layers</b>, carry out photosynthesis."))
story.append(b1(
    "Even in green plants <b>all other organs, tissues and cells that are non-green need food "
    "for oxidation</b>. Hence, <b>food has to be translocated to all non-green parts</b>."))
story.append(b1(
    "<b>Animals are heterotrophic</b>, i.e., they obtain food from plants <b>directly "
    "(herbivores)</b> or <b>indirectly (carnivores)</b>."))
story.append(b1(
    "<b>Saprophytes like fungi</b> are dependent on <b>dead and decaying matter</b>."))
story.append(body(
    "So <b>ultimately all the food that is respired for life processes comes from "
    "photosynthesis</b>. <b>Photosynthesis takes place within the chloroplasts</b> (in the "
    "<b>eukaryotes</b>), whereas the <b>breakdown of complex molecules to yield energy takes "
    "place in the cytoplasm and in the mitochondria</b> (also <b>only in eukaryotes</b>)."))
story.append(keyterm(
    "<b>Respiration:</b> the <b>breaking of the C-C bonds of complex compounds through "
    "oxidation within the cells</b>, leading to <b>release of considerable amount of "
    "energy</b>."))
story.append(keyterm(
    "<b>Respiratory substrates:</b> the <b>compounds that are oxidised</b> during this "
    "process. <b>Usually carbohydrates are oxidised</b> to release energy, but "
    "<b>proteins, fats and even organic acids can be used</b> as respiratory substances "
    "in <b>some plants, under certain conditions</b>."))
story.append(body(
    "During oxidation within a cell, <b>all the energy contained in respiratory substrates is "
    "not released free into the cell, or in a single step</b>. It is released in a <b>series "
    "of slow step-wise reactions controlled by enzymes</b>, and it is <b>trapped as chemical "
    "energy in the form of ATP</b>. The energy released by oxidation in respiration is "
    "<b>not (or rather cannot be) used directly</b> but is used to <b>synthesise ATP</b>, "
    "which is <b>broken down whenever (and wherever) energy needs to be utilised</b>. Hence "
    "<b>ATP acts as the energy currency of the cell</b>."))
story.append(note(
    "Respiration does not only pay the energy bill. The <b>carbon skeleton produced during "
    "respiration is used as precursors for biosynthesis of other molecules in the cell</b> - "
    "the point SS12.6 returns to as the amphibolic nature of the pathway."))

# ======================================================================================
# ---- 12.1 Do Plants Breathe? ---- F018-F037
# ======================================================================================
story.append(heading("12.1", "Do Plants Breathe?", 1))
story.append(body(
    "The answer to this question is <b>not quite so direct</b>. <b>Yes</b>, plants require "
    f"{O2} for respiration to occur and they <b>also give out</b> {CO2}. But "
    "<b>plants, unlike animals, have no specialised organs for gaseous exchange</b> - "
    "<b>they have stomata and lenticels</b> for this purpose."))
story.append(heading("12.1a", "Why No Respiratory System Is Needed", 3, has_table=True))
story.append(data_table([
    ["Reason", "What NCERT states"],
    ["<b>Each part is on its own</b>",
     "<b>Each plant part takes care of its own gas-exchange needs</b>. There is <b>very "
     "little transport of gases from one plant part to another</b>."],
    ["<b>The demand is low</b>",
     "Plants <b>do not present great demands for gas exchange</b>. <b>Roots, stems and leaves "
     "respire at rates far lower than animals do</b>."],
    ["<b>Peak demand is self-served</b>",
     "<b>Only during photosynthesis are large volumes of gases exchanged</b>, and <b>each leaf "
     "is well adapted to take care of its own needs during these periods</b>. When cells "
     f"photosynthesise, <b>availability of {O2} is not a problem</b> in these cells since "
     f"<b>{O2} is released within the cell</b>."],
    ["<b>Diffusion distances are short</b>",
     "The <b>distance that gases must diffuse even in large, bulky plants is not great</b>. "
     "<b>Each living cell in a plant is located quite close to the surface of the plant</b>. "
     "In <b>stems</b>, the <b>'living' cells are organised in thin layers inside and beneath "
     "the bark</b>; they also have <b>openings called lenticels</b>. The <b>cells in the "
     "interior are dead and provide only mechanical support</b>."],
    ["<b>Air reaches the cells</b>",
     "<b>Most cells of a plant have at least a part of their surface in contact with air</b>. "
     "This is also facilitated by the <b>loose packing of parenchyma cells in leaves, stems and "
     "roots</b>, which provide an <b>interconnected network of air spaces</b>."],
], col_widths=[3.4, 9.2]))
story.append(gap())
story.append(body(
    "<b>The complete combustion of glucose</b>, which produces "
    f"{CO2} and {H2O} as end products, <b>yields energy most of which is given out as "
    "heat</b>:"))
story.append(body(
    "<b>C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + 6O<sub>2</sub> yields "
    "6CO<sub>2</sub> + 6H<sub>2</sub>O + Energy</b>"))
story.append(body(
    "<b>The key is to oxidise glucose not in one step but in several small steps</b>, enabling "
    "<b>some steps to be just large enough such that the energy released can be coupled to ATP "
    "synthesis</b>. During the process of respiration, <b>oxygen is utilised</b>, and "
    "<b>carbon dioxide, water and energy are released as products</b>."))
story.append(heading("12.1b", "The Anaerobic Legacy", 3))
# [VERIFICATION FIX D1] Pass 3(b) direction 2 found the NCERT antecedent sentence
# "Even among present-day living organisms, we know of several that are adapted to
# anaerobic conditions." missing from the freeze AND from this block (new row F034a).
# Without it "Some of these organisms" attached to "the first cells on this planet",
# which reads facultative/obligate anaerobes as extinct first cells - a DRIFT of
# meaning, not just a dropped sentence.
story.append(body(
    "There are <b>sufficient reasons to believe that the first cells on this planet lived in an "
    "atmosphere that lacked oxygen</b>. <b>Even among present-day living organisms, we know of "
    "several that are adapted to anaerobic conditions.</b> <b>Some of these organisms are "
    "facultative "
    "anaerobes</b>, while <b>in others the requirement for anaerobic condition is "
    "obligate</b>. In any case, <b>all living organisms retain the enzymatic machinery to "
    "partially oxidise glucose without the help of oxygen</b>."))
story.append(keyterm(
    "<b>Glycolysis:</b> this <b>breakdown of glucose to pyruvic acid</b>."))

# ======================================================================================
# ---- 12.2 Glycolysis ---- F038-F060, and Fig 12.1 / Fig 12.2 (F061-F062, F076-F077)
# ======================================================================================
story.append(heading("12.2", "Glycolysis", 1))
story.append(body(
    "The term <b>glycolysis</b> has originated from the <b>Greek words, glycos for sugar, and "
    "lysis for splitting</b>. The <b>scheme of glycolysis was given by Gustav Embden, Otto "
    "Meyerhof, and J. Parnas</b>, and is <b>often referred to as the EMP pathway</b>."))
story.append(b1(
    "<b>In anaerobic organisms, it is the only process in respiration.</b>"))
story.append(b1(
    "<b>Glycolysis occurs in the cytoplasm of the cell</b> and is <b>present in all living "
    "organisms</b>."))
story.append(b1(
    "In this process, <b>glucose undergoes partial oxidation to form two molecules of pyruvic "
    "acid</b>."))
story.append(body(
    "<b>In plants, this glucose is derived from sucrose</b>, which is the <b>end product of "
    "photosynthesis</b>, or <b>from storage carbohydrates</b>. <b>Sucrose is converted into "
    "glucose and fructose by the enzyme, invertase</b>, and <b>these two monosaccharides "
    "readily enter the glycolytic pathway</b>. <b>Glucose and fructose are phosphorylated to "
    "give rise to glucose-6-phosphate by the activity of the enzyme hexokinase</b>. This "
    "<b>phosphorylated form of glucose then isomerises to produce fructose-6-phosphate</b>. "
    "<b>Subsequent steps of metabolism of glucose and fructose are same.</b>"))
story.append(heading("12.2a", "The Ten Reactions, Step by Step", 3))
story.append(body(
    "In glycolysis, <b>a chain of ten reactions, under the control of different enzymes</b>, "
    "takes place to <b>produce pyruvate from glucose</b>."))
story.append(process_flow([
    "<b>Glucose (6C)</b> is phosphorylated to <b>glucose-6-phosphate (6C)</b> by "
    "<b>hexokinase</b> - <b>ATP is utilised</b> here (first of the two ATP-spending steps) and "
    "<b>ADP</b> is released.",
    "<b>Glucose-6-phosphate isomerises to fructose-6-phosphate (6C)</b>.",
    "<b>Fructose 6-phosphate to fructose 1,6-bisphosphate (6C)</b> - the <b>second step at "
    "which ATP is utilised</b>.",
    "The <b>fructose 1,6-bisphosphate is split</b> into the two <b>triose phosphates</b>: "
    "<b>dihydroxyacetone phosphate (3C)</b> and <b>3-phosphoglyceraldehyde, PGAL</b> - also "
    "written <b>glyceraldehyde-3-phosphate (3C)</b>.",
    f"<b>PGAL to 1,3-bisphosphoglycerate (BPGA)</b>: this is the <b>one step where {NADH} is "
    f"formed from {NADp}</b>. <b>Two redox-equivalents are removed (in the form of two "
    f"hydrogen atoms) from PGAL and transferred to a molecule of {NADp}</b>; <b>PGAL is "
    "oxidised and with inorganic phosphate to get converted into BPGA</b>. As a <b>triose "
    "bisphosphate</b>, BPGA is the <b>1,3-bisphosphoglyceric acid (3C)</b> of the chart.",
    "<b>BPGA to 3-phosphoglyceric acid (PGA)</b> - the <b>triose phosphate 3-phosphoglyceric "
    "acid (3C)</b>. This is <b>also an energy yielding process</b>; <b>this energy is trapped "
    "by the formation of ATP</b>.",
    "<b>PGA to 2-phosphoglycerate</b>.",
    f"<b>2-phosphoglycerate loses {H2O}</b> to give <b>phosphoenolpyruvate (PEP)</b>.",
    "<b>Another ATP is synthesised during the conversion of PEP to pyruvic acid</b>.",
    "<b>Pyruvic acid (3C)</b> is then the <b>key product of glycolysis</b>.",
]))
story.append(gap())
story.append(body(
    "<b>What is the metabolic fate of pyruvate? This depends on the cellular need.</b> There "
    "are <b>three major ways in which different cells handle pyruvic acid produced by "
    "glycolysis</b>."))
story.append(data_table([
    ["Fate of pyruvic acid", "Conditions", "Outcome"],
    ["<b>Lactic acid fermentation</b>", "<b>Anaerobic</b>",
     "<b>Incomplete oxidation</b>; pyruvic acid is reduced to <b>lactic acid</b>"],
    ["<b>Alcoholic fermentation</b>", "<b>Anaerobic</b>",
     f"<b>Incomplete oxidation</b>; pyruvic acid is converted to {CO2} and <b>ethanol</b>"],
    ["<b>Aerobic respiration</b>", f"<b>Requires {O2} supply</b>",
     f"<b>Complete oxidation of glucose to {CO2} and {H2O}</b> through <b>Krebs' cycle</b>"],
], col_widths=[3.4, 3.0, 6.4]))
story.append(gap())
story.append(body(
    "<b>Fermentation takes place under anaerobic conditions in many prokaryotes and "
    "unicellular eukaryotes.</b> For the <b>complete oxidation of glucose</b> to "
    f"{CO2} and {H2O}, however, <b>organisms adopt Krebs' cycle which is also called as "
    f"aerobic respiration</b>. <b>This requires {O2} supply.</b>"))
story.append(gap(6))

# LAYOUT: Fig 12.1 stands alone and is sized to FILL the page it closes (SS12.2).
# The two plates used to be paired into one row purely to avoid wasting a column; that
# forced both onto the following page and left the glycolysis chart at a cramped 6.6 cm.
# Unpaired, 12.1 is HEIGHT-limited, not width-limited: the page has 17.69 cm free below
# the pyruvate-fate table, the full-column caption costs 2.65 cm and the frame padding
# 0.35 cm, leaving 14.4 cm of picture. At AR 0.556 that is 8.0 cm wide - still inside the
# 8.54 cm natural width, so the chart is scaled up to fill the page with NO upscaling past
# the 300 dpi cap. Numbers + reasoning: figure_layout_decisions.md SS1-SS2.
story.append(figure(
    "fig_12_1.png",
    "Fig. 12.1 - Steps of glycolysis. The chart runs from <b>Glucose (6C)</b> down through "
    "<b>Glucose-6-phosphate (6C)</b> and <b>Fructose-6-phosphate (6C)</b> - each of the "
    "first two steps spending one <b>ATP</b> and releasing <b>ADP</b> - to <b>Fructose "
    "1,6-bisphosphate (6C)</b>, which splits into the <b>Triose phosphate dihydroxyacetone "
    "phosphate (3C)</b> and the <b>Triose phosphate glyceraldehyde-3-phosphate (3C)</b>. The "
    f"latter, with {NADp} reduced to {NADH}, becomes the <b>Triose bisphosphate "
    "1,3-bisphosphoglyceric acid (3C)</b>, then the <b>Triose phosphate 3-phosphoglyceric "
    f"acid (3C)</b>, then <b>2-phosphoglycerate</b>, which loses {H2O} to give "
    "<b>phosphoenolpyruvate</b> and finally <b>Pyruvic acid (3C)</b>.",
    max_width_cm=8.0))

# LAYOUT: Fig 12.2 keeps its place in the reading order - it illustrates the pyruvate
# branch point the paragraph above names, and introduces SS12.3 overleaf. Enlarged
# (operator instruction, this revision) to spend the space vacated on page 4 by moving
# SS12.4 to page 5 - sized to fill that gap WITHOUT overflowing the page. The asset was
# re-rendered at higher DPI (PR #192), so its 300 dpi natural width is now 12.68 cm and
# this display width is still a DOWNWARD move: the no-upscale cap stays untouched.
story.append(figure(
    "fig_12_2.png",
    "Fig. 12.2 - Major pathways of anaerobic respiration. <b>Glucose</b> passes through "
    "<b>Glyceraldehyde 3-phosphate</b>, <b>3-phosphoglyceric acid</b> and <b>phosphoenol "
    "pyruvic acid</b> to <b>Pyruvic acid</b>, which then branches either to <b>Lactic acid</b> "
    f"or to <b>Ethanol</b> plus {CO2}. {NADp} and {NADH} are shown being interconverted "
    "along the pathway, since the reducing power taken out of the sugar is handed back at the "
    "branch.",
    max_width_cm=11.0))

# ======================================================================================
# ---- 12.3 Fermentation ---- F063-F075
# ======================================================================================
story.append(heading("12.3", "Fermentation", 1))
story.append(body(
    "In fermentation, <b>say by yeast</b>, the <b>incomplete oxidation of glucose is achieved "
    f"under anaerobic conditions</b> by <b>sets of reactions where pyruvic acid is converted "
    f"to {CO2} and ethanol</b>. The <b>enzymes, pyruvic acid decarboxylase and alcohol "
    "dehydrogenase catalyse these reactions</b>."))
story.append(b1(
    "<b>Other organisms like some bacteria produce lactic acid from pyruvic acid.</b>"))
story.append(b1(
    "<b>In animal cells also, like muscles during exercise</b>, when <b>oxygen is inadequate "
    "for cellular respiration</b> <b>pyruvic acid is reduced to lactic acid by lactate "
    "dehydrogenase</b>."))
story.append(b1(
    f"<b>The reducing agent is {NADH}</b>, which is <b>reoxidised to {NADp} in both the "
    "processes</b>."))
story.append(heading("12.3a", "Why Fermentation Is a Poor Deal", 3))
story.append(b1(
    "<b>Less than seven per cent of the energy in glucose is released</b>, and <b>not all of "
    "it is trapped as high energy bonds of ATP</b>."))
story.append(b1(
    "Also, <b>the processes are hazardous - either acid or alcohol is produced</b>."))
story.append(b1(
    "<b>Yeasts poison themselves to death when the concentration of alcohol reaches about 13 "
    "per cent.</b>"))
story.append(note(
    "<b>Where fermentation happens:</b> under <b>anaerobic conditions in many prokaryotes, "
    "unicellular eukaryotes and in germinating seeds</b>."))
story.append(heading("12.3b", "The Aerobic Alternative", 3))
story.append(keyterm(
    "<b>Aerobic respiration:</b> the process that leads to a <b>complete oxidation of organic "
    f"substances in the presence of oxygen</b>, and <b>releases {CO2}, water and a large "
    "amount of energy present in the substrate</b>."))
story.append(body(
    "<b>This type of respiration is most common in higher organisms.</b> <b>In eukaryotes "
    f"these steps take place within the mitochondria and this requires {O2}.</b>"))

# ======================================================================================
# ---- 12.4 Aerobic Respiration ---- F078-F087
# ======================================================================================
# LAYOUT (operator instruction, this revision): SS12.4 previously started at the
# bottom of page 4 (heading + intro + step 1) and its process-flow split onto
# page 5. The whole block now opens page 5 intact; the space it vacated on page 4
# is spent enlarging Fig 12.2 (see the Fig 12.2 LAYOUT note above).
story.append(PageBreak())
story.append(heading("12.4", "Aerobic Respiration", 1))
story.append(body(
    "For aerobic respiration to take place <b>within the mitochondria</b>, the <b>final product "
    "of glycolysis, pyruvate is transported from the cytoplasm into the mitochondria</b>. Two "
    "crucial events then follow:"))
story.append(process_flow([
    "<b>The complete oxidation of pyruvate</b> by the <b>stepwise removal of all the hydrogen "
    f"atoms</b>, <b>leaving three molecules of {CO2}</b>. This <b>first process takes place in "
    "the matrix of the mitochondria</b>.",
    f"<b>The passing on of the electrons removed as part of the hydrogen atoms to molecular "
    f"{O2} with simultaneous synthesis of ATP</b>. This <b>second process is located on the "
    "inner membrane of the mitochondria</b>.",
]))
story.append(gap())
story.append(body(
    "<b>Pyruvate, which is formed by the glycolytic catabolism of carbohydrates in the "
    "cytosol</b>, after it <b>enters mitochondrial matrix undergoes oxidative decarboxylation "
    "by a complex set of reactions catalysed by pyruvic dehydrogenase</b>. These reactions "
    f"<b>require the participation of several coenzymes, including {NADp} and Coenzyme A</b>:"))
story.append(body(
    "<b>Pyruvic acid + CoA + NAD<super>+</super></b> (with <b>Mg<super>2+</super></b> and "
    "<b>pyruvate dehydrogenase</b>) <b>yields Acetyl CoA + CO<sub>2</sub> + NADH + "
    "H<super>+</super></b>"))
story.append(body(
    "During this process, <b>two molecules of NADH are produced from the metabolism of two "
    "molecules of pyruvic acid</b> (produced from <b>one glucose molecule during "
    "glycolysis</b>). The <b>acetyl CoA then enters a cyclic pathway, tricarboxylic acid "
    "cycle</b>, <b>more commonly called as Krebs' cycle after the scientist Hans Krebs who "
    "first elucidated it</b>."))

# ======================================================================================
# ---- 12.4.1 Tricarboxylic Acid Cycle ---- F088-F100, and Fig 12.3 (F101-F102)
# ======================================================================================
story.append(heading("12.4.1", "Tricarboxylic Acid Cycle", 2))
story.append(process_flow([
    "The <b>TCA cycle starts with the condensation of acetyl group with oxaloacetic acid (OAA) "
    "and water to yield citric acid</b>. The reaction is <b>catalysed by the enzyme citrate "
    "synthase</b> and <b>a molecule of CoA is released</b>.",
    "<b>Citrate is then isomerised to isocitrate.</b>",
    "It is followed by <b>two successive steps of decarboxylation</b>, leading to the formation "
    "of <b>alpha-ketoglutaric acid</b> and then <b>succinyl-CoA</b>.",
    "<b>During the conversion of succinyl-CoA to succinic acid a molecule of GTP is "
    "synthesised. This is a substrate level phosphorylation.</b> In a <b>coupled reaction GTP "
    "is converted to GDP with the simultaneous synthesis of ATP from ADP</b>.",
    "In the <b>remaining steps of citric acid cycle, succinyl-CoA is oxidised to OAA allowing "
    "the cycle to continue</b>.",
], cyclic=True))
story.append(gap())
story.append(b1(
    f"There are <b>three points in the cycle where {NADp} is reduced to {NADH}</b> and "
    f"<b>one point where {FADp} is reduced to {FADH2}</b>."))
story.append(b1(
    "The <b>continued oxidation of acetyl CoA via the TCA cycle requires the continued "
    "replenishment of oxaloacetic acid, the first member of the cycle</b>."))
story.append(b1(
    f"In addition it also <b>requires regeneration of {NADp} and {FADp} from NADH and "
    f"{FADH2} respectively</b>."))
story.append(gap())
story.append(body(
    "The <b>summary equation for this stage</b> of respiration, in the "
    "<b>mitochondrial matrix</b>, may thus be written as:"))
story.append(body(
    "<b>Pyruvic acid + 4NAD<super>+</super> + FAD<super>+</super> + 2H<sub>2</sub>O + ADP + "
    "P<sub>i</sub> yields 3CO<sub>2</sub> + 4NADH + 4H<super>+</super> + FADH<sub>2</sub> + "
    "ATP</b>"))
story.append(body(
    f"By the end of the cycle, <b>glucose has been broken down to release {CO2}</b> and "
    "<b>eight molecules of NADH + H<super>+</super> and two of FADH<sub>2</sub> have been "
    "synthesised</b>, <b>besides just two molecules of ATP in TCA cycle</b>."))
story.append(gap(6))

# LAYOUT: Fig 12.3 reduced from 9.0 cm to 8.2 cm (operator instruction, this revision)
# so the SS12.4.2 oxygen-role paragraph ("...oxygen acts as the final hydrogen
# acceptor") completes on the same page as Fig 12.3 instead of stranding its last line
# on the next page. Natural width is 8.54 cm, so 8.2 cm is a downward move and the
# no-upscale cap is untouched. It has no same-section neighbour to pair with - 12.2
# belongs to SS12.3 and 12.4 to SS12.4.2.
story.append(figure(
    "fig_12_3.png",
    "Fig. 12.3 - The Citric acid cycle. <b>Pyruvate (3C)</b> loses "
    f"{CO2} and, with <b>CoA</b> and {NADp} reduced to {NADH}, gives <b>Acetyl coenzyme A "
    "(2C)</b>, which condenses with <b>Oxaloacetic acid (4C)</b> to form <b>Citric acid "
    f"(6C)</b>. Around the ring, decarboxylations give <b>alpha-ketoglutaric acid (5C)</b> and "
    f"then, via <b>Succinic acid (4C)</b> - the step in which <b>GDP</b> becomes <b>GTP</b> - "
    f"and <b>Malic acid (4C)</b>, the cycle returns to oxaloacetic acid. {FADp} to "
    f"{FADH2} marks the single flavin-linked oxidation.",
    max_width_cm=8.2))

# ======================================================================================
# ---- 12.4.2 Electron Transport System (ETS) and Oxidative Phosphorylation ----
# ---- F103-F123, and Fig 12.4 / Fig 12.5 (F124-F127)
# ======================================================================================
story.append(heading("12.4.2", "Electron Transport System (ETS) and Oxidative Phosphorylation", 2))
story.append(body(
    "The <b>following steps in the respiratory process are to release and utilise the energy "
    f"stored in {NADH} and {FADH2}</b>. This is <b>accomplished when they are oxidised through "
    f"the electron transport system and the electrons are passed on to {O2} resulting in the "
    f"formation of {H2O}</b>."))
story.append(keyterm(
    "<b>Electron transport system (ETS):</b> the <b>metabolic pathway through which the "
    "electron passes from one carrier to another</b>. It is <b>present in the inner "
    "mitochondrial membrane</b>."))
story.append(process_flow([
    f"<b>Electrons from NADH produced in the mitochondrial matrix during citric acid cycle</b> "
    "are <b>oxidised by an NADH dehydrogenase (complex I)</b>, and electrons are then "
    "<b>transferred to ubiquinone located within the inner membrane</b>.",
    f"<b>Ubiquinone also receives reducing equivalents via {FADH2} (complex II)</b> that is "
    "<b>generated during oxidation of succinate in the citric acid cycle</b>.",
    "The <b>reduced ubiquinone (ubiquinol) is then oxidised with the transfer of electrons to "
    "cytochrome c via cytochrome bc<sub>1</sub> complex (complex III)</b>.",
    "<b>Cytochrome c is a small protein attached to the outer surface of the inner "
    "membrane</b> and <b>acts as a mobile carrier for transfer of electrons between complex "
    "III and IV</b>.",
    "<b>Complex IV refers to cytochrome c oxidase complex containing cytochromes a and "
    "a<sub>3</sub>, and two copper centres.</b>",
    "When the electrons <b>pass from one carrier to another via complex I to IV in the electron "
    "transport chain</b>, they are <b>coupled to ATP synthase (complex V) for the production of "
    "ATP from ADP and inorganic phosphate</b>.",
]))
story.append(gap())
story.append(body(
    "<b>The number of ATP molecules synthesised depends on the nature of the electron "
    "donor.</b>"))
story.append(data_table([
    ["Electron donor oxidised", "ATP produced"],
    [f"<b>One molecule of NADH</b>", "<b>3 molecules of ATP</b>"],
    [f"<b>One molecule of {FADH2}</b>", "<b>2 molecules of ATP</b>"],
], col_widths=[6.0, 6.0]))
story.append(gap())
story.append(body(
    "Although the <b>aerobic process of respiration takes place only in the presence of "
    "oxygen</b>, the <b>role of oxygen is limited to the terminal stage of the process</b>. "
    "Yet <b>the presence of oxygen is vital, since it drives the whole process by removing "
    "hydrogen from the system</b>: <b>oxygen acts as the final hydrogen acceptor</b>."))
story.append(keyterm(
    "<b>Oxidative phosphorylation:</b> <b>unlike photophosphorylation where it is the light "
    "energy that is utilised for the production of proton gradient required for "
    "phosphorylation, in respiration it is the energy of oxidation-reduction utilised for the "
    "same process</b>. <b>It is for this reason that the process is called oxidative "
    "phosphorylation.</b>"))
# [VERIFICATION FIX D2] Pass 3(b) direction 2 found the NCERT sentence tying oxidative
# phosphorylation to the chemiosmotic hypothesis (source p8, lines ~414-424) missing from
# the freeze AND from this block (new row F117a). It names a real, NEET-examinable process
# ("chemiosmotic hypothesis") and belongs in source order between F117 (oxidative
# phosphorylation) and F118 (energy released -> ATP synthase), so it is restored here.
story.append(body(
    "<b>You have already studied about the mechanism of membrane-linked ATP synthesis as "
    "explained by the chemiosmotic hypothesis in the earlier chapter.</b>"))
story.append(heading("12.4.2a", "ATP Synthase - the F<sub>1</sub>/F<sub>0</sub> Machine", 3))
story.append(body(
    "The <b>energy released during the electron transport system is utilised in synthesising "
    "ATP with the help of ATP synthase (complex V)</b>. <b>This complex consists of two major "
    "components, F<sub>1</sub> and F<sub>0</sub>.</b>"))
story.append(b1(
    "The <b>F<sub>1</sub> headpiece is a peripheral membrane protein complex</b> and "
    "<b>contains the site for synthesis of ATP from ADP and inorganic phosphate</b>."))
story.append(b1(
    "<b>F<sub>0</sub> is an integral membrane protein complex that forms the channel through "
    "which protons cross the inner membrane</b>."))
story.append(b1(
    "The <b>passage of protons through the channel is coupled to the catalytic site of the "
    "F<sub>1</sub> component for the production of ATP</b>."))
story.append(b1(
    "<b>For each ATP produced, 4H<super>+</super> pass through F<sub>0</sub> from the "
    "intermembrane space to the matrix down the electrochemical proton gradient.</b>"))
story.append(gap(6))

# LAYOUT: Fig 12.4 (AR 0.595) at 8.4 cm paired with Fig 12.5 (AR 1.079) at 7.6 cm - both
# belong to SS12.4.2, so the pair displaces nothing. At full column width 12.4 would render
# ~29 cm tall (taller than the whole text column) and even at its 9.75 cm natural width it
# costs 16.4 cm while leaving ~8 cm of column empty. See figure_layout_decisions.md SS1-SS2.
#
# ENLARGEMENT (operator instruction, this revision): 12.4 was 7.0 cm. SS12.5 no longer
# trails this plate on page 7 (see the PageBreak below), and that vacated ~2.4 cm of column
# height is spent here: 8.4 cm renders 12.4 at ~14.1 cm tall, filling the page without
# overflow. Fig 12.5 is deliberately left at 7.6 cm because its 300 dpi natural width is
# only 6.67 cm - _panel() already clamps it there, so any larger request would upscale past
# 300 dpi. The pair therefore grows on the 12.4 side only; row width is ~16.1 cm of 18 cm.
# [VERIFICATION FIX F125] Fig 12.4 caption re-read against the plate. The old caption
# named "Complex V" (not on the plate - it reads F0 / F1 ATP synthase) and paraphrased the
# plate's literal carriers ("ubiquinone" for UQ/UQH2, FADH2 for FAD, "inorganic phosphate"
# for Pi). The caption is rewritten to transcribe the plate's actual labels - FMN, Fe-S,
# 2e-, UQ/UQH2, FAD, succinate/fumarate, the Cyt b / Cyt c1 / Cyt c chain, Cu_A / Cyta /
# Cyta3 / Cu_B, the 4H+/4H+/2H+ pumping stoichiometry, and F0 / F1 ATP synthase / ADP + Pi
# - so every label catalogued in inventory row F125 (F125a..) traces to running text.
# [VERIFICATION FIX F127] Fig 12.5 caption: "intermembrane space" corrected to the plate's
# literal "Outer side", and the "electrochemical proton gradient" phrase (a Fig 12.4 label,
# not on the 12.5 plate) removed.
story.append(figure_pair(
    ("fig_12_4.png",
     "Fig. 12.4 - Electron Transport System (ETS). The carriers sit in the <b>inner "
     "mitochondrial membrane</b> between the <b>inter-membrane space</b> and the <b>matrix</b>. "
     f"At <b>Complex I (NADH dehydrogenase)</b>, <b>{NADH}</b> is oxidised to <b>{NADp}</b>, "
     "handing <b>2e<super>-</super></b> to <b>FMN</b> and the <b>Fe-S</b> centres while "
     "<b>4H<super>+</super></b> are pumped out; the electrons pass to <b>UQ</b>, which becomes "
     "<b>UQH<sub>2</sub></b>. At <b>Complex II (Succinate dehydrogenase)</b>, <b>succinate</b> "
     f"is oxidised to <b>fumarate</b> via <b>FAD</b> and Fe-S, also reducing UQ. <b>Complex III "
     "(Cytochrome bc<sub>1</sub>)</b> passes electrons through <b>Cyt b</b>, Fe-S and "
     "<b>Cyt c<sub>1</sub></b> to <b>Cyt c</b>, pumping a further <b>4H<super>+</super></b>. "
     "<b>Complex IV (Cytochrome c oxidase)</b> carries them through <b>Cu<sub>A</sub></b>, "
     f"<b>Cyta</b>, <b>Cyta<sub>3</sub></b> and <b>Cu<sub>B</sub></b>, reducing <b>{O2}</b> with "
     f"<b>2H<super>+</super></b> to <b>{H2O}</b>. The protons return through <b>F<sub>0</sub></b> "
     "and drive <b>F<sub>1</sub> ATP synthase</b> down the <b>electrochemical gradient</b>, "
     "making <b>ATP</b> from <b>ADP + P<sub>i</sub></b>.",
     8.4),
    ("fig_12_5.png",
     "Fig. 12.5 - Diagramatic presentation of ATP synthesis in mitochondria. The "
     "<b>F<sub>1</sub></b> headpiece projects into the <b>matrix</b> and carries the site where "
     "<b>ADP</b> and <b>P<sub>i</sub></b> are joined into <b>ATP</b>; "
     "<b>F<sub>0</sub></b> is the channel through the <b>inner mitochondrial membrane</b> "
     "through which <b>4H<super>+</super></b> return from the <b>outer side</b> for every ATP "
     "made.",
     7.6)))

# ======================================================================================
# ---- 12.5 The Respiratory Balance Sheet ---- F128-F138
# ======================================================================================
# LAYOUT (operator instruction, this revision): SS12.5 previously began at the foot of
# page 7, directly under the Fig 12.4 / Fig 12.5 plate - the section banner plus its
# opening paragraph were stranded there while the assumptions list and the balance sheet
# carried over to page 8. An explicit PageBreak now opens the whole SS12.5 block on
# page 8, and the column height it vacates on page 7 is spent enlarging Fig 12.4 (see the
# ENLARGEMENT note above). Page 8 has the slack to absorb the moved heading, so the
# chapter still ends at 10 pages and pages 9-10 are untouched.
story.append(PageBreak())
story.append(heading("12.5", "The Respiratory Balance Sheet", 1))
story.append(body(
    "It is <b>possible to make calculations of the net gain of ATP for every glucose molecule "
    "oxidised</b>; but <b>in reality this can remain only a theoretical exercise</b>. The "
    "calculations can be made only on <b>certain assumptions</b>:"))
story.append(b1(
    "<b>There is a sequential, orderly pathway functioning, with one substrate forming the next "
    "and with glycolysis, TCA cycle and ETS pathway following one after another.</b>"))
story.append(b1(
    "<b>The NADH synthesised in glycolysis is transferred into the mitochondria and undergoes "
    "oxidative phosphorylation.</b>"))
story.append(b1(
    "<b>None of the intermediates in the pathway are utilised to synthesise any other "
    "compound.</b>"))
story.append(b1(
    "<b>Only glucose is being respired - no other alternative substrates are entering in the "
    "pathway at any of the intermediary stages.</b>"))
story.append(note(
    "<b>None of these assumptions is strictly valid in a living system:</b> <b>all pathways "
    "work simultaneously and do not take place one after another; substrates enter the pathways "
    "and are withdrawn from it as and when necessary; ATP is utilised as and when needed; "
    "enzymatic rates are controlled by multiple means.</b>"))
story.append(body(
    "With the assumptions above, <b>there can be a net gain of 38 ATP molecules during aerobic "
    "respiration of one molecule of glucose</b>."))
story.append(heading("12.5a", "Fermentation vs Aerobic Respiration", 3, has_table=True))
story.append(data_table([
    ["Point of difference", "Fermentation", "Aerobic respiration"],
    ["<b>Extent of breakdown</b>",
     "Accounts for <b>only a partial breakdown of glucose</b>",
     f"Glucose is <b>completely degraded to {CO2} and {H2O}</b>"],
    ["<b>Net ATP gain</b>",
     "<b>Net gain of only two molecules of ATP for each molecule of glucose degraded to "
     "pyruvic acid</b>",
     "<b>Many more molecules of ATP are generated under aerobic conditions</b>"],
    [f"<b>Oxidation of NADH to {NADp}</b>",
     "<b>Rather slow</b>", "<b>Very vigorous</b>"],
], col_widths=[3.2, 5.0, 5.0]))

# ======================================================================================
# ---- 12.6 Amphibolic Pathway ---- F139-F149, and Fig 12.6 (F150-F151)
# ======================================================================================
story.append(heading("12.6", "Amphibolic Pathway", 1))
story.append(body(
    "<b>Glucose is the favoured substrate for respiration.</b> <b>All carbohydrates are usually "
    "first converted into glucose before they are used for respiration.</b> <b>Other substrates "
    "can also be respired</b>, as has been mentioned earlier, <b>but then they do not enter the "
    "respiratory pathway at the first step</b>."))
story.append(data_table([
    ["Substrate", "Broken down first into", "Enters the respiratory pathway as"],
    ["<b>Fats</b>", "<b>Glycerol and fatty acids</b>",
     "<b>Fatty acids</b> would <b>first be degraded to acetyl CoA</b> and enter the pathway; "
     "<b>glycerol would enter the pathway after being converted to PGAL</b>"],
    ["<b>Proteins</b>", "<b>Individual amino acids, by proteases</b>",
     "The amino acids, <b>after deamination</b>, <b>depending on their structure would enter "
     "the pathway at some stage within the Krebs' cycle or even as pyruvate or acetyl CoA</b>"],
], col_widths=[2.2, 4.0, 7.0]))
story.append(gap())
# [VERIFICATION FIX D3] Pass 3(b) direction 2 found the NCERT sentence that generalises
# the withdrawal/synthesis link beyond fatty acids to proteins (source p10, lines ~502-514)
# missing from the freeze AND from this block, which covered only the fatty-acid case
# (new row F147a). NCERT: "Similarly, during breakdown and synthesis of protein too,
# respiratory intermediates form the link."
story.append(body(
    "Since <b>respiration involves breakdown of substrates, the respiratory process has "
    "traditionally been considered a catabolic process and the respiratory pathway as a "
    "catabolic pathway</b>. But the same intermediates are also drawn off for synthesis: "
    "<b>when the organism needs to synthesise fatty acids, acetyl CoA would be withdrawn from "
    "the respiratory pathway for it</b>. <b>Similarly, during breakdown and synthesis of "
    "protein too, respiratory intermediates form the link.</b>"))
story.append(keyterm(
    "<b>Catabolism and anabolism:</b> <b>breaking down processes within the living organism is "
    "catabolism, and synthesis is anabolism</b>."))
story.append(keyterm(
    "<b>Amphibolic pathway:</b> <b>because the respiratory pathway is involved in both "
    "anabolism and catabolism, it would hence be better to consider the respiratory pathway as "
    "an amphibolic pathway rather than as a catabolic one</b>."))
story.append(gap(6))

# LAYOUT: Fig 12.6 at 12.5 cm. Landscape plate (AR 1.288) whose 16.63 cm natural width
# exceeds the 18 cm column only slightly; rendered at 12.5 cm it is ~9.7 cm tall and its
# width is already doing the work, so it is not paired.
# [VERIFICATION FIX D4] Pass 3(b) figure re-read found the old caption fabricated "arrows
# drawn both ways" for the whole plate. The plate has exactly ONE bidirectional arrow
# (dihydroxy acetone phosphate <-> glyceraldehyde 3-phosphate); every other arrow is
# one-way into the pathway. Caption rewritten to state the true arrow pattern.
story.append(figure(
    "fig_12_6.png",
    "Fig. 12.6 - Interrelationship among metabolic pathways showing respiration mediated "
    f"breakdown of different organic molecules to {CO2} and {H2O}. <b>Fats</b>, "
    "<b>Carbohydrates</b> and <b>Proteins</b> enter from the top as <b>fatty acids</b> and "
    "<b>glycerol</b>, <b>simple sugars e.g. glucose</b>, and <b>amino acids</b>. The sugar arm "
    "runs <b>glucose 6-phosphate</b> to <b>fructose 1,6 bisphosphate</b> to the trioses "
    "<b>dihydroxy acetone phosphate</b> and <b>glyceraldehyde 3-phosphate</b> and on to "
    "<b>pyruvic acid</b>; every arm converges on <b>acetyl CoA</b> and the <b>Krebs cycle</b>, "
    f"from which <b>{H2O}</b> and <b>{CO2}</b> leave. Every arrow runs one way into the "
    "pathway except the <b>dihydroxy acetone phosphate</b> to <b>glyceraldehyde 3-phosphate</b> "
    "step, which is the single reversible (two-way) arrow on the plate.",
    max_width_cm=12.5))

# ======================================================================================
# ---- 12.7 Respiratory Quotient ---- F152-F162
# ======================================================================================
story.append(heading("12.7", "Respiratory Quotient", 1))
# F153 is the source's transitional lead-in. It carries no biology, so it is set
# unbolded - the house rule is that bold marks NCERT substance, and bolding a pure
# navigation sentence would dilute that signal. It is written rather than dropped
# because the other nine opener rows are all present and a frozen row is never
# silently discarded; the only documented no-block row is F164 (see the docstring).
story.append(body("Let us now look at another aspect of respiration."))
story.append(keyterm(
    "<b>Respiratory quotient (RQ) or respiratory ratio:</b> the <b>ratio of the volume of "
    f"{CO2} evolved to the volume of {O2} consumed in respiration</b>."))
story.append(body(
    "<b>RQ = volume of CO<sub>2</sub> evolved / volume of O<sub>2</sub> consumed</b>"))
story.append(body(
    "<b>The respiratory quotient depends upon the type of respiratory substrate used during "
    "respiration.</b>"))
story.append(data_table([
    ["Respiratory substrate", "RQ", "Why"],
    ["<b>Carbohydrates</b> (completely oxidised)", "<b>1</b>",
     f"<b>Equal amounts of {CO2} and {O2} are evolved and consumed</b>, respectively: "
     "<b>RQ = 6CO<sub>2</sub> / 6O<sub>2</sub> = 1.0</b>"],
    ["<b>Fats</b>", "<b>Less than 1</b>",
     "For <b>tripalmitin</b>: <b>2(C<sub>51</sub>H<sub>98</sub>O<sub>6</sub>) + 145O<sub>2</sub> "
     "yields 102CO<sub>2</sub> + 98H<sub>2</sub>O + energy</b>, so "
     "<b>RQ = 102CO<sub>2</sub> / 145O<sub>2</sub> = 0.7</b>"],
    ["<b>Proteins</b>", "<b>About 0.9</b>",
     "<b>When proteins are respiratory substrates the ratio would be about 0.9.</b>"],
], col_widths=[3.6, 2.2, 7.4]))
story.append(gap())
story.append(note(
    "These clean values are <b>textbook cases</b>: <b>in living organisms, respiratory "
    "substrates are often more than one; pure proteins or fats are never used as respiratory "
    "substrates</b>."))
story.append(memory_aid(
    "RQ falls in the alphabetical order of the substrates - <b>C</b>arbohydrate 1.0, "
    "<b>P</b>rotein 0.9, <b>F</b>at 0.7 is not alphabetical, but <b>C &gt; P &gt; F</b> is: "
    "the more oxygen a substrate still needs, the lower its RQ, and fat is the most "
    "hydrogen-rich of the three."))

# ======================================================================================
# ---- Quick Recap (SS5 item 8) ---- F163
# ======================================================================================
story.append(heading("Recap", "Quick Recap", 1))
story.append(b1(
    "<b>Plants unlike animals have no special systems for breathing or gaseous exchange.</b> "
    "<b>Stomata and lenticels allow gaseous exchange by diffusion</b>, and <b>almost all living "
    "cells in a plant have their surfaces exposed to air</b>."))
story.append(b1(
    "<b>The breaking of C-C bonds of complex organic molecules by oxidation leading to the "
    "release of a lot of energy is called cellular respiration.</b> <b>Glucose is the favoured "
    "substrate for respiration; fats and proteins can also be broken down to yield energy.</b>"))
story.append(b1(
    "<b>The initial stage of cellular respiration takes place in the cytoplasm.</b> <b>Each "
    "glucose molecule is broken through a series of enzyme catalysed reactions into two "
    "molecules of pyruvic acid; this process is called glycolysis.</b>"))
story.append(b1(
    "<b>The fate of the pyruvate depends on the availability of oxygen and the organism.</b> "
    "<b>Under anaerobic conditions either lactic acid fermentation or alcohol fermentation "
    "occurs</b>, and <b>fermentation takes place in many prokaryotes, unicellular eukaryotes "
    "and in germinating seeds</b> - releasing <b>less than seven per cent</b> of the energy in "
    "glucose for a <b>net gain of two ATP</b>."))
story.append(b1(
    "<b>In eukaryotic organisms aerobic respiration occurs in the presence of oxygen.</b> "
    f"<b>Pyruvic acid is transported into the mitochondria where it is converted into acetyl "
    f"CoA with the release of {CO2}.</b> <b>Acetyl CoA then enters the tricarboxylic acid "
    "pathway or Krebs' cycle operating in the matrix of the mitochondria.</b>"))
story.append(b1(
    f"<b>{NADH} and {FADH2} are generated in the Krebs' cycle.</b> <b>The energy in these "
    f"molecules as well as that in the {NADH} synthesised during glycolysis are used to "
    "synthesise ATP.</b>"))
story.append(b1(
    "<b>This is accomplished through a system of electron carriers called electron transport "
    "system (ETS) located on the inner membrane of the mitochondria.</b> <b>The electrons, as "
    "they move through the system, release enough energy that are trapped to synthesise ATP; "
    f"this is called oxidative phosphorylation.</b> <b>In this process {O2} is the ultimate "
    "acceptor of electrons and it gets reduced to water.</b> Net theoretical yield: <b>38 "
    "ATP</b> per glucose."))
story.append(b1(
    "<b>The respiratory pathway is an amphibolic pathway as it involves both anabolism and "
    "catabolism.</b> <b>The respiratory quotient depends upon the type of respiratory substance "
    "used during respiration</b> - <b>1</b> for carbohydrates, <b>0.7</b> for fats "
    "(tripalmitin) and <b>about 0.9</b> for proteins."))


if __name__ == "__main__":
    sys.exit(build_pdf(
        OUT_PDF, story,
        title="Class 11 Chapter 12 - Respiration in Plants (NEET notes)",
        subject="NEET Biology"))
