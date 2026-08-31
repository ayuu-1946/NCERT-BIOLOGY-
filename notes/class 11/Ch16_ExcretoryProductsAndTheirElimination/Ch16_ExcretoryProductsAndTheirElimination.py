"""
NCERT Class 11 Biology, Chapter 16 - Excretory Products and their Elimination
NEET replacement notes -> A4 print-ready PDF.

Built under SUPREME COMMAND PROMPT.md v6, Pass 2: written linearly from the
frozen 178-row inventory (Ch16_ExcretoryProductsAndTheirElimination_inventory.md),
in Content Order (SS5), importing the repo-level frozen style module
`neet_template.py` (SS0.6). No style, geometry, colour or font is re-declared
here.

=======================================================================
PARTIAL BUILD - THIS SCRIPT IS DELIBERATELY INCOMPLETE
=======================================================================
Scope of this build: the chapter intro block and **SS16.1 Human Excretory
System only**, as explicitly scoped for this session. Sections 16.2 - 16.8,
the SUMMARY and the EXERCISES table are NOT written yet.

Therefore:
  * Gate 2 is NOT claimed and `check_pdf.py` is NOT expected to pass on this
    file. Check 7 (every Facts row ticked) must FAIL by construction, because
    126 of the 178 rows belong to sections that do not exist yet. Check 6
    (figure-label coverage) must also FAIL, because Figure 16.5's and 16.6's
    labels live in 16.3/16.4/16.5 text that is not written yet.
  * Do not "fix" those FAILs by loosening the linter. They are the correct
    reading of a partial build and they clear themselves as 16.2-16.8 land.

Rows covered by this build: F001-F052 (chapter intro F002-F026, then 16.1
F027-F052), plus the four figures 16.1-16.4 that 16.1 calls out, with their
caption rows F165-F168 and label rows F173-F176.

Block markers `# ---- N.N ----` mark every NCERT section so a Pass 3 flag can
be found and fixed in one contiguous block. Inventory row IDs are named in the
comments so any fact can be traced back to its frozen row.

Subscripts / superscripts: the inventory stores the plasma/filtrate ions with
plain readable forms, but check_pdf.py check 5 bans Unicode sub/superscripts in
the PDF text stream, so every one is written here as a <sub> / <super> tag.

Figure callouts: all six Chapter 16 figures carry their labels as vector
artwork with no usable text layer (the inventory's 1-F session harvested them
by opening each rendered asset). Each figure is therefore followed by a NOTE
listing its callouts verbatim - that is what puts the figure-label-matrix
labels into the running text for check_pdf.py check 6, and it is also the only
way a print reader can name the parts of a diagram whose labels did not
survive extraction.

Source: Chapter/class 11/Chapter 16 - Excretory Products and their Elimination.pdf
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
    heading, keyterm, note, memory_aid, data_table, title_block, build_pdf,
)
from neet_template import figure as _shared_figure  # noqa: E402
from reportlab.platypus import Paragraph  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch16_ExcretoryProductsAndTheirElimination.pdf")

# Inline chemistry shorthands (check 5: tags, never Unicode sub/superscripts)
NA = "Na<super>+</super>"
K = "K<super>+</super>"
CL = "Cl<super>-</super>"
CO2 = "CO<sub>2</sub>"


def figure(asset_name, caption_text, max_width_cm=15.9):
    """Chapter-local binding of the shared figure() helper (SS0.6)."""
    return _shared_figure(asset_name, caption_text, ASSETS, max_width_cm=max_width_cm)


def body(text):
    return Paragraph(text, STYLES["Body"])


def b1(text):
    return Paragraph("&bull; " + text, STYLES["Bullet1"])


def b2(text):
    return Paragraph("- " + text, STYLES["Bullet2"])


story = []

# ======================================================================================
# ---- Title block (SS5 item 1) ---- F001
# ======================================================================================
story += title_block("Excretory Products and their Elimination")

# ======================================================================================
# ---- 16.intro ---- F002-F026 (opener F002)
# Covers: the waste inventory, the three nitrogenous wastes and their toxicity
# ranking, ammonotelism / ureotelism / uricotelism, and the invertebrate
# excretory-structure survey. Exercise-gap Ex 8 (osmoregulation is used three
# times in the chapter but never defined) is closed here, at first use.
# ======================================================================================
story.append(heading("16.0", "Why Excretion Exists - The Chapter's Starting Point", 1))
story.append(body(
    f"Animals <b>accumulate</b> ammonia, urea, uric acid, {CO2}, water and ions like "
    f"{NA}, {K}, {CL}, <b>phosphate, sulphate</b>, etc. They pick these up in two ways - "
    f"<b>either by metabolic activities</b> or <b>by other means like excess ingestion</b>. "
    f"These substances then <b>have to be removed totally or partially</b>."))
story.append(note(
    "This chapter is about the <b>mechanisms of elimination</b> of these substances, with "
    "<b>special emphasis on the common nitrogenous wastes</b>."))

# --- the three nitrogenous wastes, F005-F006 ---
story.append(body(
    "<b>Ammonia, urea and uric acid</b> are the <b>major forms of nitrogenous wastes</b> "
    "excreted by animals. The three differ in <b>toxicity</b>, and toxicity is what decides "
    "<b>how much water</b> an animal must spend to get rid of them:"))
story.append(data_table([
    ["Waste", "Toxicity", "Water needed to eliminate it"],
    ["Ammonia", "<b>Most toxic</b> form", "<b>Large amount</b> of water required"],
    ["Urea", "Intermediate", "Intermediate"],
    ["Uric acid", "<b>Least toxic</b>", "Removed with a <b>minimum loss</b> of water"],
], col_widths=[3.2, 4.2, 8.5]))
story.append(memory_aid(
    "<b>Toxicity falls, water saved rises</b> - Ammonia &gt; Urea &gt; Uric acid in toxicity, "
    "so the <b>same order reversed</b> gives water economy. An animal's choice of waste is "
    "really a statement about <b>how much water it can afford to lose</b>."))

# --- the three -telisms, F007-F015 ---
story.append(body(
    "Because of that trade-off, animals are classified by <b>which nitrogenous waste they "
    "excrete</b>. All three names are built the same way, on the waste plus <i>-telism</i>:"))

story.append(heading("16.0a", "Ammonotelism", 2))
story.append(keyterm(
    "<b>Ammonotelism</b> - the <b>process of excreting ammonia</b>."))
story.append(b1(
    "<b>Who:</b> many <b>bony fishes, aquatic amphibians and aquatic insects</b> are "
    "<b>ammonotelic</b> in nature."))
story.append(b1(
    "<b>How:</b> ammonia is <b>readily soluble</b>, so it is generally excreted <b>by "
    "diffusion across body surfaces</b> or <b>through gill surfaces (in fish)</b> as "
    "<b>ammonium ions</b>."))
story.append(b1(
    "<b>Kidneys do not play any significant role</b> in ammonia's removal."))

story.append(heading("16.0b", "Ureotelism", 2))
story.append(body(
    "<b>Terrestrial adaptation necessitated</b> the production of <b>lesser toxic</b> "
    "nitrogenous wastes like <b>urea and uric acid</b>, for <b>conservation of water</b>."))
story.append(keyterm(
    "<b>Ureotelic animals</b> - those that <b>mainly excrete urea</b>: <b>mammals, many "
    "terrestrial amphibians and marine fishes</b>."))
story.append(b1(
    "<b>Where urea is made:</b> ammonia produced by metabolism is <b>converted into urea in "
    "the liver</b> of these animals, and <b>released into the blood</b>, which is then "
    "<b>filtered and excreted out by the kidneys</b>."))
story.append(b1(
    "<b>Some urea is deliberately kept:</b> some amount of urea <b>may be retained in the "
    "kidney matrix</b> of some of these animals <b>to maintain a desired osmolarity</b>."))

story.append(heading("16.0c", "Uricotelism", 2))
story.append(keyterm(
    "<b>Uricotelic animals</b> - <b>reptiles, birds, land snails and insects</b>, which "
    "excrete nitrogenous wastes as <b>uric acid in the form of pellet or paste</b>, with a "
    "<b>minimum loss of water</b>."))

# --- Ex 8 gap: osmoregulation is never defined in the source ---
story.append(note(
    "<b>Osmoregulation</b> (assumed by Exercise 8; the NCERT body uses the word but never "
    "defines it): the <b>maintenance of the body's water and electrolyte balance</b> - that "
    "is, keeping the <b>volume and ionic concentration of body fluids</b> within a narrow "
    "range. Watch how often the structures below are described as doing <b>this</b> job "
    "rather than a waste-removal job; in many invertebrates the two are the same organ's "
    "work."))

# --- invertebrate survey, F017-F026 ---
story.append(heading("16.0d", "Excretory Structures Across the Animal Kingdom", 2))
story.append(body(
    "A <b>survey of the animal kingdom</b> presents a <b>variety of excretory structures</b>. "
    "In <b>most invertebrates</b> these structures are <b>simple tubular forms</b>, whereas "
    "<b>vertebrates have complex tubular organs called kidneys</b>. Some of these structures "
    "are:"))
story.append(data_table([
    ["Structure", "Found in", "What it does"],
    ["<b>Protonephridia</b><br/>or <b>flame cells</b>",
     "<b>Platyhelminthes</b> (Flatworms, e.g., <i>Planaria</i>), <b>rotifers</b>, some "
     "<b>annelids</b>, and the cephalochordate - <b>Amphioxus</b>",
     "Primarily <b>ionic and fluid volume regulation</b>, i.e., <b>osmoregulation</b>"],
    ["<b>Nephridia</b>",
     "<b>Earthworms</b> and other <b>annelids</b>",
     "Remove <b>nitrogenous wastes</b> and maintain a <b>fluid and ionic balance</b>"],
    ["<b>Malpighian tubules</b>",
     "Most <b>insects</b>, including <b>cockroaches</b>",
     "Removal of <b>nitrogenous wastes</b> and <b>osmoregulation</b>"],
    ["<b>Antennal glands</b><br/>or <b>green glands</b>",
     "<b>Crustaceans</b> like <b>prawns</b>",
     "Perform the <b>excretory function</b>"],
], col_widths=[3.4, 6.0, 6.5]))
story.append(memory_aid(
    "<b>Protonephridia are the odd one out.</b> Nephridia and Malpighian tubules are named "
    "as doing <b>both</b> jobs (wastes + balance); protonephridia are named as <b>primarily "
    "osmoregulatory</b>. A NEET stem that asks which structure is 'primarily concerned with "
    "ionic and fluid volume regulation' is asking for <b>flame cells</b>."))

# --- chapter contents panel, F016 (p. 205 margin, title-case in source) ---
story.append(body("<b>Chapter contents</b> (p. 205 margin panel):"))
story.append(b1("<b>16.1</b> Human Excretory System"))
story.append(b1("<b>16.2</b> Urine Formation"))
story.append(b1("<b>16.3</b> Function of the Tubules"))
story.append(b1("<b>16.4</b> Mechanism of Concentration of the Filtrate"))
story.append(b1("<b>16.5</b> Regulation of Kidney Function"))
story.append(b1("<b>16.6</b> Micturition"))
story.append(b1("<b>16.7</b> Role of other Organs in Excretion"))
story.append(b1("<b>16.8</b> Disorders of the Excretory System"))

# ======================================================================================
# ---- 16.1 Human Excretory System ---- F027-F052 (heading F027, opener F028)
# Figures 16.1-16.4 (captions F165-F168, labels F173-F176) all belong here.
# Figure-only facts closed here: "Inferior vena cava" and "Dorsal aorta" (Fig 16.1),
# per the inventory's figure-only-content table.
# ======================================================================================
story.append(heading("16.1", "Human Excretory System", 1))
story.append(body(
    "In humans, the excretory system consists of <b>four parts</b> (Figure 16.1):"))
story.append(b1("a <b>pair of kidneys</b>"))
story.append(b1("<b>one pair of ureters</b>"))
story.append(b1("a <b>urinary bladder</b>"))
story.append(b1("a <b>urethra</b>"))

# --- gross anatomy of the kidney, F029-F030 ---
story.append(heading("16.1a", "The Kidney - Position, Size and Outer Features", 2))
story.append(body(
    "<b>Kidneys are reddish brown, bean shaped</b> structures. They sit <b>between the levels "
    "of the last thoracic and third lumbar vertebra</b>, <b>close to the dorsal inner wall of "
    "the abdominal cavity</b>."))
story.append(body("<b>Dimensions of one adult human kidney:</b>"))
story.append(data_table([
    ["Length", "Width", "Thickness", "Average weight"],
    ["<b>10-12 cm</b>", "<b>5-7 cm</b>", "<b>2-3 cm</b>", "<b>120-170 g</b>"],
], col_widths=[4.0, 4.0, 4.0, 3.9]))
story.append(memory_aid(
    "<b>10-12 / 5-7 / 2-3, then 120-170 g.</b> The three dimensions run <b>downwards in "
    "pairs</b> and the weight is the only three-digit number in the set. NEET has asked for "
    "each of these four figures directly."))

story.append(body(
    "Towards the <b>centre of the inner concave surface</b> of the kidney is a <b>notch called "
    "the hilum</b>, through which the <b>ureter, blood vessels and nerves enter</b>. "
    "<b>Inner to the hilum</b> is a <b>broad funnel shaped space called the renal pelvis</b>, "
    "with <b>projections called calyces</b>."))

story.append(figure("fig_16_1.png", "Figure 16.1 Human Urinary system"))
story.append(note(
    "<b>Figure 16.1 callouts, verbatim:</b> Inferior vena cava; Adrenal gland; Renal artery; "
    "Renal vein; Pelvis; Kidney; Medulla; Cortex; Dorsal aorta; Ureter; Urinary bladder; "
    "Urethra."))
story.append(note(
    "<b>Two vessels the figure names but the prose never does.</b> Figure 16.1 draws the "
    "<b>renal artery</b> branching off the <b>dorsal aorta</b>, and the <b>renal vein</b> "
    "draining into the <b>inferior vena cava</b>. The running text of the chapter names "
    "neither the dorsal aorta nor the inferior vena cava, so read them off the figure: "
    "<b>aorta -&gt; renal artery -&gt; kidney -&gt; renal vein -&gt; inferior vena cava</b>. "
    "The figure also shows the <b>adrenal gland</b> capping each kidney."))

# --- internal zonation, F033-F036 ---
story.append(heading("16.1b", "Inside the Kidney - Cortex, Medulla and the Columns", 2))
story.append(b1(
    "The <b>outer layer</b> of the kidney is a <b>tough capsule</b>."))
story.append(b1(
    "Inside, there are <b>two zones</b> - an <b>outer cortex</b> and an <b>inner medulla</b>."))
story.append(b1(
    "The <b>medulla is divided into a few conical masses</b> - the <b>medullary pyramids</b> - "
    "<b>projecting into the calyces</b> (sing.: <b>calyx</b>)."))
story.append(b1(
    "The <b>cortex extends in between the medullary pyramids</b> as <b>renal columns</b> "
    "called <b>Columns of Bertini</b> (Figure 16.2)."))
story.append(figure("fig_16_2.png",
                    "Figure 16.2 Longitudinal section (Diagrammatic) of Kidney"))
story.append(note(
    "<b>Figure 16.2 callouts, verbatim:</b> Medullary pyramid; Renal column; Calyx; Renal "
    "artery; Renal vein; Renal pelvis; Ureter; Cortex; Renal capsule."))
story.append(memory_aid(
    "<b>Columns of Bertini are cortex, not medulla.</b> They are the cortex reaching "
    "<b>inwards between</b> the pyramids. A stem describing 'medullary tissue extending into "
    "the cortex' has the direction backwards."))

# --- the nephron, F037-F046 ---
story.append(heading("16.1c", "The Nephron - the Functional Unit", 2))
story.append(body(
    "Each kidney has <b>nearly one million</b> complex tubular structures called "
    "<b>nephrons</b> (Figure 16.3), which are the <b>functional units</b>. Each nephron has "
    "<b>two parts</b> - the <b>glomerulus</b> and the <b>renal tubule</b>."))
story.append(keyterm(
    "<b>Glomerulus</b> - a <b>tuft of capillaries</b> formed by the <b>afferent arteriole</b>, "
    "a <b>fine branch of the renal artery</b>. Blood from the glomerulus is <b>carried away by "
    "an efferent arteriole</b>."))
story.append(keyterm(
    "<b>Bowman's capsule</b> - the <b>double walled cup-like structure</b> the renal tubule "
    "<b>begins with</b>, which <b>encloses the glomerulus</b>."))
story.append(keyterm(
    "<b>Malpighian body</b> or <b>renal corpuscle</b> - the <b>glomerulus alongwith Bowman's "
    "capsule</b>, taken together (Figure 16.4)."))
story.append(body(
    "<b>From Bowman's capsule onward, the tubule runs through four named regions in order:</b>"))
story.append(b1(
    "<b>Proximal convoluted tubule (PCT)</b> - the tubule continues from the capsule to form "
    "this <b>highly coiled network</b>."))
story.append(b1(
    "<b>Henle's loop</b> - the <b>next part</b>, <b>hairpin shaped</b>, with a <b>descending "
    "and an ascending limb</b>."))
story.append(b1(
    "<b>Distal convoluted tubule (DCT)</b> - the <b>ascending limb continues</b> as this "
    "<b>another highly coiled tubular region</b>."))
story.append(b1(
    "<b>Collecting duct</b> - the <b>DCTs of many nephrons open into</b> this <b>straight "
    "tube</b>. <b>Many collecting ducts converge</b> and <b>open into the renal pelvis "
    "through the medullary pyramids in the calyces</b>."))
story.append(figure("fig_16_3.png",
                    "Figure 16.3 A diagrammatic representation of a nephron showing blood "
                    "vessels, duct and tubule"))
story.append(note(
    "<b>Figure 16.3 callouts, verbatim:</b> Afferent arteriole; Efferent arteriole; "
    "Glomerulus; Bowman's capsule; Proximal convoluted tubule; Distal convoluted tubule; "
    "Descending limb of loop of Henle; Ascending limb of loop of Henle; Henle's loop; Vasa "
    "recta; Collecting duct."))
story.append(figure("fig_16_4.png", "Figure 16.4 Malpighian body (renal corpuscle)"))
story.append(note(
    "<b>Figure 16.4 callouts, verbatim:</b> Afferent arteriole; Efferent arteriole; Bowman's "
    "capsule; Proximal convoluted tubule."))

# --- cortical vs juxta medullary, F047-F052 ---
story.append(heading("16.1d", "Where the Parts Sit, and the Two Types of Nephron", 2))
story.append(body(
    "<b>The nephron is not evenly spread between the two zones.</b> The <b>Malpighian "
    "corpuscle, PCT and DCT</b> are situated in the <b>cortical region</b> of the kidney, "
    "whereas the <b>loop of Henle dips into the medulla</b>."))
story.append(body(
    "<b>How far the loop dips</b> is what separates the <b>two types of nephron</b>:"))
story.append(data_table([
    ["", "<b>Cortical nephrons</b>", "<b>Juxta medullary nephrons</b>"],
    ["How many", "The <b>majority</b> of nephrons", "<b>Some</b> of the nephrons"],
    ["Loop of Henle",
     "<b>Too short</b> - extends <b>only very little</b> into the medulla",
     "<b>Very long</b> - runs <b>deep into the medulla</b>"],
    ["Vasa recta", "<b>Absent or highly reduced</b>", "<b>Present</b>"],
], col_widths=[3.4, 6.2, 6.3]))
story.append(memory_aid(
    "<b>Juxta = next to.</b> A <b>juxta medullary</b> nephron sits <b>next to the medulla</b> "
    "and so can afford a <b>long</b> loop; the <b>cortical</b> nephron stays up in the cortex "
    "with a <b>short</b> loop and <b>no real vasa recta</b>. Remember which one loses the "
    "vasa recta - it is the <b>cortical</b> one, and 16.4 will show why that matters for "
    "concentrating urine."))

story.append(body(
    "<b>The blood supply follows the tubule.</b> The <b>efferent arteriole</b> emerging from "
    "the glomerulus forms a <b>fine capillary network around the renal tubule</b>, called the "
    "<b>peritubular capillaries</b>. A <b>minute vessel of this network</b> runs <b>parallel "
    "to Henle's loop</b>, forming a <b>'U' shaped vasa recta</b>. <b>Vasa recta is absent or "
    "highly reduced in cortical nephrons.</b>"))

if __name__ == "__main__":
    sys.exit(build_pdf(
        OUT_PDF, story,
        title="Class 11 Chapter 16 - Excretory Products and their Elimination (NEET notes)",
        subject="NEET Biology"))
