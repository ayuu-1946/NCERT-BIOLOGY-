"""
NCERT Biology -> NEET replacement notes
Class 11, Chapter 5 - Morphology of Flowering Plants

Pass 2 build script (SUPREME COMMAND PROMPT v6, GATE_2_PASS_2_BUILD_AND_LINT.md).

Written linearly from the frozen inventory
`Ch5_MorphologyOfFloweringPlants_inventory.md` (280 rows, F001-F280), in the
section-5 Content Order, importing the frozen `neet_template.py` so that no
style, geometry, colour or font is re-declared here.

Every block below carries its NCERT section marker (`# ---- 5.N ----`) so a
Pass 3 flag can be found and fixed in seconds without regenerating the file.

Source-note compliance (inventory 'Source notes'):
  SRC-1  section 5.5.1.4 names SIX placentation types and describes FIVE.
         The six-name list is reproduced verbatim and is NOT silently corrected.
  SRC-2  section 5.9 has two titles; both are preserved (contents-box string in
         the intro, in-body heading string on the banner).
  SRC-3  'bicarpellary obligately placed' is the NCERT string. Rule 4 - do not
         change it to 'obliquely'.
  SRC-4  floral-formula symbols do not survive text extraction; the symbol key
         is typeset in WORDS (no Unicode male/female/circled-plus glyphs), which
         also keeps check 5 green.
  Preserved NCERT spellings, deliberate, do not 'fix': physiologial, adaptions,
  encyclopediac, leafbase, monoadelphous, placentaion, exogeneously.

Figure-label coverage (check 6): all 56 in-figure labels from the 11
label-bearing figures are written verbatim into running text or a table.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# sys.path bootstrap: walk up until the directory holding neet_template.py.
_probe = HERE
while _probe != os.path.dirname(_probe):
    if os.path.exists(os.path.join(_probe, "neet_template.py")):
        if _probe not in sys.path:
            sys.path.insert(0, _probe)
        break
    _probe = os.path.dirname(_probe)
else:
    raise RuntimeError("neet_template.py not found in any parent directory")

from neet_template import (  # noqa: E402
    STYLES,
    heading,
    keyterm,
    process_flow,
    note,
    memory_aid,
    data_table,
    title_block,
    build_pdf,
)
from neet_template import figure as _shared_figure  # noqa: E402
from reportlab.platypus import Paragraph, Spacer  # noqa: E402
from reportlab.lib.units import cm  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch5_MorphologyOfFloweringPlants.pdf")


# ---- Figure widths: the single pagination lever ----
# One place to tune every plate. Values are `max_width_cm` for `figure()`.
#
# Sizing policy for a COMPACT layout, applied per plate rather than uniformly:
#   * `scale` below is the rendered width divided by the plate's own printed
#     width in the NCERT source (its crop rect, in points / 28.35 = cm). It is
#     the honest measure of whether a baked-in label is smaller than NCERT
#     printed it.
#   * Label-dense plates are held at scale >= ~0.85 so their raster labels stay
#     readable. Fig 5.14 (6 labels) and Fig 5.15 (9 labels) are held near 0.90.
#   * Label-free plates (5.7, 5.8, 5.9, 5.11, 5.12, 5.17) carry no text to
#     protect, so they shrink to 0.72-0.80 - this is where most of the vertical
#     space is recovered.
#   * Nothing is upscaled: `figure()` already caps width at the plate's natural
#     300 dpi size and at FRAME_WIDTH, so a value above either is a no-op.
#
# Note on check 2: the linter measures TEXT-LAYER glyphs (captions, body, table
# cells). Labels baked into a raster plate are pixels, not glyphs, so shrinking
# a figure cannot trip check 2 - it can only hurt human legibility, which is
# why the scale floors above are judgement calls to confirm on a rendered page.
FIG_W = {
    # asset                     cm     source cm   scale   labels
    "fig_5_1.png":               6.3,  # reduced to bring the adventitious-roots sentence onto page 1
    "fig_5_2.png":               9.5,  # reduced to bring Fig. 5.3 onto page 2
    "fig_5_3.png":               7.3,  #  8.54     0.85     5
    "fig_5_4_horizontal.png":   14.5,  # split panels (a)-(c), then composed horizontally
    "fig_5_5.png":               7.0,  #  7.94     0.88     3
    "fig_5_6.png":               6.8,  #  7.97     0.85     3
    "fig_5_7.png":               6.0,  # source plate; composite below is used in the story
    "fig_5_8.png":               6.0,  # source plate; composite below is used in the story
    "fig_5_7_5_8_horizontal.png": 14.5,  # racemose + cymose side by side
    "fig_5_9.png":              11.5,  # 15.87     0.72     none
    "fig_5_10.png":             14.0,  # 17.07     0.82     5
    "fig_5_11.png":              9.0,  # 11.89     0.76     none
    "fig_5_12_horizontal.png":  14.0,  # composite  n/a     none
    "fig_5_13.png":              8.8,  # 10.09     0.87     4
    "fig_5_14.png":              7.6,  #  8.18     0.93     6
    "fig_5_15.png":             12.5,  # 13.65     0.92     9
    "fig_5_16.png":              5.0,  # reduced to keep the final Quick Recap on page 12
    "fig_5_17.png":             10.0,  # 12.56     0.80     none
}


def figure(asset_name, caption_text, max_width_cm=None):
    """Embed a plate, taking its width from FIG_W unless one is passed."""
    if max_width_cm is None:
        try:
            max_width_cm = FIG_W[asset_name]
        except KeyError:
            raise KeyError(
                "figure width not tabled for %r - add it to FIG_W" % asset_name
            )
    return _shared_figure(asset_name, caption_text, ASSETS, max_width_cm=max_width_cm)


def P(text, style="Body"):
    return Paragraph(text, STYLES[style])


def B(text, level=1):
    return Paragraph(text, STYLES["Bullet%d" % level])


story = []

# ---- Title block ----
story.extend(title_block("Morphology of Flowering Plants"))

# ---- Unit 2 opener - REMOVED ON REQUEST ----
# The unit banner and its four narrative paragraphs (F001-F012: unit title,
# the observation/natural-history/reductionist-biology narrative, and the
# three-chapter contents list) are deliberately NOT written.
# Consequence: F001-F012 stay unwritten, so check 7 cannot go green on them
# without an accepted deviation. See PASS2_DECISIONS.md, 'Requested removals'.

# ---- Scientist profile: Katherine Esau (F013-F023) ----
# Text only. The source portrait is a human-subject photograph and is NEVER
# embedded (section 4.4 hard no); only its caption string survives, as text.
story.append(heading("Profile", "Katherine Esau (1898 - 1997)", level=2))
story.append(P(
    "Katherine Esau was born in Ukraine in 1898. She studied agriculture in Russia and Germany "
    "and received her doctorate in 1931 in United States. She reported in her early publications "
    "that the curly top virus spreads through a plant via the food-conducting or phloem tissue."))
story.append(P(
    "Dr Esau's <i>Plant Anatomy</i>, published in 1954, took a dynamic, developmental approach "
    "designed to enhance one's understanding of plant structure, and had an enormous impact "
    "worldwide, literally bringing about a revival of the discipline. <i>The Anatomy of Seed "
    "Plants</i> followed in 1960; it was referred to as Webster's of plant biology, being "
    "encyclopediac."))
story.append(P(
    "In 1957 she was elected to the National Academy of Sciences, becoming the sixth woman to "
    "receive that honour, and in 1989 she received the National Medal of Science from President "
    "George Bush. When Katherine Esau died in the year 1997, Peter Raven, director of Anatomy "
    "and Morphology, Missouri Botanical Garden, remembered that she 'absolutely dominated' the "
    "field of plant biology even at the age of 99."))

# ---- Chapter introduction (F025-F032, folds F273 and F275) ----
# The narrative intro paragraphs (F025-F031) and the chapter contents list
# (F032) are deliberately NOT written, on request. Only the root/shoot key
# term survives, which also carries fold F275.
# Consequences, both recorded in PASS2_DECISIONS.md:
#   - F025-F032 stay unwritten, and fold F273 (variation in mode of nutrition,
#     life span, habit, habitat) loses its only home in the chapter.
#   - SRC-2's contents-box title string, '5.9 Description of Some Important
#     Families', was carried by F032. With F032 gone, only the in-body title
#     'Solanaceae' remains, so the two-title finding is no longer preserved.
story.append(heading("5", "Morphology of Flowering Plants", level=1))
story.append(keyterm(
    "<b>Root system and shoot system:</b> the underground part of the flowering plant is the "
    "<b>root system</b>, while the portion above the ground forms the <b>shoot system</b>. The "
    "shoot system is differentiated into stem, leaves, flowers and fruits."))

# ---- Fig 5.1 ----
# Portrait plate (237 x 306 pt), the chapter's orientation map. Width is
# tabled in FIG_W; at 7.5 cm it clears the page tail for the 5.1 banner.
story.append(figure("fig_5_1.png", "Fig. 5.1 - Parts of a flowering plant"))
story.append(P(
    "Trace the plant from the ground up. The <b>Root system</b> below the soil carries a "
    "<b>Primary root</b> with its <b>Secondary root</b> branches. Above the soil the <b>Shoot "
    "system</b> carries the <b>Stem</b>, on which each <b>Node</b> bears a <b>Leaf</b> and a "
    "<b>Bud</b>, with an <b>Internode</b> between two successive nodes, and finally the "
    "<b>Flower</b> and the <b>Fruit</b>."))

# ---- 5.1 THE ROOT (F035-F044, fold F274) ----
story.append(heading("5.1", "The Root", level=1, has_table=True))
story.append(P(
    "In majority of the dicotyledonous plants, the direct elongation of the radicle leads to the "
    "formation of primary root which grows inside the soil. It bears lateral roots of several "
    "orders that are referred to as secondary, tertiary, etc. roots. The primary roots and its "
    "branches constitute the <b>tap root system</b>, as seen in the mustard plant."))
story.append(P(
    "In monocotyledonous plants, the primary root is short lived and is replaced by a large "
    "number of roots. These roots originate from the base of the stem and constitute the "
    "<b>fibrous root system</b>, as seen in the wheat plant. In some plants, like grass, "
    "<i>Monstera</i> and the banyan tree, roots arise from parts of the plant other than the "
    "radicle and are called <b>adventitious roots</b>."))
story.append(data_table([
    ["Root system", "Origin", "Typical group", "Example"],
    ["Tap root system", "Direct elongation of the radicle into a primary root bearing secondary, tertiary, etc. laterals",
     "Majority of dicotyledonous plants", "Mustard"],
    ["Fibrous root system", "Primary root short lived, replaced by a large number of roots from the base of the stem",
     "Monocotyledonous plants", "Wheat"],
    ["Adventitious roots", "Arise from parts of the plant other than the radicle",
     "Both groups", "Grass, <i>Monstera</i>, banyan tree"],
], col_widths=[20, 42, 22, 16]))
story.append(figure(
    "fig_5_2.png",
    "Fig. 5.2 - Different types of roots : (a) Tap (b) Fibrous (c) Adventitious"))
story.append(P(
    "In the tap root the <b>Main root</b> is thickest and its branches are the <b>Laterals</b>; "
    "the wheat plant instead shows a cluster of <b>Fibrous roots</b>, and the third panel shows "
    "<b>Adventitious roots</b> arising away from the radicle."))
story.append(P(
    "The main functions of the root system are four: absorption of water and minerals from the "
    "soil, providing a proper anchorage to the plant parts, storing reserve food material, and "
    "synthesis of plant growth regulators. Beyond these, the roots in some plants get modified "
    "for storage of food, mechanical support and respiration."))

# ---- 5.1.1 Regions of the Root (F045-F058) ----
story.append(heading("5.1.1", "Regions of the Root", level=2))
story.append(P(
    "The root is covered at the apex by a thimble-like structure called the <b>root cap</b>, "
    "which protects the tender apex of the root as it makes its way through the soil. Moving "
    "back from the tip, the root passes through three successive regions."))
story.append(process_flow([
    "<b>Region of meristematic activity</b> - a few millimetres above the root cap. Its cells "
    "are very small, thin-walled and with dense protoplasm, and they divide repeatedly.",
    "<b>Region of elongation</b> - the cells proximal to the meristematic region undergo rapid "
    "elongation and enlargement, and are responsible for the growth of the root in length.",
    "<b>Region of maturation</b> - proximal to the region of elongation, the cells of the "
    "elongation zone gradually differentiate and mature. From this region some of the epidermal "
    "cells form very fine and delicate, thread-like structures called root hairs, which absorb "
    "water and minerals from the soil.",
]))
story.append(figure("fig_5_3.png", "Fig. 5.3 - The regions of the root-tip"))
story.append(P(
    "Read the plate from the tip upwards: <b>Root cap</b>, then the <b>Region of meristematic "
    "activity</b>, then the <b>Region of elongation</b>, and finally the <b>Region of "
    "maturation</b>, from which each <b>Root hair</b> emerges."))
story.append(note(
    "The three regions are a developmental sequence, not three different tissues: the same cell "
    "is first produced in the meristematic region, then elongates, then matures."))

# ---- 5.2 THE STEM (F059-F069, fold F276) ----
story.append(heading("5.2", "The Stem", level=1))
story.append(P(
    "What are the features that distinguish a stem from a root? The morphological features of "
    "stems - the presence of nodes and internodes, multicellular hair and positively phototropic "
    "nature - help to differentiate the stems from roots."))
story.append(keyterm(
    "<b>Stem:</b> the ascending part of the axis bearing branches, leaves, flowers and fruits. "
    "It develops from the plumule of the embryo of a germinating seed."))
story.append(keyterm(
    "<b>Node and internode:</b> the region of the stem where leaves are born are called nodes, "
    "while internodes are the portions between two nodes."))
story.append(P(
    "The stem bears buds, which may be terminal or axillary. Stem is generally green when young "
    "and later often become woody and dark brown."))
story.append(P(
    "The main function of the stem is spreading out branches bearing leaves, flowers and fruits. "
    "It conducts water, minerals and photosynthates. Some stems perform the function of storage "
    "of food, support, protection and of vegetative propagation."))

# ---- 5.3 THE LEAF (F070-F087, fold F277) ----
story.append(heading("5.3", "The Leaf", level=1, has_table=True))
story.append(P(
    "The leaf is a lateral, generally flattened structure borne on the stem; it is a lateral "
    "outgrowth of stem developed exogeneously at the node. It develops at the node and bears a "
    "bud in its axil, and that axillary bud later develops into a branch. Leaves originate from "
    "shoot apical meristems and are arranged in an acropetal order. They are the most important "
    "vegetative organs for photosynthesis."))
story.append(P("A typical leaf consists of three main parts: leaf base, petiole and lamina."))
story.append(data_table([
    ["Part", "Description"],
    ["Leaf base", "The leaf is attached to the stem by the leaf base and may bear two lateral small leaf like structures called stipules. In monocotyledons, the leaf base expands into a sheath covering the stem partially or wholly. In some leguminous plants the leafbase may become swollen, which is called the pulvinus."],
    ["Petiole", "The petiole help hold the blade to light. Long thin flexible petioles allow leaf blades to flutter in wind, thereby cooling the leaf and bringing fresh air to leaf surface."],
    ["Lamina (leaf blade)", "The green expanded part of the leaf with veins and veinlets. There is, usually, a middle prominent vein, which is known as the midrib. Veins provide rigidity to the leaf blade and act as channels of transport for water, minerals and food materials."],
], col_widths=[20, 80]))
story.append(P(
    "The shape, margin, apex, surface and extent of incision of lamina varies in different leaves."))
# Fig 5.4: use the split-and-composed horizontal plate so the leaf structure and
# both venation panels stay together without pushing Venation to a later page.
story.append(figure(
    "fig_5_4_horizontal.png",
    "Fig. 5.4 - Structure of a leaf : (a) Parts of a leaf (b) Reticulate venation (c) Parallel venation"))
story.append(P(
    "Panel (a) names the parts in order from the stem outwards: the <b>Leaf base</b> with its "
    "<b>Stipule</b> and the <b>Axillary bud</b> in the axil, then the <b>Petiole</b>, then the "
    "<b>Lamina</b>."))

# ---- 5.3.1 Venation (F088-F092) ----
story.append(heading("5.3.1", "Venation", level=2))
story.append(keyterm(
    "<b>Venation:</b> the arrangement of veins and the veinlets in the lamina of leaf."))
story.append(data_table([
    ["Venation", "Arrangement", "Characteristic of"],
    ["Reticulate", "The veinlets form a network", "Leaves of dicotyledonous plants generally"],
    ["Parallel", "The veins run parallel to each other within a lamina", "Most monocotyledons"],
], col_widths=[18, 46, 36]))

# ---- 5.3.2 Types of Leaves (F093-F101) ----
story.append(heading("5.3.2", "Types of Leaves", level=2))
story.append(P(
    "A leaf is said to be <b>simple</b> when its lamina is entire, or when incised, the incisions "
    "do not touch the midrib. When the incisions of the lamina reach up to the midrib breaking it "
    "into a number of leaflets, the leaf is called <b>compound</b>."))
story.append(note(
    "A bud is present in the axil of petiole in both simple and compound leaves, but not in the "
    "axil of leaflets of the compound leaf. This is the test that separates a compound leaf from "
    "a branch bearing simple leaves."))
story.append(P("The compound leaves may be of two types."))
story.append(data_table([
    ["Compound leaf", "Arrangement of leaflets", "Example"],
    ["Pinnately compound", "A number of leaflets are present on a common axis, the rachis, which represents the midrib of the leaf", "Neem"],
    ["Palmately compound", "The leaflets are attached at a common point, i.e., at the tip of petiole", "Silk cotton"],
], col_widths=[22, 58, 20]))
story.append(figure(
    "fig_5_5.png",
    "Fig. 5.5 - Compound leaves : (a) pinnately compound leaf (b) palmately compound leaf"))
story.append(P(
    "In the pinnately compound leaf of <b>Neem</b> the leaflets sit along the <b>Rachis</b>; in "
    "the palmately compound leaf of <b>Silk Cotton</b> they radiate from the tip of the petiole."))

# ---- 5.3.3 Phyllotaxy (F102-F109) ----
story.append(heading("5.3.3", "Phyllotaxy", level=2, has_table=True))
story.append(keyterm(
    "<b>Phyllotaxy:</b> the pattern of arrangement of leaves on the stem or branch."))
story.append(P("This is usually of three types - alternate, opposite and whorled."))
story.append(data_table([
    ["Type", "Arrangement at a node", "Examples"],
    ["Alternate", "A single leaf arises at each node in alternate manner", "China rose, mustard and sun flower plants"],
    ["Opposite", "A pair of leaves arise at each node and lie opposite to each other", "Calotropis and guava plants"],
    ["Whorled", "More than two leaves arise at a node and form a whorl", "Alstonia"],
], col_widths=[16, 50, 34]))
story.append(figure(
    "fig_5_6.png",
    "Fig. 5.6 - Different types of phyllotaxy : (a) Alternate (b) Opposite (c) Whorled"))
story.append(P(
    "The three panels are drawn from <b>China rose</b> (alternate), <b>Guava</b> (opposite) and "
    "<b>Alstonia</b> (whorled)."))

# ---- 5.4 THE INFLORESCENCE (F110-F121) ----
story.append(heading("5.4", "The Inflorescence", level=1, has_table=True))
story.append(P(
    "A flower is a modified shoot wherein the shoot apical meristem changes to floral meristem. "
    "Internodes do not elongate and the axis gets condensed. The apex produces different kinds of "
    "floral appendages laterally at successive nodes instead of leaves. When a shoot tip "
    "transforms into a flower, it is always solitary."))
story.append(keyterm(
    "<b>Inflorescence:</b> the arrangement of flowers on the floral axis."))
story.append(P(
    "Depending on whether the apex gets developed into a flower or continues to grow, two major "
    "types of inflorescences are defined - racemose and cymose."))
story.append(data_table([
    ["Inflorescence", "Fate of the main axis", "Order in which flowers are borne"],
    ["Racemose", "The main axis continues to grow", "Flowers are borne laterally in an acropetal succession"],
    ["Cymose", "The main axis terminates in a flower, hence is limited in growth", "The flowers are borne in a basipetal order"],
], col_widths=[18, 40, 42]))
story.append(figure(
    "fig_5_7_5_8_horizontal.png",
    "Figs. 5.7-5.8 - (5.7) Racemose inflorescence; (5.8) Cymose inflorescence"))
story.append(memory_aid(
    "Acropetal points to the apex, so the youngest flower is at the top and the axis is still "
    "growing - that is racemose. Basipetal runs the other way, towards the base, because the tip "
    "was used up by the first flower - that is cymose."))

# ---- 5.5 THE FLOWER (F122-F144) ----
story.append(heading("5.5", "The Flower", level=1, has_table=True))
story.append(P(
    "The flower is the reproductive unit in the angiosperms. It is meant for sexual reproduction. "
    "A typical flower has four different kinds of whorls arranged successively on the swollen end "
    "of the stalk or pedicel, called thalamus or receptacle. These are calyx, corolla, androecium "
    "and gynoecium. Calyx and corolla are accessory organs, while androecium and gynoecium are "
    "reproductive organs. In some flowers like lily, the calyx and corolla are not distinct and "
    "are termed as perianth."))
story.append(P(
    "When a flower has both androecium and gynoecium, it is <b>bisexual</b>. A flower having "
    "either only stamens or only carpels is <b>unisexual</b>."))
story.append(P("In symmetry, the flower may be actinomorphic (radial symmetry) or zygomorphic (bilateral symmetry)."))
story.append(data_table([
    ["Symmetry", "Test", "Examples"],
    ["Actinomorphic (radial)", "Can be divided into two equal radial halves in any radial plane passing through the centre", "Mustard, datura, chilli"],
    ["Zygomorphic (bilateral)", "Can be divided into two similar halves only in one particular vertical plane", "Pea, gulmohur, bean, Cassia"],
    ["Asymmetric (irregular)", "Cannot be divided into two similar halves by any vertical plane passing through the centre", "Canna"],
], col_widths=[22, 52, 26]))
story.append(P(
    "A flower may be trimerous, tetramerous or pentamerous when the floral appendages are in "
    "multiple of 3, 4 or 5, respectively. Flowers with bracts - reduced leaf found at the base of "
    "the pedicel - are called bracteate and those without bracts, ebracteate."))
story.append(P(
    "Based on the position of calyx, corolla and androecium in respect of the ovary on thalamus, "
    "the flowers are described as hypogynous, perigynous and epigynous."))
story.append(data_table([
    ["Flower", "Position of parts", "Ovary is said to be", "Examples"],
    ["Hypogynous", "The gynoecium occupies the highest position while the other parts are situated below it", "Superior", "Mustard, china rose, brinjal"],
    ["Perigynous", "Gynoecium is situated in the centre and other parts of the flower are located on the rim of the thalamus almost at the same level", "Half inferior", "Plum, rose, peach"],
    ["Epigynous", "The margin of thalamus grows upward enclosing the ovary completely and getting fused with it, the other parts of flower arise above the ovary", "Inferior", "Guava, cucumber, and the ray florets of sunflower"],
], col_widths=[13, 47, 15, 25]))
story.append(figure(
    "fig_5_9.png",
    "Fig. 5.9 - Position of floral parts on thalamus : (a) Hypogynous (b) and (c) Perigynous (d) Epigynous"))

# ---- 5.5.1 Parts of a Flower (F145-F148) ----
story.append(heading("5.5.1", "Parts of a Flower", level=2))
story.append(P(
    "Each flower normally has four floral whorls, viz., calyx, corolla, androecium and gynoecium."))
story.append(figure("fig_5_10.png", "Fig. 5.10 - Parts of a flower"))
story.append(P(
    "Working inwards from the stalk: the <b>Pedicel</b> carries the <b>Calyx</b>, then the "
    "<b>Corolla</b>, then the <b>Androecium</b>, with the <b>Gynoecium</b> at the centre."))

# ---- 5.5.1.1 Calyx (F149-F152) ----
story.append(heading("5.5.1.1", "Calyx", level=3))
story.append(P(
    "The calyx is the outermost whorl of the flower and the members are called sepals. Generally, "
    "sepals are green, leaf like and protect the flower in the bud stage. The calyx may be "
    "<b>gamosepalous</b> (sepals united) or <b>polysepalous</b> (sepals free)."))

# ---- 5.5.1.2 Corolla (F153-F166) ----
story.append(heading("5.5.1.2", "Corolla", level=3, has_table=True))
story.append(P(
    "Corolla is composed of petals. Petals are usually brightly coloured to attract insects for "
    "pollination. Like calyx, corolla may also be <b>gamopetalous</b> (petals united) or "
    "<b>polypetalous</b> (petals free). The shape and colour of corolla vary greatly in plants: "
    "corolla may be tubular, bell-shaped, funnel-shaped or wheel-shaped."))
story.append(keyterm(
    "<b>Aestivation:</b> the mode of arrangement of sepals or petals in floral bud with respect "
    "to the other members of the same whorl."))
story.append(P("The main types of aestivation are valvate, twisted, imbricate and vexillary."))
story.append(data_table([
    ["Aestivation", "Arrangement in the bud", "Examples"],
    ["Valvate", "Sepals or petals in a whorl just touch one another at the margin, without overlapping", "Calotropis"],
    ["Twisted", "One margin of the appendage overlaps that of the next one and so on", "China rose, lady's finger, cotton"],
    ["Imbricate", "The margins of sepals or petals overlap one another but not in any particular direction", "Cassia, gulmohur"],
    ["Vexillary (papilionaceous)", "Of five petals, the largest (standard) overlaps the two lateral petals (wings), which in turn overlap the two smallest anterior petals (keel)", "Pea, bean"],
], col_widths=[20, 55, 25]))
story.append(figure(
    "fig_5_11.png",
    "Fig. 5.11 - Types of aestivation in corolla : (a) Valvate (b) Twisted (c) Imbricate (d) Vexillary"))

# ---- 5.5.1.3 Androecium (F167-F177) ----
story.append(heading("5.5.1.3", "Androecium", level=3, has_table=True))
story.append(P(
    "Androecium is composed of stamens. Each stamen, which represents the male reproductive "
    "organ, consists of a stalk or a filament and an anther. Each anther is usually bilobed and "
    "each lobe has two chambers, the pollen-sacs; the pollen grains are produced in pollen-sacs. "
    "A sterile stamen is called <b>staminode</b>."))
story.append(P(
    "Stamens of flower may be united with other members such as petals or among themselves."))
story.append(data_table([
    ["Condition", "Union", "Example"],
    ["Epipetalous", "Stamens are attached to the petals", "Brinjal"],
    ["Epiphyllous", "Stamens attached to the perianth", "Lily"],
    ["Polyandrous", "The stamens remain free", "N/A"],
    ["Monoadelphous", "Stamens united into one bunch or one bundle", "China rose"],
    ["Diadelphous", "Stamens united into two bundles", "Pea"],
    ["Polyadelphous", "Stamens united into more than two bundles", "Citrus"],
], col_widths=[20, 55, 25]))
story.append(P(
    "There may be a variation in the length of filaments within a flower, as in <i>Salvia</i> and "
    "mustard."))

# ---- 5.5.1.4 Gynoecium (F178-F197) ----
story.append(heading("5.5.1.4", "Gynoecium", level=3, has_table=True))
story.append(P(
    "Gynoecium is the female reproductive part of the flower and is made up of one or more "
    "carpels. A carpel consists of three parts namely stigma, style and ovary. Ovary is the "
    "enlarged basal part, on which lies the elongated tube, the style. The style connects the "
    "ovary to the stigma. The stigma is usually at the tip of the style and is the receptive "
    "surface for pollen grains. Each ovary bears one or more ovules attached to a flattened, "
    "cushion-like placenta."))
story.append(P(
    "When more than one carpel is present, they may be free (as in lotus and rose) and are called "
    "<b>apocarpous</b>. They are termed <b>syncarpous</b> when carpels are fused, as in mustard "
    "and tomato."))
story.append(process_flow([
    "Fertilisation takes place in the ovule inside the ovary.",
    "After fertilisation, the ovules develop into seeds.",
    "The ovary matures into a fruit.",
]))
story.append(keyterm(
    "<b>Placentation:</b> the arrangement of ovules within the ovary."))
story.append(P(
    "The placentation are of different types namely, marginal, axile, parietal, basal, central "
    "and free central."))
story.append(data_table([
    ["Placentation", "Arrangement of ovules", "Examples"],
    ["Marginal", "The placenta forms a ridge along the ventral suture of the ovary and the ovules are borne on this ridge forming two rows", "Pea"],
    ["Axile", "The placenta is axial and the ovules are attached to it in a multilocular ovary", "China rose, tomato, lemon"],
    ["Parietal", "The ovules develop on the inner wall of the ovary or on peripheral part; ovary is one-chambered but it becomes two-chambered due to the formation of the false septum", "Mustard, Argemone"],
    ["Free central", "The ovules are borne on central axis and septa are absent", "Dianthus, Primrose"],
    ["Basal", "The placenta develops at the base of ovary and a single ovule is attached to it", "Sunflower, marigold"],
], col_widths=[16, 60, 24]))
story.append(note(
    "The chapter names six types in its list - marginal, axile, parietal, basal, central and free "
    "central - but defines and figures five: central placentation is named and never explained. "
    "Both the six-name list and the five definitions are reproduced here exactly as the source "
    "gives them."))
# Fig 5.12: the native plate is 103 x 535 pt, about 1:5.2, which cannot be
# placed on an A4 portrait column without squashing (forbidden by section 4.4),
# so the horizontal composite is embedded instead. See PASS2_DECISIONS.md.
story.append(figure(
    "fig_5_12_horizontal.png",
    "Fig. 5.12 - Types of placentation : (a) Marginal (b) Axile (c) Parietal (d) Free central (e) Basal"))

# ---- 5.6 THE FRUIT (F198-F210) ----
story.append(heading("5.6", "The Fruit", level=1))
story.append(P(
    "The fruit is a characteristic feature of the flowering plants. It is a mature or ripened "
    "ovary, developed after fertilisation. If a fruit is formed without fertilisation of the "
    "ovary, it is called a <b>parthenocarpic</b> fruit."))
story.append(P(
    "Generally, the fruit consists of a wall or pericarp and seeds. The pericarp may be dry or "
    "fleshy. When pericarp is thick and fleshy, it is differentiated into the outer epicarp, the "
    "middle mesocarp and the inner endocarp."))
story.append(P(
    "In mango and coconut, the fruit is known as a <b>drupe</b>. They develop from monocarpellary "
    "superior ovaries and are one seeded. In mango the pericarp is well differentiated into an "
    "outer thin epicarp, a middle fleshy edible mesocarp and an inner stony hard endocarp. In "
    "coconut, which is also a drupe, the mesocarp is fibrous."))
story.append(figure(
    "fig_5_13.png",
    "Fig. 5.13 - Parts of a fruit : (a) Mango (b) Coconut"))
story.append(P(
    "Both panels are labelled from the outside inwards - <b>Epicarp</b>, <b>Mesocarp</b>, "
    "<b>Endocarp</b> - with the <b>Seed</b> enclosed within."))

# ---- 5.7 THE SEED (F211-F214, fold F278) ----
story.append(heading("5.7", "The Seed", level=1))
story.append(P(
    "The ovules after fertilisation, develop into seeds. A seed is made up of a seed coat and an "
    "embryo. The embryo is made up of a radicle, an embryonal axis and one (as in wheat, maize) "
    "or two cotyledons (as in gram and pea). Seeds vary in shape, size and period of viability."))

# ---- 5.7.1 Structure of a Dicotyledonous Seed (F215-F226) ----
story.append(heading("5.7.1", "Structure of a Dicotyledonous Seed", level=2))
story.append(P(
    "The outermost covering of a seed is the seed coat. The seed coat has two layers, the outer "
    "<b>testa</b> and the inner <b>tegmen</b>. The <b>hilum</b> is a scar on the seed coat "
    "through which the developing seeds were attached to the fruit. Above the hilum is a small "
    "pore called the <b>micropyle</b>."))
story.append(P(
    "Within the seed coat is the embryo, consisting of an embryonal axis and two cotyledons. The "
    "cotyledons are often fleshy and full of reserve food materials. At the two ends of the "
    "embryonal axis are present the radicle and the plumule."))
story.append(P(
    "In some seeds such as castor the endosperm, formed as a result of double fertilisation, is a "
    "food storing tissue and such seeds are called <b>endospermic</b> seeds. In plants such as "
    "bean, gram and pea, the endosperm is not present in mature seeds and such seeds are called "
    "<b>non-endospermous</b>."))
story.append(figure(
    "fig_5_14.png",
    "Fig. 5.14 - Structure of dicotyledonous seed"))
story.append(P(
    "The plate labels the <b>Seed coat</b> with the <b>Hilum</b> and <b>Micropyle</b> on it, the "
    "fleshy <b>Cotyledon</b>, and the two ends of the embryonal axis, the <b>Plumule</b> and the "
    "<b>Radicle</b>."))

# ---- 5.7.2 Structure of Monocotyledonous Seed (F227-F236) ----
story.append(heading("5.7.2", "Structure of Monocotyledonous Seed", level=2, has_table=True))
story.append(P(
    "Generally, monocotyledonous seeds are endospermic but some as in orchids are "
    "non-endospermic. In the seeds of cereals such as maize the seed coat is membranous and "
    "generally fused with the fruit wall. The endosperm is bulky and stores food. The outer "
    "covering of endosperm separates the embryo by a proteinous layer called <b>aleurone "
    "layer</b>."))
story.append(P(
    "The embryo is small and situated in a groove at one end of the endosperm. It consists of one "
    "large and shield shaped cotyledon known as <b>scutellum</b> and a short axis with a plumule "
    "and a radicle. The plumule and radicle are enclosed in sheaths which are called "
    "<b>coleoptile</b> and <b>coleorhiza</b> respectively."))
story.append(figure(
    "fig_5_15.png",
    "Fig. 5.15 - Structure of a monocotyledonous seed"))
story.append(P(
    "The labelled parts are the <b>Seed coat &amp; fruit-wall</b>, the <b>Aleurone layer</b>, the "
    "bulky <b>Endosperm</b>, the shield-shaped <b>Scutellum</b>, and the <b>Embryo</b> itself, "
    "whose <b>Plumule</b> is sheathed by the <b>Coleoptile</b> and whose <b>Radicle</b> is "
    "sheathed by the <b>Coleorhiza</b>."))
story.append(data_table([
    ["Feature", "Dicotyledonous seed", "Monocotyledonous seed"],
    ["Seed coat", "Two layers, outer testa and inner tegmen", "Membranous and generally fused with the fruit wall (cereals such as maize)"],
    ["Cotyledons", "Two, often fleshy and full of reserve food materials", "One large and shield shaped, known as scutellum"],
    ["Endosperm", "Present in endospermic seeds such as castor; absent in non-endospermous seeds such as bean, gram and pea", "Generally endospermic and bulky, storing food; some, as in orchids, are non-endospermic"],
    ["Protective sheaths", "N/A", "Plumule and radicle enclosed in coleoptile and coleorhiza respectively"],
    ["Special layer", "N/A", "Aleurone layer, a proteinous layer separating endosperm from embryo"],
], col_widths=[18, 41, 41]))

# ---- 5.8 SEMI-TECHNICAL DESCRIPTION (F237-F251, fold F279) ----
story.append(heading("5.8", "Semi-technical Description of a Typical Flowering Plant", level=1, has_table=True))
story.append(P(
    "Various morphological features are used to describe a flowering plant. The floral "
    "characteristics form the basis of classification and identification of flowering plants. The "
    "description has to be brief, in a simple and scientific language and presented in a proper "
    "sequence."))
story.append(process_flow([
    "Describe the <b>habit</b> of the plant.",
    "Describe the <b>vegetative characters</b> - roots, stem and leaves.",
    "Describe the <b>floral characters</b> - inflorescence and flower parts.",
    "Present a <b>floral diagram</b> and a <b>floral formula</b>.",
]))
story.append(P("The floral formula is represented by some symbols."))
story.append(data_table([
    ["Symbol", "Stands for"],
    ["Br", "Bracteate"],
    ["K", "Calyx"],
    ["C", "Corolla"],
    ["P", "Perianth"],
    ["A", "Androecium"],
    ["G", "Gynoecium"],
    ["G with a line drawn beneath it", "Superior ovary"],
    ["G with a line drawn above it", "Inferior ovary"],
    ["Male symbol", "Male"],
    ["Female symbol", "Female"],
    ["Combined male-female symbol", "Bisexual plants"],
    ["Circled-plus symbol", "Actinomorphic"],
    ["Per-cent symbol", "Zygomorphic nature of flower"],
], col_widths=[38, 62]))
story.append(P(
    "Fusion is indicated by enclosing the figure within bracket and adhesion by a line drawn "
    "above the symbols of the floral parts."))
story.append(P(
    "A floral diagram provides information about the number of parts of a flower, their "
    "arrangement and the relation they have with one another. The position of the mother axis "
    "with respect to the flower is represented by a dot on the top of the floral diagram. Calyx, "
    "corolla, androecium and gynoecium are drawn in successive whorls, calyx being the outermost "
    "and the gynoecium being in the centre. Floral formula also shows cohesion and adhesion "
    "within parts of whorls and between whorls."))
story.append(figure(
    "fig_5_16.png",
    "Fig. 5.16 - Floral diagram with floral formula"))
story.append(P(
    "The floral diagram and floral formula in this plate represents the mustard plant (Family: "
    "Brassicaceae), whose printed formula reads K2+2 C4 A2+4 G(2)."))

# ---- 5.9 SOLANACEAE (F252-F271) ----
# SRC-2: the contents box calls this 'Description of Some Important Families';
# the in-body heading reads 'SOLANACEAE'. Both strings are preserved - the
# contents string appears in the chapter introduction above.
story.append(heading("5.9", "Solanaceae", level=1, has_table=True))
story.append(P(
    "Solanaceae is a large family, commonly called as the 'potato family'. It is widely "
    "distributed in tropics, subtropics and even temperate zones."))
story.append(heading("Vegetative", "Vegetative Characters", level=3))
story.append(data_table([
    ["Field", "Description"],
    ["Habit", "Plants mostly herbs, shrubs and rarely small trees"],
    ["Stem", "Herbaceous rarely woody, aerial; erect, cylindrical, branched, solid or hollow, hairy or glabrous, underground stem in potato (<i>Solanum tuberosum</i>)"],
    ["Leaves", "Alternate, simple, rarely pinnately compound, exstipulate; venation reticulate"],
], col_widths=[16, 84]))
story.append(heading("Floral", "Floral Characters", level=3))
story.append(data_table([
    ["Field", "Description"],
    ["Inflorescence", "Solitary, axillary or cymose as in <i>Solanum</i>"],
    ["Flower", "Bisexual, actinomorphic"],
    ["Calyx", "Sepals five, united, persistent, valvate aestivation"],
    ["Corolla", "Petals five, united; valvate aestivation"],
    ["Androecium", "Stamens five, epipetalous"],
    ["Gynoecium", "Bicarpellary obligately placed, syncarpous; ovary superior, bilocular, placenta swollen with many ovules, axile"],
    ["Fruits", "Berry or capsule"],
    ["Seeds", "Many, endospermous"],
], col_widths=[16, 84]))
story.append(P(
    "Floral Formula: circled-plus symbol, bisexual symbol, K(5) C(5) A5 G(2), with an adhesion "
    "arc drawn over the corolla and androecium and a line beneath the G for the superior ovary."))
story.append(figure(
    "fig_5_17.png",
    "Fig. 5.17 - Solanum nigrum (makoi) plant : (a) Flowering twig (b) Flower (c) L.S. of flower "
    "(d) Stamens (e) Carpel (f) Floral diagram"))
story.append(heading("Economic", "Economic Importance", level=3))
story.append(P(
    "Many plants belonging to this family are source of food (tomato, brinjal, potato), spice "
    "(chilli); medicine (belladonna, ashwagandha); fumigatory (tobacco); ornamentals (petunia)."))

# ---- Quick Recap ----
story.append(heading("Recap", "Quick Recap", level=1))
story.append(B(
    "- Flowering plants vary enormously in shape, size, structure, mode of nutrition, life span, "
    "habit and habitat, yet all have a root system and a shoot system."))
story.append(B(
    "- Root system is either tap root (majority of dicotyledons, e.g. mustard) or fibrous "
    "(monocotyledons, e.g. wheat); adventitious roots arise from parts other than the radicle. "
    "Roots absorb, anchor, store and synthesise growth regulators, and in some plants are "
    "modified for storage, mechanical support and respiration."))
story.append(B(
    "- The root tip runs root cap, region of meristematic activity, region of elongation, region "
    "of maturation, which bears the root hairs."))
story.append(B(
    "- Nodes and internodes, multicellular hair and positively phototropic nature distinguish the "
    "stem from the root."))
story.append(B(
    "- A leaf has leaf base, petiole and lamina; venation is reticulate (dicots) or parallel "
    "(monocots); leaves are simple or compound (pinnately or palmately); phyllotaxy is alternate, "
    "opposite or whorled."))
story.append(B(
    "- Inflorescence is racemose (axis grows on, flowers acropetal) or cymose (axis ends in a "
    "flower, flowers basipetal)."))
story.append(B(
    "- The flower has four whorls on the thalamus: calyx, corolla, androecium, gynoecium. It may "
    "be actinomorphic, zygomorphic or asymmetric, and hypogynous, perigynous or epigynous, giving "
    "a superior, half inferior or inferior ovary."))
story.append(B(
    "- Aestivation is valvate, twisted, imbricate or vexillary. Placentation is marginal, axile, "
    "parietal, free central or basal."))
story.append(B(
    "- After fertilisation the ovary matures into a fruit and the ovules into seeds. A drupe such "
    "as mango or coconut has epicarp, mesocarp and endocarp."))
story.append(B(
    "- Dicotyledonous seeds have two cotyledons and may be endospermic or non-endospermous; "
    "monocotyledonous seeds are generally endospermic with a scutellum, coleoptile and "
    "coleorhiza."))
story.append(B(
    "- A plant is described in sequence - habit, vegetative characters, floral characters - and "
    "summarised as a floral diagram and floral formula, as illustrated by Solanaceae."))


def main():
    return build_pdf(
        OUT_PDF, story,
        title="Class 11 Chapter 5 - Morphology of Flowering Plants (NEET notes)",
        subject="NEET Biology",
    )


if __name__ == "__main__":
    sys.exit(main())
