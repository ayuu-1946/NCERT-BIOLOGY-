"""
NCERT Class 11 Biology, Chapter 14 - Breathing and Exchange of Gases
NEET replacement notes -> A4 print-ready PDF.

Built under SUPREME COMMAND PROMPT.md v6, Pass 2: written linearly from the
frozen 139-row inventory (Ch14_BreathingAndExchangeOfGases_inventory.md),
importing the repo-level frozen style module `neet_template.py` (v6 SS0.6).
No style, geometry, colour or font is re-declared here.

Block markers `# ---- N.N ----` mark every NCERT section so a Pass 3 flag can be
found and fixed in one contiguous block. Inventory row IDs are named in the
comments so any fact can be traced back to its frozen row.

Subscripts: the inventory stores O2/CO2 with Unicode subscript digits for
human readability, but check_pdf.py check 5 bans Unicode sub/superscripts in
the PDF text stream, so every one is written here as a <sub> tag instead.

Source: Chapter/class 11/Chapter 14 - Breathing and Exchange of Gases.pdf
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
    STYLES, FRAME_WIDTH, DARK_GREY, GRID_LINE,
    heading, keyterm, process_flow, note, memory_aid, data_table, title_block, build_pdf,
)
from neet_template import figure as _shared_figure  # noqa: E402
from reportlab.platypus import Paragraph  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch14_BreathingAndExchangeOfGases.pdf")

O2 = "O<sub>2</sub>"
CO2 = "CO<sub>2</sub>"
PO2 = "pO<sub>2</sub>"
PCO2 = "pCO<sub>2</sub>"
H2O = "H<sub>2</sub>O"
H2CO3 = "H<sub>2</sub>CO<sub>3</sub>"
HCO3 = "HCO<sub>3</sub><super>-</super>"
HPLUS = "H<super>+</super>"


def figure(asset_name, caption_text, max_width_cm=15.9):
    """Chapter-local binding of the shared figure() helper (SS0.6)."""
    return _shared_figure(asset_name, caption_text, ASSETS, max_width_cm=max_width_cm)


def body(text):
    return Paragraph(text, STYLES["Body"])


def b1(text):
    return Paragraph("&bull; " + text, STYLES["Bullet1"])


def b2(text):
    return Paragraph("- " + text, STYLES["Bullet2"])


story = []

# ======================================================================================
# ---- Title block (SS5 item 1) ---- F130
# ======================================================================================
story += title_block("Breathing and Exchange of Gases")

# ======================================================================================
# ---- 14.intro ---- F001-F004 (opener F001)
# ======================================================================================
story.append(heading("14.0", "Why We Breathe - The Chapter's Starting Point", 1))
story.append(body(
    f"<b>Oxygen ({O2})</b> is utilised by organisms to <b>indirectly</b> break down simple "
    f"molecules like <b>glucose, amino acids and fatty acids</b> to derive energy for various "
    f"activities. <b>Carbon dioxide ({CO2})</b>, which is <b>harmful</b>, is released during "
    f"these <b>catabolic reactions</b>. It therefore becomes essential that {O2} is "
    f"<b>continuously provided</b> to the cells and the {CO2} produced by the cells is "
    f"<b>released out</b>."))
story.append(keyterm(
    f"<b>Breathing:</b> the process of exchange of {O2} from the atmosphere with {CO2} produced "
    f"by the cells. It is commonly known as <b>respiration</b>."))

# ======================================================================================
# ---- 14.1 Respiratory Organs ---- F005-F012 (heading F131, opener F005)
# ======================================================================================
story.append(heading("14.1", "Respiratory Organs", 1, has_table=True))
story.append(body(
    "Mechanisms of breathing <b>vary among different groups of animals</b> depending mainly on "
    "their <b>habitats</b> and <b>levels of organisation</b>."))
story.append(data_table([
    ["Animal group", "Respiratory structure / mechanism", "Named term"],
    ["Lower invertebrates - sponges, coelenterates, flatworms",
     f"Exchange {O2} with {CO2} by <b>simple diffusion over their entire body surface</b>",
     "Diffusion"],
    ["Earthworms", "Use their <b>moist cuticle</b> to exchange gases", "Cutaneous"],
    ["Insects", "A network of tubes (<b>tracheal tubes</b>) transports atmospheric air within "
                "the body", "Tracheal"],
    ["Most aquatic arthropods and molluscs",
     "Special <b>vascularised structures called gills</b>", "<b>Branchial respiration</b>"],
    ["Terrestrial forms", "<b>Vascularised bags called lungs</b>", "<b>Pulmonary respiration</b>"],
], col_widths=[3.1, 5.6, 1.9]))
story.append(body(
    "Among <b>vertebrates</b>, <b>fishes</b> use gills whereas <b>amphibians, reptiles, birds and "
    "mammals</b> respire through <b>lungs</b>. Amphibians like <b>frogs</b> can <b>also</b> respire "
    "through their <b>moist skin</b> (<b>cutaneous respiration</b>)."))

# ======================================================================================
# ---- 14.1.1 Human Respiratory System ---- F013-F039 (heading F132, opener F013)
# ======================================================================================
story.append(heading("14.1.1", "Human Respiratory System", 2))
story.append(body(
    "We have a pair of <b>external nostrils</b> opening out <b>above the upper lips</b>. These "
    "lead to a <b>nasal chamber</b> through the <b>nasal passage</b>. The nasal chamber opens into "
    "the <b>pharynx</b>, a portion of which is the <b>common passage for food and air</b>. The "
    "pharynx opens through the <b>larynx</b> region into the <b>trachea</b>."))
story.append(keyterm(
    "<b>Larynx:</b> a <b>cartilaginous box</b> which helps in <b>sound production</b> and hence is "
    "called the <b>sound box</b>."))
story.append(body(
    "During <b>swallowing</b>, the <b>glottis</b> can be covered by a <b>thin elastic "
    "cartilaginous flap called epiglottis</b> to <b>prevent the entry of food into the "
    "larynx</b>."))

story.append(heading("14.1.1a", "The Airway, Branch by Branch", 3))
story.append(process_flow([
    "<b>Trachea</b> - a <b>straight tube</b> extending up to the <b>mid-thoracic cavity</b>.",
    "The trachea <b>divides at the level of the 5th thoracic vertebra</b> into a <b>right and "
    "left primary bronchi</b>. (Each such division gives a <b>Bronchus</b>.)",
    "Each <b>bronchus</b> undergoes <b>repeated divisions</b> to form the <b>secondary and "
    "tertiary bronchi and bronchioles</b>, ending up in <b>very thin terminal bronchioles</b>. "
    "(A single such branch is a <b>Bronchiole</b>.)",
    "Each <b>terminal bronchiole</b> gives rise to a number of <b>very thin, irregular-walled "
    f"and vascularised bag-like structures called alveoli</b>.",
]))
story.append(body(
    "The <b>trachea, primary, secondary and tertiary bronchi, and initial bronchioles</b> are "
    "supported by <b>incomplete cartilaginous rings</b>. The <b>branching network of bronchi, "
    "bronchioles and alveoli comprises the lungs</b> - we have <b>two lungs</b>. Each <b>Lung</b> "
    "is covered by a <b>double-layered pleura</b>, with <b>pleural fluid</b> between its two "
    "layers, and this <b>pleural fluid reduces friction on the lung-surface</b>. Of the two "
    "<b>pleural membranes</b>, the <b>outer</b> one is in <b>close contact with the thoracic "
    "lining</b> whereas the <b>inner</b> one is in contact with the <b>lung surface</b>."))

story.append(figure(
    "fig_14_1.png",
    "Fig. 14.1 - Diagrammatic view of the human respiratory system (a sectional view of the "
    "left lung is also shown). Labelled from top down: <b>Epiglottis</b>, <b>Larynx</b>, "
    "<b>Trachea</b>, and the <b>Bronchus</b> entering each lung, dividing into a <b>Bronchiole</b> "
    "that ends in <b>Alveoli</b>; the <b>Cut end of rib</b> and the two <b>Pleural membranes</b> "
    "with <b>Pleural fluid</b> between them enclose the <b>Lung</b>, with the <b>heart</b> lying "
    "between the lungs and the dome-shaped <b>Diaphragm</b> below.",
    max_width_cm=14.6))

story.append(heading("14.1.1b", "Conducting Part vs Exchange Part", 3, has_table=True))
story.append(data_table([
    ["Part", "Extent", "Function"],
    ["<b>Conducting part</b>",
     "From the <b>external nostrils up to the terminal bronchioles</b>",
     "Transports the atmospheric air to the alveoli, <b>clears it from foreign particles</b>, "
     "<b>humidifies it</b> and <b>brings the air to body temperature</b>"],
    ["<b>Respiratory or exchange part</b>",
     "The <b>alveoli and their ducts</b>",
     f"The <b>site of actual diffusion</b> of {O2} and {CO2} between <b>blood and atmospheric "
     f"air</b>"],
], col_widths=[2.6, 4.0, 6.0]))

story.append(heading("14.1.1c", "The Thoracic Chamber", 3))
story.append(body(
    "The lungs are situated in the <b>thoracic chamber</b>, which is anatomically an "
    "<b>air-tight chamber</b>. It is formed <b>dorsally by the vertebral column</b>, "
    "<b>ventrally by the sternum</b>, <b>laterally by the ribs</b> and on the <b>lower side by "
    "the dome-shaped diaphragm</b>. The anatomical setup is such that <b>any change in the volume "
    "of the thoracic cavity is reflected in the pulmonary (lung) cavity</b>. Such an arrangement "
    "is <b>essential for breathing</b>, as <b>we cannot directly alter the pulmonary volume</b>."))
story.append(note(
    "Respiration in humans involves the following <b>five steps</b>, in this order: (i) "
    f"<b>Breathing or pulmonary ventilation</b>, by which atmospheric air is <b>drawn in</b> and "
    f"<b>{CO2}-rich alveolar air is released out</b>; (ii) <b>diffusion of gases</b> ({O2} and "
    f"{CO2}) <b>across the alveolar membrane</b>; (iii) <b>transport of gases by the blood</b>; "
    f"(iv) <b>diffusion of {O2} and {CO2} between blood and tissues</b>; and (v) <b>utilisation of "
    f"{O2} by the cells for catabolic reactions and resultant release of {CO2}</b> "
    f"(<b>cellular respiration</b>)."))

# ======================================================================================
# ---- 14.2 Mechanism of Breathing ---- F040-F053 (heading F133, opener F040)
# ======================================================================================
story.append(heading("14.2", "Mechanism of Breathing", 1))
story.append(body(
    "Breathing involves <b>two stages</b>: <b>inspiration</b>, during which <b>atmospheric air is "
    "drawn in</b>, and <b>expiration</b>, by which the <b>alveolar air is released out</b>. The "
    "movement of air into and out of the lungs is carried out by creating a <b>pressure "
    "gradient</b> between the lungs and the atmosphere."))
story.append(b1(
    "<b>Inspiration</b> can occur if the pressure within the lungs (<b>intra-pulmonary "
    "pressure</b>) is <b>less than the atmospheric pressure</b>, i.e. there is a <b>negative "
    "pressure in the lungs with respect to atmospheric pressure</b>."))
story.append(b1(
    "<b>Expiration</b> takes place when the <b>intra-pulmonary pressure is higher than the "
    "atmospheric pressure</b>."))
story.append(body(
    "The <b>diaphragm</b> and a specialised set of muscles - <b>external and internal "
    "intercostals</b> between the ribs - help in the generation of such pressure gradients."))

story.append(heading("14.2a", "Inspiration, Step by Step", 3))
story.append(process_flow([
    "Inspiration is initiated by the <b>contraction of the diaphragm</b>, which <b>increases the "
    "volume of the thoracic chamber in the antero-posterior axis</b>. In the figure this is the "
    "<b>Diaphragm contracted</b> state.",
    "<b>Contraction of the external inter-costal muscles lifts up the ribs and the sternum</b> - "
    "<b>Ribs and sternum raised</b> - causing an <b>increase in the volume of the thoracic "
    "chamber in the dorso-ventral axis</b>, expanding the <b>Rib cage</b>.",
    "The overall <b>increase in thoracic volume</b> causes a <b>similar increase in pulmonary "
    "volume</b>, so the <b>Volume of thorax increased</b>.",
    f"An increase in pulmonary volume <b>decreases the intra-pulmonary pressure to less than the "
    f"atmospheric pressure</b>, which <b>forces air from outside to move into the lungs</b> - "
    f"<b>Air entering lungs</b>. This is <b>inspiration</b>.",
]))
story.append(figure(
    "fig_14_2a.png",
    "Fig. 14.2 (a) - Mechanism of breathing showing <b>inspiration</b>: the <b>Rib cage</b> with "
    "<b>Ribs and sternum raised</b>, the <b>Diaphragm contracted</b> and flattened, the "
    "<b>Volume of thorax increased</b>, and <b>Air entering lungs</b>.",
    max_width_cm=8.6))

story.append(heading("14.2b", "Expiration, Step by Step", 3))
story.append(process_flow([
    "<b>Relaxation of the diaphragm and the inter-costal muscles</b> returns the <b>diaphragm and "
    "sternum to their normal positions</b> - the <b>Diaphragm relaxed and arched upwards</b>, and "
    "the <b>Ribs and sternum returned to original position</b> - <b>reducing the thoracic volume "
    "and thereby the pulmonary volume</b>, so the <b>Volume of thorax decreased</b>.",
    "This reduction leads to an <b>increase in intra-pulmonary pressure to slightly above the "
    "atmospheric pressure</b>, causing the <b>expulsion of air from the lungs</b> - <b>Air "
    "expelled from lungs</b>. This is <b>expiration</b>.",
]))
story.append(figure(
    "fig_14_2b.png",
    "Fig. 14.2 (b) - Mechanism of breathing showing <b>expiration</b>: the <b>Ribs and sternum "
    "returned to original position</b>, the <b>Diaphragm relaxed and arched upwards</b>, the "
    "<b>Volume of thorax decreased</b>, and <b>Air expelled from lungs</b>.",
    max_width_cm=8.6))

story.append(body(
    "We can <b>increase the strength of inspiration and expiration</b> with the help of "
    "<b>additional muscles in the abdomen</b>. On an average, a <b>healthy human breathes 12-16 "
    "times per minute</b>."))
story.append(keyterm(
    "<b>Spirometer:</b> the instrument with which the <b>volume of air involved in breathing "
    "movements</b> can be estimated. It helps in the <b>clinical assessment of pulmonary "
    "functions</b>."))

# ======================================================================================
# ---- 14.2.1 Respiratory Volumes and Capacities ---- F054-F068 (heading F134, opener F054)
# ======================================================================================
story.append(heading("14.2.1", "Respiratory Volumes and Capacities", 2, has_table=True))
story.append(body(
    "A <b>healthy man can inspire or expire approximately 6000 to 8000 mL of air per minute</b>. "
    "The individual volumes below are what a spirometer measures."))
story.append(data_table([
    ["Volume", "Definition", "Average value"],
    ["<b>Tidal Volume (TV)</b>",
     "Volume of air <b>inspired or expired during a normal respiration</b>",
     "Approx. <b>500 mL</b>"],
    ["<b>Inspiratory Reserve Volume (IRV)</b>",
     "<b>Additional volume of air a person can inspire by a forcible inspiration</b>",
     "<b>2500 mL to 3000 mL</b>"],
    ["<b>Expiratory Reserve Volume (ERV)</b>",
     "<b>Additional volume of air a person can expire by a forcible expiration</b>",
     "<b>1000 mL to 1100 mL</b>"],
    ["<b>Residual Volume (RV)</b>",
     "Volume of air <b>remaining in the lungs even after a forcible expiration</b>",
     "<b>1100 mL to 1200 mL</b>"],
], col_widths=[3.4, 7.0, 2.2]))
story.append(body(
    "By <b>adding up a few respiratory volumes</b>, one can derive various <b>pulmonary "
    "capacities</b>, which <b>can be used in clinical diagnosis</b>."))
story.append(data_table([
    ["Capacity", "Definition", "Formula"],
    ["<b>Inspiratory Capacity (IC)</b>",
     "<b>Total volume of air a person can inspire after a normal expiration</b>",
     "<b>TV + IRV</b>"],
    ["<b>Expiratory Capacity (EC)</b>",
     "<b>Total volume of air a person can expire after a normal inspiration</b>",
     "<b>TV + ERV</b>"],
    ["<b>Functional Residual Capacity (FRC)</b>",
     "<b>Volume of air that will remain in the lungs after a normal expiration</b>",
     "<b>ERV + RV</b>"],
    ["<b>Vital Capacity (VC)</b>",
     "The <b>maximum volume of air a person can breathe in after a forced expiration</b>, or "
     "<b>breathe out after a forced inspiration</b>",
     "<b>ERV + TV + IRV</b>"],
    ["<b>Total Lung Capacity (TLC)</b>",
     "<b>Total volume of air accommodated in the lungs at the end of a forced inspiration</b>",
     "<b>RV + ERV + TV + IRV</b>, i.e. <b>vital capacity + residual volume</b>"],
], col_widths=[3.4, 6.6, 2.6]))
story.append(memory_aid(
    "The four <b>capacities built by addition</b> all start from a volume you already know: "
    "<b>I</b>nspiratory <b>C</b>apacity adds the inspiratory pair (TV + IRV), <b>E</b>xpiratory "
    "<b>C</b>apacity adds the expiratory pair (TV + ERV) - the letter before 'C' tells you which "
    "reserve joins the tidal volume. <b>FRC</b> is what is left behind (ERV + RV), and <b>TLC</b> "
    "is simply <b>VC + RV</b>."))

# ======================================================================================
# ---- 14.3 Exchange of Gases ---- F069-F088 (heading F135, opener F069)
# ======================================================================================
story.append(heading("14.3", "Exchange of Gases", 1, has_table=True))
story.append(body(
    f"<b>Alveoli are the primary sites of exchange of gases</b>. Exchange of gases <b>also</b> "
    f"occurs <b>between blood and tissues</b>. {O2} and {CO2} are exchanged at these sites by "
    f"<b>simple diffusion</b>, mainly based on <b>pressure/concentration gradient</b>. "
    f"<b>Solubility of the gases</b> and the <b>thickness of the membranes</b> involved in "
    f"diffusion are <b>important factors that can affect the rate of diffusion</b>."))
story.append(keyterm(
    f"<b>Partial pressure:</b> the pressure contributed by an <b>individual gas in a mixture of "
    f"gases</b>. It is represented as <b>{PO2}</b> for oxygen and <b>{PCO2}</b> for carbon "
    f"dioxide."))
story.append(Paragraph(
    "<b>Table 14.1 - Partial pressures (in mm Hg) of oxygen and carbon dioxide at different "
    "parts involved in diffusion</b>", STYLES["Body"]))
story.append(data_table([
    ["Respiratory gas", "Atmospheric air", "Alveoli", "Blood (deoxygenated)",
     "Blood (oxygenated)", "Tissues"],
    [f"<b>{PO2}</b>", "<b>159</b>", "<b>104</b>", "<b>40</b>", "<b>95</b>", "<b>40</b>"],
    [f"<b>{PCO2}</b>", "<b>0.3</b>", "<b>40</b>", "<b>45</b>", "<b>40</b>", "<b>45</b>"],
], col_widths=[2.4, 2.2, 1.6, 2.6, 2.4, 1.6]))
story.append(body(
    f"The data in Table 14.1 indicate a <b>concentration gradient for oxygen from alveoli to "
    f"blood</b> and <b>from blood to tissues</b>. Similarly, a <b>gradient for {CO2} is present "
    f"in the opposite direction</b>, i.e. <b>from tissues to blood</b> and <b>from blood to "
    f"alveoli</b>."))
story.append(body(
    f"As the <b>solubility of {CO2} is 20-25 times higher than that of {O2}</b>, the <b>amount of "
    f"{CO2} that can diffuse through the diffusion membrane per unit difference in partial "
    f"pressure is much higher</b> compared to that of {O2}."))

story.append(heading("14.3a", "The Diffusion Membrane", 3))
story.append(body(
    "The <b>diffusion membrane</b> is made up of <b>three major layers</b>: the <b>thin squamous "
    "epithelium of alveoli</b>, the <b>endothelium of alveolar capillaries</b> and the "
    "<b>basement substance</b> in between them. The <b>basement substance</b> is composed of a "
    "<b>thin basement membrane</b> supporting the squamous epithelium and the <b>basement "
    "membrane surrounding the single-layer endothelial cells of the capillaries</b>. However, "
    "its <b>total thickness is much less than a millimetre</b>."))
story.append(figure(
    "fig_14_4.png",
    f"Fig. 14.4 - A diagram of a section of an <b>alveolus</b> with a <b>pulmonary capillary</b>. "
    f"The <b>Air</b> in the <b>Alveolar cavity</b> is separated from the <b>Blood capillary</b> by "
    f"the three layers of the diffusion membrane: the <b>Squamous epithelium of alveolar wall</b>, "
    f"the <b>Basement substance</b> and the <b>Endothelium of blood capillary</b>; a <b>Red blood "
    f"cell</b> is shown inside the capillary.",
    max_width_cm=14.2))
story.append(note(
    f"<b>All the factors in our body are favourable for diffusion of {O2} from alveoli to "
    f"tissues and of {CO2} from tissues to alveoli</b>. This is why <b>diffusion of gases occurs "
    f"in the alveolar region only and not in the other parts of the respiratory system</b>: only "
    f"there does a <b>vascularised, thin, three-layered diffusion membrane</b> lie between air and "
    f"blood, while the rest of the tract - the <b>conducting part</b> - has thick, "
    f"cartilage-supported walls and merely carries, cleans, humidifies and warms the air."))

# ======================================================================================
# ---- 14.4 Transport of Gases ---- F089-F094 (heading F136, opener F089)
# ======================================================================================
story.append(heading("14.4", "Transport of Gases", 1, has_table=True))
story.append(body(
    f"<b>Blood is the medium of transport</b> for {O2} and {CO2}."))
story.append(data_table([
    ["Gas", "Carried by", "Share"],
    [f"<b>{O2}</b>", "<b>RBCs</b> in the blood", "About <b>97 per cent</b>"],
    [f"<b>{O2}</b>", "<b>Dissolved state through the plasma</b>", "Remaining <b>3 per cent</b>"],
    [f"<b>{CO2}</b>", "<b>RBCs</b>", "Nearly <b>20-25 per cent</b>"],
    [f"<b>{CO2}</b>", f"As <b>bicarbonate</b>", "About <b>70 per cent</b>"],
    [f"<b>{CO2}</b>", "<b>Dissolved state through plasma</b>", "About <b>7 per cent</b>"],
], col_widths=[1.6, 7.0, 3.4]))

# ======================================================================================
# ---- 14.4.1 Transport of Oxygen ---- F095-F105 (heading F137, opener F095)
# ======================================================================================
story.append(heading("14.4.1", "Transport of Oxygen", 2))
story.append(keyterm(
    "<b>Haemoglobin:</b> a <b>red-coloured, iron-containing pigment</b> present in the RBCs."))
story.append(body(
    f"{O2} can <b>bind with haemoglobin in a reversible manner</b> to form "
    f"<b>oxyhaemoglobin</b>. <b>Each haemoglobin molecule can carry a maximum of four molecules "
    f"of {O2}</b>. Binding of oxygen with haemoglobin is <b>primarily related to the partial "
    f"pressure of {O2}</b>. <b>Partial pressure of {CO2}, hydrogen ion concentration and "
    f"temperature</b> are the <b>other factors which can interfere with this binding</b>."))
story.append(keyterm(
    f"<b>Oxygen dissociation curve:</b> the <b>sigmoid curve</b> obtained when the "
    f"<b>percentage saturation of haemoglobin with {O2}</b> is plotted against <b>{PO2}</b>. It is "
    f"<b>highly useful in studying the effect of factors like {PCO2} and {HPLUS} concentration on "
    f"the binding of {O2} with haemoglobin</b>."))
story.append(figure(
    "fig_14_5.png",
    f"Fig. 14.5 - <b>Oxygen dissociation curve</b>. The vertical axis is the <b>Percentage "
    f"saturation of haemoglobin with oxygen</b> and the horizontal axis is the <b>Partial pressure "
    f"of oxygen (mm Hg)</b>; the plotted sigmoid line is the <b>Oxygen dissociation curve</b> "
    f"itself.",
    max_width_cm=9.4))
story.append(data_table([
    ["Site", "Conditions", "Result"],
    ["<b>In the alveoli</b>",
     f"<b>High {PO2}</b>, <b>low {PCO2}</b>, <b>lesser {HPLUS} concentration</b> and <b>lower "
     f"temperature</b>",
     "The factors are <b>all favourable for the formation of oxyhaemoglobin</b>"],
    ["<b>In the tissues</b>",
     f"<b>Low {PO2}</b>, <b>high {PCO2}</b>, <b>high {HPLUS} concentration</b> and <b>higher "
     f"temperature</b>",
     f"Conditions are <b>favourable for dissociation of oxygen from oxyhaemoglobin</b>"],
], col_widths=[2.2, 5.4, 5.4]))
story.append(body(
    f"This clearly indicates that <b>{O2} gets bound to haemoglobin at the lung surface</b> and "
    f"<b>gets dissociated at the tissues</b>. Under <b>normal physiological conditions</b>, "
    f"<b>every 100 mL of oxygenated blood can deliver around 5 mL of {O2} to the tissues</b>."))
story.append(note(
    f"<b>Effect of {PCO2} on oxygen transport (Exercise 8):</b> a <b>high {PCO2}</b>, which also "
    f"raises the {HPLUS} concentration, is one of the tissue-side conditions that <b>favours "
    f"dissociation of {O2} from oxyhaemoglobin</b>. A <b>low {PCO2}</b>, as in the alveoli, "
    f"favours <b>formation</b> of oxyhaemoglobin instead. So {PCO2} does not carry the oxygen, but "
    f"it decides <b>where</b> the oxygen is released."))

# ======================================================================================
# ---- 14.4.2 Transport of Carbon dioxide ---- F106-F115 (heading F138, opener F106)
# ======================================================================================
story.append(heading("14.4.2", "Transport of Carbon dioxide", 2))
story.append(body(
    f"{CO2} is carried by <b>haemoglobin as carbamino-haemoglobin</b> (about <b>20-25 per "
    f"cent</b>). This binding is <b>related to the partial pressure of {CO2}</b>. <b>{PO2} is a "
    f"major factor which could affect this binding</b>."))
story.append(b1(
    f"When <b>{PCO2} is high</b> and <b>{PO2} is low</b>, as in the <b>tissues</b>, <b>more "
    f"binding of carbon dioxide occurs</b>."))
story.append(b1(
    f"When <b>{PCO2} is low</b> and <b>{PO2} is high</b>, as in the <b>alveoli</b>, "
    f"<b>dissociation of {CO2} from carbamino-haemoglobin takes place</b> - i.e. the {CO2} bound "
    f"to haemoglobin from the tissues is <b>delivered at the alveoli</b>."))
story.append(keyterm(
    "<b>Carbonic anhydrase:</b> RBCs contain a <b>very high concentration</b> of this enzyme, and "
    "<b>minute quantities of the same is present in the plasma too</b>."))
story.append(body(
    f"This enzyme facilitates the following reaction <b>in both directions</b>:"))
story.append(Paragraph(
    f"<b>{CO2} + {H2O} &lt;--carbonic anhydrase--&gt; {H2CO3} &lt;--carbonic anhydrase--&gt; "
    f"{HCO3} + {HPLUS}</b>", STYLES["Caption"]))
story.append(process_flow([
    f"<b>At the tissue site</b>, where <b>{PCO2} is high due to catabolism</b>, {CO2} <b>diffuses "
    f"into blood (RBCs and plasma)</b> and forms <b>{HCO3} and {HPLUS}</b>.",
    f"<b>At the alveolar site</b>, where <b>{PCO2} is low</b>, the reaction <b>proceeds in the "
    f"opposite direction</b>, leading to the formation of <b>{CO2} and {H2O}</b>.",
    f"Thus {CO2} <b>trapped as bicarbonate at the tissue level and transported to the alveoli is "
    f"released out as {CO2}</b>.",
]))
story.append(body(
    f"<b>Every 100 mL of deoxygenated blood delivers approximately 4 mL of {CO2} to the "
    f"alveoli</b>."))
story.append(figure(
    "fig_14_3.png",
    f"Fig. 14.3 - Diagrammatic representation of exchange of gases at the <b>Alveolus</b> and the "
    f"<b>Body tissues</b> with blood, and transport of oxygen and carbon dioxide. <b>Inspired "
    f"air</b> enters and <b>Expired air</b> leaves the alveolus, whose <b>Alveolar air</b> "
    f"exchanges <b>{CO2}</b> and <b>{O2}</b> with the blood: the <b>Pulmonary artery</b> brings "
    f"deoxygenated blood to the alveolus and the <b>Pulmonary vein</b> carries oxygenated blood "
    f"away, while the <b>Systemic arteries</b> deliver it to the <b>Body tissues</b> and the "
    f"<b>Systemic veins</b> return it. In the figure the two gases are marked <b>CO2</b> and "
    f"<b>O2</b>.",
    max_width_cm=14.6))

# ======================================================================================
# ---- 14.5 Regulation of Respiration ---- F116-F123 (heading F139, opener F116)
# ======================================================================================
story.append(heading("14.5", "Regulation of Respiration", 1))
story.append(body(
    "Human beings have a <b>significant ability to maintain and moderate the respiratory "
    "rhythm</b> to <b>suit the demands of the body tissues</b>. This is done by the <b>neural "
    "system</b>."))
story.append(b1(
    "<b>Respiratory rhythm centre:</b> a <b>specialised centre present in the medulla region of "
    "the brain</b>, <b>primarily responsible</b> for this regulation."))
story.append(b1(
    "<b>Pneumotaxic centre:</b> another centre present in the <b>pons region</b> of the brain "
    "which <b>can moderate the functions of the respiratory rhythm centre</b>. <b>Neural signal "
    "from this centre can reduce the duration of inspiration</b> and thereby <b>alter the "
    "respiratory rate</b>."))
story.append(b1(
    f"<b>Chemosensitive area:</b> situated <b>adjacent to the rhythm centre</b>, <b>highly "
    f"sensitive to {CO2} and hydrogen ions</b>. <b>Increase in these substances can activate this "
    f"centre</b>, which in turn <b>can signal the rhythm centre to make necessary adjustments in "
    f"the respiratory process by which these substances can be eliminated</b>."))
story.append(b1(
    f"<b>Receptors associated with the aortic arch and carotid artery</b> <b>also</b> can "
    f"<b>recognise changes in {CO2} and {HPLUS} concentration</b> and <b>send necessary signals to "
    f"the rhythm centre for remedial actions</b>."))
story.append(note(
    f"<b>The role of oxygen in the regulation of respiratory rhythm is quite insignificant.</b> "
    f"The regulation is driven by <b>{CO2} and {HPLUS}</b>, not by {O2} - a favourite NEET "
    f"assertion-reason trap."))

# ======================================================================================
# ---- 14.6 Disorders of Respiratory System ---- F124-F129 (heading in Facts block, opener F124)
# ======================================================================================
story.append(heading("14.6", "Disorders of Respiratory System", 1, has_table=True))
story.append(data_table([
    ["Disorder", "What happens", "Cause / note"],
    ["<b>Asthma</b>",
     "A <b>difficulty in breathing causing wheezing</b>",
     "Due to <b>inflammation of bronchi and bronchioles</b>"],
    ["<b>Emphysema</b>",
     "A <b>chronic disorder</b> in which <b>alveolar walls are damaged</b>, due to which the "
     "<b>respiratory surface is decreased</b>",
     "<b>One of the major causes of this is cigarette smoking</b>"],
    ["<b>Occupational Respiratory Disorders</b>",
     "In <b>certain industries</b>, <b>especially those involving grinding or stone-breaking</b>, "
     "<b>so much dust is produced that the defence mechanism of the body cannot fully cope with "
     "the situation</b>",
     "<b>Long exposure</b> can give rise to <b>inflammation</b> leading to <b>fibrosis</b> "
     "(<b>proliferation of fibrous tissues</b>) and thus causing <b>serious lung damage</b>. "
     "<b>Workers in such industries should wear protective masks.</b>"],
], col_widths=[2.6, 5.2, 5.2]))

# ======================================================================================
# ---- Quick Recap (SS5 item 8) ----
# ======================================================================================
story.append(heading("Recap", "Quick Recap", 1))
story.append(b1(
    f"Cells <b>utilise oxygen for metabolism and produce energy</b> along with substances like "
    f"<b>carbon dioxide which is harmful</b>. Animals have <b>evolved different mechanisms</b> "
    f"for the <b>transport of oxygen to the cells</b> and for the <b>removal of carbon dioxide</b> "
    f"from there. We have a <b>well developed respiratory system</b> comprising <b>two lungs and "
    f"associated air passages</b>."))
story.append(b1(
    f"The <b>first step in respiration is breathing</b>, by which atmospheric air is <b>taken in "
    f"(inspiration)</b> and the alveolar air is <b>released out (expiration)</b>. <b>Exchange of "
    f"{O2} and {CO2} between deoxygenated blood and alveoli</b>, <b>transport of these gases "
    f"throughout the body by blood</b>, <b>exchange of {O2} and {CO2} between the oxygenated blood "
    f"and tissues</b> and <b>utilisation of {O2} by the cells (cellular respiration)</b> are the "
    f"<b>other steps</b> involved."))
story.append(b1(
    "<b>Inspiration and expiration</b> are carried out by <b>creating pressure gradients between "
    "the atmosphere and the alveoli</b> with the help of <b>specialised muscles - intercostals "
    "and diaphragm</b>. <b>Volumes of air</b> involved in these activities <b>can be estimated "
    "with the help of a spirometer</b> and are <b>of clinical significance</b>."))
story.append(b1(
    f"<b>Exchange of {O2} and {CO2} at the alveoli and tissues occurs by diffusion.</b> The "
    f"<b>rate of diffusion is dependent on the partial pressure gradients of {O2} ({PO2}) and "
    f"{CO2} ({PCO2})</b>, <b>their solubility</b> as well as the <b>thickness of the diffusion "
    f"surface</b>. These factors in our body <b>facilitate diffusion of {O2} from the alveoli to "
    f"the deoxygenated blood as well as from the oxygenated blood to the tissues</b>, and are "
    f"<b>favourable for the diffusion of {CO2} in the opposite direction</b>, i.e. <b>from tissues "
    f"to alveoli</b>."))
story.append(b1(
    f"<b>Oxygen is transported mainly as oxyhaemoglobin.</b> In the <b>alveoli</b>, where {PO2} is "
    f"<b>higher</b>, {O2} <b>gets bound to haemoglobin</b>, which is <b>easily dissociated at the "
    f"tissues</b> where {PO2} is <b>low</b> and {PCO2} and {HPLUS} concentration are <b>high</b>."))
story.append(b1(
    f"<b>Nearly 70 per cent of carbon dioxide is transported as bicarbonate ({HCO3})</b> with the "
    f"help of the enzyme <b>carbonic anhydrase</b>. <b>20-25 per cent of carbon dioxide is carried "
    f"by haemoglobin as carbamino-haemoglobin</b>: in the <b>tissues</b>, where {PCO2} is "
    f"<b>high</b>, it <b>gets bound to blood</b>, whereas in the <b>alveoli</b>, where {PCO2} is "
    f"<b>low</b> and {PO2} is <b>high</b>, it <b>gets removed from the blood</b>."))
story.append(b1(
    "<b>Respiratory rhythm is maintained by the respiratory centre in the medulla region of the "
    "brain.</b> A <b>pneumotaxic centre in the pons region</b> of the brain and a "
    "<b>chemosensitive area in the medulla can alter the respiratory mechanism</b>."))

# ======================================================================================
# ---- Terms used in the exercises (SS5 item 9, Rule 2) ----
# The exercise-gap scan found 3 genuine gaps: high-altitude respiration (Ex 9), the
# reason for the sigmoidal pattern (Ex 11), and hypoxia (Ex 12). Each is answered here
# strictly from chapter content, with the derived quantity for Ex 14.
# ======================================================================================
story.append(heading("Terms", "Terms Used in the Exercises", 1))
story.append(heading("Ex 9", "A man going up a hill (high altitude)", 3))
story.append(body(
    f"Going up a hill means <b>climbing into thinner air</b>, so the <b>partial pressure of "
    f"oxygen ({PO2}) in the atmospheric air falls below its sea-level value of 159 mm Hg</b>. "
    f"Because <b>binding of oxygen with haemoglobin is primarily related to the partial pressure "
    f"of {O2}</b>, a lower atmospheric {PO2} means a lower alveolar {PO2}, so <b>less "
    f"oxyhaemoglobin is formed</b> and <b>less {O2} is delivered per 100 mL of blood</b> than the "
    f"usual 5 mL. The body compensates through the very mechanism of SS14.5: the <b>respiratory "
    f"rhythm centre</b>, prompted by the <b>chemosensitive area</b> and the <b>receptors of the "
    f"aortic arch and carotid artery</b>, <b>increases the rate and depth of breathing</b> - the "
    f"climber breathes <b>faster and deeper</b> than the normal <b>12-16 times per minute</b>, "
    f"using the <b>additional muscles in the abdomen</b> to strengthen inspiration and "
    f"expiration."))
story.append(heading("Ex 11", "Why the oxygen dissociation curve is sigmoidal", 3))
story.append(body(
    f"<b>Each haemoglobin molecule can carry a maximum of four molecules of {O2}</b>, and binding "
    f"is <b>reversible</b>. The <b>four binding events are not independent</b>: the first {O2} "
    f"molecule binds with difficulty, but once bound it makes the <b>remaining sites bind more "
    f"readily</b>, and the last site fills only when {PO2} is high. So saturation rises "
    f"<b>slowly at low {PO2}</b>, <b>steeply at intermediate {PO2}</b>, and <b>flattens as the "
    f"four sites fill up</b> - which is exactly the <b>S-shaped (sigmoid) curve</b> of Fig. 14.5. "
    f"The <b>steep middle portion</b> is the physiologically useful part: it is why a "
    f"<b>small fall in {PO2} at the tissues</b> (40 mm Hg against the alveolar 104 mm Hg) "
    f"<b>unloads a large amount of {O2}</b>."))
story.append(heading("Ex 12", "Hypoxia", 3))
story.append(body(
    f"<b>Hypoxia</b> is a <b>deficiency of oxygen reaching the body tissues</b> - the tissues "
    f"receive <b>less {O2} than they need</b> for the catabolic reactions that release energy. "
    f"Reading it against this chapter, hypoxia is what results whenever any link in the five-step "
    f"chain weakens: <b>reduced ventilation</b> (as in <b>asthma</b>, where inflammation of "
    f"bronchi and bronchioles obstructs breathing), a <b>reduced respiratory surface</b> (as in "
    f"<b>emphysema</b>, where alveolar walls are damaged, or in the <b>fibrosis</b> of "
    f"occupational respiratory disorders), a <b>fall in atmospheric {PO2}</b> (high altitude), or "
    f"<b>too little haemoglobin</b> to carry the <b>97 per cent</b> of {O2} that travels in the "
    f"RBCs."))
story.append(heading("Ex 14", "Tidal volume in an hour", 3))
story.append(body(
    "<b>Tidal Volume (TV)</b> is the <b>volume of air inspired or expired during a normal "
    "respiration</b>, approximately <b>500 mL</b>. A <b>healthy human breathes 12-16 times per "
    "minute</b>, i.e. <b>720 to 960 breaths per hour</b>. Multiplying by the tidal volume gives "
    "<b>about 360,000 to 480,000 mL per hour</b>, i.e. roughly <b>360 to 480 litres of air per "
    "hour</b>. (This agrees with the chapter's own figure that a healthy man can inspire or "
    "expire approximately <b>6000 to 8000 mL of air per minute</b>.)"))
story.append(memory_aid(
    "For the MCQ in Exercise 5, read Table 14.1 across one row at a time. <b>Atmospheric air vs "
    "alveolar air</b>: oxygen falls <b>159 to 104</b> (so atmospheric "
    "<b>pO<sub>2</sub> is higher</b>) while carbon dioxide rises <b>0.3 to 40</b> (so atmospheric "
    "<b>pCO<sub>2</sub> is lesser</b>). Air arriving from outside is <b>oxygen-rich and "
    "carbon-dioxide-poor</b> - which is the whole point of ventilating the alveoli."))

story.append(Paragraph(
    "<i>Every fact, number, name, qualifier, table row, figure and figure label in NCERT Class 11 "
    "Chapter 14 is carried above. Nothing outside the source chapter has been added, except the "
    "clearly marked MEMORY AID boxes and the exercise-gap explanations, which are derived only "
    "from chapter content.</i>", STYLES["Caption"]))


def main():
    return build_pdf(
        OUT_PDF, story,
        title="Class 11 Chapter 14 - Breathing and Exchange of Gases (NEET notes)",
        subject="NEET Biology",
    )


if __name__ == "__main__":
    sys.exit(main())
