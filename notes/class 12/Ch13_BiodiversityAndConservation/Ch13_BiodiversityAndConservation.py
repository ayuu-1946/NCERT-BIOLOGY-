"""
NCERT Class 12 Biology, Chapter 13 - Biodiversity and Conservation
NEET replacement notes -> A4 print-ready PDF.

Built under SUPREME COMMAND PROMPT.md v6, Pass 2: written linearly from the
frozen 189-row inventory (Ch13_BiodiversityAndConservation_inventory.md), importing
the repo-level frozen style module `neet_template.py` (v6 §0.6). No style, geometry,
colour or font is re-declared here.

Block markers `# ---- N.N ----` mark every NCERT section so a Pass 3 flag can be
found and fixed in one contiguous block. Inventory row IDs are named in the
comments so any fact can be traced back to its frozen row.

Pass 1 carry-overs actioned (inventory "Carry-overs Pass 2 must action"):
  1. Fig 13.2 caption states the lost colour distinction in words.
  2. `S = CA<super>Z</super>` written in running text (extracts as "S = CAZ").
  3. "Log S = log C + Z log A" written verbatim in running text.
  4. Degrees spelled out as "degrees N" (check 5 safe).
  5. F037 (four-class form) and F181 (all-vertebrates form) both carried, in a NOTE.
  6. F164's 448 sanctuaries carried as the body figure, F184's "more than 450" noted.
  7. Inventory Type-column casing left untouched (cosmetic, frozen rows).

Source: Chapter/class 12/Chapter 13 - Biodiversity and Conservation.pdf
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
from reportlab.platypus import Paragraph, Spacer  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch13_BiodiversityAndConservation.pdf")


def figure(asset_name, caption_text, max_width_cm=15.9):
    """Chapter-local binding of the shared figure() helper (§0.6)."""
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
story += title_block("Biodiversity and Conservation")

# ======================================================================================
# ---- Chapter opener (F001-F008) ----
# ======================================================================================
# F001 - chapter title + printed contents list
story.append(heading("Ch 13", "BIODIVERSITY AND CONSERVATION - Chapter Opener", 1))
story.append(body(
    "<b>Chapter contents (as printed on the opener page):</b> 13.1 Biodiversity; "
    "13.2 Biodiversity Conservation."))
# F002 (opener), F003
story.append(body(
    "If an <b>alien from a distant galaxy</b> were to visit our planet Earth, the first thing "
    "that would amaze and baffle him would most probably be the <b>enormous diversity of life</b> "
    "that he would encounter. Even for humans, the rich variety of living organisms with which "
    "they share this planet never ceases to astonish and fascinate us."))
# F004, F005, F006, F007 - the opener's four diversity counts, exact NCERT figures
story.append(data_table([
    ["Group", "Number of species (NCERT opener)"],
    ["<b>Ants</b>", "more than <b>20,000</b> species"],
    ["<b>Beetles</b>", "<b>3,00,000</b> species"],
    ["<b>Fishes</b>", "<b>28,000</b> species"],
    ["<b>Orchids</b>", "nearly <b>20,000</b> species"],
], col_widths=[3.0, 7.0]))
story.append(gap())
# F008 - the six framing questions asked by ecologists and evolutionary biologists
story.append(body(
    "<b>Ecologists and evolutionary biologists</b> have been struck by six questions, which frame "
    "the whole chapter:"))
story.append(b1("Why are there so many species?"))
story.append(b1("Did such great diversity exist throughout earth's history?"))
story.append(b1("How did this diversification come about?"))
story.append(b1("How and why is this diversity important to the biosphere?"))
story.append(b1("Would it function any differently if the diversity was much less?"))
story.append(b1("How do humans benefit from the diversity of life?"))

# ======================================================================================
# ---- 13.1 BIODIVERSITY (F009-F023) ----
# ======================================================================================
story.append(heading("13.1", "BIODIVERSITY", 1))
# F010 - opener sentence of 13.1
story.append(body(
    "In our biosphere <b>immense diversity (or heterogeneity)</b> exists <b>not only at the "
    "species level but at all levels of biological organisation</b>, ranging from "
    "<b>macromolecules within cells to biomes</b>."))
# F011 - definition + the man who popularised the term
story.append(keyterm(
    "<b>Biodiversity</b> is the term popularised by the <b>sociobiologist Edward Wilson</b> to "
    "describe the <b>combined diversity at all the levels of biological organisation</b>."))
# F012 - the three most important levels
story.append(body(
    "Diversity exists at many levels; <b>the most important of them are</b> three - "
    "<b>genetic diversity</b>, <b>species diversity</b> and <b>ecological diversity</b>."))
# F013-F021 - the three levels, each with its NCERT example, converted to a table (§3)
story.append(data_table([
    ["Level of diversity", "What it means (NCERT)", "NCERT example"],
    ["<b>(i) Genetic diversity</b>",
     "A <b>single species</b> might show <b>high diversity at the genetic level over its "
     "distributional range</b>.",
     "The genetic variation shown by the medicinal plant <i>Rauwolfia vomitoria</i> growing in "
     "different <b>Himalayan ranges</b> might be in terms of the <b>potency and concentration of "
     "the active chemical (reserpine)</b> that the plant produces. India has more than "
     "<b>50,000 genetically different strains of rice</b> and <b>1,000 varieties of mango</b>."],
    ["<b>(ii) Species diversity</b>",
     "Diversity <b>at the species level</b>.",
     "The <b>Western Ghats</b> have a <b>greater amphibian species diversity</b> than the "
     "<b>Eastern Ghats</b>."],
    ["<b>(iii) Ecological diversity</b>",
     "Diversity <b>at the ecosystem level</b>.",
     "<b>India</b>, with its <b>deserts, rain forests, mangroves, coral reefs, wetlands, "
     "estuaries and alpine meadows</b>, has a <b>greater ecosystem diversity</b> than a "
     "Scandinavian country like <b>Norway</b>."],
], col_widths=[2.3, 3.3, 6.4]))
story.append(gap())
# F022, F023
story.append(body(
    "It has taken <b>millions of years of evolution</b> to accumulate this rich diversity in "
    "nature, <b>but we could lose all that wealth in less than two centuries</b> if the present "
    "rates of species losses continue. Biodiversity and its conservation are now <b>vital "
    "environmental issues of international concern</b>, as more and more people around the world "
    "begin to realise the <b>critical importance of biodiversity for our survival and "
    "well-being</b> on this planet."))

# ======================================================================================
# ---- 13.1.1 How Many Species are there on Earth and How Many in India? (F024-F051,
#      F180, F181, F186) ----
# ======================================================================================
story.append(heading("13.1.1", "How Many Species are there on Earth and How Many in India?", 2))
# F025 - opener
story.append(body(
    "Since there are <b>published records</b> of all the species discovered and named, we know "
    "<b>how many species in all have been recorded so far</b>, but it is <b>not easy to answer</b> "
    "the question of <b>how many species there are on earth</b>."))
# F026, F027, F028, F029
story.append(keyterm(
    "<b>IUCN</b> - the <b>International Union for Conservation of Nature and Natural "
    "Resources</b>."))
story.append(b1(
    "According to the <b>IUCN (2004)</b>, the total number of <b>plant and animal species "
    "described so far</b> is <b>slightly more than 1.5 million</b>."))
story.append(b1(
    "But we have <b>no clear idea of how many species are yet to be discovered and described</b>. "
    "<b>Estimates vary widely</b> and many of them are <b>only educated guesses</b>."))
story.append(b1(
    "For many taxonomic groups, <b>species inventories are more complete in temperate than in "
    "tropical countries</b>."))
# F030 - the extrapolation method, written as a process flow (§4.2)
story.append(body("<b>How biologists arrive at a gross estimate of the global species total:</b>"))
story.append(process_flow([
    "Recognise that an <b>overwhelmingly large proportion of the species waiting to be "
    "discovered are in the tropics</b>.",
    "Make a <b>statistical comparison of the temperate-tropical species richness</b> of an "
    "<b>exhaustively studied group of insects</b>.",
    "<b>Extrapolate this ratio</b> to other groups of animals and plants.",
    "Arrive at a <b>gross estimate of the total number of species on earth</b>.",
]))
story.append(gap())
# F031, F032, F180
story.append(data_table([
    ["Estimate of global species diversity", "Value"],
    ["Some <b>extreme estimates</b>", "<b>20 to 50 million</b> species"],
    ["A <b>more conservative and scientifically sound estimate</b> made by "
     "<b>Robert May</b>", "about <b>7 million</b> species"],
    ["Species <b>recorded</b> so far (IUCN 2004)", "slightly more than <b>1.5 million</b>"],
    ["Species <b>still waiting to be discovered and named</b> (stated in the NCERT chapter "
     "summary)", "nearly <b>6 million</b> species on earth"],
], col_widths=[7.0, 3.4]))
story.append(gap())
# F033, F034, F035, F036 - proportions of the recorded species
story.append(b1(
    "<b>More than 70 per cent</b> of all the species recorded are <b>animals</b>, while "
    "<b>plants</b> (including <b>algae, fungi, bryophytes, gymnosperms and angiosperms</b>) "
    "comprise <b>no more than 22 per cent</b> of the total."))
story.append(b1(
    "Among animals, <b>insects</b> are the <b>most species-rich taxonomic group</b>, making up "
    "<b>more than 70 per cent</b> of the total. That means, <b>out of every 10 animals on this "
    "planet, 7 are insects</b>."))
# [VERIFICATION FIX] F035a (Pass 3(b) direction 2, UNINVENTORIED) - NCERT asks this question
# immediately after the insect figure and never answers it; exercise 9 is built on it.
story.append(b1(
    "NCERT stops here to ask, and does not answer: <b>\"Again, how do we explain this enormous "
    "diversification of insects?\"</b> - the same puzzle <b>exercise 9</b> puts as how animals "
    "achieved their greater diversification."))
# F037 + F181 - both wordings carried, per carry-over 5
story.append(note(
    "Two different NCERT statements about <b>Fungi</b>, and both are examinable. The <b>body</b> "
    "says the number of fungi species in the world is <b>more than the combined total of the "
    "species of fishes, amphibians, reptiles and mammals</b> (four classes, birds not included). "
    "The <b>chapter summary</b> makes the broader claim that <b>the group Fungi has more species "
    "than all the vertebrate species combined</b>. Learn both forms - the broader summary "
    "sentence does not replace the body's exact four-class list."))
# F186 - exercise-only figure, flagged where the body figure is given
story.append(note(
    "<b>Number mismatch NEET can quote either way.</b> The body says animals are <b>more than 70 "
    "per cent</b> of recorded species and plants <b>22 per cent</b>. NCERT <b>exercise 9</b> "
    "states the same comparison as <b>plants 22 per cent</b> versus <b>animals 72 per cent</b>. "
    "The exact <b>72 per cent</b> figure appears only in the exercise, so accept both the "
    "\"more than 70 per cent\" and the \"72 per cent\" form."))
story.append(gap())
# F038 - in-text pointer + caption; F039 - the 18 in-figure labels, all carried in the table below
story.append(body(
    "In <b>Figure 13.1</b>, biodiversity is depicted showing <b>species number of major "
    "taxa</b>."))
story.append(figure(
    "fig_13_1.png",
    "<b>Fig. 13.1</b> - Representing global biodiversity: proportionate number of species of "
    "major taxa of plants, invertebrates and vertebrates. The three panels are labelled "
    "<b>Invertebrates</b>, <b>Vertebrates</b> and <b>Plants</b>; NCERT prints no numeric "
    "percentages inside the figure, so the proportions are given in the running text above.",
    max_width_cm=11.5))
# F039 - every in-figure label written into running text (§4.4, check 6)
story.append(body(
    "<b>What each panel of Figure 13.1 names</b> (the figure carries these group labels only, "
    "with no numbers printed on it):"))
story.append(data_table([
    ["Panel", "Groups labelled in that panel of Figure 13.1"],
    ["<b>Invertebrates</b>",
     "<b>Insects</b> (by far the largest wedge), <b>Crustaceans</b>, <b>Molluscs</b> and "
     "<b>Other animal groups</b>."],
    ["<b>Vertebrates</b>",
     "<b>Fishes</b>, <b>Birds</b>, <b>Reptiles</b>, <b>Mammals</b> and <b>Amphibians</b>."],
    ["<b>Plants</b>",
     "<b>Angiosperms</b>, <b>Fungi</b>, <b>Algae</b>, <b>Mosses</b>, <b>Ferns and allies</b> and "
     "<b>Lichens</b>."],
], col_widths=[2.2, 8.0]))
story.append(gap())
# F040, F041, F042 - prokaryotes are outside these estimates
story.append(b1(
    "It should be noted that <b>these estimates do not give any figures for prokaryotes</b>."))
story.append(b1(
    "Biologists are <b>not sure how many prokaryotic species</b> there might be. "
    "<b>Conventional taxonomic methods are not suitable for identifying microbial species</b>, "
    "and <b>many species are simply not culturable under laboratory conditions</b>."))
story.append(b1(
    "If we accept <b>biochemical or molecular criteria</b> for delineating species for this group, "
    "then <b>their diversity alone might run into millions</b>."))
story.append(gap())
# F043-F048 - India's share, converted to a table
story.append(body("<b>India's share of global biodiversity:</b>"))
story.append(data_table([
    ["Item", "Figure (NCERT)"],
    ["India's share of the <b>world's land area</b>", "only <b>2.4 per cent</b>"],
    ["India's share of the <b>global species diversity</b>",
     "an impressive <b>8.1 per cent</b> - which is what makes our country one of the <b>12 mega "
     "diversity countries</b> of the world"],
    ["Species <b>recorded</b> from India",
     "nearly <b>45,000 species of plants</b> and <b>twice as many</b> of <b>animals</b>"],
    ["Proportion of all species recorded so far, if we accept <b>May's global estimate</b>",
     "only <b>22 per cent</b> of the total"],
    ["Applying that proportion to India's figures, species <b>yet to be discovered and "
     "described</b> in India",
     "probably more than <b>1,00,000 plant species</b> and more than <b>3,00,000 animal "
     "species</b>"],
], col_widths=[4.6, 5.8]))
story.append(gap())
# [VERIFICATION FIX] F048a (Pass 3(b) direction 2, UNINVENTORIED) - the two rhetorical questions
# NCERT poses between the India figures and F049; both were absent from the frozen inventory.
story.append(body(
    "NCERT then asks two questions of its own: <b>\"How many living species are actually there "
    "waiting to be discovered and named?\"</b> and <b>\"Would we ever be able to complete the "
    "inventory of the biological wealth of our country?\"</b>"))
# F049, F050, F051
story.append(body(
    "Consider the <b>immense trained manpower (taxonomists)</b> and the <b>time required to "
    "complete the job</b>. The situation appears <b>more hopeless</b> when we realise that a "
    "<b>large fraction of these species faces the threat of becoming extinct even before we "
    "discover them</b> - <b>nature's biological library is burning even before we catalogued the "
    "titles of all the books stocked there</b>."))

# ======================================================================================
# ---- 13.1.2 Patterns of Biodiversity (F052-F081, F187) ----
# ======================================================================================
story.append(heading("13.1.2", "Patterns of Biodiversity", 2))

# ---- 13.1.2 (i) Latitudinal gradients (F053-F068) ----
story.append(heading("13.1.2 (i)", "Latitudinal gradients", 3))
# F054 (opener), F055, F056, F057
story.append(body(
    "The <b>diversity of plants and animals is not uniform throughout the world</b> but shows a "
    "rather <b>uneven distribution</b>. For many group of animals or plants there are interesting "
    "patterns in diversity, the <b>most well-known being the latitudinal gradient in "
    "diversity</b>."))
story.append(b1(
    "<b>In general, species diversity decreases as we move away from the equator towards the "
    "poles.</b>"))
story.append(b1(
    "With <b>very few exceptions</b>, <b>tropics</b> (latitudinal range of <b>23.5 degrees N to "
    "23.5 degrees S</b>) <b>harbour more species</b> than <b>temperate or polar areas</b>."))
# F058-F062 - the latitude/species evidence as a table
story.append(data_table([
    ["Place", "Latitude", "Species richness (NCERT figures)"],
    ["<b>Colombia</b>", "near the <b>equator</b>", "nearly <b>1,400 species of birds</b>"],
    ["<b>New York</b>", "<b>41 degrees N</b>", "<b>105 species</b> of birds"],
    ["<b>Greenland</b>", "<b>71 degrees N</b>", "only <b>56 species</b> of birds"],
    ["<b>India</b>", "much of its land area in the <b>tropical latitudes</b>",
     "more than <b>1,200 species of birds</b>"],
    ["<b>Equador</b> (tropical) versus the <b>Midwest of the USA</b> (temperate)",
     "tropical versus temperate",
     "A forest in a tropical region like <b>Equador</b> has <b>up to 10 times as many species of "
     "vascular plants</b> as a forest of <b>equal area</b> in a temperate region like the "
     "<b>Midwest of the USA</b>."],
], col_widths=[3.0, 2.6, 5.0]))
story.append(gap())
# F063, F064 - Amazon inventory
story.append(body(
    "The largely tropical <b>Amazonian rain forest in South America</b> has the <b>greatest "
    "biodiversity on earth</b>. Its recorded inventory:"))
story.append(data_table([
    ["Group", "Species in the Amazonian rain forest"],
    ["<b>Plants</b>", "more than <b>40,000</b>"],
    ["<b>Fishes</b>", "<b>3,000</b>"],
    ["<b>Birds</b>", "<b>1,300</b>"],
    ["<b>Mammals</b>", "<b>427</b>"],
    ["<b>Amphibians</b>", "<b>427</b>"],
    ["<b>Reptiles</b>", "<b>378</b>"],
    ["<b>Invertebrates</b>", "more than <b>1,25,000</b>"],
], col_widths=[3.0, 7.0]))
story.append(gap())
# F065
story.append(b1(
    "Scientists estimate that <b>in these rain forests there might be at least two million insect "
    "species waiting to be discovered and named</b>."))
story.append(gap())
# F066, F067, F068 - the three hypotheses
# [VERIFICATION FIX] F065a (Pass 3(b) direction 2, UNINVENTORIED) - NCERT's own framing sentence,
# restored verbatim in place of the earlier paraphrase.
story.append(body(
    "<b>What is so special about tropics that might account for their greater biological "
    "diversity?</b> <b>Ecologists and evolutionary biologists</b> have proposed <b>various "
    "hypotheses</b>; some important ones are:"))
story.append(data_table([
    ["Hypothesis", "Reasoning (NCERT)"],
    ["<b>(a) More evolutionary time</b>",
     "<b>Speciation is generally a function of time.</b> Unlike temperate regions subjected to "
     "<b>frequent glaciations</b> in the past, <b>tropical latitudes have remained relatively "
     "undisturbed for millions of years</b> and thus had a <b>long evolutionary time for species "
     "diversification</b>."],
    ["<b>(b) Constant, predictable environment</b>",
     "<b>Tropical environments, unlike temperate ones, are less seasonal, relatively more "
     "constant and predictable.</b> Such constant environments <b>promote niche "
     "specialisation</b> and lead to a <b>greater species diversity</b>."],
    ["<b>(c) More solar energy</b>",
     "There is <b>more solar energy available in the tropics</b>, which <b>contributes to higher "
     "productivity</b>; this in turn <b>might contribute indirectly to greater diversity</b>."],
], col_widths=[2.8, 7.6]))

# ---- 13.1.2 (ii) Species-Area relationships (F069-F081, F187) ----
story.append(heading("13.1.2 (ii)", "Species-Area relationships", 3))
# F070, F071
story.append(body(
    "During his <b>pioneering and extensive explorations in the wilderness of South American "
    "jungles</b>, the <b>great German naturalist and geographer Alexander von Humboldt</b> "
    "observed that <b>within a region species richness increased with increasing explored area, "
    "but only up to a limit</b>."))
# F072, F073, F074 - carry-over 2 and 3: both label forms written into running text
story.append(b1(
    "For a <b>wide variety of taxa</b> - <b>angiosperm plants, birds, bats, freshwater "
    "fishes</b> - the relation between <b>species richness</b> and <b>area</b> turns out to be a "
    "<b>rectangular hyperbola</b>, of the form <b>S = CA<super>Z</super></b>."))
story.append(b1(
    "On a <b>logarithmic scale</b> the relationship is a <b>straight line</b> described by the "
    "equation <b>log S = log C + Z log A</b> (the same equation is printed on the figure as "
    "<b>Log S = log C + Z log A</b>, plotted on a <b>log-log scale</b>)."))
story.append(keyterm(
    "In this equation: <b>S = Species richness</b>; <b>A = Area</b>; <b>Z = slope of the line "
    "(regression coefficient)</b>; <b>C = Y-intercept</b>."))
# F075, F076, F077, F078
story.append(data_table([
    ["Scale of the analysis", "Value of <b>Z</b> (slope)", "NCERT evidence"],
    ["<b>Within a region</b> - small areas",
     "<b>0.1 to 0.2</b>, <b>regardless of the taxonomic group or the region</b>",
     "Whether it is the <b>plants in Britain</b>, <b>birds in California</b> or <b>molluscs in "
     "New York state</b>, the <b>slopes of the regression line are amazingly similar</b>."],
    ["<b>Very large areas</b> - entire continents",
     "much <b>steeper</b>: <b>0.6 to 1.2</b>",
     "For <b>frugivorous (fruit-eating) birds and mammals</b> in the <b>tropical forests of "
     "different continents</b>, the slope is found to be <b>1.15</b>."],
], col_widths=[2.8, 3.0, 5.0]))
story.append(gap())
# F080 - caption; F081 - all five in-figure labels carried in the caption and the text above
story.append(figure(
    "fig_13_2.png",
    "<b>Fig. 13.2</b> - Showing species area relationship. Note that on log scale the "
    "relationship becomes linear. <b>Colour-loss note:</b> the original NCERT figure told its two "
    "plots apart by colour, so read them here by tone - the <b>mid-grey curve</b> is the "
    "<b>rectangular hyperbola S = CA<super>Z</super></b> of <b>Species richness</b> against "
    "<b>Area</b> on an arithmetic scale, and the <b>near-black straight line</b> is the same "
    "relationship on a <b>log-log scale</b>, labelled <b>Log S = log C + Z log A</b>.",
    max_width_cm=9.5))
# F079 + F187 - the question the book poses and never answers, answered here (exercise gap Q4)
story.append(note(
    "NCERT asks, and leaves unanswered in the body: <b>\"What do steeper slopes mean in this "
    "context?\"</b> - and <b>exercise 4</b> asks for the <b>significance of the slope of "
    "regression in a species-area relationship</b>. A <b>steeper slope (a larger Z)</b> means "
    "<b>species richness rises faster for every unit increase in area</b>. That is why whole "
    "<b>continents</b> accumulate species far more steeply (<b>Z of 0.6 to 1.2</b>, and "
    "<b>1.15</b> for frugivorous birds and mammals) than <b>habitat patches within one "
    "region</b>, where Z stays a shallow <b>0.1 to 0.2</b> whatever the taxon or region."))

# ======================================================================================
# ---- 13.1.3 The importance of Species Diversity to the Ecosystem (F082-F094, F185) ----
# ======================================================================================
story.append(heading("13.1.3", "The importance of Species Diversity to the Ecosystem", 2))
# F083 (opener), F084
story.append(body(
    "<b>Does the number of species in a community really matter to the functioning of the "
    "ecosystem?</b> This is a question for which <b>ecologists have not been able to give a "
    "definitive answer</b>."))
# F085, F086
story.append(b1(
    "For <b>many decades</b>, ecologists believed that <b>communities with more species, "
    "generally, tend to be more stable</b> than those with <b>less species</b>."))
# [VERIFICATION FIX] F085a (Pass 3(b) direction 2, UNINVENTORIED) - NCERT asks this question and
# F086 is its answer; the question itself had no inventory row and was absent from the notes.
story.append(b1(
    "NCERT then asks: <b>\"What exactly is stability for a biological community?\"</b>"))
story.append(keyterm(
    "A <b>stable community</b> should <b>not show too much variation in productivity from year to "
    "year</b>; it must be either <b>resistant or resilient to occasional disturbances</b> "
    "(natural or man-made); and it must also be <b>resistant to invasions by alien species</b>."))
# F087, F088, F089
story.append(body(
    "We <b>don't know how these attributes are linked to species richness</b> in a community, but "
    "<b>David Tilman's long-term ecosystem experiments using outdoor plots</b> provide some "
    "<b>tentative answers</b>:"))
story.append(b1("Plots with <b>more species</b> showed <b>less year-to-year variation in total "
                "biomass</b>."))
story.append(b1("<b>Increased diversity contributed to higher productivity</b>."))
# F185 - the summary's compact triad
story.append(b1(
    "The chapter summary states this in exam-shaped form: it is believed that <b>communities with "
    "high diversity tend to be less variable, more productive and more resistant to biological "
    "invasions</b>."))
# F090
story.append(b1(
    "<b>Rich biodiversity is not only essential for ecosystem health but imperative for the very "
    "survival of the human race on this planet.</b>"))
story.append(gap())
# F091 - the three questions NCERT poses
story.append(body("NCERT poses three questions here:"))
story.append(b1("Does it really matter to us if a few species become extinct?"))
story.append(b1("Would <b>Western Ghats</b> ecosystems be <b>less functional</b> if one of its "
                "<b>tree frog species</b> is lost forever?"))
story.append(b1("How is our quality of life affected if, say, instead of <b>20,000</b> we have "
                "only <b>15,000 species of ants</b> on earth?"))
story.append(gap())
# F092, F093, F094 - the rivet popper hypothesis
# [VERIFICATION FIX] F092a (Pass 3(b) direction 2, UNINVENTORIED) - the first half of NCERT's
# sentence ("There are no direct answers to such naive questions") had no row and was dropped.
story.append(body(
    "<b>There are no direct answers to such naive questions</b>, but a proper perspective comes "
    "through an analogy - the <b>'rivet popper hypothesis'</b> used by <b>Stanford ecologist Paul "
    "Ehrlich</b>:"))
story.append(process_flow([
    "In an <b>airplane (ecosystem)</b> all parts are joined together using <b>thousands of rivets "
    "(species)</b>.",
    "If <b>every passenger</b> travelling in it starts <b>popping a rivet</b> to take home "
    "(<b>causing a species to become extinct</b>), it <b>may not affect flight safety</b> "
    "(proper functioning of the ecosystem) <b>initially</b>.",
    "But as <b>more and more rivets are removed</b>, the <b>plane becomes dangerously weak over "
    "a period of time</b>.",
    "Furthermore, <b>which rivet is removed may also be critical</b>: loss of rivets <b>on the "
    "wings</b> (<b>key species that drive major ecosystem functions</b>) is obviously a <b>more "
    "serious threat to flight safety</b> than loss of a few rivets <b>on the seats or windows "
    "inside the plane</b>.",
]))

# ======================================================================================
# ---- 13.1.4 Loss of Biodiversity (F095-F132, F179, F182, exercise gap Q10) ----
# ======================================================================================
story.append(heading("13.1.4", "Loss of Biodiversity", 2))
# F096 (opener), F097
story.append(body(
    "While it is <b>doubtful if any new species are being added (through speciation)</b> into the "
    "earth's treasury of species, there is <b>no doubt about their continuing losses</b>. The "
    "<b>biological wealth of our planet has been declining rapidly</b> and the <b>accusing finger "
    "is clearly pointing to human activities</b>."))
# F098-F104, F182 - the recorded losses
story.append(data_table([
    ["Recorded loss", "NCERT figure"],
    ["Extinction following the <b>colonisation of tropical Pacific Islands by humans</b>",
     "said to have led to the extinction of more than <b>2,000 species of native birds</b>"],
    ["Extinctions documented by the <b>IUCN Red List (2004)</b> <b>in the last 500 years</b>",
     "<b>784 species</b>, including <b>338 vertebrates</b>, <b>359 invertebrates</b> and "
     "<b>87 plants</b> (the chapter summary rounds this to <b>nearly 700 species</b> extinct in "
     "recent times)"],
    ["Some <b>examples of recent extinctions</b>",
     "the <b>dodo</b> (Mauritius), <b>quagga</b> (Africa), <b>thylacine</b> (Australia), "
     "<b>Steller's Sea Cow</b> (Russia) and <b>three subspecies (Bali, Javan, Caspian) of "
     "tiger</b>"],
    ["Disappearance in <b>the last twenty years alone</b>", "<b>27 species</b>"],
    ["Species <b>currently facing the threat of extinction</b> world-wide",
     "more than <b>15,500 species</b> (the chapter summary adds that <b>more than 650 of these "
     "are from India</b>)"],
], col_widths=[3.8, 6.6]))
story.append(gap())
# F102
story.append(b1(
    "Careful analysis of records shows that <b>extinctions across taxa are not random</b>; "
    "<b>some groups like amphibians appear to be more vulnerable to extinction</b>."))
# F104 - the four exact percentages
story.append(body("Presently, the groups facing the threat of extinction in the world are:"))
story.append(data_table([
    ["Group", "Share of all species in that group facing the threat of extinction"],
    ["<b>Birds</b>", "<b>12 per cent</b>"],
    ["<b>Mammals</b>", "<b>23 per cent</b>"],
    ["<b>Amphibians</b>", "<b>32 per cent</b>"],
    ["<b>Gymnosperms</b>", "<b>31 per cent</b>"],
], col_widths=[2.4, 7.6]))
story.append(gap())
# F105, F106, F179, F107, F108, F109
story.append(b1(
    "From a study of the <b>history of life on earth through fossil records</b>, we learn that "
    "<b>large-scale loss of species like the one we are currently witnessing have also happened "
    "earlier, even before humans appeared on the scene</b>."))
story.append(b1(
    "During the long period (<b>more than 3 billion years</b>) since the <b>origin and "
    "diversification of life on earth</b> there were <b>five episodes of mass extinction</b> of "
    "species. The chapter summary dates the origin of life more precisely: <b>life originated on "
    "earth nearly 3.8 billion years ago</b>, since when there had been <b>enormous "
    "diversification of life forms</b>."))
story.append(b1(
    "<b>How is the 'Sixth Extinction' presently in progress different from the previous "
    "episodes? The difference is in the rates.</b> The <b>current species extinction rates</b> "
    "are estimated to be <b>100 to 1,000 times faster than in the pre-human times</b>, and "
    "<b>our activities are responsible for the faster rates</b>."))
story.append(b1(
    "Ecologists warn that <b>if the present trends continue, nearly half of all the species on "
    "earth might be wiped out within the next 100 years</b>."))
story.append(gap())
# F110 - the three consequences, exactly as lettered by NCERT
story.append(body(
    "<b>In general, loss of biodiversity in a region may lead to:</b>"))
story.append(b1("<b>(a)</b> <b>decline in plant production</b>;"))
story.append(b1("<b>(b)</b> <b>lowered resistance to environmental perturbations</b> such as "
                "<b>drought</b>;"))
story.append(b1("<b>(c)</b> <b>increased variability in certain ecosystem processes</b> such as "
                "<b>plant productivity, water use, and pest and disease cycles</b>."))

# ---- 13.1.4 Causes of biodiversity losses - 'The Evil Quartet' (F111-F132) ----
story.append(heading("13.1.4", "Causes of biodiversity losses - 'The Evil Quartet'", 3))
# F111, F112; [VERIFICATION FIX] F112a (Pass 3(b) direction 2, UNINVENTORIED) - the section's own
# opening sentence ("The accelerated rates ... are largely due to human activities") had no row.
story.append(body(
    "<b>The accelerated rates of species extinctions that the world is facing now are largely due "
    "to human activities.</b> There are <b>four major causes</b> - <b>'The Evil Quartet' is the "
    "sobriquet used to describe them</b>."))

# (i) Habitat loss and fragmentation - F113-F119
story.append(body("<b>(i) Habitat loss and fragmentation:</b>"))
story.append(b1("This is the <b>most important cause driving animals and plants to "
                "extinction</b>."))
story.append(b1(
    "The <b>most dramatic examples of habitat loss come from tropical rain forests</b>. Once "
    "covering <b>more than 14 per cent of the earth's land surface</b>, these rain forests now "
    "cover <b>no more than 6 per cent</b>. By the time you finish reading this chapter, "
    "<b>1000 more hectares of rain forest</b> would have been lost."))
story.append(b1(
    "The <b>Amazon rain forest</b> - so huge that it is called the <b>'lungs of the planet'</b> - "
    "harbouring <b>probably millions of species</b>, is being <b>cut and cleared for cultivating "
    "soya beans</b> or for <b>conversion to grasslands for raising beef cattle</b>."))
story.append(b1(
    "<b>Besides total loss, the degradation of many habitats by pollution</b> also <b>threatens "
    "the survival of many species</b>."))
story.append(b1(
    "When <b>large habitats are broken up into small fragments</b> due to various human "
    "activities, <b>mammals and birds requiring large territories</b> and <b>certain animals with "
    "migratory habits</b> are <b>badly affected, leading to population declines</b>."))

# (ii) Over-exploitation - F120-F123
story.append(body("<b>(ii) Over-exploitation:</b>"))
story.append(b1(
    "Humans have <b>always depended on nature for food and shelter</b>, but when <b>'need' turns "
    "to 'greed'</b>, it leads to <b>over-exploitation of natural resources</b>."))
story.append(b1(
    "<b>Many species extinctions in the last 500 years</b> - <b>Steller's sea cow</b>, "
    "<b>passenger pigeon</b> - were due to <b>overexploitation by humans</b>."))
story.append(b1(
    "Presently <b>many marine fish populations around the world are over harvested</b>, "
    "<b>endangering the continued existence of some commercially important species</b>."))

# (iii) Alien species invasions - F124-F128
story.append(body("<b>(iii) Alien species invasions:</b>"))
story.append(b1(
    "When <b>alien species are introduced unintentionally or deliberately for whatever "
    "purpose</b>, <b>some of them turn invasive</b>, and <b>cause decline or extinction of "
    "indigenous species</b>."))
story.append(data_table([
    ["Alien species", "What it did (NCERT)"],
    ["<b>Nile perch</b> introduced into <b>Lake Victoria</b> in <b>east Africa</b>",
     "led eventually to the <b>extinction of an ecologically unique assemblage of more than 200 "
     "species of cichlid fish</b> in the lake"],
    ["<b>Carrot grass (<i>Parthenium</i>)</b>, <b>Lantana</b> and <b>water hyacinth "
     "(<i>Eicchornia</i>)</b>", "<b>invasive weed species</b>"],
    ["Recent <b>illegal introduction</b> of the <b>African catfish <i>Clarias gariepinus</i></b> "
     "for <b>aquaculture</b> purposes",
     "<b>posing a threat to the indigenous catfishes</b> in our rivers"],
], col_widths=[4.0, 6.4]))
story.append(gap())

# (iv) Co-extinctions - F129-F132
story.append(body("<b>(iv) Co-extinctions:</b>"))
story.append(keyterm(
    "<b>Co-extinction</b>: when a <b>species becomes extinct</b>, the <b>plant and animal species "
    "associated with it in an obligatory way</b> also <b>become extinct</b>."))
story.append(b1(
    "When a <b>host fish species becomes extinct</b>, its <b>unique assemblage of parasites</b> "
    "also meets the <b>same fate</b>."))
story.append(b1(
    "Another example is the case of a <b>coevolved plant-pollinator mutualism</b>, where "
    "<b>extinction of one invariably leads to the extinction of the other</b>."))
# Exercise gap Q10 - F189 - explicitly marked outside NCERT
story.append(memory_aid(
    "<b>For NCERT exercise 10</b> (\"can you think of a situation where we <b>deliberately want "
    "to make a species extinct</b>, and how would you justify it?\") the chapter itself supplies "
    "<b>no content at all</b>, so this reasoning is <b>outside NCERT</b> and is <b>not</b> "
    "examinable as NCERT text. The defensible answer is a <b>disease-causing organism</b> that "
    "exists only to harm - the <b>smallpox virus</b> (already eradicated), the <b>polio "
    "virus</b>, or the <b>Guinea worm</b>. Justification: eradicating such a parasite ends "
    "enormous human suffering, and these organisms occupy no ecosystem role that other species "
    "depend on obligatorily."))

# ======================================================================================
# ---- 13.2 BIODIVERSITY CONSERVATION (F133) ----
# ======================================================================================
story.append(heading("13.2", "BIODIVERSITY CONSERVATION", 1))

# ======================================================================================
# ---- 13.2.1 Why Should We Conserve Biodiversity? (F134-F147, F183, exercise gap Q8) ----
# ======================================================================================
story.append(heading("13.2.1", "Why Should We Conserve Biodiversity?", 2))
# F135 (opener), F136
story.append(body(
    "There are <b>many reasons, some obvious and others not so obvious, but all equally "
    "important</b>. They can be grouped into <b>three categories</b>: <b>narrowly utilitarian</b>, "
    "<b>broadly utilitarian</b>, and <b>ethical</b>."))

# Narrowly utilitarian - F137-F141
story.append(heading("13.2.1", "Narrowly utilitarian arguments", 3))
story.append(b1(
    "The <b>narrowly utilitarian arguments</b> for conserving biodiversity are <b>obvious</b>: "
    "humans derive <b>countless direct economic benefits from nature</b> - <b>food</b> (cereals, "
    "pulses, fruits), <b>firewood</b>, <b>fibre</b>, <b>construction material</b>, <b>industrial "
    "products</b> (tannins, lubricants, dyes, resins, perfumes) and <b>products of medicinal "
    "importance</b>."))
story.append(b1(
    "More than <b>25 per cent of the drugs currently sold in the market worldwide are derived "
    "from plants</b>, and <b>25,000 species of plants</b> contribute to the <b>traditional "
    "medicines</b> used by native peoples around the world."))
story.append(b1(
    "<b>Nobody knows how many more medicinally useful plants there are in tropical rain forests "
    "waiting to be explored.</b>"))
story.append(keyterm(
    "<b>Bioprospecting</b> - <b>exploring molecular, genetic and species-level diversity for "
    "products of economic importance</b>. With <b>increasing resources</b> put into "
    "bioprospecting, <b>nations endowed with rich biodiversity can expect to reap enormous "
    "benefits</b>."))

# Broadly utilitarian - F142-F146, F183, Q8
story.append(heading("13.2.1", "Broadly utilitarian arguments", 3))
story.append(b1(
    "The <b>broadly utilitarian argument</b> says that <b>biodiversity plays a major role in many "
    "ecosystem services that nature provides</b>."))
story.append(b1(
    "The <b>fast-dwindling Amazon forest</b> is estimated to produce, <b>through "
    "photosynthesis</b>, <b>20 per cent of the total oxygen in the earth's atmosphere</b>. "
    "<b>Can we put an economic value on this service by nature?</b> You can get some idea by "
    "finding out <b>how much your neighborhood hospital spends on a cylinder of oxygen</b>."))
story.append(b1(
    "<b>Pollination</b> - <b>without which plants cannot give us fruits or seeds</b> - is another "
    "service ecosystems provide through <b>pollinators</b>: <b>bees, bumblebees, birds and "
    "bats</b>. <b>What will be the costs of accomplishing pollination without help from natural "
    "pollinators?</b>"))
story.append(b1(
    "There are other <b>intangible benefits</b> we derive from nature - the <b>aesthetic "
    "pleasures of walking through thick woods</b>, <b>watching spring flowers in full bloom</b> "
    "or <b>waking up to a bulbul's song in the morning</b>. <b>Can we put a price tag on such "
    "things?</b>"))
# F183 + F188 - summary-sourced service list, visibly attributed, plus the soil-erosion inference
story.append(note(
    "<b>Summary-sourced list, and the answer to exercise 8.</b> The <b>chapter summary</b> (not "
    "the body) states that besides the <b>direct benefits</b> - <b>food, fibre, firewood, "
    "pharmaceuticals</b> and so on - there are <b>many indirect benefits we receive through "
    "ecosystem services such as pollination, pest control, climate moderation and flood "
    "control</b>. <b>Exercise 8</b> additionally asks how the <b>biotic components</b> deliver "
    "<b>control of floods and soil erosion</b>; <b>soil erosion is named nowhere in this "
    "chapter</b>, so that part is <b>necessary inference, not NCERT text</b>: vegetation cover "
    "and root systems <b>bind the soil</b> and <b>slow surface run-off</b>, so rain soaks in "
    "instead of sheeting off, which both <b>checks erosion</b> and <b>moderates flooding</b>."))

# Ethical - F147
story.append(heading("13.2.1", "The ethical argument", 3))
story.append(body(
    "The <b>ethical argument</b> for conserving biodiversity relates to <b>what we owe to "
    "millions of plant, animal and microbe species with whom we share this planet</b>. "
    "<b>Philosophically or spiritually, we need to realise that every species has an intrinsic "
    "value, even if it may not be of current or any economic value to us.</b> We have a <b>moral "
    "duty to care for their well-being</b> and to <b>pass on our biological legacy in good order "
    "to future generations</b>."))

# ======================================================================================
# ---- 13.2.2 How do we conserve Biodiversity? (F148-F178, F184) ----
# ======================================================================================
story.append(heading("13.2.2", "How do we conserve Biodiversity?", 2))
# F149 (opener), F150, F151, F152
story.append(body(
    "When we <b>conserve and protect the whole ecosystem</b>, its <b>biodiversity at all levels "
    "is protected</b> - <b>we save the entire forest to save the tiger</b>. This approach is "
    "called <b>in situ (on site) conservation</b>."))
story.append(keyterm(
    "<b>Endangered or threatened</b> - <b>organisms facing a very high risk of extinction in the "
    "wild in the near future</b>."))
story.append(body(
    "However, when there are <b>situations where an animal or plant is endangered or threatened "
    "and needs urgent measures to save it from extinction</b>, <b>ex situ (off site) "
    "conservation</b> is the <b>desirable approach</b>."))

# ---- 13.2.2 In situ conservation (F153-F167, F184) ----
story.append(heading("13.2.2", "In situ conservation", 3))
# F154, F155
story.append(b1(
    "Faced with the <b>conflict between development and conservation</b>, <b>many nations find it "
    "unrealistic and economically not feasible to conserve all their biological wealth</b>."))
story.append(b1(
    "<b>Invariably, the number of species waiting to be saved from extinction far exceeds the "
    "conservation resources available.</b> On a <b>global basis</b>, this problem has been "
    "addressed by <b>eminent conservationists</b>."))
# F156, F157
story.append(keyterm(
    "<b>Biodiversity hotspots</b> - regions identified for <b>maximum protection</b> because they "
    "have <b>very high levels of species richness</b> and a <b>high degree of endemism</b>, that "
    "is, <b>species confined to that region and not found anywhere else</b>."))
# F158-F162
story.append(data_table([
    ["Biodiversity hotspots - the numbers", "NCERT figure"],
    ["Hotspots identified",
     "<b>initially 25</b>, but <b>subsequently nine more</b> have been added, bringing the "
     "<b>total number of biodiversity hotspots in the world to 34</b>"],
    ["What else these hotspots are",
     "they are <b>also regions of accelerated habitat loss</b>"],
    ["Hotspots covering India",
     "<b>three</b> - <b>Western Ghats and Sri Lanka</b>, <b>Indo-Burma</b> and <b>Himalaya</b> - "
     "cover our country's <b>exceptionally high biodiversity regions</b>"],
    ["Land area they cover",
     "<b>all the biodiversity hotspots put together cover less than 2 per cent of the earth's "
     "land area</b>, yet the <b>number of species they collectively harbour is extremely high</b>"],
    ["Value of protecting them",
     "<b>strict protection of these hotspots could reduce the ongoing mass extinctions by almost "
     "30 per cent</b>"],
], col_widths=[3.2, 7.2]))
story.append(gap())
# F163, F164
story.append(b1(
    "In <b>India</b>, <b>ecologically unique and biodiversity-rich regions are legally protected "
    "as biosphere reserves, national parks and sanctuaries</b>. India now has <b>14 biosphere "
    "reserves</b>, <b>90 national parks</b> and <b>448 wildlife sanctuaries</b>."))
# F184 - carry-over 6
story.append(note(
    "<b>Two figures for the same item.</b> The <b>body</b> gives <b>448 wildlife "
    "sanctuaries</b>; the <b>chapter summary</b> writes the same in-situ effort as <b>more than "
    "450 wildlife sanctuaries</b> (alongside the <b>14 biosphere reserves</b>, <b>90 national "
    "parks</b> and <b>many sacred groves</b>). Take <b>448</b> as the exact body figure and "
    "recognise the summary's <b>more than 450</b> form if NEET quotes it."))
# F165, F166, F167
story.append(b1(
    "India has also a <b>history of religious and cultural traditions that emphasised protection "
    "of nature</b>. In <b>many cultures, tracts of forest were set aside</b>, and <b>all the "
    "trees and wildlife within were venerated and given total protection</b>."))
story.append(b1(
    "Such <b>sacred groves</b> are found in the <b>Khasi and Jaintia Hills in Meghalaya</b>, the "
    "<b>Aravalli Hills of Rajasthan</b>, the <b>Western Ghat regions of Karnataka and "
    "Maharashtra</b> and the <b>Sarguja, Chanda and Bastar areas of Madhya Pradesh</b>."))
story.append(b1(
    "In <b>Meghalaya</b>, the <b>sacred groves are the last refuges for a large number of rare "
    "and threatened plants</b>."))

# ---- 13.2.2 Ex situ conservation (F168-F178) ----
story.append(heading("13.2.2", "Ex situ Conservation", 3))
# F169, F170, F171
story.append(b1(
    "In this approach, <b>threatened animals and plants are taken out from their natural habitat "
    "and placed in special setting where they can be protected and given special care</b>."))
story.append(b1(
    "<b>Zoological parks, botanical gardens and wildlife safari parks</b> serve this purpose."))
story.append(b1(
    "There are <b>many animals that have become extinct in the wild but continue to be maintained "
    "in zoological parks</b>."))
# [VERIFICATION FIX] F171a (Pass 3(b) direction 2, UNINVENTORIED) - the sentence that introduces
# the modern techniques ("advanced beyond keeping threatened species in enclosures") had no row.
story.append(b1(
    "In <b>recent years ex situ conservation has advanced beyond keeping threatened species in "
    "enclosures</b>:"))
# F172, F173, F174, F175
story.append(data_table([
    ["Modern ex situ technique", "What it preserves (NCERT)"],
    ["<b>Cryopreservation techniques</b>",
     "<b>gametes of threatened species</b> can now be <b>preserved in viable and fertile "
     "condition for long periods</b>"],
    ["<b>In vitro fertilisation</b>", "<b>eggs can be fertilised in vitro</b>"],
    ["<b>Tissue culture methods</b>", "<b>plants can be propagated</b> using tissue culture"],
    ["<b>Seed banks</b>",
     "<b>seeds of different genetic strains of commercially important plants</b> can be kept for "
     "<b>long periods</b>"],
], col_widths=[3.2, 7.0]))
story.append(gap())
# F176, F177, F178
story.append(b1(
    "<b>Biodiversity knows no political boundaries</b> and its <b>conservation is therefore a "
    "collective responsibility of all nations</b>."))
story.append(process_flow([
    "<b>1992, Rio de Janeiro</b> - the <b>historic Convention on Biological Diversity ('The Earth "
    "Summit')</b> <b>called upon all nations to take appropriate measures for conservation of "
    "biodiversity and sustainable utilisation of its benefits</b>.",
    "<b>2002, Johannesburg, South Africa</b> - in a follow-up, the <b>World Summit on Sustainable "
    "Development</b> saw <b>190 countries</b> pledge their commitment to <b>achieve by 2010 a "
    "significant reduction in the current rate of biodiversity loss at global, regional and local "
    "levels</b>.",
]))

# ======================================================================================
# ---- Quick Recap (§5 item 8 - rewritten, denser version of the NCERT summary) ----
# ======================================================================================
story.append(heading("Recap", "QUICK RECAP", 1))
story.append(b1(
    "<b>Life originated nearly 3.8 billion years ago</b>; since then there has been enormous "
    "diversification of life forms. <b>Biodiversity</b> (term popularised by <b>Edward Wilson</b>) "
    "is the <b>sum total of diversity at all levels of biological organisation</b>; conservation "
    "targets the <b>genetic, species and ecosystem</b> levels."))
story.append(b1(
    "<b>More than 1.5 million species recorded</b> (IUCN 2004); <b>nearly 6 million</b> may still "
    "await discovery, against <b>Robert May's</b> global estimate of about <b>7 million</b> and "
    "extreme estimates of <b>20 to 50 million</b>. <b>More than 70 per cent</b> of named species "
    "are <b>animals</b>, of which <b>more than 70 per cent are insects</b>; <b>plants are no more "
    "than 22 per cent</b>. <b>Fungi</b> outnumber <b>fishes + amphibians + reptiles + mammals</b> "
    "combined (summary: more than <b>all vertebrates</b> combined). <b>Prokaryotes are not "
    "counted</b> in these estimates."))
story.append(b1(
    "<b>India</b>: <b>2.4 per cent of the land area</b>, <b>8.1 per cent of global species "
    "diversity</b>, about <b>45,000 plant species</b> and <b>twice as many animal species</b> - "
    "one of the <b>12 mega diversity countries</b>."))
story.append(b1(
    "<b>Patterns</b>: species diversity is <b>highest in the tropics</b> and <b>decreases towards "
    "the poles</b> - explained by <b>more evolutionary time</b>, a <b>relatively constant, less "
    "seasonal environment</b> promoting <b>niche specialisation</b>, and <b>more solar energy</b> "
    "giving <b>higher productivity</b>. Species richness also rises with <b>area</b> as a "
    "<b>rectangular hyperbola</b>, <b>S = CA<super>Z</super></b>, linear on a log-log scale as "
    "<b>log S = log C + Z log A</b>; <b>Z is 0.1 to 0.2</b> within a region and <b>0.6 to 1.2</b> "
    "across continents (<b>1.15</b> for frugivorous birds and mammals)."))
story.append(b1(
    "<b>Communities with high diversity</b> tend to be <b>less variable, more productive and more "
    "resistant to biological invasions</b> (<b>Tilman</b>'s plots; <b>Ehrlich</b>'s <b>rivet "
    "popper</b> analogy warns that losing <b>key species</b> is worst of all)."))
story.append(b1(
    "<b>Losses</b>: <b>five past mass extinctions</b>; the <b>Sixth Extinction</b> differs "
    "<b>in rate</b> - <b>100 to 1,000 times</b> pre-human rates, with <b>nearly half of all "
    "species</b> possibly gone <b>within 100 years</b>. <b>784 species</b> extinct in <b>500 "
    "years</b> (summary: nearly 700), <b>27</b> in the last twenty years, <b>more than 15,500</b> "
    "threatened (<b>more than 650 in India</b>); <b>12 per cent of birds, 23 per cent of mammals, "
    "32 per cent of amphibians, 31 per cent of gymnosperms</b>."))
story.append(b1(
    "<b>Causes - 'The Evil Quartet'</b>: <b>habitat loss and fragmentation</b> (the most "
    "important; rain forests down from <b>more than 14 per cent</b> to <b>no more than 6 per "
    "cent</b> of land surface), <b>over-exploitation</b> (Steller's sea cow, passenger pigeon), "
    "<b>alien species invasions</b> (Nile perch in Lake Victoria killing more than <b>200 cichlid "
    "species</b>; <i>Parthenium</i>, Lantana, <i>Eicchornia</i>; <i>Clarias gariepinus</i>) and "
    "<b>co-extinctions</b> (host-parasite, plant-pollinator mutualism)."))
story.append(b1(
    "<b>Why conserve</b>: <b>narrowly utilitarian</b> (food, firewood, fibre, industrial products, "
    "medicines - more than <b>25 per cent of drugs</b> plant-derived, <b>25,000 plant species</b> "
    "in traditional medicine, plus <b>bioprospecting</b>), <b>broadly utilitarian</b> (ecosystem "
    "services - the Amazon's <b>20 per cent of atmospheric oxygen</b>, pollination, pest control, "
    "climate moderation, flood control, and aesthetic benefits) and <b>ethical</b> (every species "
    "has <b>intrinsic value</b>; pass the legacy on in good order)."))
story.append(b1(
    "<b>How to conserve</b>: <b>in situ</b> - <b>34 biodiversity hotspots</b> (less than <b>2 per "
    "cent</b> of land area; strict protection could cut mass extinctions by almost <b>30 per "
    "cent</b>), of which <b>three</b> cover India; <b>14 biosphere reserves</b>, <b>90 national "
    "parks</b>, <b>448 wildlife sanctuaries</b> (summary: more than 450) and <b>sacred "
    "groves</b>. <b>Ex situ</b> - <b>zoological parks, botanical gardens, safari parks</b>, "
    "<b>cryopreservation of gametes</b>, <b>in vitro fertilisation</b>, <b>tissue culture</b> and "
    "<b>seed banks</b>. Globally: <b>Rio de Janeiro 1992</b> (Earth Summit) and "
    "<b>Johannesburg 2002</b> (<b>190 countries</b>, target year <b>2010</b>)."))

# ======================================================================================
# ---- Terms used in the exercises (§5 item 9 / Rule 2 - F186-F189) ----
# ======================================================================================
story.append(heading("Appendix", "TERMS USED IN THE EXERCISES", 1))
story.append(body(
    "All <b>10 NCERT exercises</b> were scanned. Six (<b>Q1, Q2, Q3, Q5, Q6, Q7</b>) are fully "
    "answerable from the chapter body. <b>Four</b> assume something the chapter never supplies - "
    "each is closed here."))
story.append(data_table([
    ["Exercise", "What it assumes", "Where it is answered"],
    ["<b>Q4</b>",
     "The <b>significance of the slope (Z) of the regression</b> in a species-area relationship. "
     "The body only asks <b>\"What do steeper slopes mean in this context?\"</b> and never "
     "answers it.",
     "A <b>steeper slope means species richness rises faster per unit area</b>. Whole "
     "<b>continents</b> give <b>Z of 0.6 to 1.2</b> (<b>1.15</b> for frugivorous birds and "
     "mammals), against a shallow <b>Z of 0.1 to 0.2</b> for areas within one region. See the "
     "NOTE at the end of 13.1.2 (ii)."],
    ["<b>Q8</b>",
     "<b>Control of floods and soil erosion</b> as ecosystem services delivered by the "
     "<b>biotic components</b>. <b>Flood control</b> is named only in the chapter summary; "
     "<b>soil erosion</b> is named nowhere in the chapter.",
     "<b>Vegetation cover and root systems bind the soil and slow surface run-off</b>, so water "
     "soaks in rather than sheeting away - checking <b>erosion</b> and moderating <b>floods</b>. "
     "Marked in 13.2.1 as summary-sourced plus necessary inference, not body text."],
    ["<b>Q9</b>",
     "The figure <b>animals 72 per cent</b> against <b>plants 22 per cent</b>. The body says "
     "animals are <b>more than 70 per cent</b>; the exact <b>72 per cent</b> appears only in the "
     "exercise.",
     "Both forms are valid - see the NOTE in 13.1.1. Plant species diversity (<b>22 per cent</b>) "
     "is <b>much less</b> than that of animals (<b>72 per cent</b> in the exercise's wording)."],
    ["<b>Q10</b>",
     "A situation where we <b>deliberately want to make a species extinct</b>, and its "
     "justification. The body offers <b>no content at all</b> on deliberate extinction.",
     "Answered in the <b>MEMORY AID</b> box at the end of 13.1.4, and explicitly marked "
     "<b>not in NCERT</b>: disease-causing organisms such as the <b>smallpox virus</b>, "
     "<b>polio virus</b> and <b>Guinea worm</b>."],
], col_widths=[1.4, 4.6, 5.4]))


def main():
    return build_pdf(OUT_PDF, story, title="Biodiversity and Conservation - NEET Notes")


if __name__ == "__main__":
    raise SystemExit(main())
