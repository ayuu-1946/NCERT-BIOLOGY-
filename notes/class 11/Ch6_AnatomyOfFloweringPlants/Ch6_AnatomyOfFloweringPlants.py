"""
NCERT Class 11 Biology, Chapter 6 - Anatomy of Flowering Plants
NEET replacement notes -> A4 print-ready PDF.

Built under SUPREME COMMAND PROMPT.md v6, Pass 2: written linearly from the
frozen 132-row inventory (Ch6_AnatomyOfFloweringPlants_inventory.md) in Content
Order (SS5), importing the repo-level frozen style module `neet_template.py`
(SS0.6). No style, geometry, colour or font is re-declared here.

Block markers `# ---- N.N ----` mark every NCERT section so a Pass 3 flag can be
found and fixed in one contiguous block. Inventory row IDs are named in the
comments so any fact can be traced back to its frozen row.

FIGURE-LABEL COVERAGE (check_pdf.py check 6):
All five figures (6.1-6.5) carry their part labels as vector/raster artwork, so
the extracted PDF text cannot inherit them from the image. Each figure is
therefore followed by a NOTE that lists its labels verbatim - this is what puts
all 44 figure-label-matrix labels (F036, F053, F072, F099, F116) into the
running text for check 6, and it is also the only way a print reader can name
the parts of a diagram whose labels did not survive extraction.

SUMMARY-UNIQUE folding (SS3, Rule 3): the six SUMMARY-UNIQUE facts (F125-F130)
are folded into their planned body homes AND restated in the Quick Recap, so no
summary-only fact is lost. Their fold points are commented inline.

Subscripts / Greek / arrows: this chapter has none - no chemistry, so check 5
has nothing to escape. Only ASCII hyphens and straight quotes are used.

Source: Chapter/class 11/Chapter 06 - Anatomy of Flowering Plants.pdf
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
    STYLES,
    heading, keyterm, process_flow, note, memory_aid, data_table, title_block, build_pdf,
)
from neet_template import figure as _shared_figure  # noqa: E402
from reportlab.platypus import KeepTogether, Paragraph, Spacer  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch6_AnatomyOfFloweringPlants.pdf")


def figure(asset_name, caption_text, max_width_cm=15.9):
    """Chapter-local binding of the shared figure() helper (SS0.6)."""
    return _shared_figure(asset_name, caption_text, ASSETS, max_width_cm=max_width_cm)


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
story += title_block("Anatomy of Flowering Plants")

# ======================================================================================
# ---- 6.intro ---- F002-F006
# ======================================================================================
story.append(body(
    "The external morphology of larger living organisms - plants and animals alike - shows "
    "clear structural similarities and variations; a study of their <b>internal</b> structure "
    "reveals similarities and differences too. This chapter deals with the internal structure "
    "and functional organisation of higher plants."))

# F002 definition; F003 term (cells -> tissues -> organs)
story.append(keyterm(
    "<b>Anatomy</b> - the study of the <b>internal structure of plants</b>."))
story.append(body(
    "Plants have <b>cells as the basic unit</b>; cells are organised into <b>tissues</b>, and "
    "in turn the tissues are organised into <b>organs</b>."))  # F003

# F004 / F005 / F006 - the three things internal structure reveals
story.append(b1(
    "<b>Different organs</b> in a plant show differences in their internal structure."))  # F004
story.append(b1(
    "Within <b>angiosperms</b>, the <b>monocots and dicots</b> are also seen to be "
    "<b>anatomically different</b>."))  # F005
story.append(b1(
    "Internal structures also show <b>adaptations to diverse environments</b>."))  # F006

# ======================================================================================
# ---- 6.1  The Tissue System ---- F007-F011 (+ folded summary F125, F126)
# ======================================================================================
story.append(heading("6.1", "The Tissue System", level=1))

# F008 opener
story.append(body(
    "Tissues were earlier discussed on the basis of the <b>types of cells</b> present. Tissues "
    "also vary depending on their <b>location</b> in the plant body, and their "
    "<b>structure and function are dependent on that location</b>."))  # F008 + F009

# [FOLD F125 - SUMMARY-UNIQUE] the meristematic/permanent classification is stated only
# in the SUMMARY; folded here as the context the tissue SYSTEMS build on.
story.append(body(
    "The plant tissues are broadly classified into <b>meristematic</b> (apical, lateral and "
    "intercalary) and <b>permanent</b> (simple and complex) tissues. "
    # [FOLD F126 - SUMMARY-UNIQUE] main functions of tissues, summary-only.
    "<b>Assimilation of food and its storage, transportation of water, minerals and "
    "photosynthates, and mechanical support</b> are the main functions of tissues."))

# F010 number (three) + F011 term (the three systems)
story.append(body(
    "On the basis of their structure and location, there are <b>three types of tissue "
    "systems</b>:"))  # F010
story.append(b1(
    "the <b>epidermal tissue system</b>,"))
story.append(b1(
    "the <b>ground or fundamental tissue system</b>, and"))
story.append(b1(
    "the <b>vascular or conducting tissue system</b>."))  # F011

# ======================================================================================
# ---- 6.1.1  Epidermal Tissue System ---- F012-F034 + Fig 6.1 (F035, F036)
# ======================================================================================
story.append(heading("6.1.1", "Epidermal Tissue System", level=2))

# F013 opener
story.append(body(
    "The epidermal tissue system forms the <b>outer-most covering of the whole plant body</b> "
    "and comprises <b>epidermal cells, stomata</b> and the epidermal appendages - the "
    "<b>trichomes and hairs</b>."))  # F013

story.append(body(
    "The <b>epidermis</b> is the outermost layer of the primary plant body. It is made up of "
    "<b>elongated, compactly arranged cells</b>, which form a <b>continuous layer</b>."))  # F014, F015
story.append(b1(
    "Epidermis is <b>usually single-layered</b>."))  # F016 (qualifier: usually)
story.append(b1(
    "Epidermal cells are <b>parenchymatous</b> with a small amount of cytoplasm lining the cell "
    "wall and a <b>large vacuole</b>."))  # F017
story.append(b1(
    "The outside of the epidermis is often covered with a <b>waxy thick layer called the "
    "cuticle</b>, which prevents the loss of water. <b>Cuticle is absent in roots</b>."))  # F018 term + F019 exception

# Epidermal appendages: hairs / root hairs / trichomes  (F020-F026)
story.append(body("<b>Epidermal appendages.</b> The cells of epidermis bear a number of hairs."))  # F020
story.append(b1(
    "<b>Root hairs</b> are <b>unicellular</b> elongations of the epidermal cells and help "
    "absorb <b>water and minerals from the soil</b>."))  # F021
story.append(b1(
    "On the stem the epidermal hairs are called <b>trichomes</b>. The trichomes in the shoot "
    "system are <b>usually multicellular</b>."))  # F022, F023 (qualifier: usually)
story.append(b1(
    "They <b>may be branched or unbranched</b> and <b>soft or stiff</b>; they may even be "
    "<b>secretory</b>."))  # F024 (may), F025
story.append(b1(
    "Trichomes help in <b>preventing water loss due to transpiration</b>."))  # F026

# Stomata  (F027-F034)
story.append(keyterm(
    "<b>Stomata</b> - structures present in the epidermis of <b>leaves</b> that regulate the "
    "process of <b>transpiration and gaseous exchange</b>."))  # F027, F028
story.append(b1(
    "Each stoma is composed of <b>two bean-shaped cells known as guard cells</b> which enclose "
    "the <b>stomatal pore</b>. <b>In grasses, the guard cells are dumb-bell shaped</b>."))  # F029 (two), F030 exception
story.append(b1(
    "The <b>outer walls</b> of guard cells (away from the stomatal pore) are <b>thin</b> and "
    "the <b>inner walls</b> (towards the stomatal pore) are <b>highly thickened</b>."))  # F031
story.append(b1(
    "Guard cells possess <b>chloroplasts</b> and regulate the <b>opening and closing of "
    "stomata</b>."))  # F032
story.append(b1(
    "<b>Sometimes</b>, a few epidermal cells in the vicinity of the guard cells become "
    "specialised in shape and size and are known as <b>subsidiary cells</b>."))  # F033 (sometimes)
story.append(keyterm(
    "<b>Stomatal apparatus</b> - the <b>stomatal aperture, guard cells and the surrounding "
    "subsidiary cells</b> together."))  # F034

# --- Fig 6.1 ---
story.append(figure(
    "fig_6_1.png",
    "Figure 6.1 Diagrammatic representation: (a) stomata with bean-shaped guard cells "
    "(b) stomata with dumb-bell shaped guard cell"))  # F035 caption
story.append(note(
    "Figure 6.1 labels (verbatim): <b>Epidermal cells</b>; <b>Subsidiary cells</b>; "
    "<b>Chloroplast</b>; <b>Guard cells</b>; <b>Stomatal pore</b>."))  # F036 labels -> running text (check 6)

# ======================================================================================
# ---- 6.1.2  The Ground Tissue System ---- F037-F041 (+ folded summary F127, F128)
# ======================================================================================
story.append(heading("6.1.2", "The Ground Tissue System", level=2))

# F038 opener
story.append(body(
    "<b>All tissues except epidermis and vascular bundles constitute the ground tissue.</b> "
    # [FOLD F127 - SUMMARY-UNIQUE] ground tissue forms the main bulk of the plant.
    "The ground tissue system <b>forms the main bulk of the plant</b>."))
story.append(b1(
    "It consists of <b>simple tissues</b> such as <b>parenchyma, collenchyma and "
    "sclerenchyma</b>."))  # F039
story.append(b1(
    "<b>Parenchymatous cells</b> are <b>usually present in cortex, pericycle, pith and "
    "medullary rays</b>, in the primary stems and roots."))  # F040 (usually)
story.append(b1(
    "In <b>leaves</b>, the ground tissue consists of thin-walled, chloroplast-containing cells "
    "and is called <b>mesophyll</b>."))  # F041

# [FOLD F128 - SUMMARY-UNIQUE] ground tissue divided into three zones.
story.append(b1(
    "The ground tissue is divided into <b>three zones - cortex, pericycle and pith</b>."))

# ======================================================================================
# ---- 6.1.3  The Vascular Tissue System ---- F042-F051 (+ folded summary F129) + Fig 6.2
# ======================================================================================
story.append(heading("6.1.3", "The Vascular Tissue System", level=2))

# F043 opener, F044 term
story.append(body(
    "The vascular system consists of <b>complex tissues, the phloem and the xylem</b>. The "
    "<b>xylem and phloem together constitute vascular bundles</b>. "
    # [FOLD F129 - SUMMARY-UNIQUE] vascular bundles = conducting tissue, translocate materials.
    "The vascular bundles form the <b>conducting tissue</b> and <b>translocate water, minerals "
    "and food material</b>."))

story.append(body("<b>Open vs closed vascular bundles</b> (basis: presence of cambium):"))
story.append(b1(
    "<b>Open</b> - in <b>dicotyledonous stems, cambium is present between phloem and xylem</b>. "
    "Because of this cambium these bundles can form <b>secondary xylem and phloem</b>, and are "
    "hence called <b>open</b>."))  # F045, F046
story.append(b1(
    "<b>Closed</b> - in <b>monocotyledons, the vascular bundles have no cambium</b>. Since they "
    "do <b>not form secondary tissues</b> they are referred to as <b>closed</b>."))  # F047 comparison

story.append(body("<b>Radial vs conjoint</b> (basis: relative position of xylem and phloem):"))
story.append(b1(
    "<b>Radial</b> - when xylem and phloem are arranged in an <b>alternate manner along "
    "different radii</b>, such as <b>in roots</b>."))  # F048
story.append(b1(
    "<b>Conjoint</b> - when xylem and phloem are <b>jointly situated along the same radius</b>. "
    "Such bundles are <b>common in stems and leaves</b>, and <b>usually have the phloem located "
    "only on the outer side of the xylem</b>."))  # F049, F050, F051 (usually, only)

# --- Fig 6.2 ---
story.append(figure(
    "fig_6_2.png",
    "Figure 6.2 Various types of vascular bundles: (a) radial (b) conjoint closed "
    "(c) conjoint open"))  # F052 caption
story.append(note(
    "Figure 6.2 labels (verbatim): <b>Xylem</b>; <b>Phloem</b>; <b>Cambium</b>."))  # F053 labels

# ======================================================================================
# ---- 6.2  Anatomy of Dicotyledonous and Monocotyledonous Plants ---- F054-F055 (+ F130)
# ======================================================================================
story.append(heading("6.2", "Anatomy of Dicotyledonous and Monocotyledonous Plants", level=1))

# F055 opener
story.append(body(
    "For a better understanding of tissue organisation of <b>roots, stems and leaves</b>, it is "
    "convenient to study the <b>transverse sections of the mature zones</b> of these organs. "
    # [FOLD F130 - SUMMARY-UNIQUE] secondary growth in most dicot roots and stems.
    "<b>Secondary growth occurs in most of the dicotyledonous roots and stems.</b>"))

# ======================================================================================
# ---- 6.2.1  Dicotyledonous Root ---- F056-F070 (+ Fig 6.3 with 6.2.2)
# ======================================================================================
story.append(heading("6.2.1", "Dicotyledonous Root", level=2))

# F057 opener (example organism: sunflower)
story.append(body(
    "Figure 6.3 (a) shows the transverse section of the <b>sunflower root</b>. From outside in, "
    "the internal tissue organisation is as follows:"))  # F057
story.append(b1(
    "<b>Epiblema</b> - the outermost layer. Many of its cells protrude as <b>unicellular root "
    "hairs</b>."))  # F058, F059
story.append(b1(
    "<b>Cortex</b> - several layers of <b>thin-walled parenchyma cells with intercellular "
    "spaces</b>."))  # F060
story.append(b1(
    "<b>Endodermis</b> - the innermost layer of the cortex; a <b>single layer of barrel-shaped "
    "cells without any intercellular spaces</b>. Its <b>tangential and radial walls</b> have a "
    "deposition of the water-impermeable waxy material <b>suberin</b> in the form of "
    "<b>casparian strips</b>."))  # F061, F062, F063
story.append(b1(
    "<b>Pericycle</b> - a few layers of <b>thick-walled parenchymatous cells</b> next to the "
    "endodermis. <b>Initiation of lateral roots and of vascular cambium during secondary "
    "growth</b> takes place in these cells."))  # F064, F065
story.append(b1(
    "<b>Conjunctive tissue</b> - the parenchymatous cells that lie <b>between the xylem and the "
    "phloem</b>."))  # F067
story.append(b1(
    "<b>Pith</b> - <b>small or inconspicuous</b> in the dicot root."))  # F066

story.append(body("<b>Vascular tissue and stele.</b>"))
story.append(b1(
    "There are <b>usually two to four (2-4) xylem and phloem patches</b>."))  # F068 (2-4, usually)
story.append(b1(
    "Later, a <b>cambium ring develops between the xylem and phloem</b>."))  # F069
story.append(keyterm(
    "<b>Stele</b> - all tissues on the inner side of the endodermis, i.e. <b>pericycle, "
    "vascular bundles and pith</b>, together."))  # F070

# ======================================================================================
# ---- 6.2.2  Monocotyledonous Root ---- F073-F078 (+ Fig 6.3)
# ======================================================================================
story.append(heading("6.2.2", "Monocotyledonous Root", level=2))

# F074 opener
story.append(body(
    "The anatomy of the monocot root is <b>similar to the dicot root in many respects</b>. It "
    "has <b>epidermis, cortex, endodermis, pericycle, vascular bundles and pith</b>."))  # F074, F075
story.append(b1(
    "As compared to the dicot root (which has fewer xylem bundles), there are <b>usually more "
    "than six (polyarch) xylem bundles</b> in the monocot root."))  # F076 (>6/polyarch, usually, comparison)
story.append(b1(
    "<b>Pith is large and well developed.</b>"))  # F077
story.append(b1(
    "<b>Monocotyledonous roots do not undergo any secondary growth.</b>"))  # F078 exception

# --- Fig 6.3 ---
story.append(figure(
    "fig_6_3.png",
    "Figure 6.3 T.S.: (a) Dicot root (Primary) (b) Monocot root"))  # F071 caption
story.append(note(
    "Figure 6.3 labels (verbatim): <b>Root hair</b>; <b>Epidermis</b>; <b>Cortex</b>; "
    "<b>Endodermis</b>; <b>Pericycle</b>; <b>Protoxylem</b>; <b>Metaxylem</b>; <b>Pith</b>; "
    "<b>Phloem</b>."))  # F072 labels

# ======================================================================================
# ---- 6.2.3  Dicotyledonous Stem ---- F079-F092 (+ Fig 6.4 with 6.2.4)
# ======================================================================================
story.append(heading("6.2.3", "Dicotyledonous Stem", level=2))

# F080 opener
story.append(body(
    "The transverse section of a typical young dicotyledonous stem shows the <b>epidermis</b> "
    "as the outermost protective layer. Covered with a thin layer of <b>cuticle</b>, it may "
    "bear <b>trichomes and a few stomata</b>."))  # F080, F081

story.append(body(
    "<b>Cortex.</b> The cells arranged in <b>multiple layers between epidermis and "
    "pericycle</b> constitute the cortex, which consists of <b>three sub-zones</b>:"))  # F082, F083 (three)
story.append(b1(
    "<b>Hypodermis</b> (outer) - a few layers of <b>collenchymatous cells</b> just below the "
    "epidermis, which provide <b>mechanical strength</b> to the young stem."))  # F084
story.append(b1(
    "<b>Cortical layers below the hypodermis</b> - <b>rounded, thin-walled parenchymatous "
    "cells</b> with conspicuous intercellular spaces."))  # F085
story.append(b1(
    "<b>Endodermis</b> (innermost layer of the cortex) - its cells are <b>rich in starch "
    "grains</b>, so the layer is also called the <b>starch sheath</b>."))  # F086, F087

story.append(b1(
    "<b>Pericycle</b> - present on the inner side of the endodermis and above the phloem, in "
    "the form of <b>semi-lunar patches of sclerenchyma</b>."))  # F088
story.append(b1(
    "<b>Medullary rays</b> - a few layers of radially placed parenchymatous cells <b>in between "
    "the vascular bundles</b>."))  # F089
story.append(b1(
    "<b>Vascular bundles</b> - a large number arranged <b>in a ring</b>; this 'ring' "
    "arrangement is a <b>characteristic of the dicot stem</b>. Each bundle is <b>conjoint, "
    "open, and with endarch protoxylem</b>."))  # F090, F091
story.append(b1(
    "<b>Pith</b> - a large number of rounded parenchymatous cells with large intercellular "
    "spaces occupying the <b>central portion</b> of the stem."))  # F092

# ======================================================================================
# ---- 6.2.4  Monocotyledonous Stem ---- F093-F097 (+ Fig 6.4)
# ======================================================================================
story.append(heading("6.2.4", "Monocotyledonous Stem", level=2))

# F094 opener
story.append(body(
    "The monocot stem has a <b>sclerenchymatous hypodermis</b>, a large number of "
    "<b>scattered vascular bundles</b> (each surrounded by a <b>sclerenchymatous bundle "
    "sheath</b>), and a <b>large, conspicuous parenchymatous ground tissue</b>."))  # F094
story.append(b1(
    "Vascular bundles are <b>conjoint and closed</b>."))  # F095
story.append(b1(
    "<b>Peripheral vascular bundles are generally smaller</b> than the centrally located "
    "ones."))  # F096 (generally)
story.append(b1(
    "The <b>phloem parenchyma is absent</b>, and <b>water-containing cavities</b> are present "
    "within the vascular bundles."))  # F097

# --- Fig 6.4 ---
# [VERIFICATION FIX D4] figure + its label NOTE held on one page (they were split by a
# page break, leaving the label list stranded at the top of the next page).
story.append(KeepTogether([figure(
    "fig_6_4.png",
    "Figure 6.4 T.S. of stem: (a) Dicot (b) Monocot"),  # F098 caption
    note(
    "Figure 6.4 labels (verbatim): <b>Epidermal hair</b>; <b>Epidermis</b>; <b>Hypodermis</b>; "
    "<b>Parenchyma</b>; <b>Endodermis</b>; <b>Pericycle</b>; <b>Vascular bundle</b>; "
    "<b>Medullary rays</b>; <b>Pith</b>; <b>Collenchyma</b>; <b>Phloem</b>; <b>Cambium</b>; "
    "<b>Metaxylem</b>; <b>Protoxylem</b>; <b>Xylem</b>; <b>Vascular bundles</b>; <b>Ground "
    "tissue</b>."))  # F099 labels [VERIFICATION FIX D2: 'Xylem' label of the monocot panel added - 17 labels]

# ======================================================================================
# ---- 6.2.5  Dorsiventral (Dicotyledonous) Leaf ---- F100-F114 (+ Fig 6.5 with 6.2.6)
# ======================================================================================
story.append(heading("6.2.5", "Dorsiventral (Dicotyledonous) Leaf", level=2))

# F101 opener (three parts)
story.append(body(
    "The vertical section of a dorsiventral leaf through the lamina shows <b>three main parts: "
    "epidermis, mesophyll and vascular system</b>."))  # F101 (three)

story.append(body("<b>Epidermis.</b>"))
story.append(b1(
    "It covers both the <b>upper surface (adaxial epidermis)</b> and the <b>lower surface "
    "(abaxial epidermis)</b> of the leaf and has a <b>conspicuous cuticle</b>."))  # F102
story.append(b1(
    "The <b>abaxial epidermis generally bears more stomata</b> than the adaxial epidermis; the "
    "<b>latter (adaxial) may even lack stomata</b>."))  # F103 (generally), F104 (may)

story.append(body("<b>Mesophyll.</b>"))
story.append(b1(
    "The tissue <b>between the upper and the lower epidermis</b> is the mesophyll. It possesses "
    "<b>chloroplasts</b>, carries out <b>photosynthesis</b>, and is made up of "
    "<b>parenchyma</b>."))  # F105, F106
story.append(b1(
    "It has <b>two types of cells</b> - the <b>palisade parenchyma</b> and the <b>spongy "
    "parenchyma</b>."))  # F107 (two)
story.append(b1(
    "The <b>adaxially placed palisade parenchyma</b> is made up of <b>elongated cells arranged "
    "vertically and parallel</b> to each other."))  # F108
story.append(b1(
    "The <b>oval or round, loosely arranged spongy parenchyma</b> lies <b>below the palisade "
    "cells</b> and extends to the lower epidermis, with <b>numerous large spaces and air "
    "cavities</b> between the cells."))  # F109, F110

story.append(body("<b>Vascular system.</b>"))
story.append(b1(
    "It includes <b>vascular bundles</b>, seen in the <b>veins and the midrib</b>. The <b>size "
    "of the vascular bundles depends on the size of the veins</b>, and the veins <b>vary in "
    "thickness in the reticulate venation</b> of the dicot leaves."))  # F111, F112, F113
story.append(b1(
    "The vascular bundles are surrounded by a layer of <b>thick-walled bundle sheath "
    "cells</b>."))  # F114
story.append(b1(
    "Note the <b>position of the xylem</b> within the bundle (Figure 6.5 a): the <b>xylem lies "
    "towards the adaxial (upper) side</b> and the <b>phloem towards the abaxial (lower) "
    "side</b>."))  # F114a [VERIFICATION FIX D3: NCERT's closing sentence of 6.2.5 had no inventory row]

# ======================================================================================
# ---- 6.2.6  Isobilateral (Monocotyledonous) Leaf ---- F117-F123 (+ Fig 6.5)
# ======================================================================================
story.append(heading("6.2.6", "Isobilateral (Monocotyledonous) Leaf", level=2))

# F118 opener
story.append(body(
    "The anatomy of the isobilateral leaf is <b>similar to that of the dorsiventral leaf in "
    "many ways</b>, with the following characteristic differences:"))  # F118
story.append(b1(
    "<b>Stomata are present on both surfaces</b> of the epidermis; and the <b>mesophyll is not "
    "differentiated into palisade and spongy parenchyma</b>."))  # F119 comparison
story.append(keyterm(
    "<b>Bulliform cells</b> - in <b>grasses</b>, certain adaxial epidermal cells along the "
    "veins modify into <b>large, empty, colourless cells</b>."))  # F120 (example: grasses)
story.append(b1(
    "When the bulliform cells have <b>absorbed water and are turgid</b>, the <b>leaf surface is "
    "exposed</b>."))  # F121
story.append(b1(
    "When they are <b>flaccid due to water stress</b>, they make the <b>leaves curl inwards to "
    "minimise water loss</b>."))  # F122
story.append(b1(
    "The <b>parallel venation</b> in monocot leaves is reflected in the <b>near similar sizes "
    "of vascular bundles (except in main veins)</b>, as seen in vertical sections."))  # F123 (except)

# --- Fig 6.5 ---
story.append(figure(
    "fig_6_5.png",
    "Figure 6.5 T.S. of leaf: (a) Dicot (b) Monocot"))  # F115 caption
story.append(note(
    "Figure 6.5 labels (verbatim): <b>Bundle sheath</b>; <b>Xylem</b>; <b>Phloem</b>; "
    "<b>Adaxial epidermis</b>; <b>Palisade mesophyll</b>; <b>Air cavity</b>; <b>Spongy "
    "mesophyll</b>; <b>Sub-stomatal cavity</b>; <b>Stoma</b>; <b>Abaxial epidermis</b>; "
    "<b>Mesophyll</b>."))  # F116 labels

# ======================================================================================
# ---- QUICK RECAP (from NCERT SUMMARY; F124 heading) ----
# Every summary sentence restated: BODY-PRESENT lines recap the body, SUMMARY-UNIQUE
# lines (F125-F130) are the same facts already folded above (S2, S3, S6, S7, S10, S13).
# ======================================================================================
story.append(heading("Recap", "Quick Recap", level=1))
story.append(b1(
    "Anatomically, a plant is made of different kinds of <b>tissues</b>, broadly "
    "<b>meristematic</b> (apical, lateral, intercalary) and <b>permanent</b> (simple, complex). "
    "Their main functions are <b>assimilation and storage of food, transport of water, minerals "
    "and photosynthates, and mechanical support</b>."))  # S1, S2 (F125), S3 (F126)
story.append(b1(
    "There are <b>three tissue systems - epidermal, ground and vascular</b>. The epidermal "
    "system is made of <b>epidermal cells, stomata and epidermal appendages</b>."))  # S4, S5
story.append(b1(
    "The <b>ground tissue system forms the main bulk</b> of the plant and is divided into "
    "<b>three zones - cortex, pericycle and pith</b>."))  # S6 (F127), S7 (F128)
story.append(b1(
    "The <b>vascular tissue system</b> is formed by <b>xylem and phloem</b>; on the basis of "
    "<b>presence of cambium and location of xylem and phloem</b> the vascular bundles are of "
    "different types. They form the <b>conducting tissue and translocate water, minerals and "
    "food material</b>."))  # S8, S9, S10 (F129)
story.append(b1(
    "<b>Monocots and dicots differ</b> in the <b>type, number and location of vascular "
    "bundles</b>, and <b>secondary growth occurs in most dicot roots and stems</b>."))  # S11, S12, S13 (F130)

# ======================================================================================
# ---- APPENDIX: Terms used in the exercises (Rule 2 GAP only) ---- F132
# Only the GAP exercise (Q6) is reproduced and answered; the six COVERED exercises
# (Q1-Q5, Q7) are answered by the body sections above and are NOT reproduced (SS Rule 6).
# ======================================================================================
story.append(heading("Q", "Terms Used in the Exercises", level=1))
story.append(body(
    "<b>Q6. How is the study of plant anatomy useful to us?</b>"))  # F132 exercise-gap
story.append(b1(
    "<b>Anatomy is the study of the internal structure and functional organisation of "
    "plants</b>, so it lets us understand how a plant is built from cells to tissues to "
    "organs."))  # F002 [VERIFICATION FIX D1: inventory row ID removed from reader text - Rule 6]
story.append(b1(
    "It lets us <b>distinguish monocots from dicots anatomically</b> - within angiosperms the "
    "two are internally different - which is how a stem or root is identified from a "
    "transverse section."))  # F005 [VERIFICATION FIX D1]
story.append(b1(
    "It reveals the <b>adaptations of internal structures to diverse environments</b>, "
    "e.g. bulliform cells that curl a grass leaf to reduce water loss."))  # F006 [VERIFICATION FIX D1]

# ======================================================================================
# ---- BUILD ---- (SS0.6: build_pdf owns page furniture; no footer/header/page number)
# ======================================================================================
if __name__ == "__main__":
    sys.exit(build_pdf(
        OUT_PDF, story,
        title="Class 11 Chapter 6 - Anatomy of Flowering Plants (NEET notes)",
        subject="NEET Biology"))
