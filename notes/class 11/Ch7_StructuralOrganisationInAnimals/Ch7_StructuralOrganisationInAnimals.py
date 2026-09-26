"""
NCERT Class 11 Biology, Chapter 7 - Structural Organisation in Animals
NEET replacement notes -> A4 print-ready PDF.

Built under SUPREME COMMAND PROMPT.md v6, Pass 2 (GATE_2_PASS_2_BUILD_AND_LINT.md):
written linearly from the frozen 398-row inventory
(Ch7_StructuralOrganisationInAnimals_inventory.md) in Content Order (SS5),
importing the repo-level frozen style module `neet_template.py` (SS0.6). No style,
geometry, colour or font is re-declared here.

SCOPE NOTE: Earthworm (section 7.3) has been removed from the NEET syllabus and is
intentionally excluded, matching the frozen inventory. The supplied source edition
also omits printed pages 107-110 / Figures 7.9-7.13; none were imported from another
edition. The chapter therefore runs intro -> 7.1 -> 7.2 -> 7.4 -> 7.5.

Block markers `# ---- N.N ----` mark every NCERT section so a Pass 3 flag can be
found and fixed in one contiguous block. Inventory row IDs are named in the comments.

FIGURE LABELS:
All 17 figures retain their printed labels in the artwork. At the user's request,
redundant per-figure label-transcription NOTE boxes are omitted. As a result, text-
extraction-based label coverage in check_pdf.py check 6 is no longer expected to pass.

SUMMARY-UNIQUE folding (SS3, Rule 3): the 14 SUMMARY-UNIQUE facts (F368-F381) are
folded into their planned body homes AND restated in the Quick Recap. Fold points
are commented inline as [FOLD Fxxx - SUMMARY-UNIQUE].

Subscripts / Greek / arrows: this chapter has none (no chemical formulae). Only ASCII
hyphens, slashes and straight quotes are used, so check 5 has nothing to escape. The
source fraction glyph in "1/4 inches" is written as ASCII "1/4" (never U+00BC).

Source: Chapter/class 11/Chapter 07 - Structural Organisation in Animals.pdf
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
    STYLES, FRAME_WIDTH,
    heading, keyterm, process_flow, note, memory_aid, data_table, title_block, build_pdf,
)
from neet_template import figure as _shared_figure  # noqa: E402
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch7_StructuralOrganisationInAnimals.pdf")


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
# ---- Title block (SS5 item 1) ---- F340 (chapter heading)
# ======================================================================================
story += title_block("Structural Organisation in Animals")

# ======================================================================================
# ---- intro ---- F001-F010, F355 opener (+ folded summary F368; S01)
# ======================================================================================
# F355 opener + F001-F002
story.append(body(
    "In the animal kingdom you meet a large variety of organisms, both unicellular and "
    "multicellular. In <b>unicellular organisms</b>, all functions like <b>digestion, "
    "respiration and reproduction</b> are performed by a <b>single cell</b>. In the complex "
    "body of <b>multicellular animals</b> the same basic functions are carried out by "
    "<b>different groups of cells</b> in a well organised manner."))  # F001, F002

story.append(body(
    "The body of a simple organism like <b>Hydra</b> is made of different types of cells, and "
    "the number of cells in each type can be in <b>thousands</b>. The <b>human body</b> is "
    "composed of <b>billions of cells</b> to perform various functions."))  # F003, F004

# F005, F006 + [FOLD F368 - SUMMARY-UNIQUE] add "one or more functions" to the definition (S02)
story.append(keyterm(
    "<b>Tissue</b> - in multicellular animals, a <b>group of similar cells</b> along with "
    "<b>intercellular substances</b> that together perform a <b>specific function</b> (one or "
    "more functions) in the body."))  # F005 + F006 term, F368 fold

story.append(body(
    "You may be surprised to know that <b>all complex animals consist of only four basic types "
    "of tissues</b>. These tissues are organised in specific proportion and pattern to form an "
    "<b>organ</b> like stomach, lung, heart and kidney. When <b>two or more organs</b> perform a "
    "common function by their physical and/or chemical interaction, they together form an "
    "<b>organ system</b>, e.g., digestive system, respiratory system, etc."))  # F007, F008, F009

# F010 (S01 BODY-PRESENT)
story.append(body(
    "<b>Cells, tissues, organs and organ systems</b> split up the work in a way that exhibits "
    "<b>division of labour</b> and contribute to the <b>survival of the body as a whole</b>."))  # F010

# ======================================================================================
# ---- 7.1  ANIMAL TISSUES ---- F011-F012, F341 heading, F356 opener
# ======================================================================================
story.append(heading("7.1", "Animal Tissues", level=1))

# F356 opener + F011, F012
story.append(body(
    "The <b>structure of the cells vary according to their function</b>. Therefore, the tissues "
    "are different and are broadly classified into <b>four types</b>: (i) <b>Epithelial</b>, "
    "(ii) <b>Connective</b>, (iii) <b>Muscular</b> and (iv) <b>Neural</b>."))  # F011, F012

# ======================================================================================
# ---- 7.1.1  Epithelial Tissue ---- F013-F049, F342 heading, F357 opener
#             (+ folded summary F369; Figs 7.1, 7.2, 7.3)
# ======================================================================================
story.append(heading("7.1.1", "Epithelial Tissue", level=2))

# F357 opener + F013, F014
story.append(body(
    "We commonly refer to an epithelial tissue as <b>epithelium</b> (pl.: epithelia). This "
    "tissue has a <b>free surface</b>, which faces either a body fluid or the outside "
    "environment and thus provides a <b>covering or a lining</b> for some part of the body. "
    # [FOLD F369 - SUMMARY-UNIQUE] sheet-like form + full locations, summary-only (S03)
    "Epithelia are <b>sheet-like tissues</b> lining the body's surface and its "
    "<b>cavities, ducts and tubes</b>."))  # F013, F014 + F369 fold

story.append(body(
    "The cells are <b>compactly packed with little intercellular matrix</b>. There are "
    "<b>two types</b> of epithelial tissues namely <b>simple epithelium</b> and <b>compound "
    "epithelium</b>. <b>Simple epithelium</b> is composed of a <b>single layer of cells</b> and "
    "functions as a lining for body cavities, ducts and tubes. The <b>compound epithelium</b> "
    "consists of <b>two or more cell layers</b> and has a <b>protective function</b> as it does "
    "in our skin."))  # F015, F016, F017, F018

story.append(body(
    "On the basis of structural modification of the cells, <b>simple epithelium</b> is further "
    "divided into <b>three types</b> (Figure 7.1): (i) <b>Squamous</b>, (ii) <b>Cuboidal</b>, "
    "(iii) <b>Columnar</b>."))  # F019, F020

# Simple epithelium comparison table (enumerable/comparative prose -> table, SS4)
story.append(data_table([
    ["Simple epithelium", "Structure", "Location", "Main function"],
    ["Squamous",
     "Single thin layer of flattened cells with irregular boundaries",
     "Walls of blood vessels and air sacs of lungs",
     "Forms a diffusion boundary"],
    ["Cuboidal",
     "Single layer of cube-like cells",
     "Ducts of glands and tubular parts of nephrons in kidneys",
     "Secretion and absorption"],
    ["Columnar",
     "Single layer of tall and slender cells; nuclei at the base; free surface may have microvilli",
     "Lining of stomach and intestine",
     "Secretion and absorption"],
], col_widths=[1.3, 3.0, 2.8, 2.2]))  # F021, F022, F023, F024, F026, F027, F028, F029

story.append(body(
    "The epithelium of the <b>proximal convoluted tubule (PCT)</b> of the nephron in the kidney "
    "has <b>microvilli</b>."))  # F025

story.append(b1(
    "If the columnar or cuboidal cells bear <b>cilia</b> on their free surface they are called "
    "<b>ciliated epithelium</b> (Figure 7.1d). Their function is to <b>move particles or mucus "
    "in a specific direction</b> over the epithelium. They are mainly present in the inner "
    "surface of <b>hollow organs like bronchioles and fallopian tubes</b>."))  # F030, F031, F032

story.append(b1(
    "Some of the columnar or cuboidal cells get specialised for secretion and are called "
    "<b>glandular epithelium</b> (Figure 7.2). They are mainly of two types: <b>unicellular</b>, "
    "consisting of isolated glandular cells (<b>goblet cells</b> of the alimentary canal), and "
    "<b>multicellular</b>, consisting of a cluster of cells (<b>salivary gland</b>)."))  # F033, F034

# --- Fig 7.1 ---
story.append(figure(
    "fig_7_1.png",
    "Figure 7.1 Simple epithelium: (a) Squamous (b) Cuboidal (c) Columnar "
    "(d) Columnar cells bearing cilia"))  # F323 caption

# --- Fig 7.2 ---
story.append(figure(
    "fig_7_2.png",
    "Figure 7.2 Glandular epithelium: (a) Unicellular (b) Multicellular"))  # F324 caption

# Glands: exocrine vs endocrine (comparative -> table)
story.append(body(
    "On the basis of the <b>mode of pouring of their secretions</b>, glands are divided into "
    "two categories namely <b>exocrine</b> and <b>endocrine</b> glands."))  # F035
story.append(data_table([
    ["Gland type", "Duct", "Secretions"],
    ["Exocrine",
     "Products released through ducts or tubes",
     "Mucus, saliva, earwax, oil, milk, digestive enzymes and other cell products"],
    ["Endocrine",
     "Do not have ducts",
     "Hormones, secreted directly into the fluid bathing the gland"],
], col_widths=[1.4, 3.2, 4.4]))  # F036, F037, F038, F039

# Compound epithelium (F040-F042) + Fig 7.3
story.append(body(
    "<b>Compound epithelium</b> is made of <b>more than one layer</b> (multi-layered) of cells "
    "and thus has a <b>limited role in secretion and absorption</b> (Figure 7.3). Their main "
    "function is to <b>provide protection against chemical and mechanical stresses</b>. They "
    "cover the <b>dry surface of the skin</b>, the moist surface of <b>buccal cavity, "
    "pharynx</b>, inner lining of ducts of <b>salivary glands</b> and of <b>pancreatic "
    "ducts</b>."))  # F040, F041, F042

story.append(figure(
    "fig_7_3.png",
    "Figure 7.3 Compound epithelium"))  # F325 caption

# Cell junctions (F043-F049)
story.append(body(
    "All cells in epithelium are held together with <b>little intercellular material</b>. In "
    "nearly all animal tissues, <b>specialised junctions</b> provide both <b>structural and "
    "functional links</b> between its individual cells. <b>Three types of cell junctions</b> "
    "are found in the epithelium and other tissues. These are called <b>tight, adhering and gap "
    "junctions</b>."))  # F043, F044, F045, F046
story.append(data_table([
    ["Cell junction", "Function"],
    ["Tight junctions", "Help to stop substances from leaking across a tissue"],
    ["Adhering junctions", "Perform cementing to keep neighbouring cells together"],
    ["Gap junctions",
     "Facilitate the cells to communicate with each other by connecting the cytoplasm of "
     "adjoining cells, for rapid transfer of ions, small molecules and sometimes big molecules"],
], col_widths=[1.8, 6.2]))  # F047, F048, F049

# ======================================================================================
# ---- 7.1.2  Connective Tissue ---- F050-F083, F343 heading, F358 opener
#             (+ folded summary F370-F374, F376; Figs 7.4, 7.5, 7.6)
# ======================================================================================
story.append(heading("7.1.2", "Connective Tissue", level=2))

# F358 opener + F050, F051 + folded functions
story.append(body(
    "<b>Connective tissues</b> are <b>most abundant and widely distributed</b> in the body of "
    "complex animals. They are named connective tissues because of their special function of "
    "<b>linking and supporting</b> other tissues/organs of the body. "
    # [FOLD F370 - SUMMARY-UNIQUE] full function list, summary-only (S06)
    "Diverse types of connective tissues <b>bind together, support, strengthen, protect, and "
    "insulate</b> other tissue in the body. "
    # [FOLD F376 - SUMMARY-UNIQUE] connective tissue covers all three tissue types (S16)
    "<b>Connective tissue covers all three</b> of the other tissue types."))  # F050, F051, F370, F376

story.append(body(
    "They range from <b>soft connective tissues</b> to <b>specialised types</b>, which include "
    "<b>cartilage, bone, adipose, and blood</b>. In all connective tissues <b>except blood</b>, "
    "the cells secrete <b>fibres of structural proteins called collagen or elastin</b>. The "
    "fibres provide <b>strength, elasticity and flexibility</b> to the tissue. These cells also "
    "secrete <b>modified polysaccharides</b>, which accumulate between cells and fibres and act "
    "as <b>matrix (ground substance)</b>. "
    # [FOLD F371 - SUMMARY-UNIQUE] soft connective tissue composition (S07)
    "In short, <b>soft connective tissues</b> consist of <b>protein fibres</b> as well as a "
    "variety of <b>cells arranged in a ground substance</b>."))  # F052, F053, F054, F055, F371

story.append(body(
    "Connective tissues are classified into <b>three types</b>: (i) <b>Loose connective "
    "tissue</b>, (ii) <b>Dense connective tissue</b> and (iii) <b>Specialised connective "
    "tissue</b>."))  # F056

# Loose connective tissue (F057-F062) + Fig 7.4
story.append(heading("A", "Loose Connective Tissue", level=3))
story.append(b1(
    "<b>Loose connective tissue</b> has cells and fibres <b>loosely arranged in a semi-fluid "
    "ground substance</b>, for example, <b>areolar tissue</b> present beneath the skin (Figure "
    "7.4). Often it serves as a <b>support framework for epithelium</b>. It contains "
    "<b>fibroblasts</b> (cells that produce and secrete fibres), <b>macrophages</b> and "
    "<b>mast cells</b>."))  # F057, F058, F059
story.append(b1(
    "<b>Adipose tissue</b> is another type of <b>loose connective tissue</b> located mainly "
    "beneath the skin. The cells of this tissue are <b>specialised to store fats</b>. The excess "
    "of nutrients which are not used immediately are <b>converted into fats</b> and are stored "
    "in this tissue. "
    # [FOLD F374 - SUMMARY-UNIQUE] adipose = reservoir of stored energy (S11)
    "Thus adipose tissue is a <b>reservoir of stored energy</b>."))  # F060, F061, F062, F374

story.append(figure(
    "fig_7_4.png",
    "Figure 7.4 Loose connective tissue: (a) Areolar tissue (b) Adipose tissue"))  # F326 caption

# Dense connective tissue (F063-F068) + Fig 7.5
story.append(heading("B", "Dense Connective Tissue", level=3))
story.append(body(
    "<b>Fibres and fibroblasts</b> are <b>compactly packed</b> in the dense connective tissues. "
    "Orientation of fibres shows a <b>regular or irregular pattern</b> and they are called "
    "<b>dense regular</b> and <b>dense irregular</b> tissues."))  # F063, F064
story.append(b1(
    "In the <b>dense regular</b> connective tissues, the <b>collagen fibres</b> are present in "
    "rows between many parallel bundles of fibres. <b>Tendons</b>, which attach skeletal muscles "
    "to bones, and <b>ligaments</b>, which attach one bone to another, are examples of this "
    "tissue."))  # F065, F066
story.append(b1(
    "<b>Dense irregular</b> connective tissue has fibroblasts and many fibres (mostly collagen) "
    "that are <b>oriented differently</b> (Figure 7.5). This tissue is present in the "
    "<b>skin</b>."))  # F067, F068

story.append(figure(
    "fig_7_5.png",
    "Figure 7.5 Dense connective tissue: (a) Dense regular (b) Dense irregular"))  # F327 caption

# Specialised connective tissue (F069-F083) + Fig 7.6
story.append(heading("C", "Specialised Connective Tissue", level=3))
story.append(body(
    "<b>Cartilage, bones and blood</b> are various types of <b>specialised connective "
    "tissues</b>. "
    # [FOLD F372 - SUMMARY-UNIQUE] summary classification includes adipose (source inconsistency, S08)
    "(The chapter <b>summary</b> classifies <b>cartilage, bone, blood, and adipose tissue</b> "
    "together as specialised connective tissues; section 7.1.2 above first classifies adipose "
    "as a loose connective tissue. Both source statements are preserved as written.) "
    # [FOLD F373 - SUMMARY-UNIQUE] cartilage and bone are both structural materials (S09)
    "<b>Cartilage and bone are both structural materials.</b>"))  # F069 + F372, F373

story.append(keyterm(
    "<b>Cartilage</b> - its intercellular material is <b>solid and pliable</b> and <b>resists "
    "compression</b>. Cells of this tissue (<b>chondrocytes</b>) are enclosed in <b>small "
    "cavities within the matrix</b> secreted by them (Figure 7.6a)."))  # F070, F071
story.append(b1(
    "Most of the cartilages in <b>vertebrate embryos are replaced by bones in adults</b>. In "
    "adults, cartilage is present in the <b>tip of nose, outer ear joints, between adjacent "
    "bones of the vertebral column, limbs and hands</b>."))  # F072, F073

story.append(keyterm(
    "<b>Bone</b> - has a <b>hard and non-pliable ground substance rich in calcium salts and "
    "collagen fibres</b> which give bone its strength (Figure 7.6b). It is the <b>main tissue "
    "that provides structural frame to the body</b>."))  # F074, F075
story.append(b1(
    "Bones <b>support and protect softer tissues and organs</b>. The bone cells "
    "(<b>osteocytes</b>) are present in the spaces called <b>lacunae</b>."))  # F076, F077
story.append(b1(
    "<b>Limb bones</b>, such as the long bones of the legs, serve <b>weight-bearing "
    "functions</b>. They also interact with <b>skeletal muscles</b> attached to them to bring "
    "about movements. The <b>bone marrow</b> in some bones is the <b>site of production of "
    "blood cells</b>."))  # F078, F079, F080

story.append(keyterm(
    "<b>Blood</b> - a <b>fluid connective tissue</b> containing <b>plasma, red blood cells "
    "(RBC), white blood cells (WBC) and platelets</b> (Figure 7.6c). It is the main "
    "<b>circulating fluid</b> that helps in the <b>transport of various substances</b>."))  # F081, F082
story.append(body(
    "You will learn more about blood in <b>Chapters 17 and 18</b>."))  # F083

story.append(figure(
    "fig_7_6.png",
    "Figure 7.6 Specialised connective tissues: (a) Cartilage (b) Bone (c) Blood"))  # F328 caption

# ======================================================================================
# ---- 7.1.3  Muscle Tissue ---- F084-F100, F344 heading, F359 opener
#             (+ folded summary F375; Fig 7.7)
# ======================================================================================
story.append(heading("7.1.3", "Muscle Tissue", level=2))

# F359 opener + F084-F088
story.append(body(
    "Each muscle is made of many <b>long, cylindrical fibres</b> arranged in <b>parallel "
    "arrays</b>. These fibres are composed of numerous fine fibrils, called <b>myofibrils</b>. "
    "Muscle fibres <b>contract (shorten)</b> in response to stimulation, then <b>relax "
    "(lengthen)</b> and return to their uncontracted state in a coordinated fashion. Their "
    "action moves the body to <b>adjust to changes in the environment</b> and to <b>maintain "
    "the positions of the various parts of the body</b>. In general, muscles play an "
    "<b>active role in all the movements of the body</b>."))  # F084, F085, F086, F087, F088

story.append(body(
    "Muscles are of <b>three types</b>: <b>skeletal, smooth</b>, and <b>cardiac</b> (Figure "
    "7.7)."))  # F089

# Muscle comparison table (comparative -> table, SS4)
story.append(data_table([
    ["Muscle", "Striations", "Location", "Control / junctions"],
    ["Skeletal",
     "Striated (striped)",
     "Closely attached to skeletal bones; e.g., biceps - fibres bundled in a parallel fashion, "
     "several bundles enclosed by a sheath of tough connective tissue",
     "Voluntary (learn more in Chapter 20)"],
    ["Smooth",
     "No striations; fibres taper at both ends (fusiform)",
     "Wall of internal organs such as blood vessels, stomach and intestine",
     "Involuntary - functioning cannot be directly controlled; cell junctions hold fibres "
     "together, bundled in a connective tissue sheath"],
    ["Cardiac",
     "Contractile tissue",
     "Present only in the heart",
     "Cell junctions fuse the plasma membranes; communication junctions (intercalated discs) "
     "let the cells contract as a unit"],
], col_widths=[1.1, 1.7, 3.0, 3.0]))
# F090, F091, F092, F093, F094, F095, F096, F097, F098, F099, F100

# [FOLD F375 - SUMMARY-UNIQUE] cardiac muscle makes up contractile walls of the heart (S15)
story.append(body(
    "<b>Cardiac muscle</b> makes up the <b>contractile walls of the heart</b>: when one cell "
    "receives a signal to contract, its neighbours are also stimulated to contract."))  # F100 + F375

story.append(figure(
    "fig_7_7.png",
    "Figure 7.7 Muscle tissue: (a) Skeletal (striated) muscle tissue (b) Smooth muscle tissue "
    "(c) Cardiac muscle tissue"))  # F329 caption

# ======================================================================================
# ---- 7.1.4  Neural Tissue ---- F101-F106, F345 heading, F360 opener (Fig 7.8)
# ======================================================================================
story.append(heading("7.1.4", "Neural Tissue", level=2))

# F360 opener + F101-F104
story.append(body(
    "<b>Neural tissue</b> exerts the <b>greatest control</b> over the body's responsiveness to "
    "changing conditions. <b>Neurons</b>, the unit of the neural system, are <b>excitable "
    "cells</b> (Figure 7.8). The <b>neuroglial cells</b>, which constitute the rest of the "
    "neural system, <b>protect and support neurons</b>. Neuroglia make up <b>more than one-half "
    "the volume</b> of neural tissue in our body."))  # F101, F102, F103, F104

story.append(body(
    "When a neuron is suitably stimulated, an <b>electrical disturbance</b> is generated which "
    "swiftly travels along its <b>plasma membrane</b>. Arrival of the disturbance at the "
    "neuron's endings, or <b>output zone</b>, triggers events that may cause <b>stimulation or "
    "inhibition</b> of adjacent neurons and other cells (details in <b>Chapter 21</b>)."))  # F105, F106

story.append(figure(
    "fig_7_8.png",
    "Figure 7.8 Neural tissue (Neuron with neuroglea)"))  # F330 caption

# ======================================================================================
# ---- 7.2  ORGAN AND ORGAN SYSTEM ---- F107-F117, F346 heading, F361 opener
# ======================================================================================
story.append(heading("7.2", "Organ and Organ System", level=1))

# F361 opener + F107-F110
story.append(body(
    "The basic tissues mentioned above <b>organise to form organs</b> which in turn associate "
    "to form <b>organ systems</b> in the multicellular organisms. Such an organisation is "
    "essential for <b>more efficient and better coordinated activities</b> of millions of cells "
    "constituting an organism. <b>Each organ</b> in our body is made of <b>one or more type of "
    "tissues</b>. For example, our <b>heart</b> consists of <b>all the four types of tissues</b> "
    "- epithelial, connective, muscular and neural."))  # F107, F108, F109, F110

story.append(body(
    "We also notice, after some careful study, that the complexity in organ and organ systems "
    "displays a certain discernable trend. This is called the <b>evolutionary trend</b> "
    "(details in class XII). You are being introduced to the <b>morphology and anatomy of three "
    "organisms at different evolutionary levels</b> to show their organisation and "
    "functioning."))  # F111, F112, F113

story.append(keyterm(
    "<b>Morphology</b> - the study of <b>form or externally visible features</b>. In plants or "
    "microbes, the term morphology precisely means only this; in animals it refers to the "
    "<b>external appearance</b> of the organs or parts of the body."))  # F114, F115, F116
story.append(keyterm(
    "<b>Anatomy</b> - conventionally used for the study of the <b>morphology of internal "
    "organs</b> in animals."))  # F117

story.append(note(
    "In the requested NEET syllabus, the <b>Earthworm</b> (section 7.3) has been removed, so the "
    "chapter continues from the general organ/organ-system idea directly to the "
    "<b>Cockroach</b> and the <b>Frog</b> as the worked examples of animal organisation."))

# ======================================================================================
# ---- 7.4  COCKROACH ---- F118-F122, F347 heading, F362 opener
# ======================================================================================
story.append(heading("7.4", "Cockroach", level=1))

# F362 opener + F118-F122
story.append(body(
    "<b>Cockroaches</b> are <b>brown or black bodied</b> animals that are included in class "
    "<b>Insecta</b> of Phylum <b>Arthropoda</b>. Bright <b>yellow, red and green</b> coloured "
    "cockroaches have also been reported in tropical regions."))  # F118, F119
story.append(b1(
    "Their <b>size</b> ranges from <b>1/4 inches to 3 inches (0.6-7.6 cm)</b> and they have "
    "<b>long antennae, legs</b> and a <b>flat extension of the upper body wall that conceals the "
    "head</b>."))  # F120
story.append(b1(
    "They are <b>nocturnal omnivores</b> that live in <b>damp places</b> throughout the world. "
    "They have become residents of human homes and thus are <b>serious pests and vectors of "
    "several diseases</b>."))  # F121, F122

# ======================================================================================
# ---- 7.4.1  Morphology ---- F123-F146, F348 heading, F363 opener
#             (+ folded summary F377; Figs 7.14, 7.15)
# ======================================================================================
story.append(heading("7.4.1", "Morphology", level=2))

# F363 opener + F123-F126
story.append(body(
    "The adults of the common species of cockroach, <b>Periplaneta americana</b>, are about "
    "<b>34-53 mm long</b> with <b>wings that extend beyond the tip of the abdomen in males</b>. "
    "The body of the cockroach is <b>segmented</b> and divisible into <b>three distinct "
    "regions</b> - <b>head, thorax and abdomen</b> (Figure 7.14)."))  # F123, F124
story.append(body(
    "The entire body is covered by a <b>hard chitinous exoskeleton</b> (brown in colour). In "
    "each segment, the exoskeleton has hardened plates called <b>sclerites</b> (<b>tergites</b> "
    "dorsally and <b>sternites</b> ventrally) that are joined to each other by a <b>thin and "
    "flexible articular membrane (arthrodial membrane)</b>."))  # F125, F126

story.append(figure(
    "fig_7_14.png",
    "Figure 7.14 External features of cockroach"))  # F331 caption

# Head (F127-F134) + Fig 7.15
story.append(heading("Head", "Head", level=3))
story.append(body(
    "The <b>head</b> is <b>triangular in shape</b> and lies anteriorly at <b>right angles to the "
    "longitudinal body axis</b>. It is formed by the <b>fusion of six segments</b> and shows "
    "<b>great mobility in all directions</b> due to a flexible neck (Figure 7.15)."))  # F127, F128
story.append(b1(
    "The head capsule bears a <b>pair of compound eyes</b>. A pair of <b>thread-like "
    "antennae</b> arise from <b>membranous sockets</b> lying in front of the eyes; antennae have "
    "<b>sensory receptors</b> that help in <b>monitoring the environment</b>."))  # F129, F130, F131
story.append(b1(
    "The anterior end of the head bears appendages forming <b>biting and chewing type of "
    "mouthparts</b>, consisting of a <b>labrum (upper lip)</b>, a pair of <b>mandibles</b>, a "
    "pair of <b>maxillae</b> and a <b>labium (lower lip)</b>. A median flexible lobe, acting as "
    "a tongue (<b>hypopharynx</b>), lies within the cavity enclosed by the mouthparts (Figure "
    "7.15b)."))  # F132, F133, F134

story.append(figure(
    "fig_7_15.png",
    "Figure 7.15 Head region of cockroach: (a) parts of head region (b) mouth parts"))  # F332 caption

# Thorax (F135-F140) + folded F377
story.append(heading("Thorax", "Thorax", level=3))
story.append(body(
    "The <b>thorax</b> consists of <b>three parts</b> - <b>prothorax, mesothorax and "
    "metathorax</b>. The head is connected with the thorax by a short extension of the prothorax "
    "known as the <b>neck</b>. <b>Each thoracic segment bears a pair of walking legs.</b>"))  # F135, F136, F137
story.append(b1(
    "The <b>first pair of wings</b> arises from the <b>mesothorax</b> and the <b>second pair</b> "
    "from the <b>metathorax</b>. "
    # [FOLD F377 - SUMMARY-UNIQUE] two pairs of wings, one pair each on 2nd and 3rd segment (S38)
    "(Thus <b>two pairs of wings</b> are present, <b>one pair each on the 2nd and 3rd "
    "thoracic segment</b>.)"))  # F138 + F377
story.append(b1(
    "<b>Forewings (mesothoracic)</b> called <b>tegmina</b> are <b>opaque, dark and "
    "leathery</b> and cover the hind wings when at rest. The <b>hind wings</b> are "
    "<b>transparent, membranous</b> and are used in <b>flight</b>."))  # F139, F140

# Abdomen (F141-F146)
story.append(heading("Abdomen", "Abdomen", level=3))
story.append(body(
    "The <b>abdomen</b> in both males and females consists of <b>10 segments</b>."))  # F141
story.append(b1(
    "In <b>females</b>, the <b>7th sternum</b> is boat-shaped and together with the <b>8th and "
    "9th sterna</b> forms a <b>brood or genital pouch</b> whose anterior part contains the "
    "<b>female gonopore, spermathecal pores and collateral glands</b>."))  # F142
story.append(b1(
    "In <b>males</b>, the <b>genital pouch or chamber</b> lies at the hind end of the abdomen, "
    "bounded dorsally by the <b>9th and 10th terga</b> and ventrally by the <b>9th sternum</b>. "
    "It contains the <b>dorsal anus, ventral male genital pore and gonapophysis</b>."))  # F143, F144
story.append(b1(
    "Males bear a pair of short, thread-like <b>anal styles</b> which are <b>absent in "
    "females</b>. In both sexes, the <b>10th segment</b> bears a pair of jointed filamentous "
    "structures called <b>anal cerci</b>."))  # F145, F146

# ======================================================================================
# ---- 7.4.2  Anatomy ---- F147-F209, F349 heading, F364 opener
#             (+ folded summary F378, F379; Figs 7.16, 7.17, 7.18)
# ======================================================================================
story.append(heading("7.4.2", "Anatomy", level=2))

# Digestive system (F147-F158) + folded F378 + Fig 7.16
story.append(heading("Dig", "Digestive System", level=3))
# F364 opener + F147
story.append(body(
    "The <b>alimentary canal</b> present in the body cavity is divided into <b>three "
    "regions</b>: <b>foregut, midgut and hindgut</b> (Figure 7.16). "
    # [FOLD F378 - SUMMARY-UNIQUE] a pair of salivary gland near crop (S43)
    "A <b>pair of salivary glands</b> is present near the crop."))  # F147 + F378
story.append(process_flow([
    "The <b>mouth</b> opens into a short tubular <b>pharynx</b>, leading to a narrow tubular "
    "passage called the <b>oesophagus</b>.",
    "The oesophagus opens into a sac-like structure called the <b>crop</b>, used for "
    "<b>storing food</b>.",
    "The crop is followed by the <b>gizzard or proventriculus</b>: it has an outer layer of "
    "thick circular muscles and a thick inner cuticle forming <b>six highly chitinous plates "
    "called teeth</b>, and it <b>helps in grinding the food particles</b>. The entire foregut "
    "is lined by cuticle.",
    "A ring of <b>6-8 blind tubules called hepatic or gastric caeca</b> is present at the "
    "<b>junction of foregut and midgut</b>, which <b>secrete digestive juice</b>.",
    "At the <b>junction of midgut and hindgut</b> is present another ring of <b>100-150 yellow "
    "coloured thin filamentous Malpighian tubules</b>, which <b>help in removal of excretory "
    "products from haemolymph</b>.",
    "The <b>hindgut</b> is broader than the midgut and is differentiated into <b>ileum, colon "
    "and rectum</b>; the <b>rectum opens out through the anus</b>.",
]))  # F148, F149, F150, F151, F152, F153, F154, F155, F156, F157, F158

story.append(figure(
    "fig_7_16.png",
    "Figure 7.16 Alimentary canal of cockroach"))  # F333 caption

# Circulatory system (F159-F165) + Fig 7.17
story.append(heading("Circ", "Circulatory System", level=3))
story.append(body(
    "The <b>blood vascular system</b> of cockroach is an <b>open type</b> (Figure 7.17). Blood "
    "vessels are <b>poorly developed</b> and open into a space (<b>haemocoel</b>). Visceral "
    "organs located in the haemocoel are <b>bathed in blood (haemolymph)</b>. The haemolymph is "
    "composed of <b>colourless plasma and haemocytes</b>."))  # F159, F160, F161, F162
story.append(body(
    "The <b>heart</b> of cockroach consists of an <b>elongated muscular tube</b> lying along the "
    "<b>mid-dorsal line</b> of thorax and abdomen. It is differentiated into <b>funnel-shaped "
    "chambers with ostia</b> on either side. <b>Blood from sinuses enters the heart through "
    "ostia</b> and is <b>pumped anteriorly to the sinuses again</b>."))  # F163, F164, F165

story.append(figure(
    "fig_7_17.png",
    "Figure 7.17 Open circulatory system of cockroach"))  # F334 caption

# Respiratory system (F166-F169)
story.append(heading("Resp", "Respiratory System", level=3))
story.append(body(
    "The <b>respiratory system</b> consists of a <b>network of trachea</b>, that open through "
    "<b>10 pairs of small holes called spiracles</b> present on the lateral side of the body. "
    "<b>Thin branching tubes</b> (tracheal tubes subdivided into <b>tracheoles</b>) carry "
    "<b>oxygen from the air to all the parts</b>. The opening of the spiracles is regulated by "
    "the <b>sphincters</b>. <b>Exchange of gases</b> takes place at the tracheoles by "
    "<b>diffusion</b>."))  # F166, F167, F168, F169

# Excretory system (F170-F174)
story.append(heading("Excr", "Excretory System", level=3))
story.append(body(
    "<b>Excretion</b> is performed by <b>Malpighian tubules</b>. Each tubule is lined by "
    "<b>glandular and ciliated cells</b>. They <b>absorb nitrogenous waste products</b> and "
    "<b>convert them into uric acid</b> which is excreted out through the hindgut. Therefore, "
    "this insect is called <b>uricotelic</b>. In addition, the <b>fat body, nephrocytes and "
    "urecose glands</b> also help in excretion."))  # F170, F171, F172, F173, F174

# Nervous system (F175-F185)
story.append(heading("Nerv", "Nervous System", level=3))
story.append(body(
    "The <b>nervous system</b> of cockroach consists of a series of <b>fused, segmentally "
    "arranged ganglia</b> joined by <b>paired longitudinal connectives</b> on the ventral side. "
    "<b>Three ganglia lie in the thorax, and six in the abdomen.</b> The nervous system is "
    "<b>spread throughout the body</b>: the head holds a bit of it while the rest is situated "
    "along the <b>ventral (belly-side) part</b> of the body."))  # F175, F176, F177, F178
story.append(note(
    "Because the nervous system is spread out, if the head of a cockroach is cut off it will "
    "still <b>live for as long as one week</b>."))  # F179
story.append(body(
    "In the head region, the <b>brain</b> is represented by the <b>supra-oesophageal "
    "ganglion</b> which supplies nerves to the <b>antennae and compound eyes</b>. In cockroach, "
    "the <b>sense organs</b> are <b>antennae, eyes, maxillary palps, labial palps, anal "
    "cerci</b>, etc."))  # F180, F181
story.append(body(
    "The <b>compound eyes</b> are situated at the dorsal surface of the head. Each eye consists "
    "of about <b>2000 hexagonal ommatidia</b> (sing.: ommatidium). With the help of several "
    "ommatidia, a cockroach can receive <b>several images of an object</b>. This kind of vision "
    "is known as <b>mosaic vision</b>, with <b>more sensitivity but less resolution</b>, being "
    "common during night (hence called <b>nocturnal vision</b>)."))  # F182, F183, F184, F185

# Reproductive system (F186-F209) + folded F379 + Fig 7.18
story.append(heading("Repr", "Reproductive System", level=3))
story.append(body(
    "Cockroaches are <b>dioecious</b> and both sexes have <b>well developed reproductive "
    "organs</b> (Figure 7.18)."))  # F186
story.append(b1(
    "The <b>male reproductive system</b> consists of a <b>pair of testes</b>, one lying on each "
    "lateral side in the <b>4th-6th abdominal segments</b>. From each testis arises a thin "
    "<b>vas deferens</b>, which opens into the <b>ejaculatory duct</b> through the <b>seminal "
    "vesicle</b>. The ejaculatory duct opens into the <b>male gonopore</b> situated ventral to "
    "the anus."))  # F187, F188, F189
story.append(b1(
    "A characteristic <b>mushroom-shaped gland</b> is present in the <b>6th-7th abdominal "
    "segments</b> which functions as an <b>accessory reproductive gland</b>. The external "
    "genitalia are represented by <b>male gonapophysis or phallomere</b> (chitinous asymmetrical "
    "structures surrounding the male gonopore)."))  # F190, F191
story.append(b1(
    "The <b>sperms</b> are stored in the seminal vesicles and are glued together in the form of "
    "bundles called <b>spermatophores</b> which are discharged during copulation."))  # F192
story.append(b1(
    "The <b>female reproductive system</b> consists of <b>two large ovaries</b>, lying laterally "
    "in the <b>2nd-6th abdominal segments</b>. Each ovary is formed of a group of <b>eight "
    "ovarian tubules or ovarioles</b>, containing a chain of developing ova. <b>Oviducts</b> of "
    "each ovary unite into a single <b>median oviduct (also called vagina)</b> which opens into "
    "the genital chamber."))  # F193, F194, F195
story.append(b1(
    "A pair of <b>spermatheca</b> is present in the <b>6th segment</b> which opens into the "
    "genital chamber. <b>Sperms are transferred through spermatophores.</b>"))  # F196, F197
story.append(b1(
    "Their <b>fertilised eggs</b> are encased in capsules called <b>oothecae</b>. An ootheca is "
    "a <b>dark reddish to blackish brown capsule, about 3/8 inch (8 mm) long</b>. They are "
    "dropped or glued to a suitable surface, usually in a crack or crevice of <b>high relative "
    "humidity near a food source</b>. On an average, females produce <b>9-10 oothecae, each "
    "containing 14-16 eggs</b>."))  # F198, F199, F200, F201
story.append(b1(
    "The development of <b>P. americana is paurometabolous</b>, meaning there is development "
    "through a <b>nymphal stage</b>. The <b>nymphs look very much like adults</b>. The nymph "
    "grows by <b>moulting about 13 times</b> to reach the adult form. The <b>next to last "
    "nymphal stage has wing pads</b> but only adult cockroaches have wings. "
    # [FOLD F379 - SUMMARY-UNIQUE] one ootheca yields sixteen nymphs (S51)
    "(After the rupturing of a single ootheca, <b>sixteen young ones, called nymphs</b>, come "
    "out.)"))  # F202, F203, F204, F205 + F379

story.append(figure(
    "fig_7_18.png",
    "Figure 7.18 Reproductive system of cockroach: (a) male (b) female"))  # F335 caption

# Economic importance (F206-F209)
story.append(body(
    "<b>Many species</b> of cockroaches are <b>wild</b> and are of <b>no known economic "
    "importance</b> yet. A few species <b>thrive in and around human habitat</b>. They are "
    "<b>pests</b> because they <b>spoil food and contaminate it with their smelly excreta</b>, "
    "and they can <b>transmit a variety of bacterial diseases</b> by contaminating food "
    "material."))  # F206, F207, F208, F209

# ======================================================================================
# ---- 7.5  FROGS ---- F210-F219, F350 heading, F365 opener
# ======================================================================================
story.append(heading("7.5", "Frogs", level=1))

# F365 opener + F210-F213
story.append(body(
    "<b>Frogs</b> can live both on <b>land and in freshwater</b> and belong to class "
    "<b>Amphibia</b> of phylum <b>Chordata</b>. The most common species of frog found in India "
    "is <b>Rana tigrina</b>. They <b>do not have a constant body temperature</b> - their body "
    "temperature varies with the temperature of the environment; such animals are called "
    "<b>cold blooded or poikilotherms</b>."))  # F210, F211, F212, F213
story.append(b1(
    "You might have noticed <b>changes in the colour</b> of the frogs while they are in grasses "
    "and on dry land. They have the ability to <b>change the colour to hide them from their "
    "enemies (camouflage)</b>. This <b>protective coloration is called mimicry</b>."))  # F214, F215, F216
story.append(b1(
    "Frogs are <b>not seen during peak summer and winter</b>. During this period they take "
    "shelter in <b>deep burrows</b> to protect them from extreme heat and cold. This is known as "
    "<b>summer sleep (aestivation)</b> and <b>winter sleep (hibernation)</b> respectively."))  # F217, F218, F219

# ======================================================================================
# ---- 7.5.1  Morphology ---- F220-F235, F351 heading, F366 opener
#             (+ folded summary F380 part; Fig 7.19)
# ======================================================================================
story.append(heading("7.5.1", "Morphology", level=2))

# F366 opener (rhetorical) + F221-F225 + folded F380 (skin)
story.append(body(
    "The <b>skin</b> of a frog is <b>smooth and slippery</b> due to the presence of <b>mucus</b> "
    "and is <b>always maintained in a moist condition</b>. "
    # [FOLD F380 - SUMMARY-UNIQUE] mucous glands, highly vascularised skin, respiration (S54)
    "<b>Mucous glands</b> are present in the skin, which is <b>highly vascularised and helps in "
    "respiration</b> both in water and on land. The colour of the <b>dorsal side</b> of the body "
    "is generally <b>olive green with dark irregular spots</b>, while on the <b>ventral side</b> "
    "the skin is <b>uniformly pale yellow</b>. The frog <b>never drinks water but absorbs it "
    "through the skin</b>."))  # F220, F221, F222, F223, F224, F225 + F380

story.append(body(
    "The body of a frog is divisible into <b>head and trunk</b> (Figure 7.19); a <b>neck and "
    "tail are absent</b>."))  # F226, F227
story.append(b1(
    "Above the mouth, a <b>pair of nostrils</b> is present. <b>Eyes</b> are bulged and covered "
    "by a <b>nictitating membrane</b> that protects them while in water. On either side of the "
    "eyes a <b>membranous tympanum (ear)</b> receives sound signals."))  # F228, F229, F230
story.append(b1(
    "The <b>forelimbs and hind limbs</b> help in <b>swimming, walking, leaping and "
    "burrowing</b>. The <b>hind limbs end in five digits</b> and are <b>larger and muscular</b> "
    "than the <b>fore limbs that end in four digits</b>. <b>Feet have webbed digits</b> that "
    "help in swimming."))  # F231, F232, F233
story.append(b1(
    "Frogs exhibit <b>sexual dimorphism</b>. <b>Male frogs</b> can be distinguished by the "
    "presence of <b>sound producing vocal sacs</b> and also a <b>copulatory pad on the first "
    "digit of the fore limbs</b>, which are <b>absent in female frogs</b>."))  # F234, F235

story.append(figure(
    "fig_7_19.png",
    "Figure 7.19 External features of frog"))  # F336 caption

# ======================================================================================
# ---- 7.5.2  Anatomy ---- F236-F322, F352 heading, F367 opener
#             (+ folded summary F381; Figs 7.20, 7.21, 7.22)
# ======================================================================================
story.append(heading("7.5.2", "Anatomy", level=2))

# F367 opener + F236
story.append(body(
    "The <b>body cavity</b> of frogs accommodates different organ systems - <b>digestive, "
    "circulatory, respiratory, nervous, excretory and reproductive</b> - with well developed "
    "structures and functions (Figure 7.20)."))  # F236

# Digestive system (F237-F250)
story.append(heading("Dig", "Digestive System", level=3))
story.append(body(
    "The <b>digestive system</b> consists of the <b>alimentary canal</b> and <b>digestive "
    "glands</b>. The alimentary canal is <b>short</b> because frogs are <b>carnivores</b> and "
    "hence the length of the intestine is reduced. <b>Food is captured by the bilobed "
    "tongue.</b>"))  # F237, F238, F243
story.append(process_flow([
    "The <b>mouth</b> opens into the <b>buccal cavity</b> that leads to the <b>oesophagus</b> "
    "through the <b>pharynx</b>.",
    "The oesophagus is a short tube that opens into the <b>stomach</b>. Digestion of food takes "
    "place by the action of <b>HCl and gastric juices</b> secreted from the walls of the "
    "stomach.",
    "Partially digested food called <b>chyme</b> passes from the stomach to the first part of "
    "the small intestine, the <b>duodenum</b>, which receives <b>bile from the gall bladder</b> "
    "and <b>pancreatic juices from the pancreas</b> through a <b>common bile duct</b>.",
    "<b>Bile emulsifies fat</b> and <b>pancreatic juices digest carbohydrates and proteins</b>; "
    "<b>final digestion</b> takes place in the intestine.",
    "<b>Digested food is absorbed</b> by the numerous finger-like folds in the inner wall of "
    "the intestine called <b>villi and microvilli</b>.",
    "The <b>undigested solid waste</b> moves into the <b>rectum</b> and passes out through the "
    "<b>cloaca</b>.",
]))  # F239, F240, F244, F245, F246, F247, F248, F249, F250
story.append(body(
    "The main <b>digestive glands</b> are the <b>liver</b>, which secretes <b>bile</b> that is "
    "stored in the <b>gall bladder</b>, and the <b>pancreas</b>, which produces <b>pancreatic "
    "juice</b> containing digestive enzymes."))  # F241, F242

# Respiratory system (F251-F258)
story.append(heading("Resp", "Respiratory System", level=3))
story.append(body(
    "Frogs <b>respire on land and in the water by two different methods</b>. In water, the "
    "<b>skin acts as the aquatic respiratory organ (cutaneous respiration)</b> - <b>dissolved "
    "oxygen</b> in the water is exchanged through the skin by <b>diffusion</b>. On land, the "
    "<b>buccal cavity, skin and lungs</b> act as the respiratory organs; respiration by lungs is "
    "called <b>pulmonary respiration</b>."))  # F251, F252, F253, F254, F255
story.append(b1(
    "The <b>lungs</b> are a pair of <b>elongated, pink coloured sac-like structures</b> present "
    "in the upper part of the trunk region (thorax). <b>Air enters through the nostrils</b> into "
    "the buccal cavity and then to the lungs. During <b>aestivation and hibernation, gaseous "
    "exchange takes place through the skin</b>."))  # F256, F257, F258

# Circulatory system (F259-F278) + folded F381
story.append(heading("Circ", "Circulatory System", level=3))
story.append(body(
    "The <b>vascular system</b> of frog is a <b>well-developed closed type</b>. Frogs also have "
    "a <b>lymphatic system</b>. The <b>blood vascular system</b> involves <b>heart, blood "
    "vessels and blood</b>; the <b>lymphatic system</b> consists of <b>lymph, lymph channels and "
    "lymph nodes</b>. "
    # [FOLD F381 - SUMMARY-UNIQUE] closed circulation with single circulation (S60)
    "The circulatory system is <b>closed with single circulation</b>."))  # F259, F260, F261, F262, F381
story.append(b1(
    "The <b>heart</b> is a muscular structure situated in the upper part of the body cavity. It "
    "has <b>three chambers - two atria and one ventricle</b> - and is covered by a membrane "
    "called <b>pericardium</b>. A triangular structure called the <b>sinus venosus</b> joins the "
    "<b>right atrium</b> and receives blood through the major veins called the <b>vena "
    "cava</b>. The <b>ventricle</b> opens into a sac-like <b>conus arteriosus</b> on the ventral "
    "side of the heart."))  # F263, F264, F265, F266, F267
story.append(b1(
    "The blood from the heart is carried to all parts of the body by the <b>arteries (arterial "
    "system)</b>. The <b>veins</b> collect blood from different parts of the body to the heart "
    "and form the <b>venous system</b>. Special venous connections are present: between "
    "<b>liver and intestine</b> (the <b>hepatic portal system</b>) and between the <b>kidney "
    "and lower parts of the body</b> (the <b>renal portal system</b>)."))  # F268, F269, F270, F271
story.append(b1(
    "The <b>blood</b> is composed of <b>plasma and cells</b>. The blood cells are <b>RBC (red "
    "blood cells) or erythrocytes, WBC (white blood cells) or leucocytes and platelets</b>. "
    "<b>RBCs are nucleated</b> and contain the red coloured pigment <b>haemoglobin</b>."))  # F272, F273, F274
story.append(b1(
    "The <b>lymph</b> is different from blood - it <b>lacks few proteins and RBCs</b>. The blood "
    "<b>carries nutrients, gases and water</b> to the respective sites during circulation, which "
    "is achieved by the <b>pumping action of the muscular heart</b>."))  # F275, F276, F277, F278

# Excretory system (F279-F288) + Fig 7.20
story.append(heading("Excr", "Excretory System", level=3))
story.append(body(
    "The <b>elimination of nitrogenous wastes</b> is carried out by a <b>well developed "
    "excretory system</b> consisting of a pair of <b>kidneys, ureters, cloaca and urinary "
    "bladder</b>. The kidneys are <b>compact, dark red and bean-like structures</b> situated a "
    "little posteriorly in the body cavity on both sides of the vertebral column. Each kidney is "
    "composed of several structural and functional units called <b>uriniferous tubules or "
    "nephrons</b>."))  # F279, F280, F281, F282
story.append(b1(
    "<b>Two ureters</b> emerge from the kidneys in <b>male frogs</b>; the ureters act as a "
    "<b>urinogenital duct</b> which opens into the cloaca. In <b>females</b>, the <b>ureters and "
    "oviduct open separately</b> in the cloaca. The <b>thin-walled urinary bladder</b> is "
    "present ventral to the rectum and also opens into the cloaca."))  # F283, F284, F285, F286
story.append(b1(
    "The frog <b>excretes urea</b> and thus is a <b>ureotelic animal</b>. Excretory wastes are "
    "<b>carried by blood into the kidney</b> where they are <b>separated and excreted</b>."))  # F287, F288

story.append(figure(
    "fig_7_20.png",
    "Figure 7.20 Diagrammatic representation of internal organs of frog showing complete "
    "digestive system"))  # F337 caption

# Control and coordination (F289-F306)
story.append(heading("Ctrl", "Control and Coordination", level=3))
story.append(body(
    "The system for <b>control and coordination</b> is <b>highly evolved</b> in the frog and "
    "includes both the <b>neural system and endocrine glands</b>. The <b>chemical "
    "coordination</b> of various organs is achieved by <b>hormones</b> secreted by the "
    "<b>endocrine glands</b>. The prominent endocrine glands found in the frog are the "
    "<b>pituitary, thyroid, parathyroid, thymus, pineal body, pancreatic islets, adrenals and "
    "gonads</b>."))  # F289, F290, F291, F292
story.append(b1(
    "The <b>nervous system</b> is organised into a <b>central nervous system (brain and spinal "
    "cord)</b>, a <b>peripheral nervous system (cranial and spinal nerves)</b> and an "
    "<b>autonomic nervous system (sympathetic and parasympathetic)</b>. There are <b>ten pairs "
    "of cranial nerves</b> arising from the brain."))  # F293, F294
story.append(b1(
    "The <b>brain</b> is enclosed in a bony structure called the <b>brain box (cranium)</b> and "
    "is divided into <b>fore-brain, mid-brain and hind-brain</b>. The <b>forebrain</b> includes "
    "<b>olfactory lobes, paired cerebral hemispheres and unpaired diencephalon</b>; the "
    "<b>midbrain</b> is characterised by a <b>pair of optic lobes</b>; the <b>hind-brain</b> "
    "consists of <b>cerebellum and medulla oblongata</b>. The medulla oblongata passes out "
    "through the <b>foramen magnum</b> and continues into the <b>spinal cord</b>, which is "
    "enclosed in the vertebral column."))  # F295, F296, F297, F298, F299, F300
story.append(b1(
    "The frog has different types of <b>sense organs</b>: organs of <b>touch (sensory "
    "papillae)</b>, <b>taste (taste buds)</b>, <b>smell (nasal epithelium)</b>, <b>vision "
    "(eyes)</b> and <b>hearing (tympanum with internal ears)</b>. Of these, the <b>eyes and "
    "internal ears</b> are well-organised structures and the rest are <b>cellular aggregations "
    "around nerve endings</b>."))  # F301, F302
story.append(b1(
    "<b>Eyes</b> in a frog are a pair of <b>spherical structures</b> situated in the orbit in "
    "the skull; these are <b>simple eyes (possessing only one unit)</b>. <b>External ear is "
    "absent</b> in frogs and only the <b>tympanum</b> can be seen externally. The <b>ear</b> is "
    "an organ of <b>hearing as well as balancing (equilibrium)</b>."))  # F303, F304, F305, F306

# Reproductive system (F307-F322) + Figs 7.21, 7.22
story.append(heading("Repr", "Reproductive System", level=3))
story.append(body(
    "Frogs have <b>well organised male and female reproductive systems</b>."))  # F307
story.append(b1(
    "<b>Male reproductive organs</b> consist of a pair of <b>yellowish ovoid testes</b> (Figure "
    "7.21), found adhered to the upper part of the kidneys by a double fold of peritoneum called "
    "the <b>mesorchium</b>. <b>Vasa efferentia</b> are <b>10-12 in number</b> and arise from the "
    "testes; they enter the kidneys on their side and open into <b>Bidder's canal</b>. Finally "
    "it communicates with the <b>urinogenital duct</b> that comes out of the kidneys and opens "
    "into the <b>cloaca</b>."))  # F308, F309, F310, F311
story.append(b1(
    "The <b>cloaca</b> is a small, median chamber used to pass <b>faecal matter, urine and "
    "sperms</b> to the exterior."))  # F312
story.append(b1(
    "The <b>female reproductive organs</b> include a pair of <b>ovaries</b> (Figure 7.22), "
    "situated near the kidneys with <b>no functional connection</b> with them. A pair of "
    "<b>oviducts</b> arising from the ovaries opens into the <b>cloaca separately</b>. A mature "
    "female can lay <b>2500 to 3000 ova at a time</b>."))  # F313, F314, F315, F316
story.append(b1(
    "<b>Fertilisation is external</b> and takes place in <b>water</b>. Development involves a "
    "larval stage called the <b>tadpole</b>, which undergoes <b>metamorphosis</b> to form the "
    "adult."))  # F317, F318, F319

# Table cells need the shared helper's framed image and caption as flowables;
# nesting its KeepTogether wrapper inside a cell produces an infinite row height.
reproductive_figures = Table([[
    figure("fig_7_21.png", "Figure 7.21 Male reproductive system", max_width_cm=6.9)._content,
    figure("fig_7_22.png", "Figure 7.22 Female reproductive system", max_width_cm=6.9)._content,
]], colWidths=[FRAME_WIDTH / 2, FRAME_WIDTH / 2])  # F338, F339 captions
reproductive_figures.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ("TOPPADDING", (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
]))
story.append(reproductive_figures)

# Economic importance (F320-F322)
story.append(body(
    "<b>Frogs are beneficial for mankind</b> because they <b>eat insects and protect the "
    "crop</b>. They <b>maintain ecological balance</b> as an important link of the <b>food chain "
    "and food web</b> in the ecosystem. In some countries the <b>muscular legs of frog are used "
    "as food</b> by man."))  # F320, F321, F322

# ======================================================================================
# ---- QUICK RECAP (from NCERT SUMMARY; F353 SUMMARY heading) ----
# Every summary sentence restated: BODY-PRESENT lines recap the body; SUMMARY-UNIQUE
# lines are the same facts already folded above (F368-F381; S02,S03,S06-S09,S11,S15,S16,
# S38,S43,S51,S54,S60).
# ======================================================================================
story.append(heading("Recap", "Quick Recap", level=1))
story.append(b1(
    "A <b>tissue</b> is a group of cells along with intercellular substances performing <b>one "
    "or more functions</b>. Cells, tissues, organs and organ systems exhibit <b>division of "
    "labour</b> for the survival of the whole body. Complex animals have <b>four tissue "
    "types</b>: epithelial, connective, muscular and neural."))  # S01, S02
story.append(b1(
    "<b>Epithelia</b> are sheet-like tissues lining the body's surface and its <b>cavities, "
    "ducts and tubes</b>, with one <b>free surface</b>; their cells are connected at <b>tight, "
    "adhering and gap junctions</b>. Simple epithelium is squamous, cuboidal or columnar; "
    "compound epithelium is protective."))  # S03, S04, S05
story.append(b1(
    "<b>Connective tissues</b> bind together, support, strengthen, protect and insulate other "
    "tissues, and cover all three other tissue types. <b>Soft connective tissues</b> have "
    "protein fibres and varied cells in a ground substance. <b>Cartilage, bone, blood and "
    "adipose tissue</b> are specialised connective tissues; cartilage and bone are structural "
    "materials, <b>blood is a fluid transport tissue</b>, and <b>adipose tissue is a reservoir "
    "of stored energy</b>."))  # S06, S07, S08, S09, S10, S11, S16
story.append(b1(
    "<b>Muscle tissue</b> contracts in response to stimulation and helps movement. <b>Skeletal "
    "muscle</b> is attached to bones, <b>smooth muscle</b> is a component of internal organs, "
    "and <b>cardiac muscle</b> makes up the contractile walls of the heart. <b>Nervous "
    "tissue</b> exerts the greatest control over the body's responses; <b>neurons</b> are its "
    "basic units."))  # S12, S13, S14, S15, S17, S18
story.append(b1(
    "The body of <b>Cockroach (Periplaneta americana)</b> is covered by a chitinous exoskeleton "
    "and divided into <b>head, thorax and abdomen</b>, whose segments bear jointed appendages. "
    "The <b>three thoracic segments</b> each bear a pair of walking legs, <b>two pairs of "
    "wings</b> are present (one pair each on the 2nd and 3rd segment), and the <b>abdomen has 10 "
    "segments</b>."))  # S34, S35, S36, S37, S38, S39
story.append(b1(
    "The cockroach <b>alimentary canal</b> has a mouth with mouthparts, pharynx, oesophagus, "
    "crop, gizzard, midgut, hindgut and anus, with a <b>pair of salivary glands near the "
    "crop</b>. <b>Hepatic caecae</b> lie at the foregut-midgut junction and <b>Malpighian "
    "tubules</b> at the midgut-hindgut junction (excretion). The blood vascular system is "
    "<b>open</b>; respiration is by a network of <b>tracheae</b> opening through <b>spiracles</b>; "
    "the nervous system is <b>segmentally arranged ganglia with a ventral nerve cord</b>."))  # S40-S47
story.append(b1(
    "In the cockroach, a <b>pair of testes</b> is present in the 4th-6th segments and "
    "<b>ovaries</b> in the 2nd-6th segments; <b>fertilisation is internal</b>. A female produces "
    "<b>9-10 oothecae</b> bearing developing embryos, and after rupturing of a single ootheca "
    "<b>sixteen nymphs</b> come out."))  # S48, S49, S50, S51
story.append(b1(
    "The <b>Indian bullfrog, Rana tigrina</b>, is covered by <b>skin</b> with mucous glands "
    "(highly vascularised, aids respiration in water and on land), and the body is divisible "
    "into <b>head and trunk</b>. A muscular <b>bilobed tongue</b> captures prey. Its alimentary "
    "canal (oesophagus, stomach, intestine, rectum) opens into the <b>cloaca</b>; the main "
    "<b>digestive glands are liver and pancreas</b>."))  # S52, S53, S54, S55, S56, S57, S58
story.append(b1(
    "The frog can respire through <b>skin in water and lungs on land</b>. Its circulatory system "
    "is <b>closed with single circulation</b> and <b>RBCs are nucleated</b>. The nervous system "
    "is organised into <b>central, peripheral and autonomic</b> parts. The urinogenital system "
    "has <b>kidneys and urinogenital ducts</b> opening into the cloaca."))  # S59, S60, S61, S62, S63
story.append(b1(
    "The male reproductive organ is a <b>pair of testes</b> and the female a <b>pair of "
    "ovaries</b>. A female lays <b>2500-3000 ova</b> at a time; <b>fertilisation and development "
    "are external</b>, and the eggs hatch into <b>tadpoles</b> which metamorphose into "
    "frogs."))  # S64, S65, S66, S67, S68

# ======================================================================================
# ---- APPENDIX: Terms used in the exercises (Rule 2 GAP only) ---- F354 EXERCISES heading
# Only the GAP exercise terms are reproduced and answered; the COVERED exercises are
# answered by the body sections and figures above, so they are not repeated here (SS5 item 9).
# ======================================================================================
story.append(heading("Appendix", "Terms Used in the Exercises", level=1))
story.append(body(
    "A few exercise questions use terms that the supplied chapter text does not itself define. "
    "Those <b>gap</b> terms are answered here so the exercises can be attempted from these notes "
    "alone; every other exercise is answerable from the sections and figures above."))
story.append(keyterm(
    "<b>Axon</b> [Q7(b)] - the <b>single long process of a neuron</b> that conducts the nerve "
    "impulse <b>away from the cell body</b>, towards the neuron's endings (output zone). It is "
    "labelled in Figure 7.8 but not defined in the running text."))
story.append(keyterm(
    "<b>Simple gland vs compound gland</b> [Q9(e)] - a <b>simple gland</b> has an "
    "<b>unbranched duct</b>, whereas a <b>compound gland</b> has a <b>branched duct system</b> "
    "draining many secretory units. (This is distinct from the unicellular/multicellular "
    "classification given in 7.1.1.)"))
story.append(keyterm(
    "<b>Coxa</b> [Q10(e)] - the <b>basal segment of an insect leg</b>, which attaches the leg "
    "to the thoracic segment. (The cockroach's thoracic segments - mesothorax and metathorax - "
    "are described in 7.4.1.)"))
story.append(keyterm(
    "<b>Protonema</b> [Q10(e)] - the <b>green, branched, filamentous first stage</b> of the "
    "gametophyte in the life cycle of a <b>moss</b>. It is a plant structure and does not belong "
    "to the animals studied in this chapter."))
story.append(keyterm(
    "<b>Typhlosole</b> [Q11(e)] - the <b>internal median fold of the dorsal wall of the "
    "intestine of the earthworm</b>, which <b>increases the absorptive surface area</b>. "
    "(Earthworm is outside the NEET syllabus; the term is listed only because an exercise "
    "assumes it.)"))


def main():
    return build_pdf(
        OUT_PDF, story,
        title="Class 11 Chapter 7 - Structural Organisation in Animals (NEET notes)",
        subject="NEET Biology",
    )


if __name__ == "__main__":
    sys.exit(main())
