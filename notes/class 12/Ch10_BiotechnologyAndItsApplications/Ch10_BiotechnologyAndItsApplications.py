"""
NCERT Biology -> NEET replacement notes
Class 12, Chapter 10 : Biotechnology and Its Applications

Source  : Chapter/class 12/Chapter 10 - Biotechnology and its Applications.pdf
Built to: SUPREME COMMAND PROMPT.md v6 (fixed-pass gated edition, shared canon module)

Run from the repository root:
    python3 "notes/class 12/Ch10_BiotechnologyAndItsApplications/Ch10_BiotechnologyAndItsApplications.py"

Figures: every asset in assets/ has already been clip-extracted at 300 dpi and pushed
through PIL convert("L") + autocontrast. figure() re-asserts mode == "L" at build time,
so a raw or colour asset cannot silently reach the PDF (SUPREME COMMAND PROMPT.md v6 §4.4).

Structure of this file:
  1. Imports from neet_template.py -- the frozen canon (page geometry, colours, Times New
     Roman styles, and every sanctioned helper: heading, keyterm, process_flow, note,
     memory_aid, data_table, figure, title_block). Nothing here redeclares the canon (§0.6).
  2. One linear sequence of story.append(...) calls in Content Order (§5),
     each block commented with its NCERT section number for fast auditing.
"""

import os
import sys

from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Spacer, KeepTogether, Table, TableStyle

# neet_template.py lives at the repository root; chapter scripts live several
# directories deep, so walk upward from this file until the module is found and
# put that directory on sys.path. Standard bootstrap for every chapter (§0.6).
_here = os.path.dirname(os.path.abspath(__file__))
_root = _here
while not os.path.exists(os.path.join(_root, "neet_template.py")):
    _parent = os.path.dirname(_root)
    if _parent == _root:
        raise RuntimeError("neet_template.py not found in any parent directory of this script")
    _root = _parent
if _root not in sys.path:
    sys.path.insert(0, _root)

from neet_template import (
    STYLES, FRAME_WIDTH, DARK_GREY, GRID_LINE,
    heading, keyterm, process_flow, note, memory_aid, data_table, title_block,
    build_pdf,
)
from neet_template import figure as _shared_figure

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch10_BiotechnologyAndItsApplications.pdf")


def figure(asset_name: str, caption_text: str, max_width_cm: float = 15.9):
    """Chapter-local wrapper: binds the shared figure() helper to this chapter's own
    assets/ folder so every call below stays unchanged (asset_name, caption_text,
    max_width_cm=...)."""
    return _shared_figure(asset_name, caption_text, ASSETS, max_width_cm=max_width_cm)


# --------------------------------------------------------------------------------------
# STORY -- Content Order (§5)
# --------------------------------------------------------------------------------------

story = []

# ---- Title block (page 1, no separate title page) ----
story.extend(title_block("Biotechnology and Its Applications"))

# ---- 10.0 Chapter introduction: what this chapter is about (F001-F007) ----
story.append(heading("10", "WHAT THIS CHAPTER IS ABOUT", 1))
story.append(keyterm(
    "<b>Biotechnology</b>, as learnt in the previous chapter, essentially deals with the "
    "<b>industrial-scale production</b> of <b>biopharmaceuticals and biologicals</b> using "
    "<b>genetically modified microbes, fungi, plants and animals</b>."))
story.append(Paragraph(
    "The applications of biotechnology include <b>therapeutics, diagnostics, genetically "
    "modified crops for agriculture, processed food, bioremediation, waste treatment, and "
    "energy production</b>.", STYLES["Body"]))
story.append(Paragraph(
    "There are <b>three critical research areas</b> of biotechnology:", STYLES["Body"]))
story.append(process_flow([
    "Providing the <b>best catalyst</b> in the form of an improved organism, usually a "
    "<b>microbe</b> or a <b>pure enzyme</b>.",
    "Creating <b>optimal conditions</b> through engineering for a catalyst to act.",
    "<b>Downstream processing</b> technologies to purify the protein / organic compound.",
]))
story.append(Paragraph(
    "This chapter looks at how human beings have used biotechnology to improve the quality of "
    "human life, especially in the fields of <b>food production</b> and <b>health</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 4))

# =============================== 10.1 AGRICULTURE ====================================
# ---- 10.1 Biotechnological Applications in Agriculture: three options (F008, F009) ----
story.append(heading("10.1", "BIOTECHNOLOGICAL APPLICATIONS IN AGRICULTURE", 1))
story.append(Paragraph(
    "There are <b>three options</b> that can be thought of for increasing food production:",
    STYLES["Body"]))
story.append(process_flow([
    "<b>Agro-chemical based</b> agriculture.",
    "<b>Organic</b> agriculture.",
    "<b>Genetically engineered crop-based</b> agriculture.",
]))
story.append(Spacer(1, 3))

# ---- 10.1 The limits of the Green Revolution (F010-F012) ----
story.append(heading("10.1", "Why conventional methods were not enough", 2))
story.append(Paragraph(
    "The <b>Green Revolution</b> succeeded in <b>tripling the food supply</b>, but yet it was "
    "not enough to feed the growing human population. Increased yields have <b>partly</b> been "
    "due to the use of improved crop varieties, but <b>mainly</b> due to better management "
    "practices and the use of <b>agrochemicals (fertilisers and pesticides)</b>. However, for "
    "farmers in the developing world, agrochemicals are often <b>too expensive</b>, and further "
    "increases in yield with existing varieties are <b>not possible using conventional "
    "breeding</b>.", STYLES["Body"]))
story.append(Spacer(1, 3))

# ---- 10.1 Tissue culture and totipotency (F013-F025) ----
story.append(heading("10.1", "Tissue culture, totipotency and micro-propagation", 2))
story.append(Paragraph(
    "As traditional <b>breeding techniques</b> failed to keep pace with demand and to provide "
    "sufficiently fast and efficient systems for crop improvement, another technology called "
    "<b>tissue culture</b> got developed. Scientists learnt, during the <b>1950s</b>, that "
    "whole plants could be regenerated from <b>explants</b>.", STYLES["Body"]))
story.append(keyterm(
    "An <b>explant</b> is any part of a plant taken out and grown in a test tube, under "
    "<b>sterile conditions</b> in special <b>nutrient media</b>. The capacity to generate a "
    "whole plant from any cell / explant is called <b>totipotency</b>."))
story.append(keyterm(
    "The nutrient medium must provide a <b>carbon source such as sucrose</b> and also "
    "<b>inorganic salts, vitamins, amino acids</b> and <b>growth regulators like auxins, "
    "cytokinins</b>, etc."))
story.append(Paragraph(
    "By applying these methods it is possible to achieve propagation of a <b>large number of "
    "plants in very short durations</b>.", STYLES["Body"]))
story.append(keyterm(
    "This method of producing thousands of plants through tissue culture is called "
    "<b>micro-propagation</b>. Each of these plants is <b>genetically identical</b> to the "
    "original plant from which it was grown, i.e., they are <b>somaclones</b>. Many important "
    "food plants like <b>tomato, banana, apple</b>, etc., have been produced on a commercial "
    "scale using this method."))
story.append(Paragraph(
    "Another important application of the method is the <b>recovery of healthy plants from "
    "diseased plants</b>. Even if a plant is infected with a <b>virus</b>, the <b>meristem "
    "(apical and axillary) is free of virus</b>. Hence, one can <b>remove the meristem and grow "
    "it <i>in vitro</i></b> to obtain <b>virus-free plants</b>. Scientists have succeeded in "
    "culturing meristems of <b>banana, sugarcane, potato</b>, etc.", STYLES["Body"]))
story.append(Spacer(1, 3))

# ---- 10.1 Protoplasts and somatic hybridisation (F026-F031) ----
story.append(heading("10.1", "Somatic hybridisation: the pomato", 2))
story.append(Paragraph(
    "Scientists have even isolated <b>single cells</b> from plants and, after digesting their "
    "cell walls, have isolated <b>naked protoplasts</b> (surrounded by plasma membranes). "
    "Isolated protoplasts from <b>two different varieties</b> of plants -- each having a "
    "desirable character -- can be <b>fused</b> to get <b>hybrid protoplasts</b>, which can be "
    "further grown to form a new plant.", STYLES["Body"]))
story.append(keyterm(
    "These hybrids are called <b>somatic hybrids</b>, while the process is called <b>somatic "
    "hybridisation</b>."))
story.append(Paragraph(
    "For example, a protoplast of <b>tomato</b> fused with that of <b>potato</b>, and then "
    "grown, forms new hybrid plants combining tomato and potato characteristics. This has been "
    "achieved -- resulting in the formation of <b>pomato</b>. Unfortunately, this plant did "
    "<b>not</b> have all the desired combination of characteristics for its commercial "
    "utilisation.", STYLES["Body"]))
story.append(Spacer(1, 3))

# ---- 10.1 GMO definition and the benefits of GM plants (F032-F038, F135, F136) ----
story.append(heading("10.1", "Genetically Modified Organisms (GMO)", 2, has_table=True))
story.append(keyterm(
    "Plants, bacteria, fungi and animals whose <b>genes have been altered by manipulation</b> "
    "are called <b>Genetically Modified Organisms (GMO)</b>. GMOs are created by using methods "
    "<b>other than natural methods</b> to transfer one or more genes from one organism to "
    "another, generally using recombinant DNA technology."))
story.append(Paragraph(
    "<b>GM plants have been useful in increasing crop yields.</b> More specifically, genetic "
    "modification has:", STYLES["Body"]))
story.append(data_table([
    ["Benefit of genetic modification", "What it achieves"],
    ["(i) Tolerance to <b>abiotic stresses</b>",
     "Made crops more tolerant to <b>cold, drought, salt and heat</b>."],
    ["(ii) <b>Less chemical pesticide</b>",
     "Reduced reliance on chemical pesticides (<b>pest-resistant crops</b>)."],
    ["(iii) <b>Less post-harvest loss</b>",
     "Helped to reduce <b>post-harvest losses</b>."],
    ["(iv) <b>Efficient mineral use</b>",
     "Increased efficiency of <b>mineral usage</b> by plants (this prevents early exhaustion "
     "of soil fertility)."],
    ["(v) <b>Better nutrition</b>",
     "Enhanced <b>nutritional value</b> of food, e.g., <b>golden rice</b>, i.e., Vitamin 'A' "
     "enriched rice."],
], col_widths=[1.5, 3.4]))
story.append(Paragraph(
    "In addition, GM has been used to create <b>tailor-made plants</b> to supply alternative "
    "resources to industries, in the form of <b>starches, fuels and pharmaceuticals</b>.",
    STYLES["Body"]))
story.append(Spacer(1, 4))

# ---- 10.1 Bt cotton and the Bt toxin (F039-F054) + Figure 10.1 ----
story.append(heading("10.1", "Pest-resistant plants (1): Bt cotton", 3))
story.append(Paragraph(
    "One application of biotechnology in agriculture is the production of <b>pest-resistant "
    "plants</b>, which could decrease the amount of pesticide used. <b>Bt toxin</b> is produced "
    "by a bacterium called <b><i>Bacillus thuringiensis</i></b> (<b>Bt</b> for short). The Bt "
    "toxin gene has been <b>cloned</b> from the bacteria and <b>expressed in plants</b> to "
    "provide resistance to insects without the need for insecticides -- in effect creating a "
    "<b>bio-pesticide</b>. Examples are <b>Bt cotton, Bt corn, rice, tomato, potato and "
    "soyabean</b>, etc.", STYLES["Body"]))
story.append(Paragraph(
    "Some strains of <i>Bacillus thuringiensis</i> produce proteins that kill certain insects "
    "such as <b>lepidopterans</b> (tobacco budworm, armyworm), <b>coleopterans</b> (beetles) "
    "and <b>dipterans</b> (flies, mosquitoes). <i>B. thuringiensis</i> forms <b>protein "
    "crystals</b> during a particular phase of its growth, and these crystals contain a "
    "<b>toxic insecticidal protein</b>.", STYLES["Body"]))
story.append(note(
    "<b>Why does the Bt toxin not kill the <i>Bacillus</i> itself?</b> Because the Bt toxin "
    "protein exists as <b>inactive protoxins</b>. It becomes toxic only after an insect ingests "
    "it, so the crystal is harmless while stored inside the bacterium. (This is the answer to "
    "Exercise 4: the crystals do not kill the bacteria because <b>the toxin is inactive</b>.)"))
story.append(Paragraph(
    "The mechanism of insect killing runs as follows:", STYLES["Body"]))
story.append(process_flow([
    "An insect <b>ingests</b> the inactive protoxin.",
    "The <b>alkaline pH of the gut solubilises the crystals</b>, converting the protoxin into "
    "the <b>active form</b> of the toxin.",
    "The activated toxin <b>binds to the surface of midgut epithelial cells</b> and creates "
    "<b>pores</b>.",
    "The pores cause <b>cell swelling and lysis</b>, and eventually the <b>death of the "
    "insect</b>.",
]))
story.append(Paragraph(
    "Specific Bt toxin genes were isolated from <i>Bacillus thuringiensis</i> and incorporated "
    "into several crop plants such as <b>cotton</b> (Figure 10.1). The <b>choice of genes "
    "depends upon the crop and the targeted pest</b>, as most Bt toxins are "
    "<b>insect-group specific</b>.", STYLES["Body"]))
# [VERIFICATION FIX - Pass 3(a)] This two-row table straddled the page 2 / page 3 break,
# so one cry gene sat under a repeated header on a page of its own. A table this short
# must never split: KeepTogether holds the header and both data rows on one page.
story.append(KeepTogether(data_table([
    ["<b>cry</b> gene", "Pest it controls"],
    ["<b>cryIAc</b> and <b>cryIIAb</b>", "Control the <b>cotton bollworms</b>."],
    ["<b>cryIAb</b>", "Controls the <b>corn borer</b>."],
], col_widths=[1.6, 4.0])))
story.append(note(
    "The toxins are coded by a <b>gene family called <i>cry</i></b>; there are a number of them, "
    "and <b>cryIAc</b> is one member. (The NCERT line 'the toxin is coded by a gene cryIAc named "
    "cry' compresses this family / member relationship.)"))
# [VERIFICATION FIX - Pass 3(b)] The caption credited colour with separating (a) from (b),
# but dark-vs-white is tonal and survives the mono conversion untouched. The one feature in
# this figure that genuinely relied on colour -- the green, still-closed centre boll, which
# NCERT leaves unlabelled -- was not named at all, so in monochrome a reader sees three
# bolls and has words for only two. Both corrected here (inventory "Colour-dependent
# figures", Fig 10.1 row).
story.append(figure(
    "fig_10_1.png",
    "Fig. 10.1 -- Cotton boll: (a) a <b>cotton boll destroyed by bollworms</b> (dark, dried and "
    "shrivelled on the left); (b) a <b>fully mature cotton boll</b> (the open white boll on the "
    "right). The (a) / (b) contrast is one of <b>tone, not colour</b> -- dark versus white -- so "
    "it survives this monochrome reproduction exactly as printed. The <b>centre boll</b>, green "
    "and still closed in the source photograph and mid-grey here, is an unopened boll that NCERT "
    "does not label."))
story.append(Spacer(1, 4))

# ---- 10.1 Pest-resistant plants via RNAi (F055-F065) + Figure 10.2 ----
story.append(heading("10.1", "Pest-resistant plants (2): RNA interference (RNAi)", 3))
story.append(Paragraph(
    "Several <b>nematodes</b> parasitise a wide variety of plants and animals, including human "
    "beings. A nematode <b><i>Meloidegyne incognitia</i></b> infects the <b>roots of tobacco "
    "plants</b> and causes a great reduction in yield. A novel strategy to prevent this "
    "infestation was based on the process of <b>RNA interference (RNAi)</b>.", STYLES["Body"]))
story.append(keyterm(
    "<b>RNAi</b> takes place in <b>all eukaryotic organisms</b> as a method of <b>cellular "
    "defence</b>. It involves <b>silencing of a specific mRNA</b> due to a <b>complementary "
    "dsRNA molecule</b> that binds to and prevents translation of the mRNA (silencing). The "
    "source of this complementary RNA could be an infection by <b>viruses having RNA "
    "genomes</b>, or <b>mobile genetic elements (transposons)</b> that replicate via an RNA "
    "intermediate."))
story.append(Paragraph(
    "The nematode was defeated by turning RNAi against it:", STYLES["Body"]))
story.append(process_flow([
    "Using <b><i>Agrobacterium</i> vectors</b>, <b>nematode-specific genes</b> were introduced "
    "into the host plant (Figure 10.2).",
    "The DNA was introduced such that it produced <b>both sense and anti-sense RNA</b> in the "
    "host cells.",
    "Being complementary to each other, these two RNAs formed a <b>double-stranded RNA "
    "(dsRNA)</b> that <b>initiated RNAi</b> and thus <b>silenced the specific mRNA of the "
    "nematode</b>.",
    "The parasite <b>could not survive</b> in a transgenic host expressing specific interfering "
    "RNA, so the <b>transgenic plant protected itself</b> from the parasite.",
]))
# [VERIFICATION FIX - Pass 3(b)] The caption called the galls "the colour-highlighted
# feature". They are not: both root systems are the same yellow-tan in the source, and the
# galls are picked out by white arrows and by their swollen shape -- cues that survive
# monochrome intact. Restated per the inventory "Colour-dependent figures" Fig 10.2 row.
story.append(figure(
    "fig_10_2.png",
    "Fig. 10.2 -- Host plant-generated dsRNA triggers protection against nematode infestation: "
    "(a) <b>Roots of a typical control plant</b>, where the <b>white arrows</b> mark the swollen "
    "nematode-induced galls; (b) <b>transgenic plant roots 5 days after deliberate infection of "
    "nematode but protected through the novel mechanism</b> -- the arrows here point to thin, "
    "healthy roots and no galls have formed. Both root systems are the same colour in the "
    "source: the galls are identified by the <b>arrows and their swelling</b>, so nothing is lost "
    "in monochrome."))
story.append(Spacer(1, 4))

# =============================== 10.2 MEDICINE ======================================
# ---- 10.2 Biotechnological Applications in Medicine (F066-F069, F137) ----
story.append(heading("10.2", "BIOTECHNOLOGICAL APPLICATIONS IN MEDICINE", 1))
story.append(Paragraph(
    "The <b>recombinant DNA technological processes</b> have made an immense impact in the area "
    "of healthcare by enabling <b>mass production of safe and more effective therapeutic "
    "drugs</b>.", STYLES["Body"]))
story.append(keyterm(
    "Because the <b>recombinant therapeutics are identical to human proteins</b>, they <b>do "
    "not induce unwanted immunological responses</b> and are <b>free from the risk of "
    "infection</b> -- unlike similar products isolated from <b>non-human sources</b>."))
story.append(Paragraph(
    "At present, about <b>30 recombinant therapeutics</b> have been approved for human use the "
    "world over. In <b>India, 12</b> of these are presently being marketed.", STYLES["Body"]))
story.append(Spacer(1, 4))

# ---- 10.2.1 Genetically Engineered Insulin (F070-F082, F138) + Figure 10.3 ----
story.append(heading("10.2.1", "Genetically Engineered Insulin", 2))
story.append(Paragraph(
    "Management of <b>adult-onset diabetes</b> is possible by taking <b>insulin</b> at regular "
    "time intervals. What would a diabetic patient do if enough human insulin were not "
    "available? One would have to <b>isolate and use insulin from other animals</b> -- but "
    "would animal insulin be just as effective, and would it not <b>elicit an immune "
    "response</b> in the human body? The elegant answer is a <b>bacterium that could make human "
    "insulin</b>: one can then easily grow a large quantity of bacteria and make as much "
    "insulin as needed.", STYLES["Body"]))
story.append(Paragraph(
    "Insulin used for diabetes was <b>earlier extracted from the pancreas of slaughtered cattle "
    "and pigs</b>. Insulin from an animal source, though, caused <b>some patients to develop "
    "allergy or other reactions</b> to the foreign protein.", STYLES["Body"]))
story.append(keyterm(
    "<b>Insulin</b> consists of <b>two short polypeptide chains -- chain A and chain B</b> -- "
    "that are linked together by <b>disulphide bridges (S-S)</b> (Figure 10.3)."))
story.append(Paragraph(
    "In mammals, including humans, insulin is synthesised as a <b>pro-hormone</b> (like a "
    "pro-enzyme, the pro-hormone also needs to be <b>processed</b> before it becomes a fully "
    "mature and functional hormone). This pro-hormone -- <b>proinsulin</b> -- contains an extra "
    "stretch called the <b>C peptide</b>, which is <b>not present in the mature insulin</b> and "
    "is <b>removed during maturation</b> into insulin.", STYLES["Body"]))
story.append(Paragraph(
    "The <b>main challenge</b> for producing insulin using <b>rDNA techniques</b> was getting "
    "insulin <b>assembled into a mature form</b>. The route used was:", STYLES["Body"]))
story.append(process_flow([
    "In <b>1983</b>, <b>Eli Lilly</b>, an American company, prepared <b>two DNA sequences</b> "
    "corresponding to the <b>A and B chains</b> of human insulin.",
    "These sequences were <b>introduced into plasmids of <i>E. coli</i></b> to produce the "
    "insulin chains. <b>Chains A and B were produced separately</b>.",
    "The two chains were <b>extracted and combined by creating disulfide bonds</b> to form "
    "<b>human insulin</b> -- whose structure is <b>absolutely identical</b> to that of the "
    "natural molecule.",
]))
# [VERIFICATION FIX - Pass 3(b)] This is the chapter's one truly colour-dependent figure:
# the source draws the A chain in blue and the B chain in green, and those two hues convert
# to near-identical greys, while the floating "A peptide" / "B peptide" labels do not touch
# their chains. The caption named both peptides but never said which drawn chain is which,
# so in monochrome A and B were indistinguishable. Position and shape now carry it in words
# (inventory "Colour-dependent figures", Fig 10.3 row).
story.append(figure(
    "fig_10_3.png",
    "Fig. 10.3 -- Maturation of pro-insulin into insulin (simplified). <b>Proinsulin</b> (the "
    "looped precursor at the top, held by <b>S-S disulphide bridges</b>) is processed by "
    "removing the connecting arc, yielding mature <b>Insulin</b> -- the joined <b>A peptide</b> "
    "and <b>B peptide</b> -- plus the discarded <b>Free C peptide</b>. Reading the lower half: "
    "the <b>upper wavy chain is the A peptide</b>, the <b>lower straight chain is the B "
    "peptide</b>, and the <b>free arc below is the C peptide</b> removed on maturation. (The "
    "source distinguished the A and B chains by colour alone, which is why they are named here "
    "by position and shape.)",
    max_width_cm=9.5))
story.append(Spacer(1, 4))

# ---- 10.2.2 Gene Therapy (F083-F094, F139, F140) ----
story.append(heading("10.2.2", "Gene Therapy", 2))
story.append(keyterm(
    "<b>Gene therapy</b> is a collection of methods that allows <b>correction of a gene "
    "defect</b> diagnosed in a child / embryo: <b>genes are inserted into a person's cells and "
    "tissues</b> to treat a disease. It does so by <b>replacing a defective mutant allele with "
    "a functional one</b>, or by <b>gene targeting</b> (which involves gene amplification). "
    "Correction involves <b>delivery of a normal gene</b> into the individual or embryo to take "
    "over the function of, and compensate for, the <b>non-functional gene</b>."))
story.append(Paragraph(
    "The <b>first clinical gene therapy</b> was given in <b>1990</b> to a <b>4-year-old girl</b> "
    "with <b>adenosine deaminase (ADA) deficiency</b>. This enzyme is <b>crucial for the immune "
    "system</b> to function; the disorder is caused by the <b>deletion of the gene for adenosine "
    "deaminase</b>.", STYLES["Body"]))
story.append(data_table([
    ["Earlier approaches to ADA deficiency", "Limitation"],
    ["<b>Bone marrow transplantation</b> (in some children).", "<b>Not completely curative.</b>"],
    ["<b>Enzyme replacement therapy</b> -- functional ADA given by <b>injection</b>.",
     "<b>Not completely curative.</b>"],
], col_widths=[3.2, 1.4]))
story.append(Paragraph(
    "The gene-therapy route used a <b>retroviral vector</b> -- one of the viruses that attack "
    "their hosts and introduce their genetic material into the host cell as part of their "
    "replication cycle, and are therefore used as <b>vectors to transfer healthy genes</b>:",
    STYLES["Body"]))
story.append(process_flow([
    "<b>Lymphocytes</b> from the blood of the patient are grown in a <b>culture outside the "
    "body</b>.",
    "A <b>functional ADA cDNA</b> (using a <b>retroviral vector</b>) is introduced into these "
    "lymphocytes.",
    "The lymphocytes are <b>returned to the patient</b>.",
]))
story.append(note(
    "As these cultured cells are <b>not immortal</b>, the patient requires <b>periodic infusion</b> "
    "of such genetically engineered lymphocytes. However, if the gene isolated from marrow cells "
    "producing ADA were introduced into cells at <b>early embryonic stages</b>, it could be a "
    "<b>permanent cure</b>."))
story.append(Spacer(1, 4))

# ---- 10.2.3 Molecular Diagnosis (F095-F105) ----
story.append(heading("10.2.3", "Molecular Diagnosis", 2))
story.append(Paragraph(
    "For effective treatment of a disease, <b>early diagnosis</b> and understanding its "
    "<b>pathophysiology</b> are very important. Using conventional methods of diagnosis "
    "(<b>serum and urine analysis</b>, etc.), early detection is <b>not possible</b>. "
    "<b>Recombinant DNA technology, Polymerase Chain Reaction (PCR)</b> and <b>Enzyme Linked "
    "Immuno-sorbent Assay (ELISA)</b> are some of the techniques that serve the purpose of "
    "early diagnosis.", STYLES["Body"]))
story.append(Paragraph(
    "Presence of a <b>pathogen</b> (bacteria, viruses, etc.) is normally suspected only "
    "<b>after</b> it has produced a disease symptom -- by which time the concentration of the "
    "pathogen is already <b>very high</b> in the body.", STYLES["Body"]))
story.append(data_table([
    ["Technique", "Principle", "Use"],
    ["<b>PCR</b>",
     "<b>Amplification of the nucleic acid</b> of a bacterium or virus, so even a <b>very low "
     "concentration</b> (before symptoms appear) can be detected.",
     "Routinely used to <b>detect HIV</b> in suspected AIDS patients; to detect <b>mutations "
     "in genes</b> in suspected cancer patients; and to identify many other <b>genetic "
     "disorders</b>."],
    ["<b>Radioactive probe</b> (hybridisation)",
     "A <b>single-stranded DNA or RNA tagged with a radioactive molecule (probe)</b> is "
     "allowed to <b>hybridise to its complementary DNA</b> in a clone of cells, followed by "
     "detection using <b>autoradiography</b>.",
     "The clone having the <b>mutated gene</b> will <b>not appear</b> on the photographic film, "
     "because the probe has <b>no complementarity</b> with the mutated gene."],
    ["<b>ELISA</b>",
     "Based on the principle of <b>antigen-antibody interaction</b>.",
     "Infection by a pathogen is detected by the presence of <b>antigens</b> (proteins, "
     "glycoproteins, etc.) or by detecting the <b>antibodies</b> synthesised against the "
     "pathogen."],
], col_widths=[1.1, 3.0, 3.0]))
story.append(Spacer(1, 4))

# =============================== 10.3 TRANSGENIC ANIMALS =============================
# ---- 10.3 Transgenic Animals (F106-F114) ----
story.append(heading("10.3", "TRANSGENIC ANIMALS", 1))
story.append(keyterm(
    "<b>Transgenic animals</b> are animals that have had their DNA manipulated to <b>possess "
    "and express an extra (foreign) gene</b>. <b>Transgenic rats, rabbits, pigs, sheep, cows "
    "and fish</b> have been produced, although <b>over 95 per cent</b> of all existing "
    "transgenic animals are <b>mice</b>."))
story.append(Paragraph(
    "Transgenic animals are produced for <b>five</b> common reasons:", STYLES["Body"]))
story.append(data_table([
    ["Reason", "What it is used for"],
    ["(i) <b>Normal physiology and development</b>",
     "To study <b>how genes are regulated</b> and how they affect normal body functions and "
     "development, e.g., the study of complex factors involved in growth such as <b>insulin-like "
     "growth factor</b>. Genes from other species that alter this factor are introduced, and the "
     "biological effects reveal the factor's role in the body."],
    ["(ii) <b>Study of disease</b>",
     "To understand how genes contribute to disease, by serving as <b>models for human "
     "diseases</b>. Transgenic models exist for <b>cancer, cystic fibrosis, rheumatoid arthritis "
     "and Alzheimer's</b>."],
    ["(iii) <b>Biological products</b>",
     "To produce useful, otherwise expensive, biological products by introducing the DNA (gene) "
     "that codes for it, e.g., human protein <b>alpha-1-antitrypsin</b> used to treat "
     "<b>emphysema</b>; similar attempts target <b>phenylketonuria (PKU)</b> and <b>cystic "
     "fibrosis</b>. In <b>1997</b>, the first transgenic cow, <b>Rosie</b>, produced "
     "human-protein-enriched milk (<b>2.4 grams per litre</b>) containing human "
     "<b>alpha-lactalbumin</b> -- nutritionally more balanced for human babies than natural "
     "cow milk."],
    ["(iv) <b>Vaccine safety</b>",
     "<b>Transgenic mice</b> are being developed to test the safety of vaccines before use on "
     "humans -- e.g., testing the <b>polio vaccine</b>; if reliable, they could replace the use "
     "of <b>monkeys</b> for testing safety of vaccine batches."],
    ["(v) <b>Chemical safety testing</b>",
     "Also called <b>toxicity / safety testing</b>. Transgenic animals carrying genes that make "
     "them <b>more sensitive to toxic substances</b> are exposed to those substances and the "
     "effects studied, allowing results in <b>less time</b>."],
], col_widths=[1.3, 4.3]))
story.append(Spacer(1, 4))

# =============================== 10.4 ETHICAL ISSUES ================================
# ---- 10.4 Ethical Issues: regulation and GEAC (F115-F118) ----
story.append(heading("10.4", "ETHICAL ISSUES", 1))
story.append(Paragraph(
    "The <b>manipulation of living organisms</b> by the human race cannot go on any further "
    "<b>without regulation</b>. Some <b>ethical standards</b> are required to evaluate the "
    "morality of all human activities that might help or harm living organisms. Beyond morality, "
    "the <b>biological significance</b> also matters: genetic modification of organisms can have "
    "<b>unpredictable results</b> when such organisms are introduced into the ecosystem.",
    STYLES["Body"]))
story.append(keyterm(
    "Therefore, the Indian Government has set up organisations such as <b>GEAC (Genetic "
    "Engineering Approval Committee)</b>, which makes decisions regarding the <b>validity of GM "
    "research</b> and the <b>safety of introducing GM organisms</b> for public services."))
story.append(Spacer(1, 3))

# ---- 10.4 Biopiracy, patents and Basmati (F119-F134) ----
story.append(heading("10.4", "Patents and biopiracy", 2))
story.append(Paragraph(
    "The modification / usage of living organisms for public services (as food and medicine "
    "sources, for example) has also created problems with <b>patents</b> granted for the same. "
    "There is growing public anger that certain companies are being granted patents for products "
    "and technologies that make use of <b>genetic materials, plants and other biological "
    "resources</b> that have long been <b>identified, developed and used by farmers and "
    "indigenous people</b> of a specific region / country.", STYLES["Body"]))
story.append(Paragraph(
    "The case of <b>rice</b> illustrates this. Rice is an important food grain whose presence "
    "goes back <b>thousands of years</b> in Asia's agricultural history. There are an estimated "
    "<b>200,000 varieties of rice in India</b> alone -- one of the richest diversities in the "
    "world. <b>Basmati rice</b> is distinct for its unique aroma and flavour, and <b>27 "
    "documented varieties of Basmati</b> are grown in India, with references in <b>ancient "
    "texts, folklore and poetry</b>.", STYLES["Body"]))
story.append(Paragraph(
    "In <b>1997</b>, an <b>American company got patent rights on Basmati rice</b> through the "
    "<b>US Patent and Trademark Office</b>, allowing it to sell a 'new' variety of Basmati in "
    "the US and abroad. This 'new' variety had actually been <b>derived from Indian farmers' "
    "varieties</b>: Indian Basmati was crossed with <b>semi-dwarf varieties</b> and claimed as "
    "an invention or novelty. The patent <b>extends to functional equivalents</b>, implying that "
    "other people selling Basmati rice could be <b>restricted</b> by the patent. Several attempts "
    "have also been made to patent uses, products and processes based on <b>Indian traditional "
    "herbal medicines</b>, e.g., <b>turmeric</b> and <b>neem</b>.", STYLES["Body"]))
story.append(keyterm(
    "<b>Biopiracy</b> is the term used to refer to the <b>use of bio-resources by multinational "
    "companies and other organisations without proper authorisation</b> from the countries and "
    "people concerned, and <b>without compensatory payment</b>."))
story.append(Paragraph(
    "Most <b>industrialised nations are rich financially but poor in biodiversity and traditional "
    "knowledge</b>. In contrast, the <b>developing and underdeveloped world is rich in "
    "biodiversity and traditional knowledge</b> related to bio-resources -- knowledge that can be "
    "exploited to develop modern applications and to <b>save time, effort and expenditure</b> "
    "during commercialisation.", STYLES["Body"]))
story.append(Paragraph(
    "There has been growing realisation of the <b>injustice, inadequate compensation, and benefit "
    "sharing</b> between developed and developing countries. Therefore, some nations are "
    "developing laws to <b>prevent such unauthorised exploitation</b>. The <b>Indian "
    "Parliament</b> has recently cleared the <b>second amendment of the Indian Patents Bill</b>, "
    "which takes such issues into consideration, including patent terms of emergency provisions, "
    "research, and development initiatives.", STYLES["Body"]))
story.append(Spacer(1, 5))

# =============================== QUICK RECAP ========================================
# ---- Quick Recap (denser rewrite of the chapter summary, Rule 3) ----
story.append(heading("QR", "QUICK RECAP", 1))
story.append(Paragraph(
    "&bull; Biotechnology has given humans several useful products by using <b>microbes, plants, "
    "animals and their metabolic machinery</b>.", STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; <b>Tissue culture</b> and <b>somatic hybridisation</b> offer vast potential for "
    "manipulating plants <i>in vitro</i> to produce new varieties (totipotency, "
    "micro-propagation, somaclones, virus-free plants, pomato).", STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; <b>Recombinant DNA technology</b> makes it possible to engineer microbes, plants and "
    "animals with <b>novel capabilities</b>. <b>GMOs</b> are made by non-natural transfer of one "
    "or more genes between organisms.", STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; <b>GM plants</b> increase crop yields, reduce post-harvest losses, make crops more "
    "stress-tolerant, improve nutrition (golden rice) and reduce pesticide use (Bt cotton, "
    "RNAi-based nematode resistance).", STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; Recombinant therapeutics are <b>identical to human proteins</b>, so they avoid "
    "unwanted immune responses and infection risk. <b>Human insulin</b> is made in bacteria yet "
    "is structurally identical to the natural molecule.", STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; <b>Gene therapy</b> inserts genes into an individual's cells / tissues to treat "
    "(especially hereditary) disease -- replacing a defective allele or using gene targeting; "
    "<b>viruses are used as vectors</b>. The first case (1990) treated <b>ADA deficiency</b>.",
    STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; <b>PCR, radioactive probes and ELISA</b> allow early molecular diagnosis. "
    "<b>Transgenic animals</b> (over 95% mice) model human disease and make biological products.",
    STYLES["Bullet1"]))
story.append(Paragraph(
    "&bull; The manipulation of microbes, plants and animals raises serious <b>ethical "
    "questions</b>; <b>GEAC</b> regulates GM research in India, and <b>biopiracy</b> / patent "
    "issues (Basmati, turmeric, neem) drive new protective laws.", STYLES["Bullet1"]))
story.append(Spacer(1, 5))

# =============================== EXERCISE-GAP APPENDIX ==============================
# ---- Terms used in the exercises (Rule 2 gaps; chapter facts only) ----
story.append(heading("EX", "TERMS USED IN THE EXERCISES", 1))
story.append(Paragraph(
    "A few end-of-chapter questions lean on a term or task the body states only indirectly. Each "
    "is closed below <b>using only facts from this chapter</b>.", STYLES["Body"]))
story.append(data_table([
    ["Exercise term / task", "Explanation from this chapter"],
    # [VERIFICATION FIX - Pass 3(b)] The frozen inventory's exercise-gap table promised the
    # appendix would "cross-link" the advantages and disadvantages of GM crops for Q6, but no
    # such row was ever written. The facts are all in the body, just never assembled as the
    # two-sided comparison the question asks for; gathered here, chapter facts only.
    ["<b>Advantages vs disadvantages of GM crops</b> (Q6)",
     "<b>Advantages</b> (10.1): tolerance to <b>cold, drought, salt and heat</b>; reduced "
     "reliance on <b>chemical pesticides</b>; less <b>post-harvest loss</b>; more efficient "
     "<b>mineral use</b>, sparing soil fertility; better <b>nutrition</b> (golden rice); plus "
     "tailor-made <b>starches, fuels and pharmaceuticals</b>. <b>Disadvantages</b> (10.4): "
     "genetic modification can have <b>unpredictable results when such organisms are introduced "
     "into the ecosystem</b>, which is why <b>GEAC</b> clearance is required; and the "
     "<b>patenting</b> of GM and bio-resource material raises <b>biopiracy</b> problems, since a "
     "patent extending to <b>functional equivalents</b> can restrict others (the Basmati case)."],
    ["<b>Transgenic bacteria</b> (Q5)",
     "The chapter defines transgenic <i>animals</i>; by the same idea, a <b>transgenic "
     "bacterium</b> is a bacterium carrying an introduced <b>foreign gene</b>. Example: the "
     "<b><i>E. coli</i></b> into which <b>Eli Lilly</b> introduced the human insulin <b>A- and "
     "B-chain DNA sequences</b> (1983) to make human insulin."],
    ["<b>Cry proteins</b> (Q7)",
     "The <b>toxic insecticidal proteins</b> that form the crystals of <b><i>Bacillus "
     "thuringiensis</i></b>. They are encoded by the <b><i>cry</i> gene family</b> (e.g., "
     "<b>cryIAc, cryIIAb</b> against cotton bollworms; <b>cryIAb</b> against corn borer). Man "
     "has cloned these genes into crops (<b>Bt cotton</b>) to create insect resistance."],
    ["<b>Cloning and expressing a human gene in <i>E. coli</i></b> (Q9)",
     "The route this chapter supplies is the <b>insulin</b> one: prepare DNA for the A and B "
     "chains, insert into <b><i>E. coli</i> plasmids</b>, produce each chain, then combine them "
     "by disulfide bonds. (The full general rDNA step sequence belongs to Chapter 9.)"],
    ["<b>Removing oil (hydrocarbon) from seeds</b> (Q10)",
     "The silencing tool the chapter provides is <b>RNAi</b>: introducing DNA that makes "
     "<b>sense and anti-sense RNA</b> forms a <b>dsRNA</b> that silences the target mRNA -- the "
     "same strategy used against the nematode -- pointing to how an oil-synthesis gene could be "
     "switched off."],
    ["<b>Proteases and nucleases in blood; oral protein drugs</b> (Q12, Q13)",
     "This is why <b>insulin cannot simply be swallowed</b>: as a <b>protein</b>, it would be "
     "<b>digested</b> in the gut, so it must be injected. Any orally active protein "
     "pharmaceutical faces this same <b>digestion problem</b>."],
], col_widths=[1.5, 4.3]))

if __name__ == "__main__":
    sys.exit(build_pdf(
        OUT_PDF, story,
        title="Class 12 Chapter 10 - Biotechnology and Its Applications (NEET notes)",
        subject="NEET Biology"))
