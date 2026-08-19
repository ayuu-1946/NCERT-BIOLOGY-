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

# ---- 2.3 KINGDOM FUNGI ----
story.append(heading("2.3", "Kingdom Fungi", level=1))
story.append(b1("<b>The fungi constitute a unique kingdom of heterotrophic organisms.</b> "
                "<b>They show a great diversity in morphology and habitat.</b>"))
story.append(body("Where you have already met fungi, in NCERT's own examples:"))
story.append(b2("On a <b>moist bread</b> and <b>rotten fruits</b>."))
story.append(b2("<b>The common mushroom you eat</b> and <b>toadstools</b> are also fungi."))
story.append(b2("<b>White spots seen on mustard leaves</b> are due to a <b>parasitic fungus</b>."))
story.append(b2("Some <b>unicellular fungi, e.g., yeast</b>, are used to <b>make bread and "
                "beer</b>."))
story.append(b2("Other fungi <b>cause diseases in plants and animals</b>; <b>wheat rust-causing "
                "<i>Puccinia</i></b> is an important example."))
story.append(b2("Some are the <b>source of antibiotics, e.g., <i>Penicillium</i></b>."))
story.append(b1("<b>Fungi are cosmopolitan</b> and occur in <b>air, water, soil and on animals "
                "and plants</b>. <b>They prefer to grow in warm and humid places</b>."))
story.append(note("This is where NCERT uses the word <b>cosmopolitan</b> - it is applied to "
                  "<b>fungi</b> here, and the chapter summary applies it to bacteria as well "
                  "(see Kingdom Monera). Keep the term attached to both in your recall, but note "
                  "that the body text says of bacteria only that they <b>occur almost "
                  "everywhere</b>."))
story.append(b1("This is also why we keep food in the <b>refrigerator</b> - <b>to prevent food "
                "from going bad due to bacterial or fungal infections</b>."))

story.append(heading("2.3a", "Structure of the Fungal Body", level=2))
story.append(b1("<b>With the exception of yeasts which are unicellular, fungi are "
                "filamentous.</b>"))
story.append(keyterm("Their bodies consist of long, slender thread-like structures called "
                     "<b>hyphae</b>. The network of hyphae is known as <b>mycelium</b>."))
story.append(b1("Two kinds of hyphae are distinguished:"))
story.append(b2("<b>Coenocytic hyphae</b> - some hyphae are <b>continuous tubes filled with "
                "multinucleated cytoplasm</b>."))
story.append(b2("Others have <b>septae or cross walls</b> in their hyphae."))
story.append(b1("<b>The cell walls of fungi are composed of chitin and polysaccharides.</b>"))
story.append(memory_aid("Cell-wall chemistry across the kingdoms, in one line: "
                        "<b>Monera = noncellulosic (polysaccharide + amino acid)</b>, "
                        "<b>Fungi = chitin + polysaccharides</b>, <b>Plantae = cellulose</b>, "
                        "<b>Animalia = no cell wall</b>. Only the fungal wall carries "
                        "<b>chitin</b>."))

story.append(heading("2.3b", "Modes of Nutrition", level=2))
story.append(keyterm("<b>Most fungi are heterotrophic and absorb soluble organic matter from "
                     "dead substrates and hence are called saprophytes.</b> Stated the short way, "
                     "as the chapter summary puts it: <b>most fungi are saprophytic in their mode "
                     "of nutrition</b>."))
story.append(b1("<b>Those that depend on living plants and animals are called parasites.</b>"))
story.append(b1("<b>They can also live as symbionts</b> - <b>in association with algae as "
                "lichens</b> and <b>with roots of higher plants as mycorrhiza</b>."))
story.append(note("The <b>lichen</b> partnership named here is taken up in full in section 2.6 "
                  "of this chapter, where the algal partner is named <b>phycobiont</b> and the "
                  "fungal partner <b>mycobiont</b>."))

story.append(heading("2.3c", "Reproduction in Fungi", level=2))
story.append(b1("<b>Reproduction in fungi can take place by vegetative means - fragmentation, "
                "fission and budding.</b>"))
story.append(keyterm("<b>Asexual reproduction is by spores called conidia or sporangiospores or "
                     "zoospores</b>, and <b>sexual reproduction is by oospores, ascospores and "
                     "basidiospores</b>."))
story.append(b1("<b>The various spores are produced in distinct structures called fruiting "
                "bodies.</b>"))
story.append(body("<b>The sexual cycle involves the following three steps:</b>"))
story.append(process_flow([
    "<b>Plasmogamy</b> - <b>fusion of protoplasms between two motile or non-motile gametes</b>.",
    "<b>Karyogamy</b> - <b>fusion of two nuclei</b>.",
    "<b>Meiosis in zygote</b>, <b>resulting in haploid spores</b>.",
]))
story.append(b1("<b>When a fungus reproduces sexually, two haploid hyphae of compatible mating "
                "types come together and fuse.</b> What happens next differs between groups:"))
story.append(b2("<b>In some fungi the fusion of two haploid cells immediately results in diploid "
                "cells (2n).</b>"))
story.append(b2("<b>However, in other fungi (ascomycetes and basidiomycetes), an intervening "
                "dikaryotic stage (n + n, i.e., two nuclei per cell) occurs</b>; such a condition "
                "is called a <b>dikaryon</b> and the phase is called <b>dikaryophase of "
                "fungus</b>."))
story.append(b1("<b>Later, the parental nuclei fuse and the cells become diploid.</b> <b>The fungi "
                "form fruiting bodies in which reduction division occurs, leading to formation of "
                "haploid spores.</b>"))
story.append(keyterm("<b>The morphology of the mycelium, mode of spore formation and fruiting "
                     "bodies form the basis for the division of the kingdom into various "
                     "classes.</b>"))
story.append(memory_aid("The two-step nuclear sequence never changes: <b>plasmogamy before "
                        "karyogamy</b> - cytoplasms first, nuclei second. The <b>dikaryon "
                        "(n + n)</b> is what sits between them in <b>ascomycetes and "
                        "basidiomycetes</b>."))

# ---- 2.3.1 Phycomycetes ----
story.append(heading("2.3.1", "Phycomycetes", level=2))
story.append(b1("<b>Found in aquatic habitats and on decaying wood in moist and damp places or as "
                "obligate parasites on plants.</b>"))
story.append(b1("<b>The mycelium is aseptate and coenocytic.</b>"))
story.append(b1("<b>Asexual reproduction takes place by zoospores (motile) or by aplanospores "
                "(non-motile).</b> <b>These spores are endogenously produced in sporangium.</b>"))
story.append(b1("<b>A zygospore is formed by fusion of two gametes.</b> <b>These gametes are "
                "similar in morphology (isogamous) or dissimilar (anisogamous or oogamous).</b>"))
story.append(b1("<b>Some common examples are <i>Mucor</i></b> (Figure 2.5a), "
                "<b><i>Rhizopus</i></b> (<b>the bread mould mentioned earlier</b>) and "
                "<b><i>Albugo</i></b> (<b>the parasitic fungi on mustard</b>)."))
story.append(note("<b><i>Albugo</i></b> closes the loop on the white spots on mustard leaves "
                  "mentioned at the start of this kingdom, and <b><i>Rhizopus</i></b> is the mould "
                  "on the moist bread. <b>Aplanospores are non-motile</b> and <b>zoospores are "
                  "motile</b> - the distinction is asked for directly."))

# ---- 2.3.2 Ascomycetes ----
story.append(heading("2.3.2", "Ascomycetes", level=2))
story.append(keyterm("<b>Commonly known as sac-fungi</b>, the ascomycetes are <b>mostly "
                     "multicellular, e.g., <i>Penicillium</i>, or rarely unicellular, e.g., yeast "
                     "(<i>Saccharomyces</i>)</b>."))
story.append(b1("<b>They are saprophytic, decomposers, parasitic or coprophilous (growing on "
                "dung).</b> <b>Mycelium is branched and septate.</b>"))
story.append(b1("<b>The asexual spores are conidia produced exogenously on the special mycelium "
                "called conidiophores.</b> <b>Conidia on germination produce mycelium.</b>"))
story.append(b1("<b>Sexual spores are called ascospores which are produced endogenously in sac "
                "like asci (singular ascus).</b> <b>These asci are arranged in different types of "
                "fruiting bodies called ascocarps.</b>"))
story.append(b1("<b>Some examples are <i>Aspergillus</i></b> (Figure 2.5b), "
                "<b><i>Claviceps</i></b> and <b><i>Neurospora</i></b>. <b><i>Neurospora</i> is "
                "used extensively in biochemical and genetic work.</b>"))
story.append(b1("<b>Many members like morels and truffles are edible and are considered "
                "delicacies.</b>"))
story.append(memory_aid("<b>Conidia = exogenous</b> (outside, on conidiophores); "
                        "<b>ascospores = endogenous</b> (inside the sac-like <b>ascus</b>). "
                        "Sac-fungi keep their sexual spores <i>in a sac</i>."))

# ---- 2.3.3 Basidiomycetes ----
story.append(heading("2.3.3", "Basidiomycetes", level=2))
story.append(b1("<b>Commonly known forms of basidiomycetes are mushrooms, bracket fungi or "
                "puffballs.</b>"))
story.append(b1("<b>They grow in soil, on logs and tree stumps and in living plant bodies as "
                "parasites, e.g., rusts and smuts.</b> <b>The mycelium is branched and "
                "septate.</b>"))
story.append(b1("<b>The asexual spores are generally not found, but vegetative reproduction by "
                "fragmentation is common.</b>"))
story.append(b1("<b>The sex organs are absent, but plasmogamy is brought about by fusion of two "
                "vegetative or somatic cells of different strains or genotypes.</b>"))
story.append(b1("<b>The resultant structure is dikaryotic which ultimately gives rise to "
                "basidium.</b> <b>Karyogamy and meiosis take place in the basidium producing four "
                "basidiospores.</b>"))
story.append(b1("<b>The basidiospores are exogenously produced on the basidium (pl.: "
                "basidia).</b> <b>The basidia are arranged in fruiting bodies called "
                "basidiocarps.</b>"))
story.append(b1("<b>Some common members are <i>Agaricus</i> (mushroom)</b> (Figure 2.5c), "
                "<b><i>Ustilago</i> (smut)</b> and <b><i>Puccinia</i> (rust fungus)</b>."))
story.append(memory_aid("Basidiomycetes are the group defined by absences and a fixed number: "
                        "<b>no asexual spores</b>, <b>no sex organs</b>, but <b>exactly four "
                        "basidiospores</b> per basidium, produced <b>exogenously</b>. Fruiting "
                        "body = <b>basidiocarp</b> (compare <b>ascocarp</b> in ascomycetes)."))

story.append(figure("fig_2_5.png",
                    "<b>Fig. 2.5</b> - Fungi: <b>(a)</b> <i>Mucor</i>, <b>(b)</b> "
                    "<i>Aspergillus</i>, <b>(c)</b> <i>Agaricus</i>. The three drawings carry only "
                    "the panel markers <b>(a)</b>, <b>(b)</b> and <b>(c)</b>; each fungus is "
                    "identified by this caption. One representative is drawn per class discussed "
                    "above - <i>Mucor</i> for the Phycomycetes, <i>Aspergillus</i> for the "
                    "Ascomycetes and <i>Agaricus</i>, the mushroom, for the Basidiomycetes.",
                    max_width_cm=5.4))

# ---- 2.3.4 Deuteromycetes ----
story.append(heading("2.3.4", "Deuteromycetes", level=2))
story.append(keyterm("<b>Commonly known as imperfect fungi because only the asexual or vegetative "
                     "phases of these fungi are known.</b>"))
story.append(b1("<b>When the sexual forms of these fungi were discovered they were moved into "
                "classes they rightly belong to.</b>"))
story.append(b1("The reason such a holding class was needed at all: the <b>asexual or vegetative "
                "stage</b> of a fungus could be given <b>one name</b> and placed under the "
                "deuteromycetes, while its <b>sexual stage</b> carried <b>another name</b>; once "
                "the <b>linkages between the two stages were established</b>, the fungi were "
                "<b>correctly identified and moved out of the deuteromycetes</b>."))
story.append(b1("<b>Once perfect (sexual) stages of members of deuteromycetes were discovered, "
                "they were often moved to ascomycetes and basidiomycetes.</b>"))
story.append(b1("<b>The deuteromycetes reproduce only by asexual spores known as conidia.</b> "
                "<b>The mycelium is septate and branched.</b>"))
story.append(b1("<b>Some members are saprophytes or parasites while a large number of them are "
                "decomposers of litter and help in mineral cycling.</b>"))
story.append(b1("<b>Some examples are <i>Alternaria</i>, <i>Colletotrichum</i> and "
                "<i>Trichoderma</i>.</b>"))
story.append(note("NCERT prints the class name as <b>dueteromycetes</b> in the sentence about "
                  "perfect stages being discovered, and <b>deuteromycetes</b> everywhere else. "
                  "The typo is normalised to <b>deuteromycetes</b> in the prose above, per the "
                  "source-spelling policy recorded at the top of these notes."))

# ---- Comparison of the four fungal classes (exercise Q9) ----
story.append(heading("T 2.2", "The Four Classes of Fungi Compared", level=2, has_table=True))
story.append(data_table([
    ["Class", "Habitat / nutrition", "Mycelium", "Asexual reproduction", "Sexual reproduction",
     "Examples"],
    ["<b>Phyco-<br/>mycetes</b>",
     "Aquatic habitats, on <b>decaying wood</b> in moist and damp places, or <b>obligate "
     "parasites</b> on plants",
     "<b>Aseptate</b> and <b>coenocytic</b>",
     "<b>Zoospores</b> (motile) or <b>aplanospores</b> (non-motile), produced "
     "<b>endogenously</b> in <b>sporangium</b>",
     "<b>Zygospore</b> by fusion of two gametes - <b>isogamous</b>, or <b>anisogamous</b> or "
     "<b>oogamous</b>",
     "<i>Mucor</i>, <i>Rhizopus</i>, <i>Albugo</i>"],
    ["<b>Asco-<br/>mycetes</b><br/>(sac-fungi)",
     "<b>Saprophytic, decomposers, parasitic</b> or <b>coprophilous</b> (growing on dung)",
     "<b>Branched</b> and <b>septate</b>",
     "<b>Conidia</b>, produced <b>exogenously</b> on <b>conidiophores</b>; conidia on germination "
     "produce mycelium",
     "<b>Ascospores</b>, produced <b>endogenously</b> in sac-like <b>asci</b>; asci arranged in "
     "<b>ascocarps</b>",
     "<i>Penicillium</i>, yeast (<i>Saccharomyces</i>), <i>Aspergillus</i>, <i>Claviceps</i>, "
     "<i>Neurospora</i>"],
    ["<b>Basidio-<br/>mycetes</b>",
     "Grow <b>in soil, on logs and tree stumps</b> and <b>in living plant bodies as "
     "parasites</b> (rusts and smuts)",
     "<b>Branched</b> and <b>septate</b>",
     "<b>Generally not found</b>; vegetative reproduction by <b>fragmentation</b> is common",
     "<b>Sex organs absent</b>; <b>plasmogamy</b> by fusion of two vegetative or somatic cells of "
     "different strains; <b>dikaryotic</b> structure gives rise to <b>basidium</b>, which produces "
     "<b>four basidiospores exogenously</b>; basidia in <b>basidiocarps</b>",
     "<i>Agaricus</i> (mushroom), <i>Ustilago</i> (smut), <i>Puccinia</i> (rust fungus)"],
    ["<b>Deutero-<br/>mycetes</b><br/>(imperfect fungi)",
     "<b>Saprophytes or parasites</b>; a large number are <b>decomposers of litter</b> and help in "
     "<b>mineral cycling</b>",
     "<b>Septate</b> and <b>branched</b>",
     "<b>Only</b> asexual spores known as <b>conidia</b>",
     "<b>Only the asexual or vegetative phases are known</b>; when the perfect (sexual) stage was "
     "discovered, members were <b>moved to ascomycetes and basidiomycetes</b>",
     "<i>Alternaria</i>, <i>Colletotrichum</i>, <i>Trichoderma</i>"],
], col_widths=[1.7, 2.9, 1.5, 2.9, 3.7, 2.4], font_size=7.6))

# ---- 2.4 KINGDOM PLANTAE ----
story.append(heading("2.4", "Kingdom Plantae", level=1))
story.append(keyterm("<b>Kingdom Plantae includes all eukaryotic chlorophyll-containing organisms "
                     "commonly called plants.</b>"))
story.append(b1("<b>A few members are partially heterotrophic such as the insectivorous plants or "
                "parasites.</b> <b>Bladderwort and Venus fly trap are examples of insectivorous "
                "plants and <i>Cuscuta</i> is a parasite.</b>"))
story.append(b1("<b>The plant cells have an eukaryotic structure with prominent chloroplasts and "
                "cell wall mainly made of cellulose.</b> The cell structure itself is described in "
                "<b>Chapter 8</b>."))
story.append(b1("<b>Plantae includes algae, bryophytes, pteridophytes, gymnosperms and "
                "angiosperms.</b>"))
story.append(keyterm("<b>Life cycle of plants has two distinct phases - the diploid sporophytic "
                     "and the haploid gametophytic - that alternate with each other.</b> "
                     "<b>The lengths of the haploid and diploid phases, and whether these phases "
                     "are free-living or dependent on others, vary among different groups in "
                     "plants.</b> <b>This phenomenon is called alternation of generations.</b> "
                     "Further details are taken up in <b>Chapter 3</b>."))
story.append(note("Note the exact qualifier NCERT uses: plants are <b>chlorophyll-containing</b> "
                  "and autotrophic as a rule, but <b>a few members are partially "
                  "heterotrophic</b> - the insectivorous plants and the parasites. "
                  "<b>Partially</b> is the operative word; they are not moved out of Plantae."))
story.append(memory_aid("Five groups inside Plantae, in the order NCERT lists them: "
                        "<b>Algae, Bryophytes, Pteridophytes, Gymnosperms, Angiosperms</b>. "
                        "Two partially heterotrophic examples to hold ready: <b>Bladderwort</b> "
                        "and <b>Venus fly trap</b> (insectivorous), <b><i>Cuscuta</i></b> "
                        "(parasite)."))

# ---- 2.5 KINGDOM ANIMALIA ----
story.append(heading("2.5", "Kingdom Animalia", level=1))
story.append(keyterm("<b>This kingdom is characterised by heterotrophic eukaryotic organisms that "
                     "are multicellular and their cells lack cell walls.</b>"))
story.append(b1("<b>They directly or indirectly depend on plants for food.</b> <b>They digest "
                "their food in an internal cavity and store food reserves as glycogen or "
                "fat.</b>"))
story.append(keyterm("<b>Their mode of nutrition is holozoic - by ingestion of food.</b>"))
story.append(b1("<b>They follow a definite growth pattern and grow into adults that have a "
                "definite shape and size.</b> <b>Higher forms show elaborate sensory and "
                "neuromotor mechanism.</b> <b>Most of them are capable of locomotion.</b>"))
story.append(b1("<b>The sexual reproduction is by copulation of male and female followed by "
                "embryological development.</b> The <b>salient features of the various animal "
                "phyla</b> are described in <b>Chapter 4</b>."))
story.append(memory_aid("The four defining words for Animalia: <b>heterotrophic, eukaryotic, "
                        "multicellular, no cell wall</b>. Storage is <b>glycogen or fat</b> "
                        "(not starch), digestion is in an <b>internal cavity</b>, and nutrition is "
                        "<b>holozoic</b> - by <b>ingestion</b>."))

# ---- 2.6 VIRUSES, VIROIDS, PRIONS AND LICHENS ----
story.append(heading("2.6", "Viruses, Viroids, Prions and Lichens", level=1))
story.append(b1("<b>In the five kingdom classification of Whittaker there is no mention of some "
                "acellular organisms like viruses and viroids, prions and lichens.</b> All four "
                "are <b>briefly introduced here</b>."))
story.append(b1("<b>Viruses did not find a place in classification since they are not considered "
                "truly 'living', if we understand living as those organisms that have a cell "
                "structure.</b>"))
story.append(b1("<b>All of us who have suffered the ill effects of common cold or 'flu' know what "
                "effects viruses can have on us, even if we do not associate it with our "
                "condition.</b>"))

story.append(heading("2.6a", "Viruses", level=2))
story.append(keyterm("<b>The viruses are non-cellular organisms that are characterised by having "
                     "an inert crystalline structure outside the living cell.</b> <b>Once they "
                     "infect a cell, they take over the machinery of the host cell to replicate "
                     "themselves, killing the host.</b>"))
story.append(b1("<b>Virus means venom or poisonous fluid.</b>"))
story.append(body("<b>How the virus was discovered - the three names NCERT fixes:</b>"))
story.append(process_flow([
    "<b>Dmitri Ivanowsky (1892)</b> <b>recognised certain microbes as causal organism of the "
    "mosaic disease of tobacco</b> (Figure 2.6a). These <b>were found to be smaller than bacteria "
    "because they passed through bacteria-proof filters</b>.",
    "<b>M.W. Beijerinck (1898)</b> <b>demonstrated that the extract of the infected plants of "
    "tobacco could cause infection in healthy plants</b> and <b>called the fluid as <i>Contagium "
    "vivum fluidum</i> (infectious living fluid)</b>.",
    "<b>W.M. Stanley (1935)</b> <b>showed that viruses could be crystallised and crystals consist "
    "largely of proteins</b>. They <b>are inert outside their specific host cell</b>. "
    "<b>Viruses are obligate parasites.</b>",
]))
story.append(keyterm("<b>In addition to proteins</b>, <b>viruses also contain genetic material, "
                     "that could be either RNA or DNA.</b> <b>No virus contains both RNA and "
                     "DNA.</b> <b>A virus is a nucleoprotein and the genetic material is "
                     "infectious.</b>"))
story.append(data_table([
    ["Virus group", "Genetic material as stated by NCERT"],
    ["<b>Viruses that infect plants</b>", "<b>Single stranded RNA</b>"],
    ["<b>Viruses that infect animals</b>",
     "<b>Either single or double stranded RNA or double stranded DNA</b>"],
    ["<b>Bacterial viruses or bacteriophages</b> (viruses that infect the bacteria) - "
     "Figure 2.6b",
     "<b>Usually double stranded DNA viruses</b>"],
], col_widths=[5.4, 7.6], font_size=9.0))
story.append(note("The table above is prefaced in the source by <b>In general</b> - keep that "
                  "qualifier. The absolute statement is the other one: <b>no virus contains both "
                  "RNA and DNA</b>."))
story.append(keyterm("<b>The protein coat called capsid made of small subunits called capsomeres, "
                     "protects the nucleic acid.</b> <b>These capsomeres are arranged in helical "
                     "or polyhedral geometric forms.</b>"))
story.append(b1("<b>Viruses cause diseases like mumps, small pox, herpes and influenza.</b> "
                "<b>AIDS in humans is also caused by a virus.</b>"))
story.append(b1("<b>In plants, the symptoms can be mosaic formation, leaf rolling and curling, "
                "yellowing and vein clearing, dwarfing and stunted growth.</b>"))
story.append(figure("fig_2_6.png",
                    "<b>Fig. 2.6</b> - <b>(a)</b> Tobacco Mosaic Virus (TMV), <b>(b)</b> "
                    "Bacteriophage. In <b>panel (a)</b> the two labelled parts of the TMV particle "
                    "are its <b>RNA</b> and the surrounding protein <b>Capsid</b>. In "
                    "<b>panel (b)</b> the bacteriophage is labelled <b>Head</b>, <b>Collar</b>, "
                    "<b>Sheath</b> and <b>Tail fibres</b>. In the source artwork the phage head is "
                    "printed in a different colour from the tail, sheath and collar; in this "
                    "monochrome print the parts are told apart by their <b>labels and "
                    "position</b> instead of by colour.",
                    max_width_cm=13.2))
story.append(memory_aid("Four viral diseases of humans to name on demand: <b>mumps, small pox, "
                        "herpes, influenza</b> (and <b>AIDS</b>). Plant symptoms: <b>mosaic "
                        "formation, leaf rolling and curling, yellowing and vein clearing, "
                        "dwarfing and stunted growth</b>."))
story.append(note("<b>Would you call viruses living or non-living?</b> - the chapter puts this "
                  "question to you directly, and gives you both sides rather than a verdict: "
                  "viruses are <b>not considered truly 'living'</b> if living means having a "
                  "<b>cell structure</b>, and they are <b>inert crystalline structures outside the "
                  "living cell</b>; yet they carry <b>infectious genetic material</b> and, once "
                  "inside a host cell, <b>take over its machinery to replicate</b>. Answer it with "
                  "these facts, not with a one-word label."))

story.append(heading("2.6b", "Viroids", level=2))
story.append(keyterm("<b>In 1971, T.O. Diener discovered a new infectious agent that was smaller "
                     "than viruses and caused potato spindle tuber disease.</b> <b>It was found to "
                     "be a free RNA; it lacked the protein coat that is found in viruses, hence "
                     "the name viroid.</b> <b>The RNA of the viroid was of low molecular "
                     "weight.</b>"))
story.append(memory_aid("Viroid against virus, in three strokes: <b>smaller than viruses</b>, "
                        "<b>free RNA with no protein coat (no capsid)</b>, <b>RNA of low "
                        "molecular weight</b>. Disease to remember: <b>potato spindle tuber "
                        "disease</b>."))

story.append(heading("2.6c", "Prions", level=2))
story.append(keyterm("<b>In modern medicine</b>, <b>certain infectious neurological diseases were "
                     "found to be transmitted by an agent consisting of abnormally folded "
                     "protein.</b> <b>The agent was similar in size to viruses.</b> <b>These "
                     "agents were called prions.</b>"))
story.append(b1("<b>The most notable diseases caused by prions are bovine spongiform "
                "encephalopathy (BSE) commonly called mad cow disease in cattle and its analogous "
                "variant Creutzfeldt-Jacob disease (CJD) in humans.</b>"))
story.append(memory_aid("The three acellular agents differ by <b>what carries the infection</b>: "
                        "<b>virus = nucleoprotein</b> (RNA or DNA inside a capsid), "
                        "<b>viroid = free RNA</b> (no coat), <b>prion = abnormally folded "
                        "protein</b> (no nucleic acid at all). Prion diseases: <b>BSE</b> in "
                        "cattle, <b>CJD</b> in humans."))

story.append(heading("2.6d", "Lichens", level=2))
story.append(keyterm("<b>Lichens are symbiotic associations i.e. mutually useful associations, "
                     "between algae and fungi.</b> <b>The algal component is known as phycobiont "
                     "and fungal component as mycobiont, which are autotrophic and heterotrophic, "
                     "respectively.</b>"))
story.append(b1("<b>Algae prepare food for fungi and fungi provide shelter and absorb mineral "
                "nutrients and water for its partner.</b>"))
story.append(b1("<b>So close is their association that if one saw a lichen in nature one would "
                "never imagine that they had two different organisms within them.</b>"))
story.append(b1("<b>Lichens are very good pollution indicators - they do not grow in polluted "
                "areas.</b>"))
story.append(memory_aid("<b>Phyco</b>biont = the <b>alga</b> = <b>autotrophic</b> = makes the "
                        "food. <b>Myco</b>biont = the <b>fungus</b> = <b>heterotrophic</b> = gives "
                        "shelter and absorbs mineral nutrients and water. Lichens are <b>very good "
                        "pollution indicators</b> because they <b>do not grow in polluted "
                        "areas</b>."))

# ---- Quick Recap ----
story.append(heading("Recap", "Quick Recap", level=1))
story.append(b1("<b>Biological classification was first proposed by Aristotle on the basis of "
                "simple morphological characters.</b> <b>Linnaeus later classified all living "
                "organisms into two kingdoms - Plantae and Animalia.</b>"))
story.append(b1("<b>Whittaker proposed a five kingdom classification - Monera, Protista, Fungi, "
                "Plantae and Animalia.</b> The <b>main criteria</b> were <b>cell structure, body "
                "organisation, mode of nutrition and reproduction, and phylogenetic "
                "relationships</b>. <b>This kind of changes will take place in future too</b> "
                "depending on the improvement in our understanding of characteristics and "
                "evolutionary relationships."))
story.append(b1("<b>Bacteria are included in Kingdom Monera.</b> <b>Bacteria are cosmopolitan in "
                "distribution.</b> They <b>show the most extensive metabolic diversity</b> and "
                "<b>may be autotrophic or heterotrophic</b> in their mode of nutrition."))
story.append(b1("<b>Kingdom Protista includes single-celled eukaryotes</b> - <b>Chrysophytes, "
                "Dinoflagellates, Euglenoids, Slime-moulds and Protozoans</b>. <b>Protists have a "
                "defined nucleus and other membrane-bound organelles</b>, and <b>they reproduce "
                "both asexually and sexually</b>."))
story.append(b1("<b>Fungi show a great diversity in structures and habitat</b>, reproduce "
                "<b>both asexually and sexually</b>, and are divided into <b>four classes - "
                "Phycomycetes, Ascomycetes, Basidiomycetes and Deuteromycetes</b>. <b>Most fungi "
                "are saprophytic in their mode of nutrition.</b>"))
story.append(b1("<b>Kingdom Plantae includes all eukaryotic chlorophyll-containing organisms</b>, "
                "namely <b>algae, bryophytes, pteridophytes, gymnosperms and angiosperms</b>, and "
                "their life cycle shows <b>alternation of generations</b> between a <b>diploid "
                "sporophytic</b> and a <b>haploid gametophytic</b> phase."))
story.append(b1("<b>Kingdom Animalia is characterised by heterotrophic, eukaryotic, multicellular "
                "organisms whose cells lack cell walls</b>, and <b>their mode of nutrition is "
                "holozoic</b>."))
story.append(b1("<b>Viruses, viroids, prions and lichens find no mention in the five kingdom "
                "classification.</b> A <b>virus</b> is a <b>non-cellular nucleoprotein</b> with "
                "<b>either RNA or DNA, never both</b>; a <b>viroid</b> is <b>free RNA of low "
                "molecular weight without a protein coat</b>; a <b>prion</b> is an <b>abnormally "
                "folded protein</b>; and a <b>lichen</b> is a <b>symbiotic association between an "
                "algal phycobiont and a fungal mycobiont</b>."))

# ---- Appendix: terms the exercises assume (Rule 2 exercise-gap coverage) ----
story.append(heading("Appendix", "Terms Used in the Exercises", level=1))
story.append(body("These exercise questions lean on points the chapter body assumes rather than "
                  "states outright. Each answer below is assembled <b>only</b> from facts stated "
                  "in this chapter."))
story.append(b1("<b>Why classification systems keep changing (Q1).</b> The <b>earlier "
                "classifications included bacteria, blue-green algae, fungi, mosses, ferns, "
                "gymnosperms and the angiosperms under 'Plants'</b>, so <b>groups which widely "
                "differed in other characteristics were placed together</b> because a single "
                "character - the <b>cell wall</b> - was used. Once <b>cell structure, nature of "
                "wall, mode of nutrition, habitat, methods of reproduction and evolutionary "
                "relationships</b> were considered, the <b>fungi were placed in a separate "
                "Kingdom Fungi</b> and the <b>prokaryotes were separated from the eukaryotes</b>. "
                "The chapter states plainly that <b>this kind of changes will take place in future "
                "too depending on the improvement in our understanding of characteristics and "
                "evolutionary relationships</b>."))
story.append(b1("<b>Economic uses of bacteria and archaebacteria (Q2).</b> Among the "
                "<b>heterotrophic bacteria</b>, the <b>helpful</b> ones are those that <b>make curd "
                "from milk</b>, <b>produce antibiotics</b> and <b>fix nitrogen in legume roots</b>. "
                "Among the <b>archaebacteria</b>, the <b>methanogens</b> <b>live in the gut of "
                "several ruminant animals such as cows and buffaloes</b> and are <b>responsible for "
                "the production of methane (biogas) from the dung of these animals</b>."))
story.append(b1("<b>The nature of the cell wall in diatoms (Q3).</b> In the chrysophytes, "
                "<b>the cell walls form two thin overlapping shells, which fit together as in a "
                "soap box</b>. <b>The walls are embedded with silica</b> and so are "
                "<b>indestructible</b>. That indestructibility is why diatoms have <b>left behind "
                "large amounts of cell wall deposits in their habitat</b>, an accumulation called "
                "<b>diatomaceous earth</b>, which is <b>gritty</b> and is used in <b>polishing</b> "
                "and in the <b>filtration of oils and syrups</b>."))
story.append(b1("<b>'Algal bloom' and 'red tides' (Q4).</b> The chapter never prints the phrase "
                "<b>algal bloom</b>, but it supplies the fact behind it: <b>blue-green algae "
                "(cyanobacteria) form blooms in polluted water bodies</b> - a bloom is that "
                "visible mass multiplication in the water. <b>Red tides</b> is the chapter's own "
                "term, used of the <b>dinoflagellates</b>: <b>red dinoflagellates (e.g., "
                "<i>Gonyaulax</i>) undergo such rapid multiplication that they make the sea appear "
                "red (red tides)</b>. So a bloom is the general event, and a red tide is the "
                "specific case caused by red dinoflagellates."))
story.append(b1("<b>Viroids against viruses (Q5).</b> A <b>virus</b> has <b>genetic material - "
                "either RNA or DNA, never both - enclosed in a protein coat (capsid) of "
                "capsomeres</b>, i.e. it is a <b>nucleoprotein</b>. A <b>viroid</b>, discovered by "
                "<b>T.O. Diener in 1971</b>, is <b>smaller than a virus</b>, consists of "
                "<b>free RNA</b> and <b>lacks the protein coat that is found in viruses</b> - that "
                "missing coat is the reason for the name - and its <b>RNA is of low molecular "
                "weight</b>. It caused <b>potato spindle tuber disease</b>."))
story.append(b1("<b>The four major groups of Protozoa (Q6).</b> <b>Amoeboid protozoans</b> "
                "(move and capture prey by <b>pseudopodia</b>; <i>Amoeba</i>, and the parasitic "
                "<i>Entamoeba</i>), <b>flagellated protozoans</b> (have <b>flagella</b>; the "
                "parasitic <i>Trypanosoma</i> causes <b>sleeping sickness</b>), <b>ciliated "
                "protozoans</b> (have <b>thousands of cilia</b> and a <b>cavity (gullet)</b>; "
                "<b>Paramoecium</b>) and <b>sporozoans</b> (have an <b>infectious spore-like "
                "stage</b>; <i>Plasmodium</i> causes <b>malaria</b>). <b>All protozoans are "
                "heterotrophs and live as predators or parasites</b>, and <b>they are believed to "
                "be primitive relatives of animals</b>."))
story.append(b1("<b>Partially heterotrophic plants (Q7).</b> Plantae is defined by "
                "<b>chlorophyll-containing eukaryotes</b>, but <b>a few members are partially "
                "heterotrophic</b>: the <b>insectivorous plants</b> - <b>Bladderwort</b> and "
                "<b>Venus fly trap</b> - and the <b>parasites</b>, of which the chapter's example "
                "is <b><i>Cuscuta</i></b>."))
story.append(b1("<b>Phycobiont and mycobiont (Q8).</b> These are the two partners in a "
                "<b>lichen</b>, a <b>symbiotic, i.e. mutually useful, association between algae "
                "and fungi</b>. The <b>phycobiont is the algal component and is autotrophic</b> - "
                "it <b>prepares food for the fungi</b>. The <b>mycobiont is the fungal component "
                "and is heterotrophic</b> - it <b>provides shelter and absorbs mineral nutrients "
                "and water for its partner</b>."))
story.append(b1("<b>Comparative account of the fungal classes (Q9).</b> Answered in full by "
                "<b>Table T 2.2</b> above, which sets the <b>habitat and nutrition, mycelium, "
                "asexual reproduction, sexual reproduction and examples</b> of the "
                "<b>Phycomycetes, Ascomycetes, Basidiomycetes and Deuteromycetes</b> side by "
                "side."))
story.append(b1("<b>Characteristic features of Euglenoids (Q10).</b> <b>Majority are fresh water "
                "organisms found in stagnant water.</b> <b>Instead of a cell wall, they have a "
                "protein rich layer called pellicle which makes their body flexible.</b> <b>They "
                "have two flagella, a short and a long one.</b> <b>Though they are photosynthetic "
                "in the presence of sunlight, when deprived of sunlight they behave like "
                "heterotrophs by predating on other smaller organisms.</b> Interestingly, "
                "<b>the pigments of euglenoids are identical to those present in higher "
                "plants</b>. Example: <b><i>Euglena</i></b>."))
story.append(b1("<b>Virus structure, genetic material and viral diseases (Q11).</b> A virus is a "
                "<b>nucleoprotein</b>: <b>genetic material that is either RNA or DNA - no virus "
                "contains both</b> - protected by a <b>protein coat called capsid, made of small "
                "subunits called capsomeres</b> that are <b>arranged in helical or polyhedral "
                "geometric forms</b>. <b>In general</b>, <b>plant-infecting viruses have single "
                "stranded RNA</b>; <b>animal-infecting viruses have either single or double "
                "stranded RNA or double stranded DNA</b>; and <b>bacteriophages are usually double "
                "stranded DNA viruses</b>. Four diseases: <b>mumps, small pox, herpes and "
                "influenza</b> (<b>AIDS</b> is also caused by a virus)."))
story.append(b1("<b>Are viruses living or non-living (Q12)?</b> The chapter poses this question "
                "itself and supplies both sides rather than a verdict - see the note in section "
                "2.6a. Against: viruses are <b>not considered truly 'living'</b> if living means "
                "having a <b>cell structure</b>, they have an <b>inert crystalline structure "
                "outside the living cell</b>, they <b>could be crystallised</b>, and they are "
                "<b>obligate parasites</b>. For: they contain <b>infectious genetic material</b> "
                "and, once they infect a cell, they <b>take over the machinery of the host cell to "
                "replicate themselves</b>."))

if __name__ == "__main__":
    sys.exit(build_pdf(OUT_PDF, story,
                       title="Class 11 Chapter 2 - Biological Classification (NEET notes)",
                       subject="NEET Biology"))
