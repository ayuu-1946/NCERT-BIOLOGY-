# Frozen Inventory — Evolution (Class 12, Chapter 6)
Source: `Chapter/class 12/Chapter 6 - Evolution.pdf` (17 pp) — inventoried from the prepared figureless transcript `chapter_6_evolution.md` | Frozen: 2026-09-26 | Rows: **198** (`F001`..`F198`, contiguous)

**FIGURELESS EDITION — operator order.** This chapter is being produced figureless by explicit user order. No figure assets are extracted, converted, or embedded; session 1-F is therefore run as a *textual* figure sweep — every figure caption and every in-figure textual label transcribed in the source is still captured as a Facts row (Rule 1: zero information loss), and every in-figure label is entered as a `figure-label` row so that Pass 2 prose is forced to carry the figure's biological content in running text (check 6). The `Mono`/`Verified` asset obligations (§4.4 Step 2–3) do not apply because nothing is embedded; this is recorded against the Gate 1 checklist below as **N/A — figureless**, not as an unmet criterion.

Tick legend: `x` = row's substantive content written into the script and verified present in the generated PDF, except explicitly approved trivial wording omissions recorded below. **All 198 rows are ticked**; the Gate 1 row set and original wording remain frozen.

**Approved page-1 trims (post-Gate 2):** Omit only the redundant concluding sentence in F003, the nearby-objects comparison adjacent to F006, the earth-as-speck analogy in F007/F009, and the unsupported comparative introduction after heading F017. The concepts, dates, and named mechanisms in those rows remain in the PDF. No page 2–5 trims were approved or made.

## Header counts — all machine-derived (§5 step 10), never hand-tallied

| Count | Value |
|---|---|
| Facts rows total | **198** — `F001`..`F198` |
| ID range / contiguity | `F001`..`F198` — 0 gaps, 0 duplicates |
| `Type: heading` rows | **17** — 1 front + 9 numbered (6.1–6.9) + 7 unnumbered sub-headings (Theories on the Origin of Life; Panspermia; Spontaneous Generation; Chemical Evolution; Paleontological Evidence; Embryological Support; Comparative Anatomy and Morphology) |
| `Type: opener` rows | **16** — chapter opener + 6.1 + Panspermia + Spontaneous Generation + Chemical Evolution + 6.2 + 6.3 + Paleontological + Embryological + Comparative Anatomy + 6.4 + 6.5 + 6.6 + 6.7 + 6.8 + 6.9 |
| `Type: caption` rows | **11** — one per omitted figure Fig 6.1–Fig 6.11 (F033, F060, F075, F087, F100, F104, F108, F128, F170, F178, F195) |
| `Type: figure-label` rows | **8** — Fig 6.1, 6.2, 6.3, 6.6, 6.7, 6.8, 6.9, 6.10 (F034, F061, F076, F105, F109, F129, F171, F179); Fig 6.4/6.5/6.11 carry no discrete textual labels |
| Label strings parsed by `_extract_labels` | **116** — 15+7+8+12+16+6+31+21, no doubling, no phantom `Fig #` row (verified by running check_pdf.py's own parser this session) |
| Summary sentences classified | **9** — BODY-PRESENT 8, SUMMARY-UNIQUE 1 (folded to F198) |
| Exercise questions scanned | **10** — GAP 1, COVERED 9, 0 overlooked |
| Figures | **11** (Fig 6.1–6.11), **all deliberately omitted — figureless edition**; no assets on disk, `Mono`/`Verified` N/A |

> ## GATE 1 STATUS: **GREEN — CLOSED. Gate 2 complete; Pass 3 pending.**
>
> | Gate 1 requirement (§7) | State |
> |---|---|
> | Environment re-established | done — CPython 3.13.11; only stdlib (`re`, `difflib`) needed because a figureless Pass 1 renders/extracts nothing. The full `neetenv` (reportlab/pdfplumber/pymupdf/Pillow) is a Pass 2 dependency and is deliberately not rebuilt this session |
> | Every fact has a Facts row (three source reads) | done — 198 rows, `F001`..`F198` |
> | Every in-figure label has a matrix row | done — 8 `figure-label` rows carrying 116 labels; harvested from the transcribed source labels (no assets exist to open — figureless) |
> | Inventory validated by running `check_pdf.py`'s own `_extract_labels` | done — parses **8 figures / 116 labels**, no doubling, no `Fig #` phantom row |
> | Header counts match a re-parse of the table; IDs contiguous | done — see count table; `F001`..`F198`, 0 gaps/dupes; `Type` normalized (no case-variant duplicates) |
> | Every heading has a row, incl. unnumbered sub-headings (1-H) | done — 17 heading rows, walked as their own list |
> | Every section's opening sentence has a row (1-O) | done — 16 opener rows |
> | Every figure `Mono: yes` and `Verified: yes` | **N/A — figureless by operator order**; nothing embedded, so no asset to greyscale or verify |
> | Every exercise-gap term has a planned home | done — 1 gap (definition of *species*) routed to the closing "Terms used in the exercises" appendix |
> | Every SUMMARY-UNIQUE fact folded into a body row | done — 1 folded (habitat fragmentation) → F198 in §6.7 |
> | Inventory file saved to the chapter folder | done — this file |
>
> **Pass 1 sessions (all five ran; each reported its own machine-derived count):**
> 1-S source read → Facts drafted; 1-H heading sweep → 17 heading rows; 1-O opener sweep → 16 opener rows; 1-F figure sweep (textual, figureless) → 11 caption rows + 8 figure-label rows (116 labels); 1-Z gaps/summary/freeze → 198 rows frozen, counts re-parsed.

---

## Facts

| ID | Section | Type | Exact original wording | Ticked |
|----|---------|------|------------------------|--------|
| F001 | front | heading | "CHAPTER 6 — EVOLUTION" with contents list: 6.1 Origin of Life; 6.2 Evolution of Life Forms - A Theory; 6.3 What are the Evidences for Evolution?; 6.4 What is Adaptive Radiation?; 6.5 Biological Evolution; 6.6 Mechanism of Evolution; 6.7 Hardy-Weinberg Principle; 6.8 A Brief Account of Evolution; 6.9 Origin and Evolution of Man | x |
| F002 | 6-open | opener | "Evolutionary Biology is the study of history of life forms on earth." | x |
| F003 | 6-open | concept | To understand changes in flora and fauna over millions of years we must understand "the context of origin of life, i.e., evolution of earth, of stars and indeed of the universe itself"; the chapter is "the story of origin of life and evolution of life forms or biodiversity on planet earth in the context of evolution of earth and against the background of evolution of universe itself." | x |
| F004 | 6.1 | heading | "6.1 Origin of Life" | x |
| F005 | 6.1 | opener | "When we look at stars on a clear night sky we are, in a way, looking back in time." | x |
| F006 | 6.1 | concept | "Stellar distances are measured in light years." Light we see today started its journey millions of years back from trillions of kilometres away; "when we see stars we apparently are peeping into the past." | x |
| F007 | 6.1 | concept | "The origin of life is considered a unique event in the history of universe." The universe is vast; "the earth itself is almost only a speck." | x |
| F008 | 6.1 | number | "The universe is very old - almost 13.8 billion years old." | x |
| F009 | 6.1 | concept | "Huge clusters of galaxies comprise the universe. Galaxies contain stars and clouds of gas and dust. Considering the size of universe, earth is indeed a speck." | x |
| F010 | 6.1 | concept | "The Big Bang theory attempts to explain to us the origin of universe. It talks of a singular huge explosion unimaginable in physical terms. The universe expanded and hence, the temperature came down." | x |
| F011 | 6.1 | process | "Hydrogen and Helium formed sometime later. The gases condensed under gravitation and formed the galaxies of the present day universe." | x |
| F012 | 6.1 | number | "In the solar system of the milky way galaxy, earth was supposed to have been formed about 4.5 billion years back." | x |
| F013 | 6.1 | concept | "There was no atmosphere on early earth. Water vapour, methane, carbon dioxide and ammonia released from molten mass covered the surface." | x |
| F014 | 6.1 | process | "The UV rays from the sun broke up water into Hydrogen and Oxygen and the lighter H2 escaped. Oxygen combined with ammonia and methane to form water, CO2 and others. The ozone layer was formed." | x |
| F015 | 6.1 | process | "As it cooled, the water vapour fell as rain, to fill all the depressions and form oceans." | x |
| F016 | 6.1 | number | "Life appeared 500 million years after the formation of earth, i.e., almost four billion years back." | x |
| F017 | 6.1 | heading | "Theories on the Origin of Life" | x |
| F018 | 6.1 | heading | "Panspermia" | x |
| F019 | 6.1 | opener | "Did life come from outer space?" — "Some scientists believe that it came from outside." | x |
| F020 | 6.1 | concept | "Early Greek thinkers thought units of life called spores were transferred to different planets including earth. Panspermia is still a favourite idea for some astronomers." | x |
| F021 | 6.1 | heading | "Spontaneous Generation" | x |
| F022 | 6.1 | opener | "For a long time it was also believed that life came out of decaying and rotting matter like straw, mud, etc. This was the theory of spontaneous generation." | x |
| F023 | 6.1 | name | "Louis Pasteur by careful experimentation demonstrated that life comes only from pre-existing life." | x |
| F024 | 6.1 | process | Pasteur showed that "in pre-sterilised flasks, life did not come from killed yeast while in another flask open to air, new living organisms arose from killed yeast. Spontaneous generation theory was dismissed once and for all." "However, this did not answer how the first life form came on earth." | x |
| F025 | 6.1 | heading | "Chemical Evolution" | x |
| F026 | 6.1 | opener | "Oparin of Russia and Haldane of England proposed that the first form of life could have come from pre-existing non-living organic molecules, for example RNA and protein, and that formation of life was preceded by chemical evolution" | x |
| F027 | 6.1 | definition | chemical evolution, i.e., "formation of diverse organic molecules from inorganic constituents." | x |
| F028 | 6.1 | concept | "The conditions on earth were high temperature, volcanic storms, and a reducing atmosphere containing CH4, NH3, etc." | x |
| F029 | 6.1 | name | "In 1953, S. L. Miller, an American scientist, created similar conditions on a laboratory scale." | x |
| F030 | 6.1 | process | "He created electric discharge in a closed flask containing CH4, H2, NH3 and water vapour at 800 degrees C. He observed formation of amino acids." | x |
| F031 | 6.1 | example | "In similar experiments others observed formation of sugars, nitrogen bases, pigment and fats." | x |
| F032 | 6.1 | concept | "Analysis of meteorite content also revealed similar compounds, indicating that similar processes are occurring elsewhere in space." "the first part of the conjectured story, i.e., chemical evolution was more or less accepted." | x |
| F033 | 6.1 | caption | Figure 6.1 (omitted, figureless edition). Caption: "Diagrammatic representation of Miller's experiment." | x |
| F034 | Fig 6.1 | figure-label | Figure labels: "Electrodes"; "Spark discharge"; "Gases"; "CH4"; "NH3"; "H2O"; "H2"; "To vacuum pump"; "Boiling water"; "Water out"; "Condenser"; "Water in"; "Water droplets"; "Water containing organic compounds"; "Liquid water in trap" | x |
| F035 | 6.1 | concept | "We have no idea about how the first self-replicating metabolic capsule of life arose." | x |
| F036 | 6.1 | number | "The first non-cellular forms of life could have originated 3 billion years back." | x |
| F037 | 6.1 | concept | "They would have been giant molecules, such as RNA, protein, polysaccharides, etc. These capsules reproduced their molecules perhaps." | x |
| F038 | 6.1 | number | "The first cellular form of life did not possibly originate till about 2000 million years ago. These were probably single-cells." | x |
| F039 | 6.1 | concept | "All life forms were in water environment only." Biogenesis: "the first form of life arose slowly through evolutionary forces from non-living molecules, is accepted by majority." | x |
| F040 | 6.2 | heading | "6.2 Evolution of Life Forms - A Theory" | x |
| F041 | 6.2 | opener | "Conventional religious literature tells us about the theory of special creation." | x |
| F042 | 6.2 | concept | Special creation has three connotations: "One, that all living organisms, species or types, that we see today were created as such. Two, that the diversity was always the same since creation and will be the same in future also. Three, that earth is about 4000 years old." "All these ideas were strongly challenged during the nineteenth century." | x |
| F043 | 6.2 | name | "Based on observations made during a sea voyage in a sail ship called H.M.S. Beagle round the world, Charles Darwin concluded that existing living forms share similarities to varying degrees not only among themselves but also with life forms that existed millions of years ago." | x |
| F044 | 6.2 | concept | "Many such life forms do not exist any more." Extinctions occurred just as new forms arose at different periods; "There has been gradual evolution of life forms." | x |
| F045 | 6.2 | concept | "Any population has built-in variation in characteristics." | x |
| F046 | 6.2 | concept | Characteristics "which enable some to survive better in natural conditions, such as climate, food and physical factors, would outbreed others that are less endowed to survive under such natural conditions." | x |
| F047 | 6.2 | definition | "Another word used is fitness of the individual or population. The fitness, according to Darwin, refers ultimately and only to reproductive fitness." | x |
| F048 | 6.2 | concept | "those who are better fit in an environment leave more progeny than others. These, therefore, will survive more and hence are selected by nature. He called it natural selection and implied it as a mechanism of evolution." | x |
| F049 | 6.2 | name | "Alfred Wallace, a naturalist who worked in Malay Archipelago, had also come to similar conclusions around the same time." | x |
| F050 | 6.2 | concept | "All the existing life forms share similarities and share common ancestors." These ancestors were present at different periods — "namely epochs, periods and eras." | x |
| F051 | 6.2 | concept | "The geological history of earth closely correlates with the biological history of earth." Earth is "not thousands of years as was thought earlier but billions of years old." | x |
| F052 | 6.3 | heading | "6.3 What are the Evidences for Evolution?" | x |
| F053 | 6.3 | opener | "Evidence that evolution of life forms has indeed taken place on earth has come from many quarters." | x |
| F054 | 6.3 | heading | "Paleontological Evidence" | x |
| F055 | 6.3 | opener | "Fossils are remains of hard parts of life-forms found in rocks." | x |
| F056 | 6.3 | process | "Rocks form sediments and a cross-section of earth's crust indicates the arrangement of sediments one over the other during the long history of earth. Different-aged rock sediments contain fossils of different life-forms who probably died during the formation of the particular sediment." | x |
| F057 | 6.3 | example | "Some of them appear similar to modern organisms. They represent extinct organisms, for example dinosaurs." | x |
| F058 | 6.3 | concept | "A study of fossils in different sedimentary layers indicates the geological period in which they existed." Life-forms varied over time; "certain life forms are restricted to certain geological time-spans." "All this is called paleontological evidence." | x |
| F059 | 6.3 | question | "Do you remember how the ages of the fossils are calculated? Do you recollect the method of radioactive-dating and the principles behind the procedure?" | x |
| F060 | 6.3 | caption | Figure 6.2 (omitted, figureless edition). Caption: "A family tree of dinosaurs and their living modern day counterpart organisms like crocodiles and birds." | x |
| F061 | Fig 6.2 | figure-label | Figure labels: "Triceratops"; "Tyrannosaurus"; "Pteranodon"; "Crocodilian"; "Archaeopteryx"; "Stegosaurus"; "Brachiosaurus" | x |
| F062 | 6.3 | heading | "Embryological Support" | x |
| F063 | 6.3 | opener | "Embryological support for evolution was also proposed by Ernst Heckel based upon the observation of certain features during embryonic stage common to all vertebrates that are absent in adult." | x |
| F064 | 6.3 | example | "the embryos of all vertebrates including human develop a row of vestigial gill slit just behind the head but it is a functional organ only in fish and not found in any other adult vertebrates." | x |
| F065 | 6.3 | name | "this proposal was disapproved on careful study performed by Karl Ernst von Baer. He noted that embryos never pass through the adult stages of other animals." | x |
| F066 | 6.3 | heading | "Comparative Anatomy and Morphology" | x |
| F067 | 6.3 | opener | "Comparative anatomy and morphology shows similarities and differences among organisms of today and those that existed years ago." | x |
| F068 | 6.3 | concept | "Such similarities can be interpreted to understand whether common ancestors were shared or not." | x |
| F069 | 6.3 | example | "whales, bats, cheetah and human, all mammals, share similarities in the pattern of bones of forelimbs." Different functions but "they have similar anatomical structure." | x |
| F070 | 6.3 | list | Forelimb bones shared: "humerus, radius, ulna, carpals, metacarpals and phalanges." | x |
| F071 | 6.3 | definition | "the same structure developed along different directions due to adaptations to different needs. This is divergent evolution and these structures are homologous. Homology indicates common ancestry." | x |
| F072 | 6.3 | example | "Other examples are vertebrate hearts or brains." | x |
| F073 | 6.3 | example | "In plants also, the thorn and tendrils of Bougainvillea and Cucurbita represent homology." | x |
| F074 | 6.3 | definition | "Homology is based on divergent evolution whereas analogy refers to a situation exactly opposite." | x |
| F075 | 6.3 | caption | Figure 6.3 (omitted, figureless edition). Caption: "Example of homologous organs in (a) Plants and (b) Animals." | x |
| F076 | Fig 6.3 | figure-label | Figure labels: "Thorn"; "Bougainvillea"; "Tendril"; "Cucurbita"; "Man"; "Cheetah"; "Whale"; "Bat" | x |
| F077 | 6.3 | example | "Wings of butterfly and of birds look alike. They are not anatomically similar structures though they perform similar functions." | x |
| F078 | 6.3 | definition | "analogous structures are a result of convergent evolution - different structures evolving for the same function and hence having similarity." | x |
| F079 | 6.3 | example | Other examples of analogy: "the eye of the octopus and of mammals or the flippers of Penguins and Dolphins." | x |
| F080 | 6.3 | concept | "it is the similar habitat that has resulted in selection of similar adaptive features in different groups of organisms but toward the same function." | x |
| F081 | 6.3 | example | "Sweet potato, a root modification, and potato, a stem modification, is another example for analogy." | x |
| F082 | 6.3 | concept | "similarities in proteins and genes performing a given function among diverse organisms give clues to common ancestry. These biochemical similarities point to the same shared ancestry as structural similarities among diverse organisms." | x |
| F083 | 6.3 | concept | "Man has bred selected plants and animals for agriculture, horticulture, sport or security. Man has domesticated many wild animals and crops." | x |
| F084 | 6.3 | example | "This intensive breeding programme has created breeds that differ from other breeds, for example dogs, but still are of the same group." Argument: "if within hundreds of years man could create new breeds, could not nature have done the same over millions of years?" | x |
| F085 | 6.3 | number | "In a collection of moths made in 1850s, i.e., before industrialisation set in, it was observed that there were more white-winged moths on trees than dark-winged or melanised moths." | x |
| F086 | 6.3 | number | "in the collection carried out from the same area, but after industrialisation, i.e., in 1920, there were more dark-winged moths in the same area, i.e., the proportion was reversed." | x |
| F087 | 6.3 | caption | Figure 6.4 (omitted, figureless edition). Caption: "Figure showing white-winged moth and dark-winged moth (melanised) on a tree trunk (a) In unpolluted area (b) In polluted area." | x |
| F088 | 6.3 | concept | "predators will spot a moth against a contrasting background." | x |
| F089 | 6.3 | concept | "During post-industrialisation period, the tree trunks became dark due to industrial smoke and soots. Under this condition the white-winged moth did not survive due to predators, dark-winged or melanised moth survived." | x |
| F090 | 6.3 | concept | "Before industrialisation set in, thick growth of almost white-coloured lichen covered the trees - in that background the white-winged moth survived but the dark-coloured moth were picked out by predators." | x |
| F091 | 6.3 | concept | "Do you know that lichens can be used as industrial pollution indicators? They will not grow in areas that are polluted." | x |
| F092 | 6.3 | concept | "moths that were able to camouflage themselves, i.e., hide in the background, survived." In rural non-industrialised areas "the count of melanic moths was low." "in a mixed population, those that can better adapt survive and increase in population size. Remember that no variant is completely wiped out." | x |
| F093 | 6.3 | example | "excess use of herbicides, pesticides, etc., has only resulted in selection of resistant varieties in a much lesser time scale. This is also true for microbes against which we employ antibiotics or drugs against eukaryotic organisms or cells." | x |
| F094 | 6.3 | concept | "resistant organisms or cells are appearing in a time scale of months or years and not centuries. These are examples of evolution by anthropogenic action." | x |
| F095 | 6.3 | concept | "evolution is not a directed process, but is a stochastic process based on chance events in nature and chance mutation in the organisms." | x |
| F096 | 6.4 | heading | "6.4 What is Adaptive Radiation?" | x |
| F097 | 6.4 | opener | "During his journey Darwin went to Galapagos Islands." | x |
| F098 | 6.4 | example | "There he observed an amazing diversity of creatures." "small black birds later called Darwin's Finches amazed him." "there were many varieties of finches in the same island." | x |
| F099 | 6.4 | concept | "All the varieties, he conjectured, evolved on the island itself. From the original seed-eating features, many other forms with altered beaks arose, enabling them to become insectivorous and vegetarian finches." | x |
| F100 | 6.4 | caption | Figure 6.5 (omitted, figureless edition). Caption: "Variety of beaks of finches that Darwin found in Galapagos Island." (four beak variants labelled only 1, 2, 3, 4 — no discrete textual labels) | x |
| F101 | 6.4 | definition | "This process of evolution of different species in a given geographical area starting from a point and literally radiating to other areas of geography, or habitats, is called adaptive radiation." | x |
| F102 | 6.4 | example | "Darwin's finches represent one of the best examples of this phenomenon." | x |
| F103 | 6.4 | example | "Another example is Australian marsupials. A number of marsupials, each different from the other, evolved from an ancestral stock, but all within the Australian island continent." | x |
| F104 | 6.4 | caption | Figure 6.6 (omitted, figureless edition). Caption: "Adaptive radiation of marsupials of Australia." | x |
| F105 | Fig 6.6 | figure-label | Figure labels: "Marsupial radiation"; "Australia"; "Sugar glider"; "Tasmanian wolf"; "Tiger cat"; "Marsupial mole"; "Banded anteater"; "Koala"; "Marsupial rat"; "Bandicoot"; "Wombat"; "Kangaroo" | x |
| F106 | 6.4 | definition | "When more than one adaptive radiation appeared to have occurred in an isolated geographical area, representing different habitats, one can call this convergent evolution." | x |
| F107 | 6.4 | example | "Placental mammals in Australia also exhibit adaptive radiation in evolving into varieties of such placental mammals, each of which appears to be similar to a corresponding marsupial, for example placental wolf and Tasmanian wolf-marsupial." | x |
| F108 | 6.4 | caption | Figure 6.7 (omitted, figureless edition). Caption: "Picture showing convergent evolution of Australian marsupials and placental mammals." | x |
| F109 | Fig 6.7 | figure-label | Figure labels: "Placental mammals"; "Australian marsupials"; "Mole"; "Marsupial mole"; "Anteater"; "Numbat (anteater)"; "Mouse"; "Marsupial mouse"; "Lemur"; "Spotted cuscus"; "Flying squirrel"; "Flying phalanger"; "Bobcat"; "Tasmanian tiger cat"; "Wolf"; "Tasmanian wolf" | x |
| F110 | 6.5 | heading | "6.5 Biological Evolution" | x |
| F111 | 6.5 | opener | "Evolution by natural selection, in a true sense, would have started when cellular forms of life with differences in metabolic capability originated on earth." | x |
| F112 | 6.5 | concept | "The essence of Darwinian theory about evolution is natural selection." | x |
| F113 | 6.5 | concept | "The rate of appearance of new forms is linked to the life cycle or the life span." | x |
| F114 | 6.5 | example | "Microbes that divide fast have the ability to multiply and become millions of individuals within hours." Colony A has built-in variation; a change in medium composition brings out only part B that can survive; "this variant population outgrows the others and appears as new species. This would happen within days." | x |
| F115 | 6.5 | comparison | "For the same thing to happen in a fish or fowl would take millions of years as life spans of these animals are in years." | x |
| F116 | 6.5 | concept | "fitness of B is better than that of A under the new conditions. Nature selects for fitness." | x |
| F117 | 6.5 | concept | "the so-called fitness is based on characteristics which are inherited. Hence, there must be a genetic basis for getting selected and to evolve." | x |
| F118 | 6.5 | concept | "Adaptive ability is inherited. It has a genetic basis. Fitness is the end result of the ability to adapt and get selected by nature." | x |
| F119 | 6.5 | concept | "Branching descent and natural selection are the two key concepts of Darwinian Theory of Evolution." | x |
| F120 | 6.5 | name | "Even before Darwin, a French naturalist Lamarck had said that evolution of life forms had occurred but driven by use and disuse of organs." | x |
| F121 | 6.5 | example | Lamarck's giraffe example: giraffes "in an attempt to forage leaves on tall trees, had to adapt by elongation of their necks. As they passed on this acquired character of elongated neck to succeeding generations, giraffes, slowly, over the years, came to acquire long necks. Nobody believes this conjecture any more." | x |
| F122 | 6.5 | concept | "Is evolution a process or the result of a process? The world we see, inanimate and animate, is only the success stories of evolution." | x |
| F123 | 6.5 | concept | Describing the world = evolution as a process; describing life on earth = evolution as "a consequence of a process called natural selection." "We are still not very clear whether to regard evolution and natural selection as processes or end result of unknown processes." | x |
| F124 | 6.5 | name | "It is possible that the work of Thomas Malthus on populations influenced Darwin." | x |
| F125 | 6.5 | concept | Natural selection based on factual observations: "natural resources are limited, populations are stable in size except for seasonal fluctuation, members of a population vary in characteristics - in fact no two individuals are alike - even though they look superficially similar, and most variations are inherited." | x |
| F126 | 6.5 | concept | "population size will grow exponentially if everybody reproduced maximally"; real population sizes are limited "means that there had been competition for resources. Only some survived and grew at the cost of others that could not flourish." | x |
| F127 | 6.5 | concept | Darwin's insight: "variations which are heritable and which make resource utilisation better for few, adapted to habitat better, will enable only those to reproduce and leave more progeny." Over many generations "survivors will leave more progeny and there would be a change in population characteristic and hence new forms appear to arise." | x |
| F128 | 6.5 | caption | Figure 6.8 (omitted, figureless edition). Caption: "Diagrammatic representation of the operation of natural selection on different traits: (a) Stabilising (b) Directional and (c) Disruptive." | x |
| F129 | Fig 6.8 | figure-label | Figure labels: "Number of individuals with phenotype"; "Phenotypes favoured by natural selection"; "Medium-sized individuals are favoured"; "Peak gets higher and narrower"; "Peak shifts in one direction"; "Two peaks form" | x |
| F130 | 6.6 | heading | "6.6 Mechanism of Evolution" | x |
| F131 | 6.6 | opener | "What is the origin of this variation and how does speciation occur?" | x |
| F132 | 6.6 | concept | "Even though Mendel had talked of inheritable factors influencing phenotype, Darwin either ignored these observations or kept silence." | x |
| F133 | 6.6 | name | "In the first decade of twentieth century, Hugo de Vries, based on his work on evening primrose, brought forth the idea of mutations - large difference arising suddenly in a population." | x |
| F134 | 6.6 | concept | "He believed that it is mutation which causes evolution and not the minor variations, heritable, that Darwin talked about." | x |
| F135 | 6.6 | comparison | "Mutations are random and directionless while Darwinian variations are small and directional." | x |
| F136 | 6.6 | definition | "Evolution for Darwin was gradual while de Vries believed mutation caused speciation and hence called it saltation, or single-step large mutation." | x |
| F137 | 6.6 | concept | "Studies in population genetics, later, brought out some clarity." | x |
| F138 | 6.7 | heading | "6.7 Hardy-Weinberg Principle" | x |
| F139 | 6.7 | opener | "In a given population one can find out the frequency of occurrence of alleles of a gene or a locus." | x |
| F140 | 6.7 | concept | "This frequency is supposed to remain fixed and even remain the same through generations. Hardy-Weinberg principle stated it using algebraic equations." | x |
| F141 | 6.7 | definition | "allele frequencies in a population are stable and are constant from generation to generation." | x |
| F142 | 6.7 | definition | "The gene pool, the total genes and their alleles in a population, remains a constant. This is called genetic equilibrium." | x |
| F143 | 6.7 | concept | "Sum total of all the allelic frequencies is 1. Individual frequencies, for example, can be named p, q, etc." | x |
| F144 | 6.7 | definition | "In a diploid, p and q represent the frequency of allele A and allele a." | x |
| F145 | 6.7 | concept | "The frequency of AA individuals in a population is simply p^2" (probability allele A of frequency p on both chromosomes = p x p = p^2); "the frequency of aa is q^2, and that of Aa is 2pq." | x |
| F146 | 6.7 | equation | "p^2 + 2pq + q^2 = 1" | x |
| F147 | 6.7 | concept | "This is a binomial expansion of (p + q)^2." | x |
| F148 | 6.7 | concept | "When frequency measured differs from expected values, the difference, or direction, indicates the extent of evolutionary change." Disturbance in genetic (Hardy-Weinberg) equilibrium, i.e., change of allele frequency, "would then be interpreted as resulting in evolution." | x |
| F149 | 6.7 | list | "Five factors are known to affect Hardy-Weinberg equilibrium. These are gene migration or gene flow, genetic drift, mutation, genetic recombination and natural selection." | x |
| F150 | 6.7 | process | "When migration of a section of population to another place and population occurs, gene frequencies change in the original as well as in the new population. New genes or alleles are added to the new population and these are lost from the old population." | x |
| F151 | 6.7 | definition | "There would be a gene flow if this gene migration happens multiple times." | x |
| F152 | 6.7 | definition | "If the same change occurs by chance, it is called genetic drift." | x |
| F153 | 6.7 | definition | "Sometimes the change in allele frequency is so different in the new sample of population that they become a different species. The original drifted population becomes founders and the effect is called founder effect." | x |
| F154 | 6.7 | concept | "Microbial experiments show that pre-existing advantageous mutations when selected will result in observation of new phenotypes. Over few generations, this would result in speciation." | x |
| F155 | 6.7 | definition | "Natural selection is a process in which heritable variations enabling better survival are enabled to reproduce and leave greater number of progeny." | x |
| F156 | 6.7 | concept | "variation due to mutation or variation due to recombination during gametogenesis, or due to gene flow or genetic drift, results in changed frequency of genes and alleles in future generation. Coupled to enhanced reproductive success, natural selection makes it look like different population." | x |
| F157 | 6.7 | definition | "Natural selection can lead to stabilisation, in which more individuals acquire mean character value; directional change, in which more individuals acquire value other than the mean character value; or disruption, in which more individuals acquire peripheral character value at both ends of the distribution curve." | x |
| F158 | 6.8 | heading | "6.8 A Brief Account of Evolution" | x |
| F159 | 6.8 | opener | "About 2000 million years ago, or mya, the first cellular forms of life appeared on earth." | x |
| F160 | 6.8 | concept | "The mechanism of how non-cellular aggregates of giant macromolecules could evolve into cells with membranous envelop is not known." | x |
| F161 | 6.8 | concept | "Some of these cells had the ability to release O2. The reaction could have been similar to the light reaction in photosynthesis where water is split with the help of solar energy captured and channelised by appropriate light harvesting pigments." | x |
| F162 | 6.8 | number | "Slowly single-celled organisms became multi-cellular life forms. By the time of 500 mya, invertebrates were formed and active." | x |
| F163 | 6.8 | number | "Jawless fish probably evolved around 350 mya." | x |
| F164 | 6.8 | number | "Sea weeds and few plants existed probably around 320 mya." | x |
| F165 | 6.8 | concept | "the first organisms that invaded land were plants. They were widespread on land when animals invaded land." | x |
| F166 | 6.8 | number | "Fish with stout and strong fins could move on land and go back to water. This was about 350 mya." | x |
| F167 | 6.8 | number | "In 1938, a fish caught in South Africa happened to be a Coelacanth which was thought to be extinct." | x |
| F168 | 6.8 | concept | "These animals called lobefins evolved into first amphibians that lived on both land and water. There are no specimens of these left with us. However, these were ancestors of modern day frogs and salamanders." | x |
| F169 | 6.8 | concept | "The amphibians evolved into reptiles. They lay thick-shelled eggs which do not dry up in sun unlike those of amphibians." Modern descendents: "the turtles, tortoises and crocodiles." | x |
| F170 | 6.8 | caption | Figure 6.9 (omitted, figureless edition). Caption: "A sketch of the evolution of plant forms through geological periods." | x |
| F171 | Fig 6.9 | figure-label | Figure labels: "Cenozoic"; "Mesozoic"; "Paleozoic"; "Quaternary"; "Tertiary"; "Cretaceous"; "Jurassic"; "Triassic"; "Permian"; "Carboniferous"; "Devonian"; "Silurian"; "Bryophytes"; "Sphenopsids (horsetails)"; "Ginkgos"; "Gnetales"; "Angiosperms (flowering plants)"; "Monocotyledons"; "Dicotyledons"; "herbaceous lycopods"; "Ferns"; "Conifers"; "Cycads"; "arborescent lycopods"; "seed ferns"; "Progymnosperms"; "Psilophyton"; "Zosterophyllum"; "Rhynia-type plants"; "tracheophyte ancestors"; "chlorophyte ancestors" | x |
| F172 | 6.8 | number | "In the next 200 million years or so, reptiles of different shapes and sizes dominated on earth." | x |
| F173 | 6.8 | concept | "Giant ferns, pteridophytes, were present but they all fell to form coal deposits slowly." | x |
| F174 | 6.8 | number | "Some of these land reptiles went back into water to evolve into fish-like reptiles probably 200 mya, for example Ichthyosaurs." | x |
| F175 | 6.8 | concept | "The land reptiles were, of course, the dinosaurs." | x |
| F176 | 6.8 | number | "the biggest of them, i.e., Tyrannosaurus rex was about 20 feet in height and had huge fearsome dagger-like teeth." | x |
| F177 | 6.8 | number | "About 65 mya, the dinosaurs suddenly disappeared from the earth. We do not know the true reason." Some say climatic changes killed them, some say most evolved into birds; "The truth may lie in between. Small-sized reptiles of that era still exist today." | x |
| F178 | 6.8 | caption | Figure 6.10 (omitted, figureless edition). Caption: "Representative evolutionary history of vertebrates through geological periods." | x |
| F179 | Fig 6.10 | figure-label | Figure labels: "Turtles"; "Lizards"; "Snakes"; "Tuataras"; "Crocodiles"; "Birds"; "Mammals"; "Sauropsids"; "Synapsids"; "Dinosaurs (extinct)"; "Therapsids (extinct)"; "Thecodonts (extinct)"; "Pelycosaurs (extinct)"; "Early reptiles (extinct)"; "Quaternary"; "Tertiary"; "Cretaceous"; "Jurassic"; "Triassic"; "Permian"; "Carboniferous" | x |
| F180 | 6.8 | concept | "The first mammals were like shrews. Their fossils are small sized. Mammals were viviparous and protected their unborn young inside the mother's body. Mammals were more intelligent in sensing and avoiding danger at least. When reptiles came down mammals took over this earth." | x |
| F181 | 6.8 | example | "There were in South America mammals resembling horse, hippopotamus, bear, rabbit, etc. Due to continental drift, when South America joined North America, these animals were overridden by North American fauna." | x |
| F182 | 6.8 | concept | "Due to the same continental drift pouched mammals of Australia survived because of lack of competition from any other mammal." | x |
| F183 | 6.8 | example | "some mammals live wholly in water. Whales, dolphins, seals and sea cows are some examples." | x |
| F184 | 6.8 | concept | "Evolution of horse, elephant, dog, etc., are special stories of evolution." "The most successful story is the evolution of man with language skills and self-consciousness." | x |
| F185 | 6.8 | concept | "A rough sketch of the evolution of life forms, their times on a geological scale are indicated in Figures 6.9 and 6.10." | x |
| F186 | 6.9 | heading | "6.9 Origin and Evolution of Man" | x |
| F187 | 6.9 | opener | "About 15 mya, primates called Dryopithecus and Ramapithecus were existing. They were hairy and walked like gorillas and chimpanzees." (Dryopithecus and Ramapithecus in italics) | x |
| F188 | 6.9 | comparison | "Ramapithecus was more man-like while Dryopithecus was more ape-like." | x |
| F189 | 6.9 | number | "Few fossils of man-like bones have been discovered in Ethiopia and Tanzania." Revealed hominid features; "about 3-4 mya, man-like primates walked in eastern Africa. They were probably not taller than 4 feet but walked upright." | x |
| F190 | 6.9 | number | "Two mya, Australopithecines probably lived in East African grasslands. Evidence shows they hunted with stone weapons but essentially ate fruit." | x |
| F191 | 6.9 | number | "This creature was called the first human-like being, the hominid, and was called Homo habilis. The brain capacities were between 650-800 cc. They probably did not eat meat." | x |
| F192 | 6.9 | number | "Fossils discovered in Java in 1891 revealed the next stage, i.e., Homo erectus about 1.5 mya. Homo erectus had a large brain around 900 cc. Homo erectus probably ate meat." | x |
| F193 | 6.9 | number | "The Neanderthal man with a brain size of 1400 cc lived in Near East and central Asia between 100,000-40,000 years back. They used hides to protect their body and buried their dead." | x |
| F194 | 6.9 | number | "Homo sapiens arose in Africa and moved across continents and developed into distinct races. During ice age between 75,000-10,000 years ago modern Homo sapiens arose." | x |
| F195 | 6.9 | caption | Figure 6.11 (omitted, figureless edition). Caption: "A comparison of the skulls of adult modern human being, baby chimpanzee and adult chimpanzee. The skull of baby chimpanzee is more like adult human skull than adult chimpanzee skull." (no discrete textual labels) | x |
| F196 | 6.9 | number | "Pre-historic cave art developed about 18,000 years ago. One such cave painting by pre-historic humans can be seen at Bhimbetka rock shelter in Raisen district of Madhya Pradesh." | x |
| F197 | 6.9 | number | "Agriculture came around 10,000 years back and human settlements started. The rest of what happened is part of human history of growth and decline of civilisations." | x |
| F198 | 6.7 | concept | **SUMMARY-UNIQUE, folded from summary sentence S6.** "Other phenomena like habitat fragmentation and genetic drift may accentuate these variations leading to appearance of new species and hence evolution." — the term *habitat fragmentation* is never stated in the body; folded here beside the §6.7 discussion of genetic drift so Pass 2 carries it as an explicit body fact. | x |

## Figure-label matrix

The v6-mandatory figure-label matrix lives in **exactly one place — the Facts table above**, as the 8 rows whose wording begins `Figure labels:` (**F034, F061, F076, F105, F109, F129, F171, F179**), carrying **116** label strings total. It is deliberately **not** restated as a second pipe-delimited table (a duplicate would double every label under `_extract_labels` and turn its separator into a phantom `Fig #` figure). Figures 6.4, 6.5 and 6.11 carry no discrete textual labels and so have a `caption` row only. Because this is a **figureless edition**, every one of these 116 labels must be carried in Pass 2 running text (check 6) since no artwork exists to display them.

## Summary classification

Two paragraphs, **9 sentences**. BODY-PRESENT = fact already explicit in the body (belongs in the rewritten Quick Recap). SUMMARY-UNIQUE = not explicit anywhere in the body (must be folded into a body row).

| # | Summary sentence | Classification | Folded into / Recap source |
|---|---|---|---|
| S1 | "The origin of life on earth can be understood only against the background of origin of universe especially earth." | BODY-PRESENT | F003, F007 |
| S2 | "Most scientists believe chemical evolution, i.e., formation of biomolecules preceded the appearance of the first cellular forms of life." | BODY-PRESENT | F026, F027, F032, F038 |
| S3 | "The subsequent events as to what happened to the first form of life is a conjectured story based on Darwinian ideas of organic evolution by natural selection." | BODY-PRESENT | F048, F112, F119 |
| S4 | "Diversity of life forms on earth has been changing over millions of years." | BODY-PRESENT | F003, F044 |
| S5 | "It is generally believed that variations in a population result in variable fitness." | BODY-PRESENT | F045, F046, F047, F116 |
| S6 | "Other phenomena like habitat fragmentation and genetic drift may accentuate these variations leading to appearance of new species and hence evolution." | **SUMMARY-UNIQUE** | **F198** (term *habitat fragmentation* absent from body; genetic drift itself is body-present at F152) |
| S7 | "Homology is accounted for by the idea of branching descent." | BODY-PRESENT | F071, F119 |
| S8 | "Study of comparative anatomy, fossils and comparative biochemistry provides evidence for evolution." | BODY-PRESENT | F058, F067, F082 |
| S9 | "Among the stories of evolution of individual species, the story of evolution of modern man is most interesting and appears to parallel evolution of human brain and language." | BODY-PRESENT | F184, F191–F194 |

**Arithmetic:** 9 summary sentences — 8 BODY-PRESENT, 1 SUMMARY-UNIQUE (folded to F198), 0 overlooked.

## Exercise-gap terms

Every exercise classified (Rule 2). COVERED = the rewritten body already answers it (question not reproduced, no answer written). GAP = the chapter never states what the question assumes (reproduced + answered in the closing appendix). Several exercises are open research/drawing activities that assume no unexplained term — classified COVERED (no factual gap).

| # | Exercise (abbrev.) | Class | Answering section / note |
|---|---|---|---|
| 1 | Explain antibiotic resistance in light of Darwinian selection | COVERED | §6.3 — F093, F094, F095 |
| 2 | Find new fossil discoveries/controversies from newspapers | COVERED | open research activity; assumes no unexplained term |
| 3 | Give a clear definition of the term *species* | **GAP** | chapter uses *species* throughout but never defines it → appendix "Terms used in the exercises" |
| 4 | Trace components of human evolution (brain size, skeleton, diet) | COVERED | §6.9 — F187–F194, F196, F197 |
| 5 | Find whether animals other than man have self-consciousness | COVERED | open research activity; body states man has self-consciousness (F184) |
| 6 | List 10 modern animals and link to ancient fossils | COVERED | open internet activity; assumes no unexplained term |
| 7 | Practise drawing various animals and plants | COVERED | drawing activity; no factual gap |
| 8 | Describe one example of adaptive radiation | COVERED | §6.4 — F096–F103 (Darwin's finches, Australian marsupials) |
| 9 | Can we call human evolution as adaptive radiation? | COVERED | §6.4 — adaptive-radiation definition F101 supplies the reasoning basis |
| 10 | Trace evolutionary stages of one animal (e.g. horse) | COVERED | open library/internet activity; body flags horse evolution as a special story (F184) |

**Arithmetic:** 10 exercises, 1 answered by design (GAP), 9 unanswered by design (COVERED), 0 overlooked.

## Figure manifest

**Figureless edition (operator order).** All 11 figures are deliberately omitted; no asset files are extracted or embedded. Each figure's caption is preserved as a `caption` Facts row and each figure's in-figure textual labels as a `figure-label` Facts row, so no figure fact is lost. `Mono`/`Verified` are **N/A** because nothing is embedded.

| Fig # | Caption (verbatim) | Asset file | Source page | Mono | Verified |
|---|---|---|---|---|---|
| Fig 6.1 | Diagrammatic representation of Miller's experiment. | none — omitted (figureless) | §6.1 | N/A | N/A |
| Fig 6.2 | A family tree of dinosaurs and their living modern day counterpart organisms like crocodiles and birds. | none — omitted (figureless) | §6.3 | N/A | N/A |
| Fig 6.3 | Example of homologous organs in (a) Plants and (b) Animals. | none — omitted (figureless) | §6.3 | N/A | N/A |
| Fig 6.4 | Figure showing white-winged moth and dark-winged moth (melanised) on a tree trunk (a) In unpolluted area (b) In polluted area. | none — omitted (figureless) | §6.3 | N/A | N/A |
| Fig 6.5 | Variety of beaks of finches that Darwin found in Galapagos Island. | none — omitted (figureless) | §6.4 | N/A | N/A |
| Fig 6.6 | Adaptive radiation of marsupials of Australia. | none — omitted (figureless) | §6.4 | N/A | N/A |
| Fig 6.7 | Picture showing convergent evolution of Australian marsupials and placental mammals. | none — omitted (figureless) | §6.4 | N/A | N/A |
| Fig 6.8 | Diagrammatic representation of the operation of natural selection on different traits: (a) Stabilising (b) Directional and (c) Disruptive. | none — omitted (figureless) | §6.5 | N/A | N/A |
| Fig 6.9 | A sketch of the evolution of plant forms through geological periods. | none — omitted (figureless) | §6.8 | N/A | N/A |
| Fig 6.10 | Representative evolutionary history of vertebrates through geological periods. | none — omitted (figureless) | §6.8 | N/A | N/A |
| Fig 6.11 | A comparison of the skulls of adult modern human being, baby chimpanzee and adult chimpanzee. The skull of baby chimpanzee is more like adult human skull than adult chimpanzee skull. | none — omitted (figureless) | §6.9 | N/A | N/A |

## Carry-overs for Pass 2

1. **Figureless prose burden (check 6):** all 116 in-figure labels must be carried in the Pass 2 running text because no artwork is shown. Some Fig 6.1 apparatus labels (e.g. "To vacuum pump", "Condenser", "Water out/in") are diagram-mechanical — carry them in a short prose description of Miller's apparatus so check 6 finds them, rather than forcing an awkward inline mention.
2. **GAP appendix:** add the "Terms used in the exercises" appendix with a clear definition of *species* (exercise 3), labelled as an addition (Rule 5). Zero other gaps → this is the only appendix entry.
3. **SUMMARY-UNIQUE fold (F198):** ensure *habitat fragmentation* appears as an explicit body sentence in §6.7 (beside genetic drift), not merely implied.
4. **Qualifier words to preserve verbatim (Rule 4):** "accepted by majority" (F039, not "most"); "may lie in between" (F177); "probably"/"about"/"around" on every §6.8/§6.9 date; "not directed … stochastic" (F095); "unlike those of amphibians" (F169). Do not smooth any of these.
5. **Italics:** Dryopithecus, Ramapithecus, Homo habilis, Homo erectus, Homo sapiens, Tyrannosaurus rex, Coelacanth, Ichthyosaurs, Bougainvillea, Cucurbita — preserve scientific-name styling in the PDF.

---

## Gate 2 — CLOSED (2026-09-26)

Built `Ch6_Evolution.py` linearly from the frozen Facts rows and rendered `Ch6_Evolution.pdf` (5 A4 pages, figureless by operator order). All 198 Facts rows are ticked; `check_pdf.py` exits **0**: 0 FAIL, 2 WARN. Check 3 warns because this edition deliberately embeds no figures (confirmed 0 embedded images). Check 4 matches `photo` inside `photosynthesis` in F161, not a portrait; the inventory contains no scientist photograph and the PDF contains no images. Both warnings were reviewed and are benign for the explicitly figureless edition. Check 6 finds 116/116 labels in the text; the remaining checks pass. The template smoke test imported the shared canon, rendered a clipped monochrome NCERT figure with `convert("L")` + `autocontrast`, displayed the colour and greyscale one-page outputs, and exercised the linter end-to-end. Pass 3 verification has **not** been performed.
