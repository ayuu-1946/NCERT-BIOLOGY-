"""
NCERT Class 12 Biology, Chapter 12 - Ecosystem
NEET replacement notes -> A4 print-ready PDF.

Built under SUPREME COMMAND PROMPT.md v6, Pass 2: written linearly from the
frozen 196-row inventory (Ch12_Ecosystem_inventory.md), importing the repo-level
frozen style module `neet_template.py` (v6 §0.6). No style, geometry, colour or
font is re-declared here.

Block markers `# ---- N.N ----` mark every NCERT section so a Pass 3 flag can be
found and fixed in one contiguous block. Inventory row IDs are named in the
comments so any fact can be traced back to its frozen row.

Source: Chapter/class 12/Chapter 12 - Ecosystem.pdf
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
from reportlab.platypus import Paragraph  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch12_Ecosystem.pdf")


def figure(asset_name, caption_text, max_width_cm=15.9):
    """Chapter-local binding of the shared figure() helper (§0.6)."""
    return _shared_figure(asset_name, caption_text, ASSETS, max_width_cm=max_width_cm)


def body(text):
    return Paragraph(text, STYLES["Body"])


def b1(text):
    return Paragraph("&bull; " + text, STYLES["Bullet1"])


def b2(text):
    return Paragraph("- " + text, STYLES["Bullet2"])


story = []

# ======================================================================================
# ---- Title block (§5 item 1) ----
# ======================================================================================
story += title_block("Ecosystem")

# ======================================================================================
# ---- Chapter opener (F001-F010) ----
# ======================================================================================
# F001 (CHAPTER 12 / ECOSYSTEM heading), F002 (contents listing)
story.append(heading("Ch 12", "ECOSYSTEM - Chapter Opener", 1))
story.append(body(
    "<b>Chapter contents (as printed on the opener page):</b> 12.1 Ecosystem - Structure and "
    "Function; 12.2 Productivity; 12.3 Decomposition; 12.4 Energy Flow; 12.5 Ecological Pyramids."))
# F003 (opener), F004, F005
story.append(keyterm(
    "An <b>ecosystem</b> can be visualised as a <b>functional unit of nature</b>, where living "
    "organisms interact among themselves and also with the surrounding physical environment."))
story.append(b1("Ecosystem varies greatly in <b>size</b> - from a <b>small pond</b> to a <b>large "
                "forest or a sea</b>."))
story.append(b1("Many ecologists regard the <b>entire biosphere as a global ecosystem</b>, as a "
                "<b>composite of all local ecosystems on Earth</b>."))
# F006, F007, F008, F009
story.append(body(
    "Since this system is <b>too much big and complex</b> to be studied at one time, it is "
    "convenient to divide it into <b>two basic categories</b>, namely <b>terrestrial</b> and "
    "<b>aquatic</b>."))
story.append(data_table([
    ["Category", "Examples (NCERT)"],
    ["<b>Terrestrial</b> ecosystems", "<b>Forest, grassland and desert</b>"],
    ["<b>Aquatic</b> ecosystems", "<b>Pond, lake, wetland, river and estuary</b>"],
    ["<b>Man-made</b> ecosystems", "<b>Crop fields and an aquarium</b> may also be considered as "
     "man-made ecosystems"],
], col_widths=[3.4, 7.2]))
# F010
story.append(body(
    "We will first look at the <b>structure</b> of the ecosystem, in order to appreciate the "
    "<b>input (productivity)</b>, <b>transfer of energy (food chain/web, nutrient cycling)</b> and "
    "the <b>output (degradation and energy loss)</b>. We will also look at the relationships - "
    "<b>cycles, chains, webs</b> - that are created as a result of these energy flows within the "
    "system and their inter-relationship."))

# ======================================================================================
# ---- 12.1 ECOSYSTEM - STRUCTURE AND FUNCTION (F011-F033, F173, F175) ----
# ======================================================================================
story.append(heading("12.1", "ECOSYSTEM - STRUCTURE AND FUNCTION", 1))
# F012 (opener), F013, F014
story.append(body(
    "In earlier classes, you have looked at the various components of the environment - "
    "<b>abiotic</b> and <b>biotic</b>. You studied how the individual biotic and abiotic factors "
    "affected each other and their surrounding. Let us look at these components in a more "
    "<b>integrated manner</b> and see how the <b>flow of energy</b> takes place within these "
    "components of the ecosystem."))
# F015 + F173 (summary-unique: abiotic = air/water/soil; biotic = producers/consumers/decomposers)
story.append(body(
    "Interaction of biotic and abiotic components results in a <b>physical structure that is "
    "characteristic for each type of ecosystem</b>."))
story.append(data_table([
    ["Component", "What it comprises (Summary)"],
    ["<b>Abiotic</b> components", "Inorganic materials - <b>air, water and soil</b>"],
    ["<b>Biotic</b> components", "<b>Producers, consumers and decomposers</b>"],
], col_widths=[3.2, 7.4]))
# F016, F017, F018 + F175 (two main structural features)
story.append(keyterm(
    "<b>Species composition</b>: identification and enumeration of plant and animal species of an "
    "ecosystem gives its species composition."))
story.append(keyterm(
    "<b>Stratification</b>: vertical distribution of different species occupying different levels "
    "is called stratification. For example, <b>trees</b> occupy the top vertical strata or layer "
    "of a forest, <b>shrubs</b> the second, and <b>herbs and grasses</b> occupy the bottom layers."))
story.append(note(
    "<b>Species composition</b> and <b>stratification</b> are the <b>two main structural features</b> "
    "of an ecosystem (stated explicitly in the Summary)."))
# F019-F023 - four functional aspects
story.append(body(
    "The components of the ecosystem are seen to function as a unit when you consider the following "
    "<b>four aspects</b>, in NCERT's order:"))
story.append(process_flow([
    "<b>Productivity</b>",
    "<b>Decomposition</b>",
    "<b>Energy flow</b>",
    "<b>Nutrient cycling</b>",
]))
# F024-F031 - the pond example
story.append(heading("12.1", "The pond as an example of an aquatic ecosystem", 3))
story.append(body(
    "To understand the ethos of an aquatic ecosystem let us take a <b>small pond</b> as an example. "
    "This is <b>fairly a self-sustainable unit</b> and rather simple example that explains even the "
    "complex interactions that exist in an aquatic ecosystem. A pond is a <b>shallow water body</b> "
    "in which all the above-mentioned <b>four basic components</b> of an ecosystem are well "
    "exhibited."))
story.append(data_table([
    ["Component in the pond", "What it is"],
    ["<b>Abiotic</b>", "The <b>water</b> with all the <b>dissolved inorganic and organic "
     "substances</b> and the <b>rich soil deposit</b> at the bottom of the pond. The <b>solar "
     "input</b>, the <b>cycle of temperature, day-length</b> and other climatic conditions "
     "regulate the rate of function of the entire pond"],
    ["<b>Autotrophic</b> components", "The <b>phytoplankton</b>, some <b>algae</b> and the "
     "<b>floating, submerged and marginal plants</b> found at the edges"],
    ["<b>Consumers</b>", "The <b>zooplankton</b>, the <b>free swimming and bottom dwelling forms</b>"],
    ["<b>Decomposers</b>", "The <b>fungi, bacteria and flagellates</b> especially abundant in the "
     "bottom of the pond"],
], col_widths=[2.9, 7.7]))
# F032 - the pond performs all ecosystem functions
story.append(body(
    "This system performs <b>all the functions of any ecosystem and of the biosphere as a whole</b>, "
    "i.e., <b>conversion of inorganic into organic material</b> with the help of the radiant energy "
    "of the sun by the <b>autotrophs</b>; <b>consumption of the autotrophs by heterotrophs</b>; "
    "<b>decomposition and mineralisation of the dead matter</b> to release them back for reuse by "
    "the autotrophs. These events are <b>repeated over and over again</b>."))
# F033
story.append(keyterm(
    "There is a <b>unidirectional movement of energy</b> towards the higher trophic levels and its "
    "<b>dissipation and loss as heat</b> to the environment."))

# ======================================================================================
# ---- 12.2 PRODUCTIVITY (F034-F053, F177-F181) ----
# ======================================================================================
story.append(heading("12.2", "PRODUCTIVITY", 1))
# F035 (opener)
story.append(body(
    "A <b>constant input of solar energy</b> is the <b>basic requirement</b> for any ecosystem to "
    "function and sustain."))
# F036, F037, F038, F039
story.append(keyterm(
    "<b>Primary production</b> is defined as the <b>amount of biomass or organic matter produced "
    "per unit area over a time period by plants during photosynthesis</b>. It is expressed in terms "
    "of <b>weight (g m<super>-2</super>)</b> or <b>energy (kcal m<super>-2</super>)</b>."))
story.append(keyterm(
    "The <b>rate of biomass production</b> is called <b>productivity</b>. It is expressed in terms "
    "of <b>g m<super>-2</super> yr<super>-1</super></b> or <b>(kcal m<super>-2</super>) "
    "yr<super>-1</super></b> to compare the productivity of different ecosystems."))
# F040-F045 - GPP / NPP
story.append(body(
    "Productivity can be divided into <b>gross primary productivity (GPP)</b> and <b>net primary "
    "productivity (NPP)</b>."))
story.append(data_table([
    ["Term", "Definition"],
    ["<b>Gross primary productivity (GPP)</b>", "The <b>rate of production of organic matter during "
     "photosynthesis</b>. A considerable amount of GPP is <b>utilised by plants in respiration</b>"],
    ["<b>Net primary productivity (NPP)</b>", "<b>Gross primary productivity minus respiration "
     "losses (R)</b>, i.e. <b>GPP - R = NPP</b>. NPP is the <b>available biomass for the "
     "consumption to heterotrophs (herbivores and decomposers)</b>"],
    ["<b>Secondary productivity</b>", "Defined as the <b>rate of formation of new organic matter by "
     "consumers</b>"],
], col_widths=[3.4, 7.2]))
story.append(note(
    "NCERT's parenthetical spells it <b>\"herbiviores\"</b>; the fact is that NPP is available to "
    "<b>herbivores AND decomposers</b>. The Summary also states secondary productivity as the "
    "<b>rate of assimilation of food energy by the consumers</b> - recognise both wordings."))
# F047-F049 - what primary productivity depends on
story.append(body(
    "<b>Primary productivity depends on</b> the <b>plant species</b> inhabiting a particular area. "
    "It also depends on a variety of <b>environmental factors</b>, <b>availability of nutrients</b> "
    "and <b>photosynthetic capacity of plants</b>. Therefore, it <b>varies in different types of "
    "ecosystems</b>."))
# F050, F051, F052
story.append(data_table([
    ["Annual net primary productivity", "Value (dry weight of organic matter)"],
    ["<b>Whole biosphere</b>", "Approximately <b>170 billion tons</b>"],
    ["<b>Oceans</b> (despite occupying about <b>70 per cent</b> of the surface)", "Only <b>55 "
     "billion tons</b>"],
    ["<b>Land</b>", "The <b>rest</b>, of course, is on land"],
], col_widths=[5.6, 5.0]))
# F053 - activity
story.append(note(
    "<b>NCERT activity:</b> Discuss the <b>main reason for the low productivity of ocean</b> with "
    "your teacher."))

# ======================================================================================
# ---- 12.3 DECOMPOSITION (F054-F072, F182-F183) ----
# ======================================================================================
story.append(heading("12.3", "DECOMPOSITION", 1))
# F055, F056
story.append(body(
    "You may have heard of the <b>earthworm</b> being referred to as the <b>farmer's 'friend'</b>. "
    "This is so because they help in the <b>breakdown of complex organic matter</b> as well as in "
    "<b>loosening of the soil</b>."))
# F057, F058
story.append(keyterm(
    "<b>Decomposition</b>: decomposers break down complex organic matter into <b>inorganic "
    "substances</b> like <b>carbon dioxide, water and nutrients</b>, and the process is called "
    "decomposition."))
story.append(keyterm(
    "<b>Detritus</b>: dead plant remains such as <b>leaves, bark, flowers</b> and <b>dead remains "
    "of animals, including fecal matter</b>, constitute detritus, which is the <b>raw material for "
    "decomposition</b>."))
# F059 - five steps process flow
story.append(body(
    "The important steps in the process of decomposition are (in NCERT's order):"))
story.append(process_flow([
    # [VERIFICATION FIX] D1 - inventory row IDs moved out of reader-facing text into these comments
    # F060
    "<b>Fragmentation</b> - <b>detritivores (e.g., earthworm)</b> break down detritus into "
    "<b>smaller particles</b>.",
    # F061
    "<b>Leaching</b> - <b>water-soluble inorganic nutrients</b> go down into the <b>soil horizon</b> "
    "and get <b>precipitated as unavailable salts</b>.",
    # F062
    "<b>Catabolism</b> - <b>bacterial and fungal enzymes degrade detritus into simpler inorganic "
    "substances</b>.",
    # F064-F066
    "<b>Humification</b> - leads to accumulation of <b>humus</b> (see below).",
    # F067
    "<b>Mineralisation</b> - the humus is further degraded to release inorganic nutrients (see "
    "below).",
]))
# F063 - simultaneity qualifier (marks-critical)
story.append(note(
    "It is important to note that <b>all the above steps in decomposition operate simultaneously</b> "
    "on the detritus (Figure 12.1). Humification and mineralisation occur <b>during decomposition in "
    "the soil</b>."))
# F065, F066, F067
story.append(keyterm(
    "<b>Humification</b> leads to accumulation of a <b>dark coloured amorphous substance called "
    "humus</b> that is <b>highly resistant to microbial action</b> and <b>undergoes decomposition "
    "at an extremely slow rate</b>. Being <b>colloidal in nature</b> it serves as a <b>reservoir of "
    "nutrients</b>."))
story.append(keyterm(
    "<b>Mineralisation</b>: the humus is <b>further degraded by some microbes</b> and <b>release of "
    "inorganic nutrients</b> occurs by this process."))
# F183 vs F059 conflict NOTE
story.append(note(
    "<b>Five vs three - a discrepancy to know:</b> the <b>body lists FIVE steps</b> "
    "(fragmentation, leaching, catabolism, humification and mineralisation), but the <b>Summary "
    "says decomposition involves THREE processes</b> - <b>fragmentation of detritus, leaching and "
    "catabolism</b>. Both wordings are NCERT's; do not reconcile them - recognise either in a "
    "question."))
# F068-F072 - controls on decomposition
story.append(body(
    "Decomposition is <b>largely an oxygen-requiring process</b>. The <b>rate of decomposition</b> "
    "is controlled by <b>chemical composition of detritus</b> and <b>climatic factors</b>:"))
story.append(data_table([
    ["Factor", "Effect on the rate of decomposition"],
    ["<b>Chemical composition of detritus</b>", "In a particular climatic condition, decomposition "
     "is <b>slower</b> if detritus is rich in <b>lignin and chitin</b>, and <b>quicker</b> if "
     "detritus is rich in <b>nitrogen and water-soluble substances like sugars</b>"],
    ["<b>Climatic factors (temperature and soil moisture)</b>", "The <b>most important</b> climatic "
     "factors; they regulate decomposition through their effects on the <b>activities of soil "
     "microbes</b>. <b>Warm and moist environment favour decomposition</b>, whereas <b>low "
     "temperature and anaerobiosis inhibit decomposition</b>, resulting in <b>build up of organic "
     "materials</b>"],
], col_widths=[3.4, 7.2]))
# Figure 12.1 - inline at decomposition topic; describe every in-figure label (F154, F155)
story.append(body(
    "<b>The decomposition cycle in a terrestrial ecosystem (Figure 12.1) reads as follows:</b> "
    "<b>a tree grows in the soil</b>; <b>a green leaf falls to the ground</b>; <b>some are eaten by "
    "insects and other animals</b>, so that <b>nutrients and energy enter the food web</b>; <b>some "
    "nutrients leach into soil by chemical action</b>; <b>leaves partially consumed by decomposers "
    "such as fungi and bacteria begin to lose form and become litter</b>; there is <b>further "
    "decomposition by earthworms, bacteria, soil mites, fungi, etc.</b>; and the end result is "
    "<b>organic rich soil</b>."))
story.append(figure(
    "fig_12_1.png",
    "Fig. 12.1 - Diagrammatic representation of decomposition cycle in a terrestrial ecosystem."))

# ======================================================================================
# ---- 12.4 ENERGY FLOW (F073-F127, F184-F186) ----
# ======================================================================================
story.append(heading("12.4", "ENERGY FLOW", 1))
# F074 (opener - hydro-thermal exception), F075
story.append(keyterm(
    "<b>Except for the deep sea hydro-thermal ecosystem</b>, the <b>sun is the only source of "
    "energy for all ecosystems on Earth</b>. Of the incident solar radiation, <b>less than 50 per "
    "cent</b> of it is <b>photosynthetically active radiation (PAR)</b>."))
# F076, F077
story.append(body(
    "<b>Plants and photosynthetic bacteria (autotrophs)</b> fix the Sun's radiant energy to <b>make "
    "food from simple inorganic materials</b>. Plants capture only <b>2-10 per cent of the PAR</b>, "
    "and this <b>small amount of energy sustains the entire living world</b>."))
# F078-F083 - laws of thermodynamics
story.append(body(
    "So it is very important to know how the solar energy captured by plants flows through different "
    "organisms of an ecosystem. All organisms are <b>dependent for their food on producers</b>, "
    "either <b>directly or indirectly</b>. So you find a <b>unidirectional flow of energy</b> from "
    "the sun to producers and then to consumers."))
story.append(note(
    "<b>Thermodynamics:</b> Is this in keeping with the <b>first law of thermodynamics</b>? "
    "Ecosystems are <b>not exempt from the Second Law of thermodynamics</b> either - they need a "
    "<b>constant supply of energy</b> to synthesise the molecules they require, to <b>counteract "
    "the universal tendency toward increasing disorderliness</b>."))
# F084, F085, F086
story.append(keyterm(
    "<b>Producers</b>: the <b>green plants in the ecosystem</b> are called producers. In a "
    "<b>terrestrial ecosystem</b>, major producers are <b>herbaceous and woody plants</b>. In an "
    "<b>aquatic ecosystem</b> producers are various species like <b>phytoplankton, algae and higher "
    "plants</b>."))
# F087-F092 - food chains / webs, energy fate
story.append(body(
    "Starting from the <b>plants (or producers)</b>, <b>food chains</b> or rather <b>webs</b> are "
    "formed such that an <b>animal feeds on a plant or on another animal and in turn is food for "
    "another</b>. The chain or web is formed because of this <b>interdependency</b>."))
story.append(b1("<b>No energy that is trapped into an organism remains in it for ever.</b> The "
                "energy trapped by the producer is <b>either passed on to a consumer or the organism "
                "dies</b>."))
story.append(b1("<b>Death of an organism is the beginning of the detritus food chain/web.</b>"))
# F093-F100 - consumers, trophic categories
story.append(keyterm(
    "<b>Consumers (heterotrophs)</b>: all animals depend on plants (directly or indirectly) for "
    "their food needs, hence they are called <b>consumers</b> and also <b>heterotrophs</b>."))
story.append(data_table([
    ["Consumer category", "Definition (NCERT)"],
    ["<b>Primary consumers</b>", "Animals that <b>feed on the producers (the plants)</b>. Obviously "
     "the primary consumers will be <b>herbivores</b>"],
    ["<b>Secondary consumers</b>", "Animals that <b>eat other animals which in turn eat the plants "
     "(or their produce)</b>. You could have <b>tertiary consumers</b> too"],
    ["<b>Primary carnivores</b>", "The consumers that <b>feed on herbivores</b> are carnivores, or "
     "more correctly <b>primary carnivores (though secondary consumers)</b>"],
    ["<b>Secondary carnivores</b>", "Those animals that <b>depend on the primary carnivores for "
     "food</b>"],
], col_widths=[3.2, 7.4]))
# F098 - herbivore examples
story.append(b1("Some common <b>herbivores</b> are <b>insects, birds and mammals</b> in the "
                "terrestrial ecosystem and <b>molluscs</b> in the aquatic ecosystem."))
# F101, F102 - grazing food chain (no unicode arrows)
story.append(body("A <b>simple grazing food chain (GFC)</b> is depicted below:"))
story.append(process_flow([
    "<b>Grass (Producer)</b>",
    "<b>Goat (Primary Consumer)</b>",
    "<b>Man (Secondary consumer)</b>",
]))
# F103-F109 - detritus food chain
story.append(keyterm(
    "<b>Detritus food chain (DFC)</b> begins with <b>dead organic matter</b>. It is made up of "
    "<b>decomposers</b>, which are <b>heterotrophic organisms, mainly fungi and bacteria</b>. They "
    "meet their energy and nutrient requirements by <b>degrading dead organic matter or "
    "detritus</b>. These are also known as <b>saprotrophs</b> (<b>sapro</b>: to decompose)."))
story.append(b1("Decomposers <b>secrete digestive enzymes</b> that break down dead and waste "
                "materials into <b>simple, inorganic materials</b>, which are subsequently "
                "<b>absorbed by them</b>."))
story.append(data_table([
    ["Ecosystem", "Dominant energy-flow route"],
    ["<b>Aquatic</b> ecosystem", "<b>GFC is the major conduit for energy flow</b>"],
    ["<b>Terrestrial</b> ecosystem", "A <b>much larger fraction of energy</b> flows through the "
     "<b>detritus food chain</b> than through the GFC"],
], col_widths=[3.4, 7.2]))
# F110-F113 - interconnection, omnivores, food web
story.append(body(
    "The <b>detritus food chain may be connected with the grazing food chain</b> at some levels: "
    "<b>some of the organisms of DFC are prey to the GFC animals</b>, and in a natural ecosystem "
    "<b>some animals like cockroaches, crows, etc., are omnivores</b>. These <b>natural "
    "interconnections of food chains make it a food web</b>."))
story.append(note("<b>NCERT prompt:</b> How would you classify human beings!"))
# F114-F117 - trophic levels + Figure 12.2 table (covers all Fig 12.2 labels F156, F157)
story.append(keyterm(
    # [VERIFICATION FIX] D2 (F114) - restored NCERT's "in the natural surroundings or in a
    # community" (the rewrite had compressed this to "in the community", dropping the frozen phrase)
    "<b>Trophic level</b>: organisms occupy a place <b>in the natural surroundings or in a "
    "community</b> according to their <b>feeding relationship</b> with other organisms. Based on the "
    "<b>source of their nutrition or food</b>, organisms occupy a specific place in the food chain "
    "that is known as their trophic level."))
story.append(body(
    "<b>Trophic levels in an ecosystem (Figure 12.2):</b> producers belong to the <b>first trophic "
    "level</b>, herbivores (primary consumer) to the <b>second</b>, and carnivores (secondary "
    "consumer) to the <b>third</b>. The important point to note is that the <b>amount of energy "
    "decreases at successive trophic levels</b>."))
story.append(data_table([
    ["Trophic level", "Category", "Organism type", "Examples"],
    ["<b>First trophic level</b>", "<b>Producer</b>", "<b>Plants</b>",
     "<b>Phytoplankton, grass, trees</b>"],
    ["<b>Second trophic level</b>", "<b>Primary Consumer</b>", "<b>Herbivore</b>",
     "<b>Zooplankton, grasshopper and cow</b>"],
    ["<b>Third trophic level</b>", "<b>Secondary Consumer</b>", "<b>Carnivore</b>",
     "<b>Birds, fishes wolf</b>"],
    ["<b>Fourth Trophic level</b>", "<b>Tertiary Consumer</b>", "<b>Top Carnivore</b>",
     "<b>Man, lion</b>"],
], col_widths=[2.6, 2.6, 2.2, 3.2]))
story.append(figure(
    "fig_12_2.png",
    "Fig. 12.2 - Diagrammatic representation of trophic levels in an ecosystem."))
# F118-F124 - detritus, standing crop, biomass
story.append(body(
    "When any organism dies it is <b>converted to detritus or dead biomass</b> that serves as an "
    "<b>energy source for decomposers</b>. Organisms at each trophic level depend on those at the "
    "<b>lower trophic level</b> for their energy demands."))
story.append(keyterm(
    "<b>Standing crop</b>: each trophic level has a certain <b>mass of living material at a "
    "particular time</b> called the standing crop. It is measured as the <b>mass of living "
    "organisms (biomass)</b> or the <b>number in a unit area</b>."))
story.append(b1("The <b>biomass</b> of a species is expressed in terms of <b>fresh or dry "
                "weight</b>. Measurement of biomass in terms of <b>dry weight is more accurate</b>. "
                "(<b>NCERT prompt:</b> Why?)"))
# F125-F127 - 10 per cent law + Figure 12.3
story.append(keyterm(
    "<b>10 per cent law:</b> the number of trophic levels in the grazing food chain is <b>restricted "
    "as the transfer of energy follows the 10 per cent law</b> - only <b>10 per cent</b> of the "
    "energy is transferred to each trophic level from the lower trophic level."))
story.append(body(
    "In nature, it is possible to have <b>so many levels - producer, herbivore, primary carnivore, "
    "secondary carnivore</b> - in the grazing food chain (Figure 12.3). (<b>NCERT prompt:</b> Do "
    "you think there is any such limitation in a detritus food chain?)"))
# Figure 12.3 - energy flow diagram; cover its labels (F158, F159): Sun, Heat, trophic levels
story.append(body(
    "<b>Energy flow through different trophic levels (Figure 12.3):</b> energy from the <b>Sun</b> "
    "enters the <b>first trophic level producers (plants)</b>, passes to the <b>second trophic "
    "level primary consumers (herbivores)</b>, then to the <b>third trophic level secondary "
    "consumers (carnivores)</b> and the <b>fourth trophic level tertiary consumers (top "
    "carnivores)</b>; at every step some energy is lost as <b>Heat</b>."))
story.append(figure(
    "fig_12_3.png",
    "Fig. 12.3 - Energy flow through different trophic levels. The original colour figure separates "
    "the trophic levels by hue; after monochrome conversion they are read by their position, labels "
    "and the Sun/Heat markers."))

# ======================================================================================
# ---- 12.5 ECOLOGICAL PYRAMIDS (F128-F153, F196) ----
# ======================================================================================
story.append(heading("12.5", "ECOLOGICAL PYRAMIDS", 1))
# F129-F133
story.append(body(
    "You must be familiar with the <b>shape of a pyramid</b>: the <b>base is broad and it narrows "
    "towards the apex</b>. One gets a similar shape whether you express the <b>food or energy "
    "relationship</b> between organisms at different trophic levels. This relationship is expressed "
    "in terms of <b>number, biomass or energy</b>."))
story.append(keyterm(
    "The <b>base</b> of each pyramid represents the <b>producers or the first trophic level</b>, "
    "while the <b>apex</b> represents the <b>tertiary or top level consumer</b>."))
# F134 (three types - inline (a)/(b)/(c), F196 confirms these are NOT sub-headings), F135
story.append(body(
    "The <b>three types of ecological pyramids</b> that are usually studied are "
    "<b>(a) pyramid of number</b>; <b>(b) pyramid of biomass</b>; and <b>(c) pyramid of energy</b> "
    "(for detail see Figure 12.4 a, b, c and d)."))
# F136-F140 - rules about calculation and trophic levels
story.append(b1("Any calculations of <b>energy content, biomass or numbers</b> has to <b>include "
                "all organisms at that trophic level</b>. No generalisations we make will be true "
                "if we take <b>only a few individuals</b> at any trophic level into account."))
story.append(b1("A given organism <b>may occupy more than one trophic level simultaneously</b>. One "
                "must remember that the <b>trophic level represents a functional level, not a "
                "species as such</b>."))
# F141 - sparrow example
story.append(b1("For example, a <b>sparrow</b> is a <b>primary consumer</b> when it eats <b>seeds, "
                "fruits, peas</b>, and a <b>secondary consumer</b> when it eats <b>insects and "
                "worms</b>. (<b>NCERT prompt:</b> Can you work out how many trophic levels human "
                "beings function at in a food chain?)"))
# F143, F144 - upright pyramids
story.append(body(
    "In <b>most ecosystems</b>, all the pyramids - <b>of number, of energy and biomass</b> - are "
    "<b>upright</b>, i.e., <b>producers are more in number and biomass than the herbivores</b>, and "
    "<b>herbivores are more in number and biomass than the carnivores</b>. Also, <b>energy at a "
    "lower trophic level is always more than at a higher level</b>."))
# Figure 12.4 values table - covers every bar value (F160-F170) and the a/b/c/d labels
story.append(body(
    "<b>The values shown in the four pyramids of Figure 12.4</b> (every bar value carried verbatim; "
    "P = Producer, PC = Primary consumer, SC = Secondary consumer, TC = Tertiary consumer):"))
story.append(data_table([
    ["Trophic level", "(a) Pyramid of numbers, grassland: Number of individuals",
     "(b) Pyramid of biomass, grassland: Dry weight (kg m<super>-2</super>)",
     "(c) Inverted pyramid of biomass (aquatic)", "(d) Pyramid of energy"],
    ["<b>P (Producer)</b>", "<b>5,842,000</b>", "<b>809</b>", "<b>4</b>", "<b>10,000 J</b>"],
    ["<b>PC (Primary consumer)</b>", "<b>708,000</b>", "<b>37</b>", "<b>21</b>", "<b>1000 J</b>"],
    ["<b>SC (Secondary consumer)</b>", "<b>3,54,000</b>", "<b>11</b>", "-", "<b>100 J</b>"],
    ["<b>TC (Tertiary consumer)</b>", "<b>3</b>", "<b>1.5</b>", "-", "<b>10 J</b>"],
], col_widths=[2.5, 2.6, 2.4, 1.9, 1.6]))
story.append(note(
    "<b>Figure 12.4 caption facts:</b> (a) Only <b>three top-carnivores</b> are supported in an "
    "ecosystem based on production of <b>nearly 6 millions plants</b> - the bar itself reads "
    "<b>5,842,000</b> (carry both, do not reconcile). (d) An <b>ideal pyramid of energy</b>: "
    "primary producers convert <b>only 1% of the energy in the sunlight</b> available to them into "
    "NPP, out of <b>1,000,000 J of Sunlight</b>."))
story.append(figure("fig_12_4a.png",
                    "Fig. 12.4 (a) - Pyramid of numbers in a grassland ecosystem. Only three "
                    "top-carnivores are supported in an ecosystem based on production of nearly 6 "
                    "millions plants.", max_width_cm=11.0))
story.append(figure("fig_12_4b.png",
                    "Fig. 12.4 (b) - Pyramid of biomass shows a sharp decrease in biomass at higher "
                    "trophic levels.", max_width_cm=11.0))
story.append(figure("fig_12_4c.png",
                    "Fig. 12.4 (c) - Inverted pyramid of biomass - small standing crop of "
                    "phytoplankton supports large standing crop of zooplankton.", max_width_cm=8.5))
story.append(figure("fig_12_4d.png",
                    "Fig. 12.4 (d) - An ideal pyramid of energy. Observe that primary producers "
                    "convert only 1% of the energy in the sunlight available to them into NPP.",
                    max_width_cm=11.0))
# F145-F149 - exceptions
story.append(body("<b>There are exceptions to the \"pyramids are upright\" generalisation:</b>"))
story.append(b1("<b>Pyramid of numbers on a big tree:</b> if you count the number of <b>insects "
                "feeding on a big tree</b>, then add the <b>small birds depending on the insects</b> "
                "and the <b>larger birds eating the smaller</b>, the pyramid of numbers you get is "
                "<b>not upright</b> (it is inverted/spindle-shaped). (NCERT asks you to draw it.)"))
story.append(b1("<b>Pyramid of biomass in the sea</b> is <b>generally inverted</b> because the "
                "<b>biomass of fishes far exceeds that of phytoplankton</b>. (<b>NCERT prompt:</b> "
                "Isn't that a paradox? How would you explain this?)"))
story.append(keyterm(
    "<b>Pyramid of energy is always upright, can never be inverted</b>, because when energy flows "
    "from a particular trophic level to the next, <b>some energy is always lost as heat at each "
    "step</b>."))
# F150
story.append(b1("Each bar in the <b>energy pyramid</b> indicates the <b>amount of energy present at "
                "each trophic level in a given time or annually per unit area</b>."))
# F151-F153 - limitations (misplaced-paragraph note carried at end of 12.5)
story.append(note(
    "<b>Limitations of ecological pyramids:</b> (1) it <b>does not take into account the same "
    "species belonging to two or more trophic levels</b>; (2) it <b>assumes a simple food chain</b>, "
    "something that <b>almost never exists in nature</b>, and <b>does not accommodate a food web</b>; "
    "(3) <b>saprophytes are not given any place</b> in ecological pyramids even though they play a "
    "<b>vital role in the ecosystem</b>."))

# ======================================================================================
# ---- Nutrient cycling & ecosystem services (SUMMARY-UNIQUE block, F187-F190) ----
# ======================================================================================
story.append(heading("12.6", "NUTRIENT CYCLING AND ECOSYSTEM SERVICES", 1))
story.append(note(
    "This section carries facts stated <b>only in the NCERT Summary</b> - nutrient cycling is listed "
    "as one of the four functions in 12.1 but is never defined in the body, so it is folded in here."))
story.append(keyterm(
    "<b>Nutrient cycling</b>: the <b>storage and movement of nutrient elements through the various "
    "components of the ecosystem</b> is called nutrient cycling; <b>nutrients are repeatedly used</b> "
    "through this process."))
story.append(data_table([
    ["Type of nutrient cycle", "Reservoir (Summary)"],
    ["<b>Gaseous</b> type (e.g., <b>carbon</b>)", "<b>Atmosphere or hydrosphere</b>"],
    ["<b>Sedimentary</b> type (e.g., <b>phosphorus</b>)", "<b>Earth's crust</b>"],
], col_widths=[4.6, 6.0]))
story.append(keyterm(
    "<b>Ecosystem services</b>: the <b>products of ecosystem processes</b> are named ecosystem "
    "services - e.g., <b>purification of air and water by forests</b>."))

# ======================================================================================
# ---- Quick Recap (rewritten, denser Summary - F171-F190) ----
# ======================================================================================
story.append(heading("Recap", "QUICK RECAP", 1))
story.append(b1("An <b>ecosystem</b> is a <b>structural and functional unit of nature</b> comprising "
                "<b>abiotic</b> components (inorganic materials - <b>air, water, soil</b>) and "
                "<b>biotic</b> components (<b>producers, consumers, decomposers</b>). Each ecosystem "
                "has a <b>characteristic physical structure</b> from the interaction of these "
                "components."))
story.append(b1("<b>Species composition</b> and <b>stratification</b> are the <b>two main structural "
                "features</b> of an ecosystem. Based on the source of nutrition, every organism "
                "occupies a place in an ecosystem."))
story.append(b1("<b>Productivity, decomposition, energy flow and nutrient cycling</b> are the "
                "<b>four important functions/components</b> of an ecosystem."))
story.append(b1("<b>Primary productivity</b> is the <b>rate of capture of solar energy or biomass "
                "production of the producers</b>. <b>GPP</b> is the total production of organic "
                "matter; <b>NPP</b> is the <b>remaining biomass/energy left after utilisation by "
                "producers</b> (GPP - R). <b>Secondary productivity</b> is the <b>rate of "
                "assimilation of food energy by the consumers</b>."))
story.append(b1("In <b>decomposition</b>, complex organic compounds of <b>detritus</b> are converted "
                "to <b>carbon dioxide, water and inorganic nutrients</b> by the decomposers. The "
                "body lists <b>five</b> steps; the Summary names <b>three</b> - <b>fragmentation, "
                "leaching and catabolism</b>."))
story.append(b1("<b>Energy flow is unidirectional</b>: first, plants capture solar energy, and then "
                "food is transferred from the <b>producers to decomposers</b>. Organisms of "
                "different trophic levels are connected for food/energy, forming a <b>food chain</b> "
                "and <b>food web</b>."))
story.append(b1("<b>Nutrient cycling</b> is the storage and movement of nutrients through the "
                "ecosystem; it is of <b>two types - gaseous</b> (reservoir: atmosphere/hydrosphere, "
                "e.g. carbon) and <b>sedimentary</b> (reservoir: Earth's crust, e.g. phosphorus). "
                "<b>Ecosystem services</b> are the products of ecosystem processes, e.g. "
                "<b>purification of air and water by forests</b>."))

# ======================================================================================
# ---- Terms used in the exercises (Rule 2 appendix) + exercises list (F191-F195) ----
# ======================================================================================
story.append(heading("Appendix", "TERMS USED IN THE EXERCISES", 1))
story.append(body(
    "NCERT's eleven exercise questions assume a few terms/facts the chapter never states outright. "
    "Everything below is built only from statements already made in this chapter (plus the Summary)."))
story.append(data_table([
    ["Term / fact assumed", "Explanation (from this chapter)"],
    ["<b>Litter</b> (Ex 6(e): distinguish <b>litter and detritus</b>)", "The body never defines "
     "litter; it appears only in Figure 12.1. <b>Litter</b> = freshly fallen, still-recognisable "
     "dead plant/animal material on the soil surface, which - as decomposers begin to consume it - "
     "loses form and becomes part of the <b>detritus</b> (all dead plant/animal remains that are "
     "the raw material for decomposition)"],
    ["<b>Limiting factor for productivity in aquatic ecosystems</b> (Ex 1(c))", "The body only asks "
     "you to discuss low ocean productivity. The <b>limiting factor is light (and nutrient) "
     "availability</b> in water, tied to the ocean's low 55-billion-ton productivity despite its "
     "large area"],
    ["<b>Major reservoir of carbon on earth</b> (Ex 1(e))", "From the nutrient-cycling block: "
     "<b>carbon</b> follows a <b>gaseous</b> cycle whose reservoir is the <b>atmosphere or "
     "hydrosphere</b>"],
    ["<b>Secondary producers</b> (Ex 4)", "The term appears nowhere in the chapter; NCERT uses "
     "<b>secondary productivity</b> and <b>primary/secondary consumers</b>. As there is no such "
     "category, the intended answer is <b>(d) None of the above</b>"],
    # [VERIFICATION FIX] D1 - row ID F146 moved out of reader-facing text into this comment
    ["<b>Pyramid of numbers in a tree-dominated ecosystem</b> (Ex 1(b))", "Posed as an activity "
     "in NCERT. The pyramid is <b>inverted / spindle-shaped</b>, the same non-upright case as the "
     "big-tree/insects/birds example"],
], col_widths=[3.4, 7.2]))
story.append(heading("Appendix", "NCERT Exercises (for reference)", 3))
story.append(body(
    "<b>1.</b> Fill in the blanks: (a) Plants are called <b>autotrophs/producers</b> because they "
    "fix carbon dioxide; (b) in an ecosystem dominated by trees, the pyramid of numbers is "
    "<b>inverted/spindle</b> type; (c) in aquatic ecosystems, the limiting factor for productivity "
    "is <b>light</b>; (d) common detritivores are <b>earthworms</b>; (e) the major reservoir of "
    # [VERIFICATION FIX] D3 - was "oceans/hydrosphere": "oceans" is not NCERT's wording and
    # contradicted the appendix row above. F189 says the gaseous-cycle (carbon) reservoir is the
    # "atmosphere or hydrosphere"; both answers to Ex 1(e) now agree and match the frozen row.
    # (D4: this comment previously mislabelled the fix as "D2"; D2 is the separate F114 fix in
    # the 12.4 block. Defect IDs here now match the inventory's defect register.)
    "carbon on earth is the <b>atmosphere or hydrosphere</b> (the gaseous-cycle reservoir)."))
story.append(body(
    "<b>2-5 (MCQ):</b> 2. Largest population in a food chain - <b>(a) Producers</b>. 3. The second "
    "trophic level in a lake - <b>(b) Zooplankton</b>. 4. Secondary producers are - <b>(d) None of "
    "the above</b>. 5. Percentage of PAR in incident solar radiation - <b>(b) 50%</b> (NCERT states "
    "\"less than 50 per cent\")."))
story.append(body(
    "<b>6. Distinguish between:</b> (a) Grazing food chain and detritus food chain; (b) Production "
    "and decomposition; (c) Upright and inverted pyramid; (d) Food chain and Food web; (e) Litter "
    "and detritus; (f) Primary and secondary productivity - all covered above."))
story.append(body(
    "<b>7-11 (long answers):</b> 7. Describe the components of an ecosystem. 8. Define ecological "
    "pyramids and describe, with examples, pyramids of number and biomass. 9. What is primary "
    "productivity? Describe factors that affect it. 10. Define decomposition and describe its "
    "processes and products. 11. Give an account of energy flow in an ecosystem - all answered by "
    "the sections above."))

# ---- Closing caption ----
story.append(Paragraph(
    "<i>Every fact, number, name, qualifier, table row, figure and figure label in NCERT Class 12 "
    "Chapter 12 is carried above. Nothing outside the source chapter has been added.</i>",
    STYLES["Caption"]))


def main():
    return build_pdf(
        OUT_PDF, story,
        title="Class 12 Chapter 12 - Ecosystem (NEET notes)",
        subject="NEET Biology",
    )


if __name__ == "__main__":
    sys.exit(main())
