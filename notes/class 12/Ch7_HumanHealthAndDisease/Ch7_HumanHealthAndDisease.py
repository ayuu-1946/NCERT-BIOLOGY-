"""
NCERT Class 12 Biology, Chapter 7 - Human Health and Disease
NEET replacement notes -> A4 print-ready PDF.

Built under SUPREME COMMAND PROMPT.md v6, Pass 2: written linearly from the
frozen 346-row inventory (Ch7_HumanHealthAndDisease_inventory.md), importing the
repo-level frozen style module `neet_template.py` (v6 SS0.6). No style, geometry,
colour or font is re-declared here.

Block markers `# ---- N.N ----` mark every NCERT section so a Pass 3 flag can be
found and fixed in one contiguous block. Inventory row IDs are named in the
comments so any fact can be traced back to its frozen row.

Pass 1 binding obligations actioned (inventory carry-overs):
  1. All 21 in-figure labels (F336-F346) are written into running text verbatim,
     because they are artwork and check 6 gates them.
  2. The unquoted in-plate text of figs 7.1 / 7.4 / 7.6 is carried as prose:
     the 8 malaria process sentences (F045-F052), the 8 HIV process sentences
     (F169-F176), and fig 7.4's N / C termini and S-S disulfide markers
     (F102, F103).
  3. Widal test: the inventory's 1-O structural finding requires the definition
     ("confirmed by the Widal test") to sit ADJACENT to the Typhoid Mary
     anecdote, not split across a heading as NCERT prints it.
  4. Both SUMMARY-UNIQUE facts are body rows, not summary-only text: F334
     ("psychological" in the definition of health) in the intro, F335 (cholera
     named as a human disease) in 7.1.
  5. The 2 exercise gaps are handled per the frozen plan: "water-borne" is
     stated as a grouping inside 7.1's prevention block (F067-F069), and
     "DNA vaccines" goes ONLY into the Terms used in the exercises appendix,
     flagged as outside this chapter's scope (Rule 5).
  6. Banned glyphs: no degree sign ("39 degrees C to 40 degrees C"), no Greek
     ("alpha-interferon"), no Unicode sub/superscripts (H<sub>2</sub>L<sub>2</sub>),
     no arrows.
  7. The M.S. Swaminathan portrait (source p2) is never embedded (SS5 item 3);
     the unit front matter is out of this chapter's scope per the inventory.

Source: Chapter/class 12/Chapter 7 - Human Health and Disease.pdf (22 pages)
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# sys.path bootstrap: walk up until we find the repo-level neet_template.py (SS0.6)
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
from reportlab.platypus import Paragraph, Spacer  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch7_HumanHealthAndDisease.pdf")


def figure(asset_name, caption_text, max_width_cm=15.9):
    """Chapter-local binding of the shared figure() helper (SS0.6)."""
    return _shared_figure(asset_name, caption_text, ASSETS, max_width_cm=max_width_cm)


def body(text):
    return Paragraph(text, STYLES["Body"])


def b1(text):
    return Paragraph("&bull; " + text, STYLES["Bullet1"])


def b2(text):
    return Paragraph("- " + text, STYLES["Bullet2"])


def gap(h=4):
    return Spacer(1, h)


story = []

# ======================================================================================
# ---- Title block (SS5 item 1) ----
# ======================================================================================
story += title_block("Human Health and Disease")

# ======================================================================================
# ---- Chapter opener + intro (F277 heading, F306 opener, F001-F016, F334) ----
# ======================================================================================
# F277 - the chapter title plate, carried as the opener banner
story.append(heading("Ch 7", "HUMAN HEALTH AND DISEASE - Chapter Opener", 1))
# F306 (opener)
story.append(body(
    "The term <b>health</b> is very frequently used by everybody, so it has to be defined "
    "precisely before anything else in this chapter can be built on it."))
story.append(gap())

story.append(heading("7.0", "How the idea of health was arrived at", 2))
# F001 - the 'blackbile' idea, arrived at by pure reflective thought
story.append(body(
    "Early ideas about health were <b>not</b> experimental. It was thought that persons with "
    "<b>'blackbile'</b> belonged to a <b>hot personality</b> and would have <b>fevers</b>; this idea "
    "was arrived at by <b>pure reflective thought</b>, not by measurement."))
# F002, F003 - what the experimental method did to that hypothesis
story.append(b1(
    "The <b>discovery of blood circulation</b> by <b>William Harvey</b> using the "
    "<b>experimental method</b>, and"))
story.append(b1(
    "the <b>demonstration of normal body temperature</b> in persons with blackbile using a "
    "<b>thermometer</b>, together <b>disproved the 'good humor' hypothesis</b> of health."))
story.append(gap())
# F004 - mind / immune system mechanism
story.append(body(
    "Later biology stated that the <b>mind influences</b>, through the <b>neural system</b> and the "
    "<b>endocrine system</b>, our <b>immune system</b>, and that our immune system maintains our "
    "health. Hence, <b>mind and mental state can affect our health</b>."))
story.append(gap())
# F005 - the three things health is affected by, in NCERT's own numbering
story.append(body("Health is affected by three broad things:"))
story.append(b1(
    "<b>(i) Genetic disorders</b> - deficiencies with which a child is <b>born</b>, and "
    "deficiencies/defects which the child <b>inherits from parents from birth</b>;"))
story.append(b1("<b>(ii) Infections</b>;"))
story.append(b1(
    "<b>(iii) Life style</b> - including the <b>food and water</b> we take, the <b>rest and "
    "exercise</b> we give to our bodies, and <b>habits</b> that we have or lack, etc."))
story.append(gap())
# F006 + F334 (SUMMARY-UNIQUE: the summary's definition adds "psychological")
story.append(keyterm(
    "<b>Health</b> does <b>not</b> simply mean <b>'absence of disease'</b> or <b>'physical "
    "fitness'</b>. It could be defined as a state of <b>complete physical, mental and social "
    "well-being</b>. The chapter summary states the same definition with one word added: a state "
    "of complete <b>physical, mental, social and psychological well-being</b>."))
# F007, F008 - why health matters
story.append(body(
    "When people are healthy, they are <b>more efficient at work</b>. This <b>increases "
    "productivity</b> and brings <b>economic prosperity</b>. Health also <b>increases longevity</b> "
    "of people and <b>reduces infant and maternal mortality</b>."))
# F009, F010 - maintaining health
story.append(body(
    "<b>Balanced diet</b>, <b>personal hygiene</b> and <b>regular exercise</b> are very important "
    "to maintain good health. <b>Yoga</b> has been practised <b>since time immemorial</b> to achieve "
    "<b>physical and mental health</b>."))
# F011 - the full list of what is necessary for achieving good health
story.append(body("Also necessary for achieving good health:"))
story.append(b1("<b>awareness</b> about diseases and their effect on different bodily functions;"))
story.append(b1("<b>vaccination (immunisation)</b> against infectious diseases;"))
story.append(b1("<b>proper disposal of wastes</b>;"))
story.append(b1("<b>control of vectors</b>;"))
story.append(b1("<b>maintenance of hygiene in food and water resources</b>."))
story.append(gap())
# F012 - definition of disease
story.append(keyterm(
    "When the functioning of <b>one or more organs or systems</b> of the body is <b>adversely "
    "affected</b>, characterised by appearance of various <b>signs and symptoms</b>, we say that we "
    "are not healthy, i.e., we have a <b>disease</b>."))
# F013, F014, F015, F016 - the two broad groups
story.append(body(
    "Diseases can be broadly grouped into <b>infectious</b> and <b>non-infectious</b>. Diseases "
    "which are <b>easily transmitted from one person to another</b> are called <b>infectious "
    "diseases</b>."))
story.append(data_table([
    ["Group", "What it means", "NCERT's own points"],
    ["Infectious diseases",
     "Easily transmitted from one person to another.",
     "Very common - <b>every one of us suffers from these at sometime or other</b>. Some, "
     "like <b>AIDS</b>, are <b>fatal</b>."],
    ["Non-infectious diseases",
     "Not transmitted from person to person.",
     "<b>Cancer</b> is the <b>major cause of death</b> among these. <b>Drug and alcohol "
     "abuse</b> also affect our health adversely."],
], col_widths=[22, 30, 48]))
story.append(gap())

# ======================================================================================
# ---- 7.1 COMMON DISEASES IN HUMANS (F278 heading, F307 opener) ----
# ======================================================================================
story.append(heading("7.1", "COMMON DISEASES IN HUMANS", 1))
# F307 (opener)
story.append(body(
    "A <b>wide range of organisms</b> belonging to <b>bacteria, viruses, fungi, protozoans, "
    "helminths</b>, etc., could cause diseases in man."))
# F335 (SUMMARY-UNIQUE: cholera is named as a human disease only in the summary)
story.append(body(
    "Diseases like <b>typhoid</b>, <b>cholera</b>, <b>pneumonia</b>, <b>fungal infections of "
    "skin</b>, <b>malaria</b> and many others are a <b>major cause of distress</b> to human beings."))
# F017, F018, F019
story.append(keyterm(
    "Such disease-causing organisms are called <b>pathogens</b>. <b>Most parasites are therefore "
    "pathogens</b>, as they cause harm to the host by <b>living in (or on)</b> them."))
story.append(body(
    "The pathogens can <b>enter our body by various means</b>, <b>multiply</b> and <b>interfere "
    "with normal vital activities</b>, resulting in <b>morphological and functional damage</b>."))
# F020 - host adaptation, with NCERT's own gut example
story.append(body(
    "Pathogens have to <b>adapt to life within the environment of the host</b>. For example, the "
    "pathogens that enter the <b>gut</b> must know a way of <b>surviving in the stomach at low "
    "pH</b> and <b>resisting the various digestive enzymes</b>."))
story.append(gap())

# ---- 7.1 (a) Typhoid (F021-F026, plus the Widal-test obligation) ----
story.append(heading("7.1a", "Typhoid", 2))
# F021, F022, F023, F024, F025
story.append(body(
    "<i>Salmonella typhi</i> is a <b>pathogenic bacterium</b> which causes <b>typhoid fever</b> in "
    "human beings. These pathogens generally enter the <b>small intestine</b> through <b>food and "
    "water contaminated</b> with them, and <b>migrate to other organs through blood</b>."))
story.append(b1(
    "<b>Symptoms:</b> <b>sustained high fever (39 degrees C to 40 degrees C)</b>, <b>weakness</b>, "
    "<b>stomach pain</b>, <b>constipation</b>, <b>headache</b> and <b>loss of appetite</b>."))
story.append(b1("<b>Intestinal perforation</b> and <b>death may occur in severe cases</b>."))
story.append(b1("<b>Diagnosis:</b> typhoid fever could be confirmed by the <b>Widal test</b>."))
story.append(gap())
# F279 heading + F308 opener. The 1-O structural finding: NCERT prints the "Widal test"
# run-in head ABOVE the Mary Mallon anecdote while the test's definition sits in the
# prose above the heading. The definition is repeated here so the anecdote does not read
# as a non-sequitur (inventory Pass 2 obligation).
story.append(heading("7.1b", "Widal test", 3))
story.append(body(
    "The <b>Widal test</b> is the test that <b>confirms typhoid fever</b> (stated in the prose "
    "above). Under this same heading NCERT places a classic case in medicine:"))
# F026
story.append(note(
    "A classic case in medicine, that of <b>Mary Mallon</b> nicknamed <b>Typhoid Mary</b>, is worth "
    "mentioning here. She was a <b>cook by profession</b> and was a <b>typhoid carrier</b> who "
    "continued to <b>spread typhoid for several years</b> through the <b>food she prepared</b>."))
story.append(gap())

# ---- 7.1 (b) Pneumonia (F027-F030) ----
story.append(heading("7.1c", "Pneumonia", 2))
# F027, F028
story.append(body(
    "Bacteria like <b><i>Streptococcus pneumoniae</i></b> and <b><i>Haemophilus influenzae</i></b> "
    "are responsible for the disease <b>pneumonia</b> in humans, which infects the <b>alveoli (air "
    "filled sacs) of the lungs</b>. As a result of the infection, the <b>alveoli get filled with "
    "fluid</b>, leading to <b>severe problems in respiration</b>."))
# F029, F030
story.append(b1(
    "<b>Symptoms:</b> <b>fever</b>, <b>chills</b>, <b>cough</b> and <b>headache</b>. In severe "
    "cases, the <b>lips and finger nails may turn gray to bluish in colour</b>."))
story.append(b1(
    "<b>Transmission:</b> a healthy person acquires the infection by <b>inhaling the "
    "droplets/aerosols</b> released by an infected person, or even by <b>sharing glasses and "
    "utensils</b> with an infected person."))
# F031
story.append(body(
    "<b>Dysentery</b>, <b>plague</b>, <b>diphtheria</b>, etc., are some of the <b>other bacterial "
    "diseases</b> in man."))
story.append(gap())

# ---- 7.1 (c) Common cold (F032-F034) ----
story.append(heading("7.1d", "Common cold", 2))
# F032
story.append(body(
    "<b>Rhino viruses</b> represent one such group of viruses which cause one of the <b>most "
    "infectious human ailments</b> - the <b>common cold</b>. They infect the <b>nose and "
    "respiratory passage</b> but <b>not the lungs</b>."))
# F033, F034
story.append(b1(
    "<b>Symptoms:</b> <b>nasal congestion and discharge</b>, <b>sore throat</b>, "
    "<b>hoarseness</b>, <b>cough</b>, <b>headache</b>, <b>tiredness</b>, etc., which "
    "<b>usually last for 3-7 days</b>."))
story.append(b1(
    "<b>Transmission:</b> droplets resulting from <b>cough or sneezes</b> of an infected person are "
    "either <b>inhaled directly</b> or transmitted through <b>contaminated objects</b> such as "
    "<b>pens, books, cups, doorknobs, computer keyboard or mouse</b>, etc., and cause infection in "
    "a healthy person."))
story.append(gap())

# ---- 7.1 (d) Malaria (F035-F044) + Figure 7.1 (F045-F052 in-plate text, F336 labels) ----
story.append(heading("7.1e", "Malaria", 2))
# F035, F036, F037
story.append(body(
    "<b><i>Plasmodium</i></b>, a <b>tiny protozoan</b>, is responsible for this disease. "
    "<b>Different species</b> of <i>Plasmodium</i> (<b><i>P. vivax</i></b>, <b><i>P. malaria</i></b> "
    "and <b><i>P. falciparum</i></b>) are responsible for <b>different types of malaria</b>. Of "
    "these, <b>malignant malaria</b> caused by <b><i>Plasmodium falciparum</i></b> is the <b>most "
    "serious one</b> and <b>can even be fatal</b>."))
# F038 - F042 as the process flow, with the in-plate sentences of Figure 7.1 folded in
# (F045-F052) so the plate's text exists in running prose as well.
story.append(body("<b>Life cycle of the malarial parasite (two hosts, one cycle):</b>"))
story.append(process_flow([
    "<b>Plasmodium</b> enters the human body as <b>sporozoites (infectious form)</b> through the "
    "<b>bite of an infected female <i>Anopheles</i> mosquito</b> - when the mosquito bites another "
    "human, <b>sporozoites are injected with the bite</b>.",
    "The parasite (<b>sporozoites</b>) <b>reach the liver through blood</b>: the parasites "
    "<b>initially multiply within the liver cells</b>, the parasite <b>reproduces asexually in "
    "liver cells, bursting the cell and releasing into the blood</b>.",
    "They then <b>attack the red blood cells (RBCs)</b>, resulting in their <b>rupture</b>. "
    "Parasites <b>reproduce asexually in red blood cells, bursting the red blood cells and causing "
    "cycles of fever and other symptoms</b>; released parasites <b>infect new red blood cells</b>.",
    "The rupture of RBCs releases a <b>toxic substance, haemozoin</b>, which is responsible for the "
    "<b>chill and high fever recurring every three to four days</b>.",
    "<b>Sexual stages (gametocytes)</b> develop in the red blood cells - the <b>male</b> and "
    "<b>female</b> forms shown on the plate.",
    "When a <b>female <i>Anopheles</i> mosquito</b> bites an infected person, these parasites "
    "<b>enter the mosquito's body</b> and undergo <b>further development</b>: the <b>female "
    "mosquito takes up gametocytes with the blood meal</b>.",
    "<b>Fertilization and development take place in the mosquito's gut.</b>",
    "The parasites <b>multiply within them to form sporozoites</b> that are <b>stored in their "
    "salivary glands</b>: the <b>mature infective stages (sporozoites) escape from the gut and "
    "migrate to the mosquito salivary glands</b>. When these mosquitoes bite a human, the "
    "<b>sporozoites are introduced into his/her body</b>, thereby <b>initiating the events "
    "mentioned above</b>.",
], cyclic=True))
story.append(gap())
# F043, F044
story.append(keyterm(
    "The <b>malarial parasite requires two hosts - human and mosquitoes - to complete its life "
    "cycle</b>, and the <b>female <i>Anopheles</i> mosquito is the vector (transmitting agent)</b> "
    "too."))
# F336 - every in-figure label of Figure 7.1, in running text (check 6)
story.append(body(
    "<b>Reading Figure 7.1:</b> the plate is drawn as two linked loops - the <b>Human Host</b> on "
    "one side and the <b>Mosquito Host</b> on the other. Labelled on it are the "
    "<b>Sporozoites</b> leaving the mosquito's <b>Salivary glands</b>, and the "
    "<b>Gametocytes</b> in the human blood, which are of two kinds, <b>Male</b> and <b>Female</b>."))
story.append(figure("fig_7_1.png",
                    "Fig. 7.1 - Stages in the life cycle of <i>Plasmodium</i>."))
story.append(gap())

# ---- 7.1 (e) Amoebiasis (F053-F055) ----
story.append(heading("7.1f", "Amoebiasis (amoebic dysentery)", 2))
# F053, F054, F055
story.append(body(
    "<b><i>Entamoeba histolytica</i></b> is a <b>protozoan parasite in the large intestine</b> of "
    "human which causes <b>amoebiasis (amoebic dysentery)</b>."))
story.append(b1(
    "<b>Symptoms:</b> <b>constipation</b>, <b>abdominal pain and cramps</b>, <b>stools with excess "
    "mucous and blood clots</b>."))
story.append(b1(
    "<b>Transmission:</b> <b>houseflies act as mechanical carriers</b> and serve to transmit the "
    "parasite <b>from faeces of infected person to food and food products</b>, thereby "
    "contaminating them. <b>Drinking water and food contaminated by the faecal matter</b> are the "
    "<b>main source of infection</b>."))
story.append(gap())

# ---- 7.1 (f) Helminth diseases: ascariasis, filariasis (F056-F062) + Figure 7.2 ----
story.append(heading("7.1g", "Helminth diseases - Ascariasis and Filariasis", 2))
# F056, F057, F058, F059
story.append(body(
    "<b><i>Ascaris</i></b>, the <b>common round worm</b>, and <b><i>Wuchereria</i></b>, the "
    "<b>filarial worm</b>, are some of the <b>helminths</b> which are known to be <b>pathogenic to "
    "man</b>. <b><i>Ascaris</i></b>, an <b>intestinal parasite</b>, causes <b>ascariasis</b>."))
story.append(b1(
    "<b>Symptoms of ascariasis:</b> <b>internal bleeding</b>, <b>muscular pain</b>, <b>fever</b>, "
    "<b>anemia</b> and <b>blockage of the intestinal passage</b>."))
story.append(b1(
    "<b>Transmission:</b> the <b>eggs of the parasite are excreted along with the faeces</b> of "
    "infected persons, which <b>contaminate soil, water, plants</b>, etc. A healthy person acquires "
    "this infection through <b>contaminated water, vegetables, fruits</b>, etc."))
story.append(gap())
# F060, F061, F062
story.append(body(
    "<b><i>Wuchereria</i></b> (<b><i>W. bancrofti</i></b> and <b><i>W. malayi</i></b>), the "
    "<b>filarial worms</b>, cause a <b>slowly developing chronic inflammation</b> of the organs in "
    "which they live for <b>many years</b>, <b>usually the lymphatic vessels of the lower limbs</b>, "
    "and the disease is called <b>elephantiasis</b> or <b>filariasis</b>. The <b>genital organs</b> "
    "are also <b>often affected</b>, resulting in <b>gross deformities</b>. The pathogens are "
    "transmitted to a healthy person through the <b>bite by the female mosquito vectors</b>."))
# F337 - Figure 7.2 carries no in-figure labels
story.append(figure("fig_7_2.png",
                    "Fig. 7.2 - Diagram showing inflammation in one of the lower limbs due to "
                    "elephantiasis. The plate is an unlabelled illustration; the swelling shown is "
                    "the chronic inflammation of the lymphatic vessels of the lower limb described "
                    "above."))
story.append(gap())

# ---- 7.1 (g) Ringworm (F063-F066) + Figure 7.3 ----
story.append(heading("7.1h", "Ringworms", 2))
# F063, F064, F065, F066
story.append(body(
    "Many <b>fungi</b> belonging to the genera <b><i>Microsporum</i></b>, "
    "<b><i>Trichophyton</i></b> and <b><i>Epidermophyton</i></b> are responsible for "
    "<b>ringworms</b>, which is <b>one of the most common infectious diseases in man</b>."))
story.append(b1(
    "<b>Symptoms:</b> appearance of <b>dry, scaly lesions</b> on various parts of the body such as "
    "<b>skin, nails and scalp</b>. These lesions are accompanied by <b>intense itching</b>."))
story.append(b1(
    "<b>Heat and moisture</b> help these fungi to grow, which makes them <b>thrive in skin "
    "folds</b> such as those in the <b>groin</b> or <b>between the toes</b>."))
story.append(b1(
    "<b>Transmission:</b> ringworms are <b>generally acquired from soil</b>, or by <b>using towels, "
    "clothes or even the comb of infected individuals</b>."))
# F338 - Figure 7.3 carries no in-figure labels
story.append(figure("fig_7_3.png",
                    "Fig. 7.3 - Diagram showing ringworm affected area of the skin. The plate is "
                    "an unlabelled photograph of a lesion on the chin and jaw - one of the dry, "
                    "scaly, intensely itching lesions described above."))
story.append(gap())

# ---- 7.1 (h) Prevention and control of infectious diseases (F067-F078) ----
story.append(heading("7.1i", "Prevention and control of infectious diseases", 2, has_table=True))
# F067, F068
story.append(data_table([
    ["Level of hygiene", "What NCERT includes in it"],
    ["Personal hygiene",
     "Keeping the <b>body clean</b>; consumption of <b>clean drinking water, food, vegetables, "
     "fruits</b>, etc."],
    ["Public hygiene",
     "<b>Proper disposal of waste and excreta</b>; <b>periodic cleaning and disinfection of water "
     "reservoirs, pools, cesspools and tanks</b>; and <b>observing standard practices of hygiene "
     "in public catering</b>."],
], col_widths=[26, 74]))
story.append(gap())
# F069 + the Ex-4 terminology gap ("water-borne"), stated here per the frozen plan
story.append(body(
    "These measures are <b>particularly essential where the infectious agents are transmitted "
    "through food and water</b> - such as <b>typhoid</b>, <b>amoebiasis</b> and <b>ascariasis</b>. "
    "Because they travel in contaminated food and water, these three are exactly the diseases that "
    "a question calls <b>water-borne</b>; NCERT's own wording for the other two routes is "
    "<b>air-borne</b> and <b>vector-borne</b>."))
# F070
story.append(b1(
    "In cases of <b>air-borne diseases</b> such as <b>pneumonia</b> and <b>common cold</b>, in "
    "addition to the above measures, <b>close contact with the infected persons or their belongings "
    "should be avoided</b>."))
# F071, F072, F073
story.append(b1(
    "For diseases such as <b>malaria</b> and <b>filariasis</b> that are transmitted through "
    "<b>insect vectors</b>, the <b>most important measure</b> is to <b>control or eliminate the "
    "vectors and their breeding places</b>. This can be achieved by:"))
story.append(b2("<b>avoiding stagnation of water</b> in and around residential areas;"))
story.append(b2("<b>regular cleaning of household coolers</b>;"))
story.append(b2("<b>use of mosquito nets</b>;"))
story.append(b2("introducing <b>fishes like <i>Gambusia</i></b> in ponds that <b>feed on mosquito "
                "larvae</b>;"))
story.append(b2("<b>spraying of insecticides</b> in <b>ditches, drainage areas and swamps</b>, etc.;"))
story.append(b2("providing <b>doors and windows with wire mesh</b> to <b>prevent the entry of "
                "mosquitoes</b>."))
# F074
story.append(body(
    "Such precautions have become <b>more important</b> especially in the light of <b>recent "
    "widespread incidences</b> of the <b>vector-borne (<i>Aedes</i> mosquitoes)</b> diseases like "
    "<b>dengue</b> and <b>chikungunya</b> in many parts of <b>India</b>."))
story.append(gap())
# F075, F076, F077, F078
story.append(b1(
    "The use of <b>vaccines and immunisation programmes</b> has enabled us to <b>completely "
    "eradicate</b> a deadly disease like <b>smallpox</b>."))
story.append(b1(
    "A large number of other infectious diseases like <b>polio</b>, <b>diphtheria</b>, "
    "<b>pneumonia</b> and <b>tetanus</b> have been <b>controlled to a large extent</b> by the use "
    "of vaccines."))
story.append(b1(
    "<b>Biotechnology</b> (about which you will read more in <b>Chapter 10</b>) is <b>at the verge "
    "of making available newer and safer vaccines</b>."))
story.append(b1(
    "<b>Discovery of antibiotics</b> and various other <b>drugs</b> has also enabled us to "
    "<b>effectively treat infectious diseases</b>."))
story.append(gap())

# INSERTION_POINT_2
