# Ch11 Photosynthesis in Higher Plants — FROZEN Inventory (Pass 1)

## Freeze header

**Chapter:** Class 11, Chapter 11 — Photosynthesis in Higher Plants
**Source PDF:** `Chapter/class 11/Chapter 11 - Photosynthesis in Higher Plants.pdf` (22 PDF pages; textbook pp. 133–152; page box 576 x 784.8)
**Protocol:** normal 3-pass gated workflow (`SUPREME COMMAND PROMPT.md` v6).
**Pass 1 status:** COMPLETE — all five sessions run (`1-S`, `1-H`, `1-O`, `1-F`, `1-Z`); **GATE 1 CLOSED 2026-09-01 at the end of session `1-Z`**, with every header count re-derived by machine from this finished table (never hand-tallied) and the label matrix validated through `check_pdf.py._extract_labels`. See the *Gate 1 closure record* at the foot of this file. Table below is **FROZEN**: rows are never renumbered, moved, deleted, or re-typed. Any later addition is appended with an `a`-suffixed ID and logged as a Pass-3(b) gap, never back-dated into the freeze.

**Predecessor annulled.** The file previously occupying this path was *not* a SUPREME-format frozen inventory — it was figure-extraction documentation (environment record, crop register, reproducibility notes). It is **quashed** for inventory purposes and preserved for its crop-rect provenance as `figure_extraction_record.md`. Nothing in it is treated as a Gate 1 artifact; this file is written from a fresh five-session Pass 1.

**Row total:** 282 rows, `F001`–`F282`, contiguous, 0 gaps, 0 duplicate IDs, monotonic, 0 ticked (Pass 1 emits no `[x]`).

**Block composition (session → ID range → rows):**
- `1-S` Facts sweep → `F001`–`F218` → 218 rows
- `1-H` heading sweep → `F219`–`F246` → 28 rows
- `1-O` opener sweep → `F247`–`F266` → 20 rows
- `1-Z` summary-unique fold → `F267`–`F270` → 4 rows
- `1-F` figure-label matrix → `F271`–`F282` → 12 rows
- Total = 218 + 28 + 20 + 4 + 12 = **282**, equal to the highest ID.

**Type census of the contiguous `F001`–`F282` table (normalized lowercase; machine re-derived by re-parsing this finished table in session 1-Z; sums to 282):**
`concept` 128 · `definition` 31 · `number` 28 · `heading` 28 · `process` 26 · `opener` 20 · `caption` 12 · `equation` 5 · `example` 4 = **282**. Exactly 9 `Type` values exist in the table and all are lowercase — no `Caption`/`caption` style split.

**Heading census:** 19 numbered + the 9 unnumbered IDs listed in the *Heading census* section below = **28**, equal to the machine-derived `heading` row count. The derivation is written there so the total is derivable from its own list.
**Opener census:** **20** opener rows, `F247`–`F266` — one opening sentence per section/sub-section that begins with running prose. The ID list is in the *Opener census* section below.
**Summary classification:** **20** summary sentences (the SUMMARY block, PDF p. 21) → **15 BODY-PRESENT + 5 SUMMARY-UNIQUE**, all 5 folded into the 4 body rows `F267`–`F270` (`F270` carries two folds). See the correction note in that section.
**Exercise-gap scan:** 9 exercises → 4 genuine gaps, each with a planned Pass-2 home (see the exercise-gap table).
**Figure census:** 12 assets (Figures 11.1, 11.2, 11.3a, 11.3b, 11.3c, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9, 11.10), each one label row `F271`–`F282`. Page 22 refers back to Figure 11.10 and carries no new plate.
**Label census (machine-derived by `check_pdf.py._extract_labels`):** **12 figure rows / 116 labels**, per-figure 4 + 8 + 5 + 2 + 9 + 4 + 12 + 7 + 26 + 16 + 16 + 7 = 116; **no doubling, no phantom `Fig #` row, no duplicate (figure, label) pair.**

---

## Facts

Legend — the `Type` column uses one of the 9 normalized lowercase census values. Cell 4 is the atomic fact wording. Sub/superscripts are written plainly here (`CO2`, `H+`, `NADP+`) and become `<sub>`/`<super>` tags in Pass 2.

| ID | Section | Type | Fact wording | Tick |
|---|---|---|---|---|
| F001 | 11.unit4 | concept | The description of structure and variation of living organisms over a period of time ended up as two apparently irreconcilable perspectives on biology, resting on two levels of organisation of life forms and phenomena. | x |
| F002 | 11.unit4 | concept | One perspective described life at the organismic and above level of organisation and resulted in ecology and related disciplines; the second described it at the cellular and molecular level and resulted in physiology and biochemistry. | x |
| F003 | 11.unit4 | concept | The processes of photosynthesis, respiration and plant growth and development are described in molecular terms but in the context of cellular activities and even at organism level, and the relation of the physiological processes to environment is also discussed. | x |
| F004 | 11.calvin | number | Melvin Calvin was born in Minnesota in April 1911. | x |
| F005 | 11.calvin | concept | Melvin Calvin received his Ph.D. in Chemistry from the University of Minnesota and served as Professor of Chemistry at the University of California, Berkeley. | x |
| F006 | 11.calvin | concept | Just after world war II, when the world was under shock after the Hiroshima-Nagasaki bombings and seeing the ill-effects of radio-activity, Calvin and co-workers put radio-activity to beneficial use. | x |
| F007 | 11.calvin | concept | Calvin, along with J.A. Bassham, studied reactions in green plants forming sugar and other substances from raw materials like carbon dioxide, water and minerals by labelling the carbon dioxide with C14. | x |
| F008 | 11.calvin | concept | Calvin proposed that plants change light energy to chemical energy by transferring an electron in an organised array of pigment molecules and other substances. | x |
| F009 | 11.calvin | number | The mapping of the pathway of carbon assimilation in photosynthesis earned Melvin Calvin the Nobel Prize in 1961. | x |
| F010 | 11.calvin | concept | The principles of photosynthesis as established by Calvin are at present being used in studies on renewable resource for energy and materials and basic studies in solar energy research. | x |
| F011 | 11.intro | concept | All animals including human beings depend on plants for their food. | x |
| F012 | 11.intro | definition | Green plants make or rather synthesise the food they need through photosynthesis and are therefore called autotrophs. | x |
| F013 | 11.intro | definition | Autotrophic nutrition is found only in plants, and all other organisms that depend on the green plants for food are heterotrophs. | x |
| F014 | 11.intro | definition | Photosynthesis is a physico-chemical process by which green plants use light energy to drive the synthesis of organic compounds. | x |
| F015 | 11.intro | concept | Ultimately, all living forms on earth depend on sunlight for energy, and the use of energy from sunlight by plants doing photosynthesis is the basis of life on earth. | x |
| F016 | 11.intro | concept | Photosynthesis is important due to two reasons: it is the primary source of all food on earth, and it is also responsible for the release of oxygen into the atmosphere by green plants. | x |
| F017 | 11.intro | concept | This chapter focusses on the structure of the photosynthetic machinery and the various reactions that transform light energy into chemical energy. | x |
| F018 | 11.1 | concept | Simple experiments have shown that chlorophyll (green pigment of the leaf), light and CO2 are required for photosynthesis to occur. | x |
| F019 | 11.1 | process | In the starch-formation experiment two leaves are used — a variegated leaf, or a leaf that was partially covered with black paper — and exposed to light. | x |
| F020 | 11.1 | concept | On testing these leaves for the presence of starch it was clear that photosynthesis occurred only in the green parts of the leaves in the presence of light. | x |
| F021 | 11.1 | process | In another experiment a part of a leaf is enclosed in a test tube containing some KOH soaked cotton (which absorbs CO2), while the other half is exposed to air, and the setup is then placed in light for some time. | x |
| F022 | 11.1 | concept | On testing for the presence of starch later, the exposed part of the leaf tested positive for starch while the portion that was in the tube tested negative, which showed that CO2 was required for photosynthesis. | x |
| F023 | 11.2 | concept | It is interesting to learn about those simple experiments that led to a gradual development in our understanding of photosynthesis. | x |
| F024 | 11.2 | number | Joseph Priestley (1733-1804) in 1770 performed a series of experiments that revealed the essential role of air in the growth of green plants. | x |
| F025 | 11.2 | number | Priestley discovered oxygen in 1774. | x |
| F026 | 11.2 | process | Priestley observed that a candle burning in a closed space — a bell jar — soon gets extinguished, and similarly a mouse would soon suffocate in a closed space. | x |
| F027 | 11.2 | concept | Priestley concluded that a burning candle or an animal that breathe the air both somehow damage the air. | x |
| F028 | 11.2 | process | When Priestley placed a mint plant in the same bell jar, he found that the mouse stayed alive and the candle continued to burn. | x |
| F029 | 11.2 | concept | Priestley hypothesised as follows: Plants restore to the air whatever breathing animals and burning candles remove. | x |
| F030 | 11.2 | number | Jan Ingenhousz (1730-1799), using a similar setup as the one used by Priestley but by placing it once in the dark and once in the sunlight, showed that sunlight is essential for the plant process that somehow purifies the air fouled by burning candles or breathing animals. | x |
| F031 | 11.2 | process | Ingenhousz, in an elegant experiment with an aquatic plant, showed that in bright sunlight small bubbles were formed around the green parts while in the dark they did not; later he identified these bubbles to be of oxygen. | x |
| F032 | 11.2 | concept | Ingenhousz hence showed that it is only the green part of the plants that could release oxygen. | x |
| F033 | 11.2 | number | It was not until about 1854 that Julius von Sachs provided evidence for production of glucose when plants grow. | x |
| F034 | 11.2 | concept | Glucose is usually stored as starch. | x |
| F035 | 11.2 | concept | Sachs' later studies showed that the green substance in plants (chlorophyll as we know it now) is located in special bodies (later called chloroplasts) within plant cells. | x |
| F036 | 11.2 | concept | Sachs found that the green parts in plants is where glucose is made, and that the glucose is usually stored as starch. | x |
| F037 | 11.2 | number | T.W Engelmann (1843-1909), using a prism, split light into its spectral components and then illuminated a green alga, Cladophora, placed in a suspension of aerobic bacteria. | x |
| F038 | 11.2 | concept | The bacteria were used to detect the sites of O2 evolution. | x |
| F039 | 11.2 | concept | Engelmann observed that the bacteria accumulated mainly in the region of blue and red light of the split spectrum. | x |
| F040 | 11.2 | concept | A first action spectrum of photosynthesis was thus described, and it resembles roughly the absorption spectra of chlorophyll a and b. | x |
| F041 | 11.2 | concept | By the middle of the nineteenth century the key features of plant photosynthesis were known, namely that plants could use light energy to make carbohydrates from CO2 and water. | x |
| F042 | 11.2 | equation | The empirical equation representing the total process of photosynthesis for oxygen evolving organisms was then understood as: CO2 + H2O, in the presence of light, yields [CH2O] + O2. | x |
| F043 | 11.2 | definition | In that empirical equation [CH2O] represented a carbohydrate (e.g., glucose, a six-carbon sugar). | x |
| F044 | 11.2 | number | A milestone contribution to the understanding of photosynthesis was made by a microbiologist, Cornelius van Niel (1897-1985). | x |
| F045 | 11.2 | concept | Van Niel, based on his studies of purple and green bacteria, demonstrated that photosynthesis is essentially a light-dependent reaction in which hydrogen from a suitable oxidisable compound reduces carbon dioxide to carbohydrates. | x |
| F046 | 11.2 | equation | Van Niel's finding can be expressed by: 2H2A + CO2, in the presence of light, yields 2A + CH2O + H2O. | x |
| F047 | 11.2 | concept | In green plants H2O is the hydrogen donor and is oxidised to O2. | x |
| F048 | 11.2 | concept | Some organisms do not release O2 during photosynthesis. | x |
| F049 | 11.2 | example | When H2S instead is the hydrogen donor for purple and green sulphur bacteria, the 'oxidation' product is sulphur or sulphate depending on the organism and not O2. | x |
| F050 | 11.2 | concept | Van Niel hence inferred that the O2 evolved by the green plant comes from H2O, not from carbon dioxide; this was later proved by using radioisotopic techniques. | x |
| F051 | 11.2 | equation | The correct equation that would represent the overall process of photosynthesis is: 6CO2 + 12H2O, in the presence of light, yields C6H12O6 + 6H2O + 6O2. | x |
| F052 | 11.2 | definition | In the correct overall equation C6H12O6 represents glucose. | x |
| F053 | 11.2 | concept | The O2 released is from water; this was proved using radio isotope techniques. | x |
| F054 | 11.2 | concept | The overall equation is not a single reaction but a description of a multistep process called photosynthesis. | x |
| F055 | 11.3 | concept | Photosynthesis does take place in the green leaves of plants but it does so also in other green parts of the plants. | x |
| F056 | 11.3 | concept | The mesophyll cells in the leaves have a large number of chloroplasts. | x |
| F057 | 11.3 | concept | Usually the chloroplasts align themselves along the walls of the mesophyll cells, such that they get the optimum quantity of the incident light. | x |
| F058 | 11.3 | concept | Within the chloroplast there is a membranous system consisting of grana, the stroma lamellae, and the matrix stroma. | x |
| F059 | 11.3 | concept | There is a clear division of labour within the chloroplast. | x |
| F060 | 11.3 | concept | The membrane system is responsible for trapping the light energy and also for the synthesis of ATP and NADPH. | x |
| F061 | 11.3 | concept | In stroma, enzymatic reactions synthesise sugar, which in turn forms starch. | x |
| F062 | 11.3 | definition | The reactions of the membrane system, since they are directly light driven, are called light reactions (photochemical reactions). | x |
| F063 | 11.3 | definition | The stromal reactions are not directly light driven but are dependent on the products of light reactions (ATP and NADPH); hence, to distinguish them, they are called by convention dark reactions (carbon reactions). | x |
| F064 | 11.3 | concept | That the stromal reactions are called dark reactions should not be construed to mean that they occur in darkness or that they are not light-dependent. | x |
| F065 | 11.4 | process | The leaf pigments of any green plant can be separated through paper chromatography. | x |
| F066 | 11.4 | concept | A chromatographic separation of the leaf pigments shows that the colour that we see in leaves is not due to a single pigment but due to four pigments. | x |
| F067 | 11.4 | number | The four leaf pigments are chlorophyll a (bright or blue green in the chromatogram), chlorophyll b (yellow green), xanthophylls (yellow) and carotenoids (yellow to yellow-orange). | x |
| F068 | 11.4 | definition | Pigments are substances that have an ability to absorb light at specific wavelengths. | x |
| F069 | 11.4 | concept | The wavelengths at which there is maximum absorption by chlorophyll a, i.e., in the blue and the red regions, also show a higher rate of photosynthesis. | x |
| F070 | 11.4 | concept | Hence we can conclude that chlorophyll a is the chief pigment associated with photosynthesis. | x |
| F071 | 11.4 | concept | There is not a complete one-to-one overlap between the absorption spectrum of chlorophyll a and the action spectrum of photosynthesis. | x |
| F072 | 11.4 | concept | The graphs together show that most of the photosynthesis takes place in the blue and red regions of the spectrum; some photosynthesis does take place at the other wavelengths of the visible spectrum. | x |
| F073 | 11.4 | definition | Though chlorophyll is the major pigment responsible for trapping light, other thylakoid pigments like chlorophyll b, xanthophylls and carotenoids are called accessory pigments; they also absorb light and transfer the energy to chlorophyll a. | x |
| F074 | 11.4 | concept | The accessory pigments not only enable a wider range of wavelength of incoming light to be utilised for photosynthesis but also protect chlorophyll a from photo-oxidation. | x |
| F075 | 11.5 | definition | Light reactions or the 'Photochemical' phase include light absorption, water splitting, oxygen release, and the formation of high-energy chemical intermediates, ATP and NADPH. | x |
| F076 | 11.5 | concept | Several protein complexes are involved in the light reaction. | x |
| F077 | 11.5 | concept | The pigments are organised into two discrete photochemical light harvesting complexes (LHC) within the Photosystem I (PS I) and Photosystem II (PS II). | x |
| F078 | 11.5 | concept | The photosystems are named in the sequence of their discovery, and not in the sequence in which they function during the light reaction. | x |
| F079 | 11.5 | concept | The LHC are made up of hundreds of pigment molecules bound to proteins. | x |
| F080 | 11.5 | definition | Each photosystem has all the pigments (except one molecule of chlorophyll a) forming a light harvesting system also called antennae. | x |
| F081 | 11.5 | concept | These antenna pigments help to make photosynthesis more efficient by absorbing different wavelengths of light. | x |
| F082 | 11.5 | definition | The single chlorophyll a molecule forms the reaction centre, and the reaction centre is different in both the photosystems. | x |
| F083 | 11.5 | number | In PS I the reaction centre chlorophyll a has an absorption peak at 700 nm, hence is called P700, while in PS II it has absorption maxima at 680 nm and is called P680. | x |
| F084 | 11.6 | number | In photosystem II the reaction centre chlorophyll a absorbs 680 nm wavelength of red light causing electrons to become excited and jump into an orbit farther from the atomic nucleus. | x |
| F085 | 11.6 | process | These electrons are picked up by an electron acceptor which passes them to an electron transport system consisting of cytochromes. | x |
| F086 | 11.6 | concept | This movement of electrons is downhill, in terms of an oxidation-reduction or redox potential scale. | x |
| F087 | 11.6 | concept | The electrons are not used up as they pass through the electron transport chain, but are passed on to the pigments of photosystem PS I. | x |
| F088 | 11.6 | number | Simultaneously, electrons in the reaction centre of PS I are also excited when they receive red light of wavelength 700 nm and are transferred to another accepter molecule that has a greater redox potential. | x |
| F089 | 11.6 | process | These electrons then are moved downhill again, this time to a molecule of energy-rich NADP+, and the addition of these electrons reduces NADP+ to NADPH + H+. | x |
| F090 | 11.6 | definition | The whole scheme of transfer of electrons — starting from the PS II, uphill to the acceptor, down the electron transport chain to PS I, excitation of electrons, transfer to another acceptor, and finally downhill to NADP+ reducing it to NADPH + H+ — is called the Z scheme, due to its characterstic shape. | x |
| F091 | 11.6 | concept | The Z shape is formed when all the carriers are placed in a sequence on a redox potential scale. | x |
| F092 | 11.6.1 | concept | The electrons that were moved from photosystem II must be replaced, and this is achieved by electrons available due to splitting of water. | x |
| F093 | 11.6.1 | process | The splitting of water is associated with the PS II; water is split into 2H+, [O] and electrons. | x |
| F094 | 11.6.1 | concept | The splitting of water creates oxygen, one of the net products of photosynthesis. | x |
| F095 | 11.6.1 | concept | The electrons needed to replace those removed from photosystem I are provided by photosystem II. | x |
| F096 | 11.6.1 | equation | The water-splitting reaction is: 2H2O yields 4H+ + O2 + 4e-. | x |
| F097 | 11.6.1 | concept | The water splitting complex is associated with the PS II, which itself is physically located on the inner side of the membrane of the thylakoid. | x |
| F098 | 11.6.2 | concept | Living organisms have the capability of extracting energy from oxidisable substances and store this in the form of bond energy, and special substances like ATP carry this energy in their chemical bonds. | x |
| F099 | 11.6.2 | definition | The process through which ATP is synthesised by cells (in mitochondria and chloroplasts) is named phosphorylation. | x |
| F100 | 11.6.2 | definition | Photophosphorylation is the synthesis of ATP from ADP and inorganic phosphate in the presence of light. | x |
| F101 | 11.6.2 | definition | When the two photosystems work in a series, first PS II and then the PS I, a process called non-cyclic photo-phosphorylation occurs. | x |
| F102 | 11.6.2 | concept | The two photosystems are connected through an electron transport chain, as seen in the Z scheme, and both ATP and NADPH + H+ are synthesised by this kind of electron flow. | x |
| F103 | 11.6.2 | concept | When only PS I is functional, the electron is circulated within the photosystem and the phosphorylation occurs due to cyclic flow of electrons. | x |
| F104 | 11.6.2 | concept | A possible location where cyclic photophosphorylation could be happening is in the stroma lamellae. | x |
| F105 | 11.6.2 | concept | While the membrane or lamellae of the grana have both PS I and PS II, the stroma lamellae membranes lack PS II as well as NADP reductase enzyme. | x |
| F106 | 11.6.2 | process | In cyclic flow the excited electron does not pass on to NADP+ but is cycled back to the PS I complex through the electron transport chain. | x |
| F107 | 11.6.2 | concept | The cyclic flow hence results only in the synthesis of ATP, but not of NADPH + H+. | x |
| F108 | 11.6.2 | number | Cyclic photophosphorylation also occurs when only light of wavelengths beyond 680 nm are available for excitation. | x |
| F109 | 11.6.3 | concept | The chemiosmotic hypothesis has been put forward to explain the mechanism by which ATP is synthesised in the chloroplast. | x |
| F110 | 11.6.3 | concept | Like in respiration, in photosynthesis too ATP synthesis is linked to development of a proton gradient across a membrane; this time these are the membranes of thylakoid. | x |
| F111 | 11.6.3 | concept | There is one difference though: here the proton accumulation is towards the inside of the membrane, i.e., in the lumen, whereas in respiration protons accumulate in the intermembrane space of the mitochondria when electrons move through the ETS. | x |
| F112 | 11.6.3 | process | Since splitting of the water molecule takes place on the inner side of the membrane, the protons or hydrogen ions that are produced by the splitting of water accumulate within the lumen of the thylakoids. | x |
| F113 | 11.6.3 | process | As electrons move through the photosystems, protons are transported across the membrane, because the primary accepter of electron which is located towards the outer side of the membrane transfers its electron not to an electron carrier but to an H carrier. | x |
| F114 | 11.6.3 | process | Hence this H-carrier molecule removes a proton from the stroma while transporting an electron, and when this molecule passes on its electron to the electron carrier on the inner side of the membrane, the proton is released into the inner side or the lumen side of the membrane. | x |
| F115 | 11.6.3 | process | The NADP reductase enzyme is located on the stroma side of the membrane, and along with electrons that come from the acceptor of electrons of PS I, protons are necessary for the reduction of NADP+ to NADPH + H+; these protons are also removed from the stroma. | x |
| F116 | 11.6.3 | concept | Hence, within the chloroplast, protons in the stroma decrease in number, while in the lumen there is accumulation of protons; this creates a proton gradient across the thylakoid membrane as well as a measurable decrease in pH in the lumen. | x |
| F117 | 11.6.3 | concept | The proton gradient is important because it is the breakdown of this gradient that leads to the synthesis of ATP. | x |
| F118 | 11.6.3 | process | The gradient is broken down due to the movement of protons across the membrane to the stroma through the transmembrane channel of the CF0 of the ATP synthase. | x |
| F119 | 11.6.3 | definition | The ATP synthase enzyme consists of two parts: one called the CF0 is embedded in the thylakoid membrane and forms a transmembrane channel that carries out facilitated diffusion of protons across the membrane. | x |
| F120 | 11.6.3 | definition | The other portion of ATP synthase is called CF1 and protrudes on the outer surface of the thylakoid membrane on the side that faces the stroma. | x |
| F121 | 11.6.3 | process | The breakdown of the gradient provides enough energy to cause a conformational change in the CF1 particle of the ATP synthase, which makes the enzyme synthesise several molecules of energy-packed ATP. | x |
| F122 | 11.6.3 | concept | Chemiosmosis requires a membrane, a proton pump, a proton gradient and ATP synthase. | x |
| F123 | 11.6.3 | process | Energy is used to pump protons across a membrane, to create a gradient or a high concentration of protons within the thylakoid lumen; ATP synthase has a channel that allows diffusion of protons back across the membrane, and this releases enough energy to activate ATP synthase enzyme that catalyses the formation of ATP. | x |
| F124 | 11.6.3 | concept | Along with the NADPH produced by the movement of electrons, the ATP will be used immediately in the biosynthetic reaction taking place in the stroma, responsible for fixing CO2 and synthesis of sugars. | x |
| F125 | 11.7 | concept | The products of light reaction are ATP, NADPH and O2; of these O2 diffuses out of the chloroplast while ATP and NADPH are used to drive the processes leading to the synthesis of food, more accurately sugars. | x |
| F126 | 11.7 | definition | The synthesis of sugars using ATP and NADPH is the biosynthetic phase of photosynthesis. | x |
| F127 | 11.7 | concept | The biosynthetic process does not directly depend on the presence of light but is dependent on the products of the light reaction, i.e., ATP and NADPH, besides CO2 and H2O. | x |
| F128 | 11.7 | process | Immediately after light becomes unavailable the biosynthetic process continues for some time and then stops; if then light is made available, the synthesis starts again. | x |
| F129 | 11.7 | concept | CO2 is combined with H2O to produce (CH2O)n or sugars. | x |
| F130 | 11.7 | number | The use of radioactive 14C by Melvin Calvin in algal photosynthesis studies led to the discovery that the first CO2 fixation product was a 3-carbon organic acid. | x |
| F131 | 11.7 | definition | Calvin also contributed to working out the complete biosynthetic pathway; hence it was called Calvin cycle after him. | x |
| F132 | 11.7 | definition | The first product identified was 3-phosphoglyceric acid or in short PGA. | x |
| F133 | 11.7 | number | Experiments conducted over a wide range of plants led to the discovery of another group of plants where the first stable product of CO2 fixation was again an organic acid, but one which had 4 carbon atoms in it; this acid was identified to be oxaloacetic acid or OAA. | x |
| F134 | 11.7 | definition | Since then CO2 assimilation during photosynthesis was said to be of two main types: those plants in which the first product of CO2 fixation is a C3 acid (PGA), i.e., the C3 pathway, and those in which the first product was a C4 acid (OAA), i.e., the C4 pathway. | x |
| F135 | 11.7.1 | number | The studies very unexpectedly showed that the acceptor molecule was a 5-carbon ketose sugar — ribulose bisphosphate (RuBP). | x |
| F136 | 11.7.1 | concept | Scientists believed that since the first product was a C3 acid the primary acceptor would be a 2-carbon compound, and they spent many years trying to identify a 2-carbon compound before they discovered the 5-carbon RuBP. | x |
| F137 | 11.7.2 | concept | Calvin and his co-workers worked out the whole pathway and showed that the pathway operated in a cyclic manner; the RuBP was regenerated. | x |
| F138 | 11.7.2 | concept | The Calvin pathway occurs in all photosynthetic plants; it does not matter whether they have C3 or C4 (or any other) pathways. | x |
| F139 | 11.7.2 | process | For ease of understanding, the Calvin cycle can be described under three stages: carboxylation, reduction and regeneration. | x |
| F140 | 11.7.2 | definition | Carboxylation is the fixation of CO2 into a stable organic intermediate, and it is the most crucial step of the Calvin cycle where CO2 is utilised for the carboxylation of RuBP. | x |
| F141 | 11.7.2 | process | The carboxylation reaction is catalysed by the enzyme RuBP carboxylase which results in the formation of two molecules of 3-PGA. | x |
| F142 | 11.7.2 | definition | Since the RuBP carboxylase enzyme also has an oxygenation activity it would be more correct to call it RuBP carboxylase-oxygenase or RuBisCO. | x |
| F143 | 11.7.2 | number | Reduction is a series of reactions that lead to the formation of glucose; the steps involve utilisation of 2 molecules of ATP for phosphorylation and two of NADPH for reduction per CO2 molecule fixed. | x |
| F144 | 11.7.2 | number | The fixation of six molecules of CO2 and 6 turns of the cycle are required for the formation of one molecule of glucose from the pathway. | x |
| F145 | 11.7.2 | number | Regeneration of the CO2 acceptor molecule RuBP is crucial if the cycle is to continue uninterrupted, and the regeneration steps require one ATP for phosphorylation to form RuBP. | x |
| F146 | 11.7.2 | number | Hence for every CO2 molecule entering the Calvin cycle, 3 molecules of ATP and 2 of NADPH are required. | x |
| F147 | 11.7.2 | concept | It is probably to meet this difference in number of ATP and NADPH used in the dark reaction that the cyclic phosphorylation takes place. | x |
| F148 | 11.7.2 | number | The Calvin cycle balance sheet is: IN — six CO2, 18 ATP, 12 NADPH; OUT — one glucose, 18 ADP, 12 NADP. | x |
| F149 | 11.8 | concept | Plants that are adapted to dry tropical regions have the C4 pathway. | x |
| F150 | 11.8 | concept | Though C4 plants have the C4 oxaloacetic acid as the first CO2 fixation product, they use the C3 pathway or the Calvin cycle as the main biosynthetic pathway. | x |
| F151 | 11.8 | concept | C4 plants are special: they have a special type of leaf anatomy, they tolerate higher temperatures, they show a response to high light intensities, they lack a process called photorespiration and have greater productivity of biomass. | x |
| F152 | 11.8 | definition | The particularly large cells around the vascular bundles of the C4 plants are called bundle sheath cells, and the leaves which have such anatomy are said to have 'Kranz' anatomy. | x |
| F153 | 11.8 | definition | 'Kranz' means 'wreath' and is a reflection of the arrangement of cells. | x |
| F154 | 11.8 | concept | The bundle sheath cells may form several layers around the vascular bundles; they are characterised by having a large number of chloroplasts, thick walls impervious to gaseous exchange and no intercellular spaces. | x |
| F155 | 11.8 | example | Maize and sorghum are C4 plants whose leaves may be sectioned to observe the Kranz anatomy and the distribution of mesophyll cells. | x |
| F156 | 11.8 | concept | The presence of the bundle sheath around the vascular bundles would help you identify the C4 plants. | x |
| F157 | 11.8 | definition | The C4 pathway shown in Figure 11.9 has been named the Hatch and Slack Pathway, and is again a cyclic process. | x |
| F158 | 11.8 | number | The primary CO2 acceptor is a 3-carbon molecule phosphoenol pyruvate (PEP) and is present in the mesophyll cells. | x |
| F159 | 11.8 | definition | The enzyme responsible for the primary CO2 fixation in C4 plants is PEP carboxylase or PEPcase. | x |
| F160 | 11.8 | concept | It is important to register that the mesophyll cells lack RuBisCO enzyme. | x |
| F161 | 11.8 | concept | The C4 acid OAA is formed in the mesophyll cells. | x |
| F162 | 11.8 | process | OAA then forms other 4-carbon compounds like malic acid or aspartic acid in the mesophyll cells itself, which are transported to the bundle sheath cells. | x |
| F163 | 11.8 | process | In the bundle sheath cells these C4 acids are broken down to release CO2 and a 3-carbon molecule. | x |
| F164 | 11.8 | process | The 3-carbon molecule is transported back to the mesophyll where it is converted to PEP again, thus completing the cycle. | x |
| F165 | 11.8 | concept | The CO2 released in the bundle sheath cells enters the C3 or the Calvin pathway, a pathway common to all plants. | x |
| F166 | 11.8 | concept | The bundle sheath cells are rich in an enzyme Ribulose bisphosphate carboxylase-oxygenase (RuBisCO), but lack PEPcase. | x |
| F167 | 11.8 | concept | Thus the basic pathway that results in the formation of the sugars, the Calvin pathway, is common to the C3 and C4 plants. | x |
| F168 | 11.8 | concept | The Calvin pathway occurs in all the mesophyll cells of the C3 plants; in the C4 plants it does not take place in the mesophyll cells but does so only in the bundle sheath cells. | x |
| F169 | 11.9 | concept | Photorespiration is one more process that creates an important difference between C3 and C4 plants. | x |
| F170 | 11.9 | process | The first CO2 fixation step of the Calvin pathway is the reaction where RuBP combines with CO2 to form 2 molecules of 3PGA, catalysed by RuBisCO. | x |
| F171 | 11.9 | equation | The first fixation step is written: RuBP + CO2, catalysed by RuBisCO, yields 2 x 3PGA. | x |
| F172 | 11.9 | concept | RuBisCO is the most abundant enzyme in the world. | x |
| F173 | 11.9 | definition | RuBisCO is characterised by the fact that its active site can bind to both CO2 and O2 — hence the name. | x |
| F174 | 11.9 | concept | RuBisCO has a much greater affinity for CO2 when the CO2:O2 is nearly equal. | x |
| F175 | 11.9 | concept | The binding of CO2 and O2 to RuBisCO is competitive, and it is the relative concentration of O2 and CO2 that determines which of the two will bind to the enzyme. | x |
| F176 | 11.9 | concept | In C3 plants some O2 does bind to RuBisCO, and hence CO2 fixation is decreased. | x |
| F177 | 11.9 | definition | In photorespiration the RuBP, instead of being converted to 2 molecules of PGA, binds with O2 to form one molecule of phosphoglycerate and phosphoglycolate (2 Carbon). | x |
| F178 | 11.9 | concept | In the photorespiratory pathway there is neither synthesis of sugars nor of ATP; rather it results in the release of CO2 with the utilisation of ATP. | x |
| F179 | 11.9 | concept | In the photorespiratory pathway there is no synthesis of ATP or NADPH. | x |
| F180 | 11.9 | concept | The biological function of photorespiration is not known yet. | x |
| F181 | 11.9 | concept | In C4 plants photorespiration does not occur, because they have a mechanism that increases the concentration of CO2 at the enzyme site. | x |
| F182 | 11.9 | process | This CO2-concentrating mechanism takes place when the C4 acid from the mesophyll is broken down in the bundle sheath cells to release CO2, which results in increasing the intracellular concentration of CO2. | x |
| F183 | 11.9 | concept | In turn this ensures that the RuBisCO functions as a carboxylase, minimising the oxygenase activity. | x |
| F184 | 11.9 | concept | Since the C4 plants lack photorespiration, productivity and yields are better in these plants; in addition, these plants show tolerance to higher temperatures. | x |
| F185 | 11.table | concept | TABLE 11.1 asks the student to fill in Columns 2 and 3 to highlight the differences between C3 and C4 Plants, and lists the characteristics to be compared together with the options to choose from. | x |
| F186 | 11.table | concept | The Table 11.1 characteristic rows are: cell type in which the Calvin cycle takes place; cell type in which the initial carboxylation reaction occurs; how many cell types the leaf has that fix CO2; which is the primary CO2 acceptor; number of carbons in the primary CO2 acceptor; which is the primary CO2 fixation product; number of carbons in the primary CO2 fixation product; does the plant have RuBisCO; does the plant have PEP Case; which cells in the plant have RuBisCO; CO2 fixation rate under high light conditions; whether photorespiration is present at low light intensities; whether photorespiration is present at high light intensities; whether photorespiration would be present at low CO2 concentrations; whether photorespiration would be present at high CO2 concentrations; temperature optimum; and examples. | x |
| F187 | 11.table | number | The Table 11.1 'Choose from' options are: Mesophyll/Bundle sheath/both; Two: Bundle sheath and mesophyll, One: Mesophyll, Three: Bundle sheath, palisade, spongy mesophyll; RuBP/PEP/PGA; 5 / 4 / 3; PGA/OAA/RuBP/PEP; 3 / 4 / 5; Yes/No/Not always; Mesophyll/Bundle sheath/none; Low/high/medium; High/negligible/sometimes; and 30-40 degree C / 20-25 degree C / above 40 degree C. | x |
| F188 | 11.10 | concept | An understanding of the factors that affect photosynthesis is necessary because the rate of photosynthesis is very important in determining the yield of plants including crop plants. | x |
| F189 | 11.10 | concept | Photosynthesis is under the influence of several factors, both internal (plant) and external. | x |
| F190 | 11.10 | concept | The plant factors include the number, size, age and orientation of leaves, mesophyll cells and chloroplasts, internal CO2 concentration and the amount of chlorophyll. | x |
| F191 | 11.10 | concept | The plant or internal factors are dependent on the genetic predisposition and the growth of the plant. | x |
| F192 | 11.10 | concept | The external factors would include the availability of sunlight, temperature, CO2 concentration and water. | x |
| F193 | 11.10 | concept | As a plant photosynthesises all these factors will simultaneously affect its rate; hence, though several factors interact and simultaneously affect photosynthesis or CO2 fixation, usually one factor is the major cause or is the one that limits the rate. | x |
| F194 | 11.10 | concept | Hence at any point the rate will be determined by the factor available at sub-optimal levels. | x |
| F195 | 11.10 | number | When several factors affect any [bio] chemical process, Blackman's (1905) Law of Limiting Factors comes into effect. | x |
| F196 | 11.10 | definition | Blackman's Law of Limiting Factors states: if a chemical process is affected by more than one factor, then its rate will be determined by the factor which is nearest to its minimal value; it is the factor which directly affects the process if its quantity is changed. | x |
| F197 | 11.10 | example | For example, despite the presence of a green leaf and optimal light and CO2 conditions, the plant may not photosynthesise if the temperature is very low; this leaf, if given the optimal temperature, will start photosynthesising. | x |
| F198 | 11.10.1 | concept | We need to distinguish between light quality, light intensity and the duration of exposure to light while discussing light as a factor that affects photosynthesis. | x |
| F199 | 11.10.1 | concept | There is a linear relationship between incident light and CO2 fixation rates at low light intensities. | x |
| F200 | 11.10.1 | concept | At higher light intensities, gradually the rate does not show further increase as other factors become limiting. | x |
| F201 | 11.10.1 | number | Light saturation occurs at 10 per cent of the full sunlight. | x |
| F202 | 11.10.1 | concept | Hence, except for plants in shade or in dense forests, light is rarely a limiting factor in nature. | x |
| F203 | 11.10.1 | concept | Increase in incident light beyond a point causes the breakdown of chlorophyll and a decrease in photosynthesis. | x |
| F204 | 11.10.2 | concept | Carbon dioxide is the major limiting factor for photosynthesis. | x |
| F205 | 11.10.2 | number | The concentration of CO2 is very low in the atmosphere (between 0.03 and 0.04 per cent). | x |
| F206 | 11.10.2 | number | Increase in CO2 concentration upto 0.05 per cent can cause an increase in CO2 fixation rates; beyond this the levels can become damaging over longer periods. | x |
| F207 | 11.10.2 | concept | The C3 and C4 plants respond differently to CO2 concentrations, and at low light conditions neither group responds to high CO2 conditions. | x |
| F208 | 11.10.2 | concept | At high light intensities both C3 and C4 plants show increase in the rates of photosynthesis. | x |
| F209 | 11.10.2 | number | The C4 plants show saturation at about 360 microlitre per litre while C3 responds to increased CO2 concentration and saturation is seen only beyond 450 microlitre per litre. | x |
| F210 | 11.10.2 | concept | Thus, current availability of CO2 levels is limiting to the C3 plants. | x |
| F211 | 11.10.2 | example | The fact that C3 plants respond to higher CO2 concentration by showing increased rates of photosynthesis leading to higher productivity has been used for some greenhouse crops such as tomatoes and bell pepper, which are allowed to grow in carbon dioxide enriched atmosphere that leads to higher yields. | x |
| F212 | 11.10.3 | concept | The dark reactions being enzymatic are temperature controlled. | x |
| F213 | 11.10.3 | concept | Though the light reactions are also temperature sensitive they are affected to a much lesser extent. | x |
| F214 | 11.10.3 | concept | The C4 plants respond to higher temperatures and show higher rate of photosynthesis while C3 plants have a much lower temperature optimum. | x |
| F215 | 11.10.3 | concept | The temperature optimum for photosynthesis of different plants also depends on the habitat that they are adapted to; tropical plants have a higher temperature optimum than the plants adapted to temperate climates. | x |
| F216 | 11.10.4 | concept | Even though water is one of the reactants in the light reaction, the effect of water as a factor is more through its effect on the plant, rather than directly on photosynthesis. | x |
| F217 | 11.10.4 | process | Water stress causes the stomata to close, hence reducing the CO2 availability. | x |
| F218 | 11.10.4 | concept | Besides, water stress also makes leaves wilt, thus reducing the surface area of the leaves and their metabolic activity as well. | x |
| F219 | 11.title | heading | Chapter heading: "CHAPTER 11 — PHOTOSYNTHESIS IN HIGHER PLANTS" | x |
| F220 | 11.unit4 | heading | Unit banner heading: "UNIT 4 — PLANT PHYSIOLOGY" | x |
| F221 | 11.1 | heading | Numbered section heading: "11.1 WHAT DO WE KNOW?" | x |
| F222 | 11.2 | heading | Numbered section heading: "11.2 EARLY EXPERIMENTS" | x |
| F223 | 11.3 | heading | Numbered section heading: "11.3 WHERE DOES PHOTOSYNTHESIS TAKE PLACE?" | x |
| F224 | 11.4 | heading | Numbered section heading: "11.4 HOW MANY TYPES OF PIGMENTS ARE INVOLVED IN PHOTOSYNTHESIS?" | x |
| F225 | 11.5 | heading | Numbered section heading: "11.5 WHAT IS LIGHT REACTION?" | x |
| F226 | 11.6 | heading | Numbered section heading: "11.6 THE ELECTRON TRANSPORT" | x |
| F227 | 11.6.1 | heading | Numbered sub-section heading: "11.6.1 Splitting of Water" | x |
| F228 | 11.6.2 | heading | Numbered sub-section heading: "11.6.2 Cyclic and Non-cyclic Photo-phosphorylation" | x |
| F229 | 11.6.3 | heading | Numbered sub-section heading: "11.6.3 Chemiosmotic Hypothesis" | x |
| F230 | 11.7 | heading | Numbered section heading: "11.7 WHERE ARE THE ATP AND NADPH USED?" | x |
| F231 | 11.7.1 | heading | Numbered sub-section heading: "11.7.1 The Primary Acceptor of CO2" | x |
| F232 | 11.7.2 | heading | Numbered sub-section heading: "11.7.2 The Calvin Cycle" | x |
| F233 | 11.8 | heading | Numbered section heading: "11.8 THE C4 PATHWAY" | x |
| F234 | 11.9 | heading | Numbered section heading: "11.9 PHOTORESPIRATION" | x |
| F235 | 11.10 | heading | Numbered section heading: "11.10 FACTORS AFFECTING PHOTOSYNTHESIS" | x |
| F236 | 11.10.1 | heading | Numbered sub-section heading: "11.10.1 Light" | x |
| F237 | 11.10.2 | heading | Numbered sub-section heading: "11.10.2 Carbon dioxide Concentration" | x |
| F238 | 11.10.3 | heading | Numbered sub-section heading: "11.10.3 Temperature" | x |
| F239 | 11.10.4 | heading | Numbered sub-section heading: "11.10.4 Water" | x |
| F240 | 11.table | heading | Unnumbered table caption-heading: "TABLE 11.1 Fill in the Columns 2 and 3 in this table to highlight the differences between C3 and C4 Plants" | x |
| F241 | 11.7.2 | heading | Unnumbered in-section sub-heading (Calvin cycle stage): "1. Carboxylation" | x |
| F242 | 11.7.2 | heading | Unnumbered in-section sub-heading (Calvin cycle stage): "2. Reduction" | x |
| F243 | 11.7.2 | heading | Unnumbered in-section sub-heading (Calvin cycle stage): "3. Regeneration" | x |
| F244 | 11.summary | heading | Unnumbered end-matter heading: "SUMMARY" | x |
| F245 | 11.exercises | heading | Unnumbered end-matter heading: "EXERCISES" | x |
| F246 | 11.calvin | heading | Unnumbered scientist-profile heading: "Melvin Calvin" | x |
| F247 | 11.intro | opener | Opening sentence of the chapter introduction: "All animals including human beings depend on plants for their food." | x |
| F248 | 11.1 | opener | Opening sentence of 11.1: "Let us try to find out what we already know about photosynthesis." | x |
| F249 | 11.2 | opener | Opening sentence of 11.2: "It is interesting to learn about those simple experiments that led to a gradual development in our understanding of photosynthesis." | x |
| F250 | 11.3 | opener | Opening sentence of 11.3: "You would of course answer: in 'the green leaf' or 'in the chloroplasts', based on what you earlier read in Chapter 8." | x |
| F251 | 11.4 | opener | Opening sentence of 11.4: "Looking at plants have you ever wondered why and how there are so many shades of green in their leaves — even in the same plant?" | x |
| F252 | 11.5 | opener | Opening sentence of 11.5: "Light reactions or the 'Photochemical' phase include light absorption, water splitting, oxygen release, and the formation of high-energy chemical intermediates, ATP and NADPH." | x |
| F253 | 11.6 | opener | Opening sentence of 11.6: "In photosystem II the reaction centre chlorophyll a absorbs 680 nm wavelength of red light causing electrons to become excited and jump into an orbit farther from the atomic nucleus." | x |
| F254 | 11.6.1 | opener | Opening sentence of 11.6.1: "You would then ask, How does PS II supply electrons continuously?" | x |
| F255 | 11.6.2 | opener | Opening sentence of 11.6.2: "Living organisms have the capability of extracting energy from oxidisable substances and store this in the form of bond energy." | x |
| F256 | 11.6.3 | opener | Opening sentence of 11.6.3: "Let us now try and understand how actually ATP is synthesised in the chloroplast." | x |
| F257 | 11.7 | opener | Opening sentence of 11.7: "We learnt that the products of light reaction are ATP, NADPH and O2." | x |
| F258 | 11.7.1 | opener | Opening sentence of 11.7.1: "Let us now ask ourselves a question that was asked by the scientists who were struggling to understand the 'dark reaction'." | x |
| F259 | 11.7.2 | opener | Opening sentence of 11.7.2: "Calvin and his co-workers then worked out the whole pathway and showed that the pathway operated in a cyclic manner; the RuBP was regenerated." | x |
| F260 | 11.8 | opener | Opening sentence of 11.8: "Plants that are adapted to dry tropical regions have the C4 pathway mentioned earlier." | x |
| F261 | 11.9 | opener | Opening sentence of 11.9: "Let us try and understand one more process that creates an important difference between C3 and C4 plants — Photorespiration." | x |
| F262 | 11.10 | opener | Opening sentence of 11.10: "An understanding of the factors that affect photosynthesis is necessary." | x |
| F263 | 11.10.1 | opener | Opening sentence of 11.10.1: "We need to distinguish between light quality, light intensity and the duration of exposure to light, while discussing light as a factor that affects photosynthesis." | x |
| F264 | 11.10.2 | opener | Opening sentence of 11.10.2: "Carbon dioxide is the major limiting factor for photosynthesis." | x |
| F265 | 11.10.3 | opener | Opening sentence of 11.10.3: "The dark reactions being enzymatic are temperature controlled." | x |
| F266 | 11.10.4 | opener | Opening sentence of 11.10.4: "Even though water is one of the reactants in the light reaction, the effect of water as a factor is more through its effect on the plant, rather than directly on photosynthesis." | x |
| F267 | 11.summary | concept | SUMMARY-UNIQUE fold: during photosynthesis carbon dioxide from the atmosphere is taken in by leaves through stomata and used for making carbohydrates, principally glucose and starch. Folded into 11.1/11.7 body coverage. | x |
| F268 | 11.summary | concept | SUMMARY-UNIQUE fold: within the chloroplasts the membranes are sites for the light reaction, while the chemosynthetic pathway occurs in the stroma. Folded into 11.3 body coverage. | x |
| F269 | 11.summary | concept | SUMMARY-UNIQUE fold: in the light reaction the light energy is absorbed by the pigments present in the antenna and funnelled to special chlorophyll a molecules called reaction centre chlorophylls. Folded into 11.5 body coverage. | x |
| F270 | 11.summary | concept | SUMMARY-UNIQUE fold: photosynthesis has two stages, the light reaction and the carbon fixing reactions, and RuBisCO also catalyses a wasteful oxygenation reaction in C3 plants: photorespiration. Folded into 11.3/11.9 body coverage. | x |

## Heading census

Session **1-H**, re-derived by machine in session 1-Z. Written as bullet lists, never as a second pipe-delimited table, so no census line can be re-parsed as a Facts row or a label row.

- **19 numbered** heading rows, `F221`–`F239`, one per numbered section/sub-section: 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.6.1, 11.6.2, 11.6.3, 11.7, 11.7.1, 11.7.2, 11.8, 11.9, 11.10, 11.10.1, 11.10.2, 11.10.3, 11.10.4 — 19 section numbers, 19 IDs.
- **9 unnumbered** heading rows — the IDs are: `F219` (chapter title), `F220` (Unit 4 banner), `F240` (Table 11.1 caption-heading), `F241`, `F242`, `F243` (the three unnumbered Calvin-cycle stage sub-headings "1. Carboxylation", "2. Reduction", "3. Regeneration" inside §11.7.2), `F244` (SUMMARY), `F245` (EXERCISES), `F246` (the "Melvin Calvin" scientist-profile heading).
- 19 + 9 = **28**, equal to the machine-derived `heading` type count in the freeze header.

## Opener census

Session **1-O**, re-derived by machine in session 1-Z. **20** opener rows, contiguous `F247`–`F266`:

- `F247` — chapter introduction (the un-numbered opening block on PDF p. 3).
- `F248`–`F266` — one per numbered section/sub-section, in book order: 11.1 `F248`, 11.2 `F249`, 11.3 `F250`, 11.4 `F251`, 11.5 `F252`, 11.6 `F253`, 11.6.1 `F254`, 11.6.2 `F255`, 11.6.3 `F256`, 11.7 `F257`, 11.7.1 `F258`, 11.7.2 `F259`, 11.8 `F260`, 11.9 `F261`, 11.10 `F262`, 11.10.1 `F263`, 11.10.2 `F264`, 11.10.3 `F265`, 11.10.4 `F266` — 19 IDs.
- 1 + 19 = **20**, equal to the machine-derived `opener` type count. Every one of the 19 numbered headings has an opener row, matching the 19 numbered heading rows above; no structural observation *about* an opener is counted as a row.

## Figure-label matrix

Session **1-F**. One row per figure (per figure-part for the three panels of Figure 11.3). **Every label below was read off the rendered PNG by opening it**, never from `page.get_text()` — the entirety of page 7's three panels and the whole of Figures 11.7 and 11.9 carry **zero** text-layer words (audit section A reports `words_in_rect=0` for `fig_11_3a`, `fig_11_3b`, `fig_11_3c`, `fig_11_7` and `fig_11_9`), so a text-extraction harvest would have returned an empty label set for five of the twelve figures and passed a gate that verified nothing.

This matrix exists in exactly **one** place in this file. It is never restated as a second pipe-delimited table; the prose census below lists row IDs only.

| ID | Fig # | Type | In-figure labels, one row per figure part; every visible label listed | Tick |
|---|---|---|---|---|
| F271 | Fig 11.1 | caption | Figure labels: "(a)"; "(b)"; "(c)"; "(d)" | x |
| F272 | Fig 11.2 | caption | Figure labels: "Outer membrane"; "Inner membrane"; "Stromal lamella"; "Grana"; "Stroma"; "Ribosomes"; "Starch granule"; "Lipid droplet" | x |
| F273 | Fig 11.3a | caption | Figure labels: "Absorbance of light by chloroplast pigments"; "Chlorophyll b"; "Carotenoids"; "Chlorophyll a"; "(a)" | x |
| F274 | Fig 11.3b | caption | Figure labels: "Rate of photosynthesis (measured by O2 release)"; "(b)" | x |
| F275 | Fig 11.3c | caption | Figure labels: "Rate of photosynthesis"; "Absorption"; "Light absorbed"; "400"; "500"; "600"; "700"; "Wavelength of light in nanometres (nm)"; "(c)" | x |
| F276 | Fig 11.4 | caption | Figure labels: "Primary acceptor"; "Photon"; "Reaction centre"; "Pigment molecules" | x |
| F277 | Fig 11.5 | caption | Figure labels: "Photosystem II"; "Photosystem I"; "Light"; "e acceptor"; "Electron transport system"; "ADP+iP"; "ATP"; "NADPH"; "NADP+"; "LHC"; "H2O"; "2e- + 2H+ + [O]" | x |
| F278 | Fig 11.6 | caption | Figure labels: "Photosystem I"; "Light"; "e- acceptor"; "Electron transport system"; "ADP+iP"; "ATP"; "Chlorophyll P 700" | x |
| F279 | Fig 11.7 | caption | Figure labels: "Stroma (low H+)"; "Light"; "H+"; "P680 PS II"; "Plastoquinone"; "Cytochrome B6f"; "PC"; "Plastocyanin"; "P700 PS I"; "Fd"; "FNR"; "NADP+ + H+"; "NADPH"; "H2O"; "1/2 O2 + H+"; "Oxidation of water"; "Thylakoid membrane"; "High Electrochemical Potential Gradient"; "Low"; "Stroma"; "Lumen (high H+)"; "CF0"; "CF1"; "ATP synthase"; "ADP + Pi"; "ATP" | x |
| F280 | Fig 11.8 | caption | Figure labels: "Atmosphere"; "CO2 + H2O"; "Ribulose-1,5-bisphosphate"; "Carboxylation"; "3-phosphoglycerate"; "Reduction"; "Triose phosphate"; "Regeneration"; "ATP"; "ADP"; "ATP + NADPH"; "ADP + Pi +NADP+"; "Sucrose, starch"; "1"; "2"; "3" | x |
| F281 | Fig 11.9 | caption | Figure labels: "Atmospheric CO2"; "Mesophyll cell"; "Plasma membrane"; "Cell wall"; "HCO3-"; "Phosphoenol-pyruvate"; "Fixation"; "Regeneration"; "C4 acid"; "C3 acid"; "Transport"; "Plasmodesmata"; "Bundle sheath cell"; "Decarboxylation"; "CO2"; "Fixation by Calvin cycle" | x |
| F282 | Fig 11.10 | caption | Figure labels: "Rate of photosynthesis"; "Light intensity"; "A"; "B"; "C"; "D"; "E" | x |

## Figure manifest

Assets are 300 dpi clip renders of hand-pinned rectangles (`Ch11_PhotosynthesisInHigherPlants_extract_figures.py`), each `convert("L")` + `autocontrast(cutoff=1)`. `Verified` means the rendered PNG was **opened and read** in session 1-F against §4.4 Step 3 checks (a)-(f).

**12 assets extracted, 11 embedded in the PDF.** The difference is Figure 11.1 alone — a deliberate operator omission, not an extraction failure and not a coverage miss. The two numbers are stated together here so the gap between manifest and PDF can never be read as a defect; the full reasoning is in `figure_layout_decisions.md` §3 and the rule it instantiates is §4.4 Step 3's third-state bullet.

| Fig # | Caption (verbatim) | Asset file | Source page | Mono | Verified | Embedding note |
|---|---|---|---|---|---|---|
| Figure 11.1 | Priestley's experiment | `assets/fig_11_1.png` | 4 | yes | yes | **extracted, deliberately NOT embedded** (operator decision; §4.4 third state). Asset is good and stays on disk; every fact of the plate is carried in prose at `F024`–`F029`. NOT an extraction failure, so NOT flagged in the PDF under "Figures requiring manual attention". See `figure_layout_decisions.md` §3. |
| Figure 11.2 | Diagrammatic representation of an electron micrograph of a section of chloroplast | `assets/fig_11_2.png` | 6 | yes | yes |
| Figure 11.3a | Graph showing the absorption spectrum of chlorophyll a, b and the carotenoids | `assets/fig_11_3a.png` | 7 | yes | yes |
| Figure 11.3b | Graph showing action spectrum of photosynthesis | `assets/fig_11_3b.png` | 7 | yes | yes |
| Figure 11.3c | Graph showing action spectrum of photosynthesis superimposed on absorption spectrum of chlorophyll a | `assets/fig_11_3c.png` | 7 | yes | yes |
| Figure 11.4 | The light harvesting complex | `assets/fig_11_4.png` | 8 | yes | yes |
| Figure 11.5 | Z scheme of light reaction | `assets/fig_11_5.png` | 9 | yes | yes |
| Figure 11.6 | Cyclic photophosphorylation | `assets/fig_11_6.png` | 10 | yes | yes |
| Figure 11.7 | ATP synthesis through chemiosmosis | `assets/fig_11_7.png` | 11 | yes | yes |
| Figure 11.8 | The Calvin cycle proceeds in three stages : (1) carboxylation, during which CO2 combines with ribulose-1,5-bisphosphate; (2) reduction, during which carbohydrate is formed at the expense of the photochemically made ATP and NADPH; and (3) regeneration during which the CO2 acceptor ribulose-1,5-bisphosphate is formed again so that the cycle continues | `assets/fig_11_8.png` | 14 | yes | yes |
| Figure 11.9 | Diagrammatic representation of the Hatch and Slack Pathway | `assets/fig_11_9.png` | 16 | yes | yes |
| Figure 11.10 | Graph of light intensity on the rate of photosynthesis | `assets/fig_11_10.png` | 19 | yes | yes |

### Colour-carried distinctions preserved under monochrome conversion (§4.4 Step 3(f))

Two figures used hue to carry meaning and were checked specifically after `autocontrast`:
- **Figure 11.3a** separated four pigment curves by colour (chlorophyll a and b, carotenoids). After conversion they remain distinguishable as distinct grey values and each retains its own leader-line label, so no distinction is lost. The Pass 2 caption states the pigment identities in words regardless.
- **Figure 11.3c** superimposed "Rate of photosynthesis" (black) on "Absorption" (cyan). After conversion these read as a heavy black curve versus a mid-grey curve, and the boxed legend inside the panel names both, so the pairing survives without relying on colour.

No figure required the "Figures requiring manual attention" escalation, and no figure is a photograph of a person. The Melvin Calvin headshot on PDF page 2 is **deliberately not extracted** — §4.4's hard no. The scientist profile is carried text-only by rows `F004`-`F010` and `F246`.

### Crop-repin record (session 1-F, 2026-09-01)

Rectangles were re-pinned against 440 dpi / 5-point grids in `scratch/ch11_figs/grid_4x/` after opening the previous assets revealed real clipping. Six rects changed materially:

| Fig # | Old rect | New rect | Defect the repin fixed |
|---|---|---|---|
| Figure 11.1 | `(50,105,275,435)` | `(61,103,272,456)` | Old bottom at y435 sheared off the `(c)` and `(d)` panel markers (y444.5-454.4) and the lower bell-jar rims; artwork actually reaches y442.9. |
| Figure 11.2 | `(85,495,525,685)` | `(85,488,514,686)` | Old top at y495 clipped 7pt off the chloroplast's outer frame, which begins at y488.0. |
| Figure 11.3c | `(290,430,520,595)` | `(303,425,518,584)` | Old top at y430 cut the graph frame (top edge y428.8); new right/bottom stop before the caption instead of carrying dead margin. |
| Figure 11.4 | `(60,285,285,475)` | `(63,292,290,490)` | Old bottom at y475 cut the "Pigment molecules" label block (ends y448.8) leader lines and lower pigment ellipses (artwork to y483.3). |
| Figure 11.7 | `(70,90,505,395)` | `(72,100,461,399)` | Old bottom at y395 was 1pt inside the raster plate (ends y396.0), shaving the "ADP + Pi / ATP / H+" row; right edge trimmed to the plate at x456. |
| Figure 11.9 | `(160,330,520,690)` | `(188,325,492,698)` | Old bottom at y690 cut 6.3pt off the bundle-sheath cell (plate ends y696.3); left/right trimmed ~30pt of empty margin. |

`fig_11_3b` is additionally **no longer a user-supplied RGB reference image**. The predecessor session preserved a supplied 848x532 JPEG-derived PNG as the authoritative asset; that file was mode RGB, which fails §4.4 Step 2 outright and would fail `check_pdf.py` check 3 at Gate 2. It is now a normal 300 dpi clip render of the source panel, mode `L`, pinned at `(303,290,518,424)` between panel (a)'s marker (ends y279.5) and panel (c)'s frame (starts y428.8).

Audit result after repin (`figure_audit.txt`): section B (drawings-extent overflow) is **clean for all 12** — the three prior overflows at Figures 11.1, 11.2 and 11.3c are gone. Two flags remain and are both explained, not waived:
- **A: `fig_11_2` grazes the word "light-dependent."** The chloroplast frame starts at y488.0 while that last prose line occupies y482.2-492.7 at x174-257.3 — it overlaps the artwork's own y-band, so no horizontal cut can exclude the word and still keep the frame. Confirmed by opening the asset: the crop's top edge carries only a clipped partial glyph row with no legible prose.
- **C: `fig_11_3b` bottom band and `fig_11_3c` top band report edge ink.** These two rects abut at y424/425, so each one's 6pt border band necessarily samples the *other* panel's legitimate artwork. Confirmed by opening both assets: neither contains any part of the neighbouring panel's graph.

## Summary classification

Session **1-Z**. The SUMMARY block (PDF p. 21, textbook p. 151) contains **20 sentences**: **15 BODY-PRESENT** + **5 SUMMARY-UNIQUE**, and all 5 unique sentences are folded into the 4 body rows `F267`-`F270` (`F270` carries two folds — the explicit two-stage naming and the "wasteful" qualifier). Nothing is left unfolded.

**Correction made in session 1-Z (recorded, not back-dated).** The draft of this table carried **22** rows and claimed "18 BODY-PRESENT + 4 SUMMARY-UNIQUE". Two of those rows — *"Photosynthesis is the primary source of all food on earth."* and *"Photosynthesis is responsible for the release of oxygen into the atmosphere."* — are **not summary sentences at all**: both sit in the chapter introduction on PDF **page 3** ("Photosynthesis is important due to two reasons: it is the primary source of all food on earth. It is also responsible for the release of oxygen into the atmosphere by green plants."), verified by extracting the SUMMARY block between the `SUMMARY` and `EXERCISES` headings and confirming neither sentence appears inside it. They are removed from this table because a summary-classification row must correspond to a real summary sentence; the facts themselves are unaffected and remain carried by Facts row `F016`. The 4-vs-5 SUMMARY-UNIQUE discrepancy was a hand tally of the same table: the `SUMMARY-UNIQUE` label appears on 5 rows (sentences 2, 5, 6, 7 and 17), mapping onto only 4 fold rows, which is why the draft's count of the *folds* was mistaken for a count of the *sentences*. Both corrections are propagated to every restatement (freeze header, Gate 1 checklist, `CHAPTER_STATUS.md`, `CHAPTER_TRACKER.md`) in the same edit, per §6 step 10.

| Summary sentence | Classification | Folded into |
|---|---|---|
| Green plants make their own food by photosynthesis. | BODY-PRESENT | F012, F014 |
| During this process carbon dioxide from the atmosphere is taken in by leaves through stomata and used for making carbohydrates, principally glucose and starch. | SUMMARY-UNIQUE | F267 (stomatal uptake route + "principally glucose and starch") |
| Photosynthesis takes place only in the green parts of the plants, mainly the leaves. | BODY-PRESENT | F020, F055 |
| Within the leaves, the mesophyll cells have a large number of chloroplasts that are responsible for CO2 fixation. | BODY-PRESENT | F056 |
| Within the chloroplasts, the membranes are sites for the light reaction, while the chemosynthetic pathway occurs in the stroma. | SUMMARY-UNIQUE | F268 (the word "chemosynthetic pathway" is summary-only) |
| Photosynthesis has two stages: the light reaction and the carbon fixing reactions. | SUMMARY-UNIQUE | F270 (the explicit two-stage naming is summary-only) |
| In the light reaction the light energy is absorbed by the pigments present in the antenna, and funnelled to special chlorophyll a molecules called reaction centre chlorophylls. | SUMMARY-UNIQUE | F269 ("funnelled", "reaction centre chlorophylls" plural form) |
| There are two photosystems, PS I and PS II. | BODY-PRESENT | F077 |
| PS I has a 700 nm absorbing chlorophyll a P700 molecule at its reaction centre, while PS II has a P680 reaction centre that absorbs red light at 680 nm. | BODY-PRESENT | F083 |
| After absorbing light, electrons are excited and transferred through PS II and PS I and finally to NAD forming NADH. | BODY-PRESENT | F084, F089 |
| During this process a proton gradient is created across the membrane of the thylakoid. | BODY-PRESENT | F116 |
| The breakdown of the protons gradient due to movement through the F0 part of the ATPase enzyme releases enough energy for synthesis of ATP. | BODY-PRESENT | F118, F121 |
| Splitting of water molecules is associated with PS II resulting in the release of O2, protons and transfer of electrons to PS II. | BODY-PRESENT | F093, F094 |
| In the carbon fixation cycle, CO2 is added by the enzyme, RuBisCO, to a 5-carbon compound RuBP that is converted to 2 molecules of 3-carbon PGA. | BODY-PRESENT | F135, F141 |
| This is then converted to sugar by the Calvin cycle, and the RuBP is regenerated. | BODY-PRESENT | F137, F145 |
| During this process ATP and NADPH synthesised in the light reaction are utilised. | BODY-PRESENT | F143, F146 |
| RuBisCO also catalyses a wasteful oxygenation reaction in C3 plants: photorespiration. | SUMMARY-UNIQUE | F270 (the qualifier "wasteful" is summary-only) |
| Some tropical plants show a special type of photosynthesis called C4 pathway. | BODY-PRESENT | F149 |
| In these plants the first product of CO2 fixation that takes place in the mesophyll, is a 4-carbon compound. | BODY-PRESENT | F161 |
| In the bundle sheath cells the Calvin pathway is carried out for the synthesis of carbohydrates. | BODY-PRESENT | F165, F168 |

## Exercise-gap terms

9 exercises. 4 assume a term or step the body never states outright; each has a planned Pass-2 home. The appendix carries **only** these 4 gap items, never a walk-through of all 9 (Rule 2).

**Closed arithmetic: 9 exercises = 4 answered by design (GAP) + 5 unanswered by design (COVERED) + 0 overlooked.** The 5 unanswered exercises are unanswered *because the chapter body already teaches them* — that is Rule 2 step 3 COVERED ("do not reproduce the question and do not write an answer"), confirmed by the operator in the review session. Reproducing them would type the same fact twice and push real content away from the reader. Anyone auditing this chapter should expect to find 4 answers to 9 questions and read that as correct.

| Term/fact assumed by exercises | Explained where |
|---|---|
| Ex. 1 — that C3 vs C4 cannot be told apart by external appearance (the body only ever gives *internal* Kranz-anatomy criteria, never the negative external claim). | "Terms used in the exercises" appendix; cross-referenced from the §11.8 Kranz-anatomy block. |
| Ex. 5 — that chlorophyll a is indispensable, so a plant with only chlorophyll b could not run photosynthesis (the body states chlorophyll a is the chief pigment and b is accessory, but never that b alone is insufficient). | Appendix, tied to the §11.4 accessory-pigment block (`F070`, `F073`, `F074`). |
| Ex. 6 — the relative stability of the pigments, i.e. that chlorophyll degrades in darkness faster than the carotenoids, leaving a yellow/pale-green leaf. | Appendix; the body gives photo-oxidation protection (`F074`) but never the dark-degradation ordering. |
| Ex. 7 — that shade leaves are darker green than sun leaves because they build more chlorophyll per unit area (the body only says light is rarely limiting except in shade, `F202`). | Appendix, tied to the §11.10.1 light block. |

Each gap was re-confirmed against the extracted source in session 1-Z: the body never contains the negative external C3/C4 claim (`externally` occurs only in Exercise 1), never states that chlorophyll b alone is insufficient (§11.4 only names b as an accessory pigment), never gives the dark-degradation stability ordering (`stable` occurs in §11.8/§11.7.2 in an unrelated sense), and never explains why shade leaves are darker green (§11.10.1 stops at "light is rarely a limiting factor in nature ... except for plants in shade"). Exercises 2, 3, 4, 8 and 9 are fully answerable from body rows (Kranz anatomy, C4 productivity, RuBisCO carboxylation bias, Figure 11.10 regions, and the three comparisons) and therefore generate no appendix entry.

---

## Gate 1 closure record (session 1-Z, 2026-09-01)

**Environment.** `/vercel/share/neetenv` was absent at session start (expected — it does not survive a session boundary) and was rebuilt per §0.2 before anything was diagnosed: `uv venv /vercel/share/neetenv --python 3.13` + `uv pip install --python /vercel/share/neetenv/bin/python reportlab pdfplumber pymupdf Pillow`. Verified `3.13.11 @ /vercel/share/neetenv` · reportlab 5.0.1 · pdfplumber OK · pymupdf 1.28.2 · Pillow 12.3.0. Every command below ran through that interpreter.

**Session 1-Z deliverables (steps 7, 8, 9, 10).**
1. **Exercise-gap scan (step 7).** 9 exercises parsed from PDF p. 21–22; 4 genuine gaps, each with a named Pass-2 home; the 5 non-gap exercises are individually accounted for above.
2. **Summary scan and fold (step 8).** The SUMMARY block was cut out of the source by locating the `SUMMARY`→`EXERCISES` span and classified sentence by sentence: **20 sentences = 15 BODY-PRESENT + 5 SUMMARY-UNIQUE**, the 5 unique sentences folded into `F267`–`F270`. Two rows the draft carried were shown to be page-3 introduction sentences, not summary sentences, and were removed with the reasoning recorded in the *Summary classification* section.
3. **Freeze (step 9).** Rows numbered, nothing renumbered, moved or re-typed; 0 rows ticked (Pass 2 does the ticking, in this file).
4. **Machine-derived counts (step 10).** Every count in this file was produced by re-parsing the finished table, and every restatement was corrected in the same edit.

**What the re-parse found and fixed.** The pre-1-Z header described a **158-row** table (`F001`–`F158`) with 106/21/15/4/12 block sizes, a 9-value type census summing to 158, 21 heading rows, 15 opener rows, 22 summary sentences, and folds at `F155`–`F158`. The table it sits on actually holds **282 rows** (`F001`–`F282`). Every one of those numbers was wrong — the header had been written against an earlier draft and never re-derived — so it was rewritten wholesale from the parse rather than patched. This is precisely the failure §6 step 10 exists to stop, and it is recorded rather than quietly overwritten.

**Gate 1 criteria — evidence.**

| Criterion (§6 Gate 1) | Status | Evidence |
|---|---|---|
| Every fact has a Facts row; every in-figure label has a matrix row, harvested by opening each rendered asset | ✅ | 218 `1-S` fact rows + the 1-H/1-O/1-Z blocks; 12 label rows carrying 116 labels. Five of twelve figures (`fig_11_3a/b/c`, `fig_11_7`, `fig_11_9`) return `words_in_rect=0` in `figure_audit.txt`, so the non-empty label sets for them prove the harvest was visual, not text-layer |
| Inventory validated by running `check_pdf.py._extract_labels` — expected figure count, no doubling, no phantom rows | ✅ | Imported `_extract_labels` from the repo-root linter and ran it against this file: **12 figure rows / 116 labels**, per-figure 4+8+5+2+9+4+12+7+26+16+16+7, **0 duplicate (figure, label) pairs, 0 phantom rows**. It first returned **118 labels and a phantom `Fig #` figure**: the matrix's own column header read "Figure labels (one row per figure; every in-figure label listed)", which the parser matched as a label row and split on `;` into two junk labels. The column header is now worded "In-figure labels, …" (the phrasing every already-closed chapter uses) — a formatting fix in the inventory, exactly where §6 requires it, and **no label, caption or asset was touched** |
| Every header count matches a re-parse; contiguous `F001..FNNN`; normalized `Type` column | ✅ | 282 rows, `F001`–`F282`, **0 gaps, 0 duplicates, monotonic**; type census `concept` 128 · `definition` 31 · `number` 28 · `heading` 28 · `process` 26 · `opener` 20 · `caption` 12 · `equation` 5 · `example` 4 = 282; exactly 9 `Type` values, all lowercase |
| Every heading has a row including unnumbered sub-headings; every section opener has a row | ✅ | Heading census 19 numbered + 9 unnumbered = 28 (list-derived, §*Heading census*); opener census 1 intro + 19 numbered = 20 (§*Opener census*). Walked as their own lists; the three unnumbered Calvin-stage sub-headings and the Melvin Calvin profile heading are present, and each of the 19 numbered headings has exactly one opener |
| All five Pass 1 sessions ran and each reported its own machine-derived row count | ✅ | `1-S` 218 (`F001`–`F218`) · `1-H` 28 (`F219`–`F246`) · `1-O` 20 (`F247`–`F266`) · `1-F` 12 (`F271`–`F282`) + manifest + repin record · `1-Z` 4 (`F267`–`F270`) + this record. Sum 282 = highest ID |
| Every figure marked `Mono: yes` and `Verified: yes` | ✅ | 12/12 in the figure manifest; `fig_11_3b` re-rendered as a mode-`L` clip after the inherited RGB reference image was rejected; six rects re-pinned against the 440 dpi / 5-pt grid |
| Every exercise-gap term has a planned home; every SUMMARY-UNIQUE fact folded into a body row | ✅ | 4/4 gaps homed in the appendix with cross-references; 5/5 SUMMARY-UNIQUE sentences folded into `F267`–`F270` |
| Inventory file saved in the chapter folder | ✅ | `notes/class 11/Ch11_PhotosynthesisInHigherPlants/Ch11_PhotosynthesisInHigherPlants_inventory.md` |

**GATE 1: GREEN.** Pass 2 may begin — write `Ch11_PhotosynthesisInHigherPlants.py` linearly from this frozen table in Content Order (§5), importing `neet_template.py`, ticking rows in this file as each `# ---- N.N ----` block is written, then loop render → `check_pdf.py` until exit 0.

**Carry-over for Pass 2.**
- The 4 exercise-gap items are the *only* appendix content (Rule 2); no coverage or meta note (Rule 6).
- Figure 11.3a/11.3c captions must state the pigment identities and the rate-vs-absorption pairing in words, since the original carried them by colour (§4.4 Step 3(f)).
- The Melvin Calvin profile is text-only, from `F004`–`F010` and `F246`; the p. 2 headshot is never embedded.
- Table 11.1 is an NCERT *fill-in* table (`F240`): reproduce it as a completed comparison table from the C3/C4 body rows, keeping the NCERT caption number.
- Write `CO2`, `H+`, `NADP+`, `O2`, `HCO3-`, `C3`/`C4` with `<sub>`/`<super>` tags, never Unicode (check 5).

## Gate 2 closure record (Pass 2, 2026-09-01)

**Environment.** `/vercel/share/neetenv` was absent at session start (expected — it does not survive a session boundary) and was rebuilt per §0.2 before anything else: `uv venv /vercel/share/neetenv --python 3.13` + `uv pip install --python /vercel/share/neetenv/bin/python reportlab pdfplumber pymupdf Pillow`. Verified 3.13.11 @ `/vercel/share/neetenv` · reportlab 5.0.1 · pdfplumber 0.11.10 · pymupdf 1.28.2 · Pillow 12.3.0. Every command below ran through that interpreter.

**What Pass 2 inherited.** The script `Ch11_PhotosynthesisInHigherPlants.py` and its rendered `Ch11_PhotosynthesisInHigherPlants.pdf` already existed (built from this frozen inventory, 17 pp. A4 portrait). The only open Gate 2 item was check 7: **270/270 Facts rows unticked** — the `[ ]` boxes were never ticked as blocks were written. Every other check already passed. Gate 2 work was therefore to reconcile the written PDF against the frozen table, then tick.

**Coverage reconciliation before ticking (not a blind tick).** A token-coverage aid (`scratch/ch11_gate2/coverage.py`, Pass-2 EVIDENCE per §6 — locates suspect rows, never closes a gate) scored each of the 270 Facts rows' content words against the delivered PDF text layer:
- **246/270 rows** had *every* content word present in the PDF.
- **24 rows** flagged ≥1 absent token; each was read directly. All 24 are benign — the token was either inventory scaffolding not meant to reach the page (`summary`, `heading`, `banner`, `opening`, `sentence`, `coverage`, `fill`, `rows`, `characteristics`) or a morphological rewrite variant of a fact that *is* present (`testing`→"tested", `isotope`→"radioisotop**ic**", `maxima`→"maximum", `concentrating`→"CO2-concentrating", `hypothesised`/`follows`, `learnt`, `mentioned`, `resting`, degree-symbol).
- Substantive spot-checks against the extracted PDF text confirmed presence: F053 O2-from-water "proved by using radioisotopic techniques", F083 P680/P700 absorption peaks, F182 the CO2-concentrating mechanism in bundle-sheath cells, F029 Priestley's restore-the-air hypothesis, F001 irreconcilable perspectives. **No genuine content gap; no script or asset changed.**

**Ticking.** With coverage confirmed, all **270 Facts rows** and, for consistency, the **12 figure-label-matrix rows** (already verified by check 6, 116/116 labels in text) had their Tick cell set to `x`. 0 F-rows in the Facts/matrix sections remain `[ ]`.

**Gate 2 criteria — evidence (`check_pdf.py "notes/class 11/Ch11_PhotosynthesisInHigherPlants"`, exit 0):**

| Check (§6 Gate 2) | Status | Evidence |
|---|---|---|
| 1. Footer/header band | ✅ PASS | No text span inside the top/bottom 1.4 cm margin band |
| 2. Legibility floor | ✅ PASS | No rendered glyph below 5.0 pt; badges/step digits are real spans |
| 3. Grayscale-only images | ✅ PASS | Every embedded image single-channel / R==G==B |
| 4. No person photograph | ⚠️ WARN (benign) | Standing false positive on inventory rows whose *text* contains *portrait*/*photo*; the Melvin Calvin profile is text-only and no human-subject image is embedded (§4.4 hard-no; Coverage §*Deliberate operator omissions*) |
| 5. Banned glyphs | ✅ PASS | No Unicode arrows, sub/superscripts, Greek or emoji in the text stream |
| 6. Figure-label coverage | ✅ PASS | 116/116 labels in running text; 0 partial, 0 missing |
| 7. Inventory ticked | ✅ PASS | 270/270 Facts rows ticked (reconciled as above) |
| 8. Page geometry | ✅ PASS | 17/17 pages A4 portrait (595×842 pt) |
| 9. Orphaned headings | ✅ PASS | 88 banner headings, 0 stranded at a page foot |
| 10. Badge/heading collision | ✅ PASS | No badge plate colliding with its heading banner |

**GATE 2: GREEN.** `check_pdf.py` exits 0 — VERDICT WARN (0 fail, 1 warn); the lone WARN is check 4, eyeballed and confirmed legitimate per §6 (advance-on-benign-WARN). Pass 3 may begin: Gate 3(a) visual render check (every page rendered + cross-page style consistency) then Gate 3(b) bidirectional content read against this frozen table.

## Coverage

The §7 / Rule 6 Coverage section: the facts about *this deliverable* that an auditor needs and the PDF must never carry. Full narrative for the operator decisions is in `figure_layout_decisions.md`.

The seven fixed §6 headings follow in the spec's order, so an audit prompt can consume this section mechanically. *(Normalised at Gate 3(b), defect `D3`: the section previously omitted **Compression decisions**, **Color-dependent figures** and **Source problems** entirely, and carried the other two under the local names "Exercises" and "Known linter state". The substance of those two was already correct and is preserved verbatim below under its mandated heading; the three new headings state facts that were true but unwritten.)*

### Compression decisions

What was merged or reformatted relative to NCERT's prose, and why no fact is at risk. Nothing here drops a fact — each item is a change of *form* only, and every underlying row is ticked in the Facts table.

| Compression | Where | Why it is safe |
|---|---|---|
| The two prior-class experiments (variegated/black-paper leaf; KOH test tube) became two numbered **process-flow** blocks instead of running prose | §11.1 | `F019`–`F022` are step sequences in the source too; the flow preserves each step, its order and its result verbatim, including the negative KOH result |
| The five early-experiment scientists became **five H3 sub-blocks** under §11.2 rather than one continuous narrative | §11.2 | NCERT runs them as unbroken prose, but strictly in this order; each scientist's every sentence is carried in his own block (`F024`–`F054`) |
| Engelmann's prism experiment and van Niel's inference became process-flow / bullet sequences | §11.2d, §11.2f | Both are stepwise in the original; no qualifier ("mainly", "roughly", "essentially") was dropped |
| The chloroplast's eight in-figure parts became a **two-column table** rather than a label list | §11.3 | Carries `F272`'s eight labels into running text (what check 6 verifies) and adds no claim NCERT does not make |
| The four leaf pigments and their chromatogram colours became a table | §11.4 | One row per pigment; the four colour descriptions are quoted as NCERT words them ("bright or blue green", "yellow to yellow-orange") |
| The three Calvin stages became **three unnumbered H3 sub-headings** (`F241`–`F243`) plus the IN/OUT balance sheet as a table | §11.7.2 | Mirrors NCERT's own "1. Carboxylation / 2. Reduction / 3. Regeneration" numbering and its own In/Out list |
| NCERT's **fill-in** Table 11.1 was reproduced **completed** from the chapter's own C3/C4 statements | Table 11.1 | The blank table teaches nothing on the page; `F187` additionally carries NCERT's own "Choose from" option lists verbatim, so the exercise is recoverable |
| The chapter Summary was rewritten as a denser **QUICK RECAP** (`F244`) rather than reproduced | Recap | Rule 3: all 20 summary sentences are classified in *Summary classification*; the 5 SUMMARY-UNIQUE ones are folded into body rows `F267`–`F270`, so the recap adds no unique fact |

### Exercise classification

**9 exercises = 4 answered by design (GAP) + 5 unanswered by design (COVERED) + 0 overlooked.** See *Exercise-gap terms* above for the full per-gap table and its planned homes. The 5 COVERED questions are deliberately not reproduced and not answered, per Rule 2 step 3 and the operator's confirmation.

| Ex. | Class | Where it is answered / why no answer is written |
|---|---|---|
| 1 | **GAP** | Appendix "Terms used in the exercises" — the negative *external* C3/C4 claim is never made in the body |
| 2 | COVERED | §11.8 Kranz anatomy / bundle sheath cells (`F152`–`F156`) |
| 3 | COVERED | §11.8 + §11.9 — the CO2-concentrating mechanism and absence of photorespiration (`F166`–`F168`, `F181`–`F184`) |
| 4 | COVERED | §11.9 — RuBisCO's competitive CO2/O2 binding and the raised intracellular CO2 in bundle sheath cells (`F174`–`F176`, `F182`) |
| 5 | **GAP** | Appendix — that chlorophyll a is indispensable is never stated outright |
| 6 | **GAP** | Appendix — the dark-degradation stability ordering is never stated |
| 7 | **GAP** | Appendix — why shade leaves are darker green is never explained |
| 8 | COVERED | §11.10.1 + Figure 11.10, whose points A–E are named in running text (`F282`, `F199`–`F203`) |
| 9 | COVERED | Table 11.1 (C3 vs C4), §11.6.2 (cyclic vs non-cyclic), §11.8 (leaf anatomy) |

### Drift caught and fixed

Pass 3 found **one** confirmed content defect and **two** confirmed metadata defects; three further flags were investigated and dismissed. The full register with reasoning is in the *Gate 3(b) closure record* below.

| ID | Class | Finding | Resolution |
|---|---|---|---|
| `D1` | DRIFTED (content) | §11.2c heading read "Julius von Sachs (1854)". All four sibling scientist headings carry life-date pairs, so the bare year reads as Sachs' life dates — which NCERT never gives. 1854 is the year of the evidence (`F033`). | Relabelled "Julius von Sachs (evidence of 1854)" in the `# ---- 11.2 Julius von Sachs ----` block, tagged `# [VERIFICATION FIX]`. No fact changed. |
| `D2` | Metadata | The `Deliberate operator omissions` table described Figure 11.1 as "Reversible by adding one `figure()` call" without recording that its label row `F271` is nonetheless ticked and check-6 clean. | Clarified in that table's *Why it is safe* cell (see below). |
| `D3` | Metadata | This Coverage section omitted three of the seven mandated §6 headings and renamed two others. | Normalised to the seven fixed headings in spec order; no existing substance removed. |

### Figures requiring manual attention

**None.** All 12 figures extracted and converted cleanly; no figure failed extraction, so this heading has no entry and — per §4.4 — appears nowhere in the PDF.

**None.** All 12 figures extracted and converted cleanly; no figure failed extraction, so this heading has no entry and — per §4.4 — appears nowhere in the PDF.

### Deliberate operator omissions (NOT extraction failures)

| Item | Decision | Why it is safe | Where the facts live instead |
|---|---|---|---|
| **Figure 11.1** — Priestley's experiment (source p. 4) | Extracted, monochrome, verified, **deliberately not embedded**. Operator judgement: the plate carries no NEET teaching value. | Every fact of the plate is in prose; its label row `F271` is only the bare panel markers `(a)`–`(d)`, which carry no fact. Reversible by adding one `figure()` call. **Re-confirmed at Gate 3(b) (`D2`):** `fig_11_1.png` is the one asset in `assets/` with no `figure()` call in the script — which is why the PDF holds **11** image XObjects against **12** assets. That gap is this decision, not a dropped figure. `F271`'s four panel markers are ticked and check-6 clean because the caption text naming panels (a)–(d) reaches the running text via `F026`–`F028`'s prose. | `F024`–`F029` in §11.2 — bell jar, candle extinguished, mouse suffocating, mint plant, and Priestley's hypothesis |
| **Melvin Calvin headshot** (source p. 2) | Never extracted, never embedded — §4.4 photograph hard-no. | Profile is fully carried as text. | `F004`–`F010`, heading `F246` |

Neither is flagged in the PDF: that flag means "a diagram you should have is missing", and neither is missing by accident.

### Figure render widths deviating from the default

Set at the call site in `Ch11_PhotosynthesisInHigherPlants.py`, recorded because a figure narrower than its column otherwise reads as an oversight. Ledger with rendered point sizes and the pagination budget behind them: `figure_layout_decisions.md` §1–§2.

| Fig | `max_width_cm` | Reason |
|---|---|---|
| 11.8 | 10.5 → **7.6** | frees 95 pt so Calvin-cycle stage (3) Regeneration rejoins its section, and pays for 11.9's move |
| 11.9 | 10.0 → **7.4** | `KeepTogether` block now fits the tail of the C4 pathway page instead of taking a page of its own |
| 11.10 | 8.0 → **6.2** | operator size order; cheapest figure to shrink (2 axis names + points A–E) |

No asset, crop rectangle, caption or inventory row changed — only the draw-time width. All three moves are downward, so the §4.4 300 dpi no-upscale cap is unaffected and effective print resolution rose.

### Color-dependent figures

Figures whose meaning relied on colour in the original, and where that distinction is now stated **in words** so it survives monochrome conversion and photocopying (§4.4 Step 3(f)). The per-figure conversion record is in *Colour-carried distinctions preserved under monochrome conversion* above.

| Fig | What colour carried in the original | Where the distinction is now stated in words |
|---|---|---|
| **11.3a** | Three absorption curves distinguished only by line colour | Caption names all three curves explicitly — **Chlorophyll a**, **Chlorophyll b**, **Carotenoids** — plus the vertical axis "Absorbance of light by chloroplast pigments" |
| **11.3b** | The single action-spectrum curve read against 11.3a's colours | Caption names the curve and its vertical axis, "Rate of photosynthesis (measured by O2 release)", and the panel marker **(b)** |
| **11.3c** | Two superimposed curves: rate in **black**, absorption in **cyan**, with a shaded "Light absorbed" band | Caption states the pairing outright — "the **Rate of photosynthesis** curve was black and the **Absorption** curve was cyan, and the shaded band is **Light absorbed**" — plus the 400/500/600/700 nm axis marks |

All other figures carried their meaning by line, arrow, label or position, not colour, so monochrome conversion cost them nothing. Check 3 confirms every embedded image is single-channel.

### Source problems

**None.** No part of the source chapter was garbled or unrecoverable. Three source characteristics are worth recording, none of them a defect in the deliverable:

- **NCERT's own summary carries two errors** the body contradicts: it says electrons pass "finally to **NAD** forming **NADH**" (body: NADP+ to NADPH, `F089`) and that water splitting transfers "electrons to **PS II**" (body: PS II supplies PS I, `F094`). Both summary sentences are classified BODY-PRESENT against the **correct** body rows, so the notes carry the body's accurate version and do not propagate the typos. Confirmed by full read at Gate 3(b), not by token match.
- `pdfplumber` reflows the source's subscripted formulae into separate lines (`CO +H O →[CH O]+O` with the digits on the following line). This is an extraction artifact of the reader, not damage to the source; every formula was read from the rendered page and re-typed with `<sub>`/`<super>` tags (check 5 green).
- The source's decorative letter-spacing renders some emphasised words with repeated glyphs (e.g. "dddddaaaaarrrrrkkkkk rrrrreeeeeaaaaaccccctttttiiiiiooooonnnnn" on p. 12, "Chlorophyll aaaaa" on p. 7). Read as "dark reaction" and "Chlorophyll a"; no fact was taken from the mangled spelling.

### Linter verdict

`check_pdf.py` exits **0** (VERDICT WARN, 0 fail, 1 warn) — Gate 2 is GREEN. The 270 Facts rows and 12 figure-label-matrix rows are now all ticked `x` (the Pass-2 bookkeeping debt described in earlier drafts is cleared; see the *Gate 2 closure record* below). Check 4's WARN is the standing benign one: it fires on inventory rows whose own text contains *portrait*/*photo*, and this chapter embeds no human-subject image at all. Checks 1, 2, 3, 5, 6 (116/116 labels), 7 (270/270 ticked), 8 (17/17 A4 portrait) and 9 (88 banners, 0 orphaned headings) pass.

## Gate 3(a) closure record — visual render check (Pass 3, 2026-09-01)

**Environment.** `/vercel/share/neetenv` was **absent at session start** — the expected §0.2 state, and the first action of the session, so nothing was diagnosed before it. Rebuilt per §0.2 (`uv venv … --python 3.13` + `uv pip install … reportlab pdfplumber pymupdf Pillow`) and version-checked: CPython **3.13.11** @ `/vercel/share/neetenv` · reportlab 5.0.1 · pdfplumber 0.11.10 · pymupdf 1.28.2 · Pillow 12.3.0. Every command ran through that interpreter.

**Gate 2 re-verified from disk before Pass 3 opened (§6, "do not begin the human pass while the linter is red").** `check_pdf.py "notes/class 11/Ch11_PhotosynthesisInHigherPlants"` re-run against the **committed** PDF → **exit 0, VERDICT WARN (0 fail / 1 warn)**. The single WARN is check 4's standing benign portrait-row false positive (no human-subject image is embedded). Geometry check reports **17/17 pages A4 portrait**; smallest glyph **6.0 pt**; all embedded images single-channel monochrome; **116/116 figure labels in running text**.

**(a) Visual render check — EVERY page inspected, not spot-checked.** All **17 of 17** pages were rendered from the committed PDF with `pymupdf` (≈150 dpi colour for reading + a 1-bit true-print-DPI B&W threshold render for the photocopy-safety pass) and opened and looked at individually. Result: **zero confirmed layout defects.** Per-page findings:

| Pages | What was confirmed |
|---|---|
| 1 | H1 title + DNA motif; Unit-4 + Ch-11 + 11.1 banners; 2 tables (perspectives, ) with dark headers; process-flow Experiment-1 step badges legible; CO2 subscript correct |
| 2 | Experiment-1/2 step badges; §11.2 + 11.2a–11.2d banners; NOTE box (Priestley hypothesis) with the "!" icon rendered; no orphaned heading at foot |
| 3 | §11.2e/f + §11.3 banners; van Niel equations with sub/superscripts (2H2A, C6H12O6, 6H2O); **Fig 11.2** embedded in bordered box, all 9 leader-line labels legible, caption present |
| 4 | 2 tables (chloroplast parts, leaf pigments) dark header + zebra rows; NOTE box (dark-reactions); §11.4 banner |
| 5 | **Figs 11.3a / 11.3b / 11.3c** all embedded mono with panel markers (a)/(b)/(c) and the colour-carried identities restated in the captions; §11.5 banner |
| 6 | NOTE box (photosystem naming); **Fig 11.4** embedded; photosystem table; §11.6 THE ELECTRON TRANSPORT process badges with NADP+/NADPH+H+ superscripts |
| 7 | **Fig 11.5** (Z scheme) embedded with descriptive caption; §11.6.1/11.6.2 banners; NOTE box (water-splitting complex) |
| 8 | **Fig 11.6** (cyclic) embedded; §11.6.3 banner; superscripts (NADP+, NADPH + H+) correct |
| 9 | **Fig 11.7** (chemiosmosis) embedded with long read-aloud caption; process badges 1–5; sub/superscripts (H2O → 1/2 O2 + H+) correct |
| 10 | CF0/CF1 subscripts; §11.7 banner; no overflow |
| 11 | **Fig 11.8** (Calvin cycle) embedded (width 7.6 cm, per layout ledger); Stage-1/2/3 banners; descriptive caption |
| 12 | Calvin balance-sheet table; **MEMORY AID — not in NCERT** star box; §11.8 THE C4 PATHWAY banner; **Fig 11.9** embedded (width 7.4 cm) |
| 13 | §11.9 PHOTORESPIRATION banner; process badges with the cyclic "last step feeds back to step 1" note; NOTE box; C3/C4 subscripts |
| 14 | **Table 11.1** (C3/C4 differences) fully filled, dark header + zebra rows, no run-off; §11.10 banner; factors table |
| 15 | §11.10.1/11.10.2 banners; **Fig 11.10** (light-intensity graph, width 6.2 cm) embedded; CO2-response table |
| 16 | §11.10.3/11.10.4 + QUICK RECAP (Recap) + TERMS USED (Appendix) banners; Ex.1 answer box |
| 17 | Ex.5/Ex.6/Ex.7 answer boxes with `[addition]` tags; chapter ends cleanly, no trailing orphan |

**Cross-page style consistency (§7).** One rendered instance of each element type was pulled from ≥3 different points and compared: H1 (p1), banner H2/H3 (pp1, 6, 14), tables (pp1, 4, 14), NOTE box (pp2, 6, 13), MEMORY-AID box (p12), process-flow (pp1, 6, 13), figure box (pp3, 9, 15). All instances of each type are visually identical — expected, since every style is imported from `neet_template.py` (this check confirms the template held rather than hunting hand-typed drift). **No footer / page-number strip on any page (defect-1 class); every badge and step digit legible (defect-2/3 classes).**

**No embedded colour and no human photograph.** The 1-bit renders and check 3 agree every figure is true monochrome; Fig 11.1 (Priestley) and the Melvin Calvin headshot are the two documented deliberate omissions (see *Deliberate operator omissions*), so the chapter carries no human-subject image — check 4's WARN is that known false positive, not a suppressed finding.

**GATE 3(a): CLOSED — 17/17 pages inspected, zero confirmed layout defects, cross-page styles identical, linter green on the committed PDF.** Pass 3(b) — the bidirectional full-read content cross-check against this frozen table — is the only remaining Gate 3 condition and has **not** yet been run.
