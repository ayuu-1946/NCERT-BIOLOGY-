"""
NCERT Class 12 Biology, Chapter 11 - Organisms and Populations
NEET replacement notes -> A4 print-ready PDF.

Built under SUPREME COMMAND PROMPT.md v6, Pass 2: written linearly from the
frozen 268-row inventory (Ch11_OrganismsAndPopulations_inventory.md), importing
the repo-level frozen style module `neet_template.py` (v6 §0.6). No style,
geometry, colour or font is re-declared here.

Block markers `# ---- N.N ----` mark every NCERT section so a Pass 3 flag can be
found and fixed in one contiguous block. Inventory row IDs are named in the
comments so any fact can be traced back to its frozen row.

Source: Chapter/class 12/Chapter 11 - Organisms and Populations.pdf
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
    STYLES, FRAME_WIDTH, DARK_GREY, GRID_LINE,
    heading, keyterm, process_flow, note, memory_aid, data_table, title_block, build_pdf,
)
from neet_template import figure as _shared_figure  # noqa: E402
from reportlab.platypus import Paragraph, Spacer, KeepTogether  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch11_OrganismsAndPopulations.pdf")


def figure(asset_name, caption_text, max_width_cm=15.9):
    """Chapter-local binding of the shared figure() helper (§0.6)."""
    return _shared_figure(asset_name, caption_text, ASSETS, max_width_cm=max_width_cm)


def body(text):
    return Paragraph(text, STYLES["Body"])


def b1(text):
    return Paragraph("&bull; " + text, STYLES["Bullet1"])


def b2(text):
    return Paragraph("- " + text, STYLES["Bullet2"])


def b3(text):
    return Paragraph("* " + text, STYLES["Bullet3"])


story = []

# ======================================================================================
# ---- Title block (§5 item 1) ----
# ======================================================================================
story += title_block("Organisms and Populations")

# ======================================================================================
# ---- Unit X opener (F001-F010) ----
# ======================================================================================
story.append(heading("Unit X", "ECOLOGY - Unit Introduction", 1))
story.append(body(
    "Diversity is not only a characteristic of living organisms but also of content in "
    "biology textbooks. Biology is presented either as <b>botany, zoology and microbiology</b> "
    "or as <b>classical and modern</b>; the latter is a euphemism for molecular aspects of "
    "biology. Luckily we have many threads which weave the different areas of biological "
    "information into a unifying principle, and <b>ecology</b> is one such thread - it gives "
    "us a holistic perspective to biology."))
story.append(body(
    "The essence of biological understanding is to know how organisms, while remaining an "
    "individual, interact with other organisms and physical habitats as a group and hence "
    "behave like organised wholes, i.e., <b>population, community, ecosystem</b> or even as "
    "the whole <b>biosphere</b>. Ecology explains to us all this. A particular aspect of this "
    "is the study of anthropogenic environmental degradation and the socio-political issues "
    "it has raised. This unit describes as well as takes a critical view of the above aspects."))
story.append(b1("Unit X (ten) - <b>ECOLOGY</b> - contains three chapters: Chapter 11 "
                "<i>Organisms and Populations</i>; Chapter 12 <i>Ecosystem</i>; Chapter 13 "
                "<i>Biodiversity and Conservation</i>."))

# ======================================================================================
# ---- Scientist profile: RAMDEO MISRA (F011-F022) - TEXT ONLY, no photograph (§4.4) ----
# ======================================================================================
story.append(heading("Profile", "RAMDEO MISRA (1908-1998)", 2))
story.append(b1("<b>Ramdeo Misra is revered as the Father of Ecology in India.</b> Born on "
                "<b>26 August 1908</b>; dates <b>1908-1998</b>."))
story.append(b1("Obtained <b>Ph.D in Ecology (1937)</b> under Prof. <b>W. H. Pearsall, FRS</b>, "
                "from <b>Leeds University</b> in UK."))
story.append(b1("Established teaching and research in ecology at the <b>Department of Botany "
                "of the Banaras Hindu University, Varanasi</b>."))
story.append(b1("His research laid the foundations for understanding of <b>tropical communities "
                "and their succession</b>, <b>environmental responses of plant populations</b> and "
                "<b>productivity and nutrient cycling in tropical forest and grassland "
                "ecosystems</b>."))
story.append(b1("Formulated the <b>first postgraduate course in ecology in India</b>."))
story.append(b1("<b>Over 50 scholars</b> obtained Ph. D degree under his supervision and moved "
                "on to other universities and research institutes to initiate ecology teaching "
                "and research across the country."))
story.append(b1("Honoured with the Fellowships of the <b>Indian National Science Academy</b> and "
                "<b>World Academy of Arts and Science</b>, and the prestigious <b>Sanjay Gandhi "
                "Award in Environment and Ecology</b>."))
story.append(b1("Due to his efforts, the Government of India established the <b>National "
                "Committee for Environmental Planning and Coordination (1972)</b>, which in later "
                "years paved the way for the establishment of the <b>Ministry of Environment and "
                "Forests (1984)</b>."))

# ======================================================================================
# ---- Chapter opener (F023-F031, F030a) ----
# ======================================================================================
story.append(heading("Ch 11", "ORGANISMS AND POPULATIONS - Chapter Opener", 1))
story.append(body(
    "Our living world is fascinatingly diverse and amazingly complex. We can try to understand "
    "its complexity by investigating processes at various levels of biological organisation - "
    "<b>macromolecules, cells, tissues, organs, individual organisms, population, communities, "
    "ecosystems and biomes</b>."))
story.append(body(
    "At any level of biological organisation we can ask <b>two types of questions</b>. When we "
    "hear the bulbul singing early morning in the garden, we may ask <i>'How does the bird "
    "sing?'</i> or <i>'Why does the bird sing?'</i>"))
story.append(data_table([
    ["Question type", "What it seeks", "Answer for the singing bulbul"],
    ["<b>'How-type'</b>", "The <b>mechanism</b> behind the process",
     "For the first question, the answer <b>might</b> be in terms of the operation of the "
     "<b>voice box</b> and the <b>vibrating bone</b> in the bird"],
    ["<b>'Why-type'</b>", "The <b>significance</b> of the process",
     "For the second question, the answer <b>may lie</b> in the bird's <b>need to communicate "
     "with its mate during breeding season</b>"],
], col_widths=[2.0, 3.2, 5.4]))
story.append(body(
    "When you observe nature around you with a scientific frame of mind you will certainly come "
    "up with many interesting questions <b>of both types</b> - Why are night-blooming flowers "
    "generally white? How does the bee know which flower has nectar? Why does cactus have so "
    "many thorns? How does the chick spures recognise her own mother? - and so on."))
story.append(note(
    "NCERT prints \"chick spures\" in this list of questions; the wording is reproduced as "
    "printed. Note the qualifier in the first question: night-blooming flowers are "
    "<b>generally</b> white, not always."))

# ======================================================================================
# ---- 11.1 POPULATIONS (F032-F035) ----
# ======================================================================================
story.append(heading("11.1", "POPULATIONS", 1))
story.append(body(
    "You have already learnt in previous classes that <b>Ecology</b> is a subject which studies "
    "the interactions among organisms and between the organism and its physical (<b>abiotic</b>) "
    "environment. As a branch of biology, ecology is the study of the relationships of living "
    "organisms with the <b>abiotic (physico-chemical factors)</b> and <b>biotic components "
    "(other species)</b> of their environment."))
story.append(keyterm(
    "Ecology is basically concerned with <b>four levels of biological organisation</b> - "
    "<b>organisms, populations, communities and biomes</b>. In this chapter we explore ecology "
    "at <b>population</b> levels."))

# ======================================================================================
# ---- 11.1.1 Population Attributes (F036-F069, F251) ----
# ======================================================================================
story.append(heading("11.1.1", "Population Attributes", 2))
story.append(body(
    "In nature, we <b>rarely</b> find isolated, single individuals of any species; <b>majority</b> "
    "of them live in groups in a well defined geographical area, share or compete for similar "
    "resources, potentially interbreed and thus constitute a <b>population</b>."))
story.append(b1("Although the term <b>interbreeding</b> implies sexual reproduction, a group of "
                "individuals resulting from even <b>asexual reproduction</b> is also "
                "<b>generally</b> considered a population for the purpose of ecological studies."))
story.append(b1("Examples of a population: <b>all the cormorants in a wetland</b>, <b>rats in an "
                "abandoned dwelling</b>, <b>teakwood trees in a forest tract</b>, <b>bacteria in "
                "a culture plate</b> and <b>lotus plants in a pond</b>."))
story.append(b1("Although an <b>individual organism</b> is the one that has to cope with a "
                "changed environment, it is at the <b>population level</b> that <b>natural "
                "selection</b> operates to evolve the desired traits. Population ecology is, "
                "therefore, an important area because it links <b>ecology to population genetics "
                "and evolution</b>."))

story.append(heading("11.1.1", "Attributes a population has but an individual does not", 3))
story.append(body(
    "A population has certain attributes whereas an individual organism does not. An individual "
    "may have <b>births and deaths</b>, but a population has <b>birth rates and death rates</b>. "
    "In a population these rates refer to <b>per capita</b> births and deaths, i.e. the rates "
    "expressed are change in numbers (increase or decrease) <b>with respect to members of the "
    "population</b>."))
story.append(data_table([
    ["Attribute", "An individual", "A population"],
    ["Births / deaths", "Has births and deaths", "Has <b>birth rates</b> and <b>death rates</b> (per capita)"],
    ["Sex", "Is either a male or a female", "Has a <b>sex ratio</b> (e.g., 60 per cent of the population are females and 40 per cent males)"],
    ["Age", "Has one age at a time", "Is composed of individuals of <b>different ages</b>; the <b>age distribution</b> can be plotted as an <b>age pyramid</b>"],
], col_widths=[2.2, 3.4, 5.0]))
story.append(data_table([
    ["Worked example", "Calculation", "Rate"],
    ["A pond had <b>20</b> lotus plants last year; through reproduction <b>8</b> new plants are "
     "added, taking the current population to <b>28</b>",
     "8/20", "<b>0.4 offspring per lotus per year</b> (birth rate)"],
    ["<b>4</b> individuals in a laboratory population of <b>40</b> fruitflies died during a "
     "specified time interval, say <b>a week</b>",
     "4/40", "<b>0.1 individuals per fruitfly per week</b> (death rate)"],
], col_widths=[6.0, 1.6, 3.0]))

story.append(heading("11.1.1", "Age pyramids", 3))
story.append(body(
    "A population at any given time is composed of individuals of different ages. If the "
    "<b>age distribution</b> (per cent individuals of a given age or age group) is plotted for "
    "the population, the resulting structure is called an <b>age pyramid</b> (Figure 11.1). For "
    "human population, the age pyramids <b>generally</b> show age distribution of <b>males and "
    "females</b> in a diagram. The three age classes plotted are <b>Pre-reproductive</b>, "
    "<b>Reproductive</b> and <b>Post-reproductive</b>."))
story.append(data_table([
    ["Pyramid shape (as labelled in Figure 11.1)", "Growth status of the population"],
    ["<b>Expanding</b> - broad Pre-reproductive base", "(a) whether it is <b>growing</b>"],
    ["<b>Stable</b> - Pre-reproductive and Reproductive classes about equal", "(b) <b>stable</b> (the Summary calls this <b>stationary</b>)"],
    ["<b>Declining</b> - narrow Pre-reproductive base", "(c) <b>declining</b>"],
], col_widths=[6.0, 4.6]))
story.append(note(
    "The <b>shape</b> of the pyramids reflects the growth status of the population - (a) whether "
    "it is growing, (b) stable or (c) declining. The chapter Summary uses the word "
    "<b>stationary</b> where the body and the figure label say <b>Stable</b>; both wordings are "
    "NCERT's, so recognise either in a question."))
story.append(figure(
    "fig_11_1.png",
    "Fig. 11.1 - Representation of age pyramids for human population. Each pyramid is read as "
    "three stacked age classes - Pre-reproductive (bottom), Reproductive (middle) and "
    "Post-reproductive (top) - with males and females on the two sides; the three shapes are "
    "labelled Expanding, Stable and Declining."))

story.append(heading("11.1.1", "Population size and population density (N)", 3))
story.append(body(
    "The <b>size</b> of the population tells us a lot about its status in the habitat. Whatever "
    "ecological processes we wish to investigate in a population - be it the outcome of "
    "<b>competition</b> with another species, the impact of a <b>predator</b> or the effect of a "
    "<b>pesticide application</b> - we <b>always</b> evaluate them in terms of any change in the "
    "population size."))
story.append(b1("The size, in nature, could be as low as <b>&lt;10</b> (<i>Siberian cranes</i> at "
                "<b>Bharatpur wetlands</b> in any year) or go into <b>millions</b> "
                "(<i>Chlamydomonas</i> in a pond)."))
story.append(keyterm(
    "<b>Population size</b>, technically called <b>population density</b> (designated as "
    "<b>N</b>), need <b>not necessarily</b> be measured in numbers only."))
story.append(body(
    "Although <b>total number</b> is <b>generally</b> the most appropriate measure of population "
    "density, it is <b>in some cases</b> either meaningless or difficult to determine:"))
story.append(data_table([
    ["Problem with total number", "NCERT's case", "Better measure"],
    ["Total number is <b>meaningless</b> - it hides the ecological role of a huge individual",
     "An area with <b>200 carrot grass</b> (<i>Parthenium hysterophorus</i>) plants but only a "
     "<b>single huge banyan tree with a large canopy</b>: calling banyan density low relative to "
     "carrot grass underestimates the enormous role of the Banyan in that community",
     "<b>Per cent cover</b> or <b>biomass</b>"],
    ["Total number is <b>not easily adoptable</b> - the population is huge and counting is "
     "impossible or very time-consuming",
     "A <b>dense laboratory culture of bacteria in a petri dish</b> (embedded question: what is "
     "the best measure to report its density?)",
     "A measure that does not need head-counting, e.g. biomass or per cent cover"],
    ["<b>Sometimes</b>, for certain ecological investigations, there is no need to know the "
     "<b>absolute</b> population densities",
     "The number of <b>fish caught per trap</b> is good enough measure of its total population "
     "density in the lake",
     "<b>Relative densities</b> serve the purpose equally well"],
    ["We are <b>mostly</b> obliged to estimate population sizes <b>indirectly</b>, without "
     "actually counting them or seeing them",
     "The <b>tiger census</b> in our national parks and tiger reserves",
     "<b>Indirect evidence</b> - often based on <b>pug marks</b> and <b>fecal pellets</b>"],
], col_widths=[3.0, 5.2, 2.4]))
story.append(note(
    "Ecological effects of any factor on a population are <b>generally</b> reflected in its size "
    "(population density), which may be expressed in different ways - <b>numbers, biomass, per "
    "cent cover</b>, etc. - depending on the species."))

# ======================================================================================
# ---- 11.1.2 Population Growth (F070-F084) ----
# ======================================================================================
story.append(heading("11.1.2", "Population Growth", 2))
story.append(body(
    "The size of a population for any species is <b>not a static parameter</b>. It keeps changing "
    "with time, depending on various factors including <b>food availability, predation pressure "
    "and adverse weather</b>. In fact, it is these changes in population density that give us "
    "some idea of what is happening to the population - whether it is <b>flourishing or "
    "declining</b>."))
story.append(body(
    "The density of a population in a given habitat during a given period fluctuates due to "
    "changes in <b>four basic processes</b>, <b>two</b> of which (<b>natality</b> and "
    "<b>immigration</b>) contribute to an <b>increase</b> in population density and <b>two</b> "
    "(<b>mortality</b> and <b>emigration</b>) to a <b>decrease</b>:"))
story.append(data_table([
    ["Process (as labelled in Figure 11.2)", "Symbol", "NCERT definition", "Effect on Population Density (N)"],
    ["(i) <b>Natality (B)</b>", "B",
     "The number of <b>births</b> during a given period in the population that are <b>added to "
     "the initial density</b>", "<b>Increase</b>"],
    ["(iii) <b>Immigration (I)</b>", "I",
     "The number of individuals of the <b>same species</b> that have <b>come into</b> the habitat "
     "from elsewhere during the time period under consideration", "<b>Increase</b>"],
    ["(ii) <b>Mortality (D)</b>", "D",
     "The number of <b>deaths</b> in the population during a given period", "<b>Decrease</b>"],
    ["(iv) <b>Emigration (E)</b>", "E",
     "The number of individuals of the population who <b>left the habitat and gone elsewhere</b> "
     "during the time period under consideration", "<b>Decrease</b>"],
], col_widths=[2.4, 0.9, 5.5, 1.9]))
story.append(body(
    "So, if <b>N</b> is the population density at time <b>t</b>, then its density at time "
    "<b>t + 1</b> is"))
story.append(Paragraph(
    "<b>N<sub>t+1</sub> = N<sub>t</sub> + [(B + I) - (D + E)]</b>", STYLES["Body"]))
story.append(body(
    "You can see from the above equation (Fig. 11.2) that <b>population density will increase</b> "
    "if the number of births plus the number of immigrants <b>(B + I)</b> is <b>more than</b> the "
    "number of deaths plus the number of emigrants <b>(D + E)</b>."))
story.append(b1("Under <b>normal conditions</b>, <b>births and deaths</b> are the most important "
                "factors influencing population density, the other two factors assuming importance "
                "<b>only under special conditions</b>."))
story.append(b1("For instance, if a <b>new habitat is just being colonised</b>, <b>immigration</b> "
                "may contribute more significantly to population growth than birth rates."))
story.append(figure(
    "fig_11_2.png",
    "Fig. 11.2 - The four processes acting on Population Density (N): Natality (B) and "
    "Immigration (I) add to it, Mortality (D) and Emigration (E) subtract from it. NCERT gives "
    "this figure no caption text beyond the number; the '+' and '-' signs on its arrows are the "
    "same sign convention used in the equation above.", max_width_cm=11.0))
story.append(memory_aid(
    "<b>IN</b> raises density, <b>ME</b> lowers it: <b>I</b>mmigration + <b>N</b>atality in; "
    "<b>M</b>ortality + <b>E</b>migration out."))

# ---- 11.1.2 Growth Models (F085-F088) ----
story.append(heading("11.1.2", "Growth Models", 3))
story.append(body(
    "Does the growth of a population with time show any <b>specific and predictable pattern</b>? "
    "We have been concerned about <b>unbridled human population growth</b> and problems created "
    "by it in our country, and it is therefore natural for us to be curious if different animal "
    "populations in nature behave the same way or show some restraints on growth. Perhaps we can "
    "learn a lesson or two from nature on how to control population growth."))

# ---- 11.1.2 (i) Exponential growth (F089-F112, F252a, F253) ----
story.append(heading("(i)", "Exponential growth", 3))
story.append(body(
    "<b>Resource (food and space) availability</b> is obviously essential for the <b>unimpeded</b> "
    "growth of a population. <b>Ideally</b>, when resources in the habitat are <b>unlimited</b>, "
    "each species has the ability to realise <b>fully</b> its <b>innate potential</b> to grow in "
    "number, as <b>Darwin</b> observed while developing his theory of <b>natural selection</b>. "
    "Then the population grows in an <b>exponential or geometric</b> fashion."))
story.append(note(
    "The chapter Summary hedges this statement: \"When resources are unlimited, the growth is "
    "<b>usually</b> exponential but when resources become progressively limiting, the growth "
    "pattern turns logistic.\" The body states the exponential case without the hedge - keep "
    "NCERT's <b>usually</b> when the Summary wording is quoted."))
story.append(body(
    "If in a population of size <b>N</b> the birth rates (<b>not total number but per capita "
    "births</b>) are represented as <b>b</b> and death rates (again, <b>per capita</b> death "
    "rates) as <b>d</b>, then the increase or decrease in N during a unit time period t "
    "(<b>dN/dt</b>) will be:"))
story.append(Paragraph("<b>dN/dt = (b - d) x N</b>", STYLES["Body"]))
story.append(body("Let <b>(b - d) = r</b>, then"))
story.append(Paragraph("<b>dN/dt = rN</b>", STYLES["Body"]))
story.append(keyterm(
    "The <b>r</b> in this equation is called the <b>'intrinsic rate of natural increase'</b> and "
    "is a very important parameter chosen for <b>assessing impacts of any biotic or abiotic "
    "factor</b> on population growth. The Summary adds that <b>r</b> is a measure of the "
    "<b>inherent potential of a population to grow</b>."))
story.append(data_table([
    ["Population", "r value"],
    ["<b>Norway rat</b>", "<b>0.015</b>"],
    ["<b>Flour beetle</b>", "<b>0.12</b>"],
    ["<b>Human population in India, 1981</b>", "<b>0.0205</b>"],
], col_widths=[6.0, 4.6]))
story.append(note(
    "NCERT activity: <b>find out what the current r value is</b>. For calculating it, you need to "
    "know the <b>birth rates and death rates</b>."))
story.append(body(
    "The above equation describes the <b>exponential or geometric growth pattern</b> of a "
    "population (Figure 11.3) and results in a <b>J-shaped curve</b> when we plot <b>N in "
    "relation to time</b>. If you are familiar with basic calculus, you can derive the "
    "<b>integral form</b> of the exponential growth equation as:"))
story.append(Paragraph(
    "<b>N<sub>t</sub> = N<sub>0</sub> e<super>rt</super></b>", STYLES["Body"]))
story.append(data_table([
    ["Term", "Meaning"],
    ["<b>N<sub>t</sub></b>", "Population density <b>after time t</b>"],
    ["<b>N<sub>0</sub></b>", "Population density <b>at time zero</b>"],
    ["<b>r</b>", "<b>Intrinsic rate of natural increase</b>"],
    ["<b>e</b>", "The base of <b>natural logarithms (2.71828)</b>"],
], col_widths=[2.0, 8.6]))
story.append(body(
    "<b>Any</b> species growing exponentially under unlimited resource conditions can reach "
    "<b>enormous population densities in a short time</b>. <b>Darwin</b> showed how even a "
    "<b>slow growing animal like elephant</b> could reach enormous numbers <b>in the absence of "
    "checks</b>. The following anecdote is popularly narrated to demonstrate dramatically how "
    "fast a huge population could build up when growing exponentially."))
story.append(process_flow([
    "The <b>king and the minister</b> sat for a <b>chess game</b>. The king, confident of winning, "
    "was ready to accept <b>any bet</b> proposed by the minister.",
    "The minister humbly asked only for <b>some wheat grains</b>, the quantity to be calculated by "
    "placing on the chess board <b>one grain in Square 1, two in Square 2, four in Square 3, eight "
    "in Square 4</b>, and so on - <b>doubling each time</b> the previous quantity of wheat on the "
    "next square <b>until all the 64 squares were filled</b>.",
    "The king accepted the seemingly silly bet and started the game, but <b>unluckily for him, the "
    "minister won</b>.",
    "By the time he covered <b>half the chess board</b>, the king realised to his dismay that "
    "<b>all the wheat produced in his entire kingdom pooled together</b> would still be "
    "<b>inadequate</b> to cover all the <b>64 squares</b>.",
]))
story.append(body(
    "Now think of a tiny <i>Paramecium</i> starting with just <b>one individual</b> and, through "
    "<b>binary fission</b>, <b>doubling in numbers every day</b> - imagine what a mind-boggling "
    "population size it would reach in <b>64 days</b> (provided <b>food and space remain "
    "unlimited</b>)."))

# ---- 11.1.2 (ii) Logistic growth (F113-F127, F252) ----
story.append(heading("(ii)", "Logistic growth", 3))
story.append(body(
    "<b>No population of any species in nature</b> has at its disposal <b>unlimited</b> resources "
    "to permit exponential growth. This leads to <b>competition between individuals for limited "
    "resources</b>. Eventually, the <b>'fittest' individual will survive and reproduce</b>. The "
    "governments of many countries have also realised this fact and introduced various "
    "<b>restraints</b> with a view to limit human population growth."))
story.append(keyterm(
    "In nature, a given habitat has enough resources to support a <b>maximum possible number</b>, "
    "beyond which <b>no further growth is possible</b>. This limit is nature's <b>carrying "
    "capacity (K)</b> for that species in that habitat."))
story.append(body(
    "A population growing in a habitat with <b>limited resources</b> shows <b>initially</b> a "
    "<b>lag phase</b>, <b>followed</b> by phases of <b>acceleration</b> and <b>deceleration</b> "
    "and <b>finally</b> an <b>asymptote</b>, when the population density reaches the carrying "
    "capacity:"))
story.append(process_flow([
    "<b>Lag phase</b> - the initial phase.",
    "<b>Acceleration</b> - growth speeds up.",
    "<b>Deceleration</b> - growth slows down.",
    "<b>Asymptote</b> - reached when the <b>population density reaches the carrying capacity "
    "(K)</b>.",
]))
story.append(body(
    "A plot of <b>N in relation to time (t)</b> results in a <b>sigmoid curve</b>. This type of "
    "population growth is called <b>Verhulst-Pearl Logistic Growth</b> (Figure 11.3) and is "
    "described by the following equation:"))
story.append(Paragraph("<b>dN/dt = rN [(K - N)/K]</b>", STYLES["Body"]))
story.append(data_table([
    ["Term", "Meaning"],
    ["<b>N</b>", "Population density at time <b>t</b>"],
    ["<b>r</b>", "<b>Intrinsic rate of natural increase</b>"],
    ["<b>K</b>", "<b>Carrying capacity</b>"],
], col_widths=[2.0, 8.6]))
story.append(b1("Since resources for growth for <b>most</b> animal populations are <b>finite</b> "
                "and become limiting <b>sooner or later</b>, the <b>logistic growth model is "
                "considered a more realistic one</b>."))
story.append(figure(
    "fig_11_3.png",
    "Fig. 11.3 - Population growth curve: <b>a</b> when responses are not limiting the growth, "
    "plot is exponential; <b>b</b> when responses are limiting the growth, plot is logistic; "
    "<b>K</b> is carrying capacity. Axes: Population density (N) against Time (t); curve "
    "<b>a</b> carries dN/dt = rN and curve <b>b</b> carries dN/dt = rN (K-N)/K.",
    max_width_cm=12.5))
story.append(note(
    "Both models are limited in the end: as the Summary puts it, <b>in either case, growth is "
    "ultimately limited by the carrying capacity of the environment</b>. The two curves in Figure "
    "11.3 differ only in whether resources are limiting - exponential (<b>a</b>, J-shaped) versus "
    "logistic (<b>b</b>, sigmoid, flattening at <b>K</b>)."))
story.append(data_table([
    ["Feature", "Exponential (geometric) growth", "Logistic (Verhulst-Pearl) growth"],
    ["Resources", "<b>Unlimited</b>", "<b>Limited</b> - competition between individuals"],
    ["Equation", "<b>dN/dt = rN</b>; integral form <b>N<sub>t</sub> = N<sub>0</sub> "
     "e<super>rt</super></b>", "<b>dN/dt = rN [(K - N)/K]</b>"],
    ["Curve", "<b>J-shaped</b> (curve <b>a</b> of Figure 11.3)",
     "<b>Sigmoid</b> (curve <b>b</b> of Figure 11.3), with lag, acceleration, deceleration and "
     "asymptote phases"],
    ["Carrying capacity", "Not reached - density can become enormous in a short time",
     "Growth stops at <b>K</b>"],
    ["Realism", "Ideal case only", "<b>More realistic</b> for most animal populations"],
], col_widths=[1.9, 4.3, 4.4]))
story.append(note(
    "NCERT activity: gather from <b>Government Census data</b> the population figures for "
    "<b>India for the last 100 years</b>, plot them and check <b>which growth pattern is "
    "evident</b>."))

# ======================================================================================
# ---- 11.1.3 Life History Variation (F128-F135) ----
# ======================================================================================
story.append(heading("11.1.3", "Life History Variation", 2))
story.append(body(
    "Populations evolve to <b>maximise their reproductive fitness</b>, also called <b>Darwinian "
    "fitness (high r value)</b>, in the habitat in which they live. Under a particular set of "
    "<b>selection pressures</b>, organisms evolve towards the <b>most efficient reproductive "
    "strategy</b>."))
story.append(data_table([
    ["Life history trait", "One extreme", "The other extreme"],
    ["<b>Number of breeding events</b>", "Breed <b>only once</b> in their lifetime - <b>Pacific "
     "salmon fish, bamboo</b>", "Breed <b>many times</b> during their lifetime - <b>most birds "
     "and mammals</b>"],
    ["<b>Number and size of offspring</b>", "A <b>large number of small-sized</b> offspring - "
     "<b>Oysters, pelagic fishes</b>", "A <b>small number of large-sized</b> offspring - "
     "<b>birds, mammals</b>"],
], col_widths=[2.6, 4.0, 4.0]))
story.append(body(
    "So, <b>which is desirable for maximising fitness</b>? Ecologists suggest that <b>life history "
    "traits</b> of organisms have evolved <b>in relation to the constraints imposed by the abiotic "
    "and biotic components of the habitat</b> in which they live. Evolution of life history traits "
    "in different species is <b>currently an important area of research</b> being conducted by "
    "ecologists."))

# ======================================================================================
# ---- 11.1.4 Population Interactions (F136-F157, Table 11.1) ----
# ======================================================================================
story.append(heading("11.1.4", "Population Interactions", 2))
story.append(body(
    "Can you think of any natural habitat on earth that is inhabited <b>just by a single "
    "species</b>? <b>There is no such habitat</b> and such a situation is <b>even "
    "inconceivable</b>. For any species, the <b>minimal requirement is one more species on which "
    "it can feed</b>."))
story.append(b1("Even a <b>plant species</b>, which makes its own food, <b>cannot survive "
                "alone</b>; it needs <b>soil microbes</b> to break down the <b>organic matter</b> "
                "in soil and return the <b>inorganic nutrients</b> for absorption. And then, how "
                "will the plant manage <b>pollination without an animal agent</b>?"))
story.append(keyterm(
    "In nature, animals, plants and microbes <b>do not and cannot live in isolation</b> but "
    "interact in various ways to form a <b>biological community</b>. Even in <b>minimal "
    "communities</b>, <b>many</b> interactive linkages exist, although <b>all may not</b> be "
    "readily apparent."))
story.append(body(
    "<b>Interspecific interactions</b> arise from the interaction of <b>populations of two "
    "different species</b>. They could be <b>beneficial, detrimental or neutral</b> (neither harm "
    "nor benefit) <b>to one of the species or both</b>. Assigning a <b>'+'</b> sign for beneficial "
    "interaction, <b>'-'</b> sign for detrimental and <b>0</b> for neutral interaction, we get "
    "all the possible outcomes of interspecific interactions (Table 11.1)."))
story.append(KeepTogether([
    heading("Table 11.1", "Population Interactions", 3),
    data_table([
        ["Species A", "Species B", "Name of Interaction"],
        ["<b>+</b>", "<b>+</b>", "<b>Mutualism</b>"],
        ["<b>-</b>", "<b>-</b>", "<b>Competition</b>"],
        ["<b>+</b>", "<b>-</b>", "<b>Predation</b>"],
        ["<b>+</b>", "<b>-</b>", "<b>Parasitism</b>"],
        ["<b>+</b>", "<b>0</b>", "<b>Commensalism</b>"],
        ["<b>-</b>", "<b>0</b>", "<b>Amensalism</b>"],
    ], col_widths=[2.5, 2.5, 5.6]),
]))
story.append(b1("<b>Both</b> the species <b>benefit</b> in <b>mutualism</b> and <b>both lose</b> "
                "in <b>competition</b> in their interactions with each other."))
story.append(b1("In <b>both parasitism and predation</b> <b>only one</b> species benefits "
                "(<b>parasite</b> and <b>predator</b>, respectively) and the interaction is "
                "<b>detrimental to the other species</b> (<b>host</b> and <b>prey</b>, "
                "respectively)."))
story.append(b1("The interaction where <b>one species is benefitted and the other is neither "
                "benefitted nor harmed</b> is called <b>commensalism</b>."))
story.append(b1("In <b>amensalism</b>, on the other hand, <b>one species is harmed whereas the "
                "other is unaffected</b>."))
story.append(b1("<b>Predation, parasitism and commensalism</b> share a common characteristic - "
                "<b>the interacting species live closely together</b>."))
story.append(memory_aid(
    "Read Table 11.1 by signs, not by names: <b>++</b> mutualism, <b>--</b> competition, "
    "<b>+-</b> predation and parasitism, <b>+0</b> commensalism, <b>-0</b> amensalism."))

# ---- 11.1.4 (i) Predation (F158-F182, F254) ----
story.append(heading("(i)", "Predation", 3))
story.append(body(
    "What would happen to <b>all the energy fixed by autotrophic organisms</b> if the community "
    "has <b>no animals to eat the plants</b>? You can think of <b>predation</b> as nature's way "
    "of <b>transferring to higher trophic levels the energy fixed by plants</b>."))
story.append(b1("When we think of predator and prey, <b>most probably</b> it is the <b>tiger and "
                "the deer</b> that readily come to our mind, but a <b>sparrow eating any seed is "
                "no less a predator</b>."))
story.append(b1("Although animals eating plants are categorised separately as <b>herbivores</b>, "
                "they are, <b>in a broad ecological context, not very different from "
                "predators</b>."))
story.append(body("Besides acting as <b>'conduits' for energy transfer across trophic levels</b>, "
                  "predators play other important roles:"))
story.append(b1("<b>They keep prey populations under control.</b> But for predators, prey species "
                "could achieve <b>very high population densities</b> and cause <b>ecosystem "
                "instability</b>. (The Summary hedges this as <b>some</b> predators help in "
                "controlling their prey populations.)"))
story.append(b2("When certain <b>exotic species</b> are introduced into a geographical area, they "
                "become <b>invasive</b> and start spreading fast because the <b>invaded land does "
                "not have its natural predators</b>."))
story.append(b2("The <b>prickly pear cactus</b> introduced into <b>Australia in the early "
                "1920's</b> caused havoc by spreading rapidly into <b>millions of hectares of "
                "rangeland</b>. The invasive cactus was brought under control <b>only</b> after a "
                "<b>cactus-feeding predator (a moth)</b> from its natural habitat was introduced "
                "into the country."))
story.append(b2("<b>Biological control methods</b> adopted in <b>agricultural pest control</b> "
                "are based on the ability of the <b>predator to regulate prey population</b>."))
story.append(b1("<b>Predators also help in maintaining species diversity</b> in a community, by "
                "<b>reducing the intensity of competition</b> among competing prey species."))
story.append(b2("In the <b>rocky intertidal communities of the American Pacific Coast</b> the "
                "starfish <i>Pisaster</i> is an important predator. In a field experiment, when "
                "<b>all the starfish were removed</b> from an enclosed intertidal area, <b>more "
                "than 10 species of invertebrates became extinct within a year</b>, because of "
                "<b>inter-specific competition</b>."))
story.append(note(
    "If a predator is <b>too efficient</b> and <b>overexploits its prey</b>, then the prey might "
    "become extinct and, following it, the predator will <b>also</b> become extinct for lack of "
    "food. <b>This is the reason why predators in nature are 'prudent'.</b>"))
story.append(body("<b>Prey species have evolved various defenses to lessen the impact of "
                  "predation:</b>"))
story.append(data_table([
    ["Prey defence", "NCERT example"],
    ["<b>Cryptic colouration (camouflage)</b> - to avoid being detected easily by the predator",
     "<b>Some species of insects and frogs</b>"],
    ["<b>Being poisonous</b> - and therefore avoided by the predators", "<b>Some</b> prey species"],
    ["<b>Distastefulness</b> from a <b>special chemical</b> present in the body - acquired during "
     "the <b>caterpillar stage by feeding on a poisonous weed</b>",
     "The <b>Monarch butterfly</b>, highly distasteful to its predator (<b>bird</b>)"],
], col_widths=[5.6, 5.0]))
story.append(body(
    "<b>For plants, herbivores are the predators.</b> Nearly <b>25 per cent</b> of all insects are "
    "known to be <b>phytophagous</b> (feeding on <b>plant sap and other parts of plants</b>). The "
    "problem is <b>particularly severe for plants</b> because, <b>unlike animals</b>, they "
    "<b>cannot run away</b> from their predators. Plants therefore have evolved an <b>astonishing "
    "variety of morphological and chemical defences</b> against herbivores."))
story.append(data_table([
    ["Defence type", "How it works", "NCERT example"],
    ["<b>Morphological</b>", "<b>Thorns</b> are the <b>most common</b> morphological means of "
     "defence", "<b><i>Acacia</i>, <i>Cactus</i></b>"],
    ["<b>Chemical</b>", "<b>Many</b> plants produce and store chemicals that make the herbivore "
     "<b>sick when they are eaten</b>, <b>inhibit feeding or digestion</b>, <b>disrupt its "
     "reproduction</b> or <b>even kill it</b>",
     "The weed <b><i>Calotropis</i></b> growing in abandoned fields produces <b>highly poisonous "
     "cardiac glycosides</b> - which is why you <b>never</b> see any <b>cattle or goats</b> "
     "browsing on this plant"],
    ["<b>Chemical (commercial)</b>", "A wide variety of chemical substances extracted from plants "
     "on a <b>commercial scale</b> are <b>actually</b> produced as defences against <b>grazers "
     "and browsers</b>",
     "<b>Nicotine, caffeine, quinine, strychnine, opium</b>, etc."],
], col_widths=[2.2, 4.6, 3.8]))

# ---- 11.1.4 (ii) Competition (F183-F198, F189a) ----
story.append(heading("(ii)", "Competition", 3))
story.append(body(
    "When <b>Darwin</b> spoke of the <b>struggle for existence and survival of the fittest</b> in "
    "nature, he was convinced that <b>interspecific competition is a potent force in organic "
    "evolution</b>. It is <b>generally believed</b> that competition occurs when <b>closely "
    "related species</b> compete for the <b>same resources that are limiting</b>, but <b>this is "
    "not entirely true</b>:"))
story.append(b1("<b>Firstly, totally unrelated species could also compete</b> for the same "
                "resource. For instance, in <b>some shallow South American lakes</b>, <b>visiting "
                "flamingoes</b> and <b>resident fishes</b> compete for their common food, the "
                "<b>zooplankton</b> in the lake."))
story.append(b1("<b>Secondly, resources need not be limiting</b> for competition to occur; in "
                "<b>interference competition</b>, the <b>feeding efficiency</b> of one species "
                "might be <b>reduced</b> due to the <b>interfering and inhibitory presence</b> of "
                "the other species, <b>even if resources (food and space) are abundant</b>."))
story.append(keyterm(
    "Therefore, <b>competition</b> is best defined as a process in which the <b>fitness of one "
    "species</b> (measured in terms of its <b>'r'</b>, the <b>intrinsic rate of increase</b>) is "
    "<b>significantly lower in the presence of another species</b>."))
story.append(body(
    "It is <b>relatively easy to demonstrate in laboratory experiments</b>, as <b>Gause</b> and "
    "other experimental ecologists did, that when resources are limited the <b>competitively "
    "superior species will eventually eliminate the other species</b> - but evidence for such "
    "<b>competitive exclusion</b> occurring <b>in nature is not always conclusive</b>. "
    "<b>Strong and persuasive circumstantial evidence does exist however in some cases:</b>"))
story.append(b1("<b>The Abingdon tortoise</b> in <b>Galapagos Islands</b> became <b>extinct within "
                "a decade</b> after <b>goats</b> were introduced on the island, <b>apparently</b> "
                "due to the <b>greater browsing efficiency of the goats</b>."))
story.append(b1("<b>'Competitive release'</b> - another evidence for the occurrence of competition "
                "in nature. A species whose distribution is <b>restricted to a small geographical "
                "area</b> because of the presence of a <b>competitively superior species</b> is "
                "found to <b>expand its distributional range dramatically</b> when the competing "
                "species is <b>experimentally removed</b>."))
story.append(b2("<b>Connell's</b> elegant field experiments showed that on the <b>rocky sea coasts "
                "of Scotland</b>, the <b>larger and competitively superior barnacle "
                "<i>Balanus</i></b> dominates the <b>intertidal area</b>, and <b>excludes the "
                "smaller barnacle <i>Chathamalus</i></b> from that zone."))
story.append(b1("<b>In general, herbivores and plants appear to be more adversely affected by "
                "competition than carnivores.</b>"))
story.append(keyterm(
    "<b>Gause's 'Competitive Exclusion Principle'</b> states that <b>two closely related species "
    "competing for the same resources cannot co-exist indefinitely</b> and the <b>competitively "
    "inferior one will be eliminated eventually</b>. This <b>may</b> be true <b>if resources are "
    "limiting, but not otherwise</b>."))
story.append(body(
    "<b>More recent studies do not support such gross generalisations</b> about competition. While "
    "they <b>do not rule out</b> the occurrence of interspecific competition in nature, they point "
    "out that species facing competition <b>might evolve mechanisms that promote co-existence "
    "rather than exclusion</b>."))
story.append(b1("One such mechanism is <b>'resource partitioning'</b>. If two species compete for "
                "the same resource, they could <b>avoid competition</b> by choosing, for instance, "
                "<b>different times for feeding</b> or <b>different foraging patterns</b>."))
story.append(b1("<b>MacArthur</b> showed that <b>five closely related species of warblers</b> "
                "living on the <b>same tree</b> were able to <b>avoid competition and co-exist</b> "
                "due to <b>behavioural differences in their foraging activities</b>."))

# ---- 11.1.4 (iii) Parasitism (F199-F219) ----
story.append(heading("(iii)", "Parasitism", 3))
story.append(body(
    "Considering that the <b>parasitic mode of life ensures free lodging and meals</b>, it is not "
    "surprising that parasitism has evolved in <b>so many taxonomic groups from plants to higher "
    "vertebrates</b>."))
story.append(b1("<b>Many</b> parasites have evolved to be <b>host-specific</b> (they can "
                "parasitise <b>only a single species of host</b>) in such a way that <b>both host "
                "and the parasite tend to co-evolve</b>: if the host evolves special mechanisms "
                "for <b>rejecting or resisting</b> the parasite, the parasite has to evolve "
                "mechanisms to <b>counteract and neutralise</b> them, in order to be successful "
                "with the <b>same host species</b>."))
story.append(b1("In accordance with their life styles, parasites evolved <b>special "
                "adaptations</b>: <b>loss of unnecessary sense organs</b>, presence of "
                "<b>adhesive organs or suckers</b> to cling on to the host, <b>loss of digestive "
                "system</b> and <b>high reproductive capacity</b>."))
story.append(b1("The life cycles of parasites are <b>often complex</b>, involving <b>one or two "
                "intermediate hosts or vectors</b> to facilitate parasitisation of its <b>primary "
                "host</b>."))
story.append(b2("The <b>human liver fluke</b> (a <b>trematode</b> parasite) depends on <b>two "
                "intermediate hosts (a snail and a fish)</b> to complete its life cycle."))
story.append(b2("The <b>malarial parasite</b> needs a <b>vector (mosquito)</b> to spread to other "
                "hosts."))
story.append(note(
    "<b>Majority</b> of the parasites <b>harm</b> the host: they <b>may</b> reduce the "
    "<b>survival, growth and reproduction</b> of the host and reduce its <b>population "
    "density</b>. They <b>might</b> render the host <b>more vulnerable to predation</b> by making "
    "it <b>physically weak</b>. NCERT asks: do you believe that an <b>ideal parasite</b> should be "
    "able to thrive within the host <b>without harming it</b>? Then why didn't natural selection "
    "lead to the evolution of such <b>totally harmless parasites</b>?"))
story.append(data_table([
    ["Type", "Definition", "Examples / features"],
    ["<b>Ectoparasites</b>", "Parasites that feed on the <b>external surface</b> of the host "
     "organism",
     "The <b>most familiar examples</b>: <b>lice on humans</b> and <b>ticks on dogs</b>; <b>many "
     "marine fish</b> are infested with <b>ectoparasitic copepods</b>; <b><i>Cuscuta</i></b>, a "
     "parasitic plant <b>commonly found growing on hedge plants</b>, has <b>lost its chlorophyll "
     "and leaves</b> in the course of evolution and derives its nutrition from the host plant "
     "which it parasitises"],
    ["<b>Endoparasites</b>", "In contrast, those that live <b>inside the host body</b> at "
     "different sites (<b>liver, kidney, lungs, red blood cells</b>, etc.)",
     "Life cycles are <b>more complex</b> because of their <b>extreme specialisation</b>; their "
     "<b>morphological and anatomical features are greatly simplified</b> while <b>emphasising "
     "their reproductive potential</b>"],
    ["<b>Brood parasitism</b>", "A fascinating example of parasitism <b>in birds</b>, in which "
     "the <b>parasitic bird lays its eggs in the nest of its host</b> and <b>lets the host "
     "incubate them</b>",
     "During the course of evolution, the <b>eggs of the parasitic bird have evolved to resemble "
     "the host's egg in size and colour</b>, to <b>reduce the chances of the host bird detecting "
     "the foreign eggs and ejecting them from the nest</b>"],
], col_widths=[2.0, 3.6, 5.0]))
story.append(note(
    "Two NCERT prompts here. (1) The <b>female mosquito is not considered a parasite</b>, although "
    "it needs our blood for reproduction - can you explain why? (2) Try to follow the movements of "
    "the <b>cuckoo (koel)</b> and the <b>crow</b> in your neighborhood park during the <b>breeding "
    "season (spring to summer)</b> and watch <b>brood parasitism</b> in action."))

# ---- 11.1.4 (iv) Commensalism (F220-F224) ----
story.append(heading("(iv)", "Commensalism", 3))
story.append(keyterm(
    "<b>Commensalism</b> is the interaction in which <b>one species benefits and the other is "
    "neither harmed nor benefited</b>."))
story.append(data_table([
    ["Example", "Who benefits", "Who is unaffected"],
    ["An <b>orchid</b> growing as an <b>epiphyte</b> on a <b>mango branch</b>", "The orchid",
     "Neither the <b>mango tree</b> derives any apparent benefit"],
    ["<b>Barnacles</b> growing on the <b>back of a whale</b>", "The barnacles",
     "Nor the <b>whale</b> derives any apparent benefit"],
    ["The <b>cattle egret</b> and <b>grazing cattle</b> in close association - a <b>classic "
     "example</b>, a sight you are most likely to catch if you live in <b>farmed rural areas</b>",
     "The <b>egrets always forage close to where the cattle are grazing</b>, because the cattle, "
     "as they move, <b>stir up and flush out insects</b> from the vegetation that <b>otherwise "
     "might be difficult for the egrets to find and catch</b>", "The grazing cattle"],
    ["<b>Sea anemone</b> that has <b>stinging tentacles</b> and the <b>clown fish</b> that lives "
     "among them",
     "The fish <b>gets protection from predators</b> which <b>stay away from the stinging "
     "tentacles</b>",
     "The <b>anemone does not appear to derive any benefit</b> by hosting the clown fish"],
], col_widths=[3.4, 4.0, 3.2]))

# ---- 11.1.4 (v) Mutualism (F225-F248) ----
story.append(heading("(v)", "Mutualism", 3))
story.append(keyterm(
    "<b>Mutualism</b>: this interaction <b>confers benefits on both</b> the interacting species."))
story.append(b1("<b>Lichens</b> represent an <b>intimate mutualistic relationship</b> between a "
                "<b>fungus</b> and <b>photosynthesising algae or cyanobacteria</b>."))
story.append(b1("<b>Mycorrhizae</b> are associations between <b>fungi</b> and the <b>roots of "
                "higher plants</b>: the fungi help the plant in the <b>absorption of essential "
                "nutrients from the soil</b>, while the plant in turn provides the fungi with "
                "<b>energy-yielding carbohydrates</b>."))
story.append(body(
    "<b>The most spectacular and evolutionarily fascinating examples of mutualism are found in "
    "plant-animal relationships.</b> Plants need the help of animals for <b>pollinating their "
    "flowers</b> and <b>dispersing their seeds</b>. Animals obviously have to be paid <b>'fees'</b> "
    "for the services that plants expect from them."))
story.append(b1("Plants offer <b>rewards or fees</b> in the form of <b>pollen and nectar for "
                "pollinators</b> and <b>juicy and nutritious fruits for seed dispersers</b>."))
story.append(b1("But the mutually beneficial system <b>should also be safeguarded against "
                "'cheaters'</b> - for example, <b>animals that try to steal nectar without aiding "
                "in pollination</b>."))
story.append(keyterm(
    "This is why plant-animal interactions <b>often involve co-evolution of the mutualists</b>, "
    "that is, the <b>evolutions of the flower and its pollinator species are tightly linked with "
    "one another</b>."))
story.append(body(
    "In <b>many species of fig trees</b>, there is a <b>tight one-to-one relationship</b> with the "
    "<b>pollinator species of wasp</b> (Figure 11.4). It means that a given fig species <b>can be "
    "pollinated only by its 'partner' wasp species and no other species</b>. The <b>female "
    "wasp</b> uses the fruit <b>not only as an oviposition (egg-laying) site</b> but uses the "
    "<b>developing seeds within the fruit for nourishing its larvae</b>."))
story.append(process_flow([
    "The <b>wasp pollinates the fig inflorescence</b> while searching for <b>suitable egg-laying "
    "sites</b>.",
    "In return for the favour of pollination, the <b>fig offers the wasp some of its developing "
    "seeds</b>, as <b>food for the developing wasp larvae</b>.",
]))
story.append(figure(
    "fig_11_4a.png",
    "Fig. 11.4 (a) - Mutual relationship between fig tree and wasp: Fig flower is pollinated by "
    "wasp.", max_width_cm=9.0))
story.append(figure(
    "fig_11_4b.png",
    "Fig. 11.4 (b) - Mutual relationship between fig tree and wasp: Wasp laying eggs in a fig "
    "fruit.", max_width_cm=9.0))
story.append(body(
    "<b>Orchids</b> show a <b>bewildering diversity of floral patterns</b>, many of which have "
    "evolved to <b>attract the right pollinator insect (bees and bumblebees)</b> and <b>ensure "
    "guaranteed pollination by it</b> (Figure 11.5). <b>Not all orchids offer rewards.</b>"))
story.append(b1("The <b>Mediterranean orchid <i>Ophrys</i></b> employs <b>'sexual deceit'</b> to "
                "get pollination done by <b>a species of bee</b>. <b>One petal</b> of its flower "
                "bears an <b>uncanny resemblance to the female of the bee in size, colour and "
                "markings</b>."))
story.append(process_flow([
    "The <b>male bee is attracted to what it perceives as a female</b> and "
    "<b>'pseudocopulates'</b> with the flower.",
    "During that process it is <b>dusted with pollen from the flower</b>.",
    "When this <b>same bee 'pseudocopulates' with another flower</b>, it <b>transfers pollen</b> "
    "to it and thus <b>pollinates the flower</b>.",
]))
story.append(figure(
    "fig_11_5.png",
    "Fig. 11.5 - Showing bee-a pollinator on orchid flower. The original is a colour photograph; "
    "after monochrome conversion the bee still reads clearly against the pale flower and the dark "
    "background.", max_width_cm=8.5))
story.append(note(
    "<b>Co-evolution in action:</b> if the <b>female bee's colour patterns change even "
    "slightly</b> for any reason during evolution, <b>pollination success will be reduced "
    "unless</b> the orchid flower <b>co-evolves</b> to maintain the resemblance of its petal to "
    "the <b>female bee</b>."))

# ======================================================================================
# ---- Quick Recap (rewritten Summary, F249-F254, F252a) ----
# ======================================================================================
story.append(heading("Recap", "QUICK RECAP", 1))
story.append(b1("<b>Ecology</b> is the study of the relationships of living organisms with the "
                "<b>abiotic (physico-chemical factors)</b> and <b>biotic components (other "
                "species)</b> of their environment; it is concerned with <b>four levels</b> of "
                "biological organisation - <b>organisms, populations, communities and biomes</b>."))
story.append(b1("<b>Evolutionary changes through natural selection take place at the population "
                "level</b>, hence <b>population ecology</b> is an important area of ecology."))
story.append(b1("A <b>population</b> is a group of individuals of a given species <b>sharing or "
                "competing for similar resources in a defined geographical area</b>."))
story.append(b1("Populations have attributes that individual organisms do not - <b>birth rates and "
                "death rates, sex ratio and age distribution</b>. The proportion of different age "
                "groups of males and females is <b>often presented graphically as an age "
                "pyramid</b>; its <b>shape</b> indicates whether a population is <b>stationary, "
                "growing or declining</b>."))
story.append(b1("Ecological effects of any factors on a population are <b>generally</b> reflected "
                "in its <b>size (population density)</b>, which may be expressed in different ways "
                "(<b>numbers, biomass, per cent cover</b>, etc.) depending on the species."))
story.append(b1("Populations <b>grow</b> through <b>births and immigration</b> and <b>decline</b> "
                "through <b>deaths and emigration</b>. When resources are unlimited the growth is "
                "<b>usually exponential</b>; when resources become <b>progressively limiting</b> "
                "the growth pattern turns <b>logistic</b>. <b>In either case, growth is ultimately "
                "limited by the carrying capacity of the environment.</b>"))
story.append(b1("The <b>intrinsic rate of natural increase (r)</b> is a measure of the "
                "<b>inherent potential of a population to grow</b>."))
story.append(b1("Populations of different species in a habitat <b>do not live in isolation but "
                "interact in many ways</b>. Depending on the outcome, interactions between two "
                "species are classified as <b>competition</b> (both species suffer), "
                "<b>predation</b> and <b>parasitism</b> (one benefits and the other suffers), "
                "<b>commensalism</b> (one benefits and the other is unaffected), <b>amensalism</b> "
                "(one is harmed, other unaffected) and <b>mutualism</b> (both species benefit)."))
story.append(b1("<b>Predation</b> is a very important process through which <b>trophic energy "
                "transfer</b> is facilitated, and <b>some</b> predators help in <b>controlling "
                "their prey populations</b>. Plants have evolved <b>diverse morphological and "
                "chemical defenses against herbivory</b>."))
story.append(b1("In competition it is presumed that the <b>superior competitor eliminates the "
                "inferior one</b> (the <b>Competitive Exclusion Principle</b>), but <b>many</b> "
                "closely related species have evolved various mechanisms which <b>facilitate their "
                "co-existence</b>. Some of the most fascinating cases of <b>mutualism</b> in nature "
                "are seen in <b>plant-pollinator interactions</b>."))

# ======================================================================================
# ---- Terms used in the exercises (Rule 2 appendix, F255-F265) ----
# ======================================================================================
story.append(heading("Appendix", "TERMS USED IN THE EXERCISES", 1))
story.append(body(
    "NCERT's ten exercise questions for this chapter, and the two things they assume but the "
    "chapter never states outright. Everything below is built only from statements already made in "
    "this chapter."))
story.append(data_table([
    ["#", "NCERT exercise question", "Where the chapter answers it"],
    ["1", "List the attributes that populations possess but not individuals.",
     "11.1.1 - <b>birth rates and death rates</b> (per capita), <b>sex ratio</b>, <b>age "
     "distribution / age pyramid</b>, and <b>population density (N)</b>"],
    ["2", "If a population growing exponentially double in size in 3 years, what is the intrinsic "
     "rate of increase (r) of the population?",
     "Use the chapter's own integral equation - worked below"],
    ["3", "Name important defence mechanisms in plants against herbivory.",
     "11.1.4 (i) - <b>thorns</b> (<i>Acacia</i>, <i>Cactus</i>) and <b>chemical defences</b> "
     "(<i>Calotropis</i> cardiac glycosides; nicotine, caffeine, quinine, strychnine, opium)"],
    ["4", "An orchid plant is growing on the branch of mango tree. How do you describe this "
     "interaction between the orchid and the mango tree?",
     "11.1.4 (iv) - <b>commensalism</b>: the orchid (an <b>epiphyte</b>) benefits, the mango tree "
     "is neither harmed nor benefited"],
    ["5", "What is the ecological principle behind the biological control method of managing with "
     "pest insects?",
     "11.1.4 (i) - the ability of the <b>predator to regulate prey population</b> (as with the "
     "cactus-feeding moth in Australia)"],
    ["6", "Define population and community.",
     "<b>Population</b> - 11.1.1; <b>community</b> - not defined outright in the body, so it is "
     "stated below"],
    ["7", "Define the following terms and give one example for each: (a) Commensalism "
     "(b) Parasitism (c) Camouflage (d) Mutualism (e) Interspecific competition",
     "11.1.4 - (a) cattle egret and grazing cattle; (b) lice on humans / <i>Cuscuta</i>; "
     "(c) cryptically-coloured insects and frogs; (d) lichens (fungus + algae or cyanobacteria); "
     "(e) flamingoes and resident fishes competing for zooplankton"],
    ["8", "With the help of suitable diagram describe the logistic population growth curve.",
     "11.1.2 (ii) with <b>Figure 11.3</b> curve <b>b</b> - lag, acceleration, deceleration, "
     "asymptote at <b>K</b>; dN/dt = rN [(K - N)/K]"],
    ["9", "Select the statement which explains best parasitism. (a) One organism is benefited. "
     "(b) Both the organisms are benefited. (c) One organism is benefited, other is not affected. "
     "(d) One organism is benefited, other is affected.",
     "11.1.4 / Table 11.1 - parasitism is <b>+ -</b>, so <b>(d) one organism is benefited, other "
     "is affected</b>"],
    ["10", "List any three important characteristics of a population and explain.",
     "11.1.1 - e.g. <b>population density (N)</b>, <b>sex ratio</b> and <b>age distribution</b>; "
     "also birth rates and death rates"],
], col_widths=[0.5, 5.1, 5.0]))
story.append(heading("Appendix", "Community (assumed by Exercise 6)", 3))
story.append(body(
    "The chapter never gives <b>community</b> a one-line definition; it says only that in nature "
    "animals, plants and microbes <b>interact in various ways to form a biological community</b>, "
    "and that <b>communities</b> are one of ecology's four levels of biological organisation. Put "
    "together, from the chapter's own two statements: a <b>community</b> is the <b>populations of "
    "the different species living together in a habitat and interacting with one another</b>, the "
    "level of organisation just above the population."))
story.append(heading("Appendix", "Solving for r from a doubling time (Exercise 2)", 3))
story.append(body(
    "The chapter supplies the equation and the constant but never demonstrates rearranging it. "
    "Using only chapter content - <b>N<sub>t</sub> = N<sub>0</sub> e<super>rt</super></b> with "
    "<b>e = 2.71828</b>:"))
story.append(process_flow([
    "The population <b>doubles</b>, so N<sub>t</sub>/N<sub>0</sub> = <b>2</b>, and <b>t = 3 "
    "years</b>.",
    "Substituting: <b>2 = e<super>3r</super></b>.",
    "Taking natural logarithms of both sides: <b>3r = natural log of 2 = 0.6931</b>.",
    "So <b>r = 0.6931/3 = 0.2310 per year</b> (about <b>0.231</b>).",
]))
story.append(note(
    "Compare this <b>r = 0.231</b> with the chapter's own r values - <b>0.015</b> for the Norway "
    "rat, <b>0.12</b> for the flour beetle and <b>0.0205</b> for the human population in India in "
    "<b>1981</b>. A doubling in 3 years is a very high intrinsic rate of natural increase."))

story.append(Spacer(1, 6))
story.append(Paragraph(
    "<i>Every fact, number, name, qualifier, table row, figure and figure label in NCERT Class 12 "
    "Chapter 11 is carried above. Nothing outside the source chapter has been added, except the "
    "clearly marked MEMORY AID boxes.</i>", STYLES["Caption"]))


def main():
    return build_pdf(
        OUT_PDF, story,
        title="Class 12 Chapter 11 - Organisms and Populations (NEET notes)",
        subject="NEET Biology",
    )


if __name__ == "__main__":
    sys.exit(main())
