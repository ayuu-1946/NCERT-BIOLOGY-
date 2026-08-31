"""
NCERT Class 11 Biology, Chapter 16 - Excretory Products and their Elimination
NEET replacement notes -> A4 print-ready PDF.

Built under SUPREME COMMAND PROMPT.md v6, Pass 2: written linearly from the
frozen 178-row inventory (Ch16_ExcretoryProductsAndTheirElimination_inventory.md)
in Content Order (SS5), importing the repo-level frozen style module
`neet_template.py` (SS0.6). No style, geometry, colour or font is re-declared
here.

Block markers `# ---- N.N ----` mark every NCERT section so a Pass 3 flag can be
found and fixed in one contiguous block. Inventory row IDs are named in the
comments so any fact can be traced back to its frozen row.

WHY THIS CHAPTER LEANS ON process_flow():
Chapter 16 is the most process-dense chapter in the Class 11 book - glomerular
filtration, the three tubular processes, the counter current multiplier, the
renin-angiotensin-aldosterone cascade, the ADH feedback loop, the micturition
reflex and haemodialysis are all ordered, causal sequences. NEET questions on
this chapter are overwhelmingly "which step / in which segment / what happens
next" items, so every such sequence is written as a numbered process_flow block
rather than as prose. The SUPREME COMMAND PROMPT allows extra explanatory
content where it improves understanding (SS3), and that allowance is spent here
almost entirely on making the ORDER and the SITE of each step unambiguous.

Subscripts / superscripts: the inventory stores Na+, K+, Cl-, HCO3-, NH3, H2O,
CO2, mOsmolL-1 in plain readable form, but check_pdf.py check 5 bans Unicode
sub/superscripts in the PDF text stream, so every one is written here as a
<sub> / <super> tag instead.

Figure callouts: all six figures carry their labels as vector artwork, so each
figure is followed by a NOTE listing its callouts verbatim. That is what puts
all 76 figure-label-matrix labels (F173-F178) into the running text for
check_pdf.py check 6, and it is also the only way a print reader can name the
parts of a diagram whose labels did not survive extraction.

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
    heading, keyterm, process_flow, note, memory_aid, data_table, title_block, build_pdf,
)
from neet_template import figure as _shared_figure  # noqa: E402
from reportlab.platypus import Paragraph, Spacer  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch16_ExcretoryProductsAndTheirElimination.pdf")

# Inline chemistry / unit shorthands (check 5: tags, never Unicode sub/superscripts)
NA = "Na<super>+</super>"
K = "K<super>+</super>"
CL = "Cl<super>-</super>"
H = "H<super>+</super>"
HCO3 = "HCO<sub>3</sub><super>-</super>"
NH3 = "NH<sub>3</sub>"
NH4 = "NH<sub>4</sub><super>+</super>"
H2O = "H<sub>2</sub>O"
CO2 = "CO<sub>2</sub>"
MOSM = "mOsmolL<super>-1</super>"


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
story += title_block("Excretory Products and their Elimination")

# ======================================================================================
# ---- 16.intro ---- F002-F026 (opener F002)
# ======================================================================================

story.append(body(
    "Animals accumulate <b>ammonia, urea, uric acid, carbon dioxide, water</b> and ions "
    f"like {NA}, {K}, {CL}, phosphate and sulphate, either as by-products of their own "
    "metabolic activities or by other means such as excess ingestion. These substances "
    "have to be removed totally or partially, because allowing them to build up would "
    "poison the body fluids. This chapter deals with the mechanisms of elimination of "
    "these substances, with special emphasis on the common nitrogenous wastes."))

story.append(keyterm(
    "<b>Excretion</b> - the removal of metabolic waste products, especially nitrogenous "
    "wastes, from the body."))

story.append(keyterm(
    "<b>Osmoregulation</b> - the maintenance of a constant water and electrolyte (ionic) "
    "balance in the body fluids. Excretory organs almost always perform osmoregulation "
    "alongside waste removal, and in many invertebrates osmoregulation is the primary job. "
    "<i>[definition supplied for Exercise 8, which asks for it although the chapter uses "
    "the word without ever defining it]</i>"))

story.append(gap())
story.append(body(
    "<b>Ammonia, urea and uric acid</b> are the three major forms of nitrogenous waste "
    "excreted by animals. They differ in exactly one respect that matters, and every other "
    "fact about them follows from it: <b>toxicity runs opposite to water cost</b>. Ammonia "
    "is the most toxic form and therefore requires a large amount of water for its "
    "elimination; uric acid, being the least toxic, can be removed with a minimum loss of "
    "water. Which one an animal makes is decided mainly by its <b>habitat</b>, that is, by "
    "how much water it can afford to throw away."))

story.append(data_table([
    ["Waste", "Toxicity", "Water needed", "Excretory habit", "Animals"],
    ["Ammonia", "Most toxic", "Largest amount", "<b>Ammonotelism</b>",
     "Many bony fishes, aquatic amphibians, aquatic insects"],
    ["Urea", "Moderately toxic", "Moderate", "<b>Ureotelism</b>",
     "Mammals, many terrestrial amphibians, marine fishes"],
    ["Uric acid", "Least toxic", "Minimum loss",
     "<b>Uricotelism</b>", "Reptiles, birds, land snails, insects"],
], col_widths=[13, 13, 12, 17, 45]))

story.append(gap())
story.append(keyterm(
    "<b>Ammonotelism</b> - the process of excreting ammonia. Many bony fishes, aquatic "
    "amphibians and aquatic insects are <b>ammonotelic</b> in nature."))

story.append(b1(
    "Ammonia, as it is readily soluble, is generally excreted by <b>diffusion across body "
    f"surfaces</b> or through <b>gill surfaces</b> (in fish) as <b>ammonium ions</b> ({NH4})."))
story.append(b1(
    "<b>Kidneys do not play any significant role</b> in the removal of ammonia. This is a "
    "favourite NEET distractor: ammonotelic excretion is a body-surface process, not a "
    "renal one."))

story.append(gap())
story.append(body(
    "<b>Terrestrial adaptation necessitated the production of lesser toxic nitrogenous "
    "wastes</b> like urea and uric acid, for conservation of water. Land animals cannot "
    "spare the water that ammonia disposal costs, so evolution traded toxicity for dryness."))

story.append(keyterm(
    "<b>Ureotelism</b> - excretion of urea. Mammals, many terrestrial amphibians and marine "
    "fishes mainly excrete urea and are called <b>ureotelic</b> animals."))

story.append(process_flow([
    "Ammonia is produced by metabolism (chiefly deamination of amino acids).",
    "It is converted into <b>urea in the liver</b> of these animals - the liver, not the "
    "kidney, is the site of urea <i>synthesis</i>.",
    "The urea is released into the <b>blood</b>.",
    "The blood is <b>filtered by the kidneys</b> and the urea is excreted out.",
]))

story.append(gap())
story.append(note(
    "Some amount of urea may be <b>retained in the kidney matrix</b> of some of these animals "
    "to maintain a desired osmolarity. Urea is therefore not purely a waste to be dumped - "
    "in the mammalian kidney it is also a working solute, a point that returns in 16.4."))

story.append(gap())
story.append(keyterm(
    "<b>Uricotelism</b> - excretion of uric acid. Reptiles, birds, land snails and insects "
    "excrete nitrogenous wastes as uric acid in the form of <b>pellet or paste</b> with a "
    "minimum loss of water and are called <b>uricotelic</b> animals."))

story.append(gap())
story.append(memory_aid(
    "<b>Toxicity ladder, most to least toxic: Ammonia &gt; Urea &gt; Uric acid</b> - and the "
    "water bill falls in the same order. <b>\"A-U-U\" = Aquatic - in between - Arid.</b> "
    "Ammonotelic = water everywhere (bony fish); ureotelic = mammals; uricotelic = birds and "
    "reptiles that must fly or hoard water, hence a semi-solid pellet."))

story.append(gap())
story.append(heading("16.0", "Excretory Structures Across the Animal Kingdom", level=2))

story.append(body(
    "A survey of the animal kingdom presents a variety of excretory structures. In most of "
    "the <b>invertebrates</b>, these structures are <b>simple tubular forms</b>, whereas "
    "<b>vertebrates</b> have <b>complex tubular organs called kidneys</b>. Some of these "
    "structures are mentioned here."))

story.append(data_table([
    ["Excretory structure", "Found in", "Function"],
    ["<b>Protonephridia</b> or <b>flame cells</b>",
     "Platyhelminthes (flatworms, e.g., <i>Planaria</i>), rotifers, some annelids and the "
     "cephalochordate - <i>Amphioxus</i>",
     "Primarily <b>ionic and fluid volume regulation</b>, i.e., <b>osmoregulation</b>"],
    ["<b>Nephridia</b>", "Earthworms and other annelids",
     "Remove <b>nitrogenous wastes</b> and maintain <b>fluid and ionic balance</b>"],
    ["<b>Malpighian tubules</b>", "Most insects, including cockroaches",
     "Removal of <b>nitrogenous wastes</b> and <b>osmoregulation</b>"],
    ["<b>Antennal glands</b> or <b>green glands</b>", "Crustaceans like prawns",
     "Perform the <b>excretory function</b>"],
    ["<b>Kidneys</b>", "Vertebrates, including humans",
     "Complex tubular organs; nitrogenous waste removal plus osmoregulation and "
     "acid-base balance"],
], col_widths=[24, 38, 38]))

story.append(gap())
story.append(memory_aid(
    "<b><i>Amphioxus</i> is the exam trap.</b> Exercise 11(a) asks for \"a chordate animal "
    "having flame cells\" - the answer is <i>Amphioxus</i>, not <i>Planaria</i>. <i>Planaria</i> "
    "is a flatworm; <i>Amphioxus</i> is the cephalochordate on that same list."))

story.append(gap())
story.append(note(
    "These five organ types are not merely a list to memorise. Every one of them does two "
    "jobs at once - it eliminates nitrogenous waste <b>and</b> helps maintain the ionic and "
    "acid-base balance of body fluids. That dual role is the single idea the human kidney "
    "then executes with far more precision in the rest of this chapter."))

# ======================================================================================
# ---- 16.1 HUMAN EXCRETORY SYSTEM ---- F027-F052 (heading F027, opener F028)
# ======================================================================================

story.append(heading("16.1", "HUMAN EXCRETORY SYSTEM", level=1))

story.append(body(
    "In humans, the excretory system consists of a <b>pair of kidneys</b>, <b>one pair of "
    "ureters</b>, a <b>urinary bladder</b> and a <b>urethra</b> (Figure 16.1)."))

story.append(gap())
story.append(heading("16.1a", "Position, Size and Gross Structure of the Kidney", level=2))

story.append(b1(
    "Kidneys are <b>reddish brown, bean shaped</b> structures situated between the levels "
    "of the <b>last thoracic and third lumbar vertebra</b>, close to the <b>dorsal inner "
    "wall of the abdominal cavity</b>."))
story.append(b1(
    "Each kidney of an adult human measures <b>10-12 cm in length</b>, <b>5-7 cm in "
    "width</b>, <b>2-3 cm in thickness</b>, with an average weight of <b>120-170 g</b>."))
story.append(b1(
    "Towards the centre of the inner concave surface of the kidney is a notch called "
    "<b>hilum</b>, through which the <b>ureter, blood vessels and nerves</b> enter."))
story.append(b1(
    "Inner to the hilum is a broad funnel shaped space called the <b>renal pelvis</b>, with "
    "projections called <b>calyces</b>."))
story.append(b1(
    "The outer layer of the kidney is a <b>tough capsule</b> (the renal capsule)."))

story.append(gap())
story.append(body(
    "Inside the kidney there are <b>two zones</b>: an outer <b>cortex</b> and an inner "
    "<b>medulla</b>."))

story.append(b1(
    "The <b>medulla</b> is divided into a few <b>conical masses</b> - the <b>medullary "
    "pyramids</b> - projecting into the <b>calyces</b> (sing.: <b>calyx</b>)."))
story.append(b1(
    "The <b>cortex</b> extends in between the medullary pyramids as renal columns called "
    "<b>Columns of Bertini</b>."))

story.append(gap())
story.append(note(
    "The kidney receives its blood through the <b>renal artery</b>, a branch of the "
    "<b>dorsal aorta</b>, and returns it through the <b>renal vein</b>, which drains into "
    "the <b>inferior vena cava</b>. Both great vessels are drawn and labelled in Figure 16.1 "
    "but are never named in the chapter's running text, so they are named here: they are the "
    "reason a kidney can filter about one-fifth of the cardiac output every minute. Sitting "
    "on top of each kidney is the <b>adrenal gland</b>, also labelled in Figure 16.1; its "
    "cortex supplies the aldosterone that appears in 16.5."))

story.append(gap())
story.append(figure("fig_16_1.png", "Figure 16.1 Human Urinary system"))

story.append(note(
    "<b>Figure 16.1 labels, verbatim:</b> \"Inferior vena cava\"; \"Adrenal gland\"; "
    "\"Renal artery\"; \"Renal vein\"; \"Pelvis\"; \"Kidney\"; \"Medulla\"; \"Cortex\"; "
    "\"Dorsal aorta\"; \"Ureter\"; \"Urinary bladder\"; \"Urethra\"."))

story.append(gap())
story.append(figure("fig_16_2.png",
                    "Figure 16.2 Longitudinal section (Diagrammatic) of Kidney"))

story.append(note(
    "<b>Figure 16.2 labels, verbatim:</b> \"Medullary pyramid\"; \"Renal column\"; "
    "\"Calyx\"; \"Renal artery\"; \"Renal vein\"; \"Renal pelvis\"; \"Ureter\"; "
    "\"Cortex\"; \"Renal capsule\"."))

story.append(gap())
story.append(memory_aid(
    "<b>Urine's one-way road: Nephron -&gt; Collecting duct -&gt; Medullary pyramid -&gt; "
    "Calyx -&gt; Renal pelvis -&gt; Ureter -&gt; Urinary bladder -&gt; Urethra.</b> "
    "Nothing is reabsorbed after the collecting duct - once the filtrate leaves the duct it "
    "is final urine, and everything downstream is plumbing and storage only."))

story.append(gap())
story.append(heading("16.1b", "The Nephron - Functional Unit of the Kidney", level=2))

story.append(body(
    "Each kidney has nearly <b>one million</b> complex tubular structures called "
    "<b>nephrons</b> (Figure 16.3), which are the <b>functional units</b> of the kidney. "
    "Each nephron has <b>two parts</b> - the <b>glomerulus</b> and the <b>renal tubule</b>."))

story.append(keyterm(
    "<b>Glomerulus</b> - a <b>tuft of capillaries</b> formed by the <b>afferent "
    "arteriole</b>, a fine branch of the renal artery. Blood from the glomerulus is carried "
    "away by an <b>efferent arteriole</b>."))

story.append(keyterm(
    "<b>Malpighian body</b> or <b>renal corpuscle</b> - the glomerulus together with "
    "<b>Bowman's capsule</b> (Figure 16.4). The renal tubule begins with this double walled "
    "cup-like Bowman's capsule, which encloses the glomerulus."))

# [VERIFICATION FIX] Fig 16.4 embed was dropped in Pass 2 (asset present, image never
# appended); check_pdf.py check 6 verifies label text only, not image embedding, so this
# was linter-invisible. Restored at its topic (Malpighian-body keyterm).
story.append(gap())
story.append(figure("fig_16_4.png", "Figure 16.4 Malpighian body (renal corpuscle)"))

story.append(note(
    "<b>Figure 16.4 labels, verbatim:</b> \"Afferent arteriole\"; \"Efferent arteriole\"; "
    "\"Bowman's capsule\"; \"Proximal convoluted tubule\"."))

story.append(gap())
story.append(body("The renal tubule then runs through four named segments in strict order:"))

story.append(process_flow([
    "<b>Bowman's capsule</b> - double walled, cup-like, encloses the glomerulus; the filtrate "
    "enters the tubule here.",
    "<b>Proximal convoluted tubule (PCT)</b> - the tubule continues to form a highly coiled "
    "network.",
    "<b>Henle's loop</b> - a <b>hairpin shaped</b> region with a <b>descending</b> and an "
    "<b>ascending limb</b>.",
    "<b>Distal convoluted tubule (DCT)</b> - the ascending limb continues as another highly "
    "coiled tubular region.",
    "<b>Collecting duct</b> - the DCTs of many nephrons open into a straight tube; many "
    "collecting ducts converge and open into the <b>renal pelvis</b> through the "
    "<b>medullary pyramids</b> in the <b>calyces</b>.",
]))

story.append(gap())
story.append(note(
    "<b>Which segment sits in which zone.</b> The <b>Malpighian corpuscle, PCT and DCT</b> of "
    "the nephron are situated in the <b>cortical region</b> of the kidney, whereas the "
    "<b>loop of Henle dips into the medulla</b>. This single sentence is the anatomical basis "
    "of the whole of 16.4: only the loop and the collecting duct travel through the salty "
    "medulla, so only they can exploit its osmotic gradient."))

story.append(gap())
story.append(heading("16.1c", "Two Kinds of Nephron", level=2))

story.append(data_table([
    ["Feature", "Cortical nephrons", "Juxta medullary nephrons"],
    ["Proportion", "The <b>majority</b> of nephrons", "<b>Some</b> of the nephrons"],
    ["Loop of Henle", "<b>Too short</b>; extends only <b>very little</b> into the medulla",
     "<b>Very long</b>; runs <b>deep into the medulla</b>"],
    ["Vasa recta", "<b>Absent or highly reduced</b>", "<b>Present</b> and well developed"],
    ["Consequence", "Limited ability to build a medullary gradient",
     "Drive the counter current mechanism and concentrated urine (16.4)"],
], col_widths=[18, 41, 41]))

story.append(gap())
story.append(body("The blood supply around the tubule has its own two named parts:"))

story.append(b1(
    "The <b>efferent arteriole</b> emerging from the glomerulus forms a fine capillary "
    "network around the renal tubule called the <b>peritubular capillaries</b>."))
story.append(b1(
    "A minute vessel of this network runs <b>parallel to Henle's loop</b>, forming a "
    "<b>'U' shaped vasa recta</b>."))
story.append(b1(
    "<b>Vasa recta is absent or highly reduced in cortical nephrons</b> - which is exactly "
    "why cortical nephrons cannot concentrate urine strongly."))

story.append(gap())
story.append(figure("fig_16_3.png",
                    "Figure 16.3 A diagrammatic representation of a nephron showing blood "
                    "vessels, duct and tubules"))

story.append(note(
    "<b>Figure 16.3 labels, verbatim:</b> \"Afferent arteriole\"; \"Efferent arteriole\"; "
    "\"Glomerulus\"; \"Bowman's capsule\"; \"Proximal convoluted tubule\"; \"Distal "
    "convoluted tubule\"; \"Descending limb of loop of Henle\"; \"Ascending limb of loop of "
    "Henle\"; \"Henle's loop\"; \"Vasa recta\"; \"Collecting duct\"."))

story.append(gap())
story.append(memory_aid(
    "<b>Two arterioles, one capillary bed in between - the kidney's signature.</b> "
    "<i>A</i>fferent <i>A</i>rrives, <i>E</i>fferent <i>E</i>xits. Because a capillary tuft "
    "lies between <b>two arterioles</b> (not between an arteriole and a vein), the kidney can "
    "hold glomerular pressure high enough to filter - and can adjust it. Exercise 11(c) asks "
    "for \"a loop of capillary running parallel to the Henle's loop\": <b>vasa recta</b>."))

# ======================================================================================
# ---- 16.2 URINE FORMATION ---- F053-F073 (heading F053, opener F054)
# ======================================================================================

story.append(heading("16.2", "URINE FORMATION", level=1))

story.append(body(
    "Urine formation involves <b>three main processes</b>, namely <b>glomerular "
    "filtration</b>, <b>reabsorption</b> and <b>secretion</b>, that take place in different "
    "parts of the nephron."))

story.append(gap())
story.append(memory_aid(
    "<b>Urine = Filtered - Reabsorbed + Secreted.</b> Keep that equation in view for the "
    "whole chapter. Filtration is bulk and indiscriminate; reabsorption claims back "
    "everything valuable; secretion actively dumps a short list of extras. Anything in your "
    "urine got there because it was either filtered and <b>not</b> reclaimed, or "
    "deliberately secreted."))

story.append(gap())
story.append(heading("16.2a", "Glomerular Filtration", level=2))

story.append(body(
    "The <b>first step</b> in urine formation is the <b>filtration of blood</b>, which is "
    "carried out by the <b>glomerulus</b> and is called <b>glomerular filtration</b>. It is "
    "a <b>non-selective</b> process: the glomerulus does not choose what to let through, it "
    "simply uses the <b>glomerular capillary blood pressure</b> to push fluid across, and "
    "the membranes decide by size alone."))

story.append(b1(
    "On an average, <b>1100-1200 ml of blood is filtered by the kidneys per minute</b>, "
    "which constitutes roughly <b>1/5th (one-fifth) of the blood pumped out by each "
    "ventricle</b> of the heart in a minute."))

story.append(gap())
story.append(body(
    "The glomerular capillary blood pressure causes filtration of blood through "
    "<b>3 layers</b>:"))

story.append(process_flow([
    "The <b>endothelium of the glomerular blood vessels</b>.",
    "The <b>epithelium of Bowman's capsule</b> - its cells, called <b>podocytes</b>, are "
    "arranged in an intricate manner so as to leave some minute spaces called <b>filtration "
    "slits</b> or <b>slit pores</b>.",
    "A <b>basement membrane</b> lying between these two layers.",
]))

story.append(gap())
story.append(body(
    "Blood is filtered so finely through these membranes that <b>almost all the constituents "
    "of the plasma except the proteins</b> pass into the lumen of the Bowman's capsule. The "
    "fluid that arrives in the capsule is therefore a <b>protein-free fluid</b> filtered from "
    "the blood plasma."))

story.append(keyterm(
    "<b>Ultra filtration</b> - because the filtration is fine enough to hold back essentially "
    "all plasma proteins while letting everything smaller through, glomerular filtration is "
    "considered a process of ultra filtration."))

story.append(gap())
story.append(note(
    "Two exam-critical consequences of \"protein-free\". <b>(1)</b> Proteins are retained, so "
    "plasma proteins stay in the blood and hold its osmotic pull - this is why "
    "<b>proteinuria</b> signals a damaged filtration barrier. <b>(2)</b> Glucose, amino acids "
    "and ions are <b>not</b> retained at the glomerulus - they are filtered freely and must "
    "be won back downstream by reabsorption. Filtration does not protect anything useful "
    "except protein; the tubules do all the saving."))

story.append(gap())
story.append(keyterm(
    "<b>Glomerular filtration rate (GFR)</b> - the amount of the filtrate formed by the "
    "kidneys <b>per minute</b>. <i>[Exercise 1 asks exactly this.]</i>"))

story.append(b1(
    "GFR in a healthy individual is approximately <b>125 ml/minute</b>, i.e., <b>180 litres "
    "per day</b>!"))

story.append(gap())
story.append(data_table([
    ["Quantity", "Value", "Read it as"],
    ["Blood filtered by the glomerulus", "about <b>1100-1200 ml per minute</b>",
     "roughly <b>1/5th of the cardiac output</b>"],
    ["Filtrate formed in Bowman's capsule (GFR)", "<b>125 ml per minute</b>",
     "<b>180 litres per day</b>"],
    ["Urine actually released", "<b>1 to 1.5 litres per day</b>",
     "so nearly <b>99 per cent</b> is reabsorbed"],
], col_widths=[36, 32, 32]))

story.append(gap())
story.append(memory_aid(
    "<b>1200 in, 125 out, 1.5 kept.</b> About <b>1200 ml of blood per minute</b> is filtered "
    "by the glomerulus to form <b>125 ml of filtrate per minute</b> in Bowman's capsule "
    "(= GFR), and only about <b>1.5 litres</b> leaves the body per day. Those three numbers, "
    "in that order, answer most numerical NEET items on this chapter."))

story.append(gap())
story.append(heading("16.2b", "Autoregulation of GFR - the JGA", level=2))

story.append(body(
    "The kidneys have <b>built-in mechanisms</b> for the regulation of glomerular filtration "
    "rate. One such efficient mechanism is carried out by the <b>juxta glomerular apparatus "
    "(JGA)</b>."))

story.append(keyterm(
    "<b>Juxta glomerular apparatus (JGA)</b> - a special sensitive region formed by cellular "
    "modifications in the <b>distal convoluted tubule</b> and the <b>afferent arteriole</b> "
    "at the location of their contact."))

story.append(process_flow([
    "<b>GFR falls</b> below normal.",
    "The fall <b>activates the JG cells</b> of the juxta glomerular apparatus.",
    "The JG cells <b>release renin</b>.",
    "Renin <b>stimulates the glomerular blood flow</b>, and thereby brings the <b>GFR back "
    "to normal</b>.",
], cyclic=True))

story.append(gap())
story.append(note(
    "This is the short, local version of the story - the full hormonal cascade that renin "
    "sets off (angiotensin I, angiotensin II, aldosterone) is developed in <b>16.5</b>. For "
    "<b>Exercise 2</b>, \"the autoregulatory mechanism of GFR\" means precisely this JGA "
    "loop: the kidney senses its own filtration rate at the DCT-afferent arteriole contact "
    "and corrects it without waiting for instructions from outside."))

story.append(gap())
story.append(heading("16.2c", "Reabsorption", level=2))

story.append(body(
    "A comparison of the volume of the filtrate formed per day (<b>180 litres per day</b>) "
    "with that of the urine released (<b>1.5 litres</b>) suggests that nearly <b>99 per cent "
    "of the filtrate has to be reabsorbed</b> by the renal tubules. This process is called "
    "<b>reabsorption</b>."))

story.append(b1(
    "The <b>tubular epithelial cells</b> in different segments of the nephron perform this "
    "either by <b>active</b> or <b>passive</b> mechanisms."))
story.append(b1(
    f"For example, substances like <b>glucose, amino acids and {NA}</b> in the filtrate are "
    "reabsorbed <b>actively</b>, whereas the <b>nitrogenous wastes</b> are absorbed by "
    "<b>passive transport</b>."))
story.append(b1(
    "Reabsorption of <b>water</b> also occurs <b>passively</b> in the initial segments of the "
    "nephron (Figure 16.5)."))

story.append(gap())
story.append(heading("16.2d", "Tubular Secretion", level=2))

story.append(body(
    f"During urine formation, the tubular cells <b>secrete</b> substances like {H}, {K} and "
    f"ammonia ({NH3}) <b>into the filtrate</b>. <b>Tubular secretion</b> is also an important "
    "step in urine formation, as it helps in the <b>maintenance of the ionic and acid-base "
    "balance of body fluids</b>."))

story.append(gap())
story.append(data_table([
    ["Process", "Direction", "Site", "What moves"],
    ["<b>Glomerular filtration</b>",
     "Blood into the tubule (Bowman's capsule)", "Glomerulus",
     "Everything in plasma <b>except proteins</b>; non-selective, pressure driven"],
    ["<b>Reabsorption</b>", "Tubule back into the blood",
     "All along the tubule; <b>PCT is the major site</b>",
     f"Glucose, amino acids, {NA} (active); nitrogenous wastes and water (passive); "
     "about <b>99%</b> of the filtrate"],
    ["<b>Secretion</b>", "Blood/tubular cells into the tubule",
     f"PCT, DCT, collecting duct", f"{H}, {K}, {NH3}; maintains ionic and acid-base balance"],
], col_widths=[19, 24, 22, 35]))

story.append(gap())
story.append(memory_aid(
    "<b>Do not confuse secretion with excretion.</b> <b>Secretion</b> is a step <i>inside</i> "
    "the nephron - the tubule adds substances to the filtrate. <b>Excretion</b> is the final "
    "removal from the body. Also note that reabsorption and secretion run in "
    "<b>opposite directions</b> across the same tubular wall at the same time."))

# ======================================================================================
# ---- 16.3 FUNCTION OF THE TUBULES ---- F074-F093
# heading F074; run-in heads F075 (PCT), F079 (Henle's Loop), F086 (DCT), F089 (Collecting
# Duct); openers F076, F080, F087, F090
# ======================================================================================

story.append(heading("16.3", "FUNCTION OF THE TUBULES", level=1))

story.append(body(
    "Each segment of the renal tubule has its own permeability and its own transport "
    "specialities, and that is what makes graded processing of the filtrate possible. Read "
    "the four segments below as one assembly line."))

# ---- 16.3 run-in head: Proximal Convoluted Tubule (PCT) ---- F075-F078
story.append(gap())
story.append(heading("PCT", "Proximal Convoluted Tubule (PCT):", level=2))

story.append(body(
    "PCT is lined by <b>simple cuboidal brush border epithelium</b>, which <b>increases the "
    "surface area for reabsorption</b>."))

story.append(b1(
    "<b>Nearly all of the essential nutrients</b>, and <b>70-80 per cent of electrolytes and "
    "water</b>, are reabsorbed by this segment. The PCT is therefore the <b>major site of "
    "reabsorption and selective secretion</b>."))
story.append(b1(
    "PCT also helps to <b>maintain the pH and ionic balance</b> of the body fluids by "
    f"<b>selective secretion of hydrogen ions ({H}) and ammonia ({NH3})</b> into the filtrate, "
    f"and by <b>absorption of {HCO3}</b> from it."))

story.append(gap())
story.append(note(
    "The <b>brush border</b> is the whole point of the PCT. Those microvilli multiply the "
    "membrane area available for carrier proteins, which is why the bulk of glucose, amino "
    "acids and electrolytes is recovered here and not later. <b>Exercise 3(e)</b> - glucose "
    "is actively reabsorbed in the proximal convoluted tubule - is <b>true</b>."))

# ---- 16.3 run-in head: Henle's Loop ---- F079-F085
story.append(gap())
story.append(heading("HL", "Henle's Loop:", level=2))

story.append(body(
    "<b>Reabsorption is minimum in its ascending limb.</b> However, this region plays a "
    "significant role in the <b>maintenance of high osmolarity of the medullary interstitial "
    "fluid</b>."))

story.append(gap())
story.append(body(
    "The two limbs are mirror opposites in permeability, and this contrast is the engine of "
    "the counter current mechanism in 16.4:"))

story.append(data_table([
    ["", "Descending limb", "Ascending limb"],
    ["Permeable to <b>water</b>?", "<b>Permeable to water</b>",
     "<b>Impermeable to water</b>"],
    ["Permeable to <b>electrolytes</b>?", "Almost <b>impermeable to electrolytes</b>",
     "Allows <b>transport of electrolytes</b>, actively or passively"],
    ["Effect on the filtrate",
     "Water leaves, so the filtrate <b>gets concentrated as it moves down</b>",
     "Electrolytes leave, so the concentrated filtrate <b>gets diluted as it passes "
     "upward</b>"],
    ["Effect on the interstitium", "Adds water to the interstitium",
     "Adds electrolytes, <b>raising medullary osmolarity</b>"],
], col_widths=[22, 39, 39]))

story.append(gap())
story.append(b1(
    "The <b>descending limb</b> of the loop of Henle is <b>permeable to water</b> but almost "
    "<b>impermeable to electrolytes</b>. This <b>concentrates the filtrate as it moves "
    "down</b>."))
story.append(b1(
    "The <b>ascending limb</b> is <b>impermeable to water</b> but allows <b>transport of "
    "electrolytes</b> actively or passively. Therefore, as the concentrated filtrate passes "
    "upward, <b>it gets diluted</b> due to the passage of electrolytes to the medullary "
    "fluid."))

story.append(gap())
story.append(note(
    "The ascending limb is not uniform along its length. Figure 16.5 labels both a <b>thick "
    "segment of ascending limb</b> and a <b>thin segment of ascending limb</b>, though the "
    "chapter's prose names only the thin one (in 16.4, where urea enters it). The distinction "
    "is worth holding: the <b>thin segment</b> lies deeper in the medulla and passes "
    "electrolytes and a little urea largely passively, whereas the <b>thick segment</b> "
    "carries the powerful active transport of NaCl out into the interstitium. Both are "
    "impermeable to water, which is why dilution of the filtrate continues all the way up."))

story.append(gap())
story.append(memory_aid(
    "<b>Descending = water Departs. Ascending = salt Ascends out.</b> So going down the "
    "filtrate gets saltier, coming up it gets more dilute - and the medulla gets saltier "
    "either way. For <b>Exercise 12(a)</b>: the ascending limb is <b>impermeable</b> to water "
    "whereas the descending limb is <b>permeable</b> to it."))

# ---- 16.3 run-in head: Distal Convoluted Tubule (DCT) ---- F086-F088
story.append(gap())
story.append(heading("DCT", "Distal Convoluted Tubule (DCT):", level=2))

story.append(body(
    f"<b>Conditional reabsorption of {NA} and water</b> takes place in this segment. The word "
    "<b>conditional</b> is doing real work here: unlike the PCT's near-automatic bulk "
    "recovery, what the DCT reclaims depends on the body's current needs, under hormonal "
    "control (ADH and aldosterone, 16.5)."))

story.append(b1(
    f"DCT is also capable of <b>reabsorption of {HCO3}</b> and <b>selective secretion of "
    f"hydrogen ({H}) and potassium ({K}) ions and {NH3}</b>, to maintain the <b>pH and "
    "sodium-potassium balance</b> in blood."))

# ---- 16.3 run-in head: Collecting Duct ---- F089-F093
story.append(gap())
story.append(heading("CD", "Collecting Duct:", level=2))

story.append(body(
    "This <b>long duct extends from the cortex</b> of the kidney <b>to the inner parts of the "
    "medulla</b>. Because it crosses the entire osmotic gradient built by the loop of Henle, "
    "it is the segment where the final water decision is made."))

story.append(b1(
    "<b>Large amounts of water could be reabsorbed</b> from this region to produce a "
    "<b>concentrated urine</b>."))
story.append(b1(
    "This segment allows passage of <b>small amounts of urea into the medullary "
    "interstitium</b>, to <b>keep up the osmolarity</b>."))
story.append(b1(
    "It also plays a role in the maintenance of <b>pH and ionic balance of blood</b> by the "
    f"<b>selective secretion of {H} and {K} ions</b> (Figure 16.5)."))

story.append(gap())
story.append(figure("fig_16_5.png",
                    "Figure 16.5 Reabsorption and secretion of major substances at different "
                    "parts of the nephron (Arrows indicate direction of movement of "
                    "materials.)"))

story.append(note(
    "<b>Figure 16.5 labels, verbatim:</b> \"Proximal convoluted tubule\"; \"Distal convoluted "
    f"tubule\"; \"Cortex\"; \"Medulla\"; \"{HCO3}\"; \"NaCl\"; \"Nutrients\"; \"{H2O}\"; "
    f"\"{K}\"; \"{H}\"; \"{NH3}\"; \"Descending limb of loop of Henle\"; \"Thick segment of "
    "ascending limb\"; \"Thin segment of ascending limb\"; \"Collecting duct\"; \"Urea\"."))

story.append(gap())
story.append(heading("16.3s", "Segment-by-Segment Summary of Tubular Function", level=2))

story.append(data_table([
    ["Segment", "Reabsorbs", "Secretes", "Signature fact"],
    ["<b>PCT</b>",
     "Nearly all essential <b>nutrients</b>; <b>70-80%</b> of electrolytes and water; "
     f"{HCO3}", f"{H}, {NH3}",
     "<b>Brush border</b> epithelium; <b>major site</b> of reabsorption"],
    ["<b>Henle's loop - descending limb</b>", "<b>Water</b> (passively)", "-",
     "Impermeable to electrolytes; <b>concentrates</b> the filtrate"],
    ["<b>Henle's loop - ascending limb</b>",
     "<b>Electrolytes</b> (to interstitium); reabsorption of water is <b>minimum</b>", "-",
     "Impermeable to water; <b>dilutes</b> the filtrate, salts the medulla"],
    ["<b>DCT</b>", f"<b>Conditional</b> {NA} and water; {HCO3}", f"{H}, {K}, {NH3}",
     "Hormone-controlled; sodium-potassium and pH balance"],
    ["<b>Collecting duct</b>",
     "<b>Large amounts of water</b>; allows <b>urea</b> into the interstitium", f"{H}, {K}",
     "Runs <b>cortex to inner medulla</b>; sets final urine concentration"],
], col_widths=[19, 30, 15, 36]))

story.append(gap())
story.append(memory_aid(
    "<b>PCT = bulk. Loop = gradient. DCT = fine tuning. Collecting duct = final water "
    "call.</b> If a NEET question asks \"where\", match the verb: <i>bulk/most/nutrients</i> "
    "means PCT, <i>osmolarity/gradient</i> means loop of Henle, <i>conditional/hormonal</i> "
    "means DCT, <i>concentrated urine</i> means collecting duct."))

# ======================================================================================
# ---- 16.4 MECHANISM OF CONCENTRATION OF THE FILTRATE ---- F094-F107
# heading F094 (running head sets "ofthe Filtrate", a source typo), opener F095
# ======================================================================================

story.append(heading("16.4", "MECHANISM OF CONCENTRATION OF THE FILTRATE", level=1))

story.append(body(
    "<b>Mammals have the ability to produce a concentrated urine.</b> The <b>Henle's loop</b> "
    "and <b>vasa recta</b> play a significant role in this."))

story.append(gap())
story.append(heading("16.4a", "Counter Current - What the Word Means", level=2))

story.append(b1(
    "The <b>flow of filtrate in the two limbs of Henle's loop is in opposite directions</b>, "
    "and thus forms a <b>counter current</b>."))
story.append(b1(
    "The <b>flow of blood through the two limbs of vasa recta is also in a counter current "
    "pattern</b>."))

story.append(gap())
story.append(body(
    f"The <b>proximity</b> between the Henle's loop and vasa recta, as well as the counter "
    f"current in them, help in maintaining an <b>increasing osmolarity towards the inner "
    f"medullary interstitium</b>, i.e., from <b>300 {MOSM} in the cortex</b> to about "
    f"<b>1200 {MOSM} in the inner medulla</b>. This <b>gradient is mainly caused by NaCl and "
    f"urea</b>."))

story.append(gap())
story.append(note(
    "Why a counter current is worth the trouble. If both limbs flowed the same way, whatever "
    "one limb built up the other would immediately wash away, and the medulla would sit at "
    "blood osmolarity. Because they run <b>opposite</b>, each small transport step is handed "
    "over to a neighbouring stream that is only slightly different in concentration, and "
    "those small differences <b>multiply along the length</b> of the loop into a four-fold "
    "gradient from cortex to inner medulla. This is why the arrangement is often called a "
    "<b>counter current multiplier</b>, and why a long loop (juxta medullary nephron) "
    "concentrates urine better than a short one."))

story.append(gap())
story.append(heading("16.4b", "The Counter Current Mechanism, Step by Step", level=2))

story.append(process_flow([
    "<b>NaCl is transported by the ascending limb of Henle's loop</b>, which is "
    "<b>exchanged with the descending limb of vasa recta</b>.",
    "<b>NaCl is returned to the interstitium by the ascending portion of vasa recta</b> - so "
    "the salt is recycled within the medulla instead of being carried away in the blood.",
    "Similarly, <b>small amounts of urea enter the thin segment of the ascending limb</b> of "
    "Henle's loop.",
    "That urea is <b>transported back to the interstitium by the collecting tubule</b>, "
    "completing a second recycling loop.",
    "The result is a standing gradient: <b>electrolytes and urea are retained in the "
    f"interstitium</b> by this arrangement, holding the inner medulla near <b>1200 {MOSM}</b>.",
]))

story.append(gap())
story.append(keyterm(
    "<b>Counter current mechanism</b> - the above described transport of substances "
    "facilitated by the <b>special arrangement of Henle's loop and vasa recta</b> "
    "(Figure. 16.6). <i>[Exercise 4 asks for a brief account of exactly this.]</i>"))

story.append(b1(
    "This mechanism helps to <b>maintain a concentration gradient in the medullary "
    "interstitium</b>."))
story.append(b1(
    "Presence of such an interstitial gradient helps in an <b>easy passage of water from the "
    "collecting tubule</b>, thereby <b>concentrating the filtrate (urine)</b>."))
story.append(b1(
    "<b>Human kidneys can produce urine nearly four times concentrated</b> than the initial "
    f"filtrate formed - the DCT and collecting duct concentrate the filtrate from about "
    f"<b>300 {MOSM}</b> to <b>1200 {MOSM}</b>, an excellent mechanism of <b>conservation of "
    "water</b>."))

story.append(gap())
story.append(figure("fig_16_6.png",
                    "Figure 16.6 Diagrammatic representation of a nephron and vasa recta "
                    "showing counter current mechanisms"))

story.append(note(
    "<b>Figure 16.6 labels, verbatim:</b> \"Afferent arteriole\"; \"Efferent arteriole\"; "
    "\"Bowman's capsule\"; \"Glomerulus\"; \"Cortex\"; \"Outer medulla\"; \"Inner medulla\"; "
    f"\"{H2O}\"; \"NaCl\"; \"Urea\"; \"Vasa recta\"; \"Nephron\". The osmolarity scale is "
    f"drawn as \"300 {MOSM}\", \"600 {MOSM}\", \"900 {MOSM}\" and \"1200 {MOSM}\", with tick "
    "marks reading \"200\", \"300\", \"400\", \"600\", \"800\", \"900\", \"1000\" and "
    "\"1200\" - values that exist only in the artwork, so they are listed here to keep the "
    "printed gradient readable."))

story.append(gap())
story.append(memory_aid(
    "<b>300 to 1200 = four times.</b> Cortex sits at <b>300</b>, inner medulla at "
    "<b>1200</b>; that ratio <i>is</i> the \"four times concentrated\" fact. Remember the two "
    "solutes that build it - <b>NaCl and urea</b> - and the two structures that recycle them "
    "- <b>Henle's loop and vasa recta</b>. Salt is handed over by the loop and returned by "
    "vasa recta; urea leaks in from the collecting duct."))

story.append(gap())
story.append(note(
    "<b>Putting 16.3 and 16.4 together.</b> The loop of Henle does not concentrate the urine "
    "directly - the filtrate actually <i>leaves</i> the loop more dilute than it entered. What "
    "the loop does is make the <b>medulla</b> salty. The concentrated urine is then produced "
    "<b>downstream</b>, when the collecting duct carries filtrate back through that salty "
    "medulla and water is drawn out. For <b>Exercise 3(d)</b> - Henle's loop plays an "
    "important role in concentrating the urine - the answer is <b>true</b>, but understand it "
    "as an indirect role: it builds the gradient that the collecting duct spends."))

# ======================================================================================
# ---- 16.5 REGULATION OF KIDNEY FUNCTION ---- F108-F126 (heading F108, opener F109)
# ======================================================================================

story.append(heading("16.5", "REGULATION OF KIDNEY FUNCTION", level=1))

story.append(body(
    "The functioning of the kidneys is efficiently monitored and regulated by <b>hormonal "
    "feedback mechanisms</b> involving the <b>hypothalamus</b>, and to a certain extent the "
    "<b>JGA</b> and, to some extent, the <b>heart</b>."))

story.append(gap())
story.append(heading("16.5a", "ADH and the Osmoreceptor Loop", level=2))

story.append(process_flow([
    "An <b>excessive loss of fluid</b> from the body <b>activates the osmoreceptors</b> in "
    "the body.",
    "These <b>stimulate the hypothalamus</b> to release <b>antidiuretic hormone (ADH)</b>, "
    "also known as <b>vasopressin</b>, from the <b>neurohypophysis</b>.",
    "ADH <b>facilitates water reabsorption from the latter parts of the tubule</b>, thereby "
    "<b>preventing diuresis</b>.",
    "<b>An increase in body fluid volume</b> results, which <b>switches off the "
    "osmoreceptors</b> and <b>suppresses the ADH release</b> to complete the feedback.",
], cyclic=True))

story.append(gap())
story.append(keyterm(
    "<b>Diuresis</b> - the loss of water (increased urine output) that ADH prevents. Because "
    "ADH is <b>anti</b>diuretic, more ADH means <b>less</b> urine and a more concentrated "
    "urine."))

story.append(gap())
story.append(note(
    "<b>ADH's second job.</b> ADH can also affect the kidney function by its constrictory "
    "effects on <b>blood vessels</b>. This <b>causes an increase in blood pressure</b>, and an "
    "increase in blood pressure <b>increases the glomerular blood flow, and thereby the "
    "GFR</b>. That is why the same hormone carries the alternative name <b>vasopressin</b> - "
    "one molecule, two levers: water retention at the tubule and vasoconstriction at the "
    "vessel."))

story.append(gap())
story.append(memory_aid(
    "<b>ADH = Add water back to the blood.</b> High ADH gives scanty, concentrated urine; no "
    "ADH gives copious, dilute urine (as in diabetes insipidus). So <b>Exercise 3(b)</b> - "
    "\"ADH helps in water elimination, making the urine hypotonic\" - is <b>false</b>; ADH "
    "does the exact opposite. <b>Exercise 12(b)</b>: reabsorption of water from distal parts "
    "of the tubules is facilitated by <b>ADH (vasopressin)</b>."))

story.append(gap())
story.append(heading("16.5b", "The Renin-Angiotensin-Aldosterone System (RAAS)", level=2))

story.append(body(
    "The <b>JGA</b> plays a complex regulatory role. Here the trigger is not osmolarity but "
    "<b>blood flow, blood volume and pressure</b> reaching the kidney itself."))

story.append(process_flow([
    "A <b>fall in glomerular blood flow / glomerular blood pressure / GFR</b> can "
    "<b>activate the JG cells</b> to release <b>renin</b>.",
    "Renin <b>converts angiotensinogen in blood to angiotensin I</b>.",
    "Angiotensin I is further converted to <b>angiotensin II</b>.",
    "<b>Angiotensin II</b>, being a powerful <b>vasoconstrictor</b>, <b>increases the "
    "glomerular blood pressure and thereby GFR</b>.",
    "Angiotensin II also <b>activates the adrenal cortex to release aldosterone</b>.",
    f"<b>Aldosterone causes reabsorption of {NA} and water from the distal parts of the "
    "tubule</b>.",
    "This also leads to an <b>increase in blood pressure and GFR</b>, restoring what the "
    "fall in step 1 had reduced.",
], cyclic=True))

story.append(keyterm(
    "<b>Renin-Angiotensin mechanism</b> - this complex mechanism, operated by the JGA, is "
    "generally known as the Renin-Angiotensin mechanism."))

story.append(gap())
story.append(note(
    "Note that <b>angiotensin II raises GFR two ways at once</b>: directly, by constricting "
    "vessels and raising glomerular pressure, and indirectly, by ordering aldosterone which "
    f"reclaims {NA} and water and so restores blood volume. Distinguish the two hormones "
    f"carefully - <b>ADH reabsorbs water alone</b>, while <b>aldosterone reabsorbs {NA} "
    "<i>and</i> water</b>. Both act on \"the distal parts of the tubule\"."))

story.append(gap())
story.append(heading("16.5c", "ANF - the Opposing Signal", level=2))

story.append(process_flow([
    "An <b>increase in blood flow to the atria of the heart</b> occurs.",
    "This causes the <b>release of Atrial Natriuretic Factor (ANF)</b>.",
    "<b>ANF causes vasodilation (dilation of blood vessels)</b>.",
    "This <b>decreases the blood pressure</b>.",
]))

story.append(gap())
story.append(body(
    "<b>ANF mechanism, therefore, acts as a check on the renin-angiotensin mechanism.</b> The "
    "kidney is thus held between two opposing hormonal pushes, which is what keeps blood "
    "pressure and fluid volume stable rather than oscillating."))

story.append(gap())
story.append(data_table([
    ["Hormone", "Source", "Trigger", "Main renal action", "Net effect"],
    ["<b>ADH</b> (vasopressin)", "<b>Hypothalamus</b>, released from <b>neurohypophysis</b>",
     "Excessive fluid loss activates <b>osmoreceptors</b>",
     "<b>Water reabsorption</b> from the latter parts of the tubule; also vasoconstriction",
     "Prevents <b>diuresis</b>; raises BP and GFR"],
    ["<b>Renin</b>", "<b>JG cells</b> of the JGA",
     "Fall in glomerular blood flow / BP / GFR",
     "Converts <b>angiotensinogen to angiotensin I</b>", "Starts the RAAS cascade"],
    ["<b>Angiotensin II</b>", "Blood (from angiotensin I)", "Renin release",
     "Powerful <b>vasoconstrictor</b>; stimulates adrenal cortex",
     "<b>Increases</b> glomerular BP and GFR"],
    ["<b>Aldosterone</b>", "<b>Adrenal cortex</b>", "Angiotensin II",
     f"Reabsorption of <b>{NA} and water</b> from the distal parts of the tubule",
     "<b>Increases</b> BP and GFR"],
    ["<b>ANF</b>", "<b>Atria of the heart</b>", "Increased blood flow to the atria",
     "<b>Vasodilation</b>", "<b>Decreases</b> BP; a <b>check</b> on RAAS"],
], col_widths=[15, 18, 19, 27, 21]))

story.append(gap())
story.append(memory_aid(
    "<b>Three sensors, three hormones.</b> <b>Osmoreceptors</b> watch concentration and call "
    "<b>ADH</b>. <b>JG cells</b> watch renal blood flow and call <b>renin</b> (leading to "
    "angiotensin II and aldosterone). <b>Atrial stretch</b> watches volume and calls "
    "<b>ANF</b>. Four of the five hormones in the table <b>raise</b> BP or GFR; only "
    "<b>ANF lowers</b> it. If an exam option says \"ANF increases blood pressure\", it is "
    "wrong."))

# ======================================================================================
# ---- 16.6 MICTURITION ---- F127-F138 (heading F127, opener F128)
# ======================================================================================

story.append(heading("16.6", "MICTURITION", level=1))

story.append(body(
    "<b>Urine formed by the nephrons is ultimately carried to the urinary bladder</b>, where "
    "it is <b>stored till a voluntary signal is given by the central nervous system "
    "(CNS)</b>. This <b>signal is initiated by the stretching of the urinary bladder</b> as "
    "it gets filled with urine."))

story.append(keyterm(
    "<b>Micturition</b> - the process of release of urine. <i>[Exercise 6 asks you to explain "
    "it.]</i>"))

story.append(keyterm(
    "<b>Micturition reflex</b> - the neural mechanisms causing micturition."))

story.append(gap())
story.append(process_flow([
    "Urine formed by the nephrons is carried to and <b>stored in the urinary bladder</b>.",
    "As the bladder fills, its <b>stretching</b> sends a signal, and <b>stretch receptors on "
    "the wall of the bladder send signals to the CNS</b>.",
    "The <b>CNS passes on motor messages</b> to initiate the <b>contraction of the smooth "
    "muscles of the bladder</b> and the <b>simultaneous relaxation of the urethral "
    "sphincter</b>, causing the <b>release of urine</b>.",
]))

story.append(gap())
story.append(note(
    "The two events in step 3 must happen <b>together</b> - contraction of the bladder wall "
    "and <b>relaxation</b> of the sphincter. A NEET distractor often flips the sphincter to "
    "\"contraction\". Note also the hybrid nature of the act: the reflex is involuntary, but "
    "it waits on a <b>voluntary signal from the CNS</b>, which is why toilet training is "
    "possible at all. For <b>Exercise 3(a)</b> - micturition is carried out by a reflex - the "
    "answer is <b>true</b>."))

story.append(gap())
story.append(body(
    "<b>An adult human excretes, on an average, 1 to 1.5 litres of urine per day.</b> Its "
    "properties are:"))

story.append(b1("The urine formed is a <b>light yellow coloured watery fluid</b>."))
story.append(b1("It is <b>slightly acidic (pH 6.0)</b>."))
story.append(b1("It has a <b>characteristic odour</b>."))
story.append(b1(
    "On an average, <b>25-30 gm of urea is excreted out per day</b>. "
    "<i>[Exercise 12(d) asks for this figure.]</i>"))

story.append(gap())
story.append(note(
    "<b>Various conditions can affect the characteristics of urine</b>, and this is precisely "
    "why urine analysis is a diagnostic tool. <b>Analysis of urine helps in clinical diagnosis "
    "of many metabolic disorders as well as malfunctioning of the kidney.</b> For example, "
    "presence of <b>glucose (glycosuria)</b> and <b>ketone bodies (ketonuria)</b> in urine "
    "are indicative of <b>diabetes mellitus</b>."))

story.append(gap())
story.append(memory_aid(
    "<b>Urine numbers to keep: 1-1.5 L per day, pH 6.0, 25-30 g urea per day.</b> And "
    "remember that <b>glycosuria + ketonuria = diabetes mellitus</b>, not a kidney disease - "
    "the kidney is reporting a metabolic problem elsewhere."))

# ======================================================================================
# ---- 16.7 ROLE OF OTHER ORGANS IN EXCRETION ---- F139-F149 (heading F139, opener F140)
# ======================================================================================

story.append(heading("16.7", "ROLE OF OTHER ORGANS IN EXCRETION", level=1))

story.append(body(
    "<b>Other than the kidneys, lungs, liver and skin also help in the elimination of "
    "excretory wastes.</b> <i>[Exercise 5 asks for exactly this account.]</i>"))

story.append(data_table([
    ["Organ", "What it eliminates", "Notes"],
    ["<b>Lungs</b>",
     f"Large amounts of <b>{CO2}</b> (approximately <b>200 mL/minute</b>) and "
     "<b>significant quantities of water</b> every day",
     "The single largest route for carbon dioxide"],
    ["<b>Liver</b>",
     "<b>Bilirubin, biliverdin, cholesterol, degraded steroid hormones, vitamins</b> and "
     "<b>drugs</b>",
     "The <b>largest gland</b> in our body; secretes <b>bile</b>, containing these "
     "substances. Most of them <b>pass out along with digestive wastes</b>"],
    ["<b>Sweat glands</b> (skin)",
     "<b>NaCl</b>, <b>small amounts of urea</b>, <b>lactic acid</b>, etc.",
     "Sweat's <b>primary function is to facilitate a cooling effect</b> on the body surface; "
     "excretion is only <b>incidental</b>"],
    ["<b>Sebaceous glands</b> (skin)",
     "<b>Sterols, hydrocarbons</b> and <b>waxes</b> through <b>sebum</b>",
     "This secretion <b>provides a protective oily covering for the skin</b>"],
], col_widths=[19, 34, 47]))

story.append(gap())
story.append(note(
    "Both skin glands are worth reading carefully, because in each case excretion is a "
    "<b>side effect</b> of the gland's real job - cooling for sweat glands, oiling the skin "
    "for sebaceous glands. Note too that <b>small amounts of nitrogenous wastes could be "
    "eliminated through saliva</b>, which is the fifth and least-remembered accessory route."))

story.append(gap())
story.append(memory_aid(
    "<b>Accessory excretory organs: Lungs, Liver, Skin (and a little saliva).</b> Match each "
    f"to its signature waste - <b>lungs = {CO2}</b>, <b>liver = bile pigments (bilirubin, "
    "biliverdin)</b>, <b>sweat = NaCl</b>, <b>sebum = sterols and waxes</b>. Sweat is the one "
    "that also carries a little <b>urea</b>."))

# ======================================================================================
# ---- 16.8 DISORDERS OF THE EXCRETORY SYSTEM ---- F150-F164 (heading F150, opener F151)
# ======================================================================================

story.append(heading("16.8", "DISORDERS OF THE EXCRETORY SYSTEM", level=1))

story.append(body(
    "<b>Malfunctioning of the kidneys can lead to accumulation of urea in blood</b>, a "
    "condition called <b>uremia</b>, which is <b>highly harmful and may lead to kidney "
    "failure</b>. In such patients, <b>urea can be removed by a process called "
    "haemodialysis</b>."))

story.append(gap())
story.append(heading("16.8a", "Haemodialysis - How the Artificial Kidney Works", level=2))

story.append(process_flow([
    "<b>Blood drained from a convenient artery</b> is <b>pumped into a dialysing unit</b> "
    "after adding an <b>anticoagulant like heparin</b>.",
    "The unit contains a <b>coiled cellophane tube</b> surrounded by the <b>dialysing "
    "fluid</b>, which has the <b>same composition as that of plasma except the nitrogenous "
    "wastes</b>.",
    "The <b>porous cellophane membrane of the tube allows the passage of molecules based on "
    "concentration gradient</b>.",
    "As <b>nitrogenous wastes are absent in the dialysing fluid</b>, these substances "
    "<b>freely move out</b>, thereby <b>clearing the blood</b>.",
    "The <b>cleared blood is pumped back to the body through a vein</b> after adding "
    "<b>anti-heparin</b> to it.",
]))

story.append(gap())
# [VERIFICATION FIX] F159 was MISSING from the built PDF - NCERT's closing sentence on
# haemodialysis. Restored verbatim in meaning (Rule 1: zero information loss).
story.append(body(
    "<b>This method is a boon for thousands of uremic patients all over the world.</b>"))

story.append(gap())
story.append(note(
    "<b>This is an artificial kidney.</b> The design is elegant because it is subtractive: by "
    "making the dialysing fluid identical to plasma <b>except</b> for the wastes, only the "
    "wastes have a gradient to follow, so nothing valuable is lost. Note the two drug steps "
    "that bracket the procedure - <b>heparin</b> going in to stop clotting in the machine, "
    "<b>anti-heparin</b> coming out to restore normal clotting. <b>Exercise 12(c)</b>: "
    "dialysis fluid contains all the constituents as in plasma except the <b>nitrogenous "
    "wastes</b>."))

story.append(gap())
story.append(body(
    "<b>Kidney transplantation is the ultimate method in the correction of acute renal "
    "failures (kidney failure).</b>"))

story.append(b1(
    "A <b>functioning kidney is used in transplantation from a donor</b>, preferably a "
    "<b>close relative</b>, to <b>minimise its chances of rejection by the immune system of "
    "the host</b>."))
story.append(b1(
    "<b>Modern clinical procedures have increased the success rate of such a "
    "complicated technique.</b>"))

story.append(gap())
story.append(heading("16.8b", "Other Kidney Disorders", level=2))

story.append(data_table([
    ["Disorder", "Definition"],
    ["<b>Uremia</b>",
     "Accumulation of <b>urea in blood</b> due to malfunctioning of the kidneys; highly "
     "harmful, may lead to kidney failure"],
    ["<b>Renal calculi</b>",
     "<b>Stone or insoluble mass of crystallised salts</b> (oxalates, etc.) formed within "
     "the kidney"],
    ["<b>Glomerulonephritis</b>", "<b>Inflammation of glomeruli</b> of kidney"],
], col_widths=[24, 76]))

story.append(gap())
story.append(memory_aid(
    "<b>Locate each disorder by its word root.</b> <b>Ur-emia</b> = urea in the blood; "
    "<b>calculi</b> = stones (Latin for pebble, as in \"calculate\" with pebbles); "
    "<b>glomerulo-nephritis</b> = inflammation (-itis) of the glomeruli. Treatment ladder for "
    "failure: <b>haemodialysis</b> first, <b>kidney transplantation</b> as the ultimate "
    "correction."))

# ======================================================================================
# ---- SUMMARY ---- F171 (heading F171); figure-caption rows F165-F170 sit in their figure blocks
# ======================================================================================

story.append(heading("S", "SUMMARY", level=1))

story.append(body(
    f"Many nitrogen containing substances, ions, {CO2}, water, etc., that accumulate in the "
    "body have to be eliminated. Nature of nitrogenous wastes formed and their excretion vary "
    "among animals, mainly depending on the <b>habitat (availability of water)</b>. "
    "<b>Ammonia, urea and uric acid</b> are the major nitrogenous wastes excreted. "
    "<b>Protonephridia, nephridia, malpighian tubules, green glands</b> and the "
    "<b>kidneys</b> are the common excretory organs in animals. They not only eliminate "
    "nitrogenous wastes but also help in the <b>maintenance of ionic and acid-base balance</b> "
    "of body fluids."))

story.append(gap())
story.append(body(
    "In humans, the excretory system consists of <b>one pair of kidneys, a pair of ureters, a "
    "urinary bladder and a urethra</b>. Each kidney has over a million tubular structures "
    "called <b>nephrons</b>. Nephron is the <b>functional unit</b> of kidney and has two "
    "portions - <b>glomerulus</b> and <b>renal tubule</b>. Glomerulus is a tuft of capillaries "
    "formed from <b>afferent arterioles</b>, fine branches of renal artery. The renal tubule "
    "starts with a double walled <b>Bowman's capsule</b> and is further differentiated into a "
    "<b>proximal convoluted tubule (PCT)</b>, <b>Henle's loop (HL)</b> and <b>distal "
    "convoluted tubule (DCT)</b>. The DCTs of many nephrons join to a common <b>collecting "
    "duct</b>, many of which ultimately open into the <b>renal pelvis</b> through the "
    "<b>medullary pyramids</b>. The Bowman's capsule encloses the glomerulus to form "
    "<b>Malpighian or renal corpuscle</b>."))

story.append(gap())
story.append(body(
    "Urine formation involves three main processes, i.e., <b>filtration, reabsorption and "
    "secretion</b>. Filtration is a <b>non-selective</b> process performed by the glomerulus "
    "using the glomerular capillary blood pressure. About <b>1200 ml of blood</b> is filtered "
    "by the glomerulus per minute to form <b>125 ml of filtrate</b> in the Bowman's capsule "
    "per minute (<b>GFR</b>). <b>JGA</b>, a specialised portion of the nephrons, plays a "
    "significant role in the regulation of GFR. Nearly <b>99 per cent reabsorption</b> of the "
    "filtrate takes place through different parts of the nephrons. <b>PCT is the major site of "
    "reabsorption and selective secretion.</b> HL primarily helps to maintain the "
    f"<b>osmolar gradient (300 {MOSM} - 1200 {MOSM})</b> within the kidney interstitium. DCT "
    "and collecting duct allow extensive reabsorption of water and certain electrolytes, which "
    f"help in <b>osmoregulation</b>: {H}, {K} and {NH3} could be secreted into the filtrate by "
    "the tubules to maintain the ionic balance and pH of body fluids."))

story.append(gap())
story.append(body(
    "A <b>counter current mechanism</b> operates between the two limbs of the loop of Henle "
    "and those of <b>vasa recta</b> (capillary parallel to Henle's loop). The filtrate gets "
    "<b>concentrated as it moves down the descending limb</b> but is <b>diluted by the "
    "ascending limb</b>. <b>Electrolytes and urea are retained in the interstitium</b> by this "
    "arrangement. DCT and collecting duct concentrate the filtrate <b>about four times</b>, "
    f"i.e., from <b>300 {MOSM} to 1200 {MOSM}</b>, an excellent mechanism of conservation of "
    "water. Urine is stored in the urinary bladder till a <b>voluntary signal from CNS</b> "
    "carries out its release through urethra, i.e., <b>micturition</b>. <b>Skin, lungs and "
    "liver</b> also assist in excretion."))

# ======================================================================================
# ---- EXERCISES ---- F172 (heading F172)
# Source numbering reproduced verbatim, including the duplicated "(d)" in Exercise 7
# (rows F169/F170) - see inventory exercise-gap notes.
# ======================================================================================

story.append(heading("E", "EXERCISES", level=1))

story.append(note(
    "All twelve NCERT exercises are reproduced below with worked answers. Every answer is "
    "sourced from the chapter text above; where the chapter never states a needed definition "
    "(osmoregulation, Exercise 8) or never explains a required reason (Exercise 9), the answer "
    "is derived from what the chapter does say, and that is flagged in place."))

story.append(gap())
story.append(body("<b>1. Define Glomerular Filtration Rate (GFR).</b>"))
story.append(body(
    "<b>Answer.</b> GFR is the <b>amount of the filtrate formed by the kidneys per "
    "minute</b>. In a healthy individual it is approximately <b>125 ml/minute</b>, i.e., about "
    "<b>180 litres per day</b>."))

story.append(gap())
story.append(body("<b>2. Explain the autoregulatory mechanism of GFR.</b>"))
story.append(body(
    "<b>Answer.</b> The kidney regulates its own GFR through the <b>juxta glomerular "
    "apparatus (JGA)</b> - a sensitive region formed by cellular modifications in the "
    "<b>distal convoluted tubule</b> and the <b>afferent arteriole</b> at their point of "
    "contact. <b>A fall in GFR activates the JG cells to release renin</b>, which "
    "<b>stimulates the glomerular blood flow and thereby brings the GFR back to normal</b>. "
    "In its fuller form (16.5), renin converts <b>angiotensinogen to angiotensin I</b> and "
    "then to <b>angiotensin II</b>, a powerful <b>vasoconstrictor</b> that increases "
    f"glomerular blood pressure and GFR, and which also stimulates the <b>adrenal cortex</b> "
    f"to release <b>aldosterone</b>, causing reabsorption of {NA} and water from the distal "
    "tubule - again raising blood pressure and GFR."))

story.append(gap())
story.append(body("<b>3. Indicate whether the following statements are true or false:</b>"))
story.append(b1(
    "<b>(a) Micturition is carried out by a reflex. - TRUE.</b> Stretch receptors on the "
    "bladder wall signal the CNS, which sends motor messages causing contraction of the "
    "bladder's smooth muscles and simultaneous relaxation of the urethral sphincter."))
story.append(b1(
    "<b>(b) ADH helps in water elimination, making the urine hypotonic. - FALSE.</b> ADH is "
    "<b>anti</b>diuretic: it <b>facilitates water reabsorption</b> from the latter parts of "
    "the tubule and <b>prevents diuresis</b>, making the urine <b>hypertonic</b> "
    "(concentrated), not hypotonic."))
story.append(b1(
    "<b>(c) Protein-free fluid is filtered from blood plasma into the Bowman's capsule. - "
    "TRUE.</b> Almost all constituents of plasma <b>except the proteins</b> pass into the "
    "lumen of the Bowman's capsule; hence glomerular filtration is called <b>ultra "
    "filtration</b>."))
story.append(b1(
    "<b>(d) Henle's loop plays an important role in concentrating the urine. - TRUE.</b> Its "
    "role is <b>indirect but essential</b>: the loop maintains the high osmolarity of the "
    "medullary interstitium, and that gradient is what lets water leave the collecting duct."))
story.append(b1(
    "<b>(e) Glucose is actively reabsorbed in the proximal convoluted tubule. - TRUE.</b> "
    "Substances like glucose, amino acids and sodium are reabsorbed <b>actively</b>, and the "
    "PCT with its <b>brush border</b> epithelium is the major site of reabsorption."))

story.append(gap())
story.append(body("<b>4. Give a brief account of the counter current mechanism.</b>"))
story.append(body(
    "<b>Answer.</b> The <b>flow of filtrate in the two limbs of Henle's loop is in opposite "
    "directions</b>, and so is the <b>flow of blood in the two limbs of vasa recta</b> - "
    "hence a <b>counter current</b>. Their <b>proximity</b> plus this opposing flow maintains "
    f"an <b>increasing osmolarity towards the inner medullary interstitium</b>, from about "
    f"<b>300 {MOSM} in the cortex to 1200 {MOSM} in the inner medulla</b>, a gradient "
    "<b>caused mainly by NaCl and urea</b>. <b>NaCl is transported by the ascending limb of "
    "Henle's loop and exchanged with the descending limb of vasa recta</b>; it is then "
    "<b>returned to the interstitium by the ascending portion of vasa recta</b>. Similarly, "
    "<b>small amounts of urea enter the thin segment of the ascending limb</b> and are "
    "<b>transported back to the interstitium by the collecting tubule</b>. Electrolytes and "
    "urea are thus <b>retained in the interstitium</b>, and this gradient permits easy passage "
    "of water out of the collecting tubule - letting human kidneys produce urine <b>nearly "
    "four times concentrated</b> than the initial filtrate."))

story.append(gap())
story.append(body("<b>5. Describe the role of liver, lungs and skin in excretion.</b>"))
story.append(b1(
    f"<b>Lungs</b> remove large amounts of <b>{CO2}</b> (approximately <b>200 mL/minute</b>) "
    "and <b>significant quantities of water</b> every day."))
story.append(b1(
    "<b>Liver</b>, the largest gland in the body, secretes <b>bile</b> containing "
    "<b>bilirubin, biliverdin, cholesterol, degraded steroid hormones, vitamins and "
    "drugs</b>. Most of these <b>pass out along with digestive wastes</b>."))
story.append(b1(
    "<b>Skin</b> excretes through two gland types. <b>Sweat glands</b> remove <b>NaCl, small "
    "amounts of urea, lactic acid</b>, etc., though sweat's primary function is <b>cooling</b> "
    "the body surface. <b>Sebaceous glands</b> eliminate <b>sterols, hydrocarbons and "
    "waxes</b> through <b>sebum</b>, which provides a <b>protective oily covering</b> for the "
    "skin."))

story.append(gap())
story.append(body("<b>6. Explain micturition.</b>"))
story.append(body(
    "<b>Answer.</b> <b>Micturition is the process of release of urine</b>, and the neural "
    "mechanisms causing it constitute the <b>micturition reflex</b>. Urine formed by the "
    "nephrons is carried to the <b>urinary bladder</b>, where it is <b>stored till a "
    "voluntary signal is given by the CNS</b>. That signal is <b>initiated by the stretching "
    "of the urinary bladder</b> as it fills: <b>stretch receptors on the bladder wall send "
    "signals to the CNS</b>, and the <b>CNS passes on motor messages</b> that cause "
    "<b>contraction of the smooth muscles of the bladder</b> with <b>simultaneous relaxation "
    "of the urethral sphincter</b>, releasing the urine. An adult human excretes <b>1 to 1.5 "
    "litres of urine per day</b>."))

story.append(gap())
story.append(body("<b>7. Match the items of column I with those of column II:</b>"))

story.append(data_table([
    ["Column I", "Column II", "Match"],
    ["(a) Ammonotelism", "(i) Birds", "<b>(iii) Bony fish</b>"],
    ["(b) Bowman's capsule", "(ii) Water reabsorption", "<b>(v) Renal tubule</b>"],
    ["(c) Micturition", "(iii) Bony fish", "<b>(iv) Urinary bladder</b>"],
    ["(d) Uricotelism", "(iv) Urinary bladder", "<b>(i) Birds</b>"],
    ["(d) ADH", "(v) Renal tubule", "<b>(ii) Water reabsorption</b>"],
], col_widths=[30, 34, 36]))

story.append(note(
    "The second-last and last items are <b>both numbered \"(d)\"</b> in the NCERT source; the "
    "numbering is reproduced verbatim above. Read the fifth row as <b>(e) ADH</b>. So the key "
    "is <b>(a)-(iii), (b)-(v), (c)-(iv), (d)-(i), (e)-(ii)</b>."))

story.append(gap())
story.append(body("<b>8. What is meant by the term osmoregulation?</b>"))
story.append(body(
    "<b>Answer.</b> <b>Osmoregulation is the maintenance of a constant water and electrolyte "
    "(ionic) balance in the body fluids</b> - regulation of the <b>osmotic concentration</b> "
    "of those fluids - so that cells are neither swollen by excess water nor shrunken by its "
    "loss. In humans the <b>DCT and collecting duct</b> allow extensive reabsorption of water "
    "and certain electrolytes, which is what achieves osmoregulation, under the control of "
    "<b>ADH</b> and <b>aldosterone</b>. In many invertebrates it is the chief job of the "
    "excretory organs: <b>protonephridia</b> in <i>Planaria</i> are used <b>primarily for "
    "osmoregulation</b>, and <b>nephridia</b> and <b>malpighian tubules</b> also maintain "
    "fluid and ionic balance."))
story.append(note(
    "<b>Source gap.</b> The chapter uses \"osmoregulation\" in 16.0, 16.3 and the Summary but "
    "<b>never defines it</b>, although this exercise demands the definition. The definition "
    "above is supplied from standard usage and tied back to what the chapter does state."))

story.append(gap())
story.append(body(
    "<b>9. Terrestrial animals are generally either ureotelic or uricotelic, not ammonotelic, "
    "why?</b>"))
story.append(body(
    "<b>Answer.</b> Because <b>ammonia is the most toxic</b> of the three nitrogenous wastes "
    "and <b>requires a large amount of water for its elimination</b>, whereas <b>uric acid, "
    "being the least toxic, can be removed with a minimum loss of water</b>. A terrestrial "
    "animal has only limited water available and cannot afford to lose that much of it, so "
    "<b>terrestrial adaptation necessitated the production of lesser toxic nitrogenous "
    "wastes</b> like <b>urea and uric acid</b> for the <b>conservation of water</b>. "
    "Ureotelic animals convert ammonia into <b>urea in the liver</b> and excrete it via the "
    "kidneys; uricotelic animals excrete <b>uric acid as a pellet or paste</b>, which is the "
    "driest option of all. Ammonotelic excretion, by contrast, depends on <b>diffusion across "
    "body or gill surfaces into surrounding water</b> - a route simply not available on land."))

story.append(gap())
story.append(body(
    "<b>10. What is the significance of juxta glomerular apparatus (JGA) in kidney "
    "function?</b>"))
story.append(body(
    "<b>Answer.</b> The JGA is a <b>specialised, sensitive region formed by cellular "
    "modifications in the distal convoluted tubule and the afferent arteriole</b> at their "
    "point of contact, and it plays a <b>significant role in the regulation of GFR</b>. It is "
    "the kidney's own <b>autoregulatory</b> device: <b>a fall in glomerular blood flow, "
    "glomerular blood pressure or GFR activates the JG cells to release renin</b>, which "
    "triggers the <b>renin-angiotensin mechanism</b> - angiotensinogen to <b>angiotensin "
    "I</b>, then <b>angiotensin II</b>, a powerful <b>vasoconstrictor</b> that raises "
    "glomerular blood pressure and GFR, and which also makes the <b>adrenal cortex release "
    f"aldosterone</b>, causing reabsorption of {NA} and water from the distal tubule. The net "
    "effect is restoration of blood pressure and GFR - held in check by <b>ANF</b> from the "
    "atria, which causes <b>vasodilation</b> and lowers blood pressure."))

story.append(gap())
story.append(body("<b>11. Name the following:</b>"))
story.append(b1(
    "<b>(a) A chordate animal having flame cells as excretory structures - <i>Amphioxus</i></b> "
    "(the cephalochordate). Flame cells, or <b>protonephridia</b>, also occur in "
    "Platyhelminthes such as <i>Planaria</i>, in rotifers and in some annelids, but among "
    "those only <i>Amphioxus</i> is a chordate."))
story.append(b1(
    "<b>(b) Cortical portions projecting between the medullary pyramids in the human kidney - "
    "Columns of Bertini</b> (the renal columns)."))
story.append(b1(
    "<b>(c) A loop of capillary running parallel to the Henle's loop - vasa recta</b> (a 'U' "
    "shaped minute vessel of the peritubular capillary network; <b>absent or highly reduced in "
    "cortical nephrons</b>)."))

story.append(gap())
story.append(body("<b>12. Fill in the gaps:</b>"))
story.append(b1(
    "<b>(a)</b> Ascending limb of Henle's loop is <b>impermeable</b> to water whereas the "
    "descending limb is <b>permeable</b> to it."))
story.append(b1(
    "<b>(b)</b> Reabsorption of water from distal parts of the tubules is facilitated by "
    "hormone <b>ADH (antidiuretic hormone, vasopressin)</b>."))
story.append(b1(
    "<b>(c)</b> Dialysis fluid contains all the constituents as in plasma except "
    "<b>the nitrogenous wastes</b> (e.g., urea)."))
story.append(b1(
    "<b>(d)</b> A healthy adult human excretes (on an average) <b>25-30</b> gm of urea/day."))

# ======================================================================================
# ---- BUILD ---- (SS0.6: build_pdf owns page furniture)
# ======================================================================================

sys.exit(build_pdf(
    OUT_PDF, story,
    title="Class 11 Chapter 16 - Excretory Products and their Elimination (NEET notes)",
    subject="NEET Biology"))
