"""
NCERT Class 11 Biology, Chapter 13 - Plant Growth and Development
NEET replacement notes -> A4 print-ready PDF.

Built under SUPREME COMMAND PROMPT.md v6, Pass 2: written linearly from the
frozen 84-row inventory (Ch13_PlantGrowthAndDevelopment_inventory.md, F001-F084),
importing the repo-level frozen style module `neet_template.py` (v6 SS0.6).
No style, geometry, colour or font is re-declared here.

Block markers `# ---- N.N ----` mark every NCERT section so a Pass 3 flag can be
found and fixed in one contiguous block. Inventory row IDs are named in the
comments so any fact can be traced back to its frozen row.

All eleven extracted NCERT figures (fig_13_1 .. fig_13_11) are embedded inline at
their topic through neet_template.figure(); every in-figure label recorded in the
inventory's figure-label matrix is also carried in the running text or a caption,
so check_pdf.py check 6 (figure-label coverage) is satisfied per figure. Inline
chemical formulae and growth equations use <sub>/<super> tags only, never Unicode
subscripts/superscripts, so check 5 (banned glyphs) stays green.
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
from reportlab.platypus import Paragraph, Spacer, PageBreak  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch13_PlantGrowthAndDevelopment.pdf")

# Inline formulae / equations - <sub>/<super> tags only, never Unicode (SS4 technical rules)
GA3 = "GA<sub>3</sub>"
C2H4 = "C<sub>2</sub>H<sub>4</sub>"
EQ_ARITH = "L<sub>t</sub> = L<sub>0</sub> + rt"
EQ_EXP = "W<sub>1</sub> = W<sub>0</sub> e<super>rt</super>"


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
# ---- Title block (SS5 item 1) ----
# ======================================================================================
story.extend(title_block("Plant Growth and Development"))

# ======================================================================================
# ---- Introduction ----  O01, F001-F006
# ======================================================================================
story.append(body(
    "You have already studied the organisation of a flowering plant in Chapter 5. "
    "<b>Development</b> is the sum of two processes: <b>growth</b> and "
    "<b>differentiation</b>. The development of a mature plant from a zygote "
    "(fertilised egg) follows a precise and highly ordered succession of events. "
    "During this development a complex body organisation is formed that produces "
    "roots, leaves, branches, flowers, fruits and seeds, and eventually they die."))
story.append(body(
    "The first step in plant growth is <b>seed germination</b>. A seed germinates only "
    "when favourable conditions for growth exist in the environment; in the absence of "
    "such conditions the seeds do not germinate and pass into a period of suspended "
    "growth or rest. The factors that govern and control developmental processes are "
    "both <b>intrinsic</b> (internal) and <b>extrinsic</b> (external) to the plant."))
story.append(body(
    "In a germinating bean seed the <b>seed coat</b> splits as the arching "
    "<b>epicotyl hook</b> pushes up through the <b>soil line</b>, drawing the "
    "<b>cotyledons</b> above ground. The axis above the point of attachment of the "
    "cotyledon is the <b>epicotyl</b> and the region below it is the "
    "<b>hypocotyl</b>."))
story.append(figure(
    "fig_13_1.png",
    "<b>Fig. 13.1</b> - Germination and seedling development in bean.",
    max_width_cm=12.5))

# ======================================================================================
# ---- 13.1 Growth ----  H02, O02, F007-F009
# ======================================================================================
story.append(heading("13.1", "Growth", level=1))
story.append(body(
    "Growth is regarded as one of the most fundamental and conspicuous characteristics "
    "of a living being."))
story.append(keyterm(
    "<b>Growth</b> is an irreversible permanent increase in the size of an organ or its "
    "parts, or even of an individual cell."))
story.append(body(
    "Generally, growth is accompanied by metabolic processes - both <b>anabolic</b> "
    "(building up) and <b>catabolic</b> (breaking down) - that occur at the expense of "
    "energy."))

# ---- 13.1.1 Plant Growth Generally is Indeterminate ----  H03, O03, F010-F014
story.append(heading("13.1.1", "Plant Growth Generally is Indeterminate", level=2))
story.append(body(
    "Plant growth is unique because plants retain the capacity for unlimited growth "
    "throughout their life. This ability is due to the presence of <b>meristems</b> at "
    "certain locations in the plant body, whose cells can divide and self-perpetuate."))
story.append(keyterm(
    "The growth in which new cells are always being added to the plant body by the "
    "activity of the meristem is called the <b>open form of growth</b>."))
story.append(body(
    "The <b>root apical meristem</b> and the <b>shoot apical meristem</b> are "
    "responsible for the <b>primary growth</b> of plants and principally contribute to "
    "elongation along the axis, in both the root and the shoot. In dicotyledonous plants "
    "and gymnosperms, the <b>lateral meristems</b> - the <b>vascular cambium</b> and the "
    "cork-cambium - appear later in life and cause an increase in girth; this is known as "
    "<b>secondary growth</b>."))
story.append(figure(
    "fig_13_2.png",
    "<b>Fig. 13.2</b> - Diagrammatic representation of locations of root apical "
    "meristem, shoot apical meristem and vascular cambium. Arrows exhibit the "
    "direction of growth of cells and organs.",
    max_width_cm=6.6))

# ---- 13.1.2 Growth is Measurable ----  H04, O04, F015-F018
story.append(heading("13.1.2", "Growth is Measurable", level=2))
story.append(body(
    "At a cellular level, growth is principally a consequence of an increase in the "
    "amount of <b>protoplasm</b>. Because protoplasm is difficult to measure directly, "
    "one measures a quantity that is proportional to it."))
story.append(body(
    "Growth is therefore measured by a variety of parameters: increase in fresh weight, "
    "dry weight, length, area, volume and cell number. A single maize root apical "
    "meristem can give rise to more than <b>17,500 new cells per hour</b>, whereas cells "
    "in a watermelon may increase in size by up to <b>3,50,000 times</b>. The growth of "
    "a pollen tube is measured in terms of its length, while an increase in surface area "
    "denotes the growth in a dorsiventral leaf."))

# ---- 13.1.3 Phases of Growth ----  H05, O05, F019-F022
story.append(heading("13.1.3", "Phases of Growth", level=2))
story.append(body(
    "The period of growth is generally divided into three phases: <b>meristematic</b>, "
    "<b>elongation</b> and <b>maturation</b>."))
story.append(b1(
    "<b>Meristematic phase:</b> the constantly dividing cells at the root apex and the "
    "shoot apex. These cells are rich in protoplasm, possess large conspicuous nuclei, "
    "and have thin, cellulosic primary walls with abundant plasmodesmatal connections."))
story.append(b1(
    "<b>Elongation phase:</b> cells proximal (just next) to the meristematic zone. It is "
    "characterised by increased vacuolation, cell enlargement and new cell wall "
    "deposition."))
story.append(b1(
    "<b>Maturation phase:</b> further away from the apex, where cells attain their "
    "maximal size in terms of wall thickening and protoplasmic modifications."))
story.append(figure(
    "fig_13_3.png",
    "<b>Fig. 13.3</b> - Detection of zones of elongation by the parallel line "
    "technique. Zones A, B, C, D immediately behind the apex have elongated most.",
    max_width_cm=8.2))

# ---- 13.1.4 Growth Rates ----  H06, O06, F023-F032
story.append(heading("13.1.4", "Growth Rates", level=2))
story.append(body(
    "The increased growth per unit time is termed the <b>growth rate</b>, and can be "
    "expressed mathematically. The growth rate shows an increase that may be "
    "<b>arithmetic</b> or <b>geometrical</b>."))
story.append(body(
    "In <b>arithmetic growth</b>, following mitotic cell division only one daughter cell "
    "continues to divide while the other differentiates and matures. A root elongating "
    "at a constant rate is the simplest example. It is expressed as:"))
story.append(body("&nbsp;&nbsp;&nbsp;&nbsp;<b>" + EQ_ARITH + "</b>"))
story.append(b2("L<sub>t</sub> = length at time t"))
story.append(b2("L<sub>0</sub> = length at time zero"))
story.append(b2("r = growth rate / elongation per unit time"))
story.append(figure(
    "fig_13_5.png",
    "<b>Fig. 13.5</b> - Constant linear growth, a plot of length L against time t; "
    "the height of the plant increases steadily along a straight line.",
    max_width_cm=7.0))
story.append(body(
    "In <b>geometrical growth</b> the initial growth is slow (<b>lag phase</b>) and then "
    "increases rapidly at an exponential rate (<b>log</b> or <b>exponential phase</b>), "
    "because both progeny cells retain the ability to divide. With a limited nutrient "
    "supply the growth slows down, leading to a <b>stationary phase</b>. Plotting growth "
    "against time gives a typical <b>sigmoid</b> or <b>S-curve</b>, characteristic of "
    "living organisms growing in a natural environment. Exponential growth is expressed "
    "as:"))
story.append(body("&nbsp;&nbsp;&nbsp;&nbsp;<b>" + EQ_EXP + "</b>"))
story.append(b2("W<sub>1</sub> = final size, W<sub>0</sub> = initial size"))
story.append(b2("r = growth rate, t = time of growth"))
story.append(b2("e = base of natural logarithms"))
story.append(body(
    "Here <b>r</b> is the <b>relative growth rate</b> and is also the measure of the "
    "ability of the plant to produce new plant material, referred to as the "
    "<b>efficiency index</b>. Hence, the final size of W<sub>1</sub> depends on the "
    "initial size, W<sub>0</sub>."))
story.append(figure(
    "fig_13_4.png",
    "<b>Fig. 13.4</b> - Diagrammatic representation of: (a) Arithmetic and "
    "(b) Geometric growth, and (c) Stages during embryo development showing the "
    "geometric and arithmetic phases.",
    max_width_cm=12.5))
story.append(body(
    "The measurement and the comparison of total growth per unit time is called the "
    "<b>absolute growth rate</b>. The growth of a system per unit time expressed on a "
    "common basis, for example per unit initial parameter, is called the "
    "<b>relative growth rate</b>."))
story.append(figure(
    "fig_13_7.png",
    "<b>Fig. 13.7</b> - Diagrammatic comparison of absolute and relative growth "
    "rates. Both leaves A and B have increased their area by 5 cm<super>2</super> in a "
    "given time to produce leaves A<super>1</super> and B<super>1</super>.",
    max_width_cm=13.0))
story.append(figure(
    "fig_13_6.png",
    "<b>Fig. 13.6</b> - An idealised sigmoid growth curve, typical of cells in "
    "culture and of many higher plants and plant organs; size/weight of the organ is "
    "plotted against time.",
    max_width_cm=6.6))

# ---- 13.1.5 Conditions for Growth ----  H07, O07, F033-F037
story.append(heading("13.1.5", "Conditions for Growth", level=2))
story.append(body(
    "Why not try to write down what you think are the necessary conditions for growth? "
    "The essential requirements are <b>water</b>, <b>oxygen</b> and <b>nutrients</b>."))
story.append(b1(
    "<b>Water:</b> plant cells grow in size by cell enlargement, which requires water. "
    "Turgidity of cells helps in extension growth, and water also provides the medium "
    "for enzymatic activities needed for growth."))
story.append(b1(
    "<b>Oxygen:</b> helps release metabolic energy essential for growth activities."))
story.append(b1(
    "<b>Nutrients:</b> the macro- and micro-essential elements are required for the "
    "synthesis of protoplasm and act as a source of energy."))
story.append(body(
    "In addition, every plant has an <b>optimum temperature</b> range best suited for "
    "its growth. Environmental signals such as <b>light</b> and <b>gravity</b> also "
    "affect certain phases or stages of growth."))

# ======================================================================================
# ---- 13.2 Differentiation, Dedifferentiation and Redifferentiation ----
#      H08, O08, F038-F043
# ======================================================================================
story.append(heading("13.2", "Differentiation, Dedifferentiation and Redifferentiation",
                      level=1))
story.append(keyterm(
    "The cells derived from the root apical and shoot-apical meristems and the cambium "
    "differentiate and mature to perform specific functions; this act leading to "
    "maturation is termed <b>differentiation</b>."))
story.append(body(
    "During differentiation, cells undergo a few to major structural changes both in "
    "their cell walls and protoplasm. For example, to form a <b>tracheary element</b>, "
    "the cells lose their protoplasm and develop a very strong, elastic, "
    "lignocellulosic secondary cell wall, so that they can carry water even under "
    "tension."))
story.append(keyterm(
    "Living differentiated cells that have lost the capacity to divide can regain it "
    "under certain conditions; this phenomenon is termed <b>dedifferentiation</b> - for "
    "example, the formation of the interfascicular cambium and the cork cambium from "
    "fully differentiated parenchyma cells."))
story.append(body(
    "Such dedifferentiated meristems divide and produce cells that once again lose the "
    "capacity to divide but mature to perform specific functions, that is, they get "
    "<b>redifferentiated</b>. Differentiation in plants is said to be <b>open</b>, "
    "because cells or tissues arising from the same meristem have different structures "
    "at maturity, determined partly by the location of the cell. For instance, cells "
    "positioned away from the root apical meristems differentiate as root-cap cells, "
    "while those pushed to the periphery mature as the epidermis."))

# ======================================================================================
# ---- 13.3 Development ----  H09, O09, F044-F049
# ======================================================================================
story.append(heading("13.3", "Development", level=1))
story.append(body(
    "<b>Development</b> is a term that includes all the changes an organism goes through "
    "during its life cycle, from the germination of the seed to <b>senescence</b>. The "
    "sequence of processes that constitute the development of a single cell of a higher "
    "plant is also broadly applicable to tissues and organs."))
story.append(body(
    "The developmental sequence within a plant cell runs from cell division onward, as "
    "shown in Fig. 13.8:"))
story.append(process_flow([
    "<b>Cell division</b> in a <b>meristematic cell</b> produces new cells.",
    "<b>Plasmatic growth</b> and <b>expansion</b> increase the volume of the cell.",
    "<b>Differentiation</b> and <b>maturation</b> convert it into a <b>mature cell</b> "
    "with a specific function.",
    "<b>Senescence</b> and finally <b>death</b> complete the cell's life cycle.",
]))
story.append(figure(
    "fig_13_8.png",
    "<b>Fig. 13.8</b> - Sequence of the developmental process in a plant cell.",
    max_width_cm=15.0))
story.append(body(
    "Plants follow different pathways in response to the environment or the phases of "
    "life to form different kinds of structures. This ability is called "
    "<b>plasticity</b> - for example, <b>heterophylly</b> in cotton, coriander and "
    "larkspur. In such plants the leaves of the juvenile plant are different in shape "
    "from those of the mature plant. In <b>buttercup</b>, the leaves produced in air are "
    "different from those produced in water - a heterophyllous development caused by the "
    "environment."))
story.append(figure(
    "fig_13_9.png",
    "<b>Fig. 13.9</b> - Heterophylly in (a) larkspur and (b) buttercup.",
    max_width_cm=12.0))
story.append(body(
    "Broadly, <b>development</b> is considered to be the sum of <b>growth</b> and "
    "<b>differentiation</b>. Development in plants is under the control of both "
    "<b>intrinsic</b> and <b>extrinsic</b> factors. The intrinsic factors include "
    "<b>intracellular</b> (genetic) and <b>intercellular</b> factors (chemicals such as "
    "plant growth regulators), while the extrinsic factors include light, temperature, "
    "water, oxygen and nutrition."))

# ======================================================================================
# ---- 13.4 Plant Growth Regulators ----  H10
# ======================================================================================
story.append(heading("13.4", "Plant Growth Regulators", level=1))

# ---- 13.4.1 Characteristics ----  H11, O10, F050-F054
story.append(heading("13.4.1", "Characteristics", level=2))
story.append(body(
    "The <b>plant growth regulators (PGRs)</b> are small, simple molecules of diverse "
    "chemical composition. They may be indole compounds (indole-3-acetic acid, IAA), "
    "adenine derivatives (kinetin), derivatives of carotenoids (abscisic acid, ABA), "
    "terpenes (gibberellic acid, " + GA3 + ") or gases (ethylene, " + C2H4 + "). PGRs "
    "are also called <b>plant growth substances</b>, <b>plant hormones</b> or "
    "<b>phytohormones</b>."))
story.append(body(
    "Based on their action, PGRs fall into two broad groups:"))
story.append(b1(
    "<b>Growth promoters</b> are involved in growth-promoting activities such as cell "
    "division, cell enlargement, pattern formation, tropic growth, flowering, fruiting "
    "and seed formation - for example, <b>auxins</b>, <b>gibberellins</b> and "
    "<b>cytokinins</b>."))
story.append(b1(
    "<b>Growth inhibitors</b> act in responses to wounds and stresses and in "
    "growth-inhibiting activities such as dormancy and abscission - <b>abscisic acid "
    "(ABA)</b> belongs to this group. The gaseous PGR <b>ethylene</b> could fit either "
    "group, but it is largely an inhibitor of growth activities."))
story.append(data_table([
    ["PGR group", "Chemical nature", "Example"],
    ["Auxins", "Indole compounds", "IAA"],
    ["Gibberellins", "Terpenes", GA3],
    ["Cytokinins", "Adenine derivatives", "Kinetin, zeatin"],
    ["Abscisic acid", "Carotenoid derivatives", "ABA"],
    ["Ethylene", "Gaseous", C2H4],
], col_widths=[3, 4, 3]))

# ---- 13.4.2 The Discovery of Plant Growth Regulators ----  H12, O11, F055-F061
story.append(heading("13.4.2", "The Discovery of Plant Growth Regulators", level=2))
story.append(body(
    "Interestingly, the discovery of each of the five major groups of PGRs has been "
    "<b>accidental</b>."))
story.append(b1(
    "<b>Auxin:</b> Charles Darwin and his son Francis Darwin observed that the "
    "coleoptiles of canary grass grow towards a unilateral source of light "
    "(<b>phototropism</b>). They concluded that the <b>tip of the coleoptile</b> was "
    "the site of a transmittable influence that caused the bending of the entire "
    "coleoptile. <b>Auxin</b> was subsequently isolated by <b>F. W. Went</b> from the "
    "tips of coleoptiles of oat seedlings."))
story.append(b1(
    "<b>Gibberellin:</b> the <b>bakanae</b> (foolish seedling) disease of rice seedlings "
    "was caused by the fungal pathogen <i>Gibberella fujikuroi</i>. <b>E. Kurosawa "
    "(1926)</b> reported the appearance of the disease symptoms in rice seedlings "
    "treated with sterile filtrates of the fungus; the active substance was later "
    "identified as <b>gibberellic acid</b>."))
story.append(b1(
    "<b>Cytokinin:</b> F. Skoog and co-workers found that the callus (a mass of cells) "
    "from tobacco stem internodes proliferated only if the nutrient medium contained, "
    "in addition to auxins, the extracts of vascular tissues, yeast extract, coconut "
    "milk or DNA. <b>Miller et al. (1955)</b> finally identified and crystallised the "
    "cytokinesis-promoting active substance and termed it <b>kinetin</b>."))
story.append(b1(
    "<b>Abscisic acid:</b> in the mid-1960s, three independent researches reported the "
    "purification and chemical characterisation of three different kinds of inhibitors - "
    "<b>inhibitor-B</b>, <b>abscission II</b> and <b>dormin</b>. Later, all three "
    "proved to be chemically identical and were named <b>abscisic acid (ABA)</b>."))
story.append(b1(
    "<b>Ethylene:</b> <b>H. H. Cousins (1910)</b> confirmed the release of a volatile "
    "substance from ripened oranges that hastened the ripening of stored bananas. This "
    "volatile substance was later identified as <b>ethylene</b>, a gaseous PGR."))
story.append(figure(
    "fig_13_10.png",
    "<b>Fig. 13.10</b> - Experiment used to demonstrate that the tip of the coleoptile "
    "is the source of auxin. Arrows indicate the direction of light.",
    max_width_cm=8.5))

# ---- 13.4.3 Physiological Effects of Plant Growth Regulators ----  H13
story.append(heading("13.4.3", "Physiological Effects of Plant Growth Regulators",
                      level=2))

# ---- 13.4.3.1 Auxins ----  H14, O12, F062-F066
story.append(heading("13.4.3.1", "Auxins", level=3))
story.append(body(
    "<b>Auxins</b> (from the Greek word 'auxein', meaning to grow) were first isolated "
    "from human urine. The term 'auxin' is applied to the indole-3-acetic acid (IAA) and "
    "to other natural and synthetic compounds having certain growth-regulating "
    "properties. Auxins are generally produced by the growing apices of the stems and "
    "roots, from where they migrate to the regions of their action. <b>IAA</b> and "
    "<b>IBA</b> (indole butyric acid) are natural auxins, whereas <b>NAA</b> "
    "(naphthalene acetic acid) and <b>2,4-D</b> (2,4-dichlorophenoxyacetic acid) are "
    "synthetic auxins."))
story.append(b1(
    "They help initiate rooting in stem cuttings, an application widely used for plant "
    "propagation."))
story.append(b1(
    "Auxins promote flowering (for example in pineapples), and help to prevent the "
    "early drop of fruits and leaves while promoting the abscission of older, mature "
    "leaves and fruits."))
story.append(b1(
    "The growing apical bud inhibits the growth of the lateral (axillary) buds, a "
    "phenomenon called <b>apical dominance</b>. Removal of the shoot tips "
    "(<b>decapitation</b>) usually results in the growth of the lateral buds - a "
    "principle applied in tea plantations and in hedge-making."))
story.append(b1(
    "Auxins induce <b>parthenocarpy</b>, for example in tomatoes. They are also widely "
    "used as <b>herbicides</b>: <b>2,4-D</b> is used to kill dicotyledonous weeds "
    "without affecting the mature monocotyledonous plants. Auxins also control xylem "
    "differentiation and help in cell division."))
story.append(figure(
    "fig_13_11.png",
    "<b>Fig. 13.11</b> - Apical dominance in plants: (a) A plant with the apical bud "
    "intact; (b) A plant with the apical bud removed. Note the growth of the lateral "
    "buds into branches after decapitation.",
    max_width_cm=8.5))

# ---- 13.4.3.2 Gibberellins ----  H15, O13, F067-F070
story.append(heading("13.4.3.2", "Gibberellins", level=3))
story.append(body(
    "<b>Gibberellins</b> are another kind of promotory PGR. There are more than 100 "
    "gibberellins reported from a wide range of organisms such as fungi and higher "
    "plants. They are denoted as GA<sub>1</sub>, GA<sub>2</sub>, GA<sub>3</sub> and so "
    "on. <b>" + GA3 + "</b> was one of the first gibberellins to be discovered and "
    "remains the most intensively studied; all gibberellins are acidic."))
story.append(b1(
    "They increase the length of the axis, and so are used to lengthen the stalks of "
    "grapes. They also cause fruits such as apples to elongate and improve their shape, "
    "and can delay senescence."))
story.append(b1(
    "<b>" + GA3 + "</b> is used to speed up the malting process in the brewing industry."))
story.append(b1(
    "Spraying sugarcane crops with gibberellins increases the length of the stem, thus "
    "increasing the yield by as much as <b>20 tonnes per acre</b>. Spraying juvenile "
    "conifers with gibberellins hastens the maturity period, leading to early seed "
    "production."))
story.append(b1(
    "Gibberellins promote <b>bolting</b> (internode elongation just prior to flowering) "
    "in beet, cabbages and many plants with a rosette habit."))

# ---- 13.4.3.3 Cytokinins ----  H16, O14, F071-F073
story.append(heading("13.4.3.3", "Cytokinins", level=3))
story.append(body(
    "<b>Cytokinins</b> have specific effects on <b>cytokinesis</b> (cell division), and "
    "were discovered as <b>kinetin</b> (a modified form of adenine) from autoclaved "
    "herring sperm DNA. Kinetin does not occur naturally as a plant hormone; the natural "
    "cytokinin <b>zeatin</b> was later isolated from corn kernels and coconut milk."))
story.append(b1(
    "Natural cytokinins are synthesised in regions where rapid cell division occurs - "
    "for example, root apices, developing shoot buds and young fruits."))
story.append(b1(
    "They help produce new leaves, chloroplasts in leaves, lateral shoot growth and "
    "adventitious shoot formation."))
story.append(b1(
    "Cytokinins help overcome <b>apical dominance</b>, promote the mobilisation of "
    "nutrients, and delay the senescence of leaves."))

# ---- 13.4.3.4 Ethylene ----  H17, O15, F074-F079
story.append(heading("13.4.3.4", "Ethylene", level=3))
story.append(body(
    "<b>Ethylene</b> is a simple gaseous PGR. It is synthesised in large amounts by "
    "tissues undergoing senescence and by ripening fruits."))
story.append(b1(
    "Ethylene influences the horizontal growth of seedlings, swelling of the axis and "
    "<b>apical hook</b> formation in dicot seedlings. It also promotes the senescence "
    "and abscission of plant organs, especially of leaves and flowers."))
story.append(b1(
    "Ethylene is highly effective in <b>fruit ripening</b>. It enhances the respiration "
    "rate during the ripening of fruits - this rise in the rate of respiration is called "
    "the <b>respiratory climactic</b>."))
story.append(b1(
    "It breaks seed and bud dormancy, initiates germination in peanut seeds and "
    "sprouting of potato tubers. Ethylene also promotes rapid internode and petiole "
    "elongation in deep-water rice plants, helping the leaves and the upper parts of the "
    "shoot to remain above water."))
story.append(b1(
    "It promotes root growth and root hair formation, thus helping the plant to increase "
    "its absorption surface. Ethylene is used to initiate flowering and to synchronise "
    "fruit-set in pineapples, and to induce flowering in mango."))
story.append(b1(
    "The most widely used source of ethylene is <b>ethephon</b>. Ethephon in an aqueous "
    "solution is readily absorbed and transported within the plant and releases ethylene "
    "slowly. Ethephon hastens fruit ripening in tomatoes and apples, and accelerates "
    "abscission in flowers and fruits (thinning of cotton, cherry and walnut). It "
    "promotes female flowers in cucumbers, thereby increasing the yield."))

# ---- 13.4.3.5 Abscisic acid ----  H18, O16, F080-F084
story.append(heading("13.4.3.5", "Abscisic acid", level=3))
story.append(body(
    "As mentioned earlier, <b>abscisic acid (ABA)</b> was discovered for its role in "
    "regulating <b>abscission</b> and <b>dormancy</b>. Like other PGRs, it has a wide "
    "range of effects; in general, ABA acts as a plant growth inhibitor and an inhibitor "
    "of plant metabolism."))
story.append(b1(
    "ABA inhibits seed germination."))
story.append(b1(
    "ABA stimulates the closure of stomata in the epidermis and increases the tolerance "
    "of plants to various kinds of stresses. It is therefore also called the "
    "<b>stress hormone</b>."))
story.append(b1(
    "ABA plays an important role in seed development, maturation and dormancy, helping "
    "the seeds to withstand desiccation and other unfavourable factors for growth. In "
    "most situations ABA acts as an <b>antagonist</b> to gibberellins."))
story.append(body(
    "For every phase of growth, differentiation and development, one or more PGRs have a "
    "role to play. Their effects may be <b>complementary</b> or <b>antagonistic</b>, and "
    "they may act <b>individualistically</b> or <b>synergistically</b>. Events such as "
    "dormancy, abscission, senescence and apical dominance each involve more than one "
    "PGR."))
story.append(note(
    "PGR-mediated control is only one kind of intrinsic control. Together with genomic "
    "control and the extrinsic factors - especially temperature and light - the PGRs "
    "regulate events such as vernalisation, flowering, dormancy, seed germination and "
    "plant movements."))

# ======================================================================================
# ---- Quick Recap (SS5 item 8 - rewritten summary) ----  H19
# ======================================================================================
story.append(PageBreak())
story.append(heading("", "Quick Recap", level=1))
story.append(b1(
    "<b>Growth</b> is the irreversible, permanent increase in size of an organ, its "
    "parts, or a cell; it is measured by parameters such as size, area, length, height, "
    "volume and cell number, and reflects an increase in protoplasmic material."))
story.append(b1(
    "<b>Meristems</b> are the sites of growth. Root and shoot apical meristems (and "
    "intercalary meristems) drive elongation and primary growth; the lateral meristems "
    "add girth in secondary growth. Because new cells are continually added, growth in "
    "higher plants is <b>indeterminate</b> (open)."))
story.append(b1(
    "Growth rate may be <b>arithmetic</b> (" + EQ_ARITH + ") or <b>geometrical</b> "
    "(" + EQ_EXP + "). Over the life of an organ, growth passes through a lag phase, a "
    "log (exponential) phase and a senescent (stationary) phase, giving the "
    "characteristic <b>sigmoid</b> growth curve. Absolute and relative growth rates "
    "allow growth to be compared."))
story.append(b1(
    "<b>Differentiation</b> is the maturation of meristem-derived cells into specific "
    "functions. <b>Dedifferentiation</b> restores dividing capacity to mature cells, "
    "and <b>redifferentiation</b> matures them again. Both growth and differentiation in "
    "higher plants are <b>open</b>."))
story.append(b1(
    "<b>Development</b> = growth + differentiation, and it is flexible: <b>plasticity</b> "
    "lets a plant form different structures (as in heterophylly). Development is "
    "controlled by <b>intrinsic</b> factors (genetic and chemical, the PGRs) and "
    "<b>extrinsic</b> factors (light, temperature, nutrition, oxygen, water and "
    "gravity)."))
story.append(b1(
    "The five major groups of <b>plant growth regulators</b> are <b>auxins</b>, "
    "<b>gibberellins</b>, <b>cytokinins</b>, <b>abscisic acid</b> and <b>ethylene</b>. "
    "They are synthesised in various plant parts, have diverse physiological effects, "
    "and act either <b>synergistically</b> or <b>antagonistically</b> - for example, ABA "
    "opposes the gibberellins."))


if __name__ == "__main__":
    sys.exit(build_pdf(
        OUT_PDF, story,
        title="Class 11 Chapter 13 - Plant Growth and Development (NEET notes)",
        subject="NEET Biology"))
