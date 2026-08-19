"""
Class 11 - Chapter 2: Biological Classification  (NEET replacement notes)

Generated per SUPREME COMMAND PROMPT.md v6. Styles, geometry, badges, boxes,
tables, process flows and figure framing all come from the repo-level frozen
module `neet_template.py` (§0.6) - nothing style-level is re-declared here.

Source of truth: Chapter/class 11/Chapter 02 - Biological Classification.pdf (13 pages)
Frozen inventory: Ch2_BiologicalClassification_inventory.md
                  (192 Facts rows F001-F192 + 6 figure-label rows L01-L06)

Source-spelling policy (Ch1 convention, §4 Rule 4 + Coverage note):
NCERT's own spellings are preserved verbatim wherever the term itself is what a
marks-scheme would test, with the standard form given alongside in brackets the
first time it appears. Treated this way in this chapter:
  "Vibrium (pl.: vibrio)"   - NCERT's genus spelling for the comma-shaped form
  "Paramoecium"             - NCERT's spelling of Paramecium
  "Mucilagenous sheath"     - as printed inside Figure 2.2
  "diaseases"               - NCERT typo, normalised to "diseases" in running prose
  "dueteromycetes"          - NCERT typo in 2.3.4, normalised to "deuteromycetes"
No source FACT is altered by this policy - only the two obvious typos are
normalised in running prose, and both are recorded here and in the inventory.

Every block below carries its NCERT section number as a `# ---- N.N ----`
marker so a verification fix can be located and edited in seconds.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE
while not os.path.exists(os.path.join(ROOT, "neet_template.py")):
    parent = os.path.dirname(ROOT)
    if parent == ROOT:
        raise RuntimeError("neet_template.py not found in any parent directory")
    ROOT = parent
sys.path.insert(0, ROOT)

from reportlab.platypus import Paragraph, Spacer, KeepTogether
from reportlab.lib.units import cm

from neet_template import (
    STYLES, FRAME_WIDTH, DARK_GREY, GRID_LINE,
    heading, keyterm, process_flow, note, memory_aid, data_table, title_block, build_pdf,
)
from neet_template import figure as _shared_figure

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch2_BiologicalClassification.pdf")


def figure(asset_name, caption_text, max_width_cm=15.9):
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

# ---- Title block ----
story += title_block("Biological Classification")

# ---- 2.0 Chapter opening - why classification kept changing ----
story.append(heading("2.0", "Why Classification Systems Kept Changing", level=1))
story.append(body("<b>Since the dawn of civilisation, there have been many attempts to classify "
                  "living organisms.</b> It was done <b>instinctively</b> - not using criteria that "
                  "were scientific, but <b>borne out of a need to use organisms for our own use</b>: "
                  "for <b>food, shelter and clothing</b>."))
story.append(b1("<b>Aristotle was the earliest to attempt a more scientific basis for "
                "classification.</b> He used <b>simple morphological characters</b> to classify "
                "plants into <b>trees, shrubs and herbs</b>. He also divided animals into "
                "<b>two groups</b>: those which had <b>red blood</b> and those that did not."))
story.append(b1("<b>In Linnaeus' time a Two Kingdom system</b> of classification with "
                "<b>Plantae and Animalia</b> kingdoms was developed, that included all plants and "
                "animals respectively."))
story.append(body("That two kingdom system carried a specific weakness - <b>it did not "
                  "distinguish between</b>:"))
story.append(b2("the <b>eukaryotes and prokaryotes</b>,"))
story.append(b2("<b>unicellular and multicellular</b> organisms, and"))
story.append(b2("<b>photosynthetic (green algae)</b> and <b>non-photosynthetic (fungi)</b> "
                "organisms."))
story.append(b1("Classification of organisms into plants and animals <b>was easily done and was "
                "easy to understand</b>, but <b>a large number of organisms did not fall into "
                "either category</b>. Hence the two kingdom classification used for a long time "
                "was found <b>inadequate</b>."))
story.append(b1("Besides gross morphology, a need was also felt for including other "
                "characteristics like <b>cell structure, nature of wall, mode of nutrition, "
                "habitat, methods of reproduction, evolutionary relationships,</b> etc."))
story.append(b1("<b>Classification systems for the living organisms have hence, undergone several "
                "changes over the time.</b> Though plant and animal kingdoms have been a "
                "<b>constant</b> under all different systems, the understanding of <b>what "
                "groups/organisms be included</b> under these kingdoms have been changing; the "
                "<b>number and nature of other kingdoms</b> have also been understood differently "
                "by different scientists over the time."))

# ---- 2.1(intro) Whittaker's five kingdom classification ----
story.append(heading("2.1", "Whittaker's Five Kingdom Classification", level=1))
story.append(body("<b>R.H. Whittaker (1969) proposed a Five Kingdom Classification.</b> The "
                  "kingdoms defined by him were named <b>Monera, Protista, Fungi, Plantae</b> and "
                  "<b>Animalia</b>."))
story.append(keyterm("<b>The main criteria for classification used by him include cell structure, "
                     "body organisation, mode of nutrition, reproduction</b> and <b>phylogenetic "
                     "relationships.</b>"))
story.append(b1("<b>Table 2.1 gives a comparative account of different characteristics of the "
                "five kingdoms</b> - it is the single most examinable table in this chapter."))
story.append(b1("A <b>three-domain system</b> has also been proposed, that divides the "
                "<b>Kingdom Monera into two domains</b>, leaving the remaining eukaryotic kingdoms "
                "in the <b>third domain</b>, and thereby a <b>six kingdom classification</b>. "
                "(You will learn about this system in detail in higher classes.)"))

# ---- Table 2.1 (verbatim from source) ----
story.append(heading("T 2.1", "Characteristics of the Five Kingdoms", level=2, has_table=True))
story.append(data_table([
    ["Characters", "Monera", "Protista", "Fungi", "Plantae", "Animalia"],
    ["Cell type", "Prokaryotic", "Eukaryotic", "Eukaryotic", "Eukaryotic", "Eukaryotic"],
    ["Cell wall", "Noncellulosic (Polysaccharide + amino acid)", "Present in some",
     "Present (with chitin)", "Present (cellulose)", "Absent"],
    ["Nuclear membrane", "Absent", "Present", "Present", "Present", "Present"],
    ["Body organisation", "Cellular", "Cellular", "Multicellular/ loose tissue", "Tissue/ organ",
     "Tissue/organ/ organ system"],
    ["Mode of nutrition",
     "Autotrophic (chemosynthetic and photosynthetic) and Heterotrophic (saprophytic/parasitic)",
     "Autotrophic (Photosynthetic) and Heterotrophic", "Heterotrophic (Saprophytic/Parasitic)",
     "Autotrophic (Photosynthetic)", "Heterotrophic (Holozoic/ Saprophytic etc.)"],
], col_widths=[1.5, 1.75, 1.5, 1.5, 1.4, 1.55], font_size=8.2))

# ---- 2.1(intro) continued - the issues that drove the regrouping ----
story.append(heading("2.1a", "What Drove the Regrouping - The 'Plants' Problem", level=2))
story.append(body("Let us look at this five kingdom classification to understand the "
                  "<b>issues and considerations</b> that influenced the classification system."))
story.append(b1("<b>Earlier classification systems included bacteria, blue green algae, fungi, "
                "mosses, ferns, gymnosperms and the angiosperms under 'Plants'.</b> The character "
                "that <b>unified this whole kingdom</b> was that all the organisms included had a "
                "<b>cell wall</b> in their cells."))
story.append(b1("This <b>placed together groups which widely differed in other "
                "characteristics</b>. It brought together the <b>prokaryotic bacteria</b> and the "
                "<b>blue green algae (cyanobacteria)</b> with other groups which were "
                "<b>eukaryotic</b>."))
story.append(b1("It also grouped together the <b>unicellular</b> organisms and the "
                "<b>multicellular</b> ones - say, for example, <i>Chlamydomonas</i> and "
                "<i>Spirogyra</i> were placed together under <b>algae</b>."))
story.append(b1("The classification <b>did not differentiate between the heterotrophic group - "
                "fungi, and the autotrophic green plants</b>, though they also showed a "
                "characteristic difference in their <b>walls composition</b>: the <b>fungi had "
                "chitin</b> in their walls while the <b>green plants had a cellulosic cell "
                "wall</b>."))
story.append(b1("When such characteristics were considered, the fungi were placed in a separate "
                "kingdom - <b>Kingdom Fungi</b>. <b>All prokaryotic organisms were grouped together "
                "under Kingdom Monera</b> and the <b>unicellular eukaryotic organisms were placed "
                "in Kingdom Protista</b>."))
story.append(b1("<b>Kingdom Protista has brought together</b> <i>Chlamydomonas</i>, "
                "<i>Chlorella</i> (earlier placed in Algae within Plants, and both having cell "
                "walls) with <b>Paramoecium</b> and <i>Amoeba</i> (which were earlier placed in the "
                "animal kingdom, which lack cell wall). Note NCERT's spelling <b>Paramoecium</b> "
                "(= <i>Paramecium</i>), used throughout this chapter."))
story.append(b1("It has put together organisms which, <b>in earlier classifications, were placed "
                "in different kingdoms</b>. <b>This happened because the criteria for "
                "classification changed.</b> This kind of changes <b>will take place in future "
                "too</b>, depending on the improvement in our understanding of characteristics and "
                "evolutionary relationships."))
story.append(b1("Over time, an attempt has been made to evolve a classification system which "
                "reflects <b>not only the morphological, physiological and reproductive "
                "similarities, but is also phylogenetic</b>, i.e., is <b>based on evolutionary "
                "relationships</b>."))
story.append(note("In this chapter we will study characteristics of <b>Kingdoms Monera, Protista "
                  "and Fungi</b> of the Whittaker system of classification. The Kingdoms "
                  "<b>Plantae</b> and <b>Animalia</b>, commonly referred to as plant and animal "
                  "kingdoms respectively, will be dealt separately in <b>chapters 3 and 4</b> - so "
                  "sections 2.4 and 2.5 below are deliberately brief in NCERT itself."))

# ---- 2.1 KINGDOM MONERA ----
story.append(heading("2.1", "Kingdom Monera - Bacteria", level=1))
story.append(body("<b>Bacteria are the sole members of the Kingdom Monera.</b> They are the "
                  "<b>most abundant micro-organisms</b>."))
story.append(b1("<b>Bacteria occur almost everywhere.</b> <b>Hundreds of bacteria are present in "
                "a handful of soil.</b> The chapter summary states the same distribution fact in "
                "its own words: <b>bacteria are cosmopolitan in distribution</b>."))
story.append(b1("They also live in <b>extreme habitats</b> such as <b>hot springs, deserts, snow "
                "and deep oceans</b>, where very few other life forms can survive."))
story.append(b1("<b>Many of them live in or on other organisms as parasites.</b>"))
story.append(body("<b>Bacteria are grouped under four categories based on their shape</b> "
                  "(Figure 2.1):"))
story.append(data_table([
    ["Shape category", "Genus name (NCERT)", "Plural form", "Shape"],
    ["Spherical", "<b>Coccus</b>", "cocci", "Ball-shaped"],
    ["Rod-shaped", "<b>Bacillus</b>", "bacilli", "Rod"],
    ["Comma-shaped", "<b>Vibrium</b>", "vibrio", "Comma"],
    ["Spiral", "<b>Spirillum</b>", "spirilla", "Spiral/coiled"],
], col_widths=[2.0, 2.2, 1.6, 2.4]))
story.append(note("NCERT prints the comma-shaped genus as <b>Vibrium (pl.: vibrio)</b>; the "
                  "widely used form elsewhere is <i>Vibrio</i>. The <b>NCERT spelling is kept "
                  "here</b> because the term itself is what an examination tests. Figure 2.1 labels "
                  "the comma-shaped cells <b>Vibrio</b>."))
story.append(figure("fig_2_1.png",
                    "<b>Fig. 2.1</b> - Bacteria of different shapes. The four shape categories are "
                    "labelled <b>Cocci</b> (spherical), <b>Bacilli</b> (rod-shaped), <b>Spirilla</b> "
                    "(spiral) and <b>Vibrio</b> (comma-shaped). Two further structures are labelled "
                    "on the drawing: a <b>Spore</b> inside a bacillus, and a <b>Flagellum</b> - the "
                    "motility structure - on the spirillum.",
                    max_width_cm=15.5))
story.append(b1("Though the <b>bacterial structure is very simple, they are very complex in "
                "behaviour</b>. Compared to many other organisms, <b>bacteria as a group show the "
                "most extensive metabolic diversity</b>."))
story.append(b1("<b>Some of the bacteria are autotrophic</b>, i.e., they <b>synthesise their own "
                "food from inorganic substrates</b>. They may be <b>photosynthetic autotrophic</b> "
                "or <b>chemosynthetic autotrophic</b>."))
story.append(b1("<b>The vast majority of bacteria are heterotrophs</b>, i.e., they depend on "
                "<b>other organisms or on dead organic matter</b> for food."))

# ---- 2.1.1 Archaebacteria ----
story.append(heading("2.1.1", "Archaebacteria", level=2))
story.append(body("These bacteria are <b>special since they live in some of the most harsh "
                  "habitats</b>. NCERT names three habitats, each with its own group name:"))
story.append(data_table([
    ["Harsh habitat", "Group name"],
    ["Extreme salty areas", "<b>halophiles</b>"],
    ["Hot springs", "<b>thermoacidophiles</b>"],
    ["Marshy areas", "<b>methanogens</b>"],
], col_widths=[4.0, 4.0]))
story.append(b1("<b>Archaebacteria differ from other bacteria in having a different cell wall "
                "structure</b>, and <b>this feature is responsible for their survival in extreme "
                "conditions</b>."))
story.append(b1("<b>Methanogens are present in the gut of several ruminant animals</b> such as "
                "<b>cows and buffaloes</b>, and they are responsible for the <b>production of "
                "methane (biogas) from the dung</b> of these animals."))
story.append(memory_aid("Three archaebacterial habitats - <b>'Salt, Heat, Marsh'</b>: "
                        "<b>Halo</b>philes = salt (halo = salt), <b>Thermo</b>acidophiles = hot "
                        "springs (thermo = heat), <b>Methano</b>gens = marshy areas and ruminant "
                        "gut (they generate methane)."))

# ---- 2.1.2 Eubacteria ----
story.append(heading("2.1.2", "Eubacteria - 'True Bacteria'", level=2))
story.append(body("<b>There are thousands of different eubacteria or 'true bacteria'.</b> They are "
                  "characterised by the presence of a <b>rigid cell wall</b>, and <b>if motile, a "
                  "flagellum</b>."))

story.append(heading("2.1.2a", "Cyanobacteria (Blue-Green Algae)", level=3))
story.append(b1("<b>The cyanobacteria</b> (also referred to as <b>blue-green algae</b>) have "
                "<b>chlorophyll <i>a</i></b> similar to green plants and are <b>photosynthetic "
                "autotrophs</b> (Figure 2.2)."))
story.append(b1("The cyanobacteria are <b>unicellular, colonial or filamentous</b>, and "
                "<b>freshwater/marine or terrestrial</b> algae."))
story.append(b1("<b>The colonies are generally surrounded by gelatinous sheath.</b> In Figure 2.2 "
                "this envelope around the filament is labelled the <b>Mucilagenous sheath</b> "
                "(NCERT's spelling as printed on the figure; standard form 'mucilaginous')."))
story.append(b1("<b>They often form blooms in polluted water bodies.</b>"))
story.append(b1("<b>Some of these organisms can fix atmospheric nitrogen in specialised cells "
                "called heterocysts</b>, e.g., <i>Nostoc</i> and <i>Anabaena</i>. The "
                "<b>Heterocyst</b> is the thick-walled cell labelled in Figure 2.2."))
story.append(figure("fig_2_2.png",
                    "<b>Fig. 2.2</b> - A filamentous blue-green algae - <i>Nostoc</i>. Two "
                    "structures are labelled on the filament: the <b>Heterocyst</b>, the specialised "
                    "cell in which atmospheric nitrogen is fixed, and the <b>Mucilagenous sheath</b>, "
                    "the gelatinous envelope that generally surrounds the colony.",
                    max_width_cm=7.6))
story.append(note("<b>Algal bloom</b> is the exact term Exercise 4 asks about. NCERT's body text "
                  "states the phenomenon as cyanobacteria that <b>'often form blooms in polluted "
                  "water bodies'</b> - a rapid build-up of algal growth in a water body. Compare "
                  "this with <b>red tides</b> (section 2.2.2), which are caused by red "
                  "dinoflagellates, not by cyanobacteria."))

story.append(heading("2.1.2b", "Chemosynthetic Autotrophic Bacteria", level=3))
story.append(b1("<b>Chemosynthetic autotrophic bacteria oxidise various inorganic substances</b> "
                "such as <b>nitrates, nitrites and ammonia</b>, and <b>use the released energy for "
                "their ATP production</b>."))
story.append(b1("<b>They play a great role in recycling nutrients</b> like <b>nitrogen, "
                "phosphorous, iron and sulphur</b>."))

story.append(heading("2.1.2c", "Heterotrophic Bacteria", level=3))
story.append(b1("<b>Heterotrophic bacteria are most abundant in nature.</b> <b>The majority are "
                "important decomposers.</b>"))
story.append(b1("<b>Many of them have a significant impact on human affairs.</b> They are helpful "
                "in <b>making curd from milk</b>, <b>production of antibiotics</b>, <b>fixing "
                "nitrogen in legume roots</b>, etc."))
story.append(b1("<b>Some are pathogens causing damage to human beings, crops, farm animals and "
                "pets.</b> <b>Cholera, typhoid, tetanus, citrus canker</b> are well known diseases "
                "caused by different bacteria."))

story.append(heading("2.1.2d", "Reproduction in Bacteria", level=3))
story.append(b1("<b>Bacteria reproduce mainly by fission</b> (Figure 2.3)."))
story.append(b1("<b>Sometimes, under unfavourable conditions, they produce spores.</b>"))
story.append(b1("<b>They also reproduce by a sort of sexual reproduction</b> by adopting a "
                "<b>primitive type of DNA transfer</b> from one bacterium to the other."))
story.append(figure("fig_2_3.png",
                    "<b>Fig. 2.3</b> - A dividing bacterium. Three structures are labelled: the "
                    "outer <b>Cell wall</b>, the <b>Cell membrane</b> lying inside it, and the "
                    "<b>DNA</b> - the genetic material that is copied and separated as the cell "
                    "divides by fission.",
                    max_width_cm=9.5))

story.append(heading("2.1.2e", "Mycoplasma", level=3))
story.append(keyterm("<b>The Mycoplasma are organisms that completely lack a cell wall.</b> They "
                     "are the <b>smallest living cells known</b> and <b>can survive without "
                     "oxygen</b>. <b>Many mycoplasma are pathogenic in animals and plants.</b>"))
story.append(memory_aid("Monera extremes worth remembering: <b>Mycoplasma</b> = smallest living "
                        "cells known + <b>no cell wall at all</b> + survives without oxygen; "
                        "<b>Archaebacteria</b> = a <b>different cell wall structure</b>, which is "
                        "what lets them survive harsh habitats. One has no wall, the other has an "
                        "unusual wall."))

# ---- 2.2 KINGDOM PROTISTA ----
story.append(heading("2.2", "Kingdom Protista", level=1))
story.append(body("<b>All single-celled eukaryotes are placed under Protista, but the boundaries "
                  "of this kingdom are not well defined.</b> <b>What may be 'a photosynthetic "
                  "protistan' to one biologist may be 'a plant' to another.</b>"))
story.append(b1("<b>In this book we include Chrysophytes, Dinoflagellates, Euglenoids, Slime "
                "moulds and Protozoans under Protista.</b>"))
story.append(b1("<b>Members of Protista are primarily aquatic.</b> <b>This kingdom forms a link "
                "with the others dealing with plants, animals and fungi.</b>"))
story.append(b1("<b>Being eukaryotes, the protistan cell body contains a well defined nucleus and "
                "other membrane-bound organelles.</b> <b>Some have flagella or cilia.</b>"))
story.append(b1("<b>Protists reproduce asexually and sexually</b> by a process involving <b>cell "
                "fusion and zygote formation</b>."))

# ---- 2.2.1 Chrysophytes ----
story.append(heading("2.2.1", "Chrysophytes", level=2))
story.append(b1("<b>This group includes diatoms and golden algae (desmids).</b> They are found in "
                "<b>fresh water as well as in marine environments</b>."))
story.append(b1("<b>They are microscopic and float passively in water currents (plankton).</b> "
                "<b>Most of them are photosynthetic.</b>"))
story.append(b1("<b>In diatoms the cell walls form two thin overlapping shells, which fit together "
                "as in a soap box.</b> <b>The walls are embedded with silica and thus the walls are "
                "indestructible.</b>"))
story.append(b1("Thus, <b>diatoms have left behind large amount of cell wall deposits in their "
                "habitat</b>; this accumulation <b>over billions of years</b> is referred to as "
                "<b>'diatomaceous earth'</b>."))
story.append(b1("<b>Being gritty this soil is used in polishing, filtration of oils and "
                "syrups.</b>"))
story.append(b1("<b>Diatoms are the chief 'producers' in the oceans.</b>"))

# ---- 2.2.2 Dinoflagellates ----
story.append(heading("2.2.2", "Dinoflagellates", level=2))
story.append(b1("These organisms are <b>mostly marine and photosynthetic</b>."))
story.append(b1("<b>They appear yellow, green, brown, blue or red depending on the main pigments "
                "present in their cells.</b>"))
story.append(b1("<b>The cell wall has stiff cellulose plates on the outer surface.</b>"))
story.append(b1("<b>Most of them have two flagella</b>; <b>one lies longitudinally and the other "
                "transversely in a furrow between the wall plates</b>."))
story.append(b1("<b>Very often, red dinoflagellates (Example: <i>Gonyaulax</i>) undergo such rapid "
                "multiplication that they make the sea appear red (red tides).</b>"))
story.append(b1("<b>Toxins released by such large numbers may even kill other marine animals such "
                "as fishes.</b>"))

# ---- 2.2.3 Euglenoids ----
story.append(heading("2.2.3", "Euglenoids", level=2))
story.append(b1("<b>Majority of them are fresh water organisms found in stagnant water.</b>"))
story.append(b1("<b>Instead of a cell wall, they have a protein rich layer called pellicle which "
                "makes their body flexible.</b>"))
story.append(b1("<b>They have two flagella, a short and a long one.</b>"))
story.append(b1("<b>Though they are photosynthetic in the presence of sunlight, when deprived of "
                "sunlight they behave like heterotrophs by predating on other smaller "
                "organisms.</b>"))
story.append(b1("<b>Interestingly, the pigments of euglenoids are identical to those present in "
                "higher plants.</b> Example: <i>Euglena</i> (Figure 2.4b)."))

# ---- 2.2.4 Slime Moulds ----
story.append(heading("2.2.4", "Slime Moulds", level=2))
story.append(b1("<b>Slime moulds are saprophytic protists.</b> <b>The body moves along decaying "
                "twigs and leaves engulfing organic material.</b>"))
story.append(b1("<b>Under suitable conditions, they form an aggregation called plasmodium which "
                "may grow and spread over several feet.</b>"))
story.append(b1("<b>During unfavourable conditions, the plasmodium differentiates and forms "
                "fruiting bodies bearing spores at their tips.</b>"))
story.append(b1("<b>The spores possess true walls.</b> <b>They are extremely resistant and survive "
                "for many years, even under adverse conditions.</b> <b>The spores are dispersed by "
                "air currents.</b>"))

# ---- 2.2.5 Protozoans ----
story.append(heading("2.2.5", "Protozoans - The Four Major Groups", level=2))
story.append(b1("<b>All protozoans are heterotrophs and live as predators or parasites.</b> "
                "<b>They are believed to be primitive relatives of animals.</b>"))
story.append(body("<b>There are four major groups of protozoans.</b>"))
story.append(data_table([
    ["Group", "Locomotion / key structure", "Habitat and nutrition", "NCERT examples"],
    ["<b>Amoeboid protozoans</b>",
     "Move and capture prey by putting out <b>pseudopodia (false feet)</b>",
     "Live in <b>fresh water, sea water or moist soil</b>; <b>marine forms have silica shells</b> "
     "on their surface",
     "<i>Amoeba</i>; <i>Entamoeba</i> (a parasite)"],
    ["<b>Flagellated protozoans</b>", "<b>They have flagella</b>",
     "Either <b>free-living or parasitic</b>; the parasitic forms cause diseases such as "
     "<b>sleeping sickness</b>",
     "<i>Trypanosoma</i>"],
    ["<b>Ciliated protozoans</b>",
     "<b>Thousands of cilia</b>; a cavity (<b>gullet</b>) that opens to the outside of the cell "
     "surface. <b>Coordinated movement of rows of cilia</b> steers water laden with food into the "
     "gullet",
     "<b>Aquatic, actively moving</b> organisms",
     "<b>Paramoecium</b> (Figure 2.4d)"],
    ["<b>Sporozoans</b>", "Have an <b>infectious spore-like stage</b> in their life cycle",
     "Diverse organisms; the most notorious causes <b>malaria</b>, a disease which has a "
     "<b>staggering effect on human population</b>",
     "<i>Plasmodium</i> (malarial parasite)"],
], col_widths=[2.1, 4.0, 4.6, 3.2], font_size=8.6))
story.append(note("NCERT prints <b>'diaseases'</b> in the flagellated-protozoans sentence "
                  "('The parasitic forms cause diaseases such as sleeping sickness'). This is a "
                  "typographical slip in the source and is written as <b>diseases</b> in the table "
                  "above; the fact itself is unchanged."))
story.append(figure("fig_2_4.png",
                    "<b>Fig. 2.4</b> - Representative protists: <b>(a)</b> Dinoflagellates, "
                    "<b>(b)</b> <i>Euglena</i>, <b>(c)</b> Slime mould, <b>(d)</b> "
                    "<b>Paramoecium</b>. The four drawings carry only the panel markers "
                    "<b>panel (a)</b>, <b>panel (b)</b>, <b>panel (c)</b> and <b>panel (d)</b>; "
                    "each organism is identified by this caption. Dinoflagellates in panel (a) "
                    "appear yellow, green, brown, blue or red in life depending on their main "
                    "pigments - that colour difference cannot be shown in a monochrome print, so "
                    "it is stated here in words.",
                    max_width_cm=6.6))
