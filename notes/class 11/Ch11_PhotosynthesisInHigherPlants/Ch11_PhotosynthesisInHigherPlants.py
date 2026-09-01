"""
NCERT Class 11 Biology, Chapter 11 - Photosynthesis in Higher Plants
NEET replacement notes -> A4 print-ready PDF.

Built under SUPREME COMMAND PROMPT.md v6, Pass 2: written linearly from the
frozen 282-row inventory (Ch11_PhotosynthesisInHigherPlants_inventory.md),
importing the repo-level frozen style module `neet_template.py` (v6 SS0.6).
No style, geometry, colour or font is re-declared here.

Block markers `# ---- N.N ----` mark every NCERT section so a Pass 3 flag can be
found and fixed in one contiguous block. Inventory row IDs are named in the
comments so any fact can be traced back to its frozen row.

Pass 1 carry-overs actioned (inventory "Carry-over for Pass 2"):
  1. The 4 exercise-gap items (Ex. 1, 5, 6, 7) are the ONLY appendix content.
  2. Fig 11.3a / 11.3c captions state the pigment identities and the
     rate-vs-absorption pairing in words (colour-carried distinction, SS4.4 3(f)).
  3. Melvin Calvin profile is text-only (F004-F010, F246); no headshot.
  4. Table 11.1 is reproduced as a COMPLETED comparison table plus NCERT's own
     "Choose from" option lists (F185, F186, F187), keeping the NCERT number.
  5. CO2 / H+ / NADP+ / O2 / HCO3- / C3 / C4 use <sub>/<super>, never Unicode.

Operator deviation for this build (session-level instruction, recorded here and
in the inventory Coverage section, never in the PDF - Rule 6):
  * Figure 11.1 ("Priestley's experiment") is NOT embedded, and its four
    inventory labels (F271: the bare panel markers "(a)", "(b)", "(c)", "(d)")
    are NOT written into running text as figure labels. The Priestley experiment
    itself is unaffected - every fact of it survives in F024-F029 in SS11.2.
    Figure 11.1 is a deliberate operator omission, NOT an extraction failure, so
    it is NOT flagged in the PDF under "Figures requiring manual attention"
    (that heading is reserved for figures that could not be extracted).
    The general rule this instantiates is the "third state" bullet at SS4.4 Step 3
    of the SUPREME COMMAND PROMPT: a figure is either embedded, or failed
    extraction (flagged in the PDF), or deliberately omitted by operator decision
    (documented in the inventory Coverage section and NOT flagged). 12 assets are
    extracted for this chapter; 11 are embedded.
  * Figures 11.3a and 11.3b are stacked horizontally side by side, with Figure
    11.3c below them, each part carrying its own caption.
  * Exercises: the appendix answers ONLY the 4 exercise-gap items (Ex. 1, 5, 6, 7).
    The other 5 of the 9 exercises are INTENTIONALLY left unanswered because the
    chapter body already teaches them - Rule 2 step 3 COVERED ("do not reproduce
    the question and do not write an answer"), confirmed by the operator. Read as:
    9 exercises = 4 answered by design + 5 unanswered by design + 0 overlooked.
  * Figures 11.8, 11.9 and 11.10 render below full column width by operator order.
    11.8 and 11.9 are a pagination fix (SS11.8 was being torn across three pages by
    its own KeepTogether figure block); 11.10 is a plain size order. Each call site
    carries a `# LAYOUT` comment; the numbers, the budget and the verification are
    in figure_layout_decisions.md SS1-SS2 and SS5.

Every operator deviation above is recorded at repo level, not just here:
  - figure_layout_decisions.md            - full narrative, budget arithmetic, verification
  - <chapter>_inventory.md "Coverage"     - the SS7/Rule 6 audit home
  - figure_extraction_record.md           - "extracted but not embedded" for Fig 11.1
  - SUPREME COMMAND PROMPT.md SS4.4, Rule 2 - the durable rules these instantiate
  - CHAPTER_STATUS.md / CHAPTER_TRACKER.md  - chapter-level status entries

Source: Chapter/class 11/Chapter 11 - Photosynthesis in Higher Plants.pdf
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
    Paragraph, Spacer, Image, Table, TableStyle, KeepTogether,
)
from reportlab.lib.units import cm  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch11_PhotosynthesisInHigherPlants.pdf")


def figure(asset_name, caption_text, max_width_cm=15.9):
    """Chapter-local binding of the shared figure() helper (SS0.6)."""
    return _shared_figure(asset_name, caption_text, ASSETS, max_width_cm=max_width_cm)


def _panel(asset_name, caption_text, width_cm):
    """One framed figure panel + its own caption, as a single-column Table.

    Used only to place Figure 11.3's parts (a) and (b) side by side, per the
    session instruction. Framing (0.5pt GRID_LINE box, 5pt padding), the
    monochrome guard and the 300 dpi no-upscale cap are the same rules
    neet_template.figure() applies - nothing style-level is invented here.
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


def figure_pair(left_asset, left_caption, right_asset, right_caption, panel_cm=8.4):
    """Two figure panels side by side, each with its own caption, kept together."""
    left, lw = _panel(left_asset, left_caption, panel_cm)
    right, rw = _panel(right_asset, right_caption, panel_cm)
    row = Table([[left, right]], colWidths=[lw, rw])
    row.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (0, -1), 6),
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
# ---- Title block (SS5 item 1) ----
# ======================================================================================
story += title_block("Photosynthesis in Higher Plants")

# ======================================================================================
# ---- UNIT 4 PLANT PHYSIOLOGY - unit introduction (F220 heading; F001-F003) ----
# ======================================================================================
story.append(heading("Unit 4", "PLANT PHYSIOLOGY - Unit Introduction", 1))
# F001
story.append(body(
    "The description of the structure and variation of living organisms over a period of time "
    "ended up as <b>two apparently irreconcilable perspectives</b> on biology. The two rest on "
    "<b>two levels of organisation</b> of life forms and phenomena."))
# F002
story.append(data_table([
    ["Perspective", "Level of organisation described", "Disciplines it resulted in"],
    ["First", "Life at the <b>organismic and above</b> level",
     "<b>Ecology</b> and related disciplines"],
    ["Second", "Life at the <b>cellular and molecular</b> level",
     "<b>Physiology</b> and <b>biochemistry</b>"],
], col_widths=[1.6, 4.6, 3.8]))
story.append(gap())
# F003
story.append(body(
    "In this unit the processes of <b>photosynthesis</b>, <b>respiration</b> and <b>plant growth "
    "and development</b> are described in molecular terms, but in the context of cellular "
    "activities and even at organism level. The relation of the physiological processes to "
    "environment is also discussed."))

# ======================================================================================
# ---- Scientist profile: Melvin Calvin (F246 heading; F004-F010) - TEXT ONLY, no photo
# ======================================================================================
story.append(heading("Profile", "MELVIN CALVIN (1911-1997)", 2))
# F004, F005
story.append(b1(
    "<b>Melvin Calvin</b> was born in <b>Minnesota</b> in <b>April 1911</b>. He received his "
    "<b>Ph.D. in Chemistry</b> from the <b>University of Minnesota</b> and served as "
    "<b>Professor of Chemistry</b> at the <b>University of California, Berkeley</b>."))
# F006
story.append(b1(
    "Just after <b>world war II</b>, when the world was under shock after the "
    "<b>Hiroshima-Nagasaki bombings</b> and seeing the ill-effects of radio-activity, Calvin and "
    "co-workers put <b>radio-activity to beneficial use</b>."))
# F007
story.append(b1(
    "Calvin, along with <b>J.A. Bassham</b>, studied reactions in green plants forming sugar and "
    "other substances from raw materials like <b>carbon dioxide, water and minerals</b>, by "
    "<b>labelling the carbon dioxide with C<super>14</super></b>."))
# F008
story.append(b1(
    "Calvin proposed that plants change <b>light energy to chemical energy</b> by transferring an "
    "electron in an <b>organised array of pigment molecules</b> and other substances."))
# F009
story.append(b1(
    "The <b>mapping of the pathway of carbon assimilation</b> in photosynthesis earned Melvin "
    "Calvin the <b>Nobel Prize in 1961</b>."))
# F010
story.append(b1(
    "The principles of photosynthesis as established by Calvin are at present being used in "
    "studies on <b>renewable resource for energy and materials</b> and basic studies in "
    "<b>solar energy research</b>."))

# ======================================================================================
# ---- Chapter opener (F219 heading; F247 opener; F011-F017) ----
# ======================================================================================
story.append(heading("Ch 11", "PHOTOSYNTHESIS IN HIGHER PLANTS", 1))
# F247 (opener), F011
story.append(body(
    "<b>All animals including human beings depend on plants for their food.</b>"))
# F012, F013 - autotroph / heterotroph definitions
story.append(keyterm(
    "<b>Autotrophs</b> - green plants make, or rather <b>synthesise</b>, the food they need "
    "through photosynthesis, and are therefore called autotrophs. <b>Autotrophic nutrition is "
    "found only in plants</b>; all other organisms that depend on the green plants for food are "
    "<b>heterotrophs</b>."))
# F014
story.append(keyterm(
    "<b>Photosynthesis</b> - a <b>physico-chemical process</b> by which green plants use "
    "<b>light energy</b> to drive the <b>synthesis of organic compounds</b>."))
# F015
story.append(body(
    "Ultimately, <b>all</b> living forms on earth depend on sunlight for energy. The use of energy "
    "from sunlight by plants doing photosynthesis is <b>the basis of life on earth</b>."))
# F016 - the two reasons, both carried
story.append(body("Photosynthesis is important due to <b>two reasons</b>:"))
story.append(b1("It is the <b>primary source of all food on earth</b>."))
story.append(b1(
    "It is also responsible for the <b>release of oxygen into the atmosphere</b> by green plants."))
# F017
story.append(body(
    "This chapter focusses on the <b>structure of the photosynthetic machinery</b> and the various "
    "reactions that transform <b>light energy into chemical energy</b>."))

# ======================================================================================
# ---- 11.1 WHAT DO WE KNOW? (F221 heading; F248 opener; F018-F022; F267 fold) ----
# ======================================================================================
story.append(heading("11.1", "WHAT DO WE KNOW?", 1))
# F248 (opener), F018
story.append(body(
    "Simple experiments have shown that <b>chlorophyll</b> (green pigment of the leaf), "
    "<b>light</b> and <b>CO<sub>2</sub></b> are required for photosynthesis to occur."))
# F267 - SUMMARY-UNIQUE fold: the stomatal uptake route and the products named
story.append(body(
    "During photosynthesis <b>carbon dioxide from the atmosphere is taken in by leaves through "
    "stomata</b> and used for making carbohydrates, <b>principally glucose and starch</b>."))
story.append(gap())
# F019, F020 - the chlorophyll-and-light experiment
story.append(body("<b>Experiment 1 - is chlorophyll and light needed?</b>"))
story.append(process_flow([
    "Two leaves are used: a <b>variegated leaf</b>, or a leaf that was <b>partially covered with "
    "black paper</b>.",
    "Both are <b>exposed to light</b>.",
    "The leaves are then <b>tested for the presence of starch</b>.",
    "Result: photosynthesis occurred <b>only in the green parts of the leaves in the presence of "
    "light</b>.",
]))
story.append(gap())
# F021, F022 - the CO2 experiment
story.append(body("<b>Experiment 2 - is CO<sub>2</sub> needed?</b>"))
story.append(process_flow([
    "A part of a leaf is enclosed in a <b>test tube containing some KOH soaked cotton</b>, which "
    "<b>absorbs CO<sub>2</sub></b>.",
    "The <b>other half is exposed to air</b>.",
    "The setup is placed <b>in light</b> for some time, then tested for starch.",
    "Result: the <b>exposed part tested positive</b> for starch, while the portion inside the tube "
    "<b>tested negative</b> - showing that <b>CO<sub>2</sub> was required</b> for photosynthesis.",
]))

# ======================================================================================
# ---- 11.2 EARLY EXPERIMENTS (F222 heading; F249 opener; F023-F054) ----
# ======================================================================================
story.append(heading("11.2", "EARLY EXPERIMENTS", 1))
# F249 (opener), F023
story.append(body(
    "It is interesting to learn about those simple experiments that led to a <b>gradual "
    "development</b> in our understanding of photosynthesis."))

# ---- 11.2 Joseph Priestley (F024-F029) ----
story.append(heading("11.2a", "Joseph Priestley (1733-1804)", 3))
# F024, F025
story.append(b1(
    "In <b>1770</b> Joseph Priestley performed a series of experiments that revealed the "
    "<b>essential role of air</b> in the growth of green plants. Priestley <b>discovered oxygen "
    "in 1774</b>."))
# F026, F027, F028
story.append(process_flow([
    "Priestley observed that a <b>candle burning in a closed space</b> - a <b>bell jar</b> - soon "
    "gets extinguished.",
    "Similarly, a <b>mouse would soon suffocate</b> in a closed space.",
    "He concluded that a burning candle or an animal that breathe the air <b>both somehow damage "
    "the air</b>.",
    "When he placed a <b>mint plant</b> in the same bell jar, the <b>mouse stayed alive</b> and "
    "the <b>candle continued to burn</b>.",
]))
# F029
story.append(note(
    "<b>Priestley's hypothesis:</b> <i>Plants restore to the air whatever breathing animals and "
    "burning candles remove.</i>"))

# ---- 11.2 Jan Ingenhousz (F030-F032) ----
story.append(heading("11.2b", "Jan Ingenhousz (1730-1799)", 3))
# F030
story.append(b1(
    "Using a <b>similar setup</b> as the one used by Priestley, but by placing it <b>once in the "
    "dark and once in the sunlight</b>, Ingenhousz showed that <b>sunlight is essential</b> to the "
    "plant process that somehow <b>purifies the air</b> fouled by burning candles or breathing "
    "animals."))
# F031, F032
story.append(b1(
    "In an <b>elegant experiment with an aquatic plant</b> he showed that in <b>bright sunlight</b> "
    "<b>small bubbles</b> were formed around the <b>green parts</b>, while <b>in the dark they did "
    "not</b>. He later identified these bubbles to be of <b>oxygen</b>. He hence showed that it is "
    "<b>only the green part</b> of the plants that could release oxygen."))

# ---- 11.2 Julius von Sachs (F033-F036) ----
story.append(heading("11.2c", "Julius von Sachs (1854)", 3))
# F033, F034, F036
story.append(b1(
    "It was not until about <b>1854</b> that <b>Julius von Sachs</b> provided evidence for the "
    "<b>production of glucose</b> when plants grow. Glucose is <b>usually stored as starch</b>. "
    "Sachs found that the <b>green parts in plants</b> is where <b>glucose is made</b>, and that "
    "the glucose is usually stored as starch."))
# F035
story.append(b1(
    "His later studies showed that the <b>green substance</b> in plants (<b>chlorophyll</b> as we "
    "know it now) is located in <b>special bodies</b> (later called <b>chloroplasts</b>) within "
    "plant cells."))

# ---- 11.2 T.W Engelmann (F037-F040) ----
story.append(heading("11.2d", "T.W Engelmann (1843-1909)", 3))
# F037, F038, F039, F040
story.append(process_flow([
    "Using a <b>prism</b>, Engelmann <b>split light into its spectral components</b>.",
    "He then <b>illuminated a green alga</b>, <i>Cladophora</i>, placed in a <b>suspension of "
    "aerobic bacteria</b>.",
    "The <b>bacteria were used to detect the sites of O<sub>2</sub> evolution</b>.",
    "The bacteria <b>accumulated mainly in the region of blue and red light</b> of the split "
    "spectrum.",
    "A <b>first action spectrum of photosynthesis</b> was thus described; it resembles roughly the "
    "<b>absorption spectra of chlorophyll a and b</b>.",
]))

# ---- 11.2 The empirical equation (F041-F043) ----
story.append(heading("11.2e", "The First Empirical Equation", 3))
# F041
story.append(b1(
    "By the <b>middle of the nineteenth century</b> the key features of plant photosynthesis were "
    "known, namely that plants could use <b>light energy to make carbohydrates from "
    "CO<sub>2</sub> and water</b>."))
# F042, F043
story.append(b1(
    "The <b>empirical equation</b> representing the total process of photosynthesis for "
    "<b>oxygen evolving organisms</b> was then understood as: "
    "<b>CO<sub>2</sub> + H<sub>2</sub>O</b>, in the presence of <b>light</b>, yields "
    "<b>[CH<sub>2</sub>O] + O<sub>2</sub></b>. Here <b>[CH<sub>2</sub>O]</b> represented a "
    "<b>carbohydrate</b> (e.g., <b>glucose, a six-carbon sugar</b>)."))

# ---- 11.2 Cornelius van Niel (F044-F054) ----
story.append(heading("11.2f", "Cornelius van Niel (1897-1985)", 3))
# F044, F045
story.append(b1(
    "A <b>milestone contribution</b> to the understanding of photosynthesis was made by a "
    "<b>microbiologist, Cornelius van Niel</b>. Based on his studies of <b>purple and green "
    "bacteria</b>, he demonstrated that photosynthesis is essentially a <b>light-dependent "
    "reaction</b> in which <b>hydrogen from a suitable oxidisable compound reduces carbon dioxide "
    "to carbohydrates</b>."))
# F046
story.append(b1(
    "His finding can be expressed by: <b>2H<sub>2</sub>A + CO<sub>2</sub></b>, in the presence of "
    "<b>light</b>, yields <b>2A + CH<sub>2</sub>O + H<sub>2</sub>O</b>."))
# F047, F048, F049
story.append(b1(
    "In <b>green plants H<sub>2</sub>O is the hydrogen donor</b> and is <b>oxidised to "
    "O<sub>2</sub></b>. <b>Some organisms do not release O<sub>2</sub></b> during photosynthesis: "
    "when <b>H<sub>2</sub>S</b> instead is the hydrogen donor for <b>purple and green sulphur "
    "bacteria</b>, the 'oxidation' product is <b>sulphur or sulphate</b> depending on the organism, "
    "and <b>not O<sub>2</sub></b>."))
# F050, F053
story.append(b1(
    "Van Niel hence inferred that the <b>O<sub>2</sub> evolved by the green plant comes from "
    "H<sub>2</sub>O, not from carbon dioxide</b>. This was later <b>proved by using "
    "radioisotopic techniques</b> - the O<sub>2</sub> released is <b>from water</b>."))
# F051, F052, F054
story.append(b1(
    "The <b>correct equation</b> that would represent the overall process of photosynthesis is: "
    "<b>6CO<sub>2</sub> + 12H<sub>2</sub>O</b>, in the presence of <b>light</b>, yields "
    "<b>C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + 6H<sub>2</sub>O + 6O<sub>2</sub></b>, where "
    "<b>C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> represents glucose</b>. This is "
    "<b>not a single reaction</b> but a description of a <b>multistep process</b> called "
    "photosynthesis."))

# ======================================================================================
# ---- 11.3 WHERE DOES PHOTOSYNTHESIS TAKE PLACE? ----
# ---- (F223 heading; F250 opener; F055-F064; F268, F270 folds; Fig 11.2) ----
# ======================================================================================
story.append(heading("11.3", "WHERE DOES PHOTOSYNTHESIS TAKE PLACE?", 1))
# F250 (opener)
story.append(body(
    "You would of course answer: in <b>'the green leaf'</b> or <b>'in the chloroplasts'</b>, based "
    "on what you earlier read in Chapter 8."))
# F055, F056, F057
story.append(b1(
    "Photosynthesis <b>does</b> take place in the <b>green leaves</b> of plants, but it does so "
    "<b>also in other green parts</b> of the plants."))
story.append(b1(
    "The <b>mesophyll cells</b> in the leaves have a <b>large number of chloroplasts</b>. "
    "<b>Usually</b> the chloroplasts <b>align themselves along the walls of the mesophyll "
    "cells</b>, such that they get the <b>optimum quantity of the incident light</b>."))
# F270 - SUMMARY-UNIQUE fold (part 1): the explicit two-stage naming
story.append(b1(
    "Photosynthesis has <b>two stages</b>: the <b>light reaction</b> and the <b>carbon fixing "
    "reactions</b>."))
story.append(gap())

# ---- 11.3 Figure 11.2 - chloroplast structure, labels F272 into running text ----
story.append(figure(
    "fig_11_2.png",
    "<b>Fig. 11.2</b> - Diagrammatic representation of an electron micrograph of a section of "
    "chloroplast.",
    max_width_cm=15.2))
story.append(gap())
# F058 + Figure 11.2 labels (F272): Outer membrane, Inner membrane, Stromal lamella, Grana,
# Stroma, Ribosomes, Starch granule, Lipid droplet - each written into the table below.
story.append(body(
    "Within the chloroplast there is a <b>membranous system</b> consisting of the <b>grana</b>, "
    "the <b>stroma lamellae</b>, and the <b>matrix stroma</b>. The parts marked on the section of "
    "the chloroplast are:"))
story.append(data_table([
    ["Part of the chloroplast", "What it is"],
    ["<b>Outer membrane</b>", "The outer of the two bounding membranes of the chloroplast"],
    ["<b>Inner membrane</b>", "The inner bounding membrane, lying within the outer membrane"],
    ["<b>Grana</b>", "The stacked membrane compartments of the membranous system"],
    ["<b>Stromal lamella</b>",
     "The membrane lamellae connecting the grana; also written <b>stroma lamellae</b>"],
    ["<b>Stroma</b>", "The <b>matrix</b> in which the grana and stromal lamella are embedded"],
    ["<b>Ribosomes</b>", "Present in the stroma of the chloroplast"],
    ["<b>Starch granule</b>", "Stored product lying in the stroma"],
    ["<b>Lipid droplet</b>", "Lipid body lying in the stroma"],
], col_widths=[3.4, 6.6]))
story.append(gap())
# F059, F060, F061 - division of labour
story.append(body("There is a clear <b>division of labour</b> within the chloroplast:"))
story.append(b1(
    "The <b>membrane system</b> is responsible for <b>trapping the light energy</b> and also for "
    "the <b>synthesis of ATP and NADPH</b>."))
story.append(b1(
    "In <b>stroma</b>, <b>enzymatic reactions synthesise sugar</b>, which in turn forms "
    "<b>starch</b>."))
# F268 - SUMMARY-UNIQUE fold: the "chemosynthetic pathway" wording
story.append(b1(
    "Within the chloroplasts the <b>membranes are sites for the light reaction</b>, while the "
    "<b>chemosynthetic pathway occurs in the stroma</b>."))
story.append(gap())
# F062, F063 - light vs dark reactions
story.append(keyterm(
    "<b>Light reactions</b> (photochemical reactions) - the reactions of the membrane system, "
    "since they are <b>directly light driven</b>."))
story.append(keyterm(
    "<b>Dark reactions</b> (carbon reactions) - the <b>stromal reactions</b>. They are <b>not "
    "directly light driven</b> but are <b>dependent on the products of light reactions</b> "
    "(<b>ATP and NADPH</b>); hence, to distinguish them, they are called dark reactions "
    "<b>by convention</b>."))
# F064
story.append(note(
    "That the stromal reactions are called <b>dark reactions</b> <b>should not</b> be construed to "
    "mean that they <b>occur in darkness</b> or that they are <b>not light-dependent</b>."))

# ======================================================================================
# ---- 11.4 HOW MANY TYPES OF PIGMENTS ARE INVOLVED IN PHOTOSYNTHESIS? ----
# ---- (F224 heading; F251 opener; F065-F074; Fig 11.3a, 11.3b, 11.3c) ----
# ======================================================================================
story.append(heading("11.4", "HOW MANY TYPES OF PIGMENTS ARE INVOLVED IN PHOTOSYNTHESIS?", 1))
# F251 (opener)
story.append(body(
    "Looking at plants have you ever wondered <b>why and how there are so many shades of green</b> "
    "in their leaves - even in the same plant?"))
# F065, F066, F067
story.append(b1(
    "The leaf pigments of any green plant can be separated through <b>paper chromatography</b>. A "
    "chromatographic separation shows that the colour that we see in leaves is <b>not due to a "
    "single pigment but due to four pigments</b>."))
story.append(data_table([
    ["Leaf pigment", "Colour in the chromatogram"],
    ["<b>Chlorophyll a</b>", "Bright or <b>blue green</b>"],
    ["<b>Chlorophyll b</b>", "<b>Yellow green</b>"],
    ["<b>Xanthophylls</b>", "<b>Yellow</b>"],
    ["<b>Carotenoids</b>", "<b>Yellow to yellow-orange</b>"],
], col_widths=[3.4, 6.6]))
story.append(gap())
# F068
story.append(keyterm(
    "<b>Pigments</b> - substances that have an <b>ability to absorb light at specific "
    "wavelengths</b>."))
story.append(gap())

# ---- 11.4 Figures 11.3a + 11.3b side by side, 11.3c below (session instruction) ----
# Figure 11.3a labels (F273) and 11.3b labels (F274) are carried in the captions and in the
# reading table that follows; the captions also state the colour-carried distinction in words.
story.append(figure_pair(
    "fig_11_3a.png",
    "<b>Fig. 11.3a</b> - Graph showing the <b>absorption spectrum</b> of chlorophyll a, b and the "
    "carotenoids. Its vertical axis is <b>Absorbance of light by chloroplast pigments</b>, and the "
    "curves - separated by colour in the original - are labelled <b>Chlorophyll a</b>, "
    "<b>Chlorophyll b</b> and <b>Carotenoids</b>. Panel marker: <b>(a)</b>.",
    "fig_11_3b.png",
    "<b>Fig. 11.3b</b> - Graph showing the <b>action spectrum of photosynthesis</b>. Its vertical "
    "axis is <b>Rate of photosynthesis (measured by O<sub>2</sub> release)</b>. Panel marker: "
    "<b>(b)</b>.",
    panel_cm=8.4))
story.append(gap(6))
story.append(figure(
    "fig_11_3c.png",
    "<b>Fig. 11.3c</b> - Graph showing the <b>action spectrum of photosynthesis superimposed on "
    "the absorption spectrum of chlorophyll a</b>. The original separated the two curves by "
    "colour: the <b>Rate of photosynthesis</b> curve was black and the <b>Absorption</b> curve was "
    "cyan, and the shaded band is <b>Light absorbed</b>. Its horizontal axis is <b>Wavelength of "
    "light in nanometres (nm)</b>, marked at <b>400</b>, <b>500</b>, <b>600</b> and <b>700</b>. "
    "Panel marker: <b>(c)</b>.",
    max_width_cm=9.0))
story.append(gap())
# F069, F070 - chlorophyll a is the chief pigment
story.append(b1(
    "The wavelengths at which there is <b>maximum absorption by chlorophyll a</b>, i.e., in the "
    "<b>blue and the red regions</b>, also show a <b>higher rate of photosynthesis</b>. Hence we "
    "can conclude that <b>chlorophyll a is the chief pigment associated with photosynthesis</b>."))
# F071, F072
story.append(b1(
    "There is <b>not a complete one-to-one overlap</b> between the <b>absorption spectrum of "
    "chlorophyll a</b> and the <b>action spectrum of photosynthesis</b>. The graphs together show "
    "that <b>most</b> of the photosynthesis takes place in the <b>blue and red regions</b> of the "
    "spectrum; <b>some</b> photosynthesis does take place at the <b>other wavelengths of the "
    "visible spectrum</b>."))
# F073
story.append(keyterm(
    "<b>Accessory pigments</b> - though chlorophyll is the <b>major pigment</b> responsible for "
    "trapping light, other thylakoid pigments like <b>chlorophyll b, xanthophylls and "
    "carotenoids</b> are called accessory pigments. They also <b>absorb light and transfer the "
    "energy to chlorophyll a</b>."))
# F074
story.append(b1(
    "The accessory pigments <b>not only</b> enable a <b>wider range of wavelength</b> of incoming "
    "light to be utilised for photosynthesis, <b>but also protect chlorophyll a from "
    "photo-oxidation</b>."))

# ======================================================================================
# ---- 11.5 WHAT IS LIGHT REACTION? (F225 heading; F252 opener; F075-F083; F269; Fig 11.4)
# ======================================================================================
story.append(heading("11.5", "WHAT IS LIGHT REACTION?", 1))
# F252 (opener), F075
story.append(keyterm(
    "<b>Light reactions</b> or the <b>'Photochemical' phase</b> include <b>light absorption</b>, "
    "<b>water splitting</b>, <b>oxygen release</b>, and the <b>formation of high-energy chemical "
    "intermediates, ATP and NADPH</b>."))
# F076, F077, F078
story.append(b1(
    "<b>Several protein complexes</b> are involved in the light reaction. The pigments are "
    "organised into <b>two discrete photochemical light harvesting complexes (LHC)</b> within "
    "<b>Photosystem I (PS I)</b> and <b>Photosystem II (PS II)</b>."))
story.append(note(
    "The photosystems are named <b>in the sequence of their discovery</b>, and <b>not</b> in the "
    "sequence in which they <b>function</b> during the light reaction."))
story.append(gap())

# ---- 11.5 Figure 11.4 - the light harvesting complex; labels F276 into running text ----
story.append(figure(
    "fig_11_4.png",
    "<b>Fig. 11.4</b> - The light harvesting complex.",
    max_width_cm=8.0))
story.append(gap())
# F079, F080, F081, F082 + Figure 11.4 labels (F276)
story.append(body(
    "The parts marked on the light harvesting complex are the <b>Pigment molecules</b>, the "
    "<b>Reaction centre</b>, the <b>Primary acceptor</b>, and the incoming <b>Photon</b> of "
    "light."))
story.append(b1(
    "The <b>LHC</b> are made up of <b>hundreds of pigment molecules</b> bound to <b>proteins</b>."))
story.append(b1(
    "<b>Each</b> photosystem has <b>all</b> the pigments (<b>except one molecule of chlorophyll "
    "a</b>) forming a <b>light harvesting system</b>, also called <b>antennae</b>. These "
    "<b>antenna pigments</b> help to make photosynthesis <b>more efficient</b> by absorbing "
    "<b>different wavelengths of light</b>."))
story.append(b1(
    "The <b>single chlorophyll a molecule</b> forms the <b>reaction centre</b>, and the reaction "
    "centre is <b>different in both the photosystems</b>."))
# F269 - SUMMARY-UNIQUE fold: "funnelled", "reaction centre chlorophylls"
story.append(b1(
    "In the light reaction the light energy is <b>absorbed by the pigments present in the "
    "antenna</b> and <b>funnelled to special chlorophyll a molecules</b> called <b>reaction centre "
    "chlorophylls</b>."))
# F083
story.append(data_table([
    ["Photosystem", "Reaction centre chlorophyll a", "Absorption peak", "Called"],
    ["<b>PS I</b>", "One chlorophyll a molecule", "<b>700 nm</b>", "<b>P700</b>"],
    ["<b>PS II</b>", "One chlorophyll a molecule", "<b>680 nm</b>", "<b>P680</b>"],
], col_widths=[2.0, 4.0, 2.0, 2.0]))

# ======================================================================================
# ---- 11.6 THE ELECTRON TRANSPORT (F226 heading; F253 opener; F084-F091; Fig 11.5) ----
# ======================================================================================
story.append(heading("11.6", "THE ELECTRON TRANSPORT", 1))
# F253 (opener), F084, F085, F086, F087, F088, F089
story.append(process_flow([
    "In <b>photosystem II</b> the reaction centre chlorophyll a <b>absorbs 680 nm wavelength of "
    "red light</b>, causing <b>electrons to become excited</b> and <b>jump into an orbit farther "
    "from the atomic nucleus</b>.",
    "These electrons are <b>picked up by an electron acceptor</b>, which passes them to an "
    "<b>electron transport system consisting of cytochromes</b>.",
    "This movement of electrons is <b>downhill</b>, in terms of an <b>oxidation-reduction or redox "
    "potential scale</b>. The electrons are <b>not used up</b> as they pass through the electron "
    "transport chain, but are <b>passed on to the pigments of photosystem PS I</b>.",
    "<b>Simultaneously</b>, electrons in the <b>reaction centre of PS I</b> are also excited when "
    "they receive <b>red light of wavelength 700 nm</b>, and are transferred to <b>another "
    "accepter molecule that has a greater redox potential</b>.",
    "These electrons then are <b>moved downhill again</b>, this time to a molecule of "
    "<b>energy-rich NADP<super>+</super></b>. The addition of these electrons <b>reduces "
    "NADP<super>+</super> to NADPH + H<super>+</super></b>.",
]))
story.append(gap())
# F090, F091 - the Z scheme
story.append(keyterm(
    "<b>Z scheme</b> - the whole scheme of transfer of electrons, starting from <b>PS II</b>, "
    "<b>uphill to the acceptor</b>, <b>down the electron transport chain to PS I</b>, "
    "<b>excitation of electrons</b>, <b>transfer to another acceptor</b>, and finally "
    "<b>downhill to NADP<super>+</super></b> reducing it to <b>NADPH + H<super>+</super></b>. It "
    "is so called due to its <b>characterstic shape</b>, which is formed when <b>all the carriers "
    "are placed in a sequence on a redox potential scale</b>."))
story.append(gap())

# ---- 11.6 Figure 11.5 - Z scheme; labels F277 into running text ----
story.append(figure(
    "fig_11_5.png",
    "<b>Fig. 11.5</b> - Z scheme of light reaction.",
    max_width_cm=8.7))
story.append(gap())
# Figure 11.5 labels (F277)
story.append(body(
    "The Z scheme diagram is marked with <b>Photosystem II</b> and <b>Photosystem I</b>, each "
    "receiving <b>Light</b> through its <b>LHC</b>; the <b>e acceptor</b> above each photosystem; "
    "the <b>Electron transport system</b> joining them; <b>ADP + iP</b> being converted to "
    "<b>ATP</b>; <b>NADP<super>+</super></b> being reduced to <b>NADPH</b>; and, at PS II, "
    "<b>H<sub>2</sub>O</b> being split to give <b>2e<super>-</super> + 2H<super>+</super> + "
    "[O]</b>."))

# ======================================================================================
# ---- 11.6.1 Splitting of Water (F227 heading; F254 opener; F092-F097) ----
# ======================================================================================
story.append(heading("11.6.1", "Splitting of Water", 2))
# F254 (opener)
story.append(body(
    "You would then ask, <b>How does PS II supply electrons continuously?</b>"))
# F092, F093, F094, F095
story.append(b1(
    "The electrons that were <b>moved from photosystem II must be replaced</b>, and this is "
    "achieved by <b>electrons available due to splitting of water</b>."))
story.append(b1(
    "The <b>splitting of water is associated with the PS II</b>; water is split into "
    "<b>2H<super>+</super>, [O] and electrons</b>. This <b>creates oxygen</b>, one of the "
    "<b>net products of photosynthesis</b>."))
story.append(b1(
    "The electrons needed to <b>replace those removed from photosystem I</b> are provided by "
    "<b>photosystem II</b>."))
# F096
story.append(b1(
    "The water-splitting reaction is: <b>2H<sub>2</sub>O</b> yields <b>4H<super>+</super> + "
    "O<sub>2</sub> + 4e<super>-</super></b>."))
# F097
story.append(note(
    "The <b>water splitting complex</b> is associated with the <b>PS II</b>, which itself is "
    "<b>physically located on the inner side of the membrane of the thylakoid</b>."))

# ======================================================================================
# ---- 11.6.2 Cyclic and Non-cyclic Photo-phosphorylation ----
# ---- (F228 heading; F255 opener; F098-F108; Fig 11.6) ----
# ======================================================================================
story.append(heading("11.6.2", "Cyclic and Non-cyclic Photo-phosphorylation", 2))
# F255 (opener), F098
story.append(body(
    "Living organisms have the capability of <b>extracting energy from oxidisable substances</b> "
    "and <b>store this in the form of bond energy</b>. Special substances like <b>ATP</b> carry "
    "this energy in their <b>chemical bonds</b>."))
# F099, F100
story.append(keyterm(
    "<b>Phosphorylation</b> - the process through which <b>ATP is synthesised by cells</b> (in "
    "<b>mitochondria and chloroplasts</b>)."))
story.append(keyterm(
    "<b>Photophosphorylation</b> - the <b>synthesis of ATP from ADP and inorganic phosphate in "
    "the presence of light</b>."))
# F101, F102
story.append(keyterm(
    "<b>Non-cyclic photo-phosphorylation</b> - occurs when the <b>two photosystems work in a "
    "series</b>, <b>first PS II and then the PS I</b>. The two photosystems are connected through "
    "an <b>electron transport chain</b>, as seen in the <b>Z scheme</b>, and <b>both ATP and "
    "NADPH + H<super>+</super></b> are synthesised by this kind of electron flow."))
# F103, F104
story.append(b1(
    "When <b>only PS I is functional</b>, the electron is <b>circulated within the "
    "photosystem</b> and the phosphorylation occurs due to <b>cyclic flow of electrons</b>. A "
    "<b>possible location</b> where cyclic photophosphorylation could be happening is in the "
    "<b>stroma lamellae</b>."))
# F105
story.append(b1(
    "While the <b>membrane or lamellae of the grana</b> have <b>both PS I and PS II</b>, the "
    "<b>stroma lamellae membranes lack PS II</b> as well as <b>NADP reductase enzyme</b>."))
story.append(gap())

# ---- 11.6.2 Figure 11.6 - cyclic photophosphorylation; labels F278 into running text ----
story.append(figure(
    "fig_11_6.png",
    "<b>Fig. 11.6</b> - Cyclic photophosphorylation.",
    max_width_cm=7.6))
story.append(gap())
# Figure 11.6 labels (F278)
story.append(body(
    "The cyclic photophosphorylation diagram is marked with <b>Photosystem I</b> alone, its "
    "incoming <b>Light</b>, its <b>Chlorophyll P 700</b> reaction centre, the <b>e- acceptor</b> "
    "above it, the <b>Electron transport system</b> returning the electron to the same "
    "photosystem, and <b>ADP + iP</b> being converted to <b>ATP</b>."))
# F106, F107, F108
story.append(b1(
    "In <b>cyclic flow</b> the excited electron <b>does not pass on to NADP<super>+</super></b> but "
    "is <b>cycled back to the PS I complex</b> through the electron transport chain. The cyclic "
    "flow hence results <b>only in the synthesis of ATP, but not of NADPH + H<super>+</super></b>."))
story.append(b1(
    "Cyclic photophosphorylation <b>also</b> occurs when <b>only light of wavelengths beyond 680 "
    "nm</b> are available for excitation."))

# ======================================================================================
# ---- 11.6.3 Chemiosmotic Hypothesis (F229 heading; F256 opener; F109-F124; Fig 11.7) ----
# ======================================================================================
story.append(heading("11.6.3", "Chemiosmotic Hypothesis", 2))
# F256 (opener), F109
story.append(body(
    "Let us now try and understand how actually ATP is synthesised in the chloroplast. The "
    "<b>chemiosmotic hypothesis</b> has been put forward to explain the <b>mechanism by which ATP "
    "is synthesised in the chloroplast</b>."))
# F110, F111
story.append(b1(
    "<b>Like in respiration</b>, in photosynthesis too <b>ATP synthesis is linked to development "
    "of a proton gradient across a membrane</b>; this time these are the <b>membranes of "
    "thylakoid</b>."))
story.append(b1(
    "There is <b>one difference</b> though: here the <b>proton accumulation is towards the inside "
    "of the membrane</b>, i.e., in the <b>lumen</b>, whereas in <b>respiration</b> protons "
    "accumulate in the <b>intermembrane space of the mitochondria</b> when electrons move through "
    "the ETS."))
story.append(gap())

# ---- 11.6.3 Figure 11.7 - ATP synthesis through chemiosmosis; labels F279 ----
story.append(figure(
    "fig_11_7.png",
    "<b>Fig. 11.7</b> - ATP synthesis through chemiosmosis.",
    max_width_cm=13.7))
story.append(gap())
# Figure 11.7 labels (F279) - all 26 written into the two blocks below
story.append(body(
    "The chemiosmosis diagram is drawn across the <b>Thylakoid membrane</b>, with the <b>Stroma "
    "(low H<super>+</super>)</b> on the outer side and the <b>Lumen (high H<super>+</super>)</b> "
    "on the inner side. Along the membrane, in order, it is marked: incoming <b>Light</b> at "
    "<b>P680 PS II</b>, then <b>Plastoquinone</b>, <b>Cytochrome B6f</b>, <b>PC</b> "
    "(<b>Plastocyanin</b>), then <b>Light</b> again at <b>P700 PS I</b>, then <b>Fd</b> and "
    "<b>FNR</b>, which reduces <b>NADP<super>+</super> + H<super>+</super></b> to <b>NADPH</b>. On "
    "the lumen side the <b>Oxidation of water</b> splits <b>H<sub>2</sub>O</b> into <b>1/2 "
    "O<sub>2</sub> + H<super>+</super></b>, releasing <b>H<super>+</super></b> into the lumen."))
story.append(body(
    "The vertical scale beside the membrane runs from <b>High Electrochemical Potential "
    "Gradient</b> down to <b>Low</b>, from the <b>Lumen</b> to the <b>Stroma</b>. At the right the "
    "<b>ATP synthase</b> is drawn in its two parts, <b>CF<sub>0</sub></b> in the membrane and "
    "<b>CF<sub>1</sub></b> facing the stroma, converting <b>ADP + Pi</b> into <b>ATP</b>."))
story.append(gap())
# F112, F113, F114, F115, F116
story.append(process_flow([
    "Since <b>splitting of the water molecule takes place on the inner side of the membrane</b>, "
    "the <b>protons or hydrogen ions</b> that are produced by the splitting of water "
    "<b>accumulate within the lumen of the thylakoids</b>.",
    "As electrons move through the photosystems, <b>protons are transported across the "
    "membrane</b>, because the <b>primary accepter of electron</b>, which is located <b>towards "
    "the outer side of the membrane</b>, transfers its electron <b>not to an electron carrier but "
    "to an H carrier</b>.",
    "Hence this <b>H-carrier molecule removes a proton from the stroma</b> while transporting an "
    "electron; when this molecule <b>passes on its electron to the electron carrier on the inner "
    "side</b> of the membrane, the <b>proton is released into the inner side or the lumen side</b> "
    "of the membrane.",
    "The <b>NADP reductase enzyme</b> is located on the <b>stroma side of the membrane</b>. Along "
    "with electrons that come from the <b>acceptor of electrons of PS I</b>, <b>protons are "
    "necessary for the reduction of NADP<super>+</super> to NADPH + H<super>+</super></b>; these "
    "protons are <b>also removed from the stroma</b>.",
    "Hence, within the chloroplast, <b>protons in the stroma decrease in number</b>, while <b>in "
    "the lumen there is accumulation of protons</b>. This creates a <b>proton gradient across the "
    "thylakoid membrane</b> as well as a <b>measurable decrease in pH in the lumen</b>.",
]))
story.append(gap())
# F117, F118
story.append(b1(
    "The <b>proton gradient</b> is important because it is the <b>breakdown of this gradient</b> "
    "that leads to the <b>synthesis of ATP</b>. The gradient is broken down due to the "
    "<b>movement of protons across the membrane to the stroma</b> through the <b>transmembrane "
    "channel of the CF<sub>0</sub> of the ATP synthase</b>."))
# F119, F120
story.append(keyterm(
    "<b>ATP synthase</b> - the enzyme consists of <b>two parts</b>. One, called "
    "<b>CF<sub>0</sub></b>, is <b>embedded in the thylakoid membrane</b> and forms a "
    "<b>transmembrane channel</b> that carries out <b>facilitated diffusion of protons across the "
    "membrane</b>. The other portion is called <b>CF<sub>1</sub></b> and <b>protrudes on the outer "
    "surface of the thylakoid membrane on the side that faces the stroma</b>."))
# F121
story.append(b1(
    "The breakdown of the gradient provides <b>enough energy to cause a conformational change in "
    "the CF<sub>1</sub> particle</b> of the ATP synthase, which makes the enzyme <b>synthesise "
    "several molecules of energy-packed ATP</b>."))
# F122, F123
story.append(body("<b>Chemiosmosis requires</b>:"))
story.append(b2("a <b>membrane</b>;"))
story.append(b2("a <b>proton pump</b>;"))
story.append(b2("a <b>proton gradient</b>;"))
story.append(b2("<b>ATP synthase</b>."))
story.append(body(
    "<b>Energy is used to pump protons across a membrane</b>, to create a <b>gradient or a high "
    "concentration of protons within the thylakoid lumen</b>. ATP synthase has a <b>channel that "
    "allows diffusion of protons back across the membrane</b>, and this <b>releases enough energy "
    "to activate ATP synthase enzyme</b> that <b>catalyses the formation of ATP</b>."))
# F124
story.append(b1(
    "Along with the <b>NADPH</b> produced by the movement of electrons, the <b>ATP will be used "
    "immediately in the biosynthetic reaction taking place in the stroma</b>, responsible for "
    "<b>fixing CO<sub>2</sub></b> and <b>synthesis of sugars</b>."))

# ======================================================================================
# ---- 11.7 WHERE ARE THE ATP AND NADPH USED? (F230 heading; F257 opener; F125-F134) ----
# ======================================================================================
story.append(heading("11.7", "WHERE ARE THE ATP AND NADPH USED?", 1))
# F257 (opener), F125
story.append(b1(
    "The <b>products of light reaction</b> are <b>ATP, NADPH and O<sub>2</sub></b>. Of these, "
    "<b>O<sub>2</sub> diffuses out of the chloroplast</b>, while <b>ATP and NADPH are used to "
    "drive the processes leading to the synthesis of food</b>, more accurately <b>sugars</b>."))
# F126
story.append(keyterm(
    "<b>Biosynthetic phase</b> of photosynthesis - the <b>synthesis of sugars using ATP and "
    "NADPH</b>."))
# F127, F128
story.append(b1(
    "The biosynthetic process <b>does not directly depend on the presence of light</b> but is "
    "<b>dependent on the products of the light reaction</b>, i.e., <b>ATP and NADPH</b>, besides "
    "<b>CO<sub>2</sub> and H<sub>2</sub>O</b>."))
story.append(b1(
    "<b>Immediately after light becomes unavailable</b> the biosynthetic process <b>continues for "
    "some time and then stops</b>. If then <b>light is made available</b>, the <b>synthesis starts "
    "again</b>."))
# F129, F130, F131, F132
story.append(b1(
    "<b>CO<sub>2</sub> is combined with H<sub>2</sub>O</b> to produce <b>(CH<sub>2</sub>O)n</b> or "
    "<b>sugars</b>. The use of <b>radioactive <super>14</super>C by Melvin Calvin</b> in algal "
    "photosynthesis studies led to the discovery that the <b>first CO<sub>2</sub> fixation product "
    "was a 3-carbon organic acid</b>. Calvin also contributed to working out the <b>complete "
    "biosynthetic pathway</b>; hence it was called the <b>Calvin cycle</b> after him. The "
    "<b>first product identified</b> was <b>3-phosphoglyceric acid</b>, or in short <b>PGA</b>."))
# F133, F134
story.append(b1(
    "Experiments conducted over a <b>wide range of plants</b> led to the discovery of "
    "<b>another group of plants</b> where the <b>first stable product of CO<sub>2</sub> fixation "
    "was again an organic acid, but one which had 4 carbon atoms</b> in it. This acid was "
    "identified to be <b>oxaloacetic acid</b> or <b>OAA</b>."))
story.append(data_table([
    ["Type of CO<sub>2</sub> assimilation", "First product of CO<sub>2</sub> fixation", "Pathway"],
    ["Plants whose first product is a <b>C<sub>3</sub> acid</b>", "<b>PGA</b>",
     "the <b>C<sub>3</sub> pathway</b>"],
    ["Plants whose first product is a <b>C<sub>4</sub> acid</b>", "<b>OAA</b>",
     "the <b>C<sub>4</sub> pathway</b>"],
], col_widths=[4.4, 3.0, 2.6]))

# ======================================================================================
# ---- 11.7.1 The Primary Acceptor of CO2 (F231 heading; F258 opener; F135-F136) ----
# ======================================================================================
story.append(heading("11.7.1", "The Primary Acceptor of CO<sub>2</sub>", 2))
# F258 (opener)
story.append(body(
    "Let us now ask ourselves a question that was asked by the scientists who were struggling to "
    "understand the <b>'dark reaction'</b>."))
# F136, F135
story.append(b1(
    "Scientists believed that <b>since the first product was a C<sub>3</sub> acid</b>, the "
    "<b>primary acceptor would be a 2-carbon compound</b>. They spent <b>many years</b> trying to "
    "identify a 2-carbon compound before they discovered the 5-carbon RuBP."))
story.append(b1(
    "The studies <b>very unexpectedly</b> showed that the acceptor molecule was a <b>5-carbon "
    "ketose sugar - ribulose bisphosphate (RuBP)</b>."))

# ======================================================================================
# ---- 11.7.2 The Calvin Cycle (F232 heading; F259 opener; F137-F148; ----
# ---- F241/F242/F243 stage sub-headings; Fig 11.8) ----
# ======================================================================================
story.append(heading("11.7.2", "The Calvin Cycle", 2))
# F259 (opener), F137
story.append(b1(
    "<b>Calvin and his co-workers</b> then worked out the <b>whole pathway</b> and showed that the "
    "pathway <b>operated in a cyclic manner</b>; the <b>RuBP was regenerated</b>."))
# F138
story.append(note(
    "The <b>Calvin pathway occurs in all photosynthetic plants</b>; it <b>does not matter</b> "
    "whether they have <b>C<sub>3</sub> or C<sub>4</sub> (or any other) pathways</b>."))
story.append(gap())

# ---- 11.7.2 Figure 11.8 - the Calvin cycle; labels F280 into running text ----
story.append(figure(
    "fig_11_8.png",
    "<b>Fig. 11.8</b> - The Calvin cycle proceeds in three stages: (1) <b>carboxylation</b>, "
    "during which CO<sub>2</sub> combines with ribulose-1,5-bisphosphate; (2) <b>reduction</b>, "
    "during which carbohydrate is formed at the expense of the photochemically made ATP and "
    "NADPH; and (3) <b>regeneration</b> during which the CO<sub>2</sub> acceptor "
    "ribulose-1,5-bisphosphate is formed again so that the cycle continues.",
    # LAYOUT (session order, see figure_layout_decisions.md SS2): 10.5 -> 7.6 cm.
    # Shrinking 11.8 pulls stage (3) Regeneration back onto the same page as the
    # rest of 11.7.2, and the vertical space it frees is what lets Figure 11.9
    # sit on the C4 pathway page instead of being pushed onto a page of its own.
    max_width_cm=7.6))
story.append(gap())
# Figure 11.8 labels (F280)
story.append(body(
    "The Calvin cycle diagram is marked with <b>CO<sub>2</sub> + H<sub>2</sub>O</b> entering from "
    "the <b>Atmosphere</b>; the three numbered stages <b>1</b>, <b>2</b> and <b>3</b> - "
    "<b>Carboxylation</b>, <b>Reduction</b> and <b>Regeneration</b>; the intermediates "
    "<b>Ribulose-1,5-bisphosphate</b>, <b>3-phosphoglycerate</b> and <b>Triose phosphate</b>; the "
    "cofactors <b>ATP</b> and <b>ADP</b> on the regeneration step and <b>ATP + NADPH</b> yielding "
    "<b>ADP + Pi + NADP<super>+</super></b> on the reduction step; and the products drawn leaving "
    "the cycle as <b>Sucrose, starch</b>."))
story.append(gap())
# F139 - the three stages
story.append(body(
    "For ease of understanding, the Calvin cycle can be described under <b>three stages</b>: "
    "<b>carboxylation</b>, <b>reduction</b> and <b>regeneration</b>."))
story.append(gap())
# F241 - unnumbered stage sub-heading
story.append(heading("Stage 1", "Carboxylation", 3))
# F140, F141, F142
story.append(b1(
    "<b>Carboxylation</b> is the <b>fixation of CO<sub>2</sub> into a stable organic "
    "intermediate</b>. It is the <b>most crucial step of the Calvin cycle</b>, where "
    "<b>CO<sub>2</sub> is utilised for the carboxylation of RuBP</b>."))
story.append(b1(
    "The reaction is <b>catalysed by the enzyme RuBP carboxylase</b>, which results in the "
    "<b>formation of two molecules of 3-PGA</b>."))
story.append(keyterm(
    "<b>RuBisCO</b> - since the <b>RuBP carboxylase enzyme also has an oxygenation activity</b>, "
    "it would be <b>more correct</b> to call it <b>RuBP carboxylase-oxygenase</b>, or RuBisCO."))
# F242 - unnumbered stage sub-heading
story.append(heading("Stage 2", "Reduction", 3))
# F143, F144
story.append(b1(
    "<b>Reduction</b> is a <b>series of reactions that lead to the formation of glucose</b>. The "
    "steps involve <b>utilisation of 2 molecules of ATP for phosphorylation</b> and <b>two of "
    "NADPH for reduction</b>, <b>per CO<sub>2</sub> molecule fixed</b>."))
story.append(b1(
    "The <b>fixation of six molecules of CO<sub>2</sub></b> and <b>6 turns of the cycle</b> are "
    "required for the <b>formation of one molecule of glucose</b> from the pathway."))
# F243 - unnumbered stage sub-heading
story.append(heading("Stage 3", "Regeneration", 3))
# F145
story.append(b1(
    "<b>Regeneration of the CO<sub>2</sub> acceptor molecule RuBP</b> is <b>crucial if the cycle "
    "is to continue uninterrupted</b>. The regeneration steps require <b>one ATP for "
    "phosphorylation to form RuBP</b>."))
story.append(gap())
# F146, F147
story.append(b1(
    "Hence <b>for every CO<sub>2</sub> molecule entering the Calvin cycle, 3 molecules of ATP and "
    "2 of NADPH are required</b>. It is <b>probably</b> to meet this <b>difference in number of "
    "ATP and NADPH used in the dark reaction</b> that the <b>cyclic phosphorylation</b> takes "
    "place."))
# F148 - the balance sheet
story.append(data_table([
    ["Calvin cycle balance sheet", "IN", "OUT"],
    ["Carbon dioxide", "<b>six CO<sub>2</sub></b>", "-"],
    ["Energy carrier", "<b>18 ATP</b>", "<b>18 ADP</b>"],
    ["Reducing power", "<b>12 NADPH</b>", "<b>12 NADP</b>"],
    ["Sugar", "-", "<b>one glucose</b>"],
], col_widths=[4.0, 3.0, 3.0]))
story.append(gap())
story.append(memory_aid(
    "For the Calvin cycle stages, remember <b>C-R-R</b>: <b>C</b>arboxylation, <b>R</b>eduction, "
    "<b>R</b>egeneration. And for the per-CO<sub>2</sub> cost, <b>\"3 A, 2 N\"</b> - "
    "<b>3</b> <b>A</b>TP and <b>2</b> <b>N</b>ADPH."))

# ======================================================================================
# ---- 11.8 THE C4 PATHWAY (F233 heading; F260 opener; F149-F168; Fig 11.9) ----
# ======================================================================================
story.append(heading("11.8", "THE C<sub>4</sub> PATHWAY", 1))
# F260 (opener), F149, F150
story.append(b1(
    "<b>Plants that are adapted to dry tropical regions have the C<sub>4</sub> pathway</b>. Though "
    "C<sub>4</sub> plants have the <b>C<sub>4</sub> oxaloacetic acid as the first "
    "CO<sub>2</sub> fixation product</b>, they use the <b>C<sub>3</sub> pathway or the Calvin "
    "cycle as the main biosynthetic pathway</b>."))
# F151 - the five ways C4 plants are special
story.append(body("<b>C<sub>4</sub> plants are special</b> - they:"))
story.append(b1("have a <b>special type of leaf anatomy</b>;"))
story.append(b1("<b>tolerate higher temperatures</b>;"))
story.append(b1("show a <b>response to high light intensities</b>;"))
story.append(b1("<b>lack a process called photorespiration</b>;"))
story.append(b1("have <b>greater productivity of biomass</b>."))
story.append(gap())
# F152, F153 - Kranz anatomy
story.append(keyterm(
    "<b>Bundle sheath cells</b> - the <b>particularly large cells around the vascular bundles</b> "
    "of the C<sub>4</sub> plants. Leaves which have such anatomy are said to have <b>'Kranz' "
    "anatomy</b>. <b>'Kranz' means 'wreath'</b> and is a <b>reflection of the arrangement of "
    "cells</b>."))
# F154
story.append(body("The <b>bundle sheath cells may form several layers</b> around the vascular "
                  "bundles. They are characterised by having:"))
story.append(b2("a <b>large number of chloroplasts</b>;"))
story.append(b2("<b>thick walls impervious to gaseous exchange</b>;"))
story.append(b2("<b>no intercellular spaces</b>."))
# F155, F156
story.append(b1(
    "<b>Maize and sorghum</b> are C<sub>4</sub> plants whose <b>leaves may be sectioned</b> to "
    "observe the <b>Kranz anatomy</b> and the <b>distribution of mesophyll cells</b>. The "
    "<b>presence of the bundle sheath around the vascular bundles</b> would help you <b>identify "
    "the C<sub>4</sub> plants</b>."))
story.append(gap())

# ---- 11.8 Figure 11.9 - the Hatch and Slack Pathway; labels F281 into running text ----
story.append(figure(
    "fig_11_9.png",
    "<b>Fig. 11.9</b> - Diagrammatic representation of the Hatch and Slack Pathway.",
    # LAYOUT (session order, see figure_layout_decisions.md SS2): 10.0 -> 7.4 cm,
    # so the whole figure block fits in the tail of the C4 pathway page (11.8)
    # and the content above the 11.9 Photorespiration heading stays contiguous.
    max_width_cm=7.4))
story.append(gap())
# Figure 11.9 labels (F281)
story.append(body(
    "The Hatch and Slack Pathway diagram is drawn across two cells. In the <b>Mesophyll cell</b>, "
    "bounded by its <b>Cell wall</b> and <b>Plasma membrane</b>, <b>Atmospheric CO<sub>2</sub></b> "
    "enters as <b>HCO<sub>3</sub><super>-</super></b> and undergoes <b>Fixation</b> with "
    "<b>Phosphoenol-pyruvate</b> to give a <b>C<sub>4</sub> acid</b>. The C<sub>4</sub> acid "
    "undergoes <b>Transport</b> through the <b>Plasmodesmata</b> into the <b>Bundle sheath "
    "cell</b>, where <b>Decarboxylation</b> releases <b>CO<sub>2</sub></b> for <b>Fixation by "
    "Calvin cycle</b>, and the <b>C<sub>3</sub> acid</b> returns to the mesophyll cell for "
    "<b>Regeneration</b> of phosphoenol-pyruvate."))
story.append(gap())
# F157, F158, F159, F160
story.append(b1(
    "The C<sub>4</sub> pathway shown in Figure 11.9 has been named the <b>Hatch and Slack "
    "Pathway</b>, and is again a <b>cyclic process</b>."))
story.append(b1(
    "The <b>primary CO<sub>2</sub> acceptor</b> is a <b>3-carbon molecule phosphoenol pyruvate "
    "(PEP)</b> and is <b>present in the mesophyll cells</b>. The enzyme responsible for the "
    "<b>primary CO<sub>2</sub> fixation</b> in C<sub>4</sub> plants is <b>PEP carboxylase</b> or "
    "<b>PEPcase</b>."))
story.append(note(
    "It is important to register that the <b>mesophyll cells lack RuBisCO enzyme</b>."))
story.append(gap())
# F161, F162, F163, F164, F165
story.append(process_flow([
    "The <b>C<sub>4</sub> acid OAA is formed in the mesophyll cells</b>.",
    "OAA then forms <b>other 4-carbon compounds like malic acid or aspartic acid</b> in the "
    "<b>mesophyll cells itself</b>, which are <b>transported to the bundle sheath cells</b>.",
    "In the <b>bundle sheath cells</b> these <b>C<sub>4</sub> acids are broken down to release "
    "CO<sub>2</sub> and a 3-carbon molecule</b>.",
    "The <b>3-carbon molecule is transported back to the mesophyll</b>, where it is <b>converted "
    "to PEP again</b>, thus <b>completing the cycle</b>.",
    "The <b>CO<sub>2</sub> released in the bundle sheath cells enters the C<sub>3</sub> or the "
    "Calvin pathway</b>, a <b>pathway common to all plants</b>.",
], cyclic=True))
story.append(gap())
# F166, F167, F168
story.append(b1(
    "The <b>bundle sheath cells are rich in an enzyme Ribulose bisphosphate "
    "carboxylase-oxygenase (RuBisCO)</b>, but <b>lack PEPcase</b>."))
story.append(b1(
    "Thus the <b>basic pathway that results in the formation of the sugars</b>, the <b>Calvin "
    "pathway</b>, is <b>common to the C<sub>3</sub> and C<sub>4</sub> plants</b>. It occurs in "
    "<b>all the mesophyll cells of the C<sub>3</sub> plants</b>; in the <b>C<sub>4</sub> plants it "
    "does not take place in the mesophyll cells</b> but does so <b>only in the bundle sheath "
    "cells</b>."))
story.append(gap())
# Exercise-gap cross-reference (Rule 2: the gap is written out ONCE, in the appendix)
story.append(body(
    "<i>Kranz anatomy is an </i><b>internal</b><i> criterion. Whether a plant can be told apart "
    "as C<sub>3</sub> or C<sub>4</sub> by looking at it </i><b>externally</b><i> is answered in "
    "the closing section, 'Terms used in the exercises'.</i>"))

# ======================================================================================
# ---- 11.9 PHOTORESPIRATION (F234 heading; F261 opener; F169-F184; F270 fold) ----
# ======================================================================================
story.append(heading("11.9", "PHOTORESPIRATION", 1))
# F261 (opener), F169
story.append(body(
    "<b>Photorespiration</b> is <b>one more process that creates an important difference between "
    "C<sub>3</sub> and C<sub>4</sub> plants</b>."))
# F170, F171
story.append(b1(
    "The <b>first CO<sub>2</sub> fixation step of the Calvin pathway</b> is the reaction where "
    "<b>RuBP combines with CO<sub>2</sub> to form 2 molecules of 3PGA</b>, <b>catalysed by "
    "RuBisCO</b>: <b>RuBP + CO<sub>2</sub></b>, catalysed by <b>RuBisCO</b>, yields <b>2 x "
    "3PGA</b>."))
# F172, F173
story.append(b1(
    "<b>RuBisCO is the most abundant enzyme in the world.</b> It is characterised by the fact that "
    "its <b>active site can bind to both CO<sub>2</sub> and O<sub>2</sub></b> - hence the name."))
# F174, F175, F176
story.append(b1(
    "RuBisCO has a <b>much greater affinity for CO<sub>2</sub></b> when the "
    "<b>CO<sub>2</sub>:O<sub>2</sub> is nearly equal</b>. The binding of CO<sub>2</sub> and "
    "O<sub>2</sub> to RuBisCO is <b>competitive</b>, and it is the <b>relative concentration of "
    "O<sub>2</sub> and CO<sub>2</sub></b> that determines <b>which of the two will bind</b> to the "
    "enzyme."))
story.append(b1(
    "In <b>C<sub>3</sub> plants some O<sub>2</sub> does bind to RuBisCO</b>, and hence "
    "<b>CO<sub>2</sub> fixation is decreased</b>."))
# F177
story.append(keyterm(
    "<b>Photorespiration</b> - here the <b>RuBP, instead of being converted to 2 molecules of "
    "PGA, binds with O<sub>2</sub></b> to form <b>one molecule of phosphoglycerate</b> and "
    "<b>phosphoglycolate (2 Carbon)</b>."))
# F178, F179, F180
story.append(b1(
    "In the <b>photorespiratory pathway</b> there is <b>neither synthesis of sugars nor of "
    "ATP</b>; rather it results in the <b>release of CO<sub>2</sub> with the utilisation of "
    "ATP</b>. There is <b>no synthesis of ATP or NADPH</b>."))
story.append(note(
    "The <b>biological function of photorespiration is not known yet</b>."))
# F270 - SUMMARY-UNIQUE fold (part 2): the "wasteful" qualifier
story.append(b1(
    "<b>RuBisCO also catalyses a wasteful oxygenation reaction in C<sub>3</sub> plants</b>: "
    "photorespiration."))
story.append(gap())
# F181, F182, F183, F184
story.append(b1(
    "In <b>C<sub>4</sub> plants photorespiration does not occur</b>, because they have a "
    "<b>mechanism that increases the concentration of CO<sub>2</sub> at the enzyme site</b>."))
story.append(b1(
    "This takes place when the <b>C<sub>4</sub> acid from the mesophyll is broken down in the "
    "bundle sheath cells to release CO<sub>2</sub></b>, which results in <b>increasing the "
    "intracellular concentration of CO<sub>2</sub></b>. In turn this ensures that the <b>RuBisCO "
    "functions as a carboxylase</b>, <b>minimising the oxygenase activity</b>."))
story.append(b1(
    "Since the <b>C<sub>4</sub> plants lack photorespiration</b>, <b>productivity and yields are "
    "better</b> in these plants. In addition, these plants show <b>tolerance to higher "
    "temperatures</b>."))

# ======================================================================================
# ---- TABLE 11.1 - C3 vs C4 plants (F240 heading; F185, F186, F187) ----
# ======================================================================================
story.append(heading("Table 11.1", "DIFFERENCES BETWEEN C<sub>3</sub> AND C<sub>4</sub> PLANTS",
                     2, has_table=True))
# F185, F186 - NCERT prints this as a fill-in table; the characteristics are its rows.
story.append(body(
    "NCERT prints <b>TABLE 11.1</b> with <b>Columns 2 and 3 left blank</b>, to be filled in to "
    "highlight the <b>differences between C<sub>3</sub> and C<sub>4</sub> Plants</b>. The "
    "completed table, filled from this chapter's own statements, is:"))
story.append(data_table([
    ["Characteristic", "C<sub>3</sub> plants", "C<sub>4</sub> plants"],
    ["Cell type in which the <b>Calvin cycle</b> takes place", "Mesophyll", "Bundle sheath"],
    ["Cell type in which the <b>initial carboxylation</b> reaction occurs",
     "Mesophyll", "Mesophyll"],
    ["How many cell types the leaf has that <b>fix CO<sub>2</sub></b>",
     "One: Mesophyll", "Two: Bundle sheath and mesophyll"],
    ["Which is the <b>primary CO<sub>2</sub> acceptor</b>", "RuBP", "PEP"],
    ["Number of carbons in the primary CO<sub>2</sub> acceptor", "5", "3"],
    ["Which is the <b>primary CO<sub>2</sub> fixation product</b>", "PGA", "OAA"],
    ["Number of carbons in the primary CO<sub>2</sub> fixation product", "3", "4"],
    ["Does the plant have <b>RuBisCO</b>", "Yes", "Yes"],
    ["Does the plant have <b>PEP Case</b>", "No", "Yes"],
    ["Which cells in the plant have <b>RuBisCO</b>", "Mesophyll", "Bundle sheath"],
    ["CO<sub>2</sub> fixation rate under <b>high light conditions</b>", "Low", "High"],
    ["Is <b>photorespiration</b> present at <b>low light intensities</b>",
     "Negligible", "Negligible"],
    ["Is <b>photorespiration</b> present at <b>high light intensities</b>",
     "High", "Negligible"],
    ["Would <b>photorespiration</b> be present at <b>low CO<sub>2</sub> concentrations</b>",
     "High", "Negligible"],
    ["Would <b>photorespiration</b> be present at <b>high CO<sub>2</sub> concentrations</b>",
     "Negligible", "Negligible"],
    ["<b>Temperature optimum</b>", "20-25 degrees C", "30-40 degrees C"],
    ["<b>Examples</b>", "Tomatoes, bell pepper", "Maize, sorghum"],
], col_widths=[5.0, 2.5, 2.5]))
story.append(gap())
# F187 - NCERT's own "Choose from" option lists, carried verbatim in substance
story.append(body(
    "The <b>'Choose from' options</b> NCERT supplies with the table are: "
    "<b>Mesophyll / Bundle sheath / both</b>; <b>Two: Bundle sheath and mesophyll, One: "
    "Mesophyll, Three: Bundle sheath, palisade, spongy mesophyll</b>; <b>RuBP / PEP / PGA</b>; "
    "<b>5 / 4 / 3</b>; <b>PGA / OAA / RuBP / PEP</b>; <b>3 / 4 / 5</b>; <b>Yes / No / Not "
    "always</b>; <b>Mesophyll / Bundle sheath / none</b>; <b>Low / high / medium</b>; "
    "<b>High / negligible / sometimes</b>; and <b>30-40 degrees C / 20-25 degrees C / above 40 "
    "degrees C</b>."))

# ======================================================================================
# ---- 11.10 FACTORS AFFECTING PHOTOSYNTHESIS (F235 heading; F262 opener; F188-F197) ----
# ======================================================================================
story.append(heading("11.10", "FACTORS AFFECTING PHOTOSYNTHESIS", 1))
# F262 (opener), F188
story.append(body(
    "An understanding of the <b>factors that affect photosynthesis</b> is necessary, because the "
    "<b>rate of photosynthesis is very important in determining the yield of plants</b>, including "
    "<b>crop plants</b>."))
# F189, F190, F191, F192
story.append(body(
    "Photosynthesis is under the influence of <b>several factors, both internal (plant) and "
    "external</b>:"))
story.append(data_table([
    ["Factor group", "Factors it includes"],
    ["<b>Plant (internal) factors</b>",
     "The <b>number, size, age and orientation of leaves</b>, <b>mesophyll cells</b> and "
     "<b>chloroplasts</b>, <b>internal CO<sub>2</sub> concentration</b>, and the <b>amount of "
     "chlorophyll</b>. These are <b>dependent on the genetic predisposition and the growth of the "
     "plant</b>."],
    ["<b>External factors</b>",
     "The availability of <b>sunlight</b>, <b>temperature</b>, <b>CO<sub>2</sub> "
     "concentration</b> and <b>water</b>."],
], col_widths=[2.6, 7.4]))
story.append(gap())
# F193, F194
story.append(b1(
    "As a plant photosynthesises, <b>all these factors will simultaneously affect its rate</b>. "
    "Hence, though <b>several factors interact and simultaneously affect photosynthesis or "
    "CO<sub>2</sub> fixation, usually one factor is the major cause</b> or is the one that "
    "<b>limits the rate</b>. Hence <b>at any point the rate will be determined by the factor "
    "available at sub-optimal levels</b>."))
# F195, F196
story.append(keyterm(
    "<b>Blackman's (1905) Law of Limiting Factors</b> - comes into effect when several factors "
    "affect any [bio] chemical process. It states: <b>if a chemical process is affected by more "
    "than one factor, then its rate will be determined by the factor which is nearest to its "
    "minimal value; it is the factor which directly affects the process if its quantity is "
    "changed.</b>"))
# F197
story.append(b1(
    "<b>For example</b>, despite the presence of a <b>green leaf</b> and <b>optimal light and "
    "CO<sub>2</sub> conditions</b>, the plant <b>may not photosynthesise if the temperature is "
    "very low</b>. This leaf, <b>if given the optimal temperature, will start "
    "photosynthesising</b>."))

# ======================================================================================
# ---- 11.10.1 Light (F236 heading; F263 opener; F198-F203; Fig 11.10) ----
# ======================================================================================
story.append(heading("11.10.1", "Light", 2))
# F263 (opener), F198
story.append(body(
    "We need to distinguish between <b>light quality</b>, <b>light intensity</b> and the "
    "<b>duration of exposure to light</b>, while discussing light as a factor that affects "
    "photosynthesis."))
story.append(gap())

# ---- 11.10.1 Figure 11.10 - light intensity vs rate; labels F282 into running text ----
story.append(figure(
    "fig_11_10.png",
    "<b>Fig. 11.10</b> - Graph of light intensity on the rate of photosynthesis.",
    # LAYOUT (session order, see figure_layout_decisions.md SS2): 8.0 -> 6.2 cm.
    # This one is a size order, not a pagination fix: the graph carries only two
    # axis names and the points A-E, so it stays legible at 6.2 cm while giving
    # 11.10.1 more text on its opening page.
    max_width_cm=6.2))
story.append(gap())
# Figure 11.10 labels (F282)
story.append(body(
    "The graph's vertical axis is the <b>Rate of photosynthesis</b> and its horizontal axis is "
    "<b>Light intensity</b>. The points <b>A</b>, <b>B</b>, <b>C</b>, <b>D</b> and <b>E</b> are "
    "marked along the curve."))
story.append(gap())
# F199, F200, F201, F202, F203
story.append(b1(
    "There is a <b>linear relationship between incident light and CO<sub>2</sub> fixation rates at "
    "low light intensities</b>."))
story.append(b1(
    "At <b>higher light intensities</b>, <b>gradually the rate does not show further increase</b> "
    "as <b>other factors become limiting</b>."))
story.append(b1(
    "<b>Light saturation occurs at 10 per cent of the full sunlight.</b> Hence, <b>except for "
    "plants in shade or in dense forests, light is rarely a limiting factor in nature</b>."))
story.append(b1(
    "<b>Increase in incident light beyond a point</b> causes the <b>breakdown of chlorophyll</b> "
    "and a <b>decrease in photosynthesis</b>."))

# ======================================================================================
# ---- 11.10.2 Carbon dioxide Concentration (F237 heading; F264 opener; F204-F211) ----
# ======================================================================================
story.append(heading("11.10.2", "Carbon dioxide Concentration", 2))
# F264 (opener), F204, F205
story.append(b1(
    "<b>Carbon dioxide is the major limiting factor for photosynthesis.</b> The <b>concentration "
    "of CO<sub>2</sub> is very low in the atmosphere</b> (<b>between 0.03 and 0.04 per cent</b>)."))
# F206
story.append(b1(
    "<b>Increase in CO<sub>2</sub> concentration upto 0.05 per cent</b> can cause an <b>increase "
    "in CO<sub>2</sub> fixation rates</b>; <b>beyond this the levels can become damaging over "
    "longer periods</b>."))
# F207, F208, F209, F210
story.append(b1(
    "The <b>C<sub>3</sub> and C<sub>4</sub> plants respond differently to CO<sub>2</sub> "
    "concentrations</b>, and at <b>low light conditions neither group responds to high "
    "CO<sub>2</sub> conditions</b>. At <b>high light intensities both</b> C<sub>3</sub> and "
    "C<sub>4</sub> plants <b>show increase in the rates of photosynthesis</b>."))
story.append(data_table([
    ["Plant group", "Response to increased CO<sub>2</sub> concentration"],
    ["<b>C<sub>4</sub> plants</b>", "Show <b>saturation at about 360 microlitre per litre</b>"],
    ["<b>C<sub>3</sub> plants</b>",
     "<b>Respond to increased CO<sub>2</sub> concentration</b>; saturation is seen <b>only beyond "
     "450 microlitre per litre</b>"],
], col_widths=[2.6, 7.4]))
story.append(gap())
story.append(b1(
    "Thus, <b>current availability of CO<sub>2</sub> levels is limiting to the C<sub>3</sub> "
    "plants</b>."))
# F211
story.append(b1(
    "The fact that <b>C<sub>3</sub> plants respond to higher CO<sub>2</sub> concentration</b> by "
    "showing <b>increased rates of photosynthesis leading to higher productivity</b> has been used "
    "for <b>some greenhouse crops such as tomatoes and bell pepper</b>, which are allowed to grow "
    "in a <b>carbon dioxide enriched atmosphere</b> that leads to <b>higher yields</b>."))

# ======================================================================================
# ---- 11.10.3 Temperature (F238 heading; F265 opener; F212-F215) ----
# ======================================================================================
story.append(heading("11.10.3", "Temperature", 2))
# F265 (opener), F212, F213
story.append(b1(
    "The <b>dark reactions being enzymatic are temperature controlled</b>. Though the <b>light "
    "reactions are also temperature sensitive</b>, they are <b>affected to a much lesser "
    "extent</b>."))
# F214
story.append(b1(
    "The <b>C<sub>4</sub> plants respond to higher temperatures</b> and show a <b>higher rate of "
    "photosynthesis</b>, while <b>C<sub>3</sub> plants have a much lower temperature optimum</b>."))
# F215
story.append(b1(
    "The <b>temperature optimum</b> for photosynthesis of different plants <b>also depends on the "
    "habitat that they are adapted to</b>: <b>tropical plants have a higher temperature optimum "
    "than the plants adapted to temperate climates</b>."))

# ======================================================================================
# ---- 11.10.4 Water (F239 heading; F266 opener; F216-F218) ----
# ======================================================================================
story.append(heading("11.10.4", "Water", 2))
# F266 (opener), F216
story.append(b1(
    "<b>Even though water is one of the reactants in the light reaction</b>, the <b>effect of "
    "water as a factor is more through its effect on the plant</b>, rather than <b>directly on "
    "photosynthesis</b>."))
# F217, F218
story.append(b1(
    "<b>Water stress causes the stomata to close</b>, hence <b>reducing the CO<sub>2</sub> "
    "availability</b>."))
story.append(b1(
    "Besides, water stress also <b>makes leaves wilt</b>, thus <b>reducing the surface area of "
    "the leaves and their metabolic activity</b> as well."))

# ======================================================================================
# ---- QUICK RECAP (F244 heading; rewritten, denser version of the chapter summary) ----
# ======================================================================================
story.append(heading("Recap", "QUICK RECAP", 1))
story.append(b1(
    "<b>Green plants are autotrophs</b> - they make their own food by <b>photosynthesis</b>, a "
    "<b>physico-chemical process</b> using <b>light energy</b> to synthesise <b>organic "
    "compounds</b>. <b>CO<sub>2</sub> is taken in through stomata</b> and used to make "
    "carbohydrates, <b>principally glucose and starch</b>."))
story.append(b1(
    "Photosynthesis occurs <b>only in the green parts</b>, <b>mainly the leaves</b>, whose "
    "<b>mesophyll cells</b> carry <b>many chloroplasts</b>. In the chloroplast, the "
    "<b>membranes</b> run the <b>light reaction</b> and the <b>stroma</b> runs the "
    "<b>chemosynthetic (carbon-fixing) pathway</b> - the <b>two stages</b> of photosynthesis."))
story.append(b1(
    "<b>Four pigments</b> separate on a chromatogram: <b>chlorophyll a</b> (the chief pigment), "
    "<b>chlorophyll b</b>, <b>xanthophylls</b> and <b>carotenoids</b>; the last three are "
    "<b>accessory pigments</b>, which <b>widen the usable wavelength range</b> and <b>protect "
    "chlorophyll a from photo-oxidation</b>. Most photosynthesis happens in the <b>blue and red</b> "
    "regions."))
story.append(b1(
    "Light energy absorbed by the <b>antenna</b> pigments is <b>funnelled to the reaction centre "
    "chlorophylls</b>. <b>PS I</b> has <b>P700</b>, <b>PS II</b> has <b>P680</b>. Electrons run "
    "<b>PS II to PS I to NADP<super>+</super></b> along the <b>Z scheme</b>, giving <b>NADPH</b>; "
    "<b>splitting of water at PS II</b> supplies the replacement electrons and releases "
    "<b>O<sub>2</sub></b> and <b>protons</b>."))
story.append(b1(
    "<b>Non-cyclic photophosphorylation</b> (PS II then PS I) makes <b>ATP and NADPH</b>; "
    "<b>cyclic photophosphorylation</b> (PS I alone, in the <b>stroma lamellae</b>, which lack "
    "PS II and NADP reductase) makes <b>only ATP</b>. ATP synthesis is <b>chemiosmotic</b>: "
    "protons accumulate in the <b>thylakoid lumen</b>, and their return through "
    "<b>CF<sub>0</sub></b> drives a <b>conformational change in CF<sub>1</sub></b> of <b>ATP "
    "synthase</b>."))
story.append(b1(
    "In the <b>carbon fixation cycle</b>, <b>RuBisCO</b> adds <b>CO<sub>2</sub></b> to the "
    "5-carbon <b>RuBP</b>, giving <b>2 molecules of 3-carbon PGA</b>. The <b>Calvin cycle</b> - "
    "<b>carboxylation, reduction, regeneration</b> - converts this to sugar and <b>regenerates "
    "RuBP</b>, at <b>3 ATP and 2 NADPH per CO<sub>2</sub></b>, so <b>6 CO<sub>2</sub>, 18 ATP and "
    "12 NADPH</b> yield <b>one glucose</b>."))
story.append(b1(
    "<b>RuBisCO also catalyses a wasteful oxygenation reaction in C<sub>3</sub> plants - "
    "photorespiration</b> - which makes <b>no sugar, no ATP and no NADPH</b>, and whose "
    "<b>biological function is not known yet</b>."))
story.append(b1(
    "<b>Some tropical plants</b> use the <b>C<sub>4</sub> pathway</b>. <b>PEPcase</b> fixes "
    "CO<sub>2</sub> in the <b>mesophyll</b> to the <b>4-carbon OAA</b>; C<sub>4</sub> acids move "
    "to the <b>bundle sheath cells</b> ('Kranz' anatomy), where <b>decarboxylation</b> "
    "concentrates CO<sub>2</sub> and the <b>Calvin pathway</b> makes the carbohydrate. This "
    "<b>abolishes photorespiration</b> and gives <b>higher productivity</b> and <b>tolerance of "
    "higher temperatures</b>."))
story.append(b1(
    "Rate-limiting factors follow <b>Blackman's Law of Limiting Factors</b>. <b>Light saturates at "
    "10 per cent of full sunlight</b>; <b>CO<sub>2</sub> (0.03-0.04 per cent in air) is the major "
    "limiting factor</b>; <b>dark reactions are temperature controlled</b>; and <b>water acts "
    "indirectly</b>, by <b>closing stomata</b> and <b>wilting leaves</b>."))

# ======================================================================================
# ---- TERMS USED IN THE EXERCISES (F245 heading) ----
# ---- Rule 2: GAP questions only (Ex. 1, 5, 6, 7), each written out ONCE. ----
# ======================================================================================
story.append(heading("Appendix", "TERMS USED IN THE EXERCISES", 1))
story.append(body(
    "<i>Four of the chapter's questions lean on something the chapter never states outright. Those "
    "four are reproduced here with their answers. The answers marked </i><b>[addition]</b><i> go "
    "beyond what this chapter states.</i>"))
story.append(gap())

# ---- Gap 1 - Exercise 1: the negative EXTERNAL C3/C4 claim is never made in the body ----
story.append(heading("Ex. 1", "By looking at a plant externally, can you tell whether a plant is "
                              "C<sub>3</sub> or C<sub>4</sub>? Why and how?", 3))
story.append(body(
    "<b>No.</b> <b>[addition]</b> C<sub>3</sub> and C<sub>4</sub> plants <b>cannot be "
    "distinguished by external appearance</b>. Every criterion this chapter gives is "
    "<b>internal</b>: the <b>'Kranz' anatomy</b> - the <b>large bundle sheath cells</b> around the "
    "vascular bundles, with <b>many chloroplasts</b>, <b>thick walls impervious to gaseous "
    "exchange</b> and <b>no intercellular spaces</b> - which is visible <b>only in a section of "
    "the leaf</b>, not from the outside."))
story.append(gap())

# ---- Gap 2 - Exercise 5: chlorophyll b alone is never stated to be insufficient ----
story.append(heading("Ex. 5", "Suppose there were plants that had a high concentration of "
                              "Chlorophyll b, but lacked chlorophyll a, would it carry out "
                              "photosynthesis? Then why do plants have chlorophyll b and other "
                              "accessory pigments?", 3))
story.append(body(
    "<b>No, it would not.</b> <b>[addition]</b> <b>Chlorophyll a is indispensable</b>: this "
    "chapter states that chlorophyll a is the <b>chief pigment associated with "
    "photosynthesis</b>, and that the <b>single chlorophyll a molecule forms the reaction "
    "centre</b> of each photosystem. A plant with <b>only chlorophyll b</b> would have <b>no "
    "reaction centre</b>, so the <b>light energy it absorbed could not be converted</b>. "
    "Chlorophyll b, xanthophylls and carotenoids are <b>accessory pigments</b>: they "
    "<b>absorb light and transfer the energy to chlorophyll a</b>, which both <b>widens the range "
    "of wavelengths</b> usable for photosynthesis and <b>protects chlorophyll a from "
    "photo-oxidation</b>."))
story.append(gap())

# ---- Gap 3 - Exercise 6: the dark-degradation stability ordering is never stated ----
story.append(heading("Ex. 6", "Why is the colour of a leaf kept in the dark frequently becomes "
                              "yellow, or pale green? Which pigment do you think is more stable?",
                     3))
story.append(body(
    "<b>[addition]</b> A leaf kept <b>in the dark</b> turns <b>yellow or pale green</b> because "
    "<b>chlorophyll breaks down faster in the dark than the carotenoids do</b>. As the green "
    "chlorophyll is lost, the <b>yellow accessory pigments - the xanthophylls and carotenoids - "
    "are left behind</b> and their colour shows through. The <b>more stable pigments are "
    "therefore the carotenoids</b> (and xanthophylls); <b>chlorophyll is the less stable</b>. "
    "This chapter states that the accessory pigments <b>protect chlorophyll a from "
    "photo-oxidation</b>, but it does not give this dark-degradation ordering."))
story.append(gap())

# ---- Gap 4 - Exercise 7: why shade leaves are darker green is never explained ----
story.append(heading("Ex. 7", "Look at leaves of the same plant on the shady side and compare it "
                              "with the leaves on the sunny side. Or, compare the potted plants "
                              "kept in the sunlight with those in the shade. Which of them has "
                              "leaves that are darker green? Why?", 3))
story.append(body(
    "The <b>leaves on the shady side</b> - and the <b>potted plants kept in the shade</b> - have "
    "the <b>darker green</b> leaves. <b>[addition]</b> A <b>shade leaf builds more chlorophyll "
    "per unit leaf area</b>, so that it can <b>trap as much as possible of the little light it "
    "receives</b>; the extra chlorophyll is what makes it look darker green. This chapter states "
    "only that <b>light is rarely a limiting factor in nature except for plants in shade or in "
    "dense forests</b>, and that <b>increase in incident light beyond a point causes the breakdown "
    "of chlorophyll</b> - so the sunny-side leaf keeps less chlorophyll."))


def main():
    return build_pdf(OUT_PDF, story, title="Photosynthesis in Higher Plants - NEET Notes")


if __name__ == "__main__":
    raise SystemExit(main())
