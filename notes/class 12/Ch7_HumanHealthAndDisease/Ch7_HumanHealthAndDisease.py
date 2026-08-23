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

# ======================================================================================
# ---- 7.2 IMMUNITY (F280 heading, F309 opener, F079-F081) ----
# ======================================================================================
story.append(heading("7.2", "IMMUNITY", 1))
# F309 (opener), F079
story.append(body(
    "<b>Everyday we are exposed to a large number of infectious agents.</b> However, <b>only a few "
    "of these exposures result in disease</b>. Why? This is due to the fact that the <b>body is "
    "able to defend itself from most of these foreign agents</b>."))
# F080, F081
story.append(keyterm(
    "This <b>overall ability of the host to fight the disease-causing organisms, conferred by the "
    "immune system, is called immunity</b>. Immunity is of <b>two types</b>: "
    "<b>(i) Innate immunity</b> and <b>(ii) Acquired immunity</b>."))
story.append(gap())

# ---- 7.2.1 Innate Immunity (F281 heading, F310 opener, F082-F087; F282-F285 + F311-F314) ----
story.append(heading("7.2.1", "Innate Immunity", 2, has_table=True))
# F310 (opener)
story.append(body(
    "<b>Innate immunity is non-specific type of defence, that is present at the time of birth.</b>"))
# F082, F083
story.append(body(
    "This is accomplished by <b>providing different types of barriers to the entry of the foreign "
    "agents into our body</b>. <b>Innate immunity consists of four types of barriers.</b>"))
# F282-F285 headings and F311-F314 openers, all four barriers as their own rows.
# NCERT sets (i)-(iii) in light italic and (iv) in bold italic; all four are the same
# structural level, so all four get a heading here (inventory 1-H class 3).
story.append(heading("7.2.1 (i)", "Physical barriers", 3))
# F084 = F311
story.append(body(
    "<b>Physical barriers:</b> <b>Skin</b> on our body is the <b>main barrier</b> which "
    "<b>prevents entry of the micro-organisms</b>. <b>Mucus coating of the epithelium</b> lining "
    "the <b>respiratory, gastrointestinal and urogenital tracts</b> also helps in <b>trapping "
    "microbes</b> entering our body."))
story.append(heading("7.2.1 (ii)", "Physiological barriers", 3))
# F085 = F312
story.append(body(
    "<b>Physiological barriers:</b> <b>Acid in the stomach</b>, <b>saliva in the mouth</b>, "
    "<b>tears from eyes</b> - <b>all prevent microbial growth</b>."))
story.append(heading("7.2.1 (iii)", "Cellular barriers", 3))
# F086 = F313
story.append(body(
    "<b>Cellular barriers:</b> Certain types of <b>leukocytes (WBC)</b> of our body like "
    "<b>polymorpho-nuclear leukocytes (PMNL-neutrophils)</b> and <b>monocytes</b> and <b>natural "
    "killer (type of lymphocytes)</b> in the blood, as well as <b>macrophages in tissues</b>, can "
    "<b>phagocytose and destroy microbes</b>."))
story.append(heading("7.2.1 (iv)", "Cytokine barriers", 3))
# F087 = F314
story.append(body(
    "<b>Cytokine barriers:</b> <b>Virus-infected cells secrete proteins called interferons</b> "
    "which <b>protect non-infected cells from further viral infection</b>."))
story.append(gap())
story.append(memory_aid(
    "The four innate barriers in NCERT's own order read <b>P-P-C-C</b>: <b>P</b>hysical, "
    "<b>P</b>hysiological, <b>C</b>ellular, <b>C</b>ytokine - skin first, then secretions, then "
    "cells, then the proteins cells secrete."))
story.append(gap())

# ---- 7.2.2 Acquired Immunity (F286 heading, F315 opener, F088-F103) + Figure 7.4 ----
story.append(heading("7.2.2", "Acquired Immunity", 2))
# F315 (opener), F088
story.append(body(
    "<b>Acquired immunity, on the other hand, is pathogen specific.</b> It is characterised by "
    "<b>memory</b>."))
# F089, F090
story.append(body(
    "When our body encounters a pathogen for the <b>first time</b> it produces a response called "
    "<b>primary response</b>, which is of <b>low intensity</b>. <b>Subsequent encounter with the "
    "same pathogen</b> elicits a <b>highly intensified secondary or anamnestic response</b>. This "
    "is ascribed to the fact that our body <b>appears to have memory of the first encounter</b>."))
# F091, F092, F093
story.append(body(
    "The <b>primary and secondary immune responses</b> are carried out with the help of <b>two "
    "special types of lymphocytes</b> present in our blood, i.e., <b>B-lymphocytes</b> and "
    "<b>T-lymphocytes</b>. The <b>B-lymphocytes produce an army of proteins</b> in response to "
    "pathogens into our blood to fight with them; these <b>proteins are called antibodies</b>. The "
    "<b>T-cells themselves do not secrete antibodies</b> but <b>help B cells to produce them</b>."))
story.append(gap())
# F094 + the fig 7.4 obligations (F102 N/C termini, F103 S-S disulfide bridges) and
# F339 labels, all in running text.
story.append(keyterm(
    "Each <b>antibody molecule</b> has <b>four peptide chains</b>: <b>two small called light "
    "chains</b> and <b>two longer called heavy chains</b>. Hence, an antibody is represented as "
    "<b>H<sub>2</sub>L<sub>2</sub></b>."))
story.append(body(
    "<b>Reading Figure 7.4:</b> the plate labels the two <b>Antigen binding site</b> regions at the "
    "top of the Y, each <b>Light chain</b> on the outside and each <b>Heavy chain</b> in the middle. "
    "Every chain is marked at its ends: <b>N</b> at the <b>amino terminus</b> and <b>C</b> at each "
    "<b>carboxyl terminus</b>. The <b>S-S</b> marks are <b>disulfide bonds</b> - the two heavy "
    "chains are held to each other, and each light chain to its heavy chain, by <b>disulfide "
    "bonds</b>."))
story.append(figure("fig_7_4.png", "Fig. 7.4 - Structure of an antibody molecule."))
story.append(gap())
# F095, F096, F097
story.append(body(
    "<b>Different types of antibodies</b> are produced in our body. <b>IgA</b>, <b>IgM</b>, "
    "<b>IgE</b>, <b>IgG</b> are some of them."))
story.append(data_table([
    ["Type of acquired immune response", "Carried out by", "Why it is named so"],
    ["<b>Humoral immune response</b> (antibody mediated)",
     "<b>Antibodies</b> produced by <b>B-lymphocytes</b>",
     "Because these <b>antibodies are found in the blood</b>. This is <b>one of the two types</b> "
     "of our acquired immune response."],
    ["<b>Cell-mediated immune response</b> or <b>cell-mediated immunity (CMI)</b>",
     "<b>T-lymphocytes</b> mediate CMI",
     "The <b>second type</b> - mediated by cells, not by antibodies in the blood."],
], col_widths=[30, 26, 44]))
story.append(gap())
# F098, F099, F100, F101 - transplantation
story.append(heading("7.2.2a", "Transplantation and graft rejection", 3))
story.append(body(
    "Very often, when some <b>human organs</b> like <b>heart, eye, liver, kidney</b> fail to "
    "function satisfactorily, <b>transplantation is the only remedy</b> to enable the patient to "
    "live a normal life."))
story.append(b1(
    "<b>Grafts from just any source</b> - an <b>animal</b>, <b>another primate</b>, or <b>any human "
    "beings</b> - <b>cannot be made</b>, since the grafts would be <b>rejected sooner or later</b>."))
story.append(b1(
    "<b>Tissue matching</b> and <b>blood group matching</b> are <b>essential</b> before undertaking "
    "any graft/transplant, and <b>even after this the patient has to take immuno-suppresants all "
    "his/her life</b>."))
story.append(b1(
    "The body is able to <b>differentiate 'self' and 'nonself'</b>, and the <b>cell-mediated immune "
    "response is responsible for the graft rejection</b>."))
story.append(gap())

# ---- 7.2.3 Active and Passive Immunity (F287 heading, F316 opener, F104-F109) ----
story.append(heading("7.2.3", "Active and Passive Immunity", 2, has_table=True))
# F316 (opener)
story.append(body(
    "When a <b>host is exposed to antigens</b>, which may be in the form of <b>living or dead "
    "microbes or other proteins</b>, <b>antibodies are produced in the host body</b>."))
# F104, F105, F106, F107
story.append(data_table([
    ["", "Active immunity", "Passive immunity"],
    ["What it is",
     "The immunity produced when the host itself makes antibodies after exposure to antigens.",
     "When <b>ready-made antibodies are directly given</b> to protect the body against foreign "
     "agents."],
    ["Speed",
     "<b>Slow</b> - <b>takes time to give its full effective response</b>.",
     "Immediate protection, because the antibodies are already formed."],
    ["How it is induced",
     "<b>Injecting the microbes deliberately during immunisation</b>, or <b>infectious organisms "
     "gaining access into body during natural infection</b>.",
     "Antibodies made elsewhere are transferred in."],
], col_widths=[16, 42, 42]))
story.append(gap())
# F108, F109
story.append(b1(
    "The <b>yellowish fluid colostrum</b> secreted by the mother during the <b>initial days of "
    "lactation</b> has <b>abundant antibodies (IgA)</b> to <b>protect the infant</b>."))
story.append(b1(
    "The <b>foetus</b> also receives <b>some antibodies from their mother, through the placenta "
    "during pregnancy</b>. These are some <b>examples of passive immunity</b>."))
story.append(gap())

# ---- 7.2.4 Vaccination and Immunisation (F288 heading, F317 opener, F110-F116) ----
story.append(heading("7.2.4", "Vaccination and Immunisation", 2))
# F317 (opener)
story.append(body(
    "The <b>principle of immunisation or vaccination</b> is based on the <b>property of 'memory' of "
    "the immune system</b>."))
# F110, F111, F112
story.append(process_flow([
    "In <b>vaccination</b>, a preparation of <b>antigenic proteins of pathogen</b> or "
    "<b>inactivated/weakened pathogen</b> (<b>vaccine</b>) is introduced into the body.",
    "The <b>antibodies produced in the body against these antigens</b> would <b>neutralise the "
    "pathogenic agents during actual infection</b>.",
    "The vaccines also <b>generate memory - B and T-cells</b> that <b>recognise the pathogen "
    "quickly on subsequent exposure</b> and <b>overwhelm the invaders with a massive production of "
    "antibodies</b>.",
]))
story.append(gap())
# F113, F114
story.append(body(
    "If a person is infected with some <b>deadly microbes to which quick immune response is "
    "required</b>, as in <b>tetanus</b>, we need to <b>directly inject the preformed antibodies</b>, "
    "or <b>antitoxin</b> (a preparation containing antibodies to the toxin). Even in cases of "
    "<b>snakebites</b>, the injection which is given to the patients <b>contains preformed "
    "antibodies against the snake venom</b>. This type of immunisation is called <b>passive "
    "immunisation</b>."))
# F115, F116
story.append(body(
    "<b>Recombinant DNA technology</b> has allowed the <b>production of antigenic polypeptides of "
    "pathogen in bacteria or yeast</b>. Vaccines produced using this approach allow <b>large scale "
    "production</b> and hence <b>greater availability for immunisation</b>, e.g., <b>hepatitis B "
    "vaccine produced from yeast</b>."))
story.append(gap())

# ---- 7.2.5 Allergies (F289 heading, F318 opener, F117-F126) ----
story.append(heading("7.2.5", "Allergies", 2))
# F318 (opener), F117
story.append(body(
    "When you have gone to a <b>new place</b> and suddenly you started <b>sneezing, wheezing</b> "
    "for no explained reason, and when you went away your <b>symptoms disappeared</b> - some of us "
    "are <b>sensitive to some particles in the environment</b>. The above-mentioned reaction could "
    "be because of <b>allergy to pollen, mites</b>, etc., which are <b>different in different "
    "places</b>."))
# F118, F119, F120, F121
story.append(keyterm(
    "The <b>exaggerated response of the immune system to certain antigens present in the "
    "environment</b> is called <b>allergy</b>. The <b>substances to which such an immune response "
    "is produced are called allergens</b>. The <b>antibodies produced to these are of IgE type</b>."))
story.append(b1(
    "<b>Common examples of allergens:</b> <b>mites in dust</b>, <b>pollens</b>, <b>animal "
    "dander</b>, etc."))
# F122, F123
story.append(b1(
    "<b>Symptoms:</b> <b>sneezing</b>, <b>watery eyes</b>, <b>running nose</b> and <b>difficulty in "
    "breathing</b>."))
story.append(b1(
    "<b>Cause:</b> allergy is due to the <b>release of chemicals like histamine and serotonin from "
    "the mast cells</b>."))
# F124, F125
story.append(b1(
    "<b>Determining the cause:</b> the patient is <b>exposed to or injected with very small doses "
    "of possible allergens</b>, and the <b>reactions studied</b>."))
story.append(b1(
    "<b>Treatment:</b> the use of drugs like <b>anti-histamine</b>, <b>adrenalin</b> and "
    "<b>steroids</b> <b>quickly reduce the symptoms of allergy</b>."))
# F126
story.append(note(
    "<b>Modern-day life style</b> has resulted in <b>lowering of immunity</b> and <b>more "
    "sensitivity to allergens</b> - <b>more and more children in metro cities of India suffer from "
    "allergies and asthma</b> due to <b>sensitivity to the environment</b>. This could be because of "
    "the <b>protected environment provided early in life</b>."))
story.append(gap())

# ---- 7.2.6 Auto Immunity (F290 heading, F319 opener, F127-F130) ----
story.append(heading("7.2.6", "Auto Immunity", 2))
# F319 (opener)
story.append(body(
    "<b>Memory-based acquired immunity evolved in higher vertebrates</b> based on the <b>ability to "
    "differentiate foreign organisms (e.g., pathogens) from self-cells</b>."))
# F127, F128, F129, F130
story.append(body(
    "While we <b>still do not understand the basis of this</b>, <b>two corollaries</b> of this "
    "ability have to be understood:"))
story.append(b1(
    "<b>One</b>, <b>higher vertebrates can distinguish foreign molecules as well as foreign "
    "organisms</b>. <b>Most of the experimental immunology deals with this aspect.</b>"))
story.append(b1(
    "<b>Two</b>, sometimes, due to <b>genetic and other unknown reasons</b>, the <b>body attacks "
    "self-cells</b>. This results in <b>damage to the body</b> and is called <b>auto-immune "
    "disease</b>."))
story.append(body(
    "<b>Rheumatoid arthritis</b>, which affects many people in our society, is an <b>auto-immune "
    "disease</b>."))
story.append(gap())

# ---- 7.2.7 Immune System in the Body (F291 heading, F320 opener, F131-F144) ----
story.append(heading("7.2.7", "Immune System in the Body", 2))
# F320 (opener)
story.append(body(
    "The <b>human immune system consists of lymphoid organs, tissues, cells and soluble molecules "
    "like antibodies</b>."))
# F131, F132
story.append(body(
    "The <b>immune system is unique</b> in the sense that it <b>recognises foreign antigens</b>, "
    "<b>responds to these</b> and <b>remembers them</b>. The immune system also plays an important "
    "role in <b>allergic reactions</b>, <b>auto-immune diseases</b> and <b>organ "
    "transplantation</b>."))
story.append(gap())
# F292 heading + F321 opener + F133-F136
story.append(heading("7.2.7a", "Lymphoid organs", 3, has_table=True))
story.append(keyterm(
    "<b>Lymphoid organs:</b> These are the <b>organs where origin and/or maturation and "
    "proliferation of lymphocytes occur</b>."))
story.append(data_table([
    ["Class", "Which organs", "What happens there"],
    ["<b>Primary</b> lymphoid organs",
     "<b>Bone marrow</b> and <b>thymus</b>",
     "<b>Immature lymphocytes differentiate into antigen-sensitive lymphocytes.</b>"],
    ["<b>Secondary</b> lymphoid organs",
     "<b>Spleen</b>, <b>lymph nodes</b>, <b>tonsils</b>, <b>Peyer's patches of small intestine</b> "
     "and <b>appendix</b>",
     "After maturation the lymphocytes <b>migrate</b> here. They <b>provide the sites for "
     "interaction of lymphocytes with the antigen</b>, which then <b>proliferate to become "
     "effector cells</b>."],
], col_widths=[22, 34, 44]))
story.append(gap())
# F137, F138, F139
story.append(b1(
    "<b>Bone marrow</b> is the <b>main lymphoid organ</b> where <b>all blood cells including "
    "lymphocytes are produced</b>."))
story.append(b1(
    "The <b>thymus</b> is a <b>lobed organ</b> located <b>near the heart</b> and <b>beneath the "
    "breastbone</b>. It is <b>quite large at the time of birth</b> but <b>keeps reducing in size "
    "with age</b>, and <b>by the time puberty is attained it reduces to a very small size</b>."))
story.append(b1(
    "<b>Both bone-marrow and thymus provide micro-environments for the development and maturation "
    "of T-lymphocytes.</b>"))
# F140
story.append(b1(
    "The <b>spleen</b> is a <b>large bean-shaped organ</b>. It <b>mainly contains lymphocytes and "
    "phagocytes</b>. It acts as a <b>filter of the blood</b> by <b>trapping blood-borne "
    "micro-organisms</b>. Spleen also has a <b>large reservoir of erythrocytes</b>."))
# F141, F142
story.append(b1(
    "The <b>lymph nodes</b> are <b>small solid structures</b> located at <b>different points along "
    "the lymphatic system</b>. They serve to <b>trap the micro-organisms or other antigens</b> which "
    "happen to <b>get into the lymph and tissue fluid</b>. <b>Antigens trapped in the lymph nodes "
    "are responsible for the activation of lymphocytes present there and cause the immune "
    "response.</b>"))
# F340 - Figure 7.5's three labels in running text
story.append(body(
    "<b>Reading Figure 7.5:</b> the plate marks the <b>Lymph nodes</b> at points along the body, the "
    "<b>Thymus</b> behind the breastbone, and the <b>Lymphatic vessels</b> that connect them."))
story.append(figure("fig_7_5.png",
                    "Fig. 7.5 - Diagrammatic representation of Lymph nodes.", max_width_cm=8.5))
story.append(gap())
# F143, F144
story.append(keyterm(
    "There is <b>lymphoid tissue also located within the lining of the major tracts</b> "
    "(<b>respiratory, digestive and urogenital tracts</b>) called <b>mucosa-associated lymphoid "
    "tissue (MALT)</b>. It constitutes <b>about 50 per cent of the lymphoid tissue in human "
    "body</b>."))
story.append(gap())

# INSERTION_POINT_3
