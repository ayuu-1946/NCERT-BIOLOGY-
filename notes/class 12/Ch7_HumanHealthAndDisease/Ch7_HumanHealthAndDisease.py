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

# ======================================================================================
# ---- 7.3 AIDS (F293 heading, F322 opener, F145-F176) + Figure 7.6 (F341 labels) ----
# ======================================================================================
story.append(heading("7.3", "AIDS", 1))
# F322 (opener), F145
story.append(keyterm(
    "The word <b>AIDS</b> stands for <b>Acquired Immuno Deficiency Syndrome</b>. This means "
    "<b>deficiency of immune system, acquired during the lifetime of an individual</b> - indicating "
    "that it is <b>not a congenital disease</b>. <b>'Syndrome' means a group of symptoms.</b>"))
# F146
story.append(body(
    "AIDS was <b>first reported in 1981</b> and in the <b>last twenty-five years or so</b>, it has "
    "<b>spread all over the world</b>, killing <b>more than 25 million persons</b>."))
# F147
story.append(keyterm(
    "AIDS is caused by the <b>Human Immuno deficiency Virus (HIV)</b>, a member of a group of "
    "viruses called <b>retrovirus</b>, which have an <b>envelope enclosing the RNA genome</b>."))
story.append(gap())
# F148 - NCERT's own four lettered routes, kept in its own (a)-(d) order
story.append(body("<b>Transmission of HIV-infection generally occurs by:</b>"))
story.append(b1("<b>(a)</b> <b>sexual contact with infected person</b>;"))
story.append(b1("<b>(b)</b> by <b>transfusion of contaminated blood and blood products</b>;"))
story.append(b1("<b>(c)</b> by <b>sharing infected needles</b> as in the case of <b>intravenous drug "
                "abusers</b>;"))
story.append(b1("<b>(d)</b> from <b>infected mother to her child through placenta</b>."))
story.append(gap())
# F149
story.append(body("<b>People who are at high risk of getting this infection</b> include:"))
story.append(b2("individuals who have <b>multiple sexual partners</b>;"))
story.append(b2("<b>drug addicts who take drugs intravenously</b>;"))
story.append(b2("individuals who <b>require repeated blood transfusions</b>;"))
story.append(b2("<b>children born to an HIV infected mother</b>."))
story.append(gap())
# F150, F151
story.append(note(
    "<b>HIV/AIDS is not spread by mere touch or physical contact; it spreads only through body "
    "fluids.</b> It is, hence, <b>imperative, for the physical and psychological well-being, that "
    "the HIV/AIDS infected persons are not isolated from family and society</b>."))
story.append(gap())
# F152
story.append(body(
    "There is <b>always a time-lag between the infection and appearance of AIDS symptoms</b>. This "
    "period <b>may vary from a few months to many years (usually 5-10 years)</b>."))
story.append(gap())
# F153-F156 as the replication flow, with Figure 7.6's eight in-plate process sentences
# (F169-F176) folded into the same steps so the plate's text exists in running prose.
story.append(body("<b>What HIV does after it gets into the body:</b>"))
story.append(process_flow([
    "After getting into the body of the person, the <b>virus enters into macrophages</b> - the "
    "<b>virus infects a normal cell</b> and <b>viral RNA is introduced into the cell</b>.",
    "Inside the macrophage, the <b>RNA genome of the virus replicates to form viral DNA</b> with "
    "the help of the enzyme <b>reverse transcriptase</b> - that is, <b>viral DNA is produced by "
    "reverse transcriptase</b>.",
    "This <b>viral DNA gets incorporated into host cell's DNA</b> - the <b>viral DNA incorporates "
    "into the host genome</b> - and <b>directs the infected cells to produce virus particles</b>: "
    "<b>new viral RNA is produced by the infected cell</b> and <b>new viruses are produced</b>, "
    "which <b>can infect other cells</b>.",
    "The <b>macrophages continue to produce virus</b> and in this way act like an <b>HIV "
    "factory</b>. On the plate this is set down as a note: the <b>infected cell can survive while "
    "viruses are being replicated and released</b>.",
    "Simultaneously, <b>HIV enters into helper T-lymphocytes (T<sub>H</sub>)</b>, <b>replicates</b> "
    "and <b>produces progeny viruses</b>.",
    "The <b>progeny viruses released in the blood attack other helper T-lymphocytes</b>. This is "
    "<b>repeated</b>, leading to a <b>progressive decrease in the number of helper T-lymphocytes</b> "
    "in the body of the infected person.",
]))
story.append(gap())
# F341 - all eight of Figure 7.6's labels, in running text (check 6)
story.append(body(
    "<b>Reading Figure 7.6:</b> the plate follows one <b>Retrovirus</b> into one <b>Animal cell</b>. "
    "The virus is drawn as a <b>Viral RNA core</b> inside a <b>Viral protein coat</b>. It fuses with "
    "the cell's <b>Plasma membrane</b>, releases its contents into the <b>Cytoplasm</b>, where "
    "reverse transcriptase makes <b>DNA</b> from the viral RNA, and that DNA then travels into the "
    "<b>Nucleus</b> to join the host genome."))
story.append(figure("fig_7_6.png", "Fig. 7.6 - Replication of retrovirus."))
story.append(gap())
# F157, F158, F159
story.append(b1(
    "During this period, the person suffers from <b>bouts of fever, diarrhoea and weight loss</b>."))
story.append(b1(
    "Due to the <b>decrease in the number of helper T lymphocytes</b>, the person <b>starts "
    "suffering from infections that could have been otherwise overcome</b> - such as those due to "
    "<b>bacteria especially <i>Mycobacterium</i></b>, <b>viruses</b>, <b>fungi</b> and even "
    "<b>parasites like <i>Toxoplasma</i></b>."))
story.append(b1(
    "The patient becomes <b>so immuno-deficient</b> that he/she is <b>unable to protect "
    "himself/herself against these infections</b>."))
story.append(gap())
# F160, F161
story.append(b1(
    "<b>Diagnosis:</b> a <b>widely used diagnostic test for AIDS</b> is <b>enzyme linked "
    "immuno-sorbent assay (ELISA)</b>."))
story.append(b1(
    "<b>Treatment:</b> treatment of AIDS with <b>anti-retroviral drugs</b> is <b>only partially "
    "effective</b>. They can <b>only prolong the life of the patient but cannot prevent death, "
    "which is inevitable</b>."))
story.append(gap())

# ---- 7.3 (a) Prevention of AIDS (F294 heading, F323 opener, F162-F168) ----
story.append(heading("7.3a", "Prevention of AIDS", 3))
# F323 (opener) = F162
story.append(body("As <b>AIDS has no cure</b>, <b>prevention is the best option</b>."))
# F163, F164
story.append(body(
    "<b>HIV infection, more often, spreads due to conscious behaviour patterns</b> and is <b>not "
    "something that happens inadvertently</b>, like pneumonia or typhoid. Infection in <b>blood "
    "transfusion patients</b>, <b>new-borns (from mother)</b>, etc., <b>may take place due to poor "
    "monitoring</b>. The <b>only excuse may be ignorance</b>, and it has been rightly said - "
    "<b>'don't die of ignorance'</b>."))
# F165
story.append(body(
    "In our country the <b>National AIDS Control Organisation (NACO)</b> and other "
    "<b>non-governmental organisations (NGOs)</b> are <b>doing a lot to educate people about "
    "AIDS</b>. <b>WHO</b> has started a <b>number of programmes to prevent the spreading of HIV "
    "infection</b>."))
# F166
story.append(body("<b>Some such steps taken up:</b>"))
story.append(b1("<b>making blood (from blood banks) safe from HIV</b>;"))
story.append(b1("<b>ensuring the use of only disposable needles and syringes</b> in <b>public and "
                "private hospitals and clinics</b>;"))
story.append(b1("<b>free distribution of condoms</b>;"))
story.append(b1("<b>controlling drug abuse</b>;"))
story.append(b1("<b>advocating safe sex</b>;"))
story.append(b1("<b>promoting regular check-ups for HIV in susceptible populations</b>."))
story.append(gap())
# F167, F168
story.append(note(
    "<b>Infection with HIV or having AIDS is something that should not be hidden</b> - since then, "
    "the <b>infection may spread to many more people</b>. <b>HIV/AIDS-infected people need help and "
    "sympathy instead of being shunned by society.</b> Unless <b>society recognises it as a problem "
    "to be dealt with in a collective manner</b>, the <b>chances of wider spread of the disease "
    "increase manifold</b>. It is a <b>malady that can only be tackled by the society and medical "
    "fraternity acting together</b>, to prevent the spread of the disease."))
story.append(gap())

# ======================================================================================
# ---- 7.4 CANCER (F295 heading, F324 opener, F177-F205) ----
# ======================================================================================
story.append(heading("7.4", "CANCER", 1))
# F324 (opener)
story.append(body(
    "<b>Cancer is one of the most dreaded diseases of human beings</b> and is a <b>major cause of "
    "death all over the globe</b>."))
# F177, F178
story.append(body(
    "<b>More than a million Indians suffer from cancer</b> and a <b>large number of them die from it "
    "annually</b>. The <b>mechanisms that underlie development of cancer</b>, or <b>oncogenic "
    "transformation of cells</b>, <b>its treatment and control</b> have been <b>some of the most "
    "intense areas of research in biology and medicine</b>."))
story.append(gap())
# F179, F180
story.append(body(
    "In our body, <b>cell growth and differentiation is highly controlled and regulated</b>. In "
    "<b>cancer cells there is breakdown of these regulatory mechanisms</b>."))
story.append(keyterm(
    "Normal cells show a property called <b>contact inhibition</b>, by virtue of which <b>contact "
    "with other cells inhibits their uncontrolled growth</b>. <b>Cancer cells appear to have lost "
    "this property.</b>"))
# F181, F182
story.append(keyterm(
    "Cancerous cells <b>just continue to divide</b>, giving rise to <b>masses of cells called "
    "tumors</b>. <b>Tumors are of two types: benign and malignant.</b>"))
story.append(gap())
# F183, F184, F185, F186 - the comparison NCERT sets out in prose, as a table
story.append(heading("7.4a", "Benign versus malignant tumors", 3, has_table=True))
story.append(data_table([
    ["", "Benign tumor", "Malignant tumor"],
    ["Where it stays",
     "<b>Normally remains confined to its original location</b> and <b>does not spread to other "
     "parts of the body</b>.",
     "A <b>mass of proliferating cells called neoplastic or tumor cells</b>."],
    ["Damage caused",
     "<b>Causes little damage.</b>",
     "These cells <b>grow very rapidly, invading and damaging the surrounding normal tissues</b>. As "
     "these cells <b>actively divide and grow</b> they also <b>starve the normal cells by competing "
     "for vital nutrients</b>."],
    ["Spread",
     "Does not spread.",
     "<b>Cells sloughed from such tumors reach distant sites through blood</b>, and <b>wherever they "
     "get lodged in the body, they start a new tumor there</b>. This property, called "
     "<b>metastasis</b>, is the <b>most feared property of malignant tumors</b>."],
], col_widths=[16, 34, 50]))
story.append(gap())
story.append(memory_aid(
    "<b>Benign stays, malignant travels.</b> The one word to attach to malignant tumors is "
    "<b>metastasis</b> - new tumors started at distant sites by cells carried there in the blood."))
story.append(gap())

# ---- 7.4 (a) Causes of cancer (F296 heading, F325 opener, F187-F191) ----
story.append(heading("7.4b", "Causes of cancer", 3))
# F325 (opener) = F187
story.append(keyterm(
    "<b>Transformation of normal cells into cancerous neoplastic cells</b> may be <b>induced by "
    "physical, chemical or biological agents</b>. These <b>agents are called carcinogens</b>."))
# F188, F189
story.append(b1(
    "<b>Ionising radiations</b> like <b>X-rays</b> and <b>gamma rays</b>, and <b>non-ionizing "
    "radiations</b> like <b>UV</b>, <b>cause DNA damage leading to neoplastic transformation</b>."))
story.append(b1(
    "The <b>chemical carcinogens present in tobacco smoke</b> have been identified as a <b>major "
    "cause of lung cancer</b>."))
# F190, F191
story.append(b1(
    "<b>Cancer causing viruses called oncogenic viruses have genes called viral oncogenes.</b>"))
story.append(b1(
    "Several genes called <b>cellular oncogenes (c-onc)</b> or <b>proto oncogenes</b> have been "
    "<b>identified in normal cells</b> which, <b>when activated under certain conditions</b>, could "
    "<b>lead to oncogenic transformation of the cells</b>."))
story.append(gap())

# ---- 7.4 (b) Cancer detection and diagnosis (F297 heading, F326 opener, F192-F200) ----
story.append(heading("7.4c", "Cancer detection and diagnosis", 3))
# F326 (opener) = F192
story.append(body(
    "<b>Early detection of cancers is essential</b> as it <b>allows the disease to be treated "
    "successfully in many cases</b>."))
# F193, F194
story.append(b1(
    "<b>Cancer detection is based on biopsy and histopathological studies of the tissue</b>, and "
    "<b>blood and bone marrow tests for increased cell counts in the case of leukemias</b>."))
story.append(b1(
    "In <b>biopsy</b>, a <b>piece of the suspected tissue cut into thin sections is stained and "
    "examined under microscope (histopathological studies) by a pathologist</b>."))
story.append(gap())
# F195, F196, F197 - the imaging techniques, as a table
story.append(data_table([
    ["Technique", "What it uses", "What it is used for"],
    ["<b>Radiography</b>", "Use of <b>X-rays</b>.",
     "Very useful to <b>detect cancers of the internal organs</b>."],
    ["<b>CT (computed tomography)</b>",
     "Uses <b>X-rays</b> to <b>generate a three-dimensional image of the internals of an "
     "object</b>.",
     "Very useful to <b>detect cancers of the internal organs</b>."],
    ["<b>MRI (magnetic resonance imaging)</b>",
     "Uses <b>strong magnetic fields</b> and <b>non-ionising radiations</b>.",
     "<b>Accurately detects pathological and physiological changes in the living tissue</b>."],
], col_widths=[24, 38, 38]))
story.append(gap())
# F198, F199, F200
story.append(b1(
    "<b>Antibodies against cancer-specific antigens</b> are also <b>used for detection of certain "
    "cancers</b>."))
story.append(b1(
    "<b>Techniques of molecular biology</b> can be applied to <b>detect genes in individuals with "
    "inherited susceptibility to certain cancers</b>."))
story.append(b1(
    "<b>Identification of such genes, which predispose an individual to certain cancers, may be "
    "very helpful in prevention of cancers.</b> Such individuals <b>may be advised to avoid exposure "
    "to particular carcinogens to which they are susceptible</b> (e.g., <b>tobacco smoke in case of "
    "lung cancer</b>)."))
story.append(gap())

# ---- 7.4 (c) Treatment of cancer (F298 heading, F327 opener, F201-F205) ----
# F205's "alpha-interferon" is written out in words: the Greek letter is a banned glyph
# under check 5 (inventory carry-over 8).
story.append(heading("7.4d", "Treatment of cancer", 3))
# F327 (opener) = F201
story.append(body(
    "The <b>common approaches for treatment of cancer</b> are <b>surgery</b>, <b>radiation "
    "therapy</b> and <b>immunotherapy</b>."))
# F202, F203, F204
story.append(b1(
    "In <b>radiotherapy</b>, <b>tumor cells are irradiated lethally</b>, <b>taking proper care of "
    "the normal tissues surrounding the tumor mass</b>."))
story.append(b1(
    "Several <b>chemotherapeutic drugs</b> are used to <b>kill cancerous cells</b>. <b>Some of these "
    "are specific for particular tumors.</b> <b>Majority of drugs have side effects</b> like <b>hair "
    "loss</b>, <b>anemia</b>, etc."))
story.append(b1(
    "<b>Most cancers are treated by combination of surgery, radiotherapy and chemotherapy.</b>"))
story.append(gap())
# F205
story.append(keyterm(
    "<b>Tumor cells have been shown to avoid detection and destruction by immune system.</b> "
    "Therefore, the patients are <b>given substances called biological response modifiers</b> such "
    "as <b>alpha-interferon</b>, which <b>activates their immune system</b> and <b>helps in "
    "destroying the tumor</b>."))
story.append(gap())

# ======================================================================================
# ---- 7.5 DRUGS AND ALCOHOL ABUSE (F299 heading, F328 opener, F206-F233) ----
# ---- Figures 7.7-7.11 (F342-F346: none of these five plates carries a descriptive
# ---- callout, so check 6 has no rows to satisfy here; each is still embedded.)
# ======================================================================================
story.append(heading("7.5", "DRUGS AND ALCOHOL ABUSE", 1))
# F328 (opener), F206
story.append(body(
    "<b>Surveys and statistics show that use of drugs and alcohol has been on the rise especially "
    "among the youth.</b> This is <b>really a cause of concern</b> as it <b>could result in many "
    "harmful effects</b>. <b>Proper education and guidance would enable youth to safeguard "
    "themselves against these dangerous behaviour patterns and follow healthy lifestyles.</b>"))
# F207
story.append(keyterm(
    "The <b>drugs which are commonly abused</b> are <b>opioids</b>, <b>cannabinoids</b> and <b>coca "
    "alkaloids</b>. <b>Majority of these are obtained from flowering plants.</b> <b>Some are obtained "
    "from fungi.</b>"))
story.append(gap())

# ---- 7.5 (a) Opioids (F208-F211) + Figures 7.7, 7.8 ----
story.append(heading("7.5a", "Opioids", 3))
# F208
story.append(keyterm(
    "<b>Opioids</b> are the drugs which <b>bind to specific opioid receptors</b> present in our "
    "<b>central nervous system</b> and <b>gastrointestinal tract</b>."))
# F209, F210, F211
story.append(b1(
    "<b>Heroin</b>, commonly called <b>smack</b>, is chemically <b>diacetylmorphine</b> - a "
    "<b>white, odourless, bitter crystalline compound</b>."))
story.append(b1(
    "This is obtained by <b>acetylation of morphine</b>, which is <b>extracted from the latex of "
    "poppy plant <i>Papaver somniferum</i></b>."))
story.append(b1(
    "Generally taken by <b>snorting</b> and <b>injection</b>, <b>heroin is a depressant</b> and "
    "<b>slows down body functions</b>."))
story.append(gap())
# F342 - fig 7.7 carries only atom/group symbols, no descriptive callouts
story.append(figure("fig_7_7.png",
                    "Fig. 7.7 - Chemical structure of Morphine. The plate is a skeletal formula "
                    "carrying only atom and group symbols (HO, O, H, N and CH<sub>3</sub>) and no "
                    "descriptive labels.", max_width_cm=7.5))
# F343 - fig 7.8 is unlabelled
story.append(figure("fig_7_8.png",
                    "Fig. 7.8 - Opium poppy. An unlabelled illustration of the poppy plant "
                    "<i>Papaver somniferum</i>, from whose latex morphine is extracted.",
                    max_width_cm=6.5))
story.append(gap())

# ---- 7.5 (b) Cannabinoids (F212-F215, F220) + Figures 7.9, 7.10 ----
story.append(heading("7.5b", "Cannabinoids", 3))
# F212
story.append(keyterm(
    "<b>Cannabinoids</b> are a <b>group of chemicals</b> which <b>interact with cannabinoid "
    "receptors</b> present <b>principally in the brain</b>."))
# F213, F214, F215
story.append(b1(
    "<b>Natural cannabinoids are obtained from the inflorescences of the plant <i>Cannabis "
    "sativa</i>.</b>"))
story.append(b1(
    "The <b>flower tops</b>, <b>leaves</b> and the <b>resin</b> of the cannabis plant are <b>used in "
    "various combinations</b> to produce <b>marijuana</b>, <b>hashish</b>, <b>charas</b> and "
    "<b>ganja</b>."))
story.append(b1(
    "Generally taken by <b>inhalation</b> and <b>oral ingestion</b>, these are <b>known for their "
    "effects on cardiovascular system of the body</b>."))
# F220
story.append(b1("<b>These days cannabinoids are also being abused by some sportspersons.</b>"))
story.append(gap())
# F344 - fig 7.9 carries only atom/group symbols
story.append(figure("fig_7_9.png",
                    "Fig. 7.9 - Skeletal structure of cannabinoid molecule. The plate is a skeletal "
                    "formula carrying only atom and group symbols (OH, O and H) and no descriptive "
                    "labels.", max_width_cm=8.0))
# F345 - fig 7.10 is unlabelled
story.append(figure("fig_7_10.png",
                    "Fig. 7.10 - Leaves of <i>Cannabis sativa</i>. An unlabelled framed "
                    "illustration of the leaf of the plant whose inflorescences yield the natural "
                    "cannabinoids.", max_width_cm=6.0))
story.append(gap())

# ---- 7.5 (c) Coca alkaloids and hallucinogens (F216-F219) + Figure 7.11 ----
story.append(heading("7.5c", "Coca alkaloids and other hallucinogenic plants", 3))
# F216, F217, F218
story.append(keyterm(
    "<b>Coca alkaloid</b> or <b>cocaine</b> is obtained from <b>coca plant <i>Erythroxylum "
    "coca</i></b>, <b>native to South America</b>. It <b>interferes with the transport of the "
    "neuro-transmitter dopamine</b>."))
story.append(b1(
    "<b>Cocaine</b>, commonly called <b>coke</b> or <b>crack</b>, is <b>usually snorted</b>. It has "
    "a <b>potent stimulating action on central nervous system</b>, producing a <b>sense of euphoria "
    "and increased energy</b>. <b>Excessive dosage of cocaine causes hallucinations.</b>"))
# F219
story.append(b1(
    "<b>Other well-known plants with hallucinogenic properties</b> are <b><i>Atropa belladona</i></b> "
    "and <b><i>Datura</i></b>."))
# F346 - fig 7.11 is unlabelled
story.append(figure("fig_7_11.png",
                    "Fig. 7.11 - Flowering branch of <i>Datura</i>. An unlabelled illustration of a "
                    "flowering branch of <i>Datura</i>, one of the two well-known plants with "
                    "hallucinogenic properties named above.", max_width_cm=7.0))
story.append(gap())

# ---- 7.5 (d) Drugs abused as medicines, and what drug abuse means (F221-F224) ----
story.append(heading("7.5d", "Medicines that are abused, and what drug abuse means", 3))
# F221, F222, F223
story.append(b1(
    "Drugs like <b>barbiturates</b>, <b>amphetamines</b>, <b>benzodiazepines</b>, and <b>other "
    "similar drugs</b>, that are <b>normally used as medicines to help patients cope with mental "
    "illnesses like depression and insomnia</b>, are <b>often abused</b>."))
story.append(b1(
    "<b>Morphine is a very effective sedative and painkiller</b>, and is <b>very useful in patients "
    "who have undergone surgery</b>."))
story.append(b1(
    "<b>Several plants, fruits and seeds having hallucinogenic properties have been used for "
    "hundreds of years in folk-medicine, religious ceremonies and rituals all over the globe.</b>"))
story.append(gap())
# F224 - the definition of drug abuse
story.append(keyterm(
    "When these are <b>taken for a purpose other than medicinal use</b>, or <b>in amounts/frequency "
    "that impairs one's physical, physiological or psychological functions</b>, it constitutes "
    "<b>drug abuse</b>."))
story.append(gap())

# ---- 7.5 (e) Tobacco (F225-F233) ----
story.append(heading("7.5e", "Tobacco and smoking", 3))
# F226, F227
story.append(body(
    "<b>Tobacco has been used by human beings for more than 400 years.</b> It is <b>smoked</b>, "
    "<b>chewed</b> or <b>used as a snuff</b>. Tobacco <b>contains a large number of chemical "
    "substances including nicotine, an alkaloid</b>."))
# F228
story.append(b1(
    "<b>Nicotine stimulates adrenal gland to release adrenaline and nor-adrenaline into blood "
    "circulation</b>, <b>both of which raise blood pressure and increase heart rate</b>."))
# F229, F230
story.append(b1(
    "<b>Smoking is associated with increased incidence of cancers of lung, urinary bladder and "
    "throat</b>, <b>bronchitis</b>, <b>emphysema</b>, <b>coronary heart disease</b>, <b>gastric "
    "ulcer</b>, etc."))
story.append(b1(
    "<b>Tobacco chewing is associated with increased risk of cancer of the oral cavity.</b>"))
# F231
story.append(b1(
    "<b>Smoking increases carbon monoxide (CO) content in blood</b> and <b>reduces the concentration "
    "of haem-bound oxygen</b>. This <b>causes oxygen deficiency in the body</b>."))
# F225
story.append(b1("<b>Smoking also paves the way to hard drugs.</b>"))
story.append(gap())
# F232, F233
story.append(note(
    "When one buys packets of cigarettes one <b>cannot miss the statutory warning</b> that is "
    "present on the packing, which <b>warns against smoking and says how it is injurious to "
    "health</b>. <b>Knowing the dangers of smoking and chewing tobacco, and its addictive nature, "
    "the youth and old need to avoid these habits.</b> <b>Any addict requires counselling and "
    "medical help to get rid of the habit.</b>"))
story.append(gap())

# ---- 7.5.1 Adolescence and Drug/Alcohol Abuse (F300 heading, F329 opener, F234-F242) ----
story.append(heading("7.5.1", "Adolescence and Drug/Alcohol Abuse", 2))
# F329 (opener)
story.append(keyterm(
    "<b>Adolescence</b> means <b>both 'a period' and 'a process'</b> during which a <b>child becomes "
    "mature in terms of his/her attitudes and beliefs for effective participation in society</b>."))
# F234, F235, F236
story.append(b1(
    "The <b>period between 12-18 years of age</b> may be thought of as <b>adolescence period</b>. In "
    "other words, <b>adolescence is a bridge linking childhood and adulthood</b>."))
story.append(b1(
    "<b>Adolescence is accompanied by several biological and behavioural changes.</b> Adolescence, "
    "thus, is a <b>very vulnerable phase of mental and psychological development of an "
    "individual</b>."))
story.append(gap())
# F237-F242 - what motivates youngsters (exercise 17 leans on this whole block)
story.append(body("<b>What motivates youngsters towards drug and alcohol use:</b>"))
story.append(b1(
    "<b>Curiosity</b>, <b>need for adventure and excitement</b>, and <b>experimentation</b> "
    "constitute <b>common causes</b>. A <b>child's natural curiosity motivates him/her to "
    "experiment</b>. This is <b>complicated further by effects that might be perceived as "
    "benefits</b>, of alcohol or drug use."))
story.append(b1(
    "The <b>first use of drugs or alcohol may be out of curiosity or experimentation</b>, but "
    "<b>later the child starts using these to escape facing problems</b>."))
story.append(b1(
    "Of late, <b>stress, from pressures to excel in academics or examinations</b>, has <b>played a "
    "significant role in persuading the youngsters to try alcohol and drugs</b>."))
story.append(b1(
    "The <b>perception among youth that it is 'cool' or progressive to smoke, use drugs or "
    "alcohol</b>, is also in a way a <b>major cause</b> for youth to start these habits. "
    "<b>Television</b>, <b>movies</b>, <b>newspapers</b> and <b>internet</b> also <b>help to promote "
    "this perception</b>."))
story.append(b1(
    "<b>Other factors</b> that have been seen to be associated with drug and alcohol abuse among "
    "adolescents are <b>unstable or unsupportive family structures</b> and <b>peer pressure</b>."))
story.append(gap())

# ---- 7.5.2 Addiction and Dependence (F301 heading, F330 opener, F243-F252) ----
story.append(heading("7.5.2", "Addiction and Dependence", 2))
# F330 (opener), F243
story.append(body(
    "<b>Because of the perceived benefits, drugs are frequently used repeatedly.</b> The <b>most "
    "important thing, which one fails to realise, is the inherent addictive nature of alcohol and "
    "drugs</b>."))
# F244, F245
story.append(keyterm(
    "<b>Addiction</b> is a <b>psychological attachment to certain effects</b> - such as <b>euphoria "
    "and a temporary feeling of well-being</b> - associated with drugs and alcohol. These <b>drive "
    "people to take them even when these are not needed, or even when their use becomes "
    "self-destructive</b>."))
# F246
story.append(body(
    "<b>With repeated use of drugs, the tolerance level of the receptors present in our body "
    "increases.</b> Consequently the <b>receptors respond only to higher doses of drugs or "
    "alcohol</b>, <b>leading to greater intake and addiction</b>."))
# F247, F248
story.append(b1(
    "It should be <b>clearly borne in mind that use of these drugs even once, can be a fore-runner "
    "to addiction</b>."))
story.append(b1(
    "The <b>addictive potential of drugs and alcohol pull the user into a vicious circle</b>, "
    "leading to their <b>regular use (abuse) from which he/she may not be able to get out</b>. In "
    "the <b>absence of any guidance or counselling</b>, the <b>person gets addicted and becomes "
    "dependent on their use</b>."))
story.append(gap())
# F249, F250, F251, F252
story.append(keyterm(
    "<b>Dependence</b> is the <b>tendency of the body to manifest a characteristic and unpleasant "
    "withdrawal syndrome if regular dose of drugs/alcohol is abruptly discontinued</b>."))
story.append(b1(
    "This is <b>characterised by anxiety, shakiness, nausea and sweating</b>, which <b>may be "
    "relieved when use is resumed again</b>."))
story.append(b1(
    "<b>In some cases, withdrawal symptoms can be severe and even life threatening</b> and the "
    "<b>person may need medical supervision</b>."))
story.append(b1(
    "<b>Dependence leads the patient to ignore all social norms</b> in order to <b>get sufficient "
    "funds to satiate his/her needs</b>. These <b>result in many social adjustment problems</b>."))
story.append(gap())

# ---- 7.5.3 Effects of Drug/Alcohol Abuse (F302 heading, F331 opener, F253-F268) ----
story.append(heading("7.5.3", "Effects of Drug/Alcohol Abuse", 2))
# F331 (opener)
story.append(body(
    "The <b>immediate adverse effects of drugs and alcohol abuse</b> are <b>manifested in the form "
    "of reckless behaviour, vandalism and violence</b>."))
# F253, F254
story.append(b1(
    "<b>Excessive doses of drugs may lead to coma and death due to respiratory failure, heart "
    "failure or cerebral hemorrhage.</b>"))
story.append(b1(
    "A <b>combination of drugs</b>, or <b>their intake along with alcohol</b>, <b>generally results "
    "in overdosing and even deaths</b>."))
story.append(gap())
# F255 - the warning signs, the exercise-14/17 block
story.append(body("<b>The most common warning signs of drug and alcohol abuse among youth:</b>"))
story.append(b2("<b>drop in academic performance</b>;"))
story.append(b2("<b>unexplained absence from school/college</b>;"))
story.append(b2("<b>lack of interest in personal hygiene</b>;"))
story.append(b2("<b>withdrawal</b>, <b>isolation</b>, <b>depression</b>, <b>fatigue</b>;"))
story.append(b2("<b>aggressive and rebellious behaviour</b>;"))
story.append(b2("<b>deteriorating relationships with family and friends</b>;"))
story.append(b2("<b>loss of interest in hobbies</b>;"))
story.append(b2("<b>change in sleeping and eating habits</b>;"))
story.append(b2("<b>fluctuations in weight, appetite</b>, etc."))
story.append(gap())
# F256, F257
story.append(b1(
    "If an <b>abuser is unable to get money to buy drugs/alcohol he/she may turn to stealing</b>."))
story.append(b1(
    "At times, a <b>drug/alcohol addict becomes the cause of mental and financial distress to "
    "his/her entire family and friends</b>."))
story.append(gap())
# F258, F259, F260
story.append(note(
    "Those who <b>take drugs intravenously</b> (<b>direct injection into the vein using a needle and "
    "syringe</b>) are <b>much more likely to acquire serious infections like AIDS and Hepatitis "
    "B</b>. The <b>viruses which are responsible for these diseases are transferred from one person "
    "to another by sharing of infected needles and syringes</b>. <b>Both AIDS and Hepatitis B "
    "infections are chronic infections and ultimately fatal.</b> <b>Both can be transmitted through "
    "sexual contact or infected blood.</b>"))
story.append(gap())
# F261, F262, F263
story.append(b1(
    "The <b>use of alcohol during adolescence may also have long-term effects</b>. It <b>could lead "
    "to heavy drinking in adulthood</b>."))
story.append(b1(
    "The <b>chronic use of drugs and alcohol damages nervous system and liver (cirrhosis)</b>."))
story.append(b1(
    "The <b>use of drugs and alcohol during pregnancy is also known to adversely affect the "
    "foetus</b>."))
story.append(gap())
# F264 - doping in sport
story.append(body(
    "<b>Another misuse of drugs</b> is what <b>certain sportspersons do to enhance their "
    "performance</b>. They <b>(mis)use narcotic analgesics, anabolic steroids, diuretics and certain "
    "hormones in sports</b> to <b>increase muscle strength and bulk</b> and to <b>promote "
    "aggressiveness</b>, and as a result <b>increase athletic performance</b>."))
# F265, F266 - the two side-effect lists, kept separate as NCERT does
story.append(data_table([
    ["Side-effects of anabolic steroids", "What NCERT lists"],
    ["<b>In females</b>",
     "<b>Masculinisation (features like males)</b>, <b>increased aggressiveness</b>, <b>mood "
     "swings</b>, <b>depression</b>, <b>abnormal menstrual cycles</b>, <b>excessive hair growth on "
     "the face and body</b>, <b>enlargement of clitoris</b>, <b>deepening of voice</b>."],
    ["<b>In males</b>",
     "<b>Acne</b>, <b>increased aggressiveness</b>, <b>mood swings</b>, <b>depression</b>, "
     "<b>reduction of size of the testicles</b>, <b>decreased sperm production</b>, <b>potential for "
     "kidney and liver dysfunction</b>, <b>breast enlargement</b>, <b>premature baldness</b>, "
     "<b>enlargement of the prostate gland</b>."],
    ["<b>In the adolescent male or female</b>",
     "<b>Severe facial and body acne</b>, and <b>premature closure of the growth centres of the "
     "long bones</b>, which <b>may result in stunted growth</b>."],
], col_widths=[26, 74]))
# F267
story.append(body("<b>These effects may be permanent with prolonged use.</b>"))
story.append(gap())

# ---- 7.5.4 Prevention and Control (F303 heading, F332 opener, F269-F276) ----
story.append(heading("7.5.4", "Prevention and Control", 2))
# F332 (opener)
story.append(body(
    "The <b>age-old adage of 'prevention is better than cure' holds true here also</b>."))
# F269, F270, F271
story.append(body(
    "It is also true that <b>habits such as smoking, taking drug or alcohol are more likely to be "
    "taken up at a young age, more during adolescence</b>. Hence, it is <b>best to identify the "
    "situations that may push an adolescent towards use of drugs or alcohol, and to take remedial "
    "measures well in time</b>. In this regard, <b>the parents and the teachers have a special "
    "responsibility</b>."))
story.append(b1(
    "<b>Parenting that combines with high levels of nurturance and consistent discipline has been "
    "associated with lowered risk of substance (alcohol/drugs/tobacco) abuse.</b>"))
story.append(gap())
# F272-F276 - NCERT's five named measures, kept under their own run-in names
story.append(body("<b>NCERT's named measures:</b>"))
story.append(process_flow([
    "<b>Avoid undue peer pressure</b> - <b>every child has his/her own choice and personality, "
    "which should be respected and nurtured</b>. A <b>child should not be pushed unduly to perform "
    "beyond his/her threshold limits</b>; be it <b>studies, sports or other activities</b>.",
    "<b>Education and counselling</b> - <b>educating and counselling him/her to face problems and "
    "stresses, and to accept disappointments and failures as a part of life</b>. It would also be "
    "<b>worthwhile to channelise the child's energy into healthy pursuits</b> like <b>sports, "
    "reading, music, yoga and other extracurricular activities</b>.",
    "<b>Seeking help from parents and peers</b> - <b>help from parents and peers should be sought "
    "immediately so that they can guide appropriately</b>. <b>Help may even be sought from close and "
    "trusted friends.</b> Besides <b>getting proper advise to sort out their problems</b>, this "
    "would <b>help young to vent their feelings of anxiety and guilt</b>.",
    "<b>Looking for danger signs</b> - <b>alert parents and teachers need to look for and identify "
    "the danger signs discussed above</b>. <b>Even friends, if they find someone using drugs or "
    "alcohol, should not hesitate to bring this to the notice of parents or teacher in the best "
    "interests of the person concerned.</b> <b>Appropriate measures would then be required to "
    "diagnose the malady and the underlying causes</b>, which <b>would help in initiating proper "
    "remedial steps or treatment</b>.",
    "<b>Seeking professional and medical help</b> - <b>a lot of help is available in the form of "
    "highly qualified psychologists, psychiatrists, and de-addiction and rehabilitation "
    "programmes</b> to <b>help individuals who have unfortunately got in the quagmire of "
    "drug/alcohol abuse</b>. <b>With such help, the affected individual with sufficient efforts and "
    "will power can get rid of the problem completely and lead a perfectly normal and healthy "
    "life.</b>",
]))
story.append(gap())

# ======================================================================================
# ---- Quick Recap (F304 heading "SUMMARY", F333 opener) ----
# A rewritten, denser version of NCERT's 18-sentence summary, NOT a copy of it (SS3).
# The two SUMMARY-UNIQUE facts are NOT introduced here for the first time - F334 is
# written into the intro and F335 into 7.1, as the freeze requires.
# ======================================================================================
story.append(heading("Recap", "QUICK RECAP", 1))
# F333 (opener)
story.append(body(
    "<b>Health is not just the absence of disease.</b> It is a <b>state of complete physical, "
    "mental, social and psychological well-being</b> - the definition the chapter summary uses, "
    "adding <b>psychological</b> to the body's three."))
story.append(b1(
    "Diseases like <b>typhoid</b>, <b>cholera</b>, <b>pneumonia</b>, <b>fungal infections of "
    "skin</b> and <b>malaria</b> are a <b>major cause of distress</b>. <b>Vector-borne diseases "
    "like malaria, especially one caused by <i>P. falciparum</i>, if not treated, may prove "
    "fatal.</b>"))
story.append(b1(
    "Such diseases can be checked by <b>public health measures</b> - <b>proper disposal of waste</b>, "
    "<b>decontamination of drinking water</b> and <b>control of vectors</b>."))
story.append(b1(
    "Our <b>immune system plays the major role in preventing these diseases</b>. The <b>innate "
    "defences</b> - <b>skin</b>, <b>mucous membranes</b>, <b>antimicrobial substances</b> in "
    "<b>tears</b> and <b>saliva</b>, and the <b>phagocytic cells</b> - act first and "
    "non-specifically."))
story.append(b1(
    "Beyond them, <b>specific antibodies (humoral immune response)</b> and <b>cells (cell mediated "
    "immune response)</b> serve to <b>kill these pathogens</b>."))
story.append(b1(
    "<b>Immune system has memory.</b> <b>On subsequent exposure to the same pathogen, the immune "
    "response is rapid and more intense.</b> <b>This forms the basis of protection afforded by "
    "vaccination and immunisation.</b>"))
story.append(b1(
    "<b>Among other diseases, AIDS and cancer kill a large number of individuals worldwide.</b> "
    "<b>AIDS, caused by the human immuno-deficiency virus (HIV), is fatal but can be prevented if "
    "certain precautions are taken.</b> <b>Many cancers are curable if detected early and "
    "appropriate therapeutic measures are taken.</b>"))
story.append(b1(
    "<b>Of late, drug and alcohol abuse among youth and adolescents is becoming another cause of "
    "concern.</b> Because of their <b>addictive nature</b> and <b>perceived benefits like relief "
    "from stress</b>, and because of <b>peer pressure</b> and <b>examinations-related and "
    "competition-related stresses</b>, a young person may try them - and <b>in doing so, he/she may "
    "get addicted to them</b>."))
story.append(b1(
    "<b>Education about their harmful effects</b>, <b>counselling</b> and <b>seeking immediate "
    "professional and medical help</b> are what get an affected individual out."))
story.append(gap())

# ======================================================================================
# ---- Terms used in the exercises (F305 heading "EXERCISES"; Rule 2 appendix) ----
# Frozen plan: 2 gaps out of 17 exercises. The "water-borne" terminology gap is closed
# inline in 7.1's prevention block above (F067-F069), so only the genuine content gap
# (Ex 5, DNA vaccines) is written here. Rule 5 forbids importing the DNA-vaccine
# mechanism from Chapter 10 (inventory carry-over 6).
# ======================================================================================
story.append(heading("App.", "TERMS USED IN THE EXERCISES", 1))
story.append(body(
    "The <b>exercises</b> at the end of this NCERT chapter lean on <b>two things the chapter itself "
    "never spells out</b>. Both are settled here so that a reader who never opens the book can still "
    "answer every question."))
story.append(gap())
story.append(heading("App. 1", "\"Water-borne\" diseases", 3))
story.append(body(
    "NCERT names the <b>route</b> but never the <b>grouping</b>: it writes <b>air-borne</b> and "
    "<b>vector-borne</b>, yet for food and water it only ever says <b>'transmitted through food and "
    "water'</b>. The diseases in <b>this chapter</b> that travel that way - and so are the ones a "
    "question calling them <b>water-borne</b> is asking about - are <b>typhoid</b>, "
    "<b>amoebiasis</b> and <b>ascariasis</b>. This is stated where the prevention measures are "
    "covered, in section 7.1."))
story.append(gap())
story.append(heading("App. 2", "\"DNA vaccines\" and \"a suitable gene\"", 3))
story.append(body(
    "The exercise asking about <b>DNA vaccines</b> and injecting <b>a suitable gene</b> uses two "
    "terms that <b>do not occur anywhere in this chapter</b>. NCERT's own wording for that question "
    "is <b>\"Discuss with your teacher\"</b>, which concedes the point."))
story.append(body("<b>What this chapter does support:</b>"))
story.append(b1(
    "<b>Recombinant DNA technology</b> has allowed the <b>production of antigenic polypeptides of "
    "pathogen in bacteria or yeast</b> (section 7.2.4). Vaccines made this way allow <b>large scale "
    "production</b> and hence <b>greater availability for immunisation</b> - e.g., the <b>hepatitis "
    "B vaccine produced from yeast</b>."))
story.append(b1(
    "Note carefully that this is a <b>different class of vaccine</b>. It delivers a "
    "<b>protein</b> - an antigenic polypeptide manufactured outside the body - whereas a "
    "<b>DNA vaccine</b> would deliver a <b>gene</b>."))
story.append(note(
    "<b>The mechanism of a DNA vaccine is outside the scope of this chapter.</b> Nothing in Chapter "
    "7 explains how injecting a gene produces immunity, so nothing here is invented to fill the gap. "
    "Read it up in <b>Chapter 10 (Biotechnology and its Applications)</b>, which section 7.1 itself "
    "points forward to when it notes that <b>biotechnology is at the verge of making available newer "
    "and safer vaccines</b>."))
story.append(gap())


# ======================================================================================
# ---- Build ----
# ======================================================================================
def main():
    build_pdf(
        OUT_PDF,
        story,
        title="Human Health and Disease - NEET Notes (NCERT Class 12, Chapter 7)",
        subject="NCERT Class 12 Biology, Chapter 7 - Human Health and Disease: "
                "NEET replacement notes",
    )


if __name__ == "__main__":
    main()
