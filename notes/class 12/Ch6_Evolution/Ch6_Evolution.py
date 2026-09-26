"""
NCERT Class 12 Biology, Chapter 6 - Evolution
NEET replacement notes -> A4 print-ready PDF.  FIGURELESS EDITION (operator order).

Built under SUPREME COMMAND PROMPT.md v6, Pass 2 (GATE_2_PASS_2_BUILD_AND_LINT.md):
written linearly from the frozen 198-row inventory (Ch6_Evolution_inventory.md),
importing the repo-level frozen style module `neet_template.py` (v6 §0.6). No style,
geometry, colour or font is re-declared here.

FIGURELESS: by explicit operator order this chapter embeds NO figure. `figure()` is
bound below for API parity with every other chapter but is called exactly zero times.
Every caption row (F033, F060, F075, F087, F100, F104, F108, F128, F170, F178, F195)
and every in-figure label row (F034, F061, F076, F105, F109, F129, F171, F179 - 116
labels) is carried in running text or a data_table so check 6 finds every label.

Block markers `# ---- N.N ----` mark every NCERT section so a Pass 3 flag can be found
and fixed in one contiguous block. Inventory row IDs are named in the comments so any
fact can be traced back to its frozen row.

Pass 1 carry-overs actioned (inventory "Carry-overs for Pass 2"):
  1. All 116 in-figure labels carried in prose/tables (Miller apparatus in a short
     prose walk-through; Figs 6.6/6.7/6.9/6.10 as tables).
  2. GAP appendix: definition of *species* (exercise 3), labelled as an addition.
  3. SUMMARY-UNIQUE F198: "habitat fragmentation" stated explicitly in 6.7.
  4. Qualifiers verbatim: "accepted by majority", "may lie in between",
     "probably"/"about"/"around" on every date, "not a directed process ... stochastic",
     "unlike those of amphibians".
  5. Scientific names in italics.

Source: Chapter/class 12/Chapter 6 - Evolution.pdf (17 pp, page-image scan)
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# sys.path bootstrap: walk up until we find the repo-level neet_template.py (§0.6)
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
from reportlab.platypus import Paragraph, Spacer, KeepTogether  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch6_Evolution.pdf")


def figure(asset_name, caption_text, max_width_cm=15.9):
    """Chapter-local binding of the shared figure() helper (§0.6). Figureless edition:
    never called - kept so the script exposes the same API as every other chapter."""
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
# ---- Title block (§5 item 1) ----
# ======================================================================================
story += title_block("Evolution")

# ======================================================================================
# ---- Chapter opener (F001-F003) ----
# ======================================================================================
# F001 - chapter title + printed contents list
story.append(heading("Ch 6", "EVOLUTION - Chapter Opener", 1))
story.append(body(
    "<b>Chapter contents (as printed on the opener page):</b> 6.1 Origin of Life; 6.2 Evolution "
    "of Life Forms - A Theory; 6.3 What are the Evidences for Evolution?; 6.4 What is Adaptive "
    "Radiation?; 6.5 Biological Evolution; 6.6 Mechanism of Evolution; 6.7 Hardy-Weinberg "
    "Principle; 6.8 A Brief Account of Evolution; 6.9 Origin and Evolution of Man."))
# F002 (opener)
story.append(body(
    "<b>Evolutionary Biology</b> is the study of <b>history of life forms on earth</b>."))
# F003
story.append(body(
    "Flora and fauna on earth have changed over millions of years. To understand these changes "
    "we must understand the context of <b>origin of life</b>, i.e., the <b>evolution of earth, of "
    "stars and indeed of the universe itself</b>. This chapter is therefore the story of origin of "
    "life and <b>evolution of life forms or biodiversity</b> on planet earth, told in the context "
    "of evolution of earth and against the background of evolution of the universe itself."))

# ======================================================================================
# ---- 6.1 Origin of Life (F004-F016) ----
# ======================================================================================
story.append(heading("6.1", "ORIGIN OF LIFE", 1))
# F005 (opener), F006
story.append(body(
    "When we look at stars on a clear night sky we are, in a way, <b>looking back in time</b>. "
    "<b>Stellar distances are measured in light years.</b> The light we see today started its "
    "journey millions of years back from objects trillions of kilometres away - so when we see "
    "stars we apparently are <b>peeping into the past</b>."))
# F007, F008, F009
story.append(body(
    "The <b>origin of life</b> is considered a <b>unique event in the history of universe</b>. The "
    "universe is vast and <b>very old - almost 13.8 billion years old</b>. Huge <b>clusters of "
    "galaxies</b> comprise the universe; <b>galaxies contain stars and clouds of gas and dust</b>. "
    "Considering the size of universe, the <b>earth is indeed a speck</b> - almost only a speck."))
# F010, F011, F012, F013, F014, F015 - converted to a process flow
story.append(body(
    "The <b>Big Bang theory</b> attempts to explain the <b>origin of universe</b>. The sequence "
    "from that event to the first oceans on earth runs as follows:"))
story.append(process_flow([
    "<b>Big Bang</b> - a <b>singular huge explosion</b> unimaginable in physical terms. The "
    "universe <b>expanded</b> and hence the <b>temperature came down</b>.",
    "<b>Hydrogen and Helium</b> formed sometime later.",
    "The gases <b>condensed under gravitation</b> and formed the <b>galaxies</b> of the present "
    "day universe.",
    "In the <b>solar system of the milky way galaxy</b>, <b>earth</b> was supposed to have been "
    "formed about <b>4.5 billion years back</b>.",
    "There was <b>no atmosphere on early earth</b>. <b>Water vapour, methane, carbon dioxide and "
    "ammonia</b> released from the molten mass covered the surface.",
    "<b>UV rays</b> from the sun <b>broke up water into Hydrogen and Oxygen</b>, and the lighter "
    "<b>H<sub>2</sub> escaped</b>. Oxygen combined with ammonia and methane to form <b>water, "
    "CO<sub>2</sub></b> and others. The <b>ozone layer</b> was formed.",
    "As it cooled, the <b>water vapour fell as rain</b>, to fill all the depressions and <b>form "
    "oceans</b>.",
]))
# F016
story.append(gap())
story.append(body(
    "<b>Life appeared 500 million years after the formation of earth</b>, i.e., <b>almost four "
    "billion years back</b>."))

# ---- 6.1 Theories on the Origin of Life (F017) ----
story.append(heading("6.1", "Theories on the Origin of Life", 2))

# ---- 6.1 Panspermia (F018-F020) ----
story.append(heading("6.1", "Panspermia", 3))
# F019 (opener), F020
story.append(body(
    "Did life come from outer space? <b>Some scientists believe that it came from outside.</b> "
    "<b>Early Greek thinkers</b> thought units of life called <b>spores</b> were transferred to "
    "different planets including earth. <b>Panspermia</b> is still a favourite idea for some "
    "<b>astronomers</b>."))

# ---- 6.1 Spontaneous Generation (F021-F024) ----
story.append(heading("6.1", "Spontaneous Generation", 3))
# F022 (opener)
story.append(body(
    "For a long time it was also believed that life came out of <b>decaying and rotting matter "
    "like straw, mud</b>, etc. This was the <b>theory of spontaneous generation</b>."))
# F023, F024
story.append(body(
    "<b>Louis Pasteur</b>, by careful experimentation, demonstrated that <b>life comes only from "
    "pre-existing life</b>. He showed that in <b>pre-sterilised flasks</b>, life did <b>not</b> "
    "come from <b>killed yeast</b>, while in another flask <b>open to air</b>, new living "
    "organisms arose from killed yeast. <b>Spontaneous generation theory was dismissed once and "
    "for all.</b> However, this did <b>not</b> answer how the <b>first life form</b> came on "
    "earth."))

# ---- 6.1 Chemical Evolution (F025-F039, Fig 6.1 = F033/F034) ----
story.append(heading("6.1", "Chemical Evolution", 3))
# F026 (opener), F027
story.append(body(
    "<b>Oparin of Russia</b> and <b>Haldane of England</b> proposed that the first form of life "
    "could have come from <b>pre-existing non-living organic molecules</b> (for example <b>RNA and "
    "protein</b>), and that formation of life was <b>preceded by chemical evolution</b>."))
story.append(keyterm(
    "<b>Chemical evolution</b> - the <b>formation of diverse organic molecules from inorganic "
    "constituents</b>."))
# F028
story.append(body(
    "The conditions on earth then were <b>high temperature, volcanic storms</b>, and a <b>reducing "
    "atmosphere containing CH<sub>4</sub>, NH<sub>3</sub></b>, etc."))
# F029, F030, F031
story.append(body(
    "In <b>1953</b>, <b>S. L. Miller</b>, an <b>American scientist</b>, created similar conditions "
    "on a laboratory scale. He created <b>electric discharge</b> in a <b>closed flask</b> "
    "containing <b>CH<sub>4</sub>, H<sub>2</sub>, NH<sub>3</sub> and water vapour at 800 degrees "
    "C</b>, and observed the <b>formation of amino acids</b>. In similar experiments others "
    "observed formation of <b>sugars, nitrogen bases, pigment and fats</b>."))
# F033 (caption) + F034 (15 apparatus labels) - Miller's apparatus walked through in prose
story.append(body(
    "<b>Miller's experiment (NCERT Figure 6.1 - diagrammatic representation of Miller's "
    "experiment).</b> The apparatus works as a closed loop:"))
story.append(process_flow([
    "The closed apparatus is connected by an outlet marked <b>To vacuum pump</b>. "
    "<b>Boiling water</b> in the lower flask sends water vapour up into the upper flask, which "
    "holds the <b>Gases</b> - <b>CH<sub>4</sub></b>, <b>NH<sub>3</sub></b>, "
    "<b>H<sub>2</sub>O</b> and <b>H<sub>2</sub></b>.",
    "Two <b>Electrodes</b> in the gas flask deliver a <b>Spark discharge</b> (the electric "
    "discharge) through the gas mixture.",
    "The products pass through a <b>Condenser</b> cooled by circulating water (<b>Water in</b> at "
    "one end, <b>Water out</b> at the other), where they form <b>Water droplets</b>.",
    "The droplets collect as <b>Water containing organic compounds</b>, held as <b>Liquid water "
    "in trap</b> at the bottom of the loop; the loop leads back to the boiling flask.",
], cyclic=True))
story.append(gap())
# F032
story.append(body(
    "<b>Analysis of meteorite content</b> also revealed similar compounds, indicating that "
    "similar processes are occurring <b>elsewhere in space</b>. With this limited evidence, the "
    "first part of the conjectured story, i.e., <b>chemical evolution, was more or less "
    "accepted</b>."))
# F035, F036, F037
story.append(body(
    "We have <b>no idea</b> about how the <b>first self-replicating metabolic capsule of life</b> "
    "arose. The <b>first non-cellular forms of life</b> could have originated <b>3 billion years "
    "back</b>. They would have been <b>giant molecules</b>, such as <b>RNA, protein, "
    "polysaccharides</b>, etc. These capsules reproduced their molecules perhaps."))
# F038, F039
story.append(body(
    "The <b>first cellular form of life</b> did not possibly originate till about <b>2000 million "
    "years ago</b>; these were probably <b>single-cells</b>. <b>All life forms were in water "
    "environment only.</b> This version of a <b>biogenesis</b>, i.e., that the first form of life "
    "arose slowly through evolutionary forces from non-living molecules, is <b>accepted by "
    "majority</b>."))

# ======================================================================================
# ---- 6.2 Evolution of Life Forms - A Theory (F040-F051) ----
# ======================================================================================
story.append(heading("6.2", "EVOLUTION OF LIFE FORMS - A THEORY", 1))
# F041 (opener), F042
story.append(body(
    "Conventional religious literature tells us about the <b>theory of special creation</b>. "
    "This theory has <b>three connotations</b>:"))
story.append(b1(
    "<b>One</b> - all living organisms (species or types) that we see today were <b>created as "
    "such</b>."))
story.append(b1(
    "<b>Two</b> - the <b>diversity was always the same</b> since creation and will be the same in "
    "future also."))
story.append(b1("<b>Three</b> - <b>earth is about 4000 years old</b>."))
story.append(body(
    "All these ideas were <b>strongly challenged during the nineteenth century</b>."))
# F043, F044
story.append(body(
    "Based on observations made during a sea voyage in a sail ship called <b>H.M.S. Beagle</b> "
    "round the world, <b>Charles Darwin</b> concluded that existing living forms <b>share "
    "similarities to varying degrees</b> not only among themselves but also with life forms that "
    "existed <b>millions of years ago</b>. Many such life forms <b>do not exist any more</b>: "
    "there had been <b>extinctions</b> of different life forms in the years gone by, just as new "
    "forms of life arose at different periods of the history of earth. There has been "
    "<b>gradual evolution of life forms</b>."))
# F045, F046, F047
story.append(body(
    "<b>Any population has built-in variation in characteristics.</b> Those characteristics which "
    "enable some to <b>survive better in natural conditions</b> (such as <b>climate, food and "
    "physical factors</b>) would <b>outbreed</b> others that are less endowed to survive under "
    "such natural conditions."))
story.append(keyterm(
    "<b>Fitness</b> of the individual or population - according to Darwin, it refers "
    "<b>ultimately and only to reproductive fitness</b>."))
# F048
story.append(keyterm(
    "<b>Natural selection</b> - those who are <b>better fit</b> in an environment <b>leave more "
    "progeny</b> than others; these therefore survive more and are <b>selected by nature</b>. "
    "Darwin called it natural selection and implied it as a <b>mechanism of evolution</b>."))
# F049
story.append(body(
    "<b>Alfred Wallace</b>, a naturalist who worked in the <b>Malay Archipelago</b>, had also "
    "come to <b>similar conclusions around the same time</b>."))
# F050, F051
story.append(body(
    "In due course of time, it became apparent that <b>all the existing life forms share "
    "similarities and share common ancestors</b>. These ancestors were present at different "
    "periods in the history of earth - <b>epochs, periods and eras</b>. The <b>geological history "
    "of earth closely correlates with the biological history of earth</b>. A common conclusion "
    "is that earth is very old - <b>not thousands of years</b> as was thought earlier <b>but "
    "billions of years old</b>."))

# ======================================================================================
# ---- 6.3 What are the Evidences for Evolution? (F052-F095) ----
# ======================================================================================
story.append(heading("6.3", "WHAT ARE THE EVIDENCES FOR EVOLUTION?", 1))
# F053 (opener)
story.append(body(
    "Evidence that evolution of life forms has indeed taken place on earth has come from "
    "<b>many quarters</b>."))

# ---- 6.3 Paleontological Evidence (F054-F061, Fig 6.2) ----
story.append(heading("6.3", "Paleontological Evidence", 2))
# F055 (opener), F056, F057, F058
story.append(body(
    "<b>Fossils</b> are <b>remains of hard parts of life-forms found in rocks</b>. Rocks form "
    "<b>sediments</b>, and a cross-section of earth's crust indicates the arrangement of sediments "
    "<b>one over the other</b> during the long history of earth. <b>Different-aged rock "
    "sediments contain fossils of different life-forms</b>, who probably died during the "
    "formation of the particular sediment. Some of them appear similar to modern organisms; they "
    "represent <b>extinct organisms</b> (for example <b>dinosaurs</b>)."))
story.append(body(
    "A study of fossils in different sedimentary layers indicates the <b>geological period</b> in "
    "which they existed. The study showed that life-forms varied over time and that <b>certain "
    "life forms are restricted to certain geological time-spans</b>. All this is called "
    "<b>paleontological evidence</b>."))
# F059
story.append(body(
    "<i>Recall:</i> how are the ages of fossils calculated? Recollect the method of "
    "<b>radioactive-dating</b> and the principles behind the procedure."))
# F060 (caption) + F061 (7 labels)
story.append(body(
    "<b>A family tree of dinosaurs</b> and their living modern day counterpart organisms "
    "<b>like crocodiles and birds</b> (NCERT Figure 6.2) places these forms on one tree: "
    "<b>Triceratops</b>, <b>Tyrannosaurus</b>, <b>Stegosaurus</b>, <b>Brachiosaurus</b> and "
    "<b>Pteranodon</b>, alongside the <b>Crocodilian</b> line (today's crocodiles) and "
    "<b>Archaeopteryx</b> on the line leading to birds."))

# ---- 6.3 Embryological Support (F062-F065) ----
story.append(heading("6.3", "Embryological Support", 2))
# F063 (opener), F064, F065
story.append(body(
    "<b>Embryological support</b> for evolution was proposed by <b>Ernst Heckel</b>, based upon "
    "the observation of certain features during <b>embryonic stage common to all vertebrates</b> "
    "that are <b>absent in adult</b>. For example, the embryos of all vertebrates <b>including "
    "human</b> develop a row of <b>vestigial gill slit just behind the head</b>, but it is a "
    "functional organ <b>only in fish</b> and not found in any other adult vertebrates."))
story.append(body(
    "However, this proposal was <b>disapproved</b> on careful study performed by <b>Karl Ernst von "
    "Baer</b>. He noted that <b>embryos never pass through the adult stages of other "
    "animals</b>."))

# ---- 6.3 Comparative Anatomy and Morphology (F066-F084, Fig 6.3) ----
story.append(heading("6.3", "Comparative Anatomy and Morphology", 2, has_table=True))
# F067 (opener), F068
story.append(body(
    "Comparative anatomy and morphology shows <b>similarities and differences</b> among organisms "
    "of today and those that existed years ago. Such similarities can be interpreted to "
    "understand <b>whether common ancestors were shared or not</b>."))
# F069, F070, F071, F072, F073
story.append(body(
    "For example, <b>whales, bats, cheetah and human</b> (all mammals) share similarities in the "
    "<b>pattern of bones of forelimbs</b>. Though these forelimbs perform <b>different "
    "functions</b> in these animals, they have <b>similar anatomical structure</b> - all of them "
    "have <b>humerus, radius, ulna, carpals, metacarpals and phalanges</b>."))
story.append(keyterm(
    "<b>Divergent evolution / homology</b> - the <b>same structure developed along different "
    "directions due to adaptations to different needs</b>. These structures are "
    "<b>homologous</b>; <b>homology indicates common ancestry</b> (it is accounted for by the idea "
    "of <b>branching descent</b>). Other examples: <b>vertebrate hearts or brains</b>; in plants, "
    "the <b>thorn and tendrils</b> of <i>Bougainvillea</i> and <i>Cucurbita</i>."))
# F075 (caption) + F076 (8 labels)
story.append(body(
    "<b>Example of homologous organs in (a) Plants and (b) Animals</b> (NCERT Figure 6.3): in "
    "plants, the <b>Thorn</b> of <b>Bougainvillea</b> and the <b>Tendril</b> of "
    "<b>Cucurbita</b>; in animals, the forelimbs of <b>Man</b>, <b>Cheetah</b>, <b>Whale</b> and "
    "<b>Bat</b>."))
# F074, F077, F078, F079, F080, F081
story.append(body(
    "<b>Homology is based on divergent evolution whereas analogy refers to a situation exactly "
    "opposite.</b> <b>Wings of butterfly and of birds</b> look alike; they are <b>not anatomically "
    "similar structures</b> though they perform <b>similar functions</b>."))
story.append(body(
    "Thus <b>analogous structures</b> are a result of <b>convergent evolution</b> - <b>different "
    "structures evolving for the same function and hence having similarity</b>. It is the "
    "<b>similar habitat</b> that has resulted in selection of similar adaptive features in "
    "different groups of organisms, but toward the same function."))
story.append(data_table([
    ["Feature", "Homologous organs", "Analogous organs"],
    ["Type of evolution", "<b>Divergent evolution</b>", "<b>Convergent evolution</b>"],
    ["Anatomy", "<b>Similar anatomical structure</b>",
     "<b>Not anatomically similar</b> structures"],
    ["Function", "<b>Different functions</b> (different needs)", "<b>Similar functions</b>"],
    ["What it indicates", "<b>Common ancestry</b>",
     "Selection of similar adaptive features by a <b>similar habitat</b>"],
    ["Animal examples",
     "Forelimbs of <b>whales, bats, cheetah and human</b>; <b>vertebrate hearts or brains</b>",
     "<b>Wings of butterfly and of birds</b>; <b>eye of the octopus and of mammals</b>; "
     "<b>flippers of Penguins and Dolphins</b>"],
    ["Plant examples",
     "<b>Thorn</b> of <i>Bougainvillea</i> and <b>tendrils</b> of <i>Cucurbita</i>",
     "<b>Sweet potato</b> (a <b>root modification</b>) and <b>potato</b> (a <b>stem "
     "modification</b>)"],
], col_widths=[2.2, 4.6, 4.6]))
story.append(gap(6))
# F082
story.append(body(
    "Similarly, <b>similarities in proteins and genes</b> performing a given function among "
    "diverse organisms give clues to <b>common ancestry</b>. These <b>biochemical "
    "similarities</b> point to the same shared ancestry as <b>structural similarities</b> among "
    "diverse organisms."))
# F083, F084
story.append(body(
    "Man has bred selected plants and animals for <b>agriculture, horticulture, sport or "
    "security</b>, and has <b>domesticated many wild animals and crops</b>. This intensive "
    "breeding programme has created <b>breeds that differ from other breeds</b> (for example "
    "<b>dogs</b>) but still are of the <b>same group</b>. The argument: if within <b>hundreds of "
    "years</b> man could create new breeds, could not nature have done the same over <b>millions "
    "of years</b>?"))

# ---- 6.3 Natural selection in action - industrial melanism (F085-F095, Fig 6.4) ----
# F085, F086, F087 (caption), F088-F092
story.append(heading("6.3", "Moths before and after industrialisation", 3, has_table=True))
story.append(data_table([
    ["Collection", "Tree trunks", "Moth that survived", "Result"],
    ["<b>1850s</b> - before industrialisation set in",
     "Covered by thick growth of <b>almost white-coloured lichen</b>",
     "<b>White-winged moth</b>; dark-coloured moths were picked out by predators",
     "<b>More white-winged moths</b> on trees than dark-winged or <b>melanised</b> moths"],
    ["<b>1920</b> - after industrialisation, same area",
     "Became <b>dark due to industrial smoke and soots</b>",
     "<b>Dark-winged or melanised moth</b>; the white-winged moth did not survive due to "
     "predators",
     "<b>More dark-winged moths</b> - the <b>proportion was reversed</b>"],
], col_widths=[2.6, 3.0, 3.2, 3.2]))
story.append(gap(6))
story.append(body(
    "NCERT Figure 6.4 shows the <b>white-winged moth and dark-winged moth (melanised) on a tree "
    "trunk (a) in unpolluted area (b) in polluted area</b>: on the pale, lichen-covered trunk the "
    "dark moth stands out, while on the soot-darkened trunk the white moth stands out. The "
    "explanation is that <b>predators will spot a moth against a contrasting background</b>; "
    "moths that were able to <b>camouflage</b> themselves, i.e., <b>hide in the background</b>, "
    "survived. Supporting this, in <b>rural areas where industrialisation did not occur</b>, the "
    "<b>count of melanic moths was low</b>."))
story.append(body(
    "This showed that in a <b>mixed population</b>, those that can better adapt survive and "
    "increase in population size. Remember that <b>no variant is completely wiped out</b>."))
# F091
story.append(note(
    "<b>Lichens can be used as industrial pollution indicators</b> - they will <b>not grow in "
    "areas that are polluted</b>."))
story.append(gap(6))
# F093, F094, F095 - anthropogenic evolution
story.append(body(
    "Similarly, <b>excess use of herbicides, pesticides</b>, etc., has only resulted in "
    "<b>selection of resistant varieties</b> in a <b>much lesser time scale</b>. This is also true "
    "for <b>microbes against which we employ antibiotics</b> or drugs against eukaryotic "
    "organisms or cells. Hence, <b>resistant organisms or cells</b> are appearing in a time scale "
    "of <b>months or years and not centuries</b>. These are examples of <b>evolution by "
    "anthropogenic action</b>."))
story.append(body(
    "This also tells us that <b>evolution is not a directed process</b>, but is a <b>stochastic "
    "process</b> based on <b>chance events in nature</b> and <b>chance mutation</b> in the "
    "organisms."))

# ======================================================================================
# ---- 6.4 What is Adaptive Radiation? (F096-F109, Figs 6.5, 6.6, 6.7) ----
# ======================================================================================
story.append(heading("6.4", "WHAT IS ADAPTIVE RADIATION?", 1, has_table=True))
# F097 (opener), F098, F099, F100 (caption)
story.append(body(
    "During his journey <b>Darwin went to Galapagos Islands</b>. There he observed an amazing "
    "diversity of creatures. Of particular interest, small black birds later called "
    "<b>Darwin's Finches</b> amazed him: he realised that there were <b>many varieties of finches "
    "in the same island</b>. All the varieties, he conjectured, <b>evolved on the island "
    "itself</b>. From the original <b>seed-eating</b> features, many other forms with <b>altered "
    "beaks</b> arose, enabling them to become <b>insectivorous and vegetarian finches</b>. NCERT "
    "Figure 6.5 shows this <b>variety of beaks of finches that Darwin found in Galapagos "
    "Island</b> - four beak forms side by side."))
# F101, F102
story.append(keyterm(
    "<b>Adaptive radiation</b> - the process of evolution of <b>different species in a given "
    "geographical area</b> starting from a point and literally <b>radiating to other areas of "
    "geography, or habitats</b>. <b>Darwin's finches</b> represent one of the best examples."))
# F103, F104 (caption), F105 (12 labels)
story.append(body(
    "Another example is <b>Australian marsupials</b>: a number of marsupials, each different from "
    "the other, evolved from an <b>ancestral stock</b>, but <b>all within the Australian island "
    "continent</b>. NCERT Figure 6.6 (<b>adaptive radiation of marsupials of Australia</b>) "
    "shows this <b>Marsupial radiation</b> fanning out across <b>Australia</b> from one "
    "ancestral stock into these marsupials, each different from the other:"))
story.append(b1(
    "<b>Sugar glider</b>, <b>Tasmanian wolf</b>, <b>Tiger cat</b>, <b>Marsupial mole</b>, "
    "<b>Banded anteater</b>, <b>Koala</b>, <b>Marsupial rat</b>, <b>Bandicoot</b>, "
    "<b>Wombat</b> and <b>Kangaroo</b>."))
story.append(gap(4))
# F106, F107, F108 (caption), F109 (16 labels)
story.append(body(
    "When <b>more than one adaptive radiation</b> appeared to have occurred in an <b>isolated "
    "geographical area</b> (representing different habitats), one can call this <b>convergent "
    "evolution</b>. <b>Placental mammals in Australia</b> also exhibit adaptive radiation in "
    "evolving into varieties of such placental mammals, <b>each of which appears to be similar "
    "to a corresponding marsupial</b> - for example <b>placental wolf and Tasmanian "
    "wolf-marsupial</b>. NCERT Figure 6.7 (<b>convergent evolution of Australian marsupials and "
    "placental mammals</b>) pairs them as follows:"))
story.append(data_table([
    ["Placental mammals", "Australian marsupials"],
    ["<b>Mole</b>", "<b>Marsupial mole</b>"],
    ["<b>Anteater</b>", "<b>Numbat (anteater)</b>"],
    ["<b>Mouse</b>", "<b>Marsupial mouse</b>"],
    ["<b>Lemur</b>", "<b>Spotted cuscus</b>"],
    ["<b>Flying squirrel</b>", "<b>Flying phalanger</b>"],
    ["<b>Bobcat</b>", "<b>Tasmanian tiger cat</b>"],
    ["<b>Wolf</b>", "<b>Tasmanian wolf</b>"],
], col_widths=[1, 1]))
story.append(gap(8))

# ======================================================================================
# ---- 6.5 Biological Evolution (F110-F129, Fig 6.8) ----
# ======================================================================================
story.append(heading("6.5", "BIOLOGICAL EVOLUTION", 1))
# F111 (opener), F112, F113
story.append(body(
    "<b>Evolution by natural selection</b>, in a true sense, would have started when <b>cellular "
    "forms of life with differences in metabolic capability</b> originated on earth. The "
    "<b>essence of Darwinian theory</b> about evolution is <b>natural selection</b>. The <b>rate "
    "of appearance of new forms is linked to the life cycle or the life span</b>."))
# F114, F115, F116
story.append(body(
    "<b>Microbes that divide fast</b> have the ability to multiply and become millions of "
    "individuals <b>within hours</b>. A colony of bacteria (say <b>A</b>) growing on a given "
    "medium has built-in variation in terms of ability to utilise a feed component. A change in "
    "the medium composition would bring out only that part of the population (say <b>B</b>) that "
    "can survive under the new conditions. In due course of time this <b>variant population "
    "outgrows the others and appears as new species</b>. This would happen <b>within days</b>. "
    "For the same thing to happen in a <b>fish or fowl</b> would take <b>millions of years</b>, as "
    "life spans of these animals are in years. We say that the <b>fitness of B is better than "
    "that of A</b> under the new conditions. <b>Nature selects for fitness.</b>"))
# F117, F118, F119
story.append(body(
    "The so-called fitness is based on characteristics which are <b>inherited</b>; hence there "
    "must be a <b>genetic basis</b> for getting selected and to evolve. In other words, "
    "<b>adaptive ability is inherited</b>; it has a genetic basis. <b>Fitness is the end result "
    "of the ability to adapt and get selected by nature.</b>"))
story.append(keyterm(
    "<b>Branching descent and natural selection</b> are the <b>two key concepts of Darwinian "
    "Theory of Evolution</b>."))
# F120, F121
story.append(body(
    "Even before Darwin, a French naturalist <b>Lamarck</b> had said that evolution of life forms "
    "had occurred but <b>driven by use and disuse of organs</b>. His example was the "
    "<b>giraffe</b>: in an attempt to forage leaves on tall trees, giraffes had to adapt by "
    "<b>elongation of their necks</b>; as they passed on this <b>acquired character</b> of "
    "elongated neck to succeeding generations, giraffes slowly, over the years, came to acquire "
    "long necks. <b>Nobody believes this conjecture any more.</b>"))
# F122, F123
story.append(body(
    "<b>Is evolution a process or the result of a process?</b> The world we see, inanimate and "
    "animate, is only the <b>success stories of evolution</b>. When we describe the story of this "
    "world, we describe evolution as a <b>process</b>; when we describe the story of life on "
    "earth, we treat evolution as a <b>consequence of a process called natural selection</b>. We "
    "are still <b>not very clear</b> whether to regard evolution and natural selection as "
    "processes or end result of unknown processes."))
# F124, F125, F126, F127 - Darwin's reasoning as a process flow
story.append(body(
    "It is possible that the work of <b>Thomas Malthus on populations</b> influenced Darwin. "
    "Natural selection is based on certain observations which are factual; Darwin's reasoning "
    "runs step by step:"))
story.append(process_flow([
    "<b>Natural resources are limited.</b>",
    "<b>Populations are stable in size</b> except for <b>seasonal fluctuation</b>.",
    "<b>Members of a population vary in characteristics</b> - in fact <b>no two individuals are "
    "alike</b> - even though they look superficially similar.",
    "<b>Most variations are inherited.</b>",
    "Population size will <b>grow exponentially</b> if everybody reproduced maximally; yet real "
    "population sizes are limited. This means there had been <b>competition for resources</b>: "
    "only some survived and grew at the cost of others that could not flourish.",
    "Darwin's insight: <b>variations which are heritable</b> and which make <b>resource "
    "utilisation better for few</b> (adapted to habitat better) will enable <b>only those to "
    "reproduce and leave more progeny</b>.",
    "Over many generations the <b>survivors leave more progeny</b>, there is a <b>change in "
    "population characteristic</b>, and hence <b>new forms appear to arise</b>.",
]))
story.append(gap())
# F128 (caption) + F129 (6 labels) - the three modes are defined in 6.7 (F157); graph read here
story.append(body(
    "<b>Operation of natural selection on different traits</b> (NCERT Figure 6.8 - "
    "(a) <b>Stabilising</b>, (b) <b>Directional</b> and (c) <b>Disruptive</b>). Each panel plots "
    "the <b>Number of individuals with phenotype</b> against the phenotype, with the shaded part "
    "marking the <b>Phenotypes favoured by natural selection</b>:"))
story.append(data_table([
    ["Mode of selection", "Which phenotypes are favoured", "Change in the curve"],
    ["<b>(a) Stabilising</b>", "<b>Medium-sized individuals are favoured</b>",
     "<b>Peak gets higher and narrower</b>"],
    ["<b>(b) Directional</b>", "Individuals at <b>one end</b> of the distribution",
     "<b>Peak shifts in one direction</b>"],
    ["<b>(c) Disruptive</b>", "Individuals at <b>both ends</b> (peripheral values)",
     "<b>Two peaks form</b>"],
], col_widths=[2.4, 4.4, 4.2]))
story.append(gap(8))

# ======================================================================================
# ---- 6.6 Mechanism of Evolution (F130-F137) ----
# ======================================================================================
story.append(heading("6.6", "MECHANISM OF EVOLUTION", 1, has_table=True))
# F131 (opener), F132
story.append(body(
    "<b>What is the origin of this variation and how does speciation occur?</b> Even though "
    "<b>Mendel</b> had talked of <b>inheritable factors influencing phenotype</b>, Darwin either "
    "<b>ignored these observations or kept silence</b>."))
# F133, F134
story.append(body(
    "In the <b>first decade of twentieth century</b>, <b>Hugo de Vries</b>, based on his work on "
    "<b>evening primrose</b>, brought forth the idea of <b>mutations</b> - <b>large difference "
    "arising suddenly in a population</b>. He believed that it is <b>mutation which causes "
    "evolution</b>, and not the minor variations (heritable) that Darwin talked about."))
# F135, F136
story.append(data_table([
    ["Point", "Darwin", "Hugo de Vries"],
    ["Cause of evolution", "Minor, heritable <b>variations</b>", "<b>Mutation</b>"],
    ["Nature of the change", "Variations are <b>small and directional</b>",
     "Mutations are <b>random and directionless</b>"],
    ["Pace", "Evolution was <b>gradual</b>",
     "Mutation caused speciation in one step - <b>saltation</b> (single-step large mutation)"],
], col_widths=[2.4, 4.3, 4.3]))
story.append(gap(6))
# F137
story.append(body(
    "Studies in <b>population genetics</b>, later, brought out some clarity."))

# ======================================================================================
# ---- 6.7 Hardy-Weinberg Principle (F138-F157, F198) ----
# ======================================================================================
story.append(heading("6.7", "HARDY-WEINBERG PRINCIPLE", 1))
# F139 (opener), F140, F141, F142
story.append(body(
    "In a given population one can find out the <b>frequency of occurrence of alleles of a gene "
    "or a locus</b>. This frequency is supposed to <b>remain fixed</b> and even remain the same "
    "through generations. The <b>Hardy-Weinberg principle</b> stated it using algebraic "
    "equations: <b>allele frequencies in a population are stable and are constant from "
    "generation to generation</b>."))
story.append(body(
    "The <b>gene pool</b> - the total genes and their alleles in a population - <b>remains a "
    "constant</b>. This is called <b>genetic equilibrium</b>."))
# F143, F144, F145, F146, F147
story.append(body(
    "<b>Sum total of all the allelic frequencies is 1.</b> Individual frequencies can be named "
    "<b>p, q</b>, etc. In a <b>diploid</b>, <b>p and q represent the frequency of allele A and "
    "allele a</b>. The frequency of <b>AA</b> individuals in a population is simply "
    "<b>p<super>2</super></b> - the probability that an allele A with frequency p appears on "
    "<b>both</b> the chromosomes of a diploid individual is the product of the probabilities, "
    "i.e., <b>p x p = p<super>2</super></b>. Similarly the frequency of <b>aa</b> is "
    "<b>q<super>2</super></b>, and that of <b>Aa</b> is <b>2pq</b>. Hence:"))
story.append(Paragraph(
    "<b>p<super>2</super> + 2pq + q<super>2</super> = 1</b>", STYLES["Caption"]))
story.append(body(
    "This is a <b>binomial expansion of (p + q)<super>2</super></b>."))
# F148
story.append(body(
    "When the <b>frequency measured differs from expected values</b>, the difference (or "
    "direction) indicates the <b>extent of evolutionary change</b>. Disturbance in genetic "
    "(Hardy-Weinberg) equilibrium, i.e., <b>change of allele frequency</b> in a population, "
    "would then be interpreted as <b>resulting in evolution</b>."))
# F149-F156 - the five factors, as a table
story.append(KeepTogether([
    body("<b>Five factors</b> are known to affect Hardy-Weinberg equilibrium: <b>gene migration or "
         "gene flow, genetic drift, mutation, genetic recombination and natural selection</b>."),
    data_table([
        ["Factor", "How it changes allele frequency"],
        ["<b>Gene migration / gene flow</b>",
         "When a section of population <b>migrates</b> to another place and population, gene "
         "frequencies change in the <b>original as well as in the new population</b>: new genes "
         "or alleles are <b>added to the new population</b> and <b>lost from the old</b>. There "
         "would be a <b>gene flow</b> if this gene migration happens <b>multiple times</b>."],
        ["<b>Genetic drift</b>",
         "If the same change occurs <b>by chance</b>, it is called genetic drift. Sometimes the "
         "change in allele frequency is so different in the new sample of population that they "
         "become a <b>different species</b>; the original drifted population becomes "
         "<b>founders</b> and the effect is called <b>founder effect</b>."],
        ["<b>Mutation</b>",
         "Microbial experiments show that <b>pre-existing advantageous mutations</b> when "
         "selected will result in observation of <b>new phenotypes</b>; over few generations "
         "this would result in <b>speciation</b>."],
        ["<b>Genetic recombination</b>",
         "Variation due to <b>recombination during gametogenesis</b> changes the frequency of "
         "genes and alleles in future generations."],
        ["<b>Natural selection</b>",
         "A process in which <b>heritable variations enabling better survival</b> are enabled to "
         "<b>reproduce and leave greater number of progeny</b>."],
    ], col_widths=[2.6, 8.4]),
]))
story.append(gap(6))
story.append(keyterm(
    "<b>Genetic drift</b> - a change in allele frequency that occurs <b>by chance</b>; the "
    "drifted population that becomes a different species acts as <b>founders</b> "
    "(<b>founder effect</b>)."))
story.append(body(
    "Variation due to <b>mutation</b>, or variation due to <b>recombination during "
    "gametogenesis</b>, or due to <b>gene flow or genetic drift</b>, results in <b>changed "
    "frequency of genes and alleles</b> in future generation. Coupled to <b>enhanced "
    "reproductive success</b>, natural selection makes it look like a <b>different "
    "population</b>."))
# F198 - SUMMARY-UNIQUE fold (habitat fragmentation), stated as an explicit body sentence
story.append(keyterm(
    "<b>Habitat fragmentation</b> - other phenomena like <b>habitat fragmentation and genetic "
    "drift</b> may <b>accentuate these variations</b>, leading to <b>appearance of new "
    "species</b> and hence <b>evolution</b>."))
# F157 - three outcomes of natural selection (graph read in 6.5)
story.append(body(
    "Natural selection can lead to:"))
story.append(b1(
    "<b>Stabilisation</b> - <b>more individuals acquire mean character value</b>."))
story.append(b1(
    "<b>Directional change</b> - <b>more individuals acquire value other than the mean character "
    "value</b>."))
story.append(b1(
    "<b>Disruption</b> - <b>more individuals acquire peripheral character value at both ends of "
    "the distribution curve</b>."))
story.append(gap(4))
story.append(memory_aid(
    "<b>\"Stay, Drive, Split\"</b> - <b>S</b>tabilising keeps the middle (one peak, higher and "
    "narrower); <b>D</b>irectional drives the peak to one side; <b>D</b>isruptive splits the "
    "curve into two peaks."))
story.append(gap(8))

# ======================================================================================
# ---- 6.8 A Brief Account of Evolution (F158-F185, Figs 6.9, 6.10) ----
# ======================================================================================
story.append(heading("6.8", "A BRIEF ACCOUNT OF EVOLUTION", 1, has_table=True))
# F159 (opener), F160, F161
story.append(body(
    "About <b>2000 million years ago</b> (<b>mya</b>) the <b>first cellular forms of life</b> "
    "appeared on earth. The mechanism of how <b>non-cellular aggregates of giant "
    "macromolecules</b> could evolve into cells with <b>membranous envelop</b> is <b>not "
    "known</b>. Some of these cells had the ability to <b>release O<sub>2</sub></b>; the reaction "
    "could have been similar to the <b>light reaction in photosynthesis</b>, where water is split "
    "with the help of solar energy captured and channelised by appropriate <b>light harvesting "
    "pigments</b>."))
# F162-F169, F172-F177 - the timeline as a table (every qualifier kept)
story.append(data_table([
    ["When (as stated)", "Event"],
    ["about <b>2000 mya</b>", "<b>First cellular forms of life</b> appeared"],
    ["by the time of <b>500 mya</b>",
     "Slowly <b>single-celled organisms became multi-cellular</b> life forms; <b>invertebrates "
     "were formed and active</b>"],
    ["probably around <b>350 mya</b>", "<b>Jawless fish</b> evolved"],
    ["probably around <b>320 mya</b>", "<b>Sea weeds and few plants</b> existed"],
    ["about <b>350 mya</b>",
     "<b>Fish with stout and strong fins</b> could move on land and go back to water "
     "(<b>lobefins</b>)"],
    ["next <b>200 million years or so</b>",
     "<b>Reptiles of different shapes and sizes dominated</b> on earth"],
    ["probably <b>200 mya</b>",
     "Some land reptiles went back into water to evolve into <b>fish-like reptiles</b> "
     "(for example <i>Ichthyosaurs</i>)"],
    ["about <b>65 mya</b>", "The <b>dinosaurs suddenly disappeared</b> from the earth"],
], col_widths=[3.0, 8.0]))
story.append(gap(6))
story.append(body(
    "We are told that the <b>first organisms that invaded land were plants</b>; they were "
    "<b>widespread on land when animals invaded land</b>. In <b>1938</b>, a fish caught in "
    "<b>South Africa</b> happened to be a <i>Coelacanth</i>, which was thought to be "
    "<b>extinct</b>. These animals, called <b>lobefins</b>, evolved into the <b>first "
    "amphibians</b> that lived on both land and water. There are <b>no specimens</b> of these left "
    "with us; however, these were <b>ancestors of modern day frogs and salamanders</b>."))
story.append(body(
    "The <b>amphibians evolved into reptiles</b>. Reptiles lay <b>thick-shelled eggs which do not "
    "dry up in sun unlike those of amphibians</b>. Again we only see their modern day "
    "descendents - the <b>turtles, tortoises and crocodiles</b>. <b>Giant ferns "
    "(pteridophytes)</b> were present, but they all fell to form <b>coal deposits</b> slowly."))
story.append(body(
    "The land reptiles were, of course, the <b>dinosaurs</b>. The biggest of them, i.e., "
    "<i>Tyrannosaurus rex</i>, was <b>about 20 feet in height</b> and had huge fearsome "
    "<b>dagger-like teeth</b>. About 65 mya the dinosaurs suddenly disappeared - <b>we do not know "
    "the true reason</b>. Some say <b>climatic changes killed them</b>; some say <b>most of them "
    "evolved into birds</b>. <b>The truth may lie in between.</b> <b>Small-sized reptiles of that "
    "era still exist today.</b>"))
# F185 + F170 (caption) + F171 (31 labels) - plant forms through geological periods
story.append(body(
    "A rough sketch of the evolution of life forms and their times on a geological scale is "
    "given in NCERT Figures 6.9 and 6.10. <b>A sketch of the evolution of plant forms through "
    "geological periods</b> (Figure 6.9) is read as two tables - first the time scale, then the "
    "plant groups:"))
story.append(data_table([
    ["Era", "Periods (oldest first)"],
    ["<b>Paleozoic</b>", "<b>Silurian</b>, <b>Devonian</b>, <b>Carboniferous</b>, <b>Permian</b>"],
    ["<b>Mesozoic</b>", "<b>Triassic</b>, <b>Jurassic</b>, <b>Cretaceous</b>"],
    ["<b>Cenozoic</b>", "<b>Tertiary</b>, <b>Quaternary</b>"],
], col_widths=[2.4, 8.6]))
story.append(gap(6))
story.append(data_table([
    ["Part of the sketch", "Plant forms shown"],
    ["Base of the tree (ancestral stock)",
     "<b>chlorophyte ancestors</b>, then <b>tracheophyte ancestors</b>, <b>Rhynia-type "
     "plants</b> and <b>Psilophyton</b> (Silurian to Devonian)"],
    ["Early side lines",
     "<b>Bryophytes</b> (from the chlorophyte ancestors); <b>Zosterophyllum</b>, leading to "
     "<b>herbaceous lycopods</b> and <b>arborescent lycopods</b>"],
    ["Lines arising from Psilophyton",
     "<b>Sphenopsids (horsetails)</b>, <b>Ferns</b> and <b>Progymnosperms</b>"],
    ["Seed plants",
     "<b>Progymnosperms</b> give <b>seed ferns</b>; the seed-plant lines include <b>Conifers</b>, "
     "<b>Cycads</b>, <b>Ginkgos</b> and <b>Gnetales</b>"],
    ["Youngest line (Cretaceous onwards)",
     "<b>Angiosperms (flowering plants)</b>, branching into <b>Monocotyledons</b> and "
     "<b>Dicotyledons</b>"],
], col_widths=[3.2, 7.8]))
story.append(gap(6))
# F178 (caption) + F179 (21 labels) - vertebrates through geological periods
story.append(KeepTogether([
    body(
        "<b>Representative evolutionary history of vertebrates through geological periods</b> "
        "(Figure 6.10) runs from the <b>Carboniferous</b> through the <b>Permian</b>, "
        "<b>Triassic</b>, <b>Jurassic</b>, <b>Cretaceous</b> and <b>Tertiary</b> to the "
        "<b>Quaternary</b>. From <b>Early reptiles (extinct)</b> at the base, two lines split:"),
    data_table([
        ["Line", "Forms along the line", "Living descendants"],
        ["<b>Sauropsids</b>",
         "<b>Thecodonts (extinct)</b>, which gave rise to <b>Dinosaurs (extinct)</b>",
         "<b>Turtles</b>, <b>Lizards</b>, <b>Snakes</b>, <b>Tuataras</b>, <b>Crocodiles</b>, "
         "<b>Birds</b>"],
        ["<b>Synapsids</b>",
         "<b>Pelycosaurs (extinct)</b>, then <b>Therapsids (extinct)</b>",
         "<b>Mammals</b>"],
    ], col_widths=[2.2, 4.6, 4.2]),
]))
story.append(gap(6))
# F180, F181, F182, F183, F184
story.append(body(
    "The <b>first mammals were like shrews</b>; their fossils are <b>small sized</b>. Mammals "
    "were <b>viviparous</b> and protected their unborn young inside the mother's body. Mammals "
    "were <b>more intelligent in sensing and avoiding danger</b> at least. When reptiles came "
    "down, <b>mammals took over this earth</b>."))
story.append(body(
    "There were in <b>South America</b> mammals resembling <b>horse, hippopotamus, bear, "
    "rabbit</b>, etc. Due to <b>continental drift</b>, when South America joined North America, "
    "these animals were <b>overridden by North American fauna</b>. Due to the same continental "
    "drift, <b>pouched mammals of Australia survived</b> because of <b>lack of competition</b> "
    "from any other mammal. Some mammals <b>live wholly in water</b> - <b>whales, dolphins, seals "
    "and sea cows</b> are some examples."))
story.append(body(
    "<b>Evolution of horse, elephant, dog</b>, etc., are special stories of evolution. The "
    "<b>most successful story is the evolution of man</b> with <b>language skills and "
    "self-consciousness</b>."))

# ======================================================================================
# ---- 6.9 Origin and Evolution of Man (F186-F197, Fig 6.11) ----
# ======================================================================================
story.append(heading("6.9", "ORIGIN AND EVOLUTION OF MAN", 1, has_table=True))
# F187 (opener), F188, F189
story.append(body(
    "About <b>15 mya</b>, primates called <i>Dryopithecus</i> and <i>Ramapithecus</i> were "
    "existing. They were <b>hairy and walked like gorillas and chimpanzees</b>. "
    "<i>Ramapithecus</i> was <b>more man-like</b> while <i>Dryopithecus</i> was <b>more "
    "ape-like</b>. Few fossils of man-like bones have been discovered in <b>Ethiopia and "
    "Tanzania</b>; these revealed <b>hominid features</b>, leading to the belief that about "
    "<b>3-4 mya</b>, man-like primates walked in <b>eastern Africa</b>. They were probably "
    "<b>not taller than 4 feet</b> but <b>walked upright</b>."))
# F190-F194 - the hominid sequence as a table
story.append(data_table([
    ["When (as stated)", "Form", "Key features (NCERT)"],
    ["about <b>15 mya</b>", "<i>Dryopithecus</i> and <i>Ramapithecus</i>",
     "Hairy; walked like gorillas and chimpanzees; <i>Ramapithecus</i> more man-like, "
     "<i>Dryopithecus</i> more ape-like"],
    ["about <b>3-4 mya</b>", "Man-like primates of eastern Africa",
     "Probably not taller than <b>4 feet</b>; walked <b>upright</b>"],
    ["<b>Two mya</b>", "<b>Australopithecines</b>",
     "Probably lived in <b>East African grasslands</b>; hunted with <b>stone weapons</b> but "
     "essentially <b>ate fruit</b>"],
    ["-", "<i>Homo habilis</i> - the <b>first human-like being, the hominid</b>",
     "Brain capacities <b>between 650-800 cc</b>; probably <b>did not eat meat</b>"],
    ["about <b>1.5 mya</b>", "<i>Homo erectus</i>",
     "Fossils discovered in <b>Java in 1891</b>; <b>large brain around 900 cc</b>; probably "
     "<b>ate meat</b>"],
    ["<b>100,000-40,000</b> years back", "<b>Neanderthal man</b>",
     "Brain size <b>1400 cc</b>; lived in <b>Near East and central Asia</b>; used <b>hides</b> "
     "to protect their body and <b>buried their dead</b>"],
    ["ice age, <b>75,000-10,000</b> years ago", "Modern <i>Homo sapiens</i>",
     "<i>Homo sapiens</i> <b>arose in Africa</b>, moved across continents and developed into "
     "<b>distinct races</b>; modern <i>Homo sapiens</i> arose during this ice age"],
], col_widths=[2.6, 3.3, 5.6]))
story.append(gap(6))
# F195 (caption) - skull comparison, carried in words
story.append(body(
    "NCERT Figure 6.11 makes <b>a comparison of the skulls of adult modern human being, baby "
    "chimpanzee and adult chimpanzee</b>: <b>the skull of baby chimpanzee is more like adult "
    "human skull than adult chimpanzee skull</b>."))
# F196, F197
story.append(body(
    "<b>Pre-historic cave art</b> developed about <b>18,000 years ago</b>. One such cave painting "
    "by pre-historic humans can be seen at <b>Bhimbetka rock shelter in Raisen district of "
    "Madhya Pradesh</b>. <b>Agriculture came around 10,000 years back</b> and <b>human settlements "
    "started</b>. The rest of what happened is part of human history of growth and decline of "
    "civilisations."))
story.append(gap(4))
story.append(memory_aid(
    "Brain size climbs in hundreds: <b>Homo habilis 650-800</b>, <b>Homo erectus about 900</b>, "
    "<b>Neanderthal 1400</b> (all in cc) - \"<b>H-E-N</b>: Habilis, Erectus, Neanderthal\" in "
    "order of increasing brain size."))
story.append(gap(8))

# ======================================================================================
# ---- Quick Recap (§5 item 8 - rewritten from summary S1-S9) ----
# ======================================================================================
story.append(heading("Recap", "QUICK RECAP", 1))
story.append(b1(
    "<b>Origin of life</b> makes sense only against the origin of the <b>universe (about 13.8 "
    "billion years)</b> and of the <b>earth (about 4.5 billion years)</b>; life appeared almost "
    "<b>four billion years back</b>."))
story.append(b1(
    "Most scientists hold that <b>chemical evolution</b> (formation of biomolecules from "
    "inorganic constituents - Oparin, Haldane; Miller 1953) <b>preceded the first cellular forms "
    "of life</b> (about 2000 mya). Pasteur dismissed <b>spontaneous generation</b>."))
story.append(b1(
    "What followed is a <b>conjectured story</b> built on <b>Darwinian ideas of organic evolution "
    "by natural selection</b>: <b>branching descent</b> and <b>natural selection</b> are its two "
    "key concepts; fitness means <b>reproductive fitness</b>."))
story.append(b1(
    "Diversity of life forms has been <b>changing over millions of years</b>. <b>Variations in a "
    "population result in variable fitness</b>; <b>habitat fragmentation and genetic drift</b> "
    "may accentuate these variations, leading to <b>new species</b> and hence evolution."))
story.append(b1(
    "Evidence for evolution comes from <b>fossils (paleontology)</b>, <b>comparative anatomy</b> "
    "(homology = divergent evolution, accounted for by <b>branching descent</b>; analogy = "
    "convergent evolution) and <b>comparative biochemistry</b>, plus industrial melanism and "
    "anthropogenic resistance."))
story.append(b1(
    "<b>Adaptive radiation</b>: Darwin's finches, Australian marsupials; several radiations in one "
    "isolated area give <b>convergent evolution</b> (placental vs marsupial look-alikes)."))
story.append(b1(
    "<b>Hardy-Weinberg</b>: p<super>2</super> + 2pq + q<super>2</super> = 1; disturbed by <b>gene "
    "flow, genetic drift, mutation, genetic recombination and natural selection</b>. Selection "
    "may be <b>stabilising, directional or disruptive</b>. de Vries: <b>mutation, "
    "saltation</b>."))
story.append(b1(
    "The story of <b>modern man</b> is the most interesting, and appears to <b>parallel the "
    "evolution of human brain and language</b> - from <i>Dryopithecus</i>/<i>Ramapithecus</i> "
    "through <i>Homo habilis</i> (650-800 cc), <i>Homo erectus</i> (900 cc) and Neanderthal "
    "(1400 cc) to <i>Homo sapiens</i>."))

# ======================================================================================
# ---- Terms used in the exercises (§5 item 9 / Rule 2 - exercise 3 GAP) ----
# ======================================================================================
story.append(heading("Appendix", "TERMS USED IN THE EXERCISES", 1))
story.append(body(
    "<b>Exercise 3</b> asks for <b>a clear definition of the term species</b>. The chapter uses "
    "the word throughout but never defines it; the definition below is an <b>addition, not "
    "stated in this NCERT chapter</b>."))
story.append(keyterm(
    "<b>Species</b> - a group of individuals that are <b>similar in their characteristics</b> and "
    "can <b>actually or potentially interbreed in nature to produce fertile offspring</b>, while "
    "being <b>reproductively isolated</b> from other such groups (the <b>biological species "
    "concept</b>)."))


def main():
    return build_pdf(OUT_PDF, story, title="Evolution - NEET Notes")


if __name__ == "__main__":
    raise SystemExit(main())
