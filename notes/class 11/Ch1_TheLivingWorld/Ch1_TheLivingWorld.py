"""
Class 11 - Chapter 1: The Living World  (NEET replacement notes)

Generated per SUPREME COMMAND PROMPT.md v6. Styles, geometry, badges, boxes,
tables, process flows and figure framing all come from the repo-level frozen
module `neet_template.py` (§0.6) - nothing style-level is re-declared here.

Source of truth: Chapter/class 11/Chapter 01 - The Living World.pdf
Frozen inventory: Ch1_TheLivingWorld_inventory.md (121 Facts rows, F001-F121)

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
OUT_PDF = os.path.join(HERE, "Ch1_TheLivingWorld.pdf")


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
story += title_block("The Living World")

# ---- Unit 1 introduction ----
story.append(heading("Unit 1", "Diversity in the Living World - Unit Introduction", level=1))
story.append(body("<b>Biology is the science of life forms and living processes.</b> The living "
                  "world comprises an amazing diversity of living organisms."))
story.append(b1("Early man could <b>easily perceive</b> the difference between inanimate matter "
                "and living organisms. He <b>deified</b> some of the inanimate matter (wind, sea, "
                "fire etc.) and some among the animals and plants; the common feature of all such "
                "inanimate and animate objects was the <b>sense of awe or fear</b> that they evoked."))
story.append(b1("Description of living organisms, including human beings, began much later in "
                "human history. Societies with an <b>anthropocentric view</b> of biology could "
                "register only limited progress in biological knowledge."))
story.append(b1("Systematic and monumental description of life forms brought in, <i>out of "
                "necessity</i>, detailed systems of <b>identification, nomenclature and "
                "classification</b>."))
story.append(b1("The biggest spin off of such studies was recognising that similarities are shared "
                "among living organisms <b>both horizontally and vertically</b>."))
story.append(b1("That all present day living organisms are related to each other, and also to all "
                "organisms that ever lived on this earth, was a revelation that humbled man and led "
                "to <b>cultural movements for conservation of biodiversity</b>."))
story.append(b1("This unit describes animals and plants, including their classification, from a "
                "<b>taxonomist's perspective</b>: Chapter 1 The Living World, Chapter 2 Biological "
                "Classification, Chapter 3 Plant Kingdom, Chapter 4 Animal Kingdom."))

# ---- Scientist profile: Ernst Mayr (text only, no photograph) ----
story.append(heading("Profile", "Ernst Mayr (1904 - 2004)", level=2))
story.append(data_table([
    ["Item", "Detail"],
    ["Born", "5 July 1904, in Kempten, Germany"],
    ["Died", "2004, at the age of 100"],
    ["Position", "Harvard University evolutionary biologist; joined Harvard's Faculty of Arts and "
                 "Sciences in 1953, retired in 1975, assuming the title <b>Alexander Agassiz "
                 "Professor of Zoology Emeritus</b>"],
    ["Called", "<b>'The Darwin of the 20th century'</b>; one of the <b>100 greatest scientists of "
               "all time</b>"],
    ["Career span", "Nearly <b>80-year career</b>; research spanned ornithology, taxonomy, "
                    "zoogeography, evolution, systematics, and the history and philosophy of biology"],
    ["Credited with", "Almost single-handedly making the <b>origin of species diversity</b> the "
                      "central question of evolutionary biology that it is today; pioneering the "
                      "<b>currently accepted definition of a biological species</b>"],
    ["Triple crown of biology", "<b>Balzan Prize (1983)</b>, <b>International Prize for Biology "
                                "(1994)</b>, <b>Crafoord Prize (1999)</b>"],
], col_widths=[1, 3.4]))

# ---- 1.0 Chapter opening - what is living? ----
story.append(heading("1.0", "What Indeed is Life? - The Question Behind the Chapter", level=1))
story.append(body("The wide range of living types is amazing. Organisms occupy extraordinary "
                  "habitats - <b>cold mountains, deciduous forests, oceans, fresh water lakes, "
                  "deserts or hot springs</b>. The beauty of a galloping horse, of the migrating "
                  "birds, the valley of flowers or the attacking shark evokes awe and a deep sense "
                  "of wonder. So does ecological <b>conflict and cooperation</b> among members of a "
                  "population and among populations of a community, and even the <b>molecular "
                  "traffic inside a cell</b>."))
story.append(body("The very range of organisms - in terms of <b>size, colour, habitat, "
                  "physiological and morphological features</b> - makes us seek the defining "
                  "characteristics of living organisms. The question 'what indeed is life?' carries "
                  "<b>two implicit questions</b>:"))
story.append(process_flow([
    "<b>The technical question</b> - what is living, as opposed to the non-living? Science answers "
    "this one.",
    "<b>The philosophical question</b> - what is the purpose of life? <i>As scientists, we shall "
    "not attempt answering the second question.</i>",
]))

# ---- 1.1 Diversity in the Living World ----
story.append(heading("1.1", "Diversity in the Living World", level=1))
story.append(body("Look around and you see a large variety of living organisms - potted plants, "
                  "insects, birds, your pets, other animals and plants. Several organisms "
                  "<b>cannot be seen with the naked eye</b>, yet they are all around you. Increase "
                  "the area you observe and the range and variety of organisms increases; visit a "
                  "<b>dense forest</b> and you would <i>probably</i> see a much greater number and "
                  "kinds of living organisms."))
story.append(keyterm("<b>Species</b> - each different kind of plant, animal or organism that you "
                     "see represents a species."))
story.append(keyterm("<b>Biodiversity</b> - the number and types of organisms present on earth. "
                     "The number of species that are known and described range between "
                     "<b>1.7-1.8 million</b>."))
story.append(b1("Millions of plants and animals have been identified and described, but a "
                "<b>large number still remains unknown</b> - as we explore new areas, and even "
                "old ones, new organisms are <b>continuously being identified</b>."))
story.append(b1("Taxonomic studies of various species of plants and animals are useful in "
                "<b>agriculture, forestry, industry</b>, and in general for knowing our "
                "<b>bio-resources</b> and their diversity."))

# ---- 1.1 (a) Nomenclature and identification ----
story.append(heading("1.1", "Nomenclature and Identification - Why Local Names Fail", level=2))
story.append(body("We know the plants and animals in our own area by their <b>local names</b>, and "
                  "these vary from place to place, <b>even within a country</b> - which is exactly "
                  "the confusion that makes talking about an organism impossible. Hence naming must "
                  "be standardised so that a particular organism is known by the <b>same name all "
                  "over the world</b>."))
story.append(keyterm("<b>Nomenclature</b> - the process of standardising the naming of living "
                     "organisms. It is <i>only</i> possible when the organism is described "
                     "correctly and we know to what organism the name is attached."))
story.append(keyterm("<b>Identification</b> - describing the organism correctly and knowing which "
                     "organism a name belongs to. Identification must therefore come before naming."))
story.append(body("A number of scientists have established procedures to assign a scientific name "
                  "to each known organism, acceptable to biologists all over the world:"))
story.append(data_table([
    ["Code", "Full form", "Applies to"],
    ["<b>ICBN</b>", "International Code for Botanical Nomenclature - scientific names based on "
                    "agreed principles and criteria", "Plants"],
    ["<b>ICZN</b>", "International Code of Zoological Nomenclature - evolved by animal taxonomists",
     "Animals"],
], col_widths=[0.8, 3.2, 1]))
story.append(b1("Scientific names ensure that each organism has <b>only one name</b>."))
story.append(b1("A description of any organism should enable people <b>in any part of the "
                "world</b> to arrive at the same name."))
story.append(b1("They also ensure that such a name <b>has not been used for any other known "
                "organism</b>."))

# ---- 1.1 (b) Binomial nomenclature ----
# [VERIFICATION FIX] has_table dropped: the frozen template's table-icon cell
# renders outside the banner fill, leaving a stray glyph in the right margin.
# The flag is decorative only, so the chapter omits it rather than patching the
# frozen module (§0.6).
story.append(heading("1.1", "Binomial Nomenclature", level=2))
story.append(body("Biologists follow universally accepted principles to provide scientific names. "
                  "Each name has <b>two components</b> - the <b>Generic name</b> and the "
                  "<b>specific epithet</b>. This system of providing a name with two components is "
                  "called <b>Binomial nomenclature</b>, given by <b>Carolus Linnaeus</b> and "
                  "practised by biologists all over the world; the two word format was found "
                  "convenient."))
story.append(body("Worked example - the scientific name of mango is <i>Mangifera indica</i>: "
                  "<i>Mangifera</i> represents the <b>genus</b>, while <i>indica</i> is a "
                  "particular species, or a <b>specific epithet</b>."))
story.append(data_table([
    ["Rule", "What it says", "Illustration"],
    ["1. Language", "Biological names are <i>generally</i> in <b>Latin</b> and written in "
                    "<b>italics</b>. They are Latinised or derived from Latin <i>irrespective of "
                    "their origin</i>.", "<i>Mangifera indica</i>"],
    ["2. Order of words", "The <b>first word</b> represents the <b>genus</b>; the <b>second "
                          "component</b> denotes the <b>specific epithet</b>.",
     "<i>Mangifera</i> = genus, <i>indica</i> = specific epithet"],
    ["3. Handwriting vs print", "Both words, when <b>handwritten</b>, are <b>separately "
                                "underlined</b>; when printed they are in <b>italics</b> - to "
                                "indicate their Latin origin.", "<u>Mangifera</u> <u>indica</u>"],
    ["4. Capitalisation", "The first word denoting the genus starts with a <b>capital letter</b>; "
                          "the specific epithet starts with a <b>small letter</b>.",
     "<i>Mangifera indica</i> (not <i>Mangifera Indica</i>)"],
    ["5. Author citation", "The name of the <b>author</b> appears <b>after the specific "
                           "epithet</b>, i.e. at the end of the biological name, in an "
                           "<b>abbreviated form</b>. It indicates who <b>first described</b> the "
                           "species.", "<i>Mangifera indica</i> Linn. - first described by Linnaeus"],
], col_widths=[1, 3, 1.5]))

# ---- 1.1 (c) Classification, taxonomy, systematics ----
story.append(heading("1.1", "Classification, Taxonomy and Systematics", level=2))
story.append(body("Since it is <b>nearly impossible</b> to study all the living organisms, some "
                  "means is necessary to make the study possible - this process is "
                  "<b>classification</b>."))
story.append(keyterm("<b>Classification</b> - the process by which anything is grouped into "
                     "<b>convenient categories</b> based on some <b>easily observable "
                     "characters</b>."))
story.append(body("We easily recognise groups such as plants, animals, dogs, cats or insects, and "
                  "the moment we use such a term we associate certain characters with the organism "
                  "in that group: think of 'dogs' and you see dogs, not cats; think of 'Alsatians' "
                  "and you know exactly what is meant; say <b>'mammals'</b> and you think of "
                  "animals with <b>external ears and body hair</b>; say 'Wheat' and you picture "
                  "wheat plants, not rice."))
story.append(keyterm("<b>Taxa</b> - the scientific term for such convenient categories. Taxa can "
                     "indicate categories at <b>very different levels</b>: 'Plants', 'Wheat', "
                     "'animals', 'mammals' and 'dogs' are all taxa - yet a dog is a mammal and "
                     "mammals are animals, so they represent taxa at different levels."))
story.append(body("Based on characteristics, all living organisms can be classified into different "
                  "taxa - and <b>this process of classification is taxonomy</b>. The basis of "
                  "<b>modern taxonomic studies</b> is: <b>external and internal structure</b>, "
                  "along with the <b>structure of cell</b>, <b>development process</b> and "
                  "<b>ecological information</b> of organisms."))
story.append(body("Four processes are <b>basic to taxonomy</b>:"))
story.append(process_flow([
    "<b>Characterisation</b> - record the characters of the organism.",
    "<b>Identification</b> - establish which organism it is.",
    "<b>Classification</b> - place it in convenient categories (taxa).",
    "<b>Nomenclature</b> - give it its universally valid two-part name.",
]))
story.append(body("Taxonomy is <b>not something new</b>. Human beings have always been interested "
                  "in knowing more about the various kinds of organisms, particularly with "
                  "reference to their own use: in early days they needed sources for their basic "
                  "needs of <b>food, clothing and shelter</b>, so the <b>earliest classifications "
                  "were based on the 'uses'</b> of various organisms."))
story.append(keyterm("<b>Systematics</b> - the branch of study of the <b>relationships</b> among "
                     "different kinds of organisms, not merely of their kinds and diversities. The "
                     "word is derived from the Latin word <b>'systema'</b>, meaning systematic "
                     "arrangement of organisms; <b>Linnaeus used <i>Systema Naturae</i></b> as the "
                     "title of his publication."))
story.append(b1("The scope of systematics was <b>later enlarged</b> to include <b>identification, "
                "nomenclature and classification</b>."))
story.append(b1("Systematics takes into account <b>evolutionary relationships</b> between "
                "organisms."))
story.append(note("Do not blur the four terms. <b>Identification</b> = which organism is this? "
                  "<b>Nomenclature</b> = what is its one valid name? <b>Classification</b> = "
                  "grouping into taxa on easily observable characters. <b>Taxonomy</b> = the whole "
                  "process of classifying organisms into taxa. <b>Systematics</b> is the widest: "
                  "identification + nomenclature + classification, <i>plus</i> evolutionary "
                  "relationships."))

# ---- 1.2 Taxonomic Categories ----
story.append(heading("1.2", "Taxonomic Categories", level=1))
story.append(body("Classification is <b>not a single step process</b> but involves a "
                  "<b>hierarchy of steps</b>, in which each step represents a <b>rank</b> or "
                  "<b>category</b>. Since the category is a part of the overall taxonomic "
                  "arrangement, it is called the <b>taxonomic category</b>, and all categories "
                  "together constitute the <b>taxonomic hierarchy</b>."))
story.append(keyterm("<b>Taxon</b> (pl.: <b>taxa</b>) - each category, referred to as a <b>unit of "
                     "classification</b>, which in fact represents a <b>rank</b>."))
story.append(body("Example: <b>insects</b> represent a group of organisms sharing common features "
                  "like <b>three pairs of jointed legs</b>. That makes insects <b>recognisable "
                  "concrete objects</b> which can be classified, and thus they were given a rank "
                  "or category. Groups represent category; category further denotes rank; each "
                  "rank or taxon represents a unit of classification."))
story.append(note("These taxonomic groups/categories are <b>distinct biological entities and not "
                  "merely morphological aggregates</b> - a favourite one-line NEET statement."))
story.append(body("Taxonomical studies of all known organisms have led to the development of "
                  "<b>common categories</b>: <b>kingdom, phylum or division (for plants), class, "
                  "order, family, genus and species</b>. All organisms, including those in the "
                  "plant and animal kingdoms, have <b>species as the lowest category</b>. To place "
                  "an organism in these categories, the basic requirement is <b>knowledge of the "
                  "characters</b> of an individual or group of organisms - this helps in "
                  "identifying <b>similarities and dissimilarities</b> among individuals of the "
                  "same kind of organisms as well as of other kinds."))

# ---- 1.2.1 Species ----
story.append(heading("1.2.1", "Species", level=3))
story.append(body("Taxonomic studies consider a group of individual organisms with "
                  "<b>fundamental similarities</b> as a <b>species</b>. One should be able to "
                  "distinguish one species from the other <b>closely related species</b> based on "
                  "the <b>distinct morphological differences</b>."))
story.append(b1("In <i>Mangifera indica</i>, <i>Solanum tuberosum</i> (potato) and "
                "<i>Panthera leo</i> (lion), the names <i>indica</i>, <i>tuberosum</i> and "
                "<i>leo</i> represent the <b>specific epithets</b>, while the first words "
                "<i>Mangifera</i>, <i>Solanum</i> and <i>Panthera</i> are <b>genera</b> and "
                "represent another <b>higher level of taxon</b> or category."))
story.append(b1("Each genus <i>may</i> have <b>one or more than one</b> specific epithets "
                "representing different organisms, but having <b>morphological similarities</b>: "
                "<i>Panthera</i> has another specific epithet called <i>tigris</i>, and "
                "<i>Solanum</i> includes species like <i>nigrum</i> and <i>melongena</i>."))
story.append(b1("Human beings belong to the species <i>sapiens</i>, grouped in the genus "
                "<i>Homo</i> - so the scientific name for human being is <i>Homo sapiens</i>."))

# ---- 1.2.2 Genus ----
story.append(heading("1.2.2", "Genus", level=3))
story.append(body("<b>Genus</b> comprises a group of <b>related species</b> which has <b>more "
                  "characters in common</b> in comparison to species of other genera; genera are "
                  "<b>aggregates of closely related species</b>."))
story.append(b1("Potato and brinjal are <b>two different species</b> but both belong to the genus "
                "<i>Solanum</i>."))
story.append(b1("Lion (<i>Panthera leo</i>), leopard (<i>P. pardus</i>) and tiger "
                "(<i>P. tigris</i>), with several common features, are all species of the genus "
                "<i>Panthera</i>. This genus <b>differs from</b> another genus <i>Felis</i>, which "
                "includes cats."))

# ---- 1.2.3 Family ----
story.append(heading("1.2.3", "Family", level=3))
story.append(body("<b>Family</b>, the next category, has a group of <b>related genera</b> with "
                  "<b>still less number of similarities</b> as compared to genus and species. "
                  "Families are characterised on the basis of <b>both vegetative and reproductive "
                  "features</b> of plant species."))
story.append(data_table([
    ["Kingdom side", "Genera placed together", "Family"],
    ["Plants", "<i>Solanum</i>, <i>Petunia</i>, <i>Datura</i> (three different genera)",
     "<b>Solanaceae</b>"],
    ["Animals", "<i>Panthera</i> (lion, tiger, leopard) put along with <i>Felis</i> (cats)",
     "<b>Felidae</b>"],
    ["Animals", "The dog line - observe a cat and a dog and you find some similarities and some "
                "differences as well, so they are separated into two different families",
     "<b>Canidae</b> (dog) vs <b>Felidae</b> (cat)"],
], col_widths=[0.9, 3.1, 1.4]))

# ---- 1.2.4 Order ----
story.append(heading("1.2.4", "Order", level=3))
story.append(body("Categories like <b>species, genus and families</b> are based on a <b>number of "
                  "similar characters</b>. <i>Generally</i>, <b>order</b> and other higher "
                  "taxonomic categories are identified based on the <b>aggregates of "
                  "characters</b>."))
story.append(b1("Order, being a higher category, is the <b>assemblage of families</b> which "
                "exhibit <b>a few similar characters</b>; these similar characters are <b>less in "
                "number</b> as compared to different genera included in a family."))
story.append(b1("Plants: families like <b>Convolvulaceae</b> and <b>Solanaceae</b> are included in "
                "the order <b>Polymoniales</b>, <i>mainly</i> based on the <b>floral "
                "characters</b>."))
story.append(b1("Animals: the order <b>Carnivora</b> includes families like <b>Felidae</b> and "
                "<b>Canidae</b>."))

# ---- 1.2.5 Class ----
story.append(heading("1.2.5", "Class", level=3))
story.append(body("This category includes <b>related orders</b>. For example, order <b>Primata</b> "
                  "comprising <b>monkey, gorilla and gibbon</b> is placed in class "
                  "<b>Mammalia</b>, along with order <b>Carnivora</b> that includes animals like "
                  "<b>tiger, cat and dog</b>. <b>Class Mammalia has other orders also.</b>"))

# ---- 1.2.6 Phylum ----
story.append(heading("1.2.6", "Phylum (Division in plants)", level=3))
story.append(body("Classes comprising animals like <b>fishes, amphibians, reptiles, birds</b> "
                  "along with <b>mammals</b> constitute the next higher category called "
                  "<b>Phylum</b>. All these, based on the common features like presence of "
                  "<b>notochord</b> and <b>dorsal hollow neural system</b>, are included in phylum "
                  "<b>Chordata</b>. In case of plants, classes with <b>a few similar "
                  "characters</b> are assigned to a higher category called <b>Division</b>."))

# ---- 1.2.7 Kingdom ----
story.append(heading("1.2.7", "Kingdom", level=3))
story.append(body("All animals belonging to various <b>phyla</b> are assigned to the <b>highest "
                  "category</b> called <b>Kingdom Animalia</b> in the classification system of "
                  "animals. The <b>Kingdom Plantae</b>, on the other hand, is <b>distinct</b>, and "
                  "comprises all plants from various <b>divisions</b>. Henceforth these two groups "
                  "are referred to as <b>animal and plant kingdoms</b>."))
story.append(body("The taxonomic categories from <b>species to kingdom</b> in <b>ascending "
                  "order</b>, starting with species, are: <b>Species</b>, <b>Genus</b>, "
                  "<b>Family</b>, <b>Order</b>, <b>Class</b>, <b>Phylum or Division</b>, "
                  "<b>Kingdom</b>. These are <b>broad categories</b>; taxonomists have also "
                  "developed <b>sub-categories</b> in this hierarchy to facilitate more sound and "
                  "scientific placement of various taxa."))
# [VERIFICATION FIX] The taxonomic hierarchy is a set of nested ranks, not a
# sequential procedure, so it is presented as a rank table rather than a
# numbered process_flow. Rank column reads bottom-up to match Fig 1.1's
# ascending order; every entry is the chapter's own definition (F073-F101).
story.append(data_table([
    ["Rank (ascending)", "What it groups", "Chapter example"],
    ["<b>Kingdom</b>", "The <b>highest category</b>; all phyla of animals, all divisions of plants",
     "Kingdom Animalia; Kingdom Plantae"],
    ["<b>Phylum or Division</b>", "<b>Phylum</b> - classes of animals with common features; "
                                  "<b>Division</b> - plant classes with a few similar characters",
     "Chordata (notochord, dorsal hollow neural system); Angiospermae"],
    ["<b>Class</b>", "Related <b>orders</b>", "Mammalia (has other orders also); Insecta"],
    ["<b>Order</b>", "<b>Assemblage of families</b> exhibiting a few similar characters",
     "Carnivora; Polymoniales; Primata"],
    ["<b>Family</b>", "Related <b>genera</b>, with still less number of similarities",
     "Felidae; Canidae; Solanaceae"],
    ["<b>Genus</b>", "<b>Aggregate of closely related species</b>", "<i>Panthera</i>; <i>Solanum</i>"],
    ["<b>Species</b>", "The <b>lowest category</b>; individuals with <b>fundamental similarities</b>",
     "<i>Panthera leo</i>; <i>Homo sapiens</i>"],
], col_widths=[1.15, 2.35, 2.0]))
story.append(figure("fig_1_1.png",
                    "Fig. 1.1 - Taxonomic categories showing hierarchial arrangement in ascending "
                    "order.",
                    max_width_cm=7.0))
story.append(body("Reading the hierarchy tells you the <b>basis of arrangement</b>:"))
story.append(b1("As we go <b>higher</b> from species to kingdom, the <b>number of common "
                "characteristics goes on decreasing</b>."))
story.append(b1("<b>Lower the taxa, more are the characteristics</b> that the members within the "
                "taxon share."))
story.append(b1("<b>Higher the category, greater is the difficulty</b> of determining the "
                "relationship to other taxa <b>at the same level</b> - hence the problem of "
                "classification becomes <b>more complex</b>."))
story.append(memory_aid("Ascending order <b>Species to Kingdom</b>: <b>S</b>ome <b>G</b>irls "
                        "<b>F</b>ind <b>O</b>ur <b>C</b>lass <b>P</b>retty <b>K</b>ind - "
                        "<b>S</b>pecies, <b>G</b>enus, <b>F</b>amily, <b>O</b>rder, <b>C</b>lass, "
                        "<b>P</b>hylum, <b>K</b>ingdom. Read it backwards for descending order."))

# ---- Table 1.1 ----
story.append(heading("Table 1.1", "Organisms with their Taxonomic Categories", level=2))
# [VERIFICATION FIX] Intro line, all four data rows and the reading NOTE are
# wrapped in KeepTogether so Table 1.1 is never split with a single orphan row
# stranded at a page break (F107, F110-F114).
story.append(KeepTogether([
    body("Table 1.1 indicates the taxonomic categories to which some common organisms "
         "like <b>housefly, man, mango and wheat</b> belong."),
    data_table([
        ["Common Name", "Biological Name", "Genus", "Family", "Order", "Class", "Phylum/Division"],
        ["Man", "<i>Homo sapiens</i>", "<i>Homo</i>", "Hominidae", "Primata", "Mammalia",
         "Chordata"],
        ["Housefly", "<i>Musca domestica</i>", "<i>Musca</i>", "Muscidae", "Diptera", "Insecta",
         "Arthropoda"],
        ["Mango", "<i>Mangifera indica</i>", "<i>Mangifera</i>", "Anacardiaceae", "Sapindales",
         "Dicotyledonae", "Angiospermae"],
        ["Wheat", "<i>Triticum aestivum</i>", "<i>Triticum</i>", "Poaceae", "Poales",
         "Monocotyledonae", "Angiospermae"],
    ], col_widths=[1.05, 1.5, 1.1, 1.5, 1.15, 1.5, 1.5], font_size=9.0),
    note("Read Table 1.1 column-wise for the two plant entries: mango is "
         "<b>Dicotyledonae</b> and wheat is <b>Monocotyledonae</b>, yet both are "
         "<b>Angiospermae</b> - the class differs while the division is the same."),
]))

# ---- Quick Recap ----
story.append(heading("Recap", "Quick Recap", level=1))
story.append(b1("The living world is <b>rich in variety</b>. Millions of plants and animals have "
                "been identified and described, but a <b>large number still remains unknown</b>. "
                "The range of organisms in <b>size, colour, habitat, physiological and "
                "morphological features</b> is what makes us seek the defining characteristics of "
                "living organisms. Known and described species: <b>1.7-1.8 million</b>."))
story.append(b1("To facilitate the study of kinds and diversity of organisms, biologists evolved "
                "<b>rules and principles for identification, nomenclature and classification</b>; "
                "the branch of knowledge dealing with these aspects is <b>taxonomy</b>."))
story.append(b1("The basics of taxonomy - identification, naming and classification - are "
                "<b>universally evolved under international codes</b>: <b>ICBN</b> for plants, "
                "<b>ICZN</b> for animals."))
story.append(b1("Based on <b>resemblances and distinct differences</b>, each organism is "
                "identified and assigned a correct scientific/biological name comprising "
                "<b>two words</b> as per the <b>binomial system of nomenclature</b> (Carolus "
                "Linnaeus): capitalised genus, small-letter specific epithet, Latin, italics in "
                "print and separately underlined when handwritten, with the abbreviated author "
                "name at the end."))
story.append(b1("An organism <b>occupies a place or position</b> in the system of classification. "
                "There are many <b>categories/ranks</b>, generally referred to as <b>taxonomic "
                "categories</b> or <b>taxa</b>, and all the categories constitute a <b>taxonomic "
                "hierarchy</b> - species (lowest) to kingdom (highest)."))
story.append(b1("Taxonomic studies of species of plants and animals are useful in "
                "<b>agriculture, forestry, industry</b> and for knowing our <b>bio-resources</b> "
                "and their diversity. <b>Systematics</b> adds <b>evolutionary relationships</b> to "
                "identification, nomenclature and classification."))

# ---- Appendix: Terms used in the exercises (Rule 2) ----
story.append(heading("Appendix", "Terms Used in the Exercises", level=1))
story.append(body("These exercise questions lean on points the chapter body assumes rather than "
                  "states outright. Each answer below is assembled <b>only</b> from facts stated "
                  "in this chapter."))
story.append(b1("<b>Why classification systems keep changing (Q2).</b> Three chapter facts explain "
                "it: (i) as we explore new areas, and even old ones, <b>new organisms are "
                "continuously being identified</b>, so the arrangement must accommodate them; "
                "(ii) taxonomists keep developing <b>sub-categories</b> in the hierarchy to "
                "facilitate more sound and scientific placement of various taxa; (iii) "
                "<b>systematics takes evolutionary relationships into account</b>, and the basis "
                "of modern taxonomic studies includes internal structure, cell structure, "
                "development process and ecological information - as this evidence improves, the "
                "grouping is revised."))
story.append(b1("<b>What identification of individuals and populations gives us (Q4).</b> "
                "Identification is what makes <b>nomenclature possible at all</b> - a name can be "
                "attached only to a correctly described organism. It yields a single universally "
                "valid name per organism, so that a description lets people in <b>any part of the "
                "world</b> arrive at the same name and no name is reused for another known "
                "organism; and it is how the count of <b>known and described species "
                "(1.7-1.8 million)</b>, i.e. our record of <b>biodiversity</b>, is built."))
story.append(b1("<b>The meaning of 'species' (Q8).</b> In this chapter, a species is a group of "
                "individual organisms with <b>fundamental similarities</b>, distinguishable from "
                "closely related species by <b>distinct morphological differences</b> - a "
                "morphological criterion. The unit profile adds that <b>Ernst Mayr pioneered the "
                "currently accepted definition of a biological species</b>. For higher plants and "
                "animals these criteria work well; <b>for bacteria this chapter supplies no "
                "criterion at all</b>, so that part of the question is deliberately left to "
                "discussion with your teacher rather than answered from outside sources."))
story.append(b1("<b>Answer keys the chapter fixes directly.</b> Q5 - the correctly written name is "
                "<i>Mangifera indica</i> (genus capitalised, specific epithet in small letters). "
                "Q7 - the correct sequence is <b>Species, Genus, Order, Phylum</b>, i.e. option "
                "(c), because the ascending order is Species, Genus, Family, Order, Class, Phylum "
                "or Division, Kingdom. Q6 - a <b>taxon</b> is a unit of classification "
                "representing a rank, e.g. <i>Homo</i> (genus), Hominidae (family), Primata "
                "(order), Mammalia (class), Chordata (phylum)."))

if __name__ == "__main__":
    sys.exit(build_pdf(OUT_PDF, story,
                       title="Class 11 Chapter 1 - The Living World (NEET notes)",
                       subject="NEET Biology"))
