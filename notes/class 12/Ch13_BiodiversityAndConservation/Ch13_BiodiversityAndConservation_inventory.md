# Frozen Inventory — Biodiversity and Conservation (Class 12, Chapter 13)
Source: `Chapter/class 12/Chapter 13 - Biodiversity and Conservation.pdf` (13 pp; p13 is a blank `NOTES` page) | Frozen: 2026-08-21 | Rows: **189** (`F001`..`F189`)

Tick legend: `x` = written into the script and verified present in the generated PDF. **All 189 rows are now ticked** — Pass 2 is complete, and `check_pdf.py` check 7 reports "All 189 Facts rows ticked." No Facts row wording was altered when ticking; only the `Ticked` column changed.

## Header counts — all machine-derived (§6 Pass 1 step 8), never hand-tallied

| Count | Value |
|---|---|
| Facts rows total | 189 |
| ID range / contiguity | F001..F189 — 0 gaps, 0 duplicates |
| `Type: heading` rows | 21 |
| `Type: opener` rows | 8 |
| Figure-label rows | 2 (F039, F081) |
| Label strings parsed by `_extract_labels` | 23 (18 + 5) — no doubling, no phantom figure |
| Summary sentences classified | 25 — BODY-PRESENT 19, SUMMARY-UNIQUE 6 |
| Exercise questions scanned | 10 — gaps found: 4 |
| Figures in manifest | 2, both `Mono: yes` / `Verified: yes` |

> ## GATE 1 STATUS: **GREEN — CLOSED. Pass 2 may begin.**
>
> | Gate 1 requirement (§6) | State |
> |---|---|
> | Environment (§0.2–0.3) re-established | done — venv `/vercel/share/neetenv`, CPython 3.13.11, reportlab 5.0.1 · pdfplumber OK · pymupdf 1.28.2 · Pillow 12.3.0 |
> | Every fact has a Facts row (three source reads) | done — 189 rows |
> | Every in-figure label has a matrix row, harvested by opening each rendered asset | done — 23 labels; both assets re-opened and re-read this session |
> | Inventory validated by running `check_pdf.py`'s own `_extract_labels` | done — 2 figures, 23 labels, no doubling, no `Fig #` phantom row |
> | Header counts match a re-parse of the table; IDs contiguous | done — see the count table above |
> | Every heading has a row, incl. unnumbered sub-headings (step 3a) | done — 21 heading rows, walked as their own list |
> | Every section's opening sentence has a row (step 3b) | done — 8 opener rows |
> | Every figure `Mono: yes` and `Verified: yes` | done — 2/2 |
> | Every exercise-gap term has a planned home | done — 4 gaps, each with a named destination |
> | Every SUMMARY-UNIQUE fact folded into a body row | done — 6 folded, F179–F184 |
> | Inventory file saved to the chapter folder | done — this file |
>
> **The provisional `FIG-1`/`FIG-2` table from the previous session has been actioned and deleted.** Both label rows now live in the Facts table as `F039` and `F081` with real contiguous IDs, and the matrix exists in **exactly one place** in this file. Do not restate it anywhere else as pipe-delimited rows — a second copy doubles every label and turns the markdown separator into a phantom figure.

> ## GATE 2 STATUS: **GREEN — CLOSED (2026-08-22). Pass 3 may begin.**
>
> Built with `Ch13_BiodiversityAndConservation.py` (imports the repo-level frozen `neet_template.py`; no style, geometry, colour or font re-declared) into `Ch13_BiodiversityAndConservation.pdf` — **11 pages**, 34,117 extracted characters, 2 embedded images.
>
> Final `check_pdf.py` run against the final rebuilt PDF: **0 FAIL, 1 WARN — exit 0.**
>
> | check | verdict |
> |---|---|
> | 1. Footer/header band | PASS — no text in the top/bottom 1.4 cm bands |
> | 2. Legibility floor | PASS — smallest rendered text 6.0pt (FAIL floor 5.0, WARN band <6.0) |
> | 3. Grayscale-only images | PASS — both embedded images monochrome |
> | 4. No person photograph | **WARN, accepted** — see justification below |
> | 5. Banned glyphs | PASS — no Unicode arrows, sub/superscripts, Greek or emoji |
> | 6. Figure-label coverage | PASS — **23/23** labels in running text, 0 partial, 0 missing |
> | 7. Inventory fully ticked | PASS — all 189 Facts rows ticked |
> | 8. Page geometry | PASS — 11/11 pages A4 portrait |
> | 9. Orphaned headings | PASS — 54 banner headings, none stranded |
> | 10. Badge/banner collision | PASS — 82 plates, none colliding |
>
> **The single WARN is a confirmed false positive, eyeballed per §6 Gate 2.** Check 4 keys off the word "photo" and matched row **F143** — *"The fast-dwindling Amazon forest is estimated to produce, through **photo**synthesis, 20 per cent of the total oxygen…"*. That row is a number fact, not a portrait row. The figure census (below) established this chapter contains **no photograph of any kind and no scientist portrait**, there is no "Do You Know?" box, and check 3 confirms the PDF embeds exactly **2** images — `fig_13_1.png` and `fig_13_2.png`, both monochrome clip renders. Nothing was suppressed; check 4 has no real portrait row to act on here.
>
> **Carry-overs actioned in Pass 2** (all seven from "Carry-overs Pass 2 must action"): Fig 13.2's caption names which plot is the arithmetic-scale hyperbola and which is the log-log line (1); `S = CA<super>Z</super>` is written into the running text and extracts as `S = CAZ`, matching F081 unchanged (2); `log S = log C + Z log A` is written verbatim in 13.1.2 (ii) (3); all degrees stayed spelled out (4); F037's four-class form and F181's all-vertebrates form are carried together in one NOTE (5); 448 sanctuaries is the body figure with the summary's "more than 450" in a NOTE (6); the `Type`-column casing was left untouched (7).
>
> **Gate 2 is not Gate 3.** Pass 3 — the every-page visual render and the bidirectional full-read content cross-check — has **not** been done, so this chapter is **not** Done and must not be counted as closed.

---

## Facts

| ID | Section | Type | Exact original wording | Ticked |
|----|---------|------|------------------------|--------|
| F001 | front | heading | "CHAPTER 13 — BIODIVERSITY AND CONSERVATION", with the contents list "13.1 Biodiversity" and "13.2 Biodiversity Conservation" | x |
| F002 | 13-open | opener | "If an alien from a distant galaxy were to visit our planet Earth, the first thing that would amaze and baffle him would most probably be the enormous diversity of life that he would encounter." | x |
| F003 | 13-open | concept | "Even for humans, the rich variety of living organisms with which they share this planet never ceases to astonish and fascinate us." | x |
| F004 | 13-open | number | "there are more than 20,000 species of ants" | x |
| F005 | 13-open | number | "3,00,000 species of beetles" | x |
| F006 | 13-open | number | "28,000 species of fishes" | x |
| F007 | 13-open | number | "nearly 20,000 species of orchids" | x |
| F008 | 13-open | questions | The six framing questions asked by "Ecologists and evolutionary biologists": "Why are there so many species?"; "Did such great diversity exist throughout earth's history?"; "How did this diversification come about?"; "How and why is this diversity important to the biosphere?"; "Would it function any differently if the diversity was much less?"; "How do humans benefit from the diversity of life?" | x |
| F009 | 13.1 | heading | "13.1 BIODIVERSITY" | x |
| F010 | 13.1 | opener | "In our biosphere immense diversity (or heterogeneity) exists not only at the species level but at all levels of biological organisation ranging from macromolecules within cells to biomes." | x |
| F011 | 13.1 | definition | "Biodiversity is the term popularised by the sociobiologist Edward Wilson to describe the combined diversity at all the levels of biological organisation." | x |
| F012 | 13.1 | list | "The most important of them are–", introducing the three levels: genetic, species and ecological diversity | x |
| F013 | 13.1 | heading | "(i) Genetic diversity:" | x |
| F014 | 13.1 | definition | "A single species might show high diversity at the genetic level over its distributional range." | x |
| F015 | 13.1 | example | "The genetic variation shown by the medicinal plant Rauwolfia vomitoria growing in different Himalayan ranges might be in terms of the potency and concentration of the active chemical (reserpine) that the plant produces." | x |
| F016 | 13.1 | number | "India has more than 50,000 genetically different strains of rice" | x |
| F017 | 13.1 | number | "and 1,000 varieties of mango" | x |
| F018 | 13.1 | heading | "(ii) Species diversity:" | x |
| F019 | 13.1 | example | "The diversity at the species level, for example, the Western Ghats have a greater amphibian species diversity than the Eastern Ghats." | x |
| F020 | 13.1 | heading | "(iii) Ecological diversity:" | x |
| F021 | 13.1 | example | "At the ecosystem level, India, for instance, with its deserts, rain forests, mangroves, coral reefs, wetlands, estuaries, and alpine meadows has a greater ecosystem diversity than a Scandinavian country like Norway." | x |
| F022 | 13.1 | concept | "It has taken millions of years of evolution, to accumulate this rich diversity in nature, but we could lose all that wealth in less than two centuries if the present rates of species losses continue." | x |
| F023 | 13.1 | concept | "Biodiversity and its conservation are now vital environmental issues of international concern as more and more people around the world begin to realise the critical importance of biodiversity for our survival and well-being on this planet." | x |
| F024 | 13.1.1 | heading | "13.1.1 How Many Species are there on Earth and How Many in India?" | x |
| F025 | 13.1.1 | opener | "Since there are published records of all the species discovered and named, we know how many species in all have been recorded so far, but it is not easy to answer the question of how many species there are on earth." | x |
| F026 | 13.1.1 | definition | "International Union for Conservation of Nature and Natural Resources (IUCN)" — the full expansion of the acronym | x |
| F027 | 13.1.1 | number | "According to the IUCN (2004), the total number of plant and animal species described so far is slightly more than 1.5 million" | x |
| F028 | 13.1.1 | concept | "but we have no clear idea of how many species are yet to be discovered and described. Estimates vary widely and many of them are only educated guesses." | x |
| F029 | 13.1.1 | concept | "For many taxonomic groups, species inventories are more complete in temperate than in tropical countries." | x |
| F030 | 13.1.1 | process | "Considering that an overwhelmingly large proportion of the species waiting to be discovered are in the tropics, biologists make a statistical comparison of the temperate-tropical species richness of an exhaustively studied group of insects and extrapolate this ratio to other groups of animals and plants to come up with a gross estimate of the total number of species on earth." | x |
| F031 | 13.1.1 | number | "Some extreme estimates range from 20 to 50 million" | x |
| F032 | 13.1.1 | number | "a more conservative and scientifically sound estimate made by Robert May places the global species diversity at about 7 million" | x |
| F033 | 13.1.1 | number | "More than 70 per cent of all the species recorded are animals" | x |
| F034 | 13.1.1 | number | "while plants (including algae, fungi, bryophytes, gymnosperms and angiosperms) comprise no more than 22 per cent of the total" | x |
| F035 | 13.1.1 | number | "Among animals, insects are the most species-rich taxonomic group, making up more than 70 per cent of the total." | x |
| F036 | 13.1.1 | number | "That means, out of every 10 animals on this planet, 7 are insects." | x |
| F037 | 13.1.1 | concept | "The number of fungi species in the world is more than the combined total of the species of fishes, amphibians, reptiles and mammals." | x |
| F038 | 13.1.1 | caption | "Figure 13.1 Representing global biodiversity: proportionate number of species of major taxa of plants, invertebrates and vertebrates", plus the in-text pointer "In Figure 13.1, biodiversity is depicted showing species number of major taxa." | x |
| F039 | Fig 13.1 | Caption | Figure labels: "Invertebrates"; "Other animal groups"; "Crustaceans"; "Molluscs"; "Insects"; "Vertebrates"; "Fishes"; "Mammals"; "Birds"; "Reptiles"; "Amphibians"; "Plants"; "Mosses"; "Ferns and allies"; "Fungi"; "Angiosperms"; "Algae"; "Lichens" | x |
| F040 | 13.1.1 | concept | "It should be noted that these estimates do not give any figures for prokaryotes." | x |
| F041 | 13.1.1 | concept | "Biologists are not sure about how many prokaryotic species there might be. The problem is that conventional taxonomic methods are not suitable for identifying microbial species and many species are simply not culturable under laboratory conditions." | x |
| F042 | 13.1.1 | concept | "If we accept biochemical or molecular criteria for delineating species for this group, then their diversity alone might run into millions." | x |
| F043 | 13.1.1 | number | "Although India has only 2.4 per cent of the world's land area" | x |
| F044 | 13.1.1 | number | "its share of the global species diversity is an impressive 8.1 per cent" | x |
| F045 | 13.1.1 | number | "That is what makes our country one of the 12 mega diversity countries of the world." | x |
| F046 | 13.1.1 | number | "Nearly 45,000 species of plants and twice as many of animals have been recorded from India." | x |
| F047 | 13.1.1 | number | "If we accept May's global estimates, only 22 per cent of the total species have been recorded so far." | x |
| F048 | 13.1.1 | number | "Applying this proportion to India's diversity figures, we estimate that there are probably more than 1,00,000 plant species and more than 3,00,000 animal species yet to be discovered and described." | x |
| F049 | 13.1.1 | concept | "Consider the immense trained manpower (taxonomists) and the time required to complete the job." | x |
| F050 | 13.1.1 | concept | "The situation appears more hopeless when we realise that a large fraction of these species faces the threat of becoming extinct even before we discover them." | x |
| F051 | 13.1.1 | concept | "Nature's biological library is burning even before we catalogued the titles of all the books stocked there." | x |
| F052 | 13.1.2 | heading | "13.1.2 Patterns of Biodiversity" | x |
| F053 | 13.1.2 | heading | "(i) Latitudinal gradients:" | x |
| F054 | 13.1.2 | opener | "The diversity of plants and animals is not uniform throughout the world but shows a rather uneven distribution." | x |
| F055 | 13.1.2 | concept | "For many group of animals or plants, there are interesting patterns in diversity, the most well-known being the latitudinal gradient in diversity." | x |
| F056 | 13.1.2 | concept | "In general, species diversity decreases as we move away from the equator towards the poles." | x |
| F057 | 13.1.2 | number | "With very few exceptions, tropics (latitudinal range of 23.5 degrees N to 23.5 degrees S) harbour more species than temperate or polar areas." | x |
| F058 | 13.1.2 | number | "Colombia located near the equator has nearly 1,400 species of birds" | x |
| F059 | 13.1.2 | number | "while New York at 41 degrees N has 105 species" | x |
| F060 | 13.1.2 | number | "and Greenland at 71 degrees N only 56 species" | x |
| F061 | 13.1.2 | number | "India, with much of its land area in the tropical latitudes, has more than 1,200 species of birds." | x |
| F062 | 13.1.2 | number | "A forest in a tropical region like Equador has up to 10 times as many species of vascular plants as a forest of equal area in a temperate region like the Midwest of the USA." | x |
| F063 | 13.1.2 | concept | "The largely tropical Amazonian rain forest in South America has the greatest biodiversity on earth" | x |
| F064 | 13.1.2 | number | The Amazon inventory: "more than 40,000 species of plants, 3,000 of fishes, 1,300 of birds, 427 of mammals, 427 of amphibians, 378 of reptiles and of more than 1,25,000 invertebrates" | x |
| F065 | 13.1.2 | number | "Scientists estimate that in these rain forests there might be at least two million insect species waiting to be discovered and named." | x |
| F066 | 13.1.2 | concept | Hypothesis (a): "Speciation is generally a function of time, unlike temperate regions subjected to frequent glaciations in the past, tropical latitudes have remained relatively undisturbed for millions of years and thus, had a long evolutionary time for species diversification" | x |
| F067 | 13.1.2 | concept | Hypothesis (b): "Tropical environments, unlike temperate ones, are less seasonal, relatively more constant and predictable. Such constant environments promote niche specialisation and lead to a greater species diversity" | x |
| F068 | 13.1.2 | concept | Hypothesis (c): "There is more solar energy available in the tropics, which contributes to higher productivity; this in turn might contribute indirectly to greater diversity." | x |
| F069 | 13.1.2 | heading | "(ii) Species-Area relationships:" | x |
| F070 | 13.1.2 | name | "During his pioneering and extensive explorations in the wilderness of South American jungles, the great German naturalist and geographer Alexander von Humboldt observed..." | x |
| F071 | 13.1.2 | concept | "...that within a region species richness increased with increasing explored area, but only up to a limit." | x |
| F072 | 13.1.2 | concept | "In fact, the relation between species richness and area for a wide variety of taxa (angiosperm plants, birds, bats, freshwater fishes) turns out to be a rectangular hyperbola" | x |
| F073 | 13.1.2 | equation | "On a logarithmic scale, the relationship is a straight line described by the equation log S = log C + Z log A" | x |
| F074 | 13.1.2 | definition | "where S = Species richness; A = Area; Z = slope of the line (regression coefficient); C = Y-intercept" | x |
| F075 | 13.1.2 | number | "Ecologists have discovered that the value of Z lies in the range of 0.1 to 0.2, regardless of the taxonomic group or the region" | x |
| F076 | 13.1.2 | example | "(whether it is the plants in Britain, birds in California or molluscs in New York state, the slopes of the regression line are amazingly similar)" | x |
| F077 | 13.1.2 | number | "But, if you analyse the species-area relationships among very large areas like the entire continents, you will find that the slope of the line to be much steeper (Z values in the range of 0.6 to 1.2)." | x |
| F078 | 13.1.2 | number | "For example, for frugivorous (fruit-eating) birds and mammals in the tropical forests of different continents, the slope is found to be 1.15." | x |
| F079 | 13.1.2 | question | "What do steeper slopes mean in this context?" — posed by the book and never answered in the body; see exercise-gap Q4 | x |
| F080 | 13.1.2 | caption | "Figure 13.2 Showing species area relationship. Note that on log scale the relationship becomes linear" | x |
| F081 | Fig 13.2 | Caption | Figure labels: "Species richness"; "Area"; "S = CAZ"; "Log S = log C + Z log A"; "log-log scale" | x |
| F082 | 13.1.3 | heading | "13.1.3 The importance of Species Diversity to the Ecosystem" | x |
| F083 | 13.1.3 | opener | "Does the number of species in a community really matter to the functioning of the ecosystem?" | x |
| F084 | 13.1.3 | concept | "This is a question for which ecologists have not been able to give a definitive answer." | x |
| F085 | 13.1.3 | concept | "For many decades, ecologists believed that communities with more species, generally, tend to be more stable than those with less species." | x |
| F086 | 13.1.3 | definition | "A stable community should not show too much variation in productivity from year to year; it must be either resistant or resilient to occasional disturbances (natural or man-made), and it must also be resistant to invasions by alien species." | x |
| F087 | 13.1.3 | name | "We don't know how these attributes are linked to species richness in a community, but David Tilman's long-term ecosystem experiments using outdoor plots provide some tentative answers." | x |
| F088 | 13.1.3 | concept | "Tilman found that plots with more species showed less year-to-year variation in total biomass." | x |
| F089 | 13.1.3 | concept | "He also showed that in his experiments, increased diversity contributed to higher productivity." | x |
| F090 | 13.1.3 | concept | "rich biodiversity is not only essential for ecosystem health but imperative for the very survival of the human race on this planet" | x |
| F091 | 13.1.3 | questions | "Does it really matter to us if a few species become extinct?"; "Would Western Ghats ecosystems be less functional if one of its tree frog species is lost forever?"; "How is our quality of life affected if, say, instead of 20,000 we have only 15,000 species of ants on earth?" | x |
| F092 | 13.1.3 | name | "we can develop a proper perspective through an analogy (the 'rivet popper hypothesis') used by Stanford ecologist Paul Ehrlich" | x |
| F093 | 13.1.3 | concept | "In an airplane (ecosystem) all parts are joined together using thousands of rivets (species). If every passenger travelling in it starts popping a rivet to take home (causing a species to become extinct), it may not affect flight safety (proper functioning of the ecosystem) initially, but as more and more rivets are removed, the plane becomes dangerously weak over a period of time." | x |
| F094 | 13.1.3 | concept | "Furthermore, which rivet is removed may also be critical. Loss of rivets on the wings (key species that drive major ecosystem functions) is obviously a more serious threat to flight safety than loss of a few rivets on the seats or windows inside the plane." | x |
| F095 | 13.1.4 | heading | "13.1.4 Loss of Biodiversity" | x |
| F096 | 13.1.4 | opener | "While it is doubtful if any new species are being added (through speciation) into the earth's treasury of species, there is no doubt about their continuing losses." | x |
| F097 | 13.1.4 | concept | "The biological wealth of our planet has been declining rapidly and the accusing finger is clearly pointing to human activities." | x |
| F098 | 13.1.4 | number | "The colonisation of tropical Pacific Islands by humans is said to have led to the extinction of more than 2,000 species of native birds." | x |
| F099 | 13.1.4 | number | "The IUCN Red List (2004) documents the extinction of 784 species (including 338 vertebrates, 359 invertebrates and 87 plants) in the last 500 years." | x |
| F100 | 13.1.4 | example | "Some examples of recent extinctions include the dodo (Mauritius), quagga (Africa), thylacine (Australia), Steller's Sea Cow (Russia) and three subspecies (Bali, Javan, Caspian) of tiger." | x |
| F101 | 13.1.4 | number | "The last twenty years alone have witnessed the disappearance of 27 species." | x |
| F102 | 13.1.4 | concept | "Careful analysis of records shows that extinctions across taxa are not random; some groups like amphibians appear to be more vulnerable to extinction." | x |
| F103 | 13.1.4 | number | "more than 15,500 species world-wide are facing the threat of extinction" | x |
| F104 | 13.1.4 | number | "Presently, 12 per cent of all bird species, 23 per cent of all mammal species, 32 per cent of all amphibian species and 31 per cent of all gymnosperm species in the world face the threat of extinction." | x |
| F105 | 13.1.4 | concept | "From a study of the history of life on earth through fossil records, we learn that large-scale loss of species like the one we are currently witnessing have also happened earlier, even before humans appeared on the scene." | x |
| F106 | 13.1.4 | number | "During the long period (> 3 billion years) since the origin and diversification of life on earth there were five episodes of mass extinction of species." | x |
| F107 | 13.1.4 | concept | "How is the 'Sixth Extinction' presently in progress different from the previous episodes? The difference is in the rates" | x |
| F108 | 13.1.4 | number | "the current species extinction rates are estimated to be 100 to 1,000 times faster than in the pre-human times and our activities are responsible for the faster rates" | x |
| F109 | 13.1.4 | number | "Ecologists warn that if the present trends continue, nearly half of all the species on earth might be wiped out within the next 100 years." | x |
| F110 | 13.1.4 | list | "In general, loss of biodiversity in a region may lead to (a) decline in plant production, (b) lowered resistance to environmental perturbations such as drought and (c) increased variability in certain ecosystem processes such as plant productivity, water use, and pest and disease cycles." | x |
| F111 | 13.1.4 | heading | "Causes of biodiversity losses:" | x |
| F112 | 13.1.4 | concept | "There are four major causes ('The Evil Quartet' is the sobriquet used to describe them)." | x |
| F113 | 13.1.4 | heading | "(i) Habitat loss and fragmentation:" | x |
| F114 | 13.1.4 | concept | "This is the most important cause driving animals and plants to extinction." | x |
| F115 | 13.1.4 | number | "The most dramatic examples of habitat loss come from tropical rain forests. Once covering more than 14 per cent of the earth's land surface, these rain forests now cover no more than 6 per cent." | x |
| F116 | 13.1.4 | number | "By the time you finish reading this chapter, 1000 more hectares of rain forest would have been lost." | x |
| F117 | 13.1.4 | example | "The Amazon rain forest (it is so huge that it is called the 'lungs of the planet') harbouring probably millions of species is being cut and cleared for cultivating soya beans or for conversion to grasslands for raising beef cattle." | x |
| F118 | 13.1.4 | concept | "Besides total loss, the degradation of many habitats by pollution also threatens the survival of many species." | x |
| F119 | 13.1.4 | concept | "When large habitats are broken up into small fragments due to various human activities, mammals and birds requiring large territories and certain animals with migratory habits are badly affected, leading to population declines." | x |
| F120 | 13.1.4 | heading | "(ii) Over-exploitation:" | x |
| F121 | 13.1.4 | concept | "Humans have always depended on nature for food and shelter, but when 'need' turns to 'greed', it leads to over-exploitation of natural resources." | x |
| F122 | 13.1.4 | example | "Many species extinctions in the last 500 years (Steller's sea cow, passenger pigeon) were due to overexploitation by humans." | x |
| F123 | 13.1.4 | concept | "Presently many marine fish populations around the world are over harvested, endangering the continued existence of some commercially important species." | x |
| F124 | 13.1.4 | heading | "(iii) Alien species invasions:" | x |
| F125 | 13.1.4 | concept | "When alien species are introduced unintentionally or deliberately for whatever purpose, some of them turn invasive, and cause decline or extinction of indigenous species." | x |
| F126 | 13.1.4 | number | "The Nile perch introduced into Lake Victoria in east Africa led eventually to the extinction of an ecologically unique assemblage of more than 200 species of cichlid fish in the lake." | x |
| F127 | 13.1.4 | example | "invasive weed species like carrot grass (Parthenium), Lantana and water hyacinth (Eicchornia)" | x |
| F128 | 13.1.4 | example | "The recent illegal introduction of the African catfish Clarias gariepinus for aquaculture purposes is posing a threat to the indigenous catfishes in our rivers." | x |
| F129 | 13.1.4 | heading | "(iv) Co-extinctions:" | x |
| F130 | 13.1.4 | definition | "When a species becomes extinct, the plant and animal species associated with it in an obligatory way also become extinct." | x |
| F131 | 13.1.4 | example | "When a host fish species becomes extinct, its unique assemblage of parasites also meets the same fate." | x |
| F132 | 13.1.4 | example | "Another example is the case of a coevolved plant-pollinator mutualism where extinction of one invariably leads to the extinction of the other." | x |
| F133 | 13.2 | heading | "13.2 BIODIVERSITY CONSERVATION" | x |
| F134 | 13.2.1 | heading | "13.2.1 Why Should We Conserve Biodiversity?" | x |
| F135 | 13.2.1 | opener | "There are many reasons, some obvious and others not so obvious, but all equally important." | x |
| F136 | 13.2.1 | list | "They can be grouped into three categories: narrowly utilitarian, broadly utilitarian, and ethical." | x |
| F137 | 13.2.1 | concept | "The narrowly utilitarian arguments for conserving biodiversity are obvious; humans derive countless direct economic benefits from nature- food (cereals, pulses, fruits), firewood, fibre, construction material, industrial products (tannins, lubricants, dyes, resins, perfumes) and products of medicinal importance." | x |
| F138 | 13.2.1 | number | "More than 25 per cent of the drugs currently sold in the market worldwide are derived from plants" | x |
| F139 | 13.2.1 | number | "and 25,000 species of plants contribute to the traditional medicines used by native peoples around the world" | x |
| F140 | 13.2.1 | concept | "Nobody knows how many more medicinally useful plants there are in tropical rain forests waiting to be explored." | x |
| F141 | 13.2.1 | definition | "With increasing resources put into 'bioprospecting' (exploring molecular, genetic and species-level diversity for products of economic importance), nations endowed with rich biodiversity can expect to reap enormous benefits." | x |
| F142 | 13.2.1 | concept | "The broadly utilitarian argument says that biodiversity plays a major role in many ecosystem services that nature provides." | x |
| F143 | 13.2.1 | number | "The fast-dwindling Amazon forest is estimated to produce, through photosynthesis, 20 per cent of the total oxygen in the earth's atmosphere." | x |
| F144 | 13.2.1 | concept | "Can we put an economic value on this service by nature? You can get some idea by finding out how much your neighborhood hospital spends on a cylinder of oxygen." | x |
| F145 | 13.2.1 | concept | "Pollination (without which plants cannot give us fruits or seeds) is another service, ecosystems provide through pollinators layer – bees, bumblebees, birds and bats. What will be the costs of accomplishing pollination without help from natural pollinators?" | x |
| F146 | 13.2.1 | concept | "There are other intangible benefits – that we derive from nature–the aesthetic pleasures of walking through thick woods, watching spring flowers in full bloom or waking up to a bulbul's song in the morning. Can we put a price tag on such things?" | x |
| F147 | 13.2.1 | concept | "The ethical argument for conserving biodiversity relates to what we owe to millions of plant, animal and microbe species with whom we share this planet. Philosophically or spiritually, we need to realise that every species has an intrinsic value, even if it may not be of current or any economic value to us. We have a moral duty to care for their well-being and pass on our biological legacy in good order to future generations." | x |
| F148 | 13.2.2 | heading | "13.2.2 How do we conserve Biodiversity?" | x |
| F149 | 13.2.2 | opener | "When we conserve and protect the whole ecosystem, its biodiversity at all levels is protected - we save the entire forest to save the tiger." | x |
| F150 | 13.2.2 | definition | "This approach is called in situ (on site) conservation." | x |
| F151 | 13.2.2 | definition | "endangered or threatened (organisms facing a very high risk of extinction in the wild in the near future)" | x |
| F152 | 13.2.2 | definition | "However, when there are situations where an animal or plant is endangered or threatened and needs urgent measures to save it from extinction, ex situ (off site) conservation is the desirable approach." | x |
| F153 | 13.2.2 | heading | "In situ conservation–" | x |
| F154 | 13.2.2 | concept | "Faced with the conflict between development and conservation, many nations find it unrealistic and economically not feasible to conserve all their biological wealth." | x |
| F155 | 13.2.2 | concept | "Invariably, the number of species waiting to be saved from extinction far exceeds the conservation resources available. On a global basis, this problem has been addressed by eminent conservationists." | x |
| F156 | 13.2.2 | definition | "They identified for maximum protection certain 'biodiversity hotspots' regions with very high levels of species richness and high degree of endemism" | x |
| F157 | 13.2.2 | definition | "endemism (that is, species confined to that region and not found anywhere else)" | x |
| F158 | 13.2.2 | number | "Initially 25 biodiversity hotspots were identified but subsequently nine more have been added to the list, bringing the total number of biodiversity hotspots in the world to 34." | x |
| F159 | 13.2.2 | concept | "These hotspots are also regions of accelerated habitat loss." | x |
| F160 | 13.2.2 | example | "Three of these hotspots – Western Ghats and Sri Lanka, Indo-Burma and Himalaya – cover our country's exceptionally high biodiversity regions." | x |
| F161 | 13.2.2 | number | "Although all the biodiversity hotspots put together cover less than 2 per cent of the earth's land area, the number of species they collectively harbour is extremely high" | x |
| F162 | 13.2.2 | number | "strict protection of these hotspots could reduce the ongoing mass extinctions by almost 30 per cent" | x |
| F163 | 13.2.2 | concept | "In India, ecologically unique and biodiversity-rich regions are legally protected as biosphere reserves, national parks and sanctuaries." | x |
| F164 | 13.2.2 | number | "India now has 14 biosphere reserves, 90 national parks and 448 wildlife sanctuaries." | x |
| F165 | 13.2.2 | concept | "India has also a history of religious and cultural traditions that emphasised protection of nature. In many cultures, tracts of forest were set aside, and all the trees and wildlife within were venerated and given total protection." | x |
| F166 | 13.2.2 | example | "Such sacred groves are found in Khasi and Jaintia Hills in Meghalaya, Aravalli Hills of Rajasthan, Western Ghat regions of Karnataka and Maharashtra and the Sarguja, Chanda and Bastar areas of Madhya Pradesh." | x |
| F167 | 13.2.2 | concept | "In Meghalaya, the sacred groves are the last refuges for a large number of rare and threatened plants." | x |
| F168 | 13.2.2 | heading | "Ex situ Conservation–" | x |
| F169 | 13.2.2 | definition | "In this approach, threatened animals and plants are taken out from their natural habitat and placed in special setting where they can be protected and given special care." | x |
| F170 | 13.2.2 | example | "Zoological parks, botanical gardens and wildlife safari parks serve this purpose." | x |
| F171 | 13.2.2 | concept | "There are many animals that have become extinct in the wild but continue to be maintained in zoological parks." | x |
| F172 | 13.2.2 | concept | "Now gametes of threatened species can be preserved in viable and fertile condition for long periods using cryopreservation techniques" | x |
| F173 | 13.2.2 | concept | "eggs can be fertilised in vitro" | x |
| F174 | 13.2.2 | concept | "and plants can be propagated using tissue culture methods" | x |
| F175 | 13.2.2 | concept | "Seeds of different genetic strains of commercially important plants can be kept for long periods in seed banks." | x |
| F176 | 13.2.2 | concept | "Biodiversity knows no political boundaries and its conservation is therefore a collective responsibility of all nations." | x |
| F177 | 13.2.2 | number | "The historic Convention on Biological Diversity ('The Earth Summit') held in Rio de Janeiro in 1992, called upon all nations to take appropriate measures for conservation of biodiversity and sustainable utilisation of its benefits." | x |
| F178 | 13.2.2 | number | "In a follow-up, the World Summit on Sustainable Development held in 2002 in Johannesburg, South Africa, 190 countries pledged their commitment to achieve by 2010, a significant reduction in the current rate of biodiversity loss at global, regional and local levels." | x |
| F179 | 13.1.4 | number | SUMMARY-UNIQUE, folded here: "Since life originated on earth nearly 3.8 billion years ago, there had been enormous diversification of life forms on earth." The body only ever says "> 3 billion years"; the 3.8-billion figure appears nowhere in the body. | x |
| F180 | 13.1.1 | number | SUMMARY-UNIQUE, folded here: "More than 1.5 million species have been recorded in the world, but there might still be nearly 6 million species on earth waiting to be discovered and named." The "nearly 6 million still waiting" figure is stated only in the summary. | x |
| F181 | 13.1.1 | concept | SUMMARY-UNIQUE, folded here: "The group Fungi has more species than all the vertebrate species combined." This is a BROADER claim than the body's "more than the combined total of the species of fishes, amphibians, reptiles and mammals" (four classes, birds omitted). Both wordings must be carried; the broader summary form must not silently replace the body's four-class list. | x |
| F182 | 13.1.4 | number | SUMMARY-UNIQUE, folded here: "Nearly 700 species have become extinct in recent times and more than 15,500 species (of which > 650 are from India) currently face the threat of extinction." The India share (more than 650) appears only in the summary; "nearly 700" is the summary's rounding of the body's 784. | x |
| F183 | 13.2.1 | list | SUMMARY-UNIQUE, folded here: "there are many indirect benefits we receive through ecosystem services such as pollination, pest control, climate moderation and flood control". Pest control, climate moderation and flood control are named nowhere in the body — and exercise 8 depends on flood control. | x |
| F184 | 13.2.2 | number | SUMMARY-UNIQUE, folded here: the summary says "> 450 wildlife sanctuaries" where the body says "448 wildlife sanctuaries". Carry the body's exact 448 as the primary figure and record the summary's "more than 450" form alongside it. | x |
| F185 | 13.1.3 | concept | The summary's compact, exam-shaped triad: "It is believed that communities with high diversity tend to be less variable, more productive and more resistant to biological invasions." | x |
| F186 | exercise 9 | number | Exercise-only figure: "The species diversity of plants (22 per cent) is much less than that of animals (72 per cent)." The body says animals are "more than 70 per cent"; the exact 72 per cent appears only in the exercise. | x |
| F187 | exercise 4 | concept | Exercise-assumed: "What is the significance of the slope of regression in a species – area relationship?" The body poses "What do steeper slopes mean in this context?" (F079) and never answers it. | x |
| F188 | exercise 8 | concept | Exercise-assumed: "Among the ecosystem services are control of floods and soil erosion. How is this achieved by the biotic components of the ecosystem?" Flood control is named only in the summary (F183); soil erosion is named nowhere in the chapter. | x |
| F189 | exercise 10 | concept | Exercise-assumed: "Can you think of a situation where we deliberately want to make a species extinct? How would you justify it?" The body offers no content at all on deliberate extinction. | x |

### Heading census (step 3a) — walked as its own list, ignoring prose

21 heading rows. Numbered: F001 (chapter title), F009 (13.1), F024 (13.1.1), F052 (13.1.2), F082 (13.1.3), F095 (13.1.4), F133 (13.2), F134 (13.2.1), F148 (13.2.2) = 9. Unnumbered run-in sub-headings, the class of item Ch9's D4 lost: F013, F018, F020 (the three diversity levels), F053, F069 (the two biodiversity patterns), F111 ("Causes of biodiversity losses:"), F113, F120, F124, F129 (the four Evil Quartet causes), F153 ("In situ conservation–"), F168 ("Ex situ Conservation–") = 12. Total 9 + 12 = 21.

**Count-correction note (Gate 1 §6 re-parse, this session):** the header and this line previously read **22** (9 numbered + "13" unnumbered) while the unnumbered ID list itself has only ever contained **12** entries — the "13" was a hand-tally slip, not a missing row. A machine re-parse of the Facts table returns exactly 21 `Type: heading` rows, matching the enumerated IDs above. No Facts row was added, removed, or reclassified to reach this figure.

**Judgement call recorded openly:** "The narrowly utilitarian arguments…", "The broadly utilitarian argument…" and "The ethical argument…" (F137, F142, F147) are *italicised phrases inside running prose*, not headings, so they are inventoried as concept rows rather than heading rows. Pass 2 may still typeset them as H3-level headings for readability — that is a presentation choice, not a structural omission. If a later pass decides they are headings, add heading rows rather than reclassifying these.

### Opener census (step 3b) — first sentence of every section, inventoried deliberately

8 opener rows: F002 (chapter opener), F010 (13.1), F025 (13.1.1), F054 (13.1.2), F083 (13.1.3), F096 (13.1.4), F135 (13.2.1), F149 (13.2.2).

Two sections have **no opener prose of their own** and therefore correctly contribute **no** opener row: **13.1.2** opens directly on sub-heading (i) (F053 is its heading, F054 the first sentence that follows), and **13.2** runs straight into 13.2.1. Both are deliberate structural findings, not missing rows.

**Count-correction note (Gate 1 §6 re-parse, this session):** the header and this line previously read **9**. The enumerated list has only ever named **8** real `Type: opener` IDs; the phantom 9th was the *structural finding* about 13.1.2/13.2 being written up as though it were an additional row. A machine re-parse returns exactly 8 `Type: opener` rows. No Facts row was added, removed, or reclassified.

---

## Summary classification

25 sentences in the p10–p11 SUMMARY block. BODY-PRESENT 19, SUMMARY-UNIQUE 6. Every SUMMARY-UNIQUE sentence is folded into a numbered body row above.

| Summary sentence | Classification | Folded into |
|---|---|---|
| "Since life originated on earth nearly 3.8 billion years ago, there had been enormous diversification of life forms on earth." | SUMMARY-UNIQUE | F179 |
| "Biodiversity refers to the sum total of diversity that exists at all levels of biological organisation." | BODY-PRESENT | F011 |
| "Of particular importance is the diversity at genetic, species and ecosystem levels and conservation efforts are aimed at protecting diversity at all these levels." | BODY-PRESENT | F012 |
| "More than 1.5 million species have been recorded in the world, but there might still be nearly 6 million species on earth waiting to be discovered and named." | SUMMARY-UNIQUE | F180 |
| "Of the named species, > 70 per cent are animals, of which 70 per cent are insects." | BODY-PRESENT | F033, F035 |
| "The group Fungi has more species than all the vertebrate species combined." | SUMMARY-UNIQUE | F181 |
| "India, with about 45,000 species of plants and twice as many species of animals, is one of the 12 mega diversity countries of the world." | BODY-PRESENT | F045, F046 |
| "Species diversity on earth is not uniformly distributed but shows interesting patterns." | BODY-PRESENT | F054 |
| "It is generally highest in the tropics and decreases towards the poles." | BODY-PRESENT | F056 |
| "Important explanations for the species richness of the tropics are: Tropics had more evolutionary time; they provide a relatively constant environment and, they receive more solar energy which contributes to greater productivity." | BODY-PRESENT | F066, F067, F068 |
| "Species richness is also function of the area of a region; the species-area relationship is generally a rectangular hyperbolic function." | BODY-PRESENT | F072 |
| "It is believed that communities with high diversity tend to be less variable, more productive and more resistant to biological invasions." | BODY-PRESENT | F185 |
| "Earth's fossil history reveals incidence of mass extinctions in the past, but the present rates of extinction, largely attributed to human activities, are 100 to 1000 times higher." | BODY-PRESENT | F105, F108 |
| "Nearly 700 species have become extinct in recent times and more than 15,500 species (of which > 650 are from India) currently face the threat of extinction." | SUMMARY-UNIQUE | F182 |
| "The causes of high extinction rates at present include habitat (particularly forests) loss and fragmentation, over-exploitation, biological invasions and co-extinctions." | BODY-PRESENT | F112 |
| "Earth's rich biodiversity is vital for the very survival of mankind." | BODY-PRESENT | F090 |
| "The reasons for conserving biodiversity are narrowly utilitarian, broadly utilitarian and ethical." | BODY-PRESENT | F136 |
| "Besides the direct benefits (food, fibre, firewood, pharmaceuticals, etc.), there are many indirect benefits we receive through ecosystem services such as pollination, pest control, climate moderation and flood control." | SUMMARY-UNIQUE | F183 |
| "We also have a moral responsibility to take good care of earth's biodiversity and pass it on in good order to our next generation." | BODY-PRESENT | F147 |
| "Biodiversity conservation may be in situ as well as ex situ." | BODY-PRESENT | F150, F152 |
| "In in situ conservation, the endangered species are protected in their natural habitat so that the entire ecosystem is protected." | BODY-PRESENT | F149 |
| "Recently, 34 'biodiversity hotspots' in the world have been proposed for intensive conservation efforts." | BODY-PRESENT | F158 |
| "Of these, three (Western Ghats-Sri Lanka, Himalaya and Indo-Burma) cover India's rich biodiversity regions." | BODY-PRESENT | F160 |
| "Our country's in situ conservation efforts are reflected in its 14 biosphere reserves, 90 national parks, > 450 wildlife sanctuaries and many sacred groves." | SUMMARY-UNIQUE | F184 |
| "Ex situ conservation methods include protective maintenance of threatened species in zoological parks and botanical gardens, in vitro fertilisation, tissue culture propagation and cryopreservation of gametes." | BODY-PRESENT | F169 to F175 |

---

## Exercise-gap terms

All 10 exercises were read. Six (Q1, Q2, Q3, Q5, Q6, Q7) are fully answerable from the body. Four assume something the body never supplies.

| Term/fact assumed by exercises | Explained where |
|---|---|
| **Q4** — the significance of the slope (Z) of the regression in a species-area relationship. The body poses "What do steeper slopes mean?" (F079) and leaves it hanging. | A NOTE box at the end of 13.1.2 (ii) stating plainly that a steeper slope means species richness rises faster per unit area, so whole continents accumulate species far more steeply (Z 0.6 to 1.2) than habitat patches within a single region (Z 0.1 to 0.2). Ties F075, F077 and F078 together and finally answers F079. |
| **Q8** — control of floods and soil erosion as ecosystem services delivered by biotic components. Flood control is named only in the summary (F183); soil erosion is named nowhere in the chapter at all. | Folded into 13.2.1's broadly-utilitarian block alongside F142 and F183, as an explicit sentence on root systems and vegetation cover binding soil and slowing run-off. Must be visibly attributed as summary-sourced plus necessary inference, not presented as body text. |
| **Q9** — the exercise's "animals (72 per cent)" figure, which the body never states (body: "more than 70 per cent"). | A NOTE under 13.1.1 carrying F186: the exercise quotes 72 per cent while the body says more than 70 per cent, so a NEET answer must recognise both forms. |
| **Q10** — a situation where a species is deliberately driven extinct, and its justification. No body content whatsoever. | A MEMORY AID box at the end of 13.1.4, explicitly marked "not in NCERT", covering disease-causing organisms such as the smallpox virus, polio virus and Guinea worm as legitimate eradication targets. Must be unmistakably marked as outside-NCERT reasoning. |

---

## Figure manifest

| Fig # | Caption (verbatim) | Asset file | Source page | Mono | Verified |
|---|---|---|---|---|---|
| Fig 13.1 | "Representing global biodiversity: proportionate number of species of major taxa of plants, invertebrates and vertebrates" | `assets/fig_13_1.png` | p3 (book p218) | yes | yes |
| Fig 13.2 | "Showing species area relationship. Note that on log scale the relationship becomes linear" | `assets/fig_13_2.png` | p5 (book p220) | yes | yes |

### Figure census — how "only 2 figures" was established (negative evidence)

A two-figure chapter is exactly the kind of suspiciously thin result §4.4 says to distrust, so the census was run four independent ways and all four agree:

1. **Caption sweep** — every text block on all 13 pages beginning `Figure`: two hits only, p3 (`Figure 13.1`) and p5 (`Figure 13.2`).
2. **In-text reference sweep** — every `Fig…13.n` mention in the extracted text: `Figure 13.1` (p3 body + caption) and `Figure13.2` / `Figure 13.2` (p5 body + caption). **No reference to any 13.3 or higher exists**, so no figure is missing its caption.
3. **Vector-drawing density per page** — pages carrying a diagram stand out sharply: p3 = 93,887 drawing ops (the three pie charts), p5 = 72 (the species–area graph). Every other page sits at 4–18 ops, the same baseline as figure-free p4, so no undetected vector diagram exists.
4. **Raster-image census** — every embedded raster on every page resolves to page furniture, not content: the 2480×3508 page background and 1894×1894 `© NCERT / not to be republished` watermark (all 13 pp), the 1275×203 header band, the p1 chapter-opener QR code (275×280) and its tilted decorative thumbnail of Fig 13.1 (177×177), and the 200×1108 decorative grain strip on pp10–11.

**Consequence for §7's person-photograph check: this chapter contains no photograph of any kind, and no scientist portrait.** There is also no "Do You Know?" box, so §5 item 3 has nothing to act on here and `check_pdf.py` check 4 should report no manifest portrait row. The p1 decorative thumbnail is a rotated miniature of Fig 13.1 itself — it is page furniture, deliberately **not** extracted, and must not be embedded as a figure.

### Per-figure verification record (§4.4 Step 3 — every figure, not a spot-check)

Both assets were extracted as **300 dpi clip renders** (`page.get_pixmap(clip=rect, dpi=300)`) rather than embedded-object grabs, because Fig 13.1 is pure vector (93,887 ops) and Fig 13.2 mixes vector strokes with vector text — an object extraction would have mangled both. Each was then `convert("L")` + `autocontrast(cutoff=1)` and **re-opened and read**. Both were **re-opened and re-read a second time during the inventory session** before their labels were frozen into the Facts table, and both label sets were confirmed unchanged (18 and 5).

| Check (a–f) | Fig 13.1 | Fig 13.2 |
|---|---|---|
| (a) correct figure for its caption | yes — three pie charts of taxa proportions | yes — species-richness vs area curve |
| (b) no label or leader line cropped | yes — clip taken at the rounded panel border; all 18 labels and all 4 leader arrows (Other animal groups, Crustaceans, Molluscs, Insects) fully inside | yes — clip taken at the outer tint box; both axis labels, both curve labels and the "log-log scale" in-line label fully inside |
| (c) legible at print size | yes | yes |
| (d) not a grab of a neighbouring figure/table/text | yes — caption sits below the clip (caption bbox starts y=581, clip ends y=578) | yes — caption sits below the clip (caption bbox starts y=463, clip ends y=458) |
| (e) genuinely monochrome | yes — `mode == "L"`, **0 colour pixels** sampled, greys span the full 0–255 range | yes — `mode == "L"`, **0 colour pixels** sampled, greys span 0–255 |
| (f) colour-carried distinctions survive | yes — see note below | yes — see note below |

- **Fig 13.1**, asset 1501×1434 px (≈12.7 × 12.1 cm at 300 dpi), sha256 `b4ecdb3378fd…`. The original separates pie wedges by hue; after conversion every wedge is separated by **both** a distinct grey level **and** a black boundary stroke, and every wedge is additionally named by its own text label, so no wedge identity rests on tone alone. NCERT prints **no numeric percentages inside this figure** — the proportions live in the running text (>70% animals, ≤22% plants, >70% of animals are insects), which is where the replacement chapter must carry them.
- **Fig 13.2**, asset 1117×959 px (≈9.5 × 8.1 cm at 300 dpi), sha256 `fd385c5e622f…`. The original distinguishes the two plots by colour — a blue arithmetic-scale curve and a crimson log-log straight line. After conversion they are **mid-grey (curve) vs near-black (straight line)**, still tell-apart-able, and each carries its own text label (the power-law form on the curve, the log form on the line, plus `log-log scale` written along the line).

**Figures requiring manual attention: none.** Both extracted and converted cleanly on the first attempt; no figure was skipped, and no bad crop was accepted.

**Residual source artefact (not a defect, recorded so a later pass does not "fix" it):** the NCERT `© NCERT / not to be republished` diagonal watermark is part of the source page and therefore appears faintly across both crops — heavily over Fig 13.1, at the right edge of Fig 13.2. It obscures no label or stroke in either figure. Every previously delivered chapter in this repo carries the same artefact.

### Label harvest method (the §4.4 self-concealing-failure test)

Per-figure label counts: Fig 13.1 = **18** (Invertebrates panel 5, Vertebrates panel 6, Plants panel 7) · Fig 13.2 = **5**. Total **23**, all distinct.

`page.get_text()` on source pp. 3 and 5 returns the captions and the body prose but **zero** in-figure labels — all 23 are baked into the artwork as vector strokes. A text-extraction harvest here would have returned an empty label set and passed both Gate 1 and check 6 trivially while catching nothing. Every label in F039 and F081 was read off the 300 dpi renders by eye.

---

## Carry-overs Pass 2 must action

1. **Colour loss in Fig 13.2 — mandatory caption sentence.** The original distinguishes the rectangular-hyperbola curve (blue) from the straight log-log line (crimson) **by colour**; after conversion they are mid-grey vs near-black. Per §4.4 the caption must state the distinction in words — name which plot is the arithmetic-scale hyperbola and which is the same relationship on a log-log scale, so the reader never needs the lost hue.
2. **`S = CAZ` in F081 is the extraction-normalised form** of the figure's `S = CA` with a superscript Z. Since §4 bans Unicode superscripts, the running text must render it as `S = CA<super>Z</super>`, which extracts as `S = CAZ` and matches the recorded label. **Do not "correct" the inventory row to contain a caret or a Unicode superscript** — either would guarantee a check-6 FAIL that no prose edit could fix.
3. **`Log S = log C + Z log A` is capitalised in the figure but lower-case in the body (F073).** `_norm` case-folds so either form matches, but the equation must be written into the running text at least once so the label is genuinely covered rather than accidentally covered.
4. **Degree signs.** F057, F059 and F060 have already been spelled out as "23.5 degrees N", "41 degrees N", "71 degrees N". Keep them spelled out in the PDF so check 5 has nothing to flag.
5. **F037 and F181 must both appear.** The body's four-class comparison (fishes, amphibians, reptiles, mammals) and the summary's broader "all vertebrates combined" claim are different statements. Writing only the summary form loses the body's exact list; writing only the body form loses the summary's generalisation. A NOTE box carrying both is the safest home.
6. **F164 vs F184.** Write 448 wildlife sanctuaries as the body figure and note the summary's "more than 450" — a NEET question may quote either.
7. **`Type` column casing is inconsistent for caption rows** (found by this session's re-parse, recorded rather than silently rewritten). F038 and F080 use lower-case `caption` (the two NCERT figure captions); F039 and F081 use capitalised `Caption` (the two label-harvest rows). A case-sensitive tally therefore sees `caption: 2` + `Caption: 2` instead of one class of 4. This breaks no Gate 1 criterion — no header count is derived from the caption type, and `check_pdf.py`'s `_extract_labels` keys off the *wording* (`Figure labels…`), not the type, so all 23 labels are still found. Left as-is deliberately: F039/F081 are structurally a different kind of row from F038/F080, and normalising the casing now would edit frozen Facts rows for a cosmetic gain. Any future pass that tallies by `Type` must case-fold.
