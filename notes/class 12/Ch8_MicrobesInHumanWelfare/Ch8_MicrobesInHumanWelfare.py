"""
NCERT Class 12 Biology, Chapter 8 - Microbes in Human Welfare
NEET replacement notes -> A4 print-ready PDF.

Built under SUPREME COMMAND PROMPT.md v6, Pass 2: written linearly from the
frozen 207-row inventory (Ch8_MicrobesInHumanWelfare_inventory.md), importing the
repo-level frozen style module `neet_template.py` (v6 SS0.6). No style, geometry,
colour or font is re-declared here.

Block markers `# ---- N.N ----` mark every NCERT section so a Pass 3 flag can be
found and fixed in one contiguous block. Inventory row IDs are named in the
comments so any fact can be traced back to its frozen row.

Pass 1 binding rules actioned (Ch8_TRACKER.md SS6):
  1. All 17 in-figure labels (F199-F207) are written into running text, verbatim
     from the matrix rows, because they are artwork and check 6 gates them.
  2. Banned glyphs: CO2, CH4, H2, B12, "100 C", "1500X" are plain ASCII - no
     subscripts, no degree sign, no Unicode arrows, no Greek.
  3. All 9 assets embedded via figure() - 9 assets / 8 NCERT figure numbers,
     because Figure 8.2 is split into (a)+(b) and (c).
  4. The 4 exercise-gap items are NOTE boxes explicitly marked as beyond the
     NCERT body text, so exercise support is never read as an NCERT sentence.
  5. Both SUMMARY-UNIQUE facts are body rows (F195 in 8.2.2, F196 in 8.3), not
     summary-only text.

Source: Chapter/class 12/Chapter 8 - Microbes in Human Welfare.pdf (12 pages)
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
from reportlab.platypus import KeepTogether, Paragraph, Spacer  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
OUT_PDF = os.path.join(HERE, "Ch8_MicrobesInHumanWelfare.pdf")


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
story += title_block("Microbes in Human Welfare")

# ======================================================================================
# ---- Chapter opener (F001-F019) ----
# ======================================================================================
# F001 - chapter title, carried as the opener banner + the printed contents strip
story.append(heading("Ch 8", "MICROBES IN HUMAN WELFARE - Chapter Opener", 1))
story.append(body(
    "<b>Chapter contents (as printed on the opener page):</b> 8.1 Microbes in Household "
    "Products; 8.2 Microbes in Industrial Products; 8.3 Microbes in Sewage Treatment; "
    "8.4 Microbes in Production of Biogas; 8.5 Microbes as Biocontrol Agents; "
    "8.6 Microbes as Biofertilisers."))
story.append(gap())
# F002 (opener), F003 (crossref), F004 (question)
story.append(body(
    "Besides <b>macroscopic plants and animals</b>, <b>microbes are the major components of "
    "biological systems on this earth</b>. You have studied about the diversity of living "
    "organisms in <b>Class XI</b>: recall which Kingdoms among the living organisms contain "
    "micro-organisms, and which of those groups are <b>only</b> microscopic."))
# F005, F006, F007, F008
story.append(body(
    "Microbes are present <b>everywhere</b> - in soil, water, air, inside our bodies and that of "
    "other animals and plants. They are present <b>even at sites where no other life-form could "
    "possibly exist</b>:"))
story.append(b1("deep inside the <b>geysers (thermal vents)</b>, where the temperature "
                "<b>may be as high as 100 C</b>;"))
story.append(b1("deep in the <b>soil</b>;"))
story.append(b1("under the layers of <b>snow several metres thick</b>;"))
story.append(b1("in <b>highly acidic environments</b>."))
story.append(gap())
# F009 - the diversity list, every group named, prions defined exactly
story.append(keyterm(
    "Microbes are <b>diverse</b> - <b>protozoa</b>, <b>bacteria</b>, <b>fungi</b> and microscopic "
    "<b>animal and plant viruses</b>, <b>viroids</b> and also <b>prions</b>, that are "
    "<b>proteinacious infectious agents</b>."))
# F010 - crossref to the figure spread
story.append(body(
    "Some of the microbes are shown in <b>Figures 8.1 and 8.2</b>, embedded below."))
# F011, F012 - colonies on nutritive media
story.append(body(
    "Microbes like <b>bacteria</b> and many <b>fungi</b> can be grown on <b>nutritive media</b> to "
    "form <b>colonies</b> (Figure 8.3), that can be seen with the <b>naked eyes</b>. Such "
    "<b>cultures</b> are useful in studies on micro-organisms."))
story.append(gap())

# F013 - caption; F199 labels "Flagella", "Rod-shaped bacterium"
story.append(figure(
    "fig_8_1.png",
    "<b>Fig. 8.1</b> - Bacteria: (a) Rod-shaped, magnified 1500X; (b) Spherical shaped, "
    "magnified 1500X; (c) A rod-shaped bacterium showing flagella, magnified 50,000X.",
    max_width_cm=7.0))
story.append(body(
    "<b>Labels on Figure 8.1:</b> panel (c) is a <b>Rod-shaped bacterium</b> whose <b>Flagella</b> "
    "are marked - the long whip-like appendages seen at 50,000X but invisible in the 1500X views "
    "of panels (a) and (b)."))
story.append(gap())

# F014 - caption (split across two assets); F200 + F201 labels
story.append(figure(
    "fig_8_2a.png",
    "<b>Fig. 8.2 (a), (b)</b> - Viruses: (a) A bacteriophage; (b) Adenovirus which causes "
    "respiratory infections.",
    max_width_cm=9.5))
story.append(figure(
    "fig_8_2c.png",
    "<b>Fig. 8.2 (c)</b> - Rod-shaped Tobacco Mosaic Virus (TMV). Magnified about "
    "1,00,000-1,50,000X.",
    max_width_cm=9.5))
story.append(body(
    "<b>Labels on Figure 8.2:</b> the <b>bacteriophage</b> of panel (a) is drawn part by part - "
    "<b>Head</b>, <b>Collar</b>, <b>Tail</b>, <b>Plate</b>, <b>Pins</b> and <b>Prongs</b> - so the "
    "phage reads as a head-plus-tail particle that anchors to a bacterium by its plate, pins and "
    "prongs. Panel (b) is the <b>Adenovirus</b> which causes respiratory infections. Panel (c) "
    "shows <b>Compact Rod-shaped viruses</b>, the Tobacco Mosaic Virus (TMV) particles, magnified "
    "about 1,00,000-1,50,000X."))
story.append(gap())

# F015 - caption; F202 label "Fungal colony"
story.append(figure(
    "fig_8_3.png",
    "<b>Fig. 8.3</b> - (a) Colonies of bacteria growing in a petri dish; (b) Fungal colony "
    "growing in a petri dish.",
    max_width_cm=13.0))
story.append(body(
    "<b>Labels on Figure 8.3:</b> panel (a) carries the bacterial colonies in a petri dish and "
    "panel (b) is marked <b>Fungal colony</b> - both are growths on nutritive media large enough "
    "to be seen with the naked eye."))
story.append(gap())

# F016 (opener, second intro block, p3), F017, F018, F019
story.append(body(
    "In <b>chapter 7</b>, you have read that <b>microbes cause a large number of diseases in human "
    "beings</b>. They also cause diseases in <b>animals and plants</b>. But this should "
    "<b>not</b> make you think that <b>all microbes are harmful</b>; <b>several microbes are "
    "useful to man in diverse ways</b>. Some of the <b>most important contributions of microbes to "
    "human welfare</b> are discussed in this chapter."))
story.append(gap())

# ======================================================================================
# ---- 8.1 MICROBES IN HOUSEHOLD PRODUCTS (F020-F038) ----
# ======================================================================================
# F020 - heading
story.append(heading("8.1", "MICROBES IN HOUSEHOLD PRODUCTS", 1, has_table=True))
# F021 (opener), F022
story.append(body(
    "We use <b>microbes or products derived from them everyday</b>. A common example is the "
    "<b>production of curd from milk</b>."))
# F023, F024, F025, F026, F027
story.append(keyterm(
    "Micro-organisms such as <b>Lactobacillus</b> and others, commonly called <b>lactic acid "
    "bacteria (LAB)</b>, grow in milk and convert it to <b>curd</b>."))
story.append(process_flow([
    "During growth, the <b>LAB produce acids</b> that <b>coagulate and partially digest the milk "
    "proteins</b>.",
    "A small amount of curd added to fresh milk as <b>inoculum</b> or <b>starter</b> contains "
    "<b>millions of LAB</b>.",
    "At <b>suitable temperatures</b> these multiply, thus converting milk to curd.",
    "Curd also has <b>improved nutritional quality</b>, because the LAB <b>increase vitamin "
    "B12</b>.",
]))
story.append(gap())
story.append(body(
    "In our <b>stomach</b> too, the LAB play a <b>very beneficial role in checking disease-causing "
    "microbes</b>."))
# F028, F029, F030
story.append(body(
    "The <b>dough</b> used for making foods such as <b>dosa</b> and <b>idli</b> is also "
    "<b>fermented by bacteria</b>. The <b>puffed-up appearance of dough</b> is due to the "
    "<b>production of CO2 gas</b>. Two questions worth answering from Class XI: which "
    "<b>metabolic pathway</b> is taking place resulting in the formation of CO2, and where do the "
    "<b>bacteria for these fermentations</b> come from?"))
# F031, F032, F033, F034
story.append(body(
    "Similarly, the dough used for making <b>bread</b> is fermented using <b>baker's yeast</b> "
    "(<i>Saccharomyces cerevisiae</i>). A number of <b>traditional drinks and foods</b> are also "
    "made by fermentation by microbes: <b>'Toddy'</b>, a traditional drink of some parts of "
    "<b>southern India</b>, is made by <b>fermenting sap from palms</b>, and microbes are also "
    "used to ferment <b>fish</b>, <b>soyabean</b> and <b>bamboo-shoots</b> to make foods."))
# F035, F036, F037, F038 - cheese as a table
story.append(body(
    "<b>Cheese</b> is <b>one of the oldest food items in which microbes were used</b>. Different "
    "varieties of cheese are known by their characteristic <b>texture, flavour and taste</b>, the "
    "<b>specificity coming from the microbes used</b>."))
story.append(data_table([
    ["Household product", "Microbe used", "What the microbe does"],
    ["<b>Curd</b> (from milk)", "<i>Lactobacillus</i> and other <b>lactic acid bacteria (LAB)</b>",
     "Produce acids that coagulate and partially digest milk proteins; increase <b>vitamin B12</b>"],
    ["<b>Dosa / idli dough</b>", "Bacteria", "Fermentation; the <b>CO2</b> produced puffs up the dough"],
    ["<b>Bread dough</b>", "<b>Baker's yeast</b>, <i>Saccharomyces cerevisiae</i>", "Fermentation of the dough"],
    ["<b>'Toddy'</b> (southern India)", "Microbes of the sap", "Ferment <b>sap from palms</b> into a traditional drink"],
    ["<b>Fermented fish, soyabean, bamboo-shoots</b>", "Microbes", "Fermentation into foods"],
    ["<b>'Swiss cheese'</b> - large holes", "Bacterium <i>Propionibacterium sharmanii</i>",
     "Produces a <b>large amount of CO2</b>, which makes the large holes"],
    ["<b>'Roquefort cheese'</b>", "A specific <b>fungi</b> grown on them",
     "<b>Ripens</b> the cheese and gives it a particular flavour"],
], col_widths=[2.8, 3.4, 4.6]))
story.append(gap())
# Exercise-gap item 4 (Q4, Bengal gram) - explicitly beyond the NCERT body text
story.append(note(
    "<b>Beyond the body text - for exercise Q4.</b> The chapter's own fermented-food examples "
    "cover <b>wheat</b> (bread dough, baker's yeast) and <b>rice</b> (idli and dosa dough), but "
    "name no <b>Bengal gram</b> dish. The mapping the exercise expects is: <b>wheat</b> gives "
    "<b>bread</b>, <b>rice</b> gives <b>idli and dosa</b>, and <b>Bengal gram</b> gives "
    "<b>dhokla</b>. Only the first two are NCERT body sentences."))
story.append(gap())

# ======================================================================================
# ---- 8.2 MICROBES IN INDUSTRIAL PRODUCTS (F039-F043) ----
# ======================================================================================
# F039 - heading
story.append(heading("8.2", "MICROBES IN INDUSTRIAL PRODUCTS", 1))
# F040 (opener), F041, F042
story.append(body(
    "Even in <b>industry</b>, microbes are used to <b>synthesise a number of products valuable to "
    "human beings</b>. <b>Beverages</b> and <b>antibiotics</b> are some examples."))
story.append(keyterm(
    "<b>Production on an industrial scale</b> requires growing microbes in <b>very large vessels "
    "called fermentors</b> (Figure 8.4)."))
# F043 - caption; F203 - no in-figure labels
story.append(figure(
    "fig_8_4.png",
    "<b>Fig. 8.4</b> - Fermentors. The very large vessels in which microbes are grown for "
    "industrial-scale production; the plate carries no labels of its own.",
    max_width_cm=8.5))
story.append(gap())

# ======================================================================================
# ---- 8.2.1 Fermented Beverages (F044-F051) ----
# ======================================================================================
# F044 - heading
story.append(heading("8.2.1", "Fermented Beverages", 2, has_table=True))
# F045 (opener), F046, F047
story.append(body(
    "Microbes, <b>especially yeasts</b>, have been used <b>from time immemorial</b> for the "
    "production of beverages like <b>wine, beer, whisky, brandy or rum</b>. For this purpose the "
    "<b>same yeast</b> <i>Saccharomyces cerevisiae</i> used for bread-making, and commonly called "
    "<b>brewer's yeast</b>, is used for <b>fermenting malted cereals and fruit juices</b>, to "
    "produce <b>ethanol</b>. Recollect the metabolic reactions which result in the production of "
    "ethanol by yeast."))
# F048, F049 - the distillation split as a table
story.append(body(
    "Depending on the <b>type of the raw material</b> used for fermentation and the <b>type of "
    "processing (with or without distillation)</b>, <b>different types of alcoholic drinks</b> are "
    "obtained."))
story.append(data_table([
    ["Processing", "Drinks obtained"],
    ["<b>Without distillation</b>", "<b>Wine</b> and <b>beer</b>"],
    ["<b>By distillation</b> of the fermented broth", "<b>Whisky</b>, <b>brandy</b> and <b>rum</b>"],
], col_widths=[4.0, 6.0]))
story.append(gap())
# F050 - crossref; F051 - caption; F204 - no in-figure labels
story.append(body("The <b>photograph of a fermentation plant</b> is shown in Figure 8.5."))
story.append(figure(
    "fig_8_5.png",
    "<b>Fig. 8.5</b> - Fermentation Plant. An industrial fermentation plant photographed whole; "
    "the plate carries no labels of its own.",
    max_width_cm=8.5))
story.append(gap())

# ======================================================================================
# ---- 8.2.2 Antibiotics (F052-F065, F195) ----
# ======================================================================================
# F052 - heading
story.append(heading("8.2.2", "Antibiotics", 2))
# F053 (opener)
story.append(body(
    "<b>Antibiotics produced by microbes</b> are regarded as <b>one of the most significant "
    "discoveries of the twentieth century</b> and have <b>greatly contributed towards the welfare "
    "of the human society</b>."))
# F054 - the etymology, exact
story.append(body(
    "<b>Anti</b> is a <b>Greek word</b> that means <b>'against'</b>, and <b>bio</b> means "
    "<b>'life'</b>; together they mean <b>'against life'</b> (in the context of disease causing "
    "organisms) - whereas <b>with reference to human beings, they are 'pro life' and not "
    "against</b>."))
# F055 - the definition
story.append(keyterm(
    "<b>Antibiotics</b> are <b>chemical substances</b>, which are <b>produced by some microbes</b> "
    "and <b>can kill or retard the growth of other (disease-causing) microbes</b>."))
# F056, F057, F058, F059, F060, F061 - the Penicillin story as a flow
story.append(body(
    "<b>Penicillin was the first antibiotic to be discovered</b>, and it was a <b>chance "
    "discovery</b>:"))
story.append(process_flow([
    "<b>Alexander Fleming</b>, while working on <b>Staphylococci</b> bacteria, once observed a "
    "<b>mould</b> growing in one of his <b>unwashed culture plates</b>, around which "
    "<b>Staphylococci could not grow</b>.",
    "He found out that it was due to a <b>chemical produced by the mould</b>, and he named it "
    "<b>Penicillin</b> after the mould <i>Penicillium notatum</i>.",
    "However, its <b>full potential as an effective antibiotic</b> was established <b>much "
    "later</b> by <b>Ernest Chain</b> and <b>Howard Florey</b>.",
    "This antibiotic was <b>extensively used to treat American soldiers wounded in World War "
    "II</b>.",
    "<b>Fleming, Chain and Florey</b> were awarded the <b>Nobel Prize in 1945</b>, for this "
    "discovery.",
]))
story.append(gap())
# F062, F063, F064, F065
story.append(body(
    "After Penicillin, <b>other antibiotics were also purified from other microbes</b> - it is "
    "worth naming some other antibiotics and finding out their sources. Antibiotics have "
    "<b>greatly improved our capacity to treat deadly diseases</b> such as <b>plague</b>, "
    "<b>whooping cough (kali khansi)</b>, <b>diphtheria (gal ghotu)</b> and <b>leprosy (kusht "
    "rog)</b>, which <b>used to kill millions all over the globe</b>. Today, <b>we cannot imagine "
    "a world without antibiotics</b>."))
# F195 - SUMMARY-UNIQUE fold-in (pneumonia)
story.append(body(
    "Stated in the chapter's own summary: <b>antibiotics have played a major role in controlling "
    "infectious diseases like diphtheria, whooping cough and pneumonia</b>."))
story.append(gap())
# Exercise-gap item 1 (Q6, two fungal species) - explicitly beyond the NCERT body text
story.append(note(
    "<b>Beyond the body text - for exercise Q6.</b> The question asks for <b>two fungal species</b> "
    "used to produce antibiotics, but the body names only <b>one fungus</b>, "
    "<i>Penicillium notatum</i> (Fleming's mould). The second conventionally accepted answer is "
    "<i>Penicillium chrysogenum</i>, the species used for commercial penicillin production. It is "
    "<b>not</b> an NCERT sentence from this chapter."))
story.append(gap())

# ======================================================================================
# ---- 8.2.3 Chemicals, Enzymes and other Bioactive Molecules (F066-F080) ----
# ======================================================================================
# F066 - heading
story.append(heading("8.2.3", "Chemicals, Enzymes and other Bioactive Molecules", 2, has_table=True))
# F067 (opener)
story.append(body(
    "Microbes are also used for <b>commercial and industrial production of certain chemicals</b> "
    "like <b>organic acids, alcohols and enzymes</b>."))
# F068, F069, F070, F071, F072 - the acid/alcohol producers table
story.append(data_table([
    ["Product", "Microbe", "Group"],
    ["<b>Citric acid</b>", "<i>Aspergillus niger</i>", "a <b>fungus</b>"],
    ["<b>Acetic acid</b>", "<i>Acetobacter aceti</i>", "a <b>bacterium</b>"],
    ["<b>Butyric acid</b>", "<i>Clostridium butylicum</i>", "a <b>bacterium</b>"],
    ["<b>Lactic acid</b>", "<i>Lactobacillus</i>", "a <b>bacterium</b>"],
    ["<b>Ethanol</b> (commercial production)", "<b>Yeast</b> (<i>Saccharomyces cerevisiae</i>)", "a <b>yeast</b>"],
], col_widths=[3.4, 4.2, 2.4]))
story.append(gap())
# F073, F074, F075, F076 - enzymes
story.append(body(
    "Microbes are also used for <b>production of enzymes</b>. <b>Lipases</b> are used in "
    "<b>detergent formulations</b> and are helpful in <b>removing oily stains from the "
    "laundry</b>. <b>Bottled fruit juices</b> bought from the market are <b>clearer</b> as "
    "compared to those made at home, because the bottled juices are <b>clarified by the use of "
    "pectinases and proteases</b>."))
# F077, F078, F079, F080 - the bioactive molecules table
story.append(data_table([
    ["Bioactive molecule", "Produced by", "Use / mechanism"],
    ["<b>Streptokinase</b> (modified by <b>genetic engineering</b>)",
     "the bacterium <i>Streptococcus</i>",
     "<b>'Clot buster'</b> - removes clots from the blood vessels of patients who have undergone "
     "<b>myocardial infarction</b> leading to <b>heart attack</b>"],
    ["<b>Cyclosporin A</b>", "the fungus <i>Trichoderma polysporum</i>",
     "<b>Immunosuppressive agent</b> in <b>organ-transplant</b> patients"],
    ["<b>Statins</b>", "the yeast <i>Monascus purpureus</i>",
     "Commercialised as <b>blood-cholesterol lowering agents</b>; act by <b>competitively "
     "inhibiting the enzyme responsible for synthesis of cholesterol</b>"],
], col_widths=[3.0, 2.8, 4.2]))
story.append(gap())
# Exercise-gap item 2 (Q13(a), single cell protein) - explicitly beyond the NCERT body text
story.append(note(
    "<b>Beyond the body text - for exercise Q13(a).</b> The term <b>single cell protein (SCP)</b> "
    "appears nowhere in this chapter's body. SCP is <b>microbial biomass</b> - the cells of "
    "microbes such as <b>Spirulina</b> grown in bulk - used as <b>protein-rich food or animal "
    "feed</b>. This definition is exercise support, not an NCERT sentence from this chapter."))
story.append(gap())

# ======================================================================================
# ---- 8.3 MICROBES IN SEWAGE TREATMENT (F081-F124, F196) ----
# ======================================================================================
# F081 - heading
story.append(heading("8.3", "MICROBES IN SEWAGE TREATMENT", 1))
# F082 (opener), F083, F084, F085, F086, F087
story.append(body(
    "<b>Large quantities of waste water are generated everyday in cities and towns</b>. A "
    "<b>major component</b> of this waste water is <b>human excreta</b>."))
story.append(keyterm("This <b>municipal waste-water</b> is also called <b>sewage</b>."))
story.append(body(
    "Sewage <b>contains large amounts of organic matter and microbes</b>. <b>Many of which are "
    "pathogenic</b>. This <b>cannot be discharged into natural water bodies</b> like rivers and "
    "streams <b>directly</b>. <b>Before disposal, hence, sewage is treated in sewage treatment "
    "plants (STPs) to make it less polluting</b>."))
# F088, F089
story.append(body(
    "<b>Treatment of waste water is done by the heterotrophic microbes naturally present in the "
    "sewage.</b> This treatment is carried out in <b>two stages</b>."))
story.append(gap())

# ---- 8.3 Primary treatment (F090-F095) ----
# F090 - unnumbered sub-heading
story.append(heading("8.3a", "Primary treatment", 3))
# F091 (opener), F092, F093, F094, F095
story.append(body(
    "These treatment steps basically involve the <b>physical removal of particles - large and "
    "small - from the sewage through filtration and sedimentation</b>. These are removed in "
    "<b>stages</b>:"))
story.append(process_flow([
    "<b>Initially</b>, <b>floating debris</b> is removed by <b>sequential filtration</b>.",
    "Then the <b>grit</b> (<b>soil and small pebbles</b>) is removed by <b>sedimentation</b>.",
    "<b>All solids that settle form the primary sludge</b>, and the <b>supernatant forms the "
    "effluent</b>.",
    "The <b>effluent from the primary settling tank</b> is taken for <b>secondary treatment</b>.",
]))
story.append(gap())

# ---- 8.3 Secondary treatment or Biological treatment (F096-F115) ----
# F096 - unnumbered sub-heading
story.append(heading("8.3b", "Secondary treatment or Biological treatment", 3))
# F097 (opener), F098, F099, F100
story.append(body(
    "The <b>primary effluent</b> is passed into <b>large aeration tanks</b> (Figure 8.6) where it "
    "is <b>constantly agitated mechanically</b> and <b>air is pumped into it</b>. This allows "
    "<b>vigorous growth of useful aerobic microbes into flocs</b> - <b>masses of bacteria "
    "associated with fungal filaments to form mesh like structures</b>. While growing, these "
    "microbes <b>consume the major part of the organic matter in the effluent</b>. This "
    "<b>significantly reduces the BOD (biochemical oxygen demand)</b> of the effluent."))
# F101, F102, F103, F104 - BOD, defined exactly
story.append(keyterm(
    "<b>BOD</b> refers to <b>the amount of the oxygen that would be consumed if all the organic "
    "matter in one liter of water were oxidised by bacteria</b>."))
story.append(b1("The sewage water is <b>treated till the BOD is reduced</b>."))
story.append(b1("The <b>BOD test measures the rate of uptake of oxygen by micro-organisms in a "
                "sample of water</b> and thus, <b>indirectly, BOD is a measure of the organic "
                "matter present in the water</b>."))
story.append(b1("<b>The greater the BOD of waste water, more is its polluting potential.</b>"))
story.append(gap())
# F105, F106, F107, F108, F109, F110, F111, F112 - the rest of the secondary train
story.append(process_flow([
    "Once the <b>BOD of sewage or waste water is reduced significantly</b>, the effluent is "
    "passed into a <b>settling tank</b> where the bacterial <b>'flocs'</b> are allowed to "
    "<b>sediment</b>.",
    "This <b>sediment is called activated sludge</b>.",
    "A <b>small part of the activated sludge is pumped back into the aeration tank</b> to serve "
    "as the <b>inoculum</b>.",
    "The <b>remaining major part of the sludge is pumped into large tanks called anaerobic sludge "
    "digesters</b>.",
    "Here, <b>other kinds of bacteria, which grow anaerobically, digest the bacteria and the "
    "fungi in the sludge</b>.",
    "During this digestion, bacteria <b>produce a mixture of gases such as methane, hydrogen "
    "sulphide and carbon dioxide</b>. These gases <b>form biogas</b> and <b>can be used as source "
    "of energy as it is inflammable</b>.",
    "The <b>effluent from the secondary treatment plant is generally released into natural water "
    "bodies</b> like rivers and streams.",
]))
story.append(gap())
# F196 - SUMMARY-UNIQUE fold-in (recycling of water in nature)
story.append(body(
    "Stated in the chapter's own summary: this treatment of sewage by the process of "
    "<b>activated sludge formation</b> also <b>helps in recycling of water in nature</b>."))
story.append(gap())
# F114 - caption; F205 - no in-figure labels
story.append(figure(
    "fig_8_6.png",
    "<b>Fig. 8.6</b> - Secondary treatment. The large aeration tank of the biological stage, "
    "photographed in operation; the plate carries no labels of its own.",
    max_width_cm=9.0))
# F113 - crossref; F115 - caption; F206 - no in-figure labels
story.append(body("An <b>aerial view</b> of such a plant is shown in Figure 8.7."))
story.append(figure(
    "fig_8_7.png",
    "<b>Fig. 8.7</b> - An aerial view of a sewage plant. The tanks of a whole sewage treatment "
    "plant seen from above; the plate carries no labels of its own.",
    max_width_cm=9.0))
story.append(gap())
# F116, F117, F118
story.append(body(
    "Microbes thus play a <b>major role in treating millions of gallons of waste water everyday "
    "across the globe</b>. This methodology has been practiced for <b>more than a century</b> now, "
    "in <b>almost all parts of the world</b>. <b>Till date, no man-made technology has been able "
    "to rival the microbial treatment of sewage.</b>"))
# F119, F120, F121, F122, F123, F124
story.append(body(
    "However, <b>due to increasing urbanisation, sewage is being produced in much larger "
    "quantities than ever before</b>, and <b>the number of sewage treatment plants has not "
    "increased enough to treat such large quantities</b>. So the <b>untreated sewage is often "
    "discharged directly into rivers</b>, leading to <b>their pollution and increase in "
    "water-borne diseases</b>. The <b>Ministry of Environment and Forests</b> has initiated the "
    "<b>Ganga Action Plan</b> and <b>Yamuna Action Plan</b> to save these <b>major rivers of our "
    "country</b> from pollution; under these plans, it is proposed to <b>build a large number of "
    "sewage treatment plants</b> so that <b>only treated sewage may be discharged in the "
    "rivers</b>. A <b>visit to a sewage treatment plant</b> situated in any place near you would "
    "be a very interesting and educating experience."))
story.append(gap())
story.append(note(
    "<b>Primary vs secondary treatment - the key difference (exercise Q8).</b> "
    "<b>Primary treatment is physical</b> - filtration and sedimentation remove floating debris "
    "and grit, giving <b>primary sludge</b> plus the <b>effluent</b>. <b>Secondary (biological) "
    "treatment is microbial</b> - aerobic microbes growing as <b>flocs</b> consume the organic "
    "matter and <b>reduce the BOD</b>, and the sediment they form is the <b>activated "
    "sludge</b>."))
story.append(gap())

# ======================================================================================
# ---- 8.4 MICROBES IN PRODUCTION OF BIOGAS (F125-F148) ----
# ======================================================================================
# F125 - heading
story.append(heading("8.4", "MICROBES IN PRODUCTION OF BIOGAS", 1))
# F126 (opener) - defines the term standing in the heading
story.append(keyterm(
    "<b>Biogas</b> is a <b>mixture of gases (containing predominantly methane) produced by the "
    "microbial activity and which may be used as fuel</b>."))
# F127, F128, F129, F130, F131, F132
story.append(body(
    "Microbes <b>produce different types of gaseous end-products during growth and metabolism</b>, "
    "and the <b>type of the gas produced depends upon the microbes and the organic substrates they "
    "utilise</b>. In the examples cited in relation to <b>fermentation of dough, cheese making and "
    "production of beverages</b>, the <b>main gas produced was CO2</b>. However, <b>certain "
    "bacteria, which grow anaerobically on cellulosic material, produce large amount of methane "
    "along with CO2 and H2</b>."))
story.append(keyterm(
    "These bacteria are collectively called <b>methanogens</b>, and one such common bacterium is "
    "<i>Methanobacterium</i>."))
story.append(body(
    "These bacteria are <b>commonly found in the anaerobic sludge during sewage treatment</b>."))
# F133, F134, F135, F136, F137, F138
story.append(body(
    "These bacteria are <b>also present in the rumen (a part of stomach) of cattle</b>. A <b>lot "
    "of cellulosic material</b> present in the <b>food of cattle</b> is also present in the "
    "rumen, and in the rumen these bacteria <b>help in the breakdown of cellulose and play an "
    "important role in the nutrition of cattle</b>. (Worth asking: are we, human beings, able to "
    "digest the cellulose present in our foods?) Thus, the <b>excreta (dung) of cattle, commonly "
    "called gobar, is rich in these bacteria</b>, and <b>dung can be used for generation of "
    "biogas, commonly called gobar gas</b>."))
# F139, F140, F141, F142 - the plant, as a flow
story.append(process_flow([
    "The <b>biogas plant</b> consists of a <b>concrete tank (10-15 feet deep)</b> in which "
    "<b>bio-wastes are collected</b> and a <b>slurry of dung is fed</b>.",
    "A <b>floating cover</b> is placed over the slurry, <b>which keeps on rising as the gas is "
    "produced in the tank due to the microbial activity</b>.",
    "The biogas plant has an <b>outlet</b>, which is <b>connected to a pipe to supply biogas to "
    "nearby houses</b>.",
    "The <b>spent slurry is removed through another outlet</b> and <b>may be used as "
    "fertiliser</b>.",
]))
story.append(gap())
# F143, F144, F145
story.append(body(
    "<b>Cattle dung is available in large quantities in rural areas</b> where cattle are used for "
    "a variety of purposes, <b>so biogas plants are more often built in rural areas</b>. The "
    "<b>biogas thus produced is used for cooking and lighting</b>. The picture of a biogas plant "
    "is shown in Figure 8.8."))
# F148 - caption; F207 labels
story.append(figure(
    "fig_8_8.png",
    "<b>Fig. 8.8</b> - A typical biogas plant.",
    max_width_cm=11.0))
story.append(body(
    "<b>Labels on Figure 8.8:</b> <b>Dung</b> and <b>Water</b> are mixed and fed as slurry into "
    "the <b>Digester</b>, the concrete tank 10-15 feet deep. The floating cover above it is the "
    "<b>Gas-holder</b>, which rises as gas collects. The <b>Gas</b> leaves by the outlet pipe and "
    "is a mixture of <b>CH4 + CO2</b>, and the spent <b>Sludge</b> is drawn off through the "
    "second outlet for use as fertiliser."))
story.append(gap())
# F146, F147
story.append(body(
    "The <b>technology of biogas production was developed in India</b> mainly due to the efforts "
    "of the <b>Indian Agricultural Research Institute (IARI)</b> and the <b>Khadi and Village "
    "Industries Commission (KVIC)</b>. If your school is situated in a village or near a village, "
    "it would be very interesting to <b>enquire if there are any biogas plants nearby</b>, visit "
    "the biogas plant and learn more about it from the people who are actually managing it."))
story.append(gap())

# ======================================================================================
# ---- 8.5 MICROBES AS BIOCONTROL AGENTS (F149-F175) ----
# ======================================================================================
# F149 - heading
story.append(heading("8.5", "MICROBES AS BIOCONTROL AGENTS", 1, has_table=True))
# F150 (opener) - defines the term standing in the heading
story.append(keyterm(
    "<b>Biocontrol</b> refers to the <b>use of biological methods for controlling plant diseases "
    "and pests</b>."))
# F151, F152, F153
story.append(body(
    "In modern society, these problems have been <b>tackled increasingly by the use of chemicals - "
    "by use of insecticides and pesticides</b>. These chemicals are <b>toxic and extremely "
    "harmful, to human beings and animals alike</b>, and have been <b>polluting our environment "
    "(soil, ground water), fruits, vegetables and crop plants</b>. Our <b>soil is also polluted "
    "through our use of weedicides to remove weeds</b>."))
story.append(gap())

# ---- 8.5 Biological control of pests and diseases (F154-F175) ----
# F154 - unnumbered sub-heading
story.append(heading("8.5a", "Biological control of pests and diseases", 3))
# F155 (opener), F156, F157, F158, F159
story.append(body(
    "In agriculture, there is a <b>method of controlling pests that relies on natural predation "
    "rather than introduced chemicals</b>."))
story.append(b1("A <b>key belief of the organic farmer</b> is that <b>biodiversity furthers "
                "health</b>. <b>The more variety a landscape has, the more sustainable it is.</b>"))
story.append(b1("The organic farmer therefore works to create a system where the insects that are "
                "<b>sometimes called pests are not eradicated, but instead are kept at manageable "
                "levels by a complex system of checks and balances</b> within a <b>living and "
                "vibrant ecosystem</b>."))
story.append(b1("Contrary to the <b>'conventional' farming practices</b>, which often use "
                "<b>chemical methods to kill both useful and harmful life forms "
                "indiscriminately</b>, this is a <b>holistic approach</b> that seeks to develop an "
                "understanding of the <b>webs of interaction between the myriad of organisms that "
                "constitute the field fauna and flora</b>."))
story.append(b1("The organic farmer holds the view that the <b>eradication of the creatures that "
                "are often described as pests is not only possible, but also undesirable</b> - for "
                "<b>without them the beneficial predatory and parasitic insects which depend upon "
                "them as food or hosts would not be able to survive</b>."))
# F160, F161
story.append(b1("Thus, the <b>use of biocontrol measures will greatly reduce our dependence on "
                "toxic chemicals and pesticides</b>."))
story.append(b1("An <b>important part of the biological farming approach</b> is to become familiar "
                "with the <b>various life forms that inhabit the field, predators as well as "
                "pests</b>, and also their <b>life cycles, patterns of feeding and the habitats "
                "that they prefer</b>. This will <b>help develop appropriate means of "
                "biocontrol</b>."))
story.append(gap())
# F162, F163, F164, F165, F166, F167, F168, F169, F170, F171, F172, F173, F174 - table + flow
story.append(data_table([
    ["Biocontrol agent", "What it is", "Target / effect"],
    ["<b>Ladybird</b> - the very familiar beetle with <b>red and black markings</b>", "A beetle",
     "Useful to get rid of <b>aphids</b>"],
    ["<b>Dragonflies</b>", "Insects", "Useful to get rid of <b>mosquitoes</b>"],
    ["<b><i>Bacillus thuringiensis</i></b> (often written as <b>Bt</b>)",
     "A <b>bacterium</b> - a microbial biocontrol agent that can be <b>introduced</b>",
     "Controls <b>butterfly caterpillars</b>"],
    ["<b><i>Trichoderma</i></b>",
     "<b>Free-living fungi</b> that are <b>very common in the root ecosystems</b>",
     "A biological control <b>being developed for use in the treatment of plant disease</b>; "
     "<b>effective biocontrol agents of several plant pathogens</b>"],
    ["<b>Baculoviruses</b>, majority in the genus <b><i>Nucleopolyhedrovirus</i></b>",
     "<b>Pathogens that attack insects and other arthropods</b>",
     "<b>Excellent candidates for species-specific, narrow spectrum insecticidal "
     "applications</b>"],
], col_widths=[3.2, 3.2, 3.6]))
story.append(gap())
story.append(body("How <b>Bt</b> works when it is applied:"))
story.append(process_flow([
    "<b>Bt</b> is available in <b>sachets as dried spores</b>, which are <b>mixed with water</b> "
    "and <b>sprayed onto vulnerable plants</b> such as <b>brassicas and fruit trees</b>.",
    "The spores are <b>eaten by the insect larvae</b>.",
    "<b>In the gut of the larvae, the toxin is released</b> and the <b>larvae get killed</b>.",
    "<b>The bacterial disease will kill the caterpillars, but leave other insects unharmed.</b>",
]))
story.append(gap())
story.append(body(
    "Because of the <b>development of methods of genetic engineering in the last decade</b> or so, "
    "scientists have <b>introduced B. thuringiensis toxin genes into plants</b>. Such plants are "
    "<b>resistant to attack by insect pests</b>. <b>Bt-cotton</b> is one such example, which is "
    "being <b>cultivated in some states of our country</b> - more about this in <b>chapter 10</b>."))
# F174, F175
story.append(body(
    "Baculoviruses <b>have been shown to have no negative impacts on plants, mammals, birds, fish "
    "or even on non-target insects</b>. This is <b>especially desirable</b> when <b>beneficial "
    "insects are being conserved</b> to aid in an overall <b>integrated pest management (IPM) "
    "programme</b>, or when an <b>ecologically sensitive area is being treated</b>."))
story.append(gap())
story.append(memory_aid(
    "For the three microbial biocontrol agents, remember <b>B-T-B</b>: <b>B</b>t the bacterium "
    "kills caterpillars, <b>T</b>richoderma the fungus fights plant pathogens, and "
    "<b>B</b>aculovirus the virus is the narrow-spectrum insecticide. Bacterium, fungus, virus - "
    "in that order."))
story.append(gap())

# ======================================================================================
# ---- 8.6 MICROBES AS BIOFERTILISERS (F176-F193) ----
# ======================================================================================
# F176 - heading
story.append(heading("8.6", "MICROBES AS BIOFERTILISERS", 1, has_table=True))
# F177 (opener) - about pollution, NOT about biofertilisers; F178, F179
story.append(body(
    "With our present day life styles, <b>environmental pollution is a major cause of concern</b>. "
    "The <b>use of the chemical fertilisers</b> to meet the <b>ever-increasing demand of "
    "agricultural produce</b> has <b>contributed significantly to this pollution</b>. We have now "
    "realised that there are <b>problems associated with the overuse of chemical fertilisers</b> "
    "and there is a <b>large pressure to switch to organic farming - the use of "
    "biofertilisers</b>."))
# F180, F181 - the definition arrives here, three sentences in
story.append(keyterm(
    "<b>Biofertilisers</b> are <b>organisms that enrich the nutrient quality of the soil</b>. The "
    "<b>main sources of biofertilisers are bacteria, fungi and cyanobacteria</b>."))
# F182, F183, F184
story.append(body(
    "You have studied about the <b>nodules on the roots of leguminous plants</b> formed by the "
    "<b>symbiotic association of Rhizobium</b>. These bacteria <b>fix atmospheric nitrogen into "
    "organic forms, which is used by the plant as nutrient</b>. <b>Other bacteria can fix "
    "atmospheric nitrogen while free-living in the soil</b> (examples <i>Azospirillum</i> and "
    "<i>Azotobacter</i>), thus <b>enriching the nitrogen content of the soil</b>."))
# F185, F186, F187, F188, F189
story.append(body(
    "<b>Fungi are also known to form symbiotic associations with plants (mycorrhiza)</b>, and "
    "<b>many members of the genus <i>Glomus</i> form mycorrhiza</b>. The <b>fungal symbiont</b> in "
    "these associations <b>absorbs phosphorus from soil and passes it to the plant</b>. Plants "
    "having such associations show <b>other benefits also</b>: <b>resistance to root-borne "
    "pathogens</b>, <b>tolerance to salinity and drought</b>, and an <b>overall increase in plant "
    "growth and development</b>. (Worth asking: what advantage does the fungus derive from this "
    "association?)"))
# F190, F191, F192
story.append(keyterm(
    "<b>Cyanobacteria</b> are <b>autotrophic microbes widely distributed in aquatic and "
    "terrestrial environments</b>, <b>many of which can fix atmospheric nitrogen</b>, e.g. "
    "<i>Anabaena</i>, <i>Nostoc</i>, <i>Oscillatoria</i>, etc."))
story.append(body(
    "<b>In paddy fields, cyanobacteria serve as an important biofertiliser.</b> <b>Blue green "
    "algae</b> also <b>add organic matter to the soil and increase its fertility</b>."))
story.append(data_table([
    ["Biofertiliser group", "Examples", "Nutrient benefit to the soil / plant"],
    ["<b>Symbiotic nitrogen-fixing bacteria</b>", "<i>Rhizobium</i> (root nodules of legumes)",
     "<b>Fix atmospheric nitrogen into organic forms</b> used by the plant as nutrient"],
    ["<b>Free-living nitrogen-fixing bacteria</b>", "<i>Azospirillum</i>, <i>Azotobacter</i>",
     "<b>Enrich the nitrogen content of the soil</b>"],
    ["<b>Mycorrhizal fungi</b>", "<b>Genus <i>Glomus</i></b>",
     "<b>Absorb phosphorus from soil and pass it to the plant</b>; also resistance to root-borne "
     "pathogens, tolerance to salinity and drought, overall increase in growth and development"],
    ["<b>Cyanobacteria</b> (blue green algae)", "<i>Anabaena</i>, <i>Nostoc</i>, <i>Oscillatoria</i>",
     "<b>Fix atmospheric nitrogen</b>; important biofertiliser <b>in paddy fields</b>; <b>add "
     "organic matter to the soil and increase its fertility</b>"],
], col_widths=[2.8, 3.0, 4.2]))
story.append(gap())
# F193
story.append(body(
    "<b>Currently, in our country, a number of biofertilisers are available commercially in the "
    "market</b> and <b>farmers use these regularly in their fields to replenish soil nutrients and "
    "to reduce dependence on chemical fertilisers</b>."))
story.append(gap())
# Exercise-gap item 3 (Q13(b), role of microbes in soil) - explicitly beyond the NCERT body text
story.append(note(
    "<b>Beyond the body text - for exercise Q13(b), the role of microbes in soil.</b> Assembled "
    "only from facts already in this chapter: soil microbes <b>fix atmospheric nitrogen</b> "
    "(<i>Rhizobium</i> in root nodules; free-living <i>Azospirillum</i> and <i>Azotobacter</i>), "
    "<b>mobilise phosphorus</b> to the plant through <b>mycorrhiza</b> (<i>Glomus</i>), <b>add "
    "organic matter and increase fertility</b> (cyanobacteria and blue green algae), and - as the "
    "sewage sections show - <b>decompose organic matter</b>, because the heterotrophic microbes "
    "that treat sewage digest exactly the organic matter and the microbial sludge fed to them. "
    "The general decomposer role is not stated as such in this chapter's body."))
story.append(gap())

# ======================================================================================
# ---- SUMMARY -> Quick Recap (F194) ----
# ======================================================================================
# F194 - "SUMMARY" heading, rewritten denser per SS3, not copied
story.append(heading("Recap", "QUICK RECAP", 1))
story.append(b1("<b>Microbes are a very important component of life on earth</b>, present "
                "everywhere including geysers at up to 100 C. <b>Not all microbes are "
                "pathogenic</b>; <b>many are very useful to human beings</b>, and we use microbes "
                "and microbially derived products <b>almost every day</b>."))
story.append(b1("<b>Curd:</b> <b>lactic acid bacteria (LAB)</b> such as <i>Lactobacillus</i> grow "
                "in milk and convert it into curd, and raise <b>vitamin B12</b>."))
story.append(b1("<b>Dough:</b> <b>bread</b> dough is fermented by the yeast "
                "<i>Saccharomyces cerevisiae</i>; <b>idli and dosa</b> are made from dough "
                "<b>fermented by microbes</b>, puffed up by <b>CO2</b>."))
story.append(b1("<b>Cheese:</b> bacteria and fungi impart <b>particular texture, taste and "
                "flavour</b> - <i>Propionibacterium sharmanii</i> makes the holes of Swiss cheese, "
                "a fungus ripens Roquefort."))
story.append(b1("<b>Industry:</b> microbes produce <b>lactic acid, acetic acid and alcohol</b> and "
                "other industrial products, in <b>fermentors</b>; <b>beverages</b> are wine and "
                "beer (no distillation) or whisky, brandy and rum (distillation)."))
story.append(b1("<b>Antibiotics</b> like <b>penicillins</b>, produced by useful microbes, are used "
                "to <b>kill disease-causing harmful microbes</b>, and have played a major role in "
                "controlling infectious diseases like <b>diphtheria, whooping cough and "
                "pneumonia</b>. Fleming, Chain and Florey: <b>Nobel Prize, 1945</b>."))
story.append(b1("<b>Bioactive molecules:</b> <b>streptokinase</b> (clot buster), <b>cyclosporin "
                "A</b> (immunosuppressive), <b>statins</b> (cholesterol lowering); enzymes "
                "<b>lipases</b>, <b>pectinases and proteases</b>."))
story.append(b1("<b>Sewage:</b> for <b>more than a hundred years</b>, microbes have been used to "
                "treat sewage (waste water) by the process of <b>activated sludge formation</b>, "
                "which <b>helps in recycling of water in nature</b>. <b>Primary</b> treatment is "
                "physical; <b>secondary</b> treatment is biological and <b>reduces the BOD</b>."))
story.append(b1("<b>Biogas:</b> <b>methanogens</b> such as <i>Methanobacterium</i> produce "
                "<b>methane (biogas)</b> while degrading plant waste, in anaerobic sludge and in "
                "the <b>rumen</b> of cattle; biogas produced by microbes is used as a <b>source of "
                "energy in rural areas</b>, for cooking and lighting."))
story.append(b1("<b>Biocontrol:</b> microbes can also be used to <b>kill harmful pests</b> - "
                "<b>Bt</b>, <b><i>Trichoderma</i></b>, <b>baculoviruses</b> - and these measures "
                "<b>help us to avoid heavy use of toxic pesticides</b> for controlling pests."))
story.append(b1("<b>Biofertilisers:</b> there is a <b>need these days to push for use of "
                "biofertilisers in place of chemical fertilisers</b> - <i>Rhizobium</i>, "
                "<i>Azospirillum</i>, <i>Azotobacter</i>, mycorrhizal <i>Glomus</i>, and "
                "cyanobacteria in paddy fields."))
story.append(b1("It is clear from the <b>diverse uses human beings have put microbes to</b> that "
                "they <b>play an important role in the welfare of human society</b>."))
story.append(gap())

# ======================================================================================
# ---- EXERCISES - terms and data the questions assume (F197, F198) ----
# ======================================================================================
# F197 - "EXERCISES" heading, carried as the appendix that closes the exercise gap (Rule 2)
story.append(heading("Appendix", "TERMS USED IN THE EXERCISES", 1, has_table=True))
story.append(body(
    "The chapter's <b>EXERCISES</b> lean on four items the body text never supplies; each is "
    "covered in a NOTE box at the point it belongs, and all four are collected here."))
story.append(b1("<b>Q4 - Bengal gram:</b> wheat gives <b>bread</b>, rice gives <b>idli and "
                "dosa</b>, Bengal gram gives <b>dhokla</b> (see 8.1)."))
story.append(b1("<b>Q6 - two fungal species for antibiotics:</b> <i>Penicillium notatum</i> from "
                "the body text, plus <i>Penicillium chrysogenum</i> (see 8.2.2)."))
story.append(b1("<b>Q13(a) - single cell protein (SCP):</b> microbial biomass, e.g. "
                "<b>Spirulina</b>, used as protein-rich food or feed (see 8.2.3)."))
story.append(b1("<b>Q13(b) - microbes in soil:</b> nitrogen fixation, phosphorus mobilisation via "
                "mycorrhiza, addition of organic matter, and decomposition of organic matter "
                "(see 8.6)."))
story.append(gap())
# F198 - the BOD data table given in exercise Q11, reproduced exactly.
# Lead-in + table + its NOTE are bound as one block: the NOTE reads the table's three
# rows back as the Q11 answer, so a page break between them strands the NOTE on a page
# of its own with the values it discusses overleaf (Pass 3(a) layout defect).
story.append(KeepTogether([
    body("<b>Exercise Q11 data (reproduce these values exactly).</b> Three samples of waste water "
         "were collected before water treatment, and their <b>BOD</b> recorded as follows:"),
    data_table([
        ["Sample", "BOD recorded", "Which water it is, by BOD"],
        ["<b>A</b>", "<b>20mg/L</b>", "River water - low BOD, so least polluting potential"],
        ["<b>B</b>", "<b>8mg/L</b>", "Secondary effluent - lowest BOD, already treated"],
        ["<b>C</b>", "<b>400mg/L</b>",
         "Untreated sewage water - highest BOD, most polluting potential"],
    ], col_widths=[1.6, 2.4, 6.0]),
    gap(),
    note("The three waters named in Q11 are <b>river water</b>, <b>untreated sewage water</b> and "
         "<b>secondary effluent</b>, and the values given are <b>20mg/L, 8mg/L and 400mg/L, "
         "respectively</b>, for samples A, B and C. Match them by the rule that <b>the greater "
         "the BOD of waste water, the more is its polluting potential</b>."),
]))


if __name__ == "__main__":
    sys.exit(build_pdf(
        OUT_PDF, story,
        title="Class 12 Chapter 8 - Microbes in Human Welfare (NEET notes)",
        subject="NEET Biology"))
