"""Class 12 Chapter 6 Evolution: figureless replacement notes, built from the frozen inventory."""

import os
import sys

from reportlab.platypus import Paragraph

HERE = os.path.dirname(os.path.abspath(__file__))
root = HERE
while not os.path.isfile(os.path.join(root, "neet_template.py")):
    parent = os.path.dirname(root)
    if parent == root:
        raise FileNotFoundError("neet_template.py not found above Ch6_Evolution.py")
    root = parent
sys.path.insert(0, root)

from neet_template import STYLES, build_pdf, data_table, heading, keyterm, note, process_flow, title_block

OUT_PDF = os.path.join(HERE, "Ch6_Evolution.pdf")
story = []


def body(text):
    story.append(Paragraph(text, STYLES["Body"]))


def section(number, text, level=1, first=None, has_table=False):
    story.append(heading(number, text, level, has_table=has_table))
    if first:
        story.append(Paragraph(first, STYLES["Body"]))


# ---- Front matter; F001-F003 ----
story.extend(title_block("Evolution"))
body("<b>Evolutionary Biology</b> studies the history of life forms on earth. Changes in flora and fauna over millions of years make sense against the origin of life, the evolution of earth and stars, and the history of the universe. The story of biodiversity on earth is therefore set within the history of earth and the universe.")

# ---- 6.1 Origin of Life; F004-F016 ----
section("6.1", "Origin of Life", first="Looking at stars is, in a way, looking back in time: their light has travelled for millions of years across trillions of kilometres. Stellar distances are measured in light years; nearby objects, by comparison, appear to us in the present.")
body("The origin of life is considered a <b>unique event</b>. Earth is only a speck in a vast universe almost <b>13.8 billion years</b> old. Huge clusters of galaxies contain stars and clouds of gas and dust. The Big Bang theory proposes an unimaginable singular explosion followed by expansion and cooling. Hydrogen and helium formed later; gravitation condensed gases into galaxies.")
body("Earth formed in the Milky Way solar system about <b>4.5 billion years ago</b>. Early earth had no atmosphere. Vapours and gases released from molten material included water vapour, methane, carbon dioxide and ammonia. Solar UV split water into hydrogen and oxygen; lighter hydrogen escaped. Oxygen combined with ammonia and methane to form water, carbon dioxide and other substances, and an ozone layer formed. Cooling caused rain to fill depressions and make oceans. Life appeared about <b>500 million years after earth formed</b>, almost four billion years ago.")

# ---- 6.1 Theories on the Origin of Life; F017-F024 ----
section("6.1", "Theories on the Origin of Life", 2, first="Several proposals address the first appearance of life, but they do not have the same experimental support.")
section("6.1", "Panspermia", 3, first="Did life arrive from outer space? Early Greek thinkers imagined units of life called spores transferred among planets, including earth. This is <b>panspermia</b>, still favoured by some astronomers.")
section("6.1", "Spontaneous Generation", 3, first="The former belief that life arose from decaying straw, mud or other rotting matter was called <b>spontaneous generation</b>.")
body("<b>Louis Pasteur</b> showed that life comes only from pre-existing life: no new life arose from killed yeast in pre-sterilised flasks, whereas organisms arose when another flask containing killed yeast was open to air. This dismissed spontaneous generation, but did not explain how the first life form appeared.")

# ---- 6.1 Chemical Evolution and Miller's experiment; F025-F039 ----
section("6.1", "Chemical Evolution", 3, first="<b>Oparin</b> of Russia and <b>Haldane</b> of England proposed that life's first form could derive from non-living organic molecules, for example RNA and protein. <b>Chemical evolution</b> means diverse organic molecules formed from inorganic constituents before life arose.")
body("Early earth had high temperature, volcanic storms and a reducing atmosphere containing methane (CH<sub>4</sub>) and ammonia (NH<sub>3</sub>). In <b>1953</b>, American scientist <b>S. L. Miller</b> simulated such conditions: an electric discharge in a closed flask with CH<sub>4</sub>, H<sub>2</sub>, NH<sub>3</sub> and water vapour at <b>800 degrees C</b> yielded amino acids. Similar experiments yielded sugars, nitrogen bases, pigment and fats. Meteorites also contain related compounds, suggesting similar chemistry elsewhere in space; this limited evidence supports the chemical-evolution part of the conjectured account.")
body("Miller's apparatus can be followed without a diagram. <b>Boiling water</b> supplied vapour to the <b>Gases</b> in the loop. <b>Electrodes</b> produced a <b>Spark discharge</b> through CH4, NH3, H2O and H2. A <b>Condenser</b>, with <b>Water in</b> and <b>Water out</b>, cooled the mixture to <b>Water droplets</b>. The trap collected <b>Water containing organic compounds</b> in <b>Liquid water in trap</b>; the apparatus also had a connection <b>To vacuum pump</b>.")
body("How the first self-replicating metabolic capsule arose remains unknown. The earliest non-cellular forms could have appeared <b>3 billion years ago</b> as giant molecules such as RNA, protein and polysaccharides; perhaps these capsules reproduced their molecules. The first cellular forms probably did not appear until about <b>2000 million years ago</b>. They were probably single cells; all life was in water. This version of <b>biogenesis</b>, in which the first life form slowly arose from non-living molecules through evolutionary forces, is <b>accepted by majority</b>.")

# ---- 6.2 Evolution of Life Forms - A Theory; F040-F051 ----
section("6.2", "Evolution of Life Forms - A Theory", first="The theory of special creation in conventional religious literature claimed that present species were created as they are, diversity would always remain unchanged, and earth was about 4000 years old. Nineteenth-century evidence challenged all three claims.")
body("On his voyage around the world aboard the <i>H.M.S. Beagle</i>, <b>Charles Darwin</b> observed varying similarities among living forms and between living and long-extinct forms. Extinctions and the appearance of new forms at different times point to gradual evolution. <b>Alfred Wallace</b>, working in the Malay Archipelago, reached similar conclusions at about the same time.")
story.append(keyterm("<b>Natural selection:</b> populations contain inherited variation. Under conditions of climate, food and other physical factors, individuals with favourable traits survive and leave more progeny. Darwinian <b>fitness</b> ultimately means <b>reproductive fitness</b>, not mere strength or longevity."))
body("Present life forms share ancestors from different epochs, periods and eras. Geological history closely tracks biological history: earth is billions, not merely thousands, of years old.")

# ---- 6.3 Fossils and embryology; F052-F065 ----
section("6.3", "What are the Evidences for Evolution?", first="Independent lines of evidence come from fossils, embryology, comparative anatomy, biochemistry and observed selection.")
section("6.3", "Paleontological Evidence", 2, first="<b>Fossils</b> are remains of hard parts of life forms in rocks. Sedimentary layers formed at different times preserve different organisms; some resemble living organisms, whereas others, such as dinosaurs, are extinct.")
body("Fossils in successive layers indicate geological periods and show that life forms changed over time, with some restricted to particular time spans. This is <b>paleontological evidence</b>. Radioactive dating is used to estimate fossil ages. A dinosaur family tree can relate extinct <b>Triceratops</b>, <b>Tyrannosaurus</b>, <b>Pteranodon</b>, <b>Archaeopteryx</b>, <b>Stegosaurus</b> and <b>Brachiosaurus</b> to living lineages such as <b>Crocodilian</b> reptiles and birds.")
section("6.3", "Embryological Support", 2, first="<b>Ernst Heckel</b> proposed embryological support from features shared by vertebrate embryos but absent in adults. Human and other vertebrate embryos develop a row of vestigial gill slits just behind the head; these are functional only in fish and are absent in other adult vertebrates.")
body("<b>Karl Ernst von Baer</b> disapproved Heckel's proposal after careful study: embryos do not pass through the adult stages of other animals.")

# ---- 6.3 Comparative anatomy, selection; F066-F095 ----
section("6.3", "Comparative Anatomy and Morphology", 2, first="Comparing living organisms with one another and with past forms reveals similarities and differences that can indicate common ancestry.", has_table=True)
body("Human (<b>Man</b>), <b>Cheetah</b>, <b>Whale</b> and <b>Bat</b> forelimbs perform different jobs but share humerus, radius, ulna, carpals, metacarpals and phalanges. In plants, the <b>Thorn</b> of <i>Bougainvillea</i> and <b>Tendril</b> of <i>Cucurbita</i> share an origin. Vertebrate hearts and brains are further examples of homology.")
story.append(data_table([
    ["Pattern", "Meaning and examples"],
    ["Homology; divergent evolution", "Common structural origin, different adaptations: mammalian forelimbs; Bougainvillea thorn and Cucurbita tendril. Indicates common ancestry."],
    ["Analogy; convergent evolution", "Different anatomy, similar function: butterfly and bird wings; octopus and mammal eyes; Penguin and Dolphin flippers; sweet potato root and potato stem."],
], col_widths=[145, 365]))
body("A similar habitat may select similar functions in unrelated groups. Shared proteins and genes performing the same function across diverse organisms also point to common ancestry. Human selective breeding for agriculture, horticulture, sport and security has produced different breeds, for example dogs, within a group in only hundreds of years; nature has had millions of years.")
body("<b>Industrial melanism:</b> collections in the <b>1850s</b> before industrialisation had more white-winged than dark-winged (melanised) moths. By <b>1920</b>, the same area had more dark-winged moths. Against pale, lichen-covered trunks in unpolluted areas, birds more easily picked out dark moths; against soot-darkened trunks after industrialisation, birds spotted white moths and dark moths survived more often. Lichens are pollution indicators because they do not grow in polluted areas. Rural areas without industrialisation had few melanic moths. Camouflaged variants increased, but <b>no variant was completely wiped out</b>.")
body("Herbicides and pesticides select resistant varieties; antibiotics select resistant microbes, and drugs can select resistant eukaryotic organisms or cells. Such <b>anthropogenic evolution</b> can be observed within months or years, not centuries. Evolution is <b>not directed</b>: it is stochastic, involving chance events and chance mutations.")

# ---- 6.4 Adaptive radiation; F096-F109 ----
section("6.4", "What is Adaptive Radiation?", first="On the Galapagos Islands Darwin observed diverse small black birds, later called <b>Darwin's Finches</b>. He inferred that varieties evolved on the islands from seed-eating ancestors. Altered beaks suited insectivorous and vegetarian diets; the familiar comparison distinguishes four beak variants, numbered 1, 2, 3 and 4.")
story.append(keyterm("<b>Adaptive radiation:</b> different species evolve in one geographical area from a starting point, radiating into other areas or habitats. Darwin's finches are a classic example."))
body("<b>Marsupial radiation</b> in <b>Australia</b> likewise produced different forms from one ancestral stock: <b>Sugar glider</b>, <b>Tasmanian wolf</b>, <b>Tiger cat</b>, <b>Marsupial mole</b>, <b>Banded anteater</b>, <b>Koala</b>, <b>Marsupial rat</b>, <b>Bandicoot</b>, <b>Wombat</b> and <b>Kangaroo</b>.")
body("More than one adaptive radiation in an isolated region, filling similar habitats independently, illustrates <b>convergent evolution</b>. <b>Placental mammals</b> and <b>Australian marsupials</b> have corresponding forms: <b>Mole</b> and <b>Marsupial mole</b>; <b>Anteater</b> and <b>Numbat (anteater)</b>; <b>Mouse</b> and <b>Marsupial mouse</b>; <b>Lemur</b> and <b>Spotted cuscus</b>; <b>Flying squirrel</b> and <b>Flying phalanger</b>; <b>Bobcat</b> and <b>Tasmanian tiger cat</b>; <b>Wolf</b> and <b>Tasmanian wolf</b>. The placental wolf and Tasmanian wolf-marsupial show the same comparison.")

# ---- 6.5 Biological Evolution; F110-F129 ----
section("6.5", "Biological Evolution", first="Evolution through natural selection began in earnest when cellular life forms with different metabolic capacities appeared. <b>Natural selection</b> is central to Darwin's explanation.")
body("The speed at which forms appear depends on generation time. Microbes multiply into millions within hours. If bacterial population A varies in ability to use a nutrient, a changed medium favours variant B, which grows and may appear as a new species within days. An analogous change in a fish or fowl may take millions of years because their life spans are measured in years. B is fitter than A <i>in the new environment</i>.")
body("Selection acts on <b>inherited</b> characteristics: adaptation and fitness have a genetic basis. <b>Branching descent</b> and <b>natural selection</b> are Darwin's two key concepts. Before Darwin, French naturalist <b>Lamarck</b> proposed evolution through use and disuse: giraffes supposedly stretched to reach high leaves and passed acquired long necks to offspring. This conjecture is no longer believed.")
body("Evolution may be described as a process when telling the world's story, or as the consequence of natural selection when telling the history of life. Whether evolution and natural selection are processes or outcomes of unknown processes is still not entirely clear in this account.")
body("<b>Thomas Malthus</b> may have influenced Darwin. Resources are limited; populations usually remain stable apart from seasonal fluctuations, though maximal reproduction would yield exponential growth. Individuals vary, and most variations are inherited. Competition means only some survive and grow at the cost of others. Those with heritable traits that better use resources leave more progeny; across generations population characteristics shift and new forms appear.")
body("The three outcomes of selection can be read as changes in the <b>Number of individuals with phenotype</b> across trait values, showing <b>Phenotypes favoured by natural selection</b>: in stabilising selection <b>Medium-sized individuals are favoured</b> and the <b>Peak gets higher and narrower</b>; in directional selection the <b>Peak shifts in one direction</b>; in disruptive selection <b>Two peaks form</b>.")

# ---- 6.6 Mechanism of Evolution; F130-F137 ----
section("6.6", "Mechanism of Evolution", first="Where does heritable variation come from, and how does speciation occur? Mendel described inherited factors affecting phenotype, but Darwin ignored or did not discuss these observations.")
body("In the first decade of the twentieth century, <b>Hugo de Vries</b> studied evening primrose and proposed <b>mutations</b>, large differences appearing suddenly in populations. He credited mutation rather than Darwin's minor heritable variations as the cause of evolution. Mutations are random and directionless; Darwinian variations were described as small and directional. Darwin envisaged gradual evolution; de Vries proposed <b>saltation</b>, speciation through a single large-step mutation. Later population genetics clarified the picture.")

# ---- 6.7 Hardy-Weinberg Principle; F138-F157, F198 ----
section("6.7", "Hardy-Weinberg Principle", first="A population has measurable frequencies of alleles at each locus. In the absence of disturbing factors these frequencies remain constant across generations: this is <b>genetic equilibrium</b>. The <b>gene pool</b> is the total of the genes and alleles in that population.")
body("All allele frequencies sum to <b>1</b>. For two alleles A and a in diploids, let their frequencies be p and q: <b>p + q = 1</b>. Expected genotype frequencies are AA = p<super>2</super>, Aa = 2pq and aa = q<super>2</super>, so <b>p<super>2</super> + 2pq + q<super>2</super> = 1</b>, the expansion of (p + q)<super>2</super>. A difference between measured and expected frequencies indicates the extent and direction of evolutionary change; disturbed equilibrium means allele-frequency change.")
body("Five factors can disturb Hardy-Weinberg equilibrium: <b>gene migration or gene flow</b>, <b>genetic drift</b>, <b>mutation</b>, <b>genetic recombination</b> and <b>natural selection</b>.")
story.append(process_flow([
    "Migration of a section of a population changes frequencies both where it leaves (alleles lost) and where it arrives (alleles added). Repeated migration produces gene flow.",
    "A chance change in allele frequency is genetic drift. If a small founding sample differs strongly from the old population, its descendants may become a different species: the founder effect.",
    "Pre-existing advantageous mutations selected in microbial experiments yield new phenotypes; over a few generations this can produce speciation.",
    "Mutation, recombination during gametogenesis, gene flow and drift change future allele frequencies; natural selection increases the offspring of individuals carrying favourable inherited variants.",
]))
body("<b>Habitat fragmentation</b> and genetic drift may accentuate variation, leading to new species and evolution. Selection can produce <b>stabilisation</b> (more individuals near the mean), <b>directional change</b> (more individuals with a value away from the mean) or <b>disruption</b> (more individuals at both extremes of the distribution).")

# ---- 6.8 A Brief Account of Evolution; F158-F185 ----
section("6.8", "A Brief Account of Evolution", first="The first cellular forms appeared about <b>2000 million years ago (mya)</b>. How giant non-cellular macromolecular aggregates became membrane-bound cells is unknown. Some cells released oxygen, perhaps using light-driven splitting of water with energy captured by light-harvesting pigments.")
story.append(data_table([
    ["Approximate time", "Event in the account"],
    ["500 mya", "Invertebrates were active after single cells had gradually become multicellular."],
    ["Around 350 mya", "Jawless fish probably evolved; strong-finned fish could move on land and return to water."],
    ["Around 320 mya", "Sea weeds and a few plants probably existed; plants were the first to invade land and spread before animals arrived."],
    ["1938", "A Coelacanth caught in South Africa was a lobefin fish thought extinct."],
    ["Probably 200 mya", "Some land reptiles returned to water and became fish-like reptiles, for example Ichthyosaurs."],
    ["About 65 mya", "Dinosaurs disappeared suddenly; the true cause remains unknown."],
], col_widths=[115, 395]))
body("Lobefins gave rise to the first amphibians, living on land and in water, ancestral to modern frogs and salamanders; no specimens of those first amphibians survive. Amphibians gave rise to reptiles, whose thick-shelled eggs, <b>unlike those of amphibians</b>, do not dry up in sunlight. Turtles, tortoises and crocodiles are modern descendants. Reptiles dominated for the next <b>200 million years or so</b>; giant ferns and other pteridophytes slowly formed coal deposits.")
body("The land reptiles included dinosaurs. <i>Tyrannosaurus rex</i> was about <b>20 feet</b> tall, with large dagger-like teeth. Dinosaurs disappeared about <b>65 mya</b>; climatic change and evolution of some into birds have been proposed, but the true reason is unknown and the truth <b>may lie in between</b>. Small reptiles from that era still exist.")
body("A geological sketch of plant evolution spans <b>Paleozoic</b> (Silurian, Devonian, Carboniferous, Permian), <b>Mesozoic</b> (Triassic, Jurassic, Cretaceous) and <b>Cenozoic</b> (Tertiary, Quaternary). Among its plant lineages are <b>chlorophyte ancestors</b>, <b>tracheophyte ancestors</b>, <b>Rhynia-type plants</b>, <b>Zosterophyllum</b>, <b>Psilophyton</b> and <b>Progymnosperms</b>; <b>arborescent lycopods</b>, <b>herbaceous lycopods</b>, <b>Sphenopsids (horsetails)</b>, <b>Ferns</b> and <b>Bryophytes</b>; <b>seed ferns</b>, <b>Cycads</b>, <b>Conifers</b>, <b>Ginkgos</b> and <b>Gnetales</b>; and <b>Angiosperms (flowering plants)</b>, divided into <b>Monocotyledons</b> and <b>Dicotyledons</b>.")
body("A comparable vertebrate history through the <b>Carboniferous</b>, <b>Permian</b>, <b>Triassic</b>, <b>Jurassic</b>, <b>Cretaceous</b>, <b>Tertiary</b> and <b>Quaternary</b> distinguishes <b>Early reptiles (extinct)</b>, <b>Pelycosaurs (extinct)</b>, <b>Therapsids (extinct)</b>, <b>Synapsids</b>, <b>Thecodonts (extinct)</b>, <b>Sauropsids</b> and <b>Dinosaurs (extinct)</b>. Living branches include <b>Turtles</b>, <b>Lizards</b>, <b>Snakes</b>, <b>Tuataras</b>, <b>Crocodiles</b>, <b>Birds</b> and <b>Mammals</b>. Together these plant and vertebrate sequences place evolutionary histories on a geological time scale.")
body("Early mammals resembled small shrews. They were viviparous, sheltered their unborn young within the mother's body and better sensed and avoided danger. After reptile dominance waned, mammals spread. South American mammals resembling horses, hippopotamuses, bears and rabbits were overridden by North American fauna when continental drift joined the continents; Australia's pouched mammals persisted with little competition. Fully aquatic mammals include whales, dolphins, seals and sea cows. Horse, elephant and dog evolution each have their own story; human evolution, with language and self-consciousness, is especially striking.")

# ---- 6.9 Origin and Evolution of Man; F186-F197 ----
section("6.9", "Origin and Evolution of Man", first="About <b>15 mya</b>, hairy primates <i>Dryopithecus</i> and <i>Ramapithecus</i> walked like gorillas and chimpanzees. <i>Ramapithecus</i> was more man-like; <i>Dryopithecus</i> was more ape-like.")
story.append(data_table([
    ["Stage / date", "Evidence and traits"],
    ["About 3-4 mya", "Fossils from Ethiopia and Tanzania show hominid traits. Upright eastern African primates were probably under four feet tall."],
    ["About 2 mya", "Australopithecines probably lived in East African grasslands, hunted with stone weapons and ate mainly fruit."],
    ["Homo habilis", "First human-like hominid in this account; 650-800 cc brain; probably did not eat meat."],
    ["Homo erectus; about 1.5 mya", "Fossils found in Java in 1891; brain around 900 cc; probably ate meat."],
    ["Neanderthal; 100,000-40,000 years ago", "Near East and central Asia; 1400 cc brain; used hides for protection and buried the dead."],
    ["Homo sapiens", "Arose in Africa, moved across continents and developed into distinct races; modern Homo sapiens arose during the ice age, 75,000-10,000 years ago."],
], col_widths=[145, 365]))
body("A comparison of skulls shows that the <b>baby chimpanzee</b> skull is more similar to an <b>adult modern human</b> skull than to an <b>adult chimpanzee</b> skull. Prehistoric cave art appeared about <b>18,000 years ago</b>; a painting survives at the <b>Bhimbetka rock shelter</b> in Raisen district, Madhya Pradesh. Agriculture and settlements began around <b>10,000 years ago</b>; the subsequent rise and decline of civilisations belongs to human history.")

# ---- Quick Recap; source summary S1-S9 ----
section("Recap", "Quick Recap", 1, first="Life's origin is considered against the formation of the universe and earth. Chemical evolution of biomolecules preceded the first cells; the later history of life is reconstructed through Darwinian branching descent and natural selection.")
body("Inherited variation changes reproductive fitness in a changing environment. Fossils, anatomy and biochemistry reveal change and common ancestry; homologous organs support branching descent. Drift and habitat fragmentation can accentuate population differences. The evolution of modern humans accompanies changes in the brain, language and behaviour.")

# ---- Terms used in the exercises; exercise 3 only ----
section("Appendix", "Terms used in the exercises", 1, first="<b>Exercise 3. Give a clear definition of species.</b> A species is a group of organisms that can interbreed in nature and produce fertile offspring, reproductively isolated from other such groups.")


def main():
    try:
        build_pdf(OUT_PDF, story, title="Class 12 Chapter 6 - Evolution (NEET notes)")
    except (OSError, ValueError) as exc:
        raise RuntimeError(f"Could not build Evolution PDF at {OUT_PDF}: {exc}") from exc


if __name__ == "__main__":
    main()
