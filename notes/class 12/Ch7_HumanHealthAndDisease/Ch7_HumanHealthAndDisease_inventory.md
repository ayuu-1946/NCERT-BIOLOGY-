# Frozen Inventory — Chapter 7: Human Health and Disease (Class XII)

**Status: PASS 1 INCOMPLETE — Gate 1 NOT met.**

This file currently holds the output of **session 1-F only** (figure extraction).
It is a partial inventory, deliberately published in this state so that the work
already done is durable and auditable. Four of the five mandatory Pass 1 sessions
have **not** run. See "Session log" and "What is missing" below before using this
file for anything.

Source PDF: `Chapter/class 12/Chapter 7 - Human Health and Disease.pdf` (22 pages).

---

## Session log — Pass 1

| Session | Scope | State |
|---|---|---|
| **1-F** | Figures: census, rect pinning, extraction, three-part audit, label matrix | **complete** (2026-08-23) |
| 1-S | Source read + Facts inventory (`F###` rows) | **not started** |
| 1-H | Structural census (heading sweep) | **not started** |
| 1-O | Section-opener census | **not started** |
| 1-Z | Independent re-verification / count derivation | **not started** |

Session 1-F was executed across two sittings. The first (previous chat) pinned the
rects, ran the audit and reviewed a contact sheet, but **ran out of budget before
writing any inventory file** and did not commit its audit script. The second
(this session) rebuilt the environment, re-derived every machine claim from
scratch, re-opened all 11 assets, and wrote this file.

### What is missing

`§6` requires Pass 1 to span **five** sessions, each with its own machine-derived
row count. Gate 1 cannot be claimed until 1-S, 1-H, 1-O and 1-Z have each run as
their own session. Specifically absent from this file:

- the **Facts table** (`F###` rows) — the substance of the chapter
- **Header counts** and the step-10 **count derivation**
- **Structural census** (headings) and **opener census**
- **Summary classification** (BODY-PRESENT vs SUMMARY-UNIQUE)
- **Exercise-gap terms**
- any **Gate 1 checklist**

Do not treat the figure work below as evidence that the chapter is inventoried.

---

## Re-derivation notes (this session)

Per `§6`, a handoff's findings are **claims to re-derive**, not facts to inherit.
Everything below was re-measured in this session against the source PDF; nothing
was copied forward on trust. Three discrepancies with the inherited account were
found and are recorded honestly rather than smoothed over:

1. **The extract script's own comment for fig 7.10 quotes stale overflow numbers.**
   It records "Check B still reports L2.8/T14.3/R7.6". Against the *current*
   (re-pinned) rect the same underlying gradient extents give **L4.8/T9.3/R11.6**.
   The old figures were measured against the *pre-re-pin* rect `(348, 224, 460, 366)`.
   Same shapes, same conclusion — the comment's arithmetic is just one revision behind.
2. **`fig_7_5` overflows left by 24.8 pt** under a raster-extent check. The
   inherited audit table never recorded this. Verified harmless this session: the
   silhouette raster's bbox starts at x=29.2 but its **first inked column is
   x=57.9** (300 dpi probe, thr 205), and the rect's left edge at x=54 clears
   real ink by 4.1 pt. It is the raster's own white margin.
3. **`fig_7_8` and `fig_7_11` had NO working mechanical edge check.** Both plates
   are rendered as thousands of sub-pixel scanline tiles (~6 x 0.2 pt each), so
   check B finds 0 drawings and check B2's 3 pt size floor discards every tile.
   Both reported clean only because they were **vacuous**. A new **check B3**
   (tile union, no size floor) was written to give them real coverage; both pass.

A fourth item is not a discrepancy but is worth stating: the previous session's
reproducibility claim was re-tested properly. Re-running `extract_figures.py`
regenerates all 11 PNGs **byte-identical** to the committed ones (verified via
`git status` on the assets directory, after a first attempt at this check was
caught being vacuous — a `sed` had stripped the md5 hashes and compared only
filenames).

---

## Facts

Rows `F001`-`F276` were added by **session 1-S** (steps 1, 2, 3). Scope discipline
per `§6`: this session read the prose only. It deliberately created **no**
`heading` rows and **no** `opener` rows — those are the sole deliverables of
sessions 1-H and 1-O, and absorbing them here is the exact failure mechanism `§6`
names. Consequently **every section's first sentence is intentionally absent from
the rows below**; that is not an omission to be repaired by editing this table, it
is 1-O's work.

Wording is verbatim NCERT, quoted. Where a row merges two adjacent source
sentences, both are quoted inside the one row because they state one fact
together. Figure **captions** are not duplicated here — they are inventoried
verbatim in the Figure manifest below, which is the single place they live.

`figure-text` rows carry the in-plate process sentences of figs 7.1 and 7.6 and
the unquoted marker sets of fig 7.4. These are carry-over item 1 from session
1-F, the item that session flagged as "the single biggest carry-over from 1-F and
must not be lost." They are recorded as ordinary Facts rows and **not** as
`Figure labels:` rows, so `_extract_labels` cannot see them — they are prose
obligations, not label-coverage obligations.

| ID | Section | Type | Exact original wording | Ticked |
|----|---------|------|------------------------|--------|
| F001 | intro | fact | "It was thought that persons with 'blackbile' belonged to hot personality and would have fevers. This idea was arrived at by pure reflective thought." | |
| F002 | intro | fact | "The discovery of blood circulation by William Harvey using experimental method" | |
| F003 | intro | fact | "the demonstration of normal body temperature in persons with blackbile using thermometer disproved the 'good humor' hypothesis of health" | |
| F004 | intro | mechanism | "biology stated that mind influences, through neural system and endocrine system, our immune system and that our immune system maintains our health. Hence, mind and mental state can affect our health." | |
| F005 | intro | fact | "health is affected by – (i) genetic disorders – deficiencies with which a child is born and deficiencies/defects which the child inherits from parents from birth; (ii) infections and (iii) life style including food and water we take, rest and exercise we give to our bodies, habits that we have or lack etc." | |
| F006 | intro | term | "Health does not simply mean 'absence of disease' or 'physical fitness'. It could be defined as a state of complete physical, mental and social well-being." | |
| F007 | intro | fact | "When people are healthy, they are more efficient at work. This increases productivity and brings economic prosperity." | |
| F008 | intro | fact | "Health also increases longevity of people and reduces infant and maternal mortality." | |
| F009 | intro | prevention | "Balanced diet, personal hygiene and regular exercise are very important to maintain good health." | |
| F010 | intro | fact | "Yoga has been practised since time immemorial to achieve physical and mental health." | |
| F011 | intro | prevention | "Awareness about diseases and their effect on different bodily functions, vaccination (immunisation) against infectious diseases, proper disposal of wastes, control of vectors and maintenance of hygiene in food and water resources are necessary for achieving good health." | |
| F012 | intro | term | "When the functioning of one or more organs or systems of the body is adversely affected, characterised by appearance of various signs and symptoms, we say that we are not healthy, i.e., we have a disease." | |
| F013 | intro | term | "Diseases can be broadly grouped into infectious and non-infectious." | |
| F014 | intro | term | "Diseases which are easily transmitted from one person to another, are called infectious diseases." | |
| F015 | intro | fact | "Infectious diseases are very common and every one of us suffers from these at sometime or other. Some of the infectious diseases like AIDS are fatal." | |
| F016 | intro | fact | "Among non-infectious diseases, cancer is the major cause of death. Drug and alcohol abuse also affect our health adversely." | |
| F017 | 7.1 | term | "Such disease-causing organisms are called pathogens." | |
| F018 | 7.1 | fact | "Most parasites are therefore pathogens as they cause harm to the host by living in (or on) them." | |
| F019 | 7.1 | process | "The pathogens can enter our body by various means, multiply and interfere with normal vital activities, resulting in morphological and functional damage." | |
| F020 | 7.1 | fact | "Pathogens have to adapt to life within the environment of the host. For example, the pathogens that enter the gut must know a way of surviving in the stomach at low pH and resisting the various digestive enzymes." | |
| F021 | 7.1 | example | "Salmonella typhi is a pathogenic bacterium which causes typhoid fever in human beings." | |
| F022 | 7.1 | transmission | "These pathogens generally enter the small intestine through food and water contaminated with them and migrate to other organs through blood." | |
| F023 | 7.1 | symptom | "Sustained high fever (39° to 40°C), weakness, stomach pain, constipation, headache and loss of appetite are some of the common symptoms of this disease." | |
| F024 | 7.1 | fact | "Intestinal perforation and death may occur in severe cases." | |
| F025 | 7.1 | diagnosis | "Typhoid fever could be confirmed by Widal test" | |
| F026 | 7.1 | example | "A classic case in medicine, that of Mary Mallon nicknamed Typhoid Mary, is worth mentioning here. She was a cook by profession and was a typhoid carrier who continued to spread typhoid for several years through the food she prepared." | |
| F027 | 7.1 | example | "Bacteria like Streptococcus pneumoniae and Haemophilus influenzae are responsible for the disease pneumonia in humans which infects the alveoli (air filled sacs) of the lungs." | |
| F028 | 7.1 | mechanism | "As a result of the infection, the alveoli get filled with fluid leading to severe problems in respiration." | |
| F029 | 7.1 | symptom | "The symptoms of pneumonia include fever, chills, cough and headache. In severe cases, the lips and finger nails may turn gray to bluish in colour." | |
| F030 | 7.1 | transmission | "A healthy person acquires the infection by inhaling the droplets/aerosols released by an infected person or even by sharing glasses and utensils with an infected person." | |
| F031 | 7.1 | example | "Dysentery, plague, diphtheria, etc., are some of the other bacterial diseases in man." | |
| F032 | 7.1 | example | "Rhino viruses represent one such group of viruses which cause one of the most infectious human ailments – the common cold. They infect the nose and respiratory passage but not the lungs." | |
| F033 | 7.1 | symptom | "The common cold is characterised by nasal congestion and discharge, sore throat, hoarseness, cough, headache, tiredness, etc., which usually last for 3-7 days." | |
| F034 | 7.1 | transmission | "Droplets resulting from cough or sneezes of an infected person are either inhaled directly or transmitted through contaminated objects such as pens, books, cups, doorknobs, computer keyboard or mouse, etc., and cause infection in a healthy person." | |
| F035 | 7.1 | example | "Plasmodium, a tiny protozoan is responsible for this disease." | |
| F036 | 7.1 | example | "Different species of Plasmodium (P. vivax, P. malaria and P. falciparum) are responsible for different types of malaria." | |
| F037 | 7.1 | fact | "Of these, malignant malaria caused by Plasmodium falciparum is the most serious one and can even be fatal." | |
| F038 | 7.1 | process | "Plasmodium enters the human body as sporozoites (infectious form) through the bite of infected female Anopheles mosquito." | |
| F039 | 7.1 | process | "The parasites initially multiply within the liver cells and then attack the red blood cells (RBCs) resulting in their rupture." | |
| F040 | 7.1 | mechanism | "The rupture of RBCs is associated with release of a toxic substance, haemozoin, which is responsible for the chill and high fever recurring every three to four days." | |
| F041 | 7.1 | process | "When a female Anopheles mosquito bites an infected person, these parasites enter the mosquito's body and undergo further development." | |
| F042 | 7.1 | process | "The parasites multiply within them to form sporozoites that are stored in their salivary glands. When these mosquitoes bite a human, the sporozoites are introduced into his/her body, thereby initiating the events mentioned above." | |
| F043 | 7.1 | fact | "the malarial parasite requires two hosts – human and mosquitoes – to complete its life cycle" | |
| F044 | 7.1 | term | "the female Anopheles mosquito is the vector (transmitting agent) too" | |
| F045 | 7.1 | figure-text | In-plate process sentence, Figure 7.1: "When the mosquito bites another human, sporozoites are injected with bite." | |
| F046 | 7.1 | figure-text | In-plate process sentence, Figure 7.1: "Parasite (sporozoites) reach the liver through blood" | |
| F047 | 7.1 | figure-text | In-plate process sentence, Figure 7.1: "The parasite reproduces asexually in liver cells, bursting the cell and releasing into the blood." | |
| F048 | 7.1 | figure-text | In-plate process sentence, Figure 7.1: "Parasites reproduce asexually in red blood cells, bursting the red blood cells and causing cycles of fever and other symptoms. Released parasites infect new red blood cells." | |
| F049 | 7.1 | figure-text | In-plate process sentence, Figure 7.1: "Sexual stages (gametocytes) develop in red blood cells." | |
| F050 | 7.1 | figure-text | In-plate process sentence, Figure 7.1: "Female mosquito takes up gametocytes with blood meal." | |
| F051 | 7.1 | figure-text | In-plate process sentence, Figure 7.1: "Fertilization and development take place in the mosquito's gut." | |
| F052 | 7.1 | figure-text | In-plate process sentence, Figure 7.1: "Mature infective stages (sporozoites) escape from gut and migrate to the mosquito salivary glands." | |
| F053 | 7.1 | example | "Entamoeba histolytica is a protozoan parasite in the large intestine of human which causes amoebiasis (amoebic dysentery)." | |
| F054 | 7.1 | symptom | "Symptoms of this disease include constipation, abdominal pain and cramps, stools with excess mucous and blood clots." | |
| F055 | 7.1 | transmission | "Houseflies act as mechanical carriers and serve to transmit the parasite from faeces of infected person to food and food products, thereby contaminating them. Drinking water and food contaminated by the faecal matter are the main source of infection." | |
| F056 | 7.1 | example | "Ascaris, the common round worm and Wuchereria, the filarial worm, are some of the helminths which are known to be pathogenic to man." | |
| F057 | 7.1 | example | "Ascaris, an intestinal parasite causes ascariasis." | |
| F058 | 7.1 | symptom | "Symptoms of these disease include internal bleeding, muscular pain, fever, anemia and blockage of the intestinal passage." | |
| F059 | 7.1 | transmission | "The eggs of the parasite are excreted along with the faeces of infected persons which contaminate soil, water, plants, etc. A healthy person acquires this infection through contaminated water, vegetables, fruits, etc." | |
| F060 | 7.1 | example | "Wuchereria (W. bancrofti and W. malayi), the filarial worms cause a slowly developing chronic inflammation of the organs in which they live for many years, usually the lymphatic vessels of the lower limbs and the disease is called elephantiasis or filariasis" | |
| F061 | 7.1 | symptom | "The genital organs are also often affected, resulting in gross deformities." | |
| F062 | 7.1 | transmission | "The pathogens are transmitted to a healthy person through the bite by the female mosquito vectors." | |
| F063 | 7.1 | example | "Many fungi belonging to the genera Microsporum, Trichophyton and Epidermophyton are responsible for ringworms which is one of the most common infectious diseases in man." | |
| F064 | 7.1 | symptom | "Appearance of dry, scaly lesions on various parts of the body such as skin, nails and scalp are the main symptoms of the disease. These lesions are accompanied by intense itching." | |
| F065 | 7.1 | fact | "Heat and moisture help these fungi to grow, which makes them thrive in skin folds such as those in the groin or between the toes." | |
| F066 | 7.1 | transmission | "Ringworms are generally acquired from soil or by using towels, clothes or even the comb of infected individuals." | |
| F067 | 7.1 | prevention | "Measures for personal hygiene include keeping the body clean; consumption of clean drinking water, food, vegetables, fruits, etc." | |
| F068 | 7.1 | prevention | "Public hygiene includes proper disposal of waste and excreta; periodic cleaning and disinfection of water reservoirs, pools, cesspools and tanks and observing standard practices of hygiene in public catering." | |
| F069 | 7.1 | prevention | "These measures are particularly essential where the infectious agents are transmitted through food and water such as typhoid, amoebiasis and ascariasis." | |
| F070 | 7.1 | prevention | "In cases of air-borne diseases such as pneumonia and common cold, in addition to the above measures, close contact with the infected persons or their belongings should be avoided." | |
| F071 | 7.1 | prevention | "For diseases such as malaria and filariasis that are transmitted through insect vectors, the most important measure is to control or eliminate the vectors and their breeding places." | |
| F072 | 7.1 | prevention | "This can be achieved by avoiding stagnation of water in and around residential areas, regular cleaning of household coolers, use of mosquito nets, introducing fishes like Gambusia in ponds that feed on mosquito larvae, spraying of insecticides in ditches, drainage areas and swamps, etc." | |
| F073 | 7.1 | prevention | "In addition, doors and windows should be provided with wire mesh to prevent the entry of mosquitoes." | |
| F074 | 7.1 | fact | "Such precautions have become more important especially in the light of recent widespread incidences of the vector-borne (Aedes mosquitoes) diseases like dengue and chikungunya in many parts of India." | |
| F075 | 7.1 | fact | "The use of vaccines and immunisation programmes have enabled us to completely eradicate a deadly disease like smallpox." | |
| F076 | 7.1 | fact | "A large number of other infectious diseases like polio, diphtheria, pneumonia and tetanus have been controlled to a large extent by the use of vaccines." | |
| F077 | 7.1 | fact | "Biotechnology (about which you will read more in Chapter 10) is at the verge of making available newer and safer vaccines." | |
| F078 | 7.1 | fact | "Discovery of antibiotics and various other drugs has also enabled us to effectively treat infectious diseases." | |
| F079 | 7.2 | fact | "only a few of these exposures result in disease. Why? This is due to the fact that the body is able to defend itself from most of these foreign agents." | |
| F080 | 7.2 | term | "This overall ability of the host to fight the disease-causing organisms, conferred by the immune system is called immunity." | |
| F081 | 7.2 | term | "Immunity is of two types: (i) Innate immunity and (ii) Acquired immunity." | |
| F082 | 7.2.1 | fact | "This is accomplished by providing different types of barriers to the entry of the foreign agents into our body." | |
| F083 | 7.2.1 | number | "Innate immunity consist of four types of barriers." | |
| F084 | 7.2.1 | term | "Physical barriers : Skin on our body is the main barrier which prevents entry of the micro-organisms. Mucus coating of the epithelium lining the respiratory, gastrointestinal and urogenital tracts also help in trapping microbes entering our body." | |
| F085 | 7.2.1 | term | "Physiological barriers : Acid in the stomach, saliva in the mouth, tears from eyes–all prevent microbial growth." | |
| F086 | 7.2.1 | term | "Cellular barriers : Certain types of leukocytes (WBC) of our body like polymorpho-nuclear leukocytes (PMNL-neutrophils) and monocytes and natural killer (type of lymphocytes) in the blood as well as macrophages in tissues can phagocytose and destroy microbes." | |
| F087 | 7.2.1 | term | "Cytokine barriers : Virus-infected cells secrete proteins called interferons which protect non-infected cells from further viral infection." | |
| F088 | 7.2.2 | term | "It is characterised by memory." | |
| F089 | 7.2.2 | process | "when our body encounters a pathogen for the first time it produces a response called primary response which is of low intensity" | |
| F090 | 7.2.2 | process | "Subsequent encounter with the same pathogen elicits a highly intensified secondary or anamnestic response. This is ascribed to the fact that our body appears to have memory of the first encounter." | |
| F091 | 7.2.2 | fact | "The primary and secondary immune responses are carried out with the help of two special types of lymphocytes present in our blood, i.e., B-lymphocytes and T-lymphocytes." | |
| F092 | 7.2.2 | term | "The B-lymphocytes produce an army of proteins in response to pathogens into our blood to fight with them. These proteins are called antibodies." | |
| F093 | 7.2.2 | fact | "The T-cells themselves do not secrete antibodies but help B cells to produce them." | |
| F094 | 7.2.2 | structure | "Each antibody molecule has four peptide chains, two small called light chains and two longer called heavy chains. Hence, an antibody is represented as H2L2." | |
| F095 | 7.2.2 | example | "Different types of antibodies are produced in our body. IgA, IgM, IgE, IgG are some of them." | |
| F096 | 7.2.2 | term | "Because these antibodies are found in the blood, the response is also called as humoral immune response. This is one of the two types of our acquired immune response – antibody mediated." | |
| F097 | 7.2.2 | term | "The second type is called cell-mediated immune response or cell-mediated immunity (CMI). The T-lymphocytes mediate CMI." | |
| F098 | 7.2.2 | fact | "Very often, when some human organs like heart, eye, liver, kidney fail to function satisfactorily, transplantation is the only remedy to enable the patient to live a normal life." | |
| F099 | 7.2.2 | fact | "Grafts from just any source – an animal, another primate, or any human beings cannot be made since the grafts would be rejected sooner or later." | |
| F100 | 7.2.2 | fact | "Tissue matching, blood group matching are essential before undertaking any graft/transplant and even after this the patient has to take immuno–suppresants all his/her life." | |
| F101 | 7.2.2 | mechanism | "The body is able to differentiate 'self' and 'nonself' and the cell-mediated immune response is responsible for the graft rejection." | |
| F102 | 7.2.2 | figure-text | In-plate markers, Figure 7.4: "N" at the amino terminus and "C" at each carboxyl terminus of the peptide chains. Single characters, deliberately excluded from the label matrix by session 1-F; the antibody passage must name the amino (N) and carboxyl (C) termini in running text. | |
| F103 | 7.2.2 | figure-text | In-plate markers, Figure 7.4: the "S-S" disulfide bridges joining the two heavy chains to each other and each light chain to its heavy chain. Excluded from the label matrix by session 1-F; the antibody passage must state that the chains are held together by disulfide bonds. | |
| F104 | 7.2.3 | term | "This type of immunity is called active immunity." | |
| F105 | 7.2.3 | fact | "Active immunity is slow and takes time to give its full effective response." | |
| F106 | 7.2.3 | fact | "Injecting the microbes deliberately during immunisation or infectious organisms gaining access into body during natural infection induce active immunity." | |
| F107 | 7.2.3 | term | "When ready-made antibodies are directly given to protect the body against foreign agents, it is called passive immunity." | |
| F108 | 7.2.3 | example | "The yellowish fluid colostrum secreted by mother during the initial days of lactation has abundant antibodies (IgA) to protect the infant." | |
| F109 | 7.2.3 | example | "The foetus also receives some antibodies from their mother, through the placenta during pregnancy. These are some examples of passive immunity." | |
| F110 | 7.2.4 | process | "In vaccination, a preparation of antigenic proteins of pathogen or inactivated/weakened pathogen (vaccine) are introduced into the body." | |
| F111 | 7.2.4 | mechanism | "The antibodies produced in the body against these antigens would neutralise the pathogenic agents during actual infection." | |
| F112 | 7.2.4 | mechanism | "The vaccines also generate memory – B and T-cells that recognise the pathogen quickly on subsequent exposure and overwhelm the invaders with a massive production of antibodies." | |
| F113 | 7.2.4 | example | "If a person is infected with some deadly microbes to which quick immune response is required as in tetanus, we need to directly inject the preformed antibodies, or antitoxin (a preparation containing antibodies to the toxin)." | |
| F114 | 7.2.4 | example | "Even in cases of snakebites, the injection which is given to the patients, contain preformed antibodies against the snake venom. This type of immunisation is called passive immunisation." | |
| F115 | 7.2.4 | fact | "Recombinant DNA technology has allowed the production of antigenic polypeptides of pathogen in bacteria or yeast." | |
| F116 | 7.2.4 | example | "Vaccines produced using this approach allow large scale production and hence greater availability for immunisation, e.g., hepatitis B vaccine produced from yeast." | |
| F117 | 7.2.5 | fact | "Some of us are sensitive to some particles in the environment. The above-mentioned reaction could be because of allergy to pollen, mites, etc., which are different in different places." | |
| F118 | 7.2.5 | term | "The exaggerated response of the immune system to certain antigens present in the environment is called allergy." | |
| F119 | 7.2.5 | term | "The substances to which such an immune response is produced are called allergens." | |
| F120 | 7.2.5 | fact | "The antibodies produced to these are of IgE type." | |
| F121 | 7.2.5 | example | "Common examples of allergens are mites in dust, pollens, animal dander, etc." | |
| F122 | 7.2.5 | symptom | "Symptoms of allergic reactions include sneezing, watery eyes, running nose and difficulty in breathing." | |
| F123 | 7.2.5 | mechanism | "Allergy is due to the release of chemicals like histamine and serotonin from the mast cells." | |
| F124 | 7.2.5 | diagnosis | "For determining the cause of allergy, the patient is exposed to or injected with very small doses of possible allergens, and the reactions studied." | |
| F125 | 7.2.5 | treatment | "The use of drugs like anti-histamine, adrenalin and steroids quickly reduce the symptoms of allergy." | |
| F126 | 7.2.5 | fact | "modern-day life style has resulted in lowering of immunity and more sensitivity to allergens – more and more children in metro cities of India suffer from allergies and asthma due to sensitivity to the environment. This could be because of the protected environment provided early in life." | |
| F127 | 7.2.6 | fact | "While we still do not understand the basis of this, two corollaries of this ability have to be understood." | |
| F128 | 7.2.6 | fact | "One, higher vertebrates can distinguish foreign molecules as well as foreign organisms. Most of the experimental immunology deals with this aspect." | |
| F129 | 7.2.6 | term | "Two, sometimes, due to genetic and other unknown reasons, the body attacks self-cells. This results in damage to the body and is called auto-immune disease." | |
| F130 | 7.2.6 | example | "Rheumatoid arthritis which affects many people in our society is an auto-immune disease." | |
| F131 | 7.2.7 | fact | "immune system is unique in the sense that it recognises foreign antigens, responds to these and remembers them." | |
| F132 | 7.2.7 | fact | "The immune system also plays an important role in allergic reactions, auto-immune diseases and organ transplantation." | |
| F133 | 7.2.7 | term | "Lymphoid organs: These are the organs where origin and/or maturation and proliferation of lymphocytes occur." | |
| F134 | 7.2.7 | term | "The primary lymphoid organs are bone marrow and thymus where immature lymphocytes differentiate into antigen-sensitive lymphocytes." | |
| F135 | 7.2.7 | term | "After maturation the lymphocytes migrate to secondary lymphoid organs like spleen, lymph nodes, tonsils, Peyer's patches of small intestine and appendix." | |
| F136 | 7.2.7 | fact | "The secondary lymphoid organs provide the sites for interaction of lymphocytes with the antigen, which then proliferate to become effector cells." | |
| F137 | 7.2.7 | fact | "The bone marrow is the main lymphoid organ where all blood cells including lymphocytes are produced." | |
| F138 | 7.2.7 | structure | "The thymus is a lobed organ located near the heart and beneath the breastbone. The thymus is quite large at the time of birth but keeps reducing in size with age and by the time puberty is attained it reduces to a very small size." | |
| F139 | 7.2.7 | fact | "Both bone-marrow and thymus provide micro-environments for the development and maturation of T-lymphocytes." | |
| F140 | 7.2.7 | structure | "The spleen is a large bean-shaped organ. It mainly contains lymphocytes and phagocytes. It acts as a filter of the blood by trapping blood-borne micro-organisms. Spleen also has a large reservoir of erythrocytes." | |
| F141 | 7.2.7 | structure | "The lymph nodes are small solid structures located at different points along the lymphatic system." | |
| F142 | 7.2.7 | mechanism | "Lymph nodes serve to trap the micro-organisms or other antigens, which happen to get into the lymph and tissue fluid. Antigens trapped in the lymph nodes are responsible for the activation of lymphocytes present there and cause the immune response." | |
| F143 | 7.2.7 | term | "There is lymphoid tissue also located within the lining of the major tracts (respiratory, digestive and urogenital tracts) called mucosa-associated lymphoid tissue (MALT)." | |
| F144 | 7.2.7 | number | "It constitutes about 50 per cent of the lymphoid tissue in human body." | |
| F145 | 7.3 | term | "This means deficiency of immune system, acquired during the lifetime of an individual indicating that it is not a congenital disease. 'Syndrome' means a group of symptoms." | |
| F146 | 7.3 | number | "AIDS was first reported in 1981 and in the last twenty-five years or so, it has spread all over the world killing more than 25 million persons." | |
| F147 | 7.3 | term | "AIDS is caused by the Human Immuno deficiency Virus (HIV), a member of a group of viruses called retrovirus, which have an envelope enclosing the RNA genome." | |
| F148 | 7.3 | transmission | "Transmission of HIV-infection generally occurs by (a) sexual contact with infected person, (b) by transfusion of contaminated blood and blood products, (c) by sharing infected needles as in the case of intravenous drug abusers and (d) from infected mother to her child through placenta." | |
| F149 | 7.3 | fact | "people who are at high risk of getting this infection includes - individuals who have multiple sexual partners, drug addicts who take drugs intravenously, individuals who require repeated blood transfusions and children born to an HIV infected mother." | |
| F150 | 7.3 | fact | "HIV/AIDS is not spread by mere touch or physical contact; it spreads only through body fluids." | |
| F151 | 7.3 | fact | "It is, hence, imperative, for the physical and psychological well-being, that the HIV/AIDS infected persons are not isolated from family and society." | |
| F152 | 7.3 | number | "There is always a time-lag between the infection and appearance of AIDS symptoms. This period may vary from a few months to many years (usually 5-10 years)." | |
| F153 | 7.3 | process | "After getting into the body of the person, the virus enters into macrophages where RNA genome of the virus replicates to form viral DNA with the help of the enzyme reverse transcriptase." | |
| F154 | 7.3 | process | "This viral DNA gets incorporated into host cell's DNA and directs the infected cells to produce virus particles." | |
| F155 | 7.3 | fact | "The macrophages continue to produce virus and in this way acts like a HIV factory." | |
| F156 | 7.3 | process | "Simultaneously, HIV enters into helper T-lymphocytes (TH), replicates and produce progeny viruses. The progeny viruses released in the blood attack other helper T-lymphocytes. This is repeated leading to a progressive decrease in the number of helper T-lymphocytes in the body of the infected person." | |
| F157 | 7.3 | symptom | "During this period, the person suffers from bouts of fever, diarrhoea and weight loss." | |
| F158 | 7.3 | mechanism | "Due to decrease in the number of helper T lymphocytes, the person starts suffering from infections that could have been otherwise overcome such as those due to bacteria especially Mycobacterium, viruses, fungi and even parasites like Toxoplasma." | |
| F159 | 7.3 | fact | "The patient becomes so immuno-deficient that he/she is unable to protect himself/herself against these infections." | |
| F160 | 7.3 | diagnosis | "A widely used diagnostic test for AIDS is enzyme linked immuno-sorbent assay (ELISA)." | |
| F161 | 7.3 | treatment | "Treatment of AIDS with anti-retroviral drugs is only partially effective. They can only prolong the life of the patient but cannot prevent death, which is inevitable." | |
| F162 | 7.3 | prevention | "As AIDS has no cure, prevention is the best option." | |
| F163 | 7.3 | fact | "HIV infection, more often, spreads due to conscious behaviour patterns and is not something that happens inadvertently, like pneumonia or typhoid." | |
| F164 | 7.3 | fact | "infection in blood transfusion patients, new-borns (from mother) etc., may take place due to poor monitoring. The only excuse may be ignorance and it has been rightly said – 'don't die of ignorance'." | |
| F165 | 7.3 | fact | "In our country the National AIDS Control Organisation (NACO) and other non-governmental organisation (NGOs) are doing a lot to educate people about AIDS. WHO has started a number of programmes to prevent the spreading of HIV infection." | |
| F166 | 7.3 | prevention | "Making blood (from blood banks) safe from HIV, ensuring the use of only disposable needles and syringes in public and private hospitals and clinics, free distribution of condoms, controlling drug abuse, advocating safe sex and promoting regular check-ups for HIV in susceptible populations, are some such steps taken up." | |
| F167 | 7.3 | fact | "Infection with HIV or having AIDS is something that should not be hidden – since then, the infection may spread to many more people. HIV/AIDS-infected people need help and sympathy instead of being shunned by society." | |
| F168 | 7.3 | fact | "Unless society recognises it as a problem to be dealt with in a collective manner – the chances of wider spread of the disease increase manifold. It is a malady that can only be tackled, by the society and medical fraternity acting together, to prevent the spread of the disease." | |
| F169 | 7.3 | figure-text | In-plate process sentence, Figure 7.6: "Virus infects normal cell" | |
| F170 | 7.3 | figure-text | In-plate process sentence, Figure 7.6: "Viral RNA is introduced into cell" | |
| F171 | 7.3 | figure-text | In-plate process sentence, Figure 7.6: "Viral DNA is produced by reverse transcriptase" | |
| F172 | 7.3 | figure-text | In-plate process sentence, Figure 7.6: "Viral DNA incorporates into host genome" | |
| F173 | 7.3 | figure-text | In-plate process sentence, Figure 7.6: "New viral RNA is produced by the infected cell" | |
| F174 | 7.3 | figure-text | In-plate process sentence, Figure 7.6: "New viruses are produced" | |
| F175 | 7.3 | figure-text | In-plate process sentence, Figure 7.6: "New viruses can infect other cells" | |
| F176 | 7.3 | figure-text | In-plate note, Figure 7.6: "NOTE: Infected cell can survive while viruses are being replicated and released" | |
| F177 | 7.4 | number | "More than a million Indians suffer from cancer and a large number of them die from it annually." | |
| F178 | 7.4 | fact | "The mechanisms that underlie development of cancer or oncogenic transformation of cells, its treatment and control have been some of the most intense areas of research in biology and medicine." | |
| F179 | 7.4 | fact | "In our body, cell growth and differentiation is highly controlled and regulated. In cancer cells, there is breakdown of these regulatory mechanisms." | |
| F180 | 7.4 | term | "Normal cells show a property called contact inhibition by virtue of which contact with other cells inhibits their uncontrolled growth. Cancer cells appears to have lost this property." | |
| F181 | 7.4 | term | "cancerous cells just continue to divide giving rise to masses of cells called tumors." | |
| F182 | 7.4 | term | "Tumors are of two types: benign and malignant." | |
| F183 | 7.4 | term | "Benign tumors normally remain confined to their original location and do not spread to other parts of the body and cause little damage." | |
| F184 | 7.4 | term | "The malignant tumors, on the other hand are a mass of proliferating cells called neoplastic or tumor cells. These cells grow very rapidly, invading and damaging the surrounding normal tissues." | |
| F185 | 7.4 | mechanism | "As these cells actively divide and grow they also starve the normal cells by competing for vital nutrients." | |
| F186 | 7.4 | term | "Cells sloughed from such tumors reach distant sites through blood, and wherever they get lodged in the body, they start a new tumor there. This property called metastasis is the most feared property of malignant tumors." | |
| F187 | 7.4 | cause | "Transformation of normal cells into cancerous neoplastic cells may be induced by physical, chemical or biological agents. These agents are called carcinogens." | |
| F188 | 7.4 | cause | "Ionising radiations like X-rays and gamma rays and non-ionizing radiations like UV cause DNA damage leading to neoplastic transformation." | |
| F189 | 7.4 | cause | "The chemical carcinogens present in tobacco smoke have been identified as a major cause of lung cancer." | |
| F190 | 7.4 | term | "Cancer causing viruses called oncogenic viruses have genes called viral oncogenes." | |
| F191 | 7.4 | term | "several genes called cellular oncogenes (c-onc) or proto oncogenes have been identified in normal cells which, when activated under certain conditions, could lead to oncogenic transformation of the cells." | |
| F192 | 7.4 | fact | "Early detection of cancers is essential as it allows the disease to be treated successfully in many cases." | |
| F193 | 7.4 | diagnosis | "Cancer detection is based on biopsy and histopathological studies of the tissue and blood and bone marrow tests for increased cell counts in the case of leukemias." | |
| F194 | 7.4 | diagnosis | "In biopsy, a piece of the suspected tissue cut into thin sections is stained and examined under microscope (histopathological studies) by a pathologist." | |
| F195 | 7.4 | diagnosis | "Techniques like radiography (use of X-rays), CT (computed tomography) and MRI (magnetic resonance imaging) are very useful to detect cancers of the internal organs." | |
| F196 | 7.4 | diagnosis | "Computed tomography uses X-rays to generate a three-dimensional image of the internals of an object." | |
| F197 | 7.4 | diagnosis | "MRI uses strong magnetic fields and non-ionising radiations to accurately detect pathological and physiological changes in the living tissue." | |
| F198 | 7.4 | diagnosis | "Antibodies against cancer-specific antigens are also used for detection of certain cancers." | |
| F199 | 7.4 | diagnosis | "Techniques of molecular biology can be applied to detect genes in individuals with inherited susceptibility to certain cancers." | |
| F200 | 7.4 | prevention | "Identification of such genes, which predispose an individual to certain cancers, may be very helpful in prevention of cancers. Such individuals may be advised to avoid exposure to particular carcinogens to which they are susceptible (e.g., tobacco smoke in case of lung cancer)." | |
| F201 | 7.4 | treatment | "The common approaches for treatment of cancer are surgery, radiation therapy and immunotherapy." | |
| F202 | 7.4 | treatment | "In radiotherapy, tumor cells are irradiated lethally, taking proper care of the normal tissues surrounding the tumor mass." | |
| F203 | 7.4 | treatment | "Several chemotherapeutic drugs are used to kill cancerous cells. Some of these are specific for particular tumors. Majority of drugs have side effects like hair loss, anemia, etc." | |
| F204 | 7.4 | treatment | "Most cancers are treated by combination of surgery, radiotherapy and chemotherapy." | |
| F205 | 7.4 | treatment | "Tumor cells have been shown to avoid detection and destruction by immune system. Therefore, the patients are given substances called biological response modifiers such as α-interferon which activates their immune system and helps in destroying the tumor." | |
| F206 | 7.5 | fact | "This is really a cause of concern as it could result in many harmful effects. Proper education and guidance would enable youth to safeguard themselves against these dangerous behaviour patterns and follow healthy lifestyles." | |
| F207 | 7.5 | term | "The drugs, which are commonly abused are opioids, cannabinoids and coca alkaloids. Majority of these are obtained from flowering plants. Some are obtained from fungi." | |
| F208 | 7.5 | term | "Opioids are the drugs, which bind to specific opioid receptors present in our central nervous system and gastrointestinal tract." | |
| F209 | 7.5 | term | "Heroin, commonly called smack is chemically diacetylmorphine which is a white, odourless, bitter crystalline compound." | |
| F210 | 7.5 | fact | "This is obtained by acetylation of morphine, which is extracted from the latex of poppy plant Papaver somniferum." | |
| F211 | 7.5 | fact | "Generally taken by snorting and injection, heroin is a depressant and slows down body functions." | |
| F212 | 7.5 | term | "Cannabinoids are a group of chemicals, which interact with cannabinoid receptors present principally in the brain." | |
| F213 | 7.5 | fact | "Natural cannabinoids are obtained from the inflorescences of the plant Cannabis sativa." | |
| F214 | 7.5 | example | "The flower tops, leaves and the resin of cannabis plant are used in various combinations to produce marijuana, hashish, charas and ganja." | |
| F215 | 7.5 | fact | "Generally taken by inhalation and oral ingestion, these are known for their effects on cardiovascular system of the body." | |
| F216 | 7.5 | term | "Coca alkaloid or cocaine is obtained from coca plant Erythroxylum coca, native to South America." | |
| F217 | 7.5 | mechanism | "It interferes with the transport of the neuro-transmitter dopamine." | |
| F218 | 7.5 | fact | "Cocaine, commonly called coke or crack is usually snorted. It has a potent stimulating action on central nervous system, producing a sense of euphoria and increased energy. Excessive dosage of cocaine causes hallucinations." | |
| F219 | 7.5 | example | "Other well-known plants with hallucinogenic properties are Atropa belladona and Datura." | |
| F220 | 7.5 | fact | "These days cannabinoids are also being abused by some sportspersons." | |
| F221 | 7.5 | example | "Drugs like barbiturates, amphetamines, benzodiazepines, and other similar drugs, that are normally used as medicines to help patients cope with mental illnesses like depression and insomnia, are often abused." | |
| F222 | 7.5 | fact | "Morphine is a very effective sedative and painkiller, and is very useful in patients who have undergone surgery." | |
| F223 | 7.5 | fact | "Several plants, fruits and seeds having hallucinogenic properties have been used for hundreds of years in folk-medicine, religious ceremonies and rituals all over the globe." | |
| F224 | 7.5 | term | "When these are taken for a purpose other than medicinal use or in amounts/frequency that impairs one's physical, physiological or psychological functions, it constitutes drug abuse." | |
| F225 | 7.5 | fact | "Smoking also paves the way to hard drugs." | |
| F226 | 7.5 | number | "Tobacco has been used by human beings for more than 400 years. It is smoked, chewed or used as a snuff." | |
| F227 | 7.5 | term | "Tobacco contains a large number of chemical substances including nicotine, an alkaloid." | |
| F228 | 7.5 | mechanism | "Nicotine stimulates adrenal gland to release adrenaline and nor-adrenaline into blood circulation, both of which raise blood pressure and increase heart rate." | |
| F229 | 7.5 | fact | "Smoking is associated with increased incidence of cancers of lung, urinary bladder and throat, bronchitis, emphysema, coronary heart disease, gastric ulcer, etc." | |
| F230 | 7.5 | fact | "Tobacco chewing is associated with increased risk of cancer of the oral cavity." | |
| F231 | 7.5 | mechanism | "Smoking increases carbon monoxide (CO) content in blood and reduces the concentration of haembound oxygen. This causes oxygen deficiency in the body." | |
| F232 | 7.5 | fact | "When one buys packets of cigarettes one cannot miss the statutory warning that is present on the packing which warns against smoking and says how it is injurious to health." | |
| F233 | 7.5 | fact | "Knowing the dangers of smoking and chewing tobacco, and its addictive nature, the youth and old need to avoid these habits. Any addict requires counselling and medical help to get rid of the habit." | |
| F234 | 7.5.1 | number | "The period between 12-18 years of age may be thought of as adolescence period." | |
| F235 | 7.5.1 | term | "In other words, adolescence is a bridge linking childhood and adulthood." | |
| F236 | 7.5.1 | fact | "Adolescence is accompanied by several biological and behavioural changes. Adolescence, thus is a very vulnerable phase of mental and psychological development of an individual." | |
| F237 | 7.5.1 | cause | "Curiosity, need for adventure and excitement, and experimentation, constitute common causes, which motivate youngsters towards drug and alcohol use." | |
| F238 | 7.5.1 | cause | "A child's natural curiosity motivates him/her to experiment. This is complicated further by effects that might be perceived as benefits, of alcohol or drug use." | |
| F239 | 7.5.1 | cause | "the first use of drugs or alcohol may be out of curiosity or experimentation, but later the child starts using these to escape facing problems." | |
| F240 | 7.5.1 | cause | "Of late, stress, from pressures to excel in academics or examinations, has played a significant role in persuading the youngsters to try alcohol and drugs." | |
| F241 | 7.5.1 | cause | "The perception among youth that it is 'cool' or progressive to smoke, use drugs or alcohol, is also in a way a major cause for youth to start these habits. Television, movies, newspapers, internet also help to promote this perception." | |
| F242 | 7.5.1 | cause | "Other factors that have been seen to be associated with drug and alcohol abuse among adolescents are unstable or unsupportive family structures and peer pressure." | |
| F243 | 7.5.2 | fact | "The most important thing, which one fails to realise, is the inherent addictive nature of alcohol and drugs." | |
| F244 | 7.5.2 | term | "Addiction is a psychological attachment to certain effects –such as euphoria and a temporary feeling of well-being – associated with drugs and alcohol." | |
| F245 | 7.5.2 | fact | "These drive people to take them even when these are not needed, or even when their use becomes self-destructive." | |
| F246 | 7.5.2 | mechanism | "With repeated use of drugs, the tolerance level of the receptors present in our body increases. Consequently the receptors respond only to higher doses of drugs or alcohol leading to greater intake and addiction." | |
| F247 | 7.5.2 | fact | "it should be clearly borne in mind that use of these drugs even once, can be a fore-runner to addiction." | |
| F248 | 7.5.2 | fact | "the addictive potential of drugs and alcohol, pull the user into a vicious circle leading to their regular use (abuse) from which he/she may not be able to get out. In the absence of any guidance or counselling, the person gets addicted and becomes dependent on their use." | |
| F249 | 7.5.2 | term | "Dependence is the tendency of the body to manifest a characteristic and unpleasant withdrawal syndrome if regular dose of drugs/alcohol is abruptly discontinued." | |
| F250 | 7.5.2 | symptom | "This is characterised by anxiety, shakiness, nausea and sweating, which may be relieved when use is resumed again." | |
| F251 | 7.5.2 | fact | "In some cases, withdrawal symptoms can be severe and even life threatening and the person may need medical supervision." | |
| F252 | 7.5.2 | fact | "Dependence leads the patient to ignore all social norms in order to get sufficient funds to satiate his/her needs. These result in many social adjustment problems." | |
| F253 | 7.5.3 | fact | "Excessive doses of drugs may lead to coma and death due to respiratory failure, heart failure or cerebral hemorrhage." | |
| F254 | 7.5.3 | fact | "A combination of drugs or their intake along with alcohol generally results in overdosing and even deaths." | |
| F255 | 7.5.3 | symptom | "The most common warning signs of drug and alcohol abuse among youth include drop in academic performance, unexplained absence from school/college, lack of interest in personal hygiene, withdrawal, isolation, depression, fatigue, aggressive and rebellious behaviour, deteriorating relationships with family and friends, loss of interest in hobbies, change in sleeping and eating habits, fluctuations in weight, appetite, etc." | |
| F256 | 7.5.3 | fact | "If an abuser is unable to get money to buy drugs/alcohol he/she may turn to stealing." | |
| F257 | 7.5.3 | fact | "At times, a drug/alcohol addict becomes the cause of mental and financial distress to his/her entire family and friends." | |
| F258 | 7.5.3 | fact | "Those who take drugs intravenously (direct injection into the vein using a needle and syringe), are much more likely to acquire serious infections like AIDS and Hepatitis B." | |
| F259 | 7.5.3 | transmission | "The viruses, which are responsible for these diseases, are transferred from one person to another by sharing of infected needles and syringes." | |
| F260 | 7.5.3 | fact | "Both AIDS and Hepatitis B infections are chronic infections and ultimately fatal. Both can be transmitted through sexual contact or infected blood." | |
| F261 | 7.5.3 | fact | "The use of alcohol during adolescence may also have long-term effects. It could lead to heavy drinking in adulthood." | |
| F262 | 7.5.3 | fact | "The chronic use of drugs and alcohol damages nervous system and liver (cirrhosis)." | |
| F263 | 7.5.3 | fact | "The use of drugs and alcohol during pregnancy is also known to adversely affect the foetus." | |
| F264 | 7.5.3 | fact | "Another misuse of drugs is what certain sportspersons do to enhance their performance. They (mis)use narcotic analgesics, anabolic steroids, diuretics and certain hormones in sports to increase muscle strength and bulk and to promote aggressiveness and as a result increase athletic performance." | |
| F265 | 7.5.3 | symptom | "The side-effects of the use of anabolic steroids in females include masculinisation (features like males), increased aggressiveness, mood swings, depression, abnormal menstrual cycles, excessive hair growth on the face and body, enlargement of clitoris, deepening of voice." | |
| F266 | 7.5.3 | symptom | "In males it includes acne, increased aggressiveness, mood swings, depression, reduction of size of the testicles, decreased sperm production, potential for kidney and liver dysfunction, breast enlargement, premature baldness, enlargement of the prostate gland." | |
| F267 | 7.5.3 | fact | "These effects may be permanent with prolonged use." | |
| F268 | 7.5.3 | symptom | "In the adolescent male or female, severe facial and body acne, and premature closure of the growth centres of the long bones may result in stunted growth." | |
| F269 | 7.5.4 | fact | "It is also true that habits such as smoking, taking drug or alcohol are more likely to be taken up at a young age, more during adolescence." | |
| F270 | 7.5.4 | prevention | "Hence, it is best to identify the situations that may push an adolescent towards use of drugs or alcohol, and to take remedial measures well in time. In this regard, the parents and the teachers have a special responsibility." | |
| F271 | 7.5.4 | prevention | "Parenting that combines with high levels of nurturance and consistent discipline, has been associated with lowered risk of substance (alcohol/drugs/tobacco) abuse." | |
| F272 | 7.5.4 | prevention | "Avoid undue peer pressure - Every child has his/her own choice and personality, which should be respected and nurtured. A child should not be pushed unduly to perform beyond his/her threshold limits; be it studies, sports or other activities." | |
| F273 | 7.5.4 | prevention | "Education and counselling - Educating and counselling him/her to face problems and stresses, and to accept disappointments and failures as a part of life. It would also be worthwhile to channelise the child's energy into healthy pursuits like sports, reading, music, yoga and other extracurricular activities." | |
| F274 | 7.5.4 | prevention | "Seeking help from parents and peers - Help from parents and peers should be sought immediately so that they can guide appropriately. Help may even be sought from close and trusted friends. Besides getting proper advise to sort out their problems, this would help young to vent their feelings of anxiety and guilt." | |
| F275 | 7.5.4 | prevention | "Looking for danger signs - Alert parents and teachers need to look for and identify the danger signs discussed above. Even friends, if they find someone using drugs or alcohol, should not hesitate to bring this to the notice of parents or teacher in the best interests of the person concerned. Appropriate measures would then be required to diagnose the malady and the underlying causes. This would help in initiating proper remedial steps or treatment." | |
| F276 | 7.5.4 | prevention | "Seeking professional and medical help - A lot of help is available in the form of highly qualified psychologists, psychiatrists, and de-addiction and rehabilitation programmes to help individuals who have unfortunately got in the quagmire of drug/alcohol abuse. With such help, the affected individual with sufficient efforts and will power, can get rid of the problem completely and lead a perfectly normal and healthy life." | |

### Session 1-S row count (machine-derived)

Parsed from the finished table by `scratch/ch7_1s/count_rows.py`, not tallied by
hand: **276 rows, `F001`..`F276`, contiguous, no gaps, no duplicates.** Type
distribution over the 12 normalized values, also machine-derived:

`fact` 100, `prevention` 22, `term` 40, `example` 22, `symptom` 20, `mechanism` 20,
`figure-text` 18, `process` 13, `transmission` 10, `diagnosis` 9, `cause` 12,
`treatment` 7, `number` 9, `structure` 5.

The authoritative numbers are whatever `count_rows.py` prints against the file as
committed; the list above is a transcription of that output and 1-Z must re-run
the parse rather than trust it.

### What 1-S deliberately did not inventory

- **Section openers and headings** — sessions 1-O and 1-H, per `§6`. The absence of
  every section's first sentence from the table above is by design.
- **Figure captions** — held verbatim in the Figure manifest, which is their single
  home. Duplicating them as Facts rows would put the same wording in two tables.
- **Unit front matter** — page 1's unit introduction ("Biology is the youngest of
  the formalised disciplines of natural science...") and page 2's M.S. Swaminathan
  biography. These belong to the *unit* that contains Chapters 7 and 8, not to
  Chapter 7, and the Swaminathan page is the same page whose portrait `§5`/`§4.4`
  already forbids embedding. Recorded here as an explicit, reasoned exclusion so a
  later audit does not read the gap as a miss.
- **Exercise questions** (page 22) — the 17 exercises are 1-Z's material under
  step 7 (exercise-gap scan), not Facts rows.
- **Summary paragraph** (pages 21-22) — 1-Z's material under step 8.

### Second hunting pass (step 3) — what it added

Step 2 built the table section by section; step 3 re-read hunting specifically for
qualifiers, parentheticals and numbers buried mid-sentence. It confirmed the bulk
of step 2 and **extended** it with these, each of which step 2 had folded into a
neighbouring row and would have lost:

- the exact typhoid fever range **"(39° to 40°C)"** (F023) and the common-cold
  duration **"3-7 days"** (F033)
- **"but not the lungs"** in the rhino-virus row (F032) — a one-clause exclusion
  that NEET tests directly
- the three *Plasmodium* species spelled as NCERT spells them, including the
  non-standard **"P. malaria"** (F036)
- **haemozoin** named as the toxin and the **"every three to four days"** fever
  periodicity (F040)
- **"W. bancrofti and W. malayi"** as the two named *Wuchereria* species (F060)
- **H2L2** as the antibody's formula notation (F094) and **IgE** as the
  allergy-specific isotype (F120) against **IgA** in colostrum (F108)
- **"about 50 per cent"** for MALT's share of lymphoid tissue (F144)
- AIDS's **1981** first report, **25 million** deaths and the **5-10 year**
  incubation window (F146, F152)
- **"more than 400 years"** of tobacco use (F226) and the **12-18 years**
  adolescence window (F234)
- **α-interferon** named as the biological response modifier (F205), and
  **Gambusia** named as the larvivorous fish (F072)
- the two **CT vs MRI** mechanism sentences kept apart (F196, F197), since the
  chapter distinguishes X-ray-based 3-D imaging from non-ionising magnetic imaging
  and a merged row would blur exactly the contrast being tested

## Figure manifest

11 numbered figures, 7.1-7.11, on artwork pages 6, 7, 9, 12, 13, 16, 17. All 11
assets are single-channel greyscale (`PIL` mode `L`), verified mechanically this
session, so the monochrome check is satisfied by construction. Captions verbatim
from the PDF text layer.

| Fig # | Caption (verbatim) | Asset file | Src page | Mono | Opened |
|---|---|---|---|---|---|
| Figure 7.1 | Stages in the life cycle of Plasmodium | `assets/fig_7_1.png` | 6 | yes (L) | yes |
| Figure 7.2 | Diagram showing inflammation in one of the lower limbs due to elephantiasis | `assets/fig_7_2.png` | 7 | yes (L) | yes |
| Figure 7.3 | Diagram showing ringworm affected area of the skin | `assets/fig_7_3.png` | 7 | yes (L) | yes |
| Figure 7.4 | Structure of an antibody molecule | `assets/fig_7_4.png` | 9 | yes (L) | yes |
| Figure 7.5 | Diagrammatic representation of Lymph nodes | `assets/fig_7_5.png` | 12 | yes (L) | yes |
| Figure 7.6 | Replication of retrovirus | `assets/fig_7_6.png` | 13 | yes (L) | yes |
| Figure 7.7 | Chemical structure of Morphine | `assets/fig_7_7.png` | 16 | yes (L) | yes |
| Figure 7.8 | Opium poppy | `assets/fig_7_8.png` | 16 | yes (L) | yes |
| Figure 7.9 | Skeletal structure of cannabinoid molecule | `assets/fig_7_9.png` | 17 | yes (L) | yes |
| Figure 7.10 | Leaves of Cannabis sativa | `assets/fig_7_10.png` | 17 | yes (L) | yes |
| Figure 7.11 | Flowering branch of Datura | `assets/fig_7_11.png` | 17 | yes (L) | yes |

**Asset count reconciliation:** 11 numbered NCERT figures -> **11** asset files.
No figure in this chapter is split into separately-captioned sub-plates, and there
is no unnumbered bonus diagram (unlike Ch5's central-dogma schematic). The
denominator is **11** everywhere it appears.

**Crop convention:** captions are excluded from every crop, because this project's
notes restate each caption in running text. Every rect's bottom edge stops short
of its caption's `y0`.

### Deliberate exclusions (census re-derived this session)

A page-by-page sweep of all 22 pages for non-furniture rasters and sizeable
drawings returns ink-bearing regions on exactly the 7 artwork pages above, plus
four regions that are **not** assets:

| Page | Region | Why excluded |
|---|---|---|
| 2 | M.S. Swaminathan portrait photograph, `(57, 272, 166, 395)` | `§5` item 3 / `§4.4` "Hard no": a scientist portrait is never embedded, greyscaled or not. |
| 3 | Chapter-opener title plate, `(344, 56, 525, 213)` + QR thumbnail | Page furniture / title block. The tilted thumbnail merely re-prints fig 7.4's antibody artwork; it carries no fact of its own. |
| 21 | Orange wheat-ear motif beside SUMMARY box, `(407, 439, 455, 705)` | Decoration. |
| 22 | Same motif, `(126, 84, 174, 265)` | Decoration. |

All other pages (1, 4, 5, 8, 10, 11, 14, 15, 18, 19, 20) carry only the 1-2
furniture drawings — the header band and the full-page
"(c) NCERT / not to be republished" watermark.

### Rects, as frozen by session 1-F

Rects are in PDF points on the artwork page; page box is 568.8 x 777.6. Pinned by
hand off a 20 pt coordinate grid (`scratch/ch7_figs/grid/pNN.png`), because — see
the label matrix below — **every** in-figure label in this chapter is artwork, so
no text-layer method can find the plate boundaries.

| Asset | Src page | Rect (pt) | Kind |
|---|---|---|---|
| `fig_7_1` | 6 | (53, 83, 536, 610) | vector + raster, full-page plate |
| `fig_7_2` | 7 | (325, 79, 513, 351) | raster illustration |
| `fig_7_3` | 7 | (267, 414, 508, 533) | raster photograph |
| `fig_7_4` | 9 | (213, 290, 521, 530) | vector panel + raster tint |
| `fig_7_5` | 12 | (54, 80, 206, 302) | raster silhouette + vector labels |
| `fig_7_6` | 13 | (84, 81, 469, 532) | pure vector schematic |
| `fig_7_7` | 16 | (122, 545, 298, 696) | vector skeletal formula |
| `fig_7_8` | 16 | (374, 538, 495, 694) | raster-tile illustration |
| `fig_7_9` | 17 | (50, 215, 263, 366) | vector skeletal formula |
| `fig_7_10` | 17 | (350, 219, 456, 364) | vector panel, mid-tone fills |
| `fig_7_11` | 17 | (326, 395, 515, 586) | raster-tile illustration |

NCERT sets 7.2, 7.3, 7.4, 7.5 and 7.11 *beside* a body-text column, so an
automatic ink box would sweep the neighbouring paragraph in; each of those rects
is clipped against the prose column's own x boundary taken from `get_text("words")`.

---

## Figure-label matrix

Eleven rows, one per asset. Rows for the six assets with no descriptive callouts
are worded so they do **not** begin `Figure labels`, because `check_pdf.py`'s
`_extract_labels` falls back to semicolon-splitting an unquoted body — a row
reading "Figure labels: (none)" would manufacture a phantom label that no running
text could ever satisfy. The column header is worded the same way, for the same
reason. The parser reads column index 3, so this table's shape is load-bearing.

Labels were harvested by **opening each rendered asset** in this session, never by
text extraction. This chapter is the textbook case for that rule: a
`page.get_text("words")` sweep returns **zero** words inside all 11 rects (see the
audit table below) even though figs 7.1, 7.4, 7.5 and 7.6 carry 30 callouts
between them. Every label is baked into the artwork.

| ID | Fig # | Type | Label row wording | Ticked |
|----|-------|------|-------------------|--------|
| — | Fig 7.1 | label | Figure labels: "Sporozoites"; "Salivary glands"; "Mosquito Host"; "Human Host"; "Gametocytes"; "Male"; "Female" | x |
| — | Fig 7.2 | label | No in-figure labels — unlabelled illustration of a seated man with elephantiasis of the lower limbs | x |
| — | Fig 7.3 | label | No in-figure labels — unlabelled photograph of a ringworm lesion on the chin and jaw | x |
| — | Fig 7.4 | label | Figure labels: "Antigen binding site"; "Light chain"; "Heavy chain" | x |
| — | Fig 7.5 | label | Figure labels: "Lymph nodes"; "Thymus"; "Lymphatic vessels" | x |
| — | Fig 7.6 | label | Figure labels: "Retrovirus"; "Viral RNA core"; "Viral protein coat"; "Animal cell"; "Plasma membrane"; "Cytoplasm"; "Nucleus"; "DNA" | x |
| — | Fig 7.7 | label | No descriptive callouts — skeletal formula bearing only atom/group symbols (HO, O, H, N, CH3) | x |
| — | Fig 7.8 | label | No in-figure labels — unlabelled illustration of an opium poppy plant | x |
| — | Fig 7.9 | label | No descriptive callouts — skeletal formula bearing only atom/group symbols (OH, O, H) | x |
| — | Fig 7.10 | label | No in-figure labels — unlabelled framed illustration of a Cannabis sativa leaf | x |
| — | Fig 7.11 | label | No in-figure labels — unlabelled illustration of a flowering Datura branch | x |

**Parsed label total: 21** (7 + 3 + 3 + 8), across 4 labelled assets. The seven
non-`Figure labels` rows contribute 0 and are invisible to the parser by design.

`F###` IDs are left as `—` because the Facts table does not exist yet; session 1-S
must assign them and 1-Z must reconcile this matrix against them.

### Labels deliberately NOT quoted, and the obligations they create

Three sets of in-figure text are real but are **not** quoted above, because
quoting them would create check-6 requirements that are either unsatisfiable or
meaningless. Each becomes an explicit Pass 2 obligation instead:

- **fig 7.4's chain-terminus markers `N` and `C`.** Single characters.
  `_coverage_ratio` strips tokens of length 1, then falls back to a bare `\bn\b`
  word-boundary search — which any stray "n" in the notes would satisfy, so the
  check would be noise either way. **Obligation:** the antibody passage must name
  the amino (N) and carboxyl (C) termini of the chains in running text.
- **The `S-S` disulfide-bridge markers in fig 7.4.** Numerous, and not a
  descriptive callout. **Obligation:** the passage must state that the chains are
  held together by disulfide bonds.
- **The process-arrow sentences in figs 7.1 and 7.6.** These are full sentences,
  not labels ("When the mosquito bites another human, sporozoites are injected
  with bite.", "Viral DNA is produced by reverse transcriptase", the in-plate
  "NOTE: Infected cell can survive while viruses are being replicated and
  released", and 11 others). Listing them as labels would misuse the mechanism.
  **Obligation:** their content must be carried by the Facts rows for the malaria
  life cycle and HIV replication, which session 1-S must create. **This is the
  single biggest carry-over from 1-F and must not be lost.**

---

## Extraction gate record (five-part audit, session 1-F)

Run: `/vercel/share/neetenv/bin/python scratch/ch7_figs/audit.py`
(script rebuilt and committed this session; the previous sitting's copy was lost).

| Asset | A) word grazing | B) drawings overflow | B2) raster overflow | B3) tile union | C) dark border ink | C2) light border ink |
|---|---|---|---|---|---|---|
| `fig_7_1` | **vacuous** (0 words) | ok (1250 shapes) | ok | ok (4276 tiles) | clean | explained (page-number tab) |
| `fig_7_2` | **vacuous** (0 words) | no drawings | ok (1 raster) | ok | clean | explained (corner motif) |
| `fig_7_3` | **vacuous** (0 words) | no drawings | ok (1 raster) | ok | clean | clean |
| `fig_7_4` | **vacuous** (0 words) | ok (1180 shapes) | ok | ok (81 tiles) | clean | clean |
| `fig_7_5` | **vacuous** (0 words) | ok (35 shapes) | OVERFLOW L24.8 — **explained** | OVERFLOW L24.8 — **explained** | clean | explained (corner motif) |
| `fig_7_6` | **vacuous** (0 words) | ok (4944 shapes) | no rasters | no tiles (pure vector) | clean | clean |
| `fig_7_7` | **vacuous** (0 words) | ok (26 shapes) | ok | ok (59 tiles) | clean | clean |
| `fig_7_8` | **vacuous** (0 words) | **vacuous** (0 drawings) | **vacuous** (3x3 px tile only) | ok (1804 tiles) | clean | clean |
| `fig_7_9` | **vacuous** (0 words) | ok (16 shapes) | ok | ok (59 tiles) | clean | clean |
| `fig_7_10` | **vacuous** (0 words) | OVERFLOW L4.8 T9.3 R11.6 — **explained** | **vacuous** (5x3 px tile only) | ok (582 tiles) | clean | clean |
| `fig_7_11` | **vacuous** (0 words) | **vacuous** (0 drawings) | **vacuous** (0 rasters) | ok (4878 tiles) | clean | clean |

### Notes on this chapter's audit

- **Check A is vacuous for all 11 assets.** Zero text-layer words fall inside any
  rect — not even a panel letter. Check A therefore provides **no** evidence
  whatsoever about crop quality in this chapter and must never be cited as if it
  did. B/B2/B3/C/C2 plus the eyeball carried this gate.
- **Check C2 (light threshold, grey < 205) was required.** The skill's standard C
  uses grey < 110, but the fig 7.10 cannabis leaf is mid-green (luma ~177) inside
  a pale grey frame, i.e. the entire plate sits *above* the dark threshold. C
  passed on it while the crop was in fact clipping the panel border. All three
  surviving C2 hits are page furniture, each identified by coordinate:
  `fig_7_1` bottom = the orange page-number tab ("132", ink from y=611.8, x 53-92);
  `fig_7_2` top = the top-right leaf/corner motif at y~73, x 469-502;
  `fig_7_5` top = the top-left corner motif at y~74. `fig_7_10`'s top band is now
  **clean**, which is the mechanical confirmation that the re-pin worked.
- **Check B3 was added this session** and is not optional for Ch7. Figures 7.8 and
  7.11 are stipple/scanline artwork built from ~1800 and ~4900 sub-pixel raster
  tiles; B (drawings) and B2 (rasters >= 3 pt) are both blind to them. Before B3
  those two plates had **no** mechanical edge check at all and were passing
  vacuously. With B3 the tile unions land at
  `x 373.0-491.2, y 541.0-694.1` (fig 7.8, inside its rect to within 1.0 pt) and
  `x 330.6-510.1, y 395.9-580.1` (fig 7.11, comfortably inside).
- **`fig_7_5`'s L24.8 overflow is the raster's own white margin,** not a clip: the
  silhouette raster bbox begins at x=29.2, but a 300 dpi column scan (thr 205)
  puts the first inked column at **x=57.9**, and the rect's left edge is x=54.
  The `Lymph nodes` / `Thymus` / `Lymphatic vessels` labels are vector and run
  right to x=201.7, which is why the box must span to x=206.
- **`fig_7_10`'s B overflow is explained by clipping, not truncation:** the leaf's
  gradient shapes are *defined* out to `x 345.2-467.6, y 209.7`, but they are
  clipped by the panel's own clip path, so no ink renders outside the frame. The
  thr-205 probe, check C2, and the opened asset all agree the frame is intact.
- **Page furniture excluded from every measurement:** the full-page watermark
  (~`(46, 191, 508, 653)` raster, present on every page), the dark green header
  band (y < 76), the brown/orange corner motifs, the right-margin decorative band,
  and the orange page-number tab.

### Rects re-pinned during session 1-F

| Asset | Was | Now | Why |
|---|---|---|---|
| `fig_7_10` | (348, 224, 460, 366) | (350, 219, 456, 364) | Check B flagged T14.3 overflow and the eyeball confirmed ~1.5 pt of the panel's top border was sliced off. The dark-ink probe had reported the plate starting at y=230.2 only because the whole figure is mid-tone; a thr-205 re-probe put the panel at `x 352.3-454.6, y 222.5-361.0` (shadow included). Rect widened to clear it by ~2 pt. |

### Visual verification

All 11 assets were opened and inspected at full size in this session (not merely
contact-sheeted). Each renders complete: fig 7.1 shows all ten callouts and both
host loops; fig 7.4 shows the rounded panel with `N` at top and both `C` termini at
bottom; fig 7.6 shows the outer panel and the in-plate NOTE line; fig 7.10 shows
all four panel borders plus the drop shadow, confirming the re-pin. No crop clips
artwork and none admits body text.

One cosmetic observation, recorded and dismissed: `fig_7_5` includes a faint grey
horizontal rule at its very bottom edge (the caption block's top rule, `y0=306.0`
vs the rect's bottom at 302). It is a rule, not text, and carries no content.

---

## Carry-over to later sessions

1. **1-S must create the Facts table**, and must cover the 14 process-arrow
   sentences in figs 7.1 and 7.6 plus the three unquoted label sets listed above.
2. **1-Z must assign `F###` IDs** to the 11 label-matrix rows and reconcile them.
3. **`check_pdf.py` check 6 cannot pass meaningfully until 1-S exists** — there is
   no running text yet for the 21 parsed labels to be found in.
4. The `extract_figures.py` docstring's stale fig 7.10 overflow numbers
   (`L2.8/T14.3/R7.6`, measured against the superseded rect) should be corrected
   to `L4.8/T9.3/R11.6` when that file is next touched, so a future session does
   not mistake the mismatch for a regression.
