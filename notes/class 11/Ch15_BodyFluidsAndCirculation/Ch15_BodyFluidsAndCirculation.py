"""
NCERT Class 11 Biology, Chapter 15 - Body Fluids and Circulation
NEET replacement notes -> A4 print-ready PDF.

Built under SUPREME COMMAND PROMPT.md v6, Pass 2: written linearly from the
frozen 245-row inventory (Ch15_BodyFluidsAndCirculation_inventory.md), in
Content Order (SS5), importing the repo-level frozen style module
`neet_template.py` (SS0.6). No style, geometry, colour or font is re-declared
here.

Block markers `# ---- N.N ----` mark every NCERT section so a Pass 3 flag can be
found and fixed in one contiguous block. Inventory row IDs are named in the
comments so any fact can be traced back to its frozen row.

Subscripts / superscripts: the inventory stores O2, CO2, mm-3, min-1 and the
plasma ions with plain or Unicode forms for human readability, but
check_pdf.py check 5 bans Unicode sub/superscripts in the PDF text stream, so
every one is written here as a <sub> / <super> tag instead.

Figure callouts: Figures 15.2, 15.3 and 15.4 carry their labels as vector
artwork with no text layer, so each figure is followed by a NOTE listing its
callouts verbatim. That is what puts all 43 figure-label-matrix labels
(F242-F245) into the running text for check_pdf.py check 6, and it is also the
only way a print reader can name the parts of a diagram whose labels did not
survive extraction.

Source: Chapter/class 11/Chapter 15 - Body Fluids and Circulation.pdf
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
from reportlab.platypus import Paragraph  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch15_BodyFluidsAndCirculation.pdf")

# Inline chemistry / unit shorthands (check 5: tags, never Unicode sub/superscripts)
O2 = "O<sub>2</sub>"
CO2 = "CO<sub>2</sub>"
NA = "Na<super>+</super>"
CA = "Ca<super>++</super>"
MG = "Mg<super>++</super>"
HCO3 = "HCO<sub>3</sub><super>-</super>"
CL = "Cl<super>-</super>"
PER_MM3 = "mm<super>-3</super>"
PER_MIN = "min<super>-1</super>"


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
# ---- Title block (SS5 item 1) ---- F001
# ======================================================================================
story += title_block("Body Fluids and Circulation")

# ======================================================================================
# ---- 15.intro ---- F002-F011 (opener F002)
# ======================================================================================
story.append(heading("15.0", "Why Body Fluids Exist - The Chapter's Starting Point", 1))
story.append(body(
    f"All living cells have to be provided with <b>nutrients, {O2} and other essential "
    f"substances</b>. Also, the <b>waste or harmful substances</b> produced have to be "
    f"<b>removed continuously</b> for healthy functioning of tissues. It is therefore "
    f"essential to have <b>efficient mechanisms</b> for the movement of these substances "
    f"<b>to the cells and from the cells</b>."))
story.append(body(
    "Different groups of animals have evolved <b>different methods</b> for this transport."))
story.append(b1(
    "<b>Simple organisms</b> like <b>sponges and coelenterates</b> circulate <b>water from "
    "their surroundings</b> through their <b>body cavities</b> to facilitate the cells to "
    "exchange these substances."))
story.append(b1(
    "<b>More complex organisms</b> use <b>special fluids within their bodies</b> to transport "
    "such materials."))
story.append(body(
    "<b>Blood</b> is the <b>most commonly used body fluid</b> by most of the higher organisms, "
    "including humans, for this purpose. Another body fluid, <b>lymph</b>, also helps in the "
    "transport of certain substances."))
story.append(note(
    "This chapter covers the <b>composition and properties of blood and lymph (tissue "
    "fluid)</b>, and the <b>mechanism of circulation of blood</b>."))
story.append(body("<b>Chapter contents</b> (p. 193 margin panel):"))
story.append(b1("<b>15.1</b> Blood"))
story.append(b1("<b>15.2</b> Lymph (Tissue Fluid)"))
story.append(b1("<b>15.3</b> Circulatory Pathways"))
story.append(b1("<b>15.4</b> Double Circulation"))
story.append(b1("<b>15.5</b> Regulation of Cardiac Activity"))
story.append(b1("<b>15.6</b> Disorders of Circulatory System"))

# ======================================================================================
# ---- 15.1 Blood ---- F012-F013 (heading F012, opener F013) + exercise-gap Ex 4
# ======================================================================================
story.append(heading("15.1", "Blood", 1))
story.append(keyterm(
    "<b>Blood</b> is a special <b>connective tissue</b> consisting of a <b>fluid matrix, "
    "plasma</b>, and <b>formed elements</b>."))
story.append(note(
    "<b>Why blood counts as a connective tissue</b> (assumed by Exercise 4; the NCERT body "
    "only asserts it): a connective tissue is <b>mesodermal in origin</b> and consists of "
    "<b>cells scattered in an extracellular matrix</b>. Blood fits exactly - its <b>formed "
    "elements</b> are the cells, and <b>plasma</b> is the matrix, which in blood happens to "
    "be <b>fluid</b> rather than solid or jelly-like."))

# ======================================================================================
# ---- 15.1.1 Plasma ---- F014-F024 (heading F014, opener F015)
# ======================================================================================
story.append(heading("15.1.1", "Plasma", 2))
story.append(body(
    "<b>Plasma</b> is a <b>straw coloured, viscous fluid</b> constituting nearly <b>55 per "
    "cent</b> of the blood."))
story.append(b1(
    "<b>90-92 per cent</b> of plasma is <b>water</b>; <b>proteins</b> contribute <b>6-8 per "
    "cent</b> of it."))
story.append(b1(
    "<b>Fibrinogen, globulins and albumins</b> are the <b>major proteins</b>:"))
story.append(b2("<b>Fibrinogens</b> - needed for <b>clotting or coagulation</b> of blood."))
story.append(b2(
    "<b>Globulins</b> - primarly involved in <b>defense mechanisms</b> of the body."))
story.append(b2("<b>Albumins</b> - help in <b>osmotic balance</b>."))
story.append(b1(
    f"Plasma also contains <b>small amounts of minerals</b> like {NA}, {CA}, {MG}, {HCO3}, "
    f"{CL}, etc."))
story.append(b1(
    "<b>Glucose, amino acids, lipids</b>, etc., are also present in the plasma as they are "
    "<b>always in transit</b> in the body."))
story.append(b1(
    "<b>Factors for coagulation or clotting</b> of blood are also present in the plasma in an "
    "<b>inactive form</b>."))
story.append(keyterm("<b>Serum:</b> plasma <b>without the clotting factors</b>."))

# ======================================================================================
# ---- 15.1.2 Formed Elements ---- F025-F050 (heading F025, opener F026, caption F050)
# ======================================================================================
story.append(heading("15.1.2", "Formed Elements", 2, has_table=True))
story.append(body(
    "<b>Erythrocytes, leucocytes and platelets</b> are collectively called <b>formed "
    "elements</b> (Figure 15.1) and they constitute nearly <b>45 per cent</b> of the blood."))

story.append(heading("15.1.2a", "Erythrocytes (RBC)", 3))
story.append(keyterm(
    "<b>Erythrocytes</b> or <b>red blood cells (RBC)</b> are the <b>most abundant</b> of all "
    "the cells in blood."))
story.append(b1(
    f"A healthy adult man has, on an average, <b>5 millions to 5.5 millions of RBCs "
    f"{PER_MM3}</b> of blood."))
story.append(b1("RBCs are formed in the <b>red bone marrow</b> in the adults."))
story.append(b1(
    "RBCs are <b>devoid of nucleus</b> in <b>most of the mammals</b> and are <b>biconcave</b> "
    "in shape."))
story.append(b1(
    "They have a <b>red coloured, iron containing complex protein</b> called "
    "<b>haemoglobin</b>, hence the colour and name of these cells."))
story.append(b1(
    "A healthy individual has <b>12-16 gms of haemoglobin</b> in every <b>100 mL</b> of blood. "
    "These molecules play a significant role in <b>transport of respiratory gases</b>."))
story.append(b1(
    "RBCs have an average <b>life span of 120 days</b>, after which they are destroyed in the "
    "<b>spleen</b> (<b>graveyard of RBCs</b>)."))

story.append(heading("15.1.2b", "Leucocytes (WBC)", 3, has_table=True))
story.append(keyterm(
    "<b>Leucocytes</b> are also known as <b>white blood cells (WBC)</b> as they are "
    "<b>colourless</b> due to the <b>lack of haemoglobin</b>."))
story.append(b1(
    f"They are <b>nucleated</b> and are <b>relatively lesser in number</b>, which averages "
    f"<b>6000-8000 {PER_MM3}</b> of blood."))
story.append(b1("Leucocytes are <b>generally short lived</b>."))
story.append(b1(
    "Two main categories of WBCs - <b>granulocytes</b> and <b>agranulocytes</b>. "
    "<b>Neutrophils, eosinophils and basophils</b> are the different types of "
    "<b>granulocytes</b>, while <b>lymphocytes and monocytes</b> are the "
    "<b>agranulocytes</b>."))
story.append(data_table([
    ["WBC type", "Group", "Per cent of total WBCs", "Function"],
    ["Neutrophils", "Granulocyte", "60-65 per cent (most abundant)",
     "Phagocytic - destroy foreign organisms entering the body"],
    ["Eosinophils", "Granulocyte", "2-3 per cent",
     "Resist infections; also associated with allergic reactions"],
    ["Basophils", "Granulocyte", "0.5-1 per cent (least)",
     "Secrete histamine, serotonin, heparin, etc.; involved in inflammatory reactions"],
    ["Lymphocytes ('B' and 'T' forms)", "Agranulocyte", "20-25 per cent",
     "Both B and T lymphocytes are responsible for immune responses of the body"],
    ["Monocytes", "Agranulocyte", "6-8 per cent",
     "Phagocytic - destroy foreign organisms entering the body"],
], col_widths=[2.1, 1.3, 2.0, 4.6]))
story.append(memory_aid(
    "<b>Never Let Mature Erythrocytes Be</b> = Neutrophils 60-65, Lymphocytes 20-25, "
    "Monocytes 6-8, Eosinophils 2-3, Basophils 0.5-1 - the five WBCs in "
    "<b>descending order of abundance</b>."))

story.append(heading("15.1.2c", "Platelets (Thrombocytes)", 3))
story.append(keyterm(
    "<b>Platelets</b>, also called <b>thrombocytes</b>, are <b>cell fragments</b> produced "
    "from <b>megakaryocytes</b> (special cells in the bone marrow)."))
story.append(b1(
    f"Blood normally contains <b>1,500,00-3,500,00 platelets {PER_MM3}</b>."))
story.append(b1(
    "Platelets can release a <b>variety of substances</b>, most of which are involved in the "
    "<b>coagulation or clotting</b> of blood."))
story.append(b1(
    "A <b>reduction in their number</b> can lead to <b>clotting disorders</b>, which will lead "
    "to <b>excessive loss of blood</b> from the body."))

story.append(figure("fig_15_1.png",
                    "Figure 15.1 Diagrammatic representation of formed elements in blood"))
story.append(note(
    "<b>Figure 15.1 callouts, verbatim:</b> R B C; Platelets; Eosinophil; Basophil; "
    "Neutrophil; Monocyte; T lymphocyte; B lymphocyte."))

# ======================================================================================
# ---- 15.1.3 Blood Groups ---- F051-F054 (heading F051, opener F052)
# ======================================================================================
story.append(heading("15.1.3", "Blood Groups", 2))
story.append(body(
    "Blood of human beings <b>differ in certain aspects</b> though it appears to be similar. "
    "<b>Various types of grouping</b> of blood has been done. Two such groupings - the "
    "<b>ABO</b> and <b>Rh</b> - are <b>widely used all over the world</b>."))

# ======================================================================================
# ---- 15.1.3.1 ABO grouping ---- F055-F067 (heading F055, opener F056, table F061-F065)
# ======================================================================================
story.append(heading("15.1.3.1", "ABO grouping", 3, has_table=True))
story.append(body(
    "<b>ABO grouping</b> is based on the <b>presence or absence of two surface antigens</b> "
    "(chemicals that can induce immune response) on the RBCs, namely <b>A</b> and <b>B</b>."))
story.append(keyterm(
    "Similarly, the <b>plasma</b> of different individuals contain <b>two natural "
    "antibodies</b> (proteins produced in response to antigens)."))
story.append(body(
    "The distribution of <b>antigens and antibodies</b> in the four groups of blood - <b>A, B, "
    "AB and O</b> - and the <b>donor's compatibility</b> are given in Table 15.1."))
story.append(data_table([
    ["Blood Group", "Antigens on RBCs", "Antibodies in Plasma", "Donor's Group"],
    ["A", "A", "anti-B", "A, O"],
    ["B", "B", "anti-A", "B, O"],
    ["AB", "A, B", "nil", "AB, A, B, O"],
    ["O", "nil", "anti-A, B", "O"],
], col_widths=[1.6, 2.0, 2.2, 2.2]))
story.append(body("<i>TABLE 15.1 Blood Groups and Donor Compatibility</i>"))
story.append(note(
    "During <b>blood transfusion</b>, <b>any blood cannot be used</b>; the blood of a "
    "<b>donor</b> has to be <b>carefully matched</b> with the blood of a <b>recipient</b> "
    "before any blood transfusion, to avoid severe problems of <b>clumping (destruction of "
    "RBC)</b>."))
story.append(b1(
    "Group <b>'O'</b> blood can be donated to persons with <b>any other blood group</b>, hence "
    "'O' group individuals are called <b>universal donors</b>."))
story.append(b1(
    "Persons with <b>'AB'</b> group can accept blood from persons with <b>AB as well as the "
    "other groups</b> of blood. Therefore, such persons are called <b>universal "
    "recipients</b>."))

# ======================================================================================
# ---- 15.1.3.2 Rh grouping ---- F068-F081 (heading F068, opener F069, folded S-U F071)
# ======================================================================================
story.append(heading("15.1.3.2", "Rh grouping", 3))
story.append(body(
    "Another antigen, the <b>Rh antigen</b> similar to one present in <b>Rhesus monkeys</b> "
    "(hence <b>Rh</b>), is also observed on the surface of RBCs of <b>majority (nearly 80 per "
    "cent)</b> of humans. This grouping is therefore done on the presence or absence of "
    "another antigen called the <b>Rhesus factor (Rh)</b> on the surface of RBCs."))
story.append(keyterm(
    "Such individuals are called <b>Rh positive (Rh+ve)</b> and those in whom this antigen is "
    "<b>absent</b> are called <b>Rh negative (Rh-ve)</b>."))
story.append(b1(
    "An <b>Rh-ve person</b>, if <b>exposed to Rh+ve blood</b>, will form <b>specific "
    "antibodies</b> against the Rh antigens. Therefore, <b>Rh group should also be matched</b> "
    "before transfusions."))

story.append(heading("15.1.3.2a", "Erythroblastosis foetalis", 3))
story.append(body(
    "A <b>special case of Rh incompatibility (mismatching)</b> has been observed between the "
    "<b>Rh-ve blood of a pregnant mother</b> with <b>Rh+ve blood of the foetus</b>."))
story.append(process_flow([
    "Rh antigens of the foetus <b>do not get exposed</b> to the Rh-ve blood of the mother in "
    "the <b>first pregnancy</b>, as the two bloods are <b>well separated by the placenta</b>.",
    "However, <b>during the delivery of the first child</b>, there is a possibility of "
    "<b>exposure of the maternal blood</b> to <b>small amounts of the Rh+ve blood</b> from the "
    "foetus.",
    "In such cases, the mother <b>starts preparing antibodies</b> against Rh antigen in her "
    "blood.",
    "In case of her <b>subsequent pregnancies</b>, the <b>Rh antibodies from the mother "
    "(Rh-ve)</b> can <b>leak into the blood of the foetus (Rh+ve)</b> and <b>destroy the "
    "foetal RBCs</b>.",
    "This could be <b>fatal to the foetus</b>, or could cause <b>severe anaemia and "
    "jaundice</b> to the baby.",
]))
story.append(keyterm("This condition is called <b>erythroblastosis foetalis</b>."))
story.append(note(
    "This can be <b>avoided</b> by administering <b>anti-Rh antibodies</b> to the mother "
    "<b>immediately after the delivery of the first child</b>."))

# ======================================================================================
# ---- 15.1.4 Coagulation of Blood ---- F082-F094 (heading F082, opener F083)
# ======================================================================================
story.append(heading("15.1.4", "Coagulation of Blood", 2))
story.append(body(
    "When you <b>cut your finger or hurt yourself</b>, your wound <b>does not continue to "
    "bleed for a long time</b>; usually the blood <b>stops flowing after sometime</b>. Blood "
    "exhibits <b>coagulation or clotting</b> in response to an <b>injury or trauma</b>. This "
    "is a mechanism to <b>prevent excessive loss of blood</b> from the body."))
story.append(body(
    "You would have observed a <b>dark reddish brown scum</b> formed at the site of a cut or "
    "an injury over a period of time."))
story.append(keyterm(
    "It is a <b>clot</b> or <b>coagulam</b> formed mainly of a <b>network of threads called "
    "fibrins</b>, in which <b>dead and damaged formed elements</b> of blood are trapped."))
story.append(process_flow([
    "An <b>injury or a trauma stimulates the platelets</b> in the blood to release certain "
    "<b>factors</b> which <b>activate the mechanism of coagulation</b>. Certain factors "
    "released by the <b>tissues at the site of injury</b> also can initiate coagulation.",
    "A <b>series of linked enzymic reactions (cascade process)</b>, involving a number of "
    "factors present in the plasma in an <b>inactive state</b>, forms an <b>enzyme complex, "
    "thrombokinase</b>.",
    "<b>Thrombokinase</b> is required to form <b>thrombin</b> from another <b>inactive "
    "substance</b> present in the plasma called <b>prothrombin</b>.",
    "<b>Fibrins</b> are formed by the conversion of <b>inactive fibrinogens</b> in the plasma "
    "by the enzyme <b>thrombin</b>.",
]))
story.append(note(
    "<b>Calcium ions</b> play a <b>very important role</b> in clotting."))
story.append(memory_aid(
    "Read the cascade <b>backwards</b> to remember it: <b>fibrin</b> needs <b>thrombin</b>, "
    "thrombin needs <b>thrombokinase</b>, thrombokinase needs the <b>cascade + platelet "
    "factors</b>. Each step turns an <b>inactive plasma factor</b> into its active form."))

# ======================================================================================
# ---- 15.2 Lymph (Tissue Fluid) ---- F095-F105 (heading F095, opener F096, folded S-U F105)
# ======================================================================================
story.append(heading("15.2", "Lymph (Tissue Fluid)", 1, has_table=True))
story.append(body(
    "As the blood passes through the <b>capillaries in tissues</b>, <b>some water along with "
    "many small water soluble substances move out</b> into the <b>spaces between the cells</b> "
    "of tissues, <b>leaving the larger proteins and most of the formed elements</b> in the "
    "blood vessels."))
story.append(keyterm(
    "This fluid released out is called the <b>interstitial fluid</b> or <b>tissue fluid</b>. "
    "It has the <b>same mineral distribution</b> as that in plasma."))
story.append(b1(
    "<b>Exchange of nutrients, gases</b>, etc., between the <b>blood and the cells</b> always "
    "occur <b>through this fluid</b>."))
story.append(b1(
    "An <b>elaborate network of vessels</b> called the <b>lymphatic system</b> collects this "
    "fluid and <b>drains it back to the major veins</b>."))
story.append(keyterm(
    "The fluid present in the lymphatic system is called the <b>lymph</b>. Lymph is a "
    "<b>colourless fluid</b> containing <b>specialised lymphocytes</b>, which are responsible "
    "for the <b>immune responses</b> of the body."))
story.append(b1("Lymph is also an <b>important carrier for nutrients, hormones</b>, etc."))
story.append(b1(
    "<b>Fats are absorbed through lymph</b> in the <b>lacteals</b> present in the "
    "<b>intestinal villi</b>."))
story.append(note(
    "Lymph is <b>almost similar to blood except for the protein content and the formed "
    "elements</b>."))
story.append(data_table([
    ["Feature", "Blood", "Lymph"],
    ["Colour", "Red (haemoglobin in RBCs)", "Colourless"],
    ["Proteins", "High - fibrinogen, globulins, albumins all present",
     "Low - larger proteins are left behind in the blood vessels"],
    ["Formed elements", "RBCs, all types of WBCs and platelets present",
     "No RBCs and no platelets; contains specialised lymphocytes only"],
    ["Flows in", "Closed network of arteries, capillaries and veins",
     "Lymphatic system, draining back into the major veins"],
    ["Main function", "Transport of respiratory gases, nutrients, wastes, hormones",
     "Immune responses; carrier of nutrients and hormones; absorption of fats in the lacteals"],
], col_widths=[1.7, 3.3, 3.9]))
story.append(body("<i>Blood versus lymph - the contrast assumed by Exercises 5 and 7(a).</i>"))

# ======================================================================================
# ---- 15.3 Circulatory Pathways ---- F106-F120 (heading F106, opener F107, folded S-U F111)
# ======================================================================================
story.append(heading("15.3", "Circulatory Pathways", 1, has_table=True))
story.append(body("The <b>circulatory patterns</b> are of <b>two types - open or closed</b>."))
story.append(b1(
    "<b>Open circulatory system</b> is present in <b>arthropods and molluscs</b>, in which "
    "blood pumped by the heart passes through <b>large vessels into open spaces or body "
    "cavities called sinuses</b>."))
story.append(b1(
    "<b>Annelids and chordates</b> have a <b>closed circulatory system</b>, in which the blood "
    "pumped by the heart is <b>always circulated through a closed network of blood "
    "vessels</b>. This pattern is considered to be <b>more advantageous</b>, as the <b>flow of "
    "fluid can be more precisely regulated</b>."))
story.append(note(
    "<b>All vertebrates and a few invertebrates</b> have a <b>closed circulatory system</b>."))

story.append(heading("15.3a", "Evolution of the Vertebrate Heart", 3, has_table=True))
story.append(body("<b>All vertebrates possess a muscular chambered heart.</b>"))
story.append(data_table([
    ["Group", "Heart chambers", "Circulation"],
    ["Fishes", "<b>2-chambered</b> - an atrium and a ventricle",
     "<b>Single circulation.</b> The heart pumps out deoxygenated blood, which is oxygenated "
     "by the <b>gills</b> and supplied to the body parts, from where deoxygenated blood is "
     "returned to the heart."],
    ["Amphibians and reptiles (except crocodiles)",
     "<b>3-chambered</b> - two atria and a single ventricle",
     "<b>Incomplete double circulation.</b> The left atrium receives oxygenated blood from the "
     "gills / lungs / skin and the right atrium gets the deoxygenated blood from other body "
     "parts; however, they <b>get mixed up in the single ventricle</b>, which pumps out "
     "<b>mixed blood</b>."],
    ["Crocodiles, birds and mammals",
     "<b>4-chambered</b> - two atria and two ventricles",
     "<b>Double circulation.</b> Oxygenated and deoxygenated blood received by the left and "
     "right atria respectively passes on to the ventricles of the same sides. The ventricles "
     "pump it out <b>without any mixing up</b>, i.e., <b>two separate circulatory "
     "pathways</b> are present."],
], col_widths=[2.0, 2.6, 5.4]))
story.append(memory_aid(
    "<b>2 - 3 - 4</b>: fishes 2, amphibians and reptiles 3, birds and mammals 4. The two "
    "exceptions both sit with the 4s: <b>crocodiles</b> are reptiles with a 4-chambered heart."))

# ======================================================================================
# ---- 15.3.1 Human Circulatory System ---- F121-F144 (heading F121, opener F122, caption F144)
# ======================================================================================
story.append(heading("15.3.1", "Human Circulatory System", 2))
story.append(keyterm(
    "<b>Human circulatory system</b>, also called the <b>blood vascular system</b>, consists "
    "of a <b>muscular chambered heart</b>, a <b>network of closed branching blood vessels</b> "
    "and <b>blood</b>, the fluid which is circulated."))
story.append(b1(
    "<b>Heart</b>, the <b>mesodermally derived</b> organ, is situated in the <b>thoracic "
    "cavity</b>, <b>in between the two lungs</b>, <b>slightly tilted to the left</b>. It has "
    "the <b>size of a clenched fist</b>."))
story.append(b1(
    "It is protected by a <b>double walled membranous bag, pericardium</b>, enclosing the "
    "<b>pericardial fluid</b>."))

story.append(heading("15.3.1a", "Chambers, Septa and Valves", 3))
story.append(b1(
    "Our heart has <b>four chambers</b> - two relatively <b>small upper chambers called "
    "atria</b> and two <b>larger lower chambers called ventricles</b>."))
story.append(b1(
    "A <b>thin, muscular wall</b> called the <b>inter-atrial septum</b> separates the right "
    "and the left atria, whereas a <b>thick-walled inter-ventricular septum</b> separates the "
    "left and the right ventricles (Figure 15.2)."))
story.append(b1(
    "The atrium and the ventricle of the same side are also separated by a <b>thick fibrous "
    "tissue called the atrio-ventricular septum</b>. However, <b>each of these septa are "
    "provided with an opening</b> through which the two chambers of the same side are "
    "connected."))
story.append(b1(
    "The opening between the <b>right atrium and the right ventricle</b> is guarded by a valve "
    "formed of <b>three muscular flaps or cusps, the tricuspid valve</b>, whereas a "
    "<b>bicuspid or mitral valve</b> guards the opening between the <b>left atrium and the "
    "left ventricle</b>."))
story.append(b1(
    "The openings of the <b>right and the left ventricles</b> into the <b>pulmonary artery</b> "
    "and the <b>aorta</b> respectively are provided with the <b>semilunar valves</b>."))
story.append(note(
    "The valves in the heart allow the flow of blood <b>only in one direction</b>, i.e., "
    "<b>from the atria to the ventricles</b> and <b>from the ventricles to the pulmonary "
    "artery or aorta</b>. These valves <b>prevent any backward flow</b>."))
story.append(b1(
    "The <b>entire heart is made of cardiac muscles</b>. The <b>walls of ventricles are much "
    "thicker</b> than that of the atria."))

story.append(heading("15.3.1b", "The Nodal Tissue", 3))
story.append(body(
    "A <b>specialised cardiac musculature</b> called the <b>nodal tissue</b> is also "
    "distributed in the heart (Figure 15.2)."))
story.append(b1(
    "A patch of this tissue is present in the <b>right upper corner of the right atrium</b> "
    "called the <b>sino-atrial node (SAN)</b>."))
story.append(b1(
    "Another mass of this tissue is seen in the <b>lower left corner of the right atrium</b>, "
    "close to the atrio-ventricular septum, called the <b>atrio-ventricular node (AVN)</b>."))
story.append(b1(
    "A bundle of nodal fibres, the <b>atrio-ventricular bundle (AV bundle)</b>, continues from "
    "the AVN, which passes through the atrio-ventricular septa to emerge on the top of the "
    "inter-ventricular septum and <b>immediately divides into a right and left bundle</b>."))
story.append(b1(
    "These branches give rise to <b>minute fibres throughout the ventricular musculature</b> "
    "of the respective sides and are called <b>purkinje fibres</b>."))
story.append(keyterm(
    "The nodal musculature has the ability to <b>generate action potentials without any "
    "external stimuli</b>, i.e., it is <b>autoexcitable</b>."))
story.append(b1(
    f"However, the <b>number of action potentials</b> that could be generated in a minute "
    f"<b>vary at different parts</b> of the nodal system. The <b>SAN can generate the maximum "
    f"number of action potentials, i.e., 70-75 {PER_MIN}</b>, and is responsible for "
    f"<b>initiating and maintaining the rhythmic contractile activity</b> of the heart. "
    f"Therefore, it is called the <b>pacemaker</b>."))
story.append(b1(
    f"Our heart normally beats <b>70-75 times in a minute</b> (average <b>72 beats "
    f"{PER_MIN}</b>)."))

story.append(figure("fig_15_2.png", "Figure 15.2 Section of a human heart"))
story.append(note(
    "<b>Figure 15.2 callouts, verbatim:</b> Vena cava; Sino-atrial node; Right atrium; "
    "Atrio-ventricular node; Chordae tendinae; Right ventricle; Aorta; Pulmonary artery; "
    "Pulmonary veins; Left atrium; Bundle of His; Left ventricle; Interventricular septum; "
    "Apex."))

# ======================================================================================
# ---- 15.3.2 Cardiac Cycle ---- F145-F171 (heading F145, opener F146, folded S-U F166)
# ======================================================================================
story.append(heading("15.3.2", "Cardiac Cycle", 2))
story.append(body("<b>How does the heart function?</b> Let us take a look."))
story.append(process_flow([
    "To begin with, <b>all the four chambers</b> of heart are in a <b>relaxed state</b>, i.e., "
    "they are in <b>joint diastole</b>. As the <b>tricuspid and bicuspid valves are open</b>, "
    "blood from the <b>pulmonary veins and vena cava</b> flows into the <b>left and the right "
    "ventricle</b> respectively through the left and right atria. The <b>semilunar valves are "
    "closed</b> at this stage.",
    "The <b>SAN now generates an action potential</b> which stimulates <b>both the atria</b> "
    "to undergo a <b>simultaneous contraction - the atrial systole</b>. This <b>increases the "
    "flow of blood into the ventricles by about 30 per cent</b>.",
    "The action potential is conducted to the ventricular side by the <b>AVN and AV bundle</b>, "
    "from where the <b>bundle of His</b> transmits it through the <b>entire ventricular "
    "musculature</b>.",
    "This causes the ventricular muscles to contract (<b>ventricular systole</b>); the atria "
    "undergoes <b>relaxation (diastole)</b>, coinciding with the ventricular systole.",
    "Ventricular systole <b>increases the ventricular pressure</b>, causing the <b>closure of "
    "tricuspid and bicuspid valves</b> due to <b>attempted backflow</b> of blood into the "
    "atria.",
    "As the ventricular pressure <b>increases further</b>, the <b>semilunar valves</b> "
    "guarding the <b>pulmonary artery (right side)</b> and the <b>aorta (left side)</b> are "
    "<b>forced open</b>, allowing the blood in the ventricles to flow through these vessels "
    "into the circulatory pathways.",
    "The ventricles now <b>relax (ventricular diastole)</b> and the <b>ventricular pressure "
    "falls</b>, causing the <b>closure of semilunar valves</b>, which <b>prevents the "
    "backflow</b> of blood into the ventricles.",
    "As the ventricular pressure <b>declines further</b>, the <b>tricuspid and bicuspid valves "
    "are pushed open</b> by the pressure in the atria exerted by the blood which was being "
    "<b>emptied into them by the veins</b>.",
    "The blood now once again <b>moves freely to the ventricles</b>. The ventricles and atria "
    "are now again in a <b>relaxed (joint diastole)</b> state, as earlier. Soon the <b>SAN "
    "generates a new action potential</b> and the events described above are <b>repeated in "
    "that sequence</b> and the process continues.",
], cyclic=True))
story.append(keyterm(
    "This <b>sequential event in the heart which is cyclically repeated</b> is called the "
    "<b>cardiac cycle</b>, and it consists of <b>systole and diastole of both the atria and "
    "ventricles</b>."))

story.append(heading("15.3.2a", "Stroke Volume and Cardiac Output", 3))
story.append(b1(
    "As mentioned earlier, the heart beats <b>72 times per minute</b>, i.e., that many cardiac "
    "cycles are performed per minute. From this it could be deduced that the <b>duration of a "
    "cardiac cycle is 0.8 seconds</b>."))
story.append(keyterm(
    "During a cardiac cycle, each ventricle pumps out approximately <b>70 mL of blood</b>, "
    "which is called the <b>stroke volume</b> (also called the <b>stroke or beat volume</b>)."))
story.append(keyterm(
    "The <b>stroke volume multiplied by the heart rate</b> (no. of beats per min.) gives the "
    "<b>cardiac output</b>. The cardiac output can be defined as the <b>volume of blood pumped "
    "out by each ventricle per minute</b>, and averages <b>5000 mL or 5 litres</b> in a "
    "healthy individual."))
story.append(note(
    "The body has the ability to <b>alter the stroke volume as well as the heart rate</b>, and "
    "thereby the <b>cardiac output</b>. For example, the cardiac output of an <b>athlete</b> "
    "will be <b>much higher</b> than that of an <b>ordinary man</b>."))

story.append(heading("15.3.2b", "Heart Sounds", 3))
story.append(body(
    "During each cardiac cycle <b>two prominent sounds</b> are produced, which can be easily "
    "heard through a <b>stethoscope</b>."))
story.append(b1(
    "The <b>first heart sound (lub)</b> is associated with the <b>closure of the tricuspid and "
    "bicuspid valves</b>."))
story.append(b1(
    "The <b>second heart sound (dub)</b> is associated with the <b>closure of the semilunar "
    "valves</b>."))
story.append(note("These sounds are of <b>clinical diagnostic significance</b>."))

# ======================================================================================
# ---- 15.3.3 Electrocardiogram (ECG) ---- F172-F187 (heading F172, opener F173, caption F187)
# ======================================================================================
story.append(heading("15.3.3", "Electrocardiogram (ECG)", 2))
story.append(body(
    "You are probably familiar with this scene from a typical hospital television show: a "
    "<b>patient is hooked up to a monitoring machine</b> that shows <b>voltage traces</b> on a "
    "screen and makes the sound '... pip... pip... pip..... peeeeeeeeeeeeeeeeeeeeee' as the "
    "patient goes into <b>cardiac arrest</b>. This type of machine "
    "(<b>electro-cardiograph</b>) is used to obtain an <b>electrocardiogram (ECG)</b>."))
story.append(keyterm(
    "<b>ECG</b> is a <b>graphical representation of the electrical activity of the heart</b> "
    "during a <b>cardiac cycle</b>."))
story.append(b1(
    "To obtain a <b>standard ECG</b> (as shown in Figure 15.3), a patient is connected to the "
    "machine with <b>three electrical leads</b> (<b>one to each wrist and to the left "
    "ankle</b>) that <b>continuously monitor the heart activity</b>."))
story.append(b1(
    "For a <b>detailed evaluation</b> of the heart's function, <b>multiple leads</b> are "
    "attached to the <b>chest region</b>. Here, we will talk <b>only about a standard "
    "ECG</b>."))
story.append(b1(
    "Each <b>peak</b> in the ECG is identified with a <b>letter from P to T</b> that "
    "corresponds to a <b>specific electrical activity</b> of the heart."))
story.append(process_flow([
    "The <b>P-wave</b> represents the <b>electrical excitation (or depolarisation) of the "
    "atria</b>, which leads to the <b>contraction of both the atria</b>.",
    "The <b>QRS complex</b> represents the <b>depolarisation of the ventricles</b>, which "
    "<b>initiates the ventricular contraction</b>. The contraction starts <b>shortly after "
    "Q</b> and marks the <b>beginning of the systole</b>.",
    "The <b>T-wave</b> represents the <b>return of the ventricles from excited to normal "
    "state (repolarisation)</b>. The <b>end of the T-wave</b> marks the <b>end of systole</b>.",
]))
story.append(note(
    "By <b>counting the number of QRS complexes</b> that occur in a given time period, one can "
    "<b>determine the heart beat rate</b> of an individual."))
story.append(note(
    "Since the ECGs obtained from different individuals have <b>roughly the same shape</b> for "
    "a given lead configuration, <b>any deviation from this shape indicates a possible "
    "abnormality or disease</b>. Hence, it is of a <b>great clinical significance</b>."))
story.append(figure("fig_15_3.png",
                    "Figure 15.3 Diagrammatic presentation of a standard ECG"))
story.append(note(
    "<b>Figure 15.3 callouts, verbatim:</b> P; Q; R; S; T."))

# ======================================================================================
# ---- 15.4 Double Circulation ---- F188-F200 (heading F188, opener F189, folded S-U F199)
# ======================================================================================
story.append(heading("15.4", "Double Circulation", 1))
story.append(body(
    "The blood flows <b>strictly by a fixed route</b> through <b>Blood Vessels - the arteries "
    "and veins</b>."))
story.append(b1(
    "Basically, <b>each artery and vein consists of three layers</b>: an <b>inner lining of "
    "squamous endothelium, the tunica intima</b>; a <b>middle layer of smooth muscle and "
    "elastic fibres, the tunica media</b>; and an <b>external layer of fibrous connective "
    "tissue with collagen fibres, the tunica externa</b>."))
story.append(b1(
    "The <b>tunica media is comparatively thin in the veins</b> (Figure 15.4)."))
story.append(body(
    "As mentioned earlier, the blood pumped by the <b>right ventricle</b> enters the "
    "<b>pulmonary artery</b>, whereas the <b>left ventricle</b> pumps blood into the "
    "<b>aorta</b>."))
story.append(process_flow([
    "<b>Pulmonary circulation.</b> The <b>deoxygenated blood</b> pumped into the <b>pulmonary "
    "artery</b> is passed on to the <b>lungs</b>, from where the <b>oxygenated blood</b> is "
    "carried by the <b>pulmonary veins</b> into the <b>left atrium</b>.",
    "<b>Systemic circulation.</b> The <b>oxygenated blood</b> entering the <b>aorta</b> is "
    "carried by a network of <b>arteries, arterioles and capillaries</b> to the tissues, from "
    "where the <b>deoxygenated blood</b> is collected by a system of <b>venules, veins and "
    "vena cava</b> and emptied into the <b>right atrium</b> (Figure 15.4).",
]))
story.append(b1(
    f"The <b>systemic circulation</b> provides <b>nutrients, {O2} and other essential "
    f"substances</b> to the tissues and takes <b>{CO2} and other harmful substances</b> away "
    f"for <b>elimination</b>."))
story.append(note(
    "We have a <b>complete double circulation</b>, i.e., <b>two circulatory pathways</b>, "
    "namely, <b>pulmonary and systemic</b>, are present. <b>Its significance</b> (assumed by "
    "Exercise 6): because the two pathways are <b>fully separate</b>, oxygenated and "
    "deoxygenated blood <b>never mix</b>, so the tissues always receive <b>fully oxygenated "
    "blood</b> - which supports the high metabolic rate of birds and mammals."))

story.append(heading("15.4a", "Two Special Vascular Connections", 3))
story.append(b1(
    "A <b>unique vascular connection</b> exists between the <b>digestive tract and liver</b> "
    "called the <b>hepatic portal system</b>. The <b>hepatic portal vein</b> carries blood "
    "<b>from intestine to the liver</b> before it is delivered to the <b>systemic "
    "circulation</b>."))
story.append(b1(
    "A special <b>coronary system</b> of blood vessels is present in our body <b>exclusively "
    "for the circulation of blood to and from the cardiac musculature</b>."))

story.append(figure("fig_15_4.png",
                    "Figure 15.4 Schematic plan of blood circulation in human"))
story.append(note(
    "<b>Figure 15.4 callouts, verbatim:</b> Lungs; Pulmonary artery; Pulmonary Vein; Vena cava "
    "(great veins); RA; RV; LA; LV; Heart; Dorsal aorta; Body parts; Smooth muscle; Lumen; "
    "Vein; Capillary; Artery."))

# ======================================================================================
# ---- 15.5 Regulation of Cardiac Activity ---- F201-F206 (heading F201, opener F202)
# ======================================================================================
story.append(heading("15.5", "Regulation of Cardiac Activity", 1))
story.append(keyterm(
    "Normal activities of the heart are <b>regulated intrinsically</b>, i.e., <b>auto "
    "regulated by specialised muscles (nodal tissue)</b>, hence the heart is called "
    "<b>myogenic</b>."))
story.append(b1(
    "A <b>special neural centre in the medulla oblangata</b> can <b>moderate the cardiac "
    "function</b> through the <b>autonomic nervous system (ANS)</b>."))
story.append(b1(
    "Neural signals through the <b>sympathetic nerves</b> (part of ANS) can <b>increase</b> "
    "the <b>rate of heart beat</b>, the <b>strength of ventricular contraction</b> and thereby "
    "the <b>cardiac output</b>."))
story.append(b1(
    "On the other hand, <b>parasympathetic neural signals</b> (another component of ANS) "
    "<b>decrease</b> the <b>rate of heart beat</b>, the <b>speed of conduction of action "
    "potential</b> and thereby the <b>cardiac output</b>."))
story.append(b1(
    "<b>Adrenal medullary hormones</b> can also <b>increase the cardiac output</b>."))

# ======================================================================================
# ---- 15.6 Disorders of Circulatory System ---- F207-F224 (heading F207)
# ======================================================================================
story.append(heading("15.6", "Disorders of Circulatory System", 1))

# ---- 15.6a High Blood Pressure (Hypertension) ---- F208-F212 (heading F208, opener F209)
story.append(heading("15.6a", "High Blood Pressure (Hypertension)", 3))
story.append(keyterm(
    "<b>Hypertension</b> is the term for <b>blood pressure that is higher than normal "
    "(120/80)</b>."))
story.append(b1(
    "In this measurement <b>120 mm Hg</b> (millimetres of mercury pressure) is the "
    "<b>systolic, or pumping, pressure</b> and <b>80 mm Hg</b> is the <b>diastolic, or "
    "resting, pressure</b>."))
story.append(b1(
    "If repeated checks of blood pressure of an individual is <b>140/90 (140 over 90) or "
    "higher</b>, it shows <b>hypertension</b>."))
story.append(note(
    "High blood pressure <b>leads to heart diseases</b> and also <b>affects vital organs like "
    "brain and kidney</b>."))

# ---- 15.6b Coronary Artery Disease (CAD) ---- F213-F215 (heading F213, opener F214)
story.append(heading("15.6b", "Coronary Artery Disease (CAD)", 3))
story.append(keyterm(
    "<b>Coronary Artery Disease</b>, often referred to as <b>atherosclerosis</b>, affects the "
    "<b>vessels that supply blood to the heart muscle</b>."))
story.append(b1(
    "It is caused by <b>deposits of calcium, fat, cholesterol and fibrous tissues</b>, which "
    "makes the <b>lumen of arteries narrower</b>."))

# ---- 15.6c Angina ---- F216-F220 (heading F216, opener F217)
story.append(heading("15.6c", "Angina", 3))
story.append(keyterm(
    "It is also called <b>'angina pectoris'</b>. A symptom of <b>acute chest pain</b> appears "
    "when <b>no enough oxygen is reaching the heart muscle</b>."))
story.append(b1(
    "Angina can occur in <b>men and women of any age</b>, but it is <b>more common among the "
    "middle-aged and elderly</b>."))
story.append(b1("It occurs due to <b>conditions that affect the blood flow</b>."))

# ---- 15.6d Heart Failure ---- F221-F224 (heading F221, opener F222)
story.append(heading("15.6d", "Heart Failure", 3))
story.append(keyterm(
    "<b>Heart failure</b> means the <b>state of heart when it is not pumping blood effectively "
    "enough to meet the needs of the body</b>."))
story.append(b1(
    "It is sometimes called <b>congestive heart failure</b>, because <b>congestion of the "
    "lungs</b> is one of the <b>main symptoms</b> of this disease."))
story.append(note(
    "Heart failure is <b>not the same as</b>:<br/>"
    "<b>cardiac arrest</b> - when the <b>heart stops beating</b>; or<br/>"
    "<b>a heart attack</b> - when the <b>heart muscle is suddenly damaged by an inadequate "
    "blood supply</b>."))

# ======================================================================================
# ---- Summary (SS5 item 8) ---- F225-F226 (heading F225, opener F226)
# ======================================================================================
story.append(heading("Recap", "Summary", 1))
story.append(body(
    "<b>Vertebrates circulate blood, a fluid connective tissue, in their body</b>, to "
    "<b>transport essential substances to the cells</b> and to <b>carry waste substances from "
    "there</b>."))
story.append(b1(
    "Another fluid, <b>lymph (tissue fluid)</b>, is also used for the transport of certain "
    "substances."))
story.append(b1(
    "Blood comprises of a <b>fluid matrix, plasma</b> and <b>formed elements</b> - <b>RBCs "
    "(erythrocytes), WBCs (leucocytes) and platelets (thrombocytes)</b>."))
story.append(b1(
    "Human blood is grouped into the <b>ABO</b> system (based on the surface antigens <b>A</b> "
    "and <b>B</b> on RBCs) and the <b>Rh</b> system (based on the <b>Rhesus factor</b>)."))
story.append(b1(
    "Our circulatory system consists of a <b>muscular pumping organ, the heart</b> (two atria "
    "and two ventricles), a <b>network of vessels</b> and the fluid, <b>blood</b>."))
story.append(b1(
    f"<b>Cardiac musculature is auto-excitable.</b> The <b>SAN</b> generates the maximum "
    f"number of action potentials per minute (<b>70-75 {PER_MIN}</b>), hence it is called the "
    f"<b>pacemaker</b>."))
story.append(b1(
    "The action potential causes the <b>atria</b> and then the <b>ventricles</b> to undergo "
    "<b>contraction (systole)</b> followed by their <b>relaxation (diastole)</b>. The systole "
    "forces the blood to move <b>from the atria to the ventricles</b> and <b>to the pulmonary "
    "artery and the aorta</b>."))
story.append(b1(
    "The <b>cardiac cycle</b> is formed by these sequential events, cyclically repeated; a "
    "healthy person shows <b>72 such cycles per minute</b>. About <b>70 mL</b> is the "
    "<b>stroke (beat) volume</b>; the <b>cardiac output</b> averages <b>5 litres</b> per "
    "minute."))
story.append(b1(
    "The electrical activity of the heart can be recorded from the body surface using an "
    "<b>electrocardiograph</b>; the recording is the <b>electrocardiogram (ECG)</b>, which is "
    "of <b>clinical importance</b>."))
story.append(b1(
    "We have a <b>complete double circulation</b>: <b>pulmonary circulation</b> starts with "
    "the right ventricle pumping deoxygenated blood to the lungs, and <b>systemic "
    "circulation</b> starts with the left ventricle pumping oxygenated blood into the aorta."))
story.append(b1(
    "Though the heart is <b>autoexcitable</b>, its functions can be <b>moderated by neural and "
    "hormonal mechanisms</b>."))

# ======================================================================================
# ---- Exercises (SS5 item 9) ---- F227-F241 (heading F227, questions F228-F241)
# ======================================================================================
story.append(heading("Ex", "Exercises - and Where Each Is Answered", 1, has_table=True))
story.append(data_table([
    ["#", "Exercise question", "Answered in"],
    ["1", "Name the components of the formed elements in the blood and mention one major "
          "function of each of them.", "15.1.2 (RBC, WBC table, platelets) + Figure 15.1"],
    ["2", "What is the importance of plasma proteins?",
     "15.1.1 - fibrinogen (clotting), globulins (defense), albumins (osmotic balance)"],
    ["3", "Match Column I with Column II. Column I: (a) Eosinophils (b) RBC (c) AB Group "
          "(d) Platelets (e) Systole. Column II: (i) Coagulation (ii) Universal Recipient "
          "(iii) Resist Infections (iv) Contraction of Heart (v) Gas transport",
     "(a)-(iii) 15.1.2b; (b)-(v) 15.1.2a; (c)-(ii) 15.1.3.1; (d)-(i) 15.1.2c; "
     "(e)-(iv) 15.3.2"],
    ["4", "Why do we consider blood as a connective tissue?",
     "15.1 - fluid matrix (plasma) plus formed elements, mesodermal in origin"],
    ["5", "What is the difference between lymph and blood?",
     "15.2 - blood versus lymph table"],
    ["6", "What is meant by double circulation? What is its significance?",
     "15.4 - pulmonary and systemic pathways; significance stated in the NOTE"],
    ["7", "Write the differences between: (a) Blood and Lymph (b) Open and Closed system of "
          "circulation (c) Systole and Diastole (d) P-wave and T-wave",
     "(a) 15.2 table; (b) 15.3; (c) 15.3.2; (d) 15.3.3"],
    ["8", "Describe the evolutionary change in the pattern of heart among the vertebrates.",
     "15.3a - the 2 / 3 / 4-chambered heart table"],
    ["9", "Why do we call our heart myogenic?",
     "15.5 - auto regulated by the nodal tissue itself"],
    ["10", "Sino-atrial node is called the pacemaker of our heart. Why?",
     "15.3.1b - SAN generates the maximum action potentials and sets the rhythm"],
    ["11", "What is the significance of atrio-ventricular node and atrio-ventricular bundle "
           "in the functioning of heart?",
     "15.3.1b + 15.3.2 - they conduct the action potential to the ventricular musculature"],
    ["12", "Define a cardiac cycle and the cardiac output.", "15.3.2 and 15.3.2a"],
    ["13", "Explain heart sounds.", "15.3.2b - lub and dub"],
    ["14", "Draw a standard ECG and explain the different segments in it.",
     "15.3.3 + Figure 15.3 - P wave, QRS complex, T wave"],
], col_widths=[0.5, 5.6, 4.6]))

if __name__ == "__main__":
    sys.exit(build_pdf(
        OUT_PDF, story,
        title="Class 11 Chapter 15 - Body Fluids and Circulation (NEET notes)",
        subject="NEET Biology"))
