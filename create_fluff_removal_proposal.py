"""
Script to generate a comprehensive Unit-wise Bullshit & Fluff Removal / Rewording Proposal DOCX.
Covers all 10 Units of NCERT Biology (Class 11 & Class 12), identifying common conversational filler,
rhetorical questions, textbook pedagogical padding, and vague intros, replacing them with crisp,
high-yield NEET/NCERT-aligned conceptual notes.
"""

import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table, color="D3D3D3", sz="4"):
    tblPr = table._element.xpath('w:tblPr')
    if tblPr:
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:insideV w:val="none"/>'
            f'<w:left w:val="none"/>'
            f'<w:right w:val="none"/>'
            f'</w:tblBorders>'
        )
        tblPr[0].append(borders)

def build_proposal_document(output_path="NCERT_Biology_Fluff_Removal_Proposal.docx"):
    doc = Document()

    # Page Margins (0.75 in / ~1.9 cm)
    for section in doc.sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)

    # Style definitions
    # Title
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(4)
    p_title.paragraph_format.space_after = Pt(2)
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_t = p_title.add_run("NCERT BIOLOGY: UNIT-WISE FLUFF & CONVERSATIONAL FILLER REMOVAL PROPOSAL")
    run_t.font.name = "Calibri"
    run_t.font.size = Pt(17)
    run_t.font.bold = True
    run_t.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D) # Deep Navy

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_after = Pt(14)
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_s = p_sub.add_run("Framework for Streamlining NCERT Narrative Text into High-Yield, Crisp & Direct NEET Notes")
    run_s.font.name = "Calibri"
    run_s.font.size = Pt(11)
    run_s.font.italic = True
    run_s.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

    # Executive Summary Box
    table_box = doc.add_table(rows=1, cols=1)
    table_box.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_box.autofit = False
    table_box.columns[0].width = Inches(7.0)
    c = table_box.rows[0].cells[0]
    set_cell_background(c, "F0F4F8")
    set_cell_margins(c, top=140, bottom=140, left=200, right=200)

    p_box = c.paragraphs[0]
    p_box.paragraph_format.space_after = Pt(4)
    r_bh = p_box.add_run("Core Philosophy & Editorial Rules:\n")
    r_bh.bold = True
    r_bh.font.name = "Calibri"
    r_bh.font.size = Pt(10.5)
    r_bh.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

    rules_text = (
        "1. Eliminate Conversational Filler: Remove phrases like 'In earlier classes, you have studied...', 'As you know...', 'Can you think why?', 'Let us now discuss...'\n"
        "2. Replace Rhetorical Questions with Direct Scientific Facts: Transform questions like 'Have you ever wondered why leaves are green?' into direct causal statements ('Chlorophyll pigments in thylakoid membranes absorb blue/red wavelengths and reflect green light').\n"
        "3. High-Yield Retention: Retain 100% of keywords, numerical values, scientific names, anatomical sequences, exceptions, and mechanism steps required for NEET.\n"
        "4. Structural Clarity: Convert wordy sequential explanations into numbered mechanisms, comparison tables, and bulleted diagnostic criteria."
    )
    r_bt = p_box.add_run(rules_text)
    r_bt.font.name = "Calibri"
    r_bt.font.size = Pt(9.5)
    r_bt.font.color.rgb = RGBColor(0x22, 0x22, 0x22)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # Data structure for unit-wise proposals
    units_data = [
        {
            "class": "Class 11",
            "unit": "Unit 1: Diversity in the Living World",
            "chapters": "Ch 1: The Living World | Ch 2: Biological Classification | Ch 3: Plant Kingdom | Ch 4: Animal Kingdom",
            "analysis": "NCERT often opens with philosophical deliberations on 'What is living?' and colloquial musings about the beauty of nature, migratory birds, and historical classification attempts before presenting taxonomic rules.",
            "examples": [
                {
                    "topic": "Ch 1: What is Living? & Biodiversity Introduction",
                    "original": "How wonderful is the living world! The wide range of living types is amazing. The extraordinary habitats in which we find living organisms, be it cold mountains, deciduous forests, oceans, fresh water lakes, deserts or hot springs, leave us speechless. The beauty of a galloping horse, of the migrating birds, the valley of flowers or the attacking shark evokes awe and a deep sense of wonder. The ecological conflict and cooperation among members of a population... what indeed is life?",
                    "revised": "Living organisms inhabit extreme and diverse environments (polar regions, thermal vents, deserts, oceans). Life is characterized by distinctive properties: Growth, Reproduction, Metabolism, Cellular Organization, and Consciousness. Among these, Cellular Organization and Metabolism are defining features without exception."
                },
                {
                    "topic": "Ch 2: Need for Biological Classification & History",
                    "original": "Since the dawn of civilisation, there have been many attempts to classify living organisms. It was done instinctively not using criteria that were scientific but borne out of a need to use organisms for our own use – for food, shelter and clothing. Aristotle was the earliest to attempt a more scientific basis for classification. He used simple morphological characters to classify plants into trees, shrubs and herbs.",
                    "revised": "Early classifications were utilitarian (food, shelter, clothing). Aristotle introduced the first morphological system (Plants: Trees, Shrubs, Herbs; Animals: Red-blooded [Enaima] vs Non-red-blooded [Anaima]). Linnaeus proposed the Two-Kingdom system (Plantae, Animalia), later superseded by R.H. Whittaker's (1969) Five-Kingdom Classification."
                },
                {
                    "topic": "Ch 3: Algal Habitats and Thallus Forms",
                    "original": "Algae are chlorophyll-bearing, simple, thalloid, autotrophic and largely aquatic (both fresh water and marine) organisms. They occur in a variety of other habitats: moist stones, soils and wood. Some of them also occur in association with fungi (lichen) and animals (e.g., on sloth bear). Have you ever thought how diverse their sizes can be?",
                    "revised": "Algae: Thalloid, autotrophic, primarily aquatic organisms occurring in freshwater, marine, and symbiotic associations (Lichen with fungi; Epizoic on sloth bear). Form & size range from unicellular (Chlamydomonas) and colonial (Volvox) to filamentous (Ulothrix, Spirogyra) and massive kelps."
                },
                {
                    "topic": "Ch 4: Animal Kingdom Basis of Classification",
                    "original": "When you look around, you will observe different animals with different structures and forms. As over a million species of animals have been described till now, the need for classification becomes all the more vital. The classification also helps in assigning a systematic position to newly described species. In spite of differences in structure and form of different animals, there are fundamental features common to various individuals in relation to the arrangement of cells, body symmetry, nature of coelom...",
                    "revised": "Animal taxonomy classifies over 1 million species based on fundamental diagnostic criteria: Level of Organisation (Cellular, Tissue, Organ, Organ-system), Body Symmetry (Asymmetry, Radial, Bilateral), Germ Layers (Diploblastic/Triploblastic), Coelom Type (Acoelomate, Pseudocoelomate, Coelomate), Segmentation (Metamerism), and Notochord presence."
                }
            ]
        },
        {
            "class": "Class 11",
            "unit": "Unit 2: Structural Organisation in Animals and Plants",
            "chapters": "Ch 5: Morphology of Flowering Plants | Ch 6: Anatomy of Flowering Plants | Ch 7: Structural Organisation in Animals",
            "analysis": "Sections frequently rely on rhetorical observations ('If you pull out any weed, you will see...', 'You can see with your naked eye that...'), which add reading friction without technical utility.",
            "examples": [
                {
                    "topic": "Ch 5: Root System Introduction",
                    "original": "If you pull out any weed, you will see that all of them have roots, stems and leaves. They may be bearing flowers and fruits. The underground part of the flowering plant is the root system while the portion above the ground forms the shoot system. Look at Figure 5.1 and observe the main parts of a flowering plant.",
                    "revised": "Angiosperms consist of an underground Root System (derived from radicle) and an aerial Shoot System (derived from plumule). The root system is categorized into Tap Root (e.g., Mustard), Fibrous Root (e.g., Wheat), and Adventitious Root (e.g., Monstera, Banyan, Grasses)."
                },
                {
                    "topic": "Ch 6: Plant Anatomy & Tissue Systems",
                    "original": "You can very easily see the structural similarities and variations in the external morphology of the larger living organism, both plants and animals. Similarly, if we were to study the internal structure, one also finds several similarities as well as differences. This chapter introduces you to the internal structure and functional organisation of higher plants. Study of internal structure of plants is called anatomy.",
                    "revised": "Plant Anatomy: The study of internal tissue organization in plants. Plant tissues are divided into Meristematic Tissues (Apical, Intercalary, Lateral) and Permanent Tissues (Simple: Parenchyma, Collenchyma, Sclerenchyma; Complex: Xylem, Phloem)."
                },
                {
                    "topic": "Ch 7: Animal Tissues Overview",
                    "original": "In the preceding chapters you came across a large variety of organisms, both unicellular and multicellular, of the animal kingdom. In unicellular organisms, all functions like digestion, respiration and reproduction are performed by a single cell. In the complex body of a multicellular animal the same basic functions are carried out by different groups of cells in a well organised manner. What are tissues? Let us examine...",
                    "revised": "In multicellular animals, specialized groups of cells with intercellular substances perform specific physiological functions as Tissues. Four primary animal tissue types: Epithelial (covering/lining), Connective (support/binding), Muscular (contraction/movement), and Neural (impulse conduction)."
                }
            ]
        },
        {
            "class": "Class 11",
            "unit": "Unit 3: Cell: Structure and Functions",
            "chapters": "Ch 8: Cell: The Unit of Life | Ch 9: Biomolecules | Ch 10: Cell Cycle and Cell Division",
            "analysis": "Heavy use of historical narratives and conversational framing ('When you look around, you see both living and non-living things... You may wonder and ask yourself - What makes an organism living?') that should be condensed into cell theory principles and biomolecular reaction tables.",
            "examples": [
                {
                    "topic": "Ch 8: What is a Cell & Cell Theory",
                    "original": "When you look around, you see both living and non-living things. You must have wondered and probably asked yourself – 'what is it that makes an organism living, or what is it that an inanimate thing does not have which a living thing has' ? The answer to this is the presence of the basic unit of life – the cell in all living organisms. All organisms are composed of cells.",
                    "revised": "The Cell is the fundamental structural and functional unit of all living organisms (Unicellular organisms exhibit independent existence and essential life functions). Cell Theory (Schleiden 1838, Schwann 1839, modified by Virchow 1855): All living organisms are composed of cells and products of cells; all cells arise from pre-existing cells ('Omnis cellula-e cellula')."
                },
                {
                    "topic": "Ch 9: How to Analyse Chemical Composition",
                    "original": "There is a wide diversity in living organisms in our biosphere. Now a question that arises in our minds is: Are all living organisms made of the same chemicals, i.e., elements and compounds? You have learnt in chemistry how elemental analysis is performed. If we perform such an analysis on a plant tissue, animal tissue or a microbial paste, we obtain a list of elements like carbon, hydrogen, oxygen and several others and their respective content per unit mass of a living tissue.",
                    "revised": "Chemical Analysis of Living Tissue: Grinding living tissue (liver/leaf) in Trichloroacetic acid (Cl3CCOOH) yields two fractions: Acid-Soluble Pool (Biomicromolecules: MW 18–800 Da; amino acids, monosaccharides, nucleotides) and Acid-Insoluble Fraction (Biomacromolecules: MW > 10,000 Da; proteins, nucleic acids, polysaccharides, and membrane lipids)."
                },
                {
                    "topic": "Ch 10: Significance of Cell Cycle and Division",
                    "original": "Are you aware that all organisms, even the largest, start their life from a single cell? You may wonder how a single cell then goes on to form such large organisms. Growth and reproduction are characteristics of cells, indeed of all living organisms. All cells reproduce by dividing into two, with each parental cell giving rise to two daughter cells each time they divide.",
                    "revised": "Cell Cycle: Coordinated sequence of events by which a cell duplicates its genome, synthesizes cellular constituents, and divides into two daughter cells. Phases: Interphase (G1, S [DNA replication], G2) and M Phase (Mitosis/Meiosis + Cytokinesis)."
                }
            ]
        },
        {
            "class": "Class 11",
            "unit": "Unit 4: Plant Physiology",
            "chapters": "Ch 11: Photosynthesis in Higher Plants | Ch 12: Respiration in Plants | Ch 13: Plant Growth and Development",
            "analysis": "Plagued by pedagogical experiment walk-throughs ('Take two leaves, cover one with black paper... Do you remember the bell jar experiment?') and conversational questions about whether plants breathe.",
            "examples": [
                {
                    "topic": "Ch 11: Early Photosynthesis Experiments",
                    "original": "Let us try to find out what we already know about photosynthesis. Some simple experiments you may have done in the earlier classes have shown that chlorophyll (green pigment of the leaf), light and CO2 are required for photosynthesis to occur. You may have carried out the variegated leaf experiment or the experiment where part of a leaf was enclosed in a test tube containing some KOH soaked cotton...",
                    "revised": "Classical Photosynthesis Milestones: (1) Variegated leaf test: proves chlorophyll requirement; (2) Moll's Half-leaf experiment (KOH absorbs CO2): proves CO2 requirement; (3) Joseph Priestley (1770): Bell jar & mint sprig demonstrated plants restore oxygen; (4) Jan Ingenhousz (1779): Sunlight is essential; oxygen bubbles emitted by aquatic plants in light; (5) T.W. Engelmann (1843-1909): First action spectrum using Cladophora & aerobic bacteria."
                },
                {
                    "topic": "Ch 12: Do Plants Breathe?",
                    "original": "All of us breathe to live, but why is breathing so essential to life? What happens when we breathe? Also, do other organisms, say plants, breathe? Can you think how plants manage without specialized respiratory organs like lungs or gills? The answer is not simple, but let us look at the reasons why plants can get along without respiratory organs.",
                    "revised": "Plant Respiration: Plants lack specialized respiratory organs (lungs/gills) because: (1) Each plant organ takes care of its own gas exchange needs; (2) Plants have low metabolic gas demands compared to animals; (3) Diffusion distances are short due to stomata, lenticels, and extensive intercellular air spaces in parenchyma."
                },
                {
                    "topic": "Ch 13: Plant Growth Regulators Discovery",
                    "original": "It is interesting that the discovery of each of the five major groups of PGRs have been accidental. All this started with the observation of Charles Darwin and his son Francis Darwin when they observed that the coleoptiles of canary grass responded to unilateral illumination by growing towards the light source (phototropism). Can you imagine how this led to auxin discovery?",
                    "revised": "Discovery of Plant Growth Regulators (PGRs): (1) Auxin: Charles & Francis Darwin observed canary grass phototropism; F.W. Went isolated auxin from Avena sativa coleoptile tips. (2) Gibberellin: E. Kurosawa discovered 'bakanae' (foolish seedling) disease in rice caused by fungus Gibberella fujikuroi. (3) Cytokinin: Skoog & Miller identified Kinetin (crystallized from autoclaved herring sperm DNA). (4) Abscisic Acid (ABA): Inhibitor-B, Abscission II, and Dormin identified simultaneously. (5) Ethylene: H.H. Cousins confirmed volatile gas from ripened oranges accelerated banana ripening."
                }
            ]
        },
        {
            "class": "Class 11",
            "unit": "Unit 5: Human Physiology",
            "chapters": "Ch 14: Breathing & Gas Exchange | Ch 15: Body Fluids & Circulation | Ch 16: Excretory Products | Ch 17: Locomotion & Movement | Ch 18: Neural Control | Ch 19: Chemical Coordination",
            "analysis": "Contains conversational introductions ('As you have read earlier...', 'You have already learnt that blood is a special connective tissue...') and narrative transitions that can be streamlined directly into anatomical structures and hormonal feedback loops.",
            "examples": [
                {
                    "topic": "Ch 14: Mechanism of Breathing Introduction",
                    "original": "As you have read earlier, oxygen (O2) is utilised by the organisms to indirectly break down simple molecules like glucose, amino acids, fatty acids, etc., to derive energy to perform various activities. Carbon dioxide (CO2) which is harmful is also released during the above catabolic reactions. It is, therefore, evident that O2 has to be continuously provided to the cells and CO2 produced by the cells have to be released out. This process of exchange of O2 from the atmosphere with CO2 produced by the cells is called breathing, commonly known as respiration. Put your hand on your chest; you can feel the chest moving up and down. You know that it is due to breathing. How do we breathe?",
                    "revised": "Breathing (Ventilation): The atmospheric exchange of O2 for cellularly generated CO2. Mechanism involves pressure gradients created by the Diaphragm and External/Internal Intercostal Muscles: (1) Inspiration: Diaphragm contraction (flattens) + External intercostal contraction -> thoracic volume increases -> intrapulmonary pressure drops below atmospheric -> air moves into lungs. (2) Expiration: Diaphragm & intercostals relax -> thoracic volume decreases -> intrapulmonary pressure rises above atmospheric -> air expelled."
                },
                {
                    "topic": "Ch 17: Locomotion and Movement Distinction",
                    "original": "Movement is one of the significant features of living beings. Animals and plants exhibit a wide range of movements. Streaming of protoplasm in the unicellular organisms like Amoeba is a simple form of movement. Movement of cilia, flagella and tentacles are shown by many organisms. Human beings can move limbs, jaws, eyelids, tongue, etc. Some of the movements result in a change of place or location. Such voluntary movements are called locomotion. Walking, running, climbing, flying, swimming are all some forms of locomotory movements.",
                    "revised": "Movements: All locomotions are movements, but not all movements are locomotion. (1) Non-locomotory Movements: Protoplasmic streaming (Amoeba), ciliary/flagellar beats, eyelid/jaw motions. (2) Locomotory Movements: Voluntary movements resulting in displacement (walking, running, swimming, flying) requiring coordinated activity of muscular, skeletal, and neural systems."
                },
                {
                    "topic": "Ch 19: Endocrine Glands and Hormones",
                    "original": "You have already learnt that the neural system provides a point-to-point rapid coordination among organs. The neural coordination is fast but short-lived. As the nerve fibres do not innervate all cells of the body and the cellular functions need to be continuously regulated; a special kind of coordination and integration has to be provided. This function is carried out by hormones. The neural system and the endocrine system jointly coordinate and regulate the physiological functions in the body.",
                    "revised": "Neuro-Endocrine Coordination: Neural regulation provides rapid, point-to-point, short-lived electrical impulses but cannot innervate every cell. Endocrine system provides widespread, sustained chemical regulation via Hormones (non-nutrient, intercellular chemical messengers produced in trace amounts and secreted directly into the bloodstream by ductless glands)."
                }
            ]
        },
        {
            "class": "Class 12",
            "unit": "Unit 6: Reproduction",
            "chapters": "Ch 1: Sexual Reproduction in Flowering Plants | Ch 2: Human Reproduction | Ch 3: Reproductive Health",
            "analysis": "Full of poetic introductions about flowers being objects of aesthetic and romantic value, and societal narrative discussions in reproductive health that obscure statutory and clinical facts.",
            "examples": [
                {
                    "topic": "Ch 1: Flowers – Fascinating Organs of Angiosperms",
                    "original": "Are we not lucky that plants reproduce sexually? The myriads of flowers that we enjoy gazing at, the scents and the perfumes that we swoon over, the rich colours that attract us, are all there as an aid to sexual reproduction. Flowers do not exist only for us to be used for our own selfishness. All flowering plants show sexual reproduction. A look at the diversity of structures of the inflorescences, flowers and floral parts shows an amazing range of adaptations to ensure formation of the end products of sexual reproduction, the fruits and seeds.",
                    "revised": "Flower: The specialized reproductive shoot of Angiosperms where sexual reproduction occurs, producing seeds and fruits. Key structural components: Calyx (sepals), Corolla (petals), Androecium (microsporophylls/stamens forming pollen grains), and Gynoecium (megasporophylls/carpels bearing ovules)."
                },
                {
                    "topic": "Ch 2: Male Reproductive System Overview",
                    "original": "As you are aware, humans are sexually reproducing and viviparous. The reproductive events in humans include formation of gametes (gametogenesis), i.e., sperms in males and ovum in females, transfer of sperms into the female genital tract (insemination) and fusion of male and female gametes (fertilisation) leading to formation of zygote. This is followed by formation and development of blastocyst and its attachment to the uterine wall (implantation), embryonic development (gestation) and delivery of the baby (parturition). You have learnt that these reproductive events occur after puberty. There are remarkable differences between the reproductive events in the male and in the female...",
                    "revised": "Human Reproductive Events (Sequential): (1) Gametogenesis (Spermatogenesis / Oogenesis) -> (2) Insemination -> (3) Fertilisation (Zygote formation) -> (4) Cleavage & Blastocyst Implantation -> (5) Gestation (Embryonic development) -> (6) Parturition (Birth). Key difference: Spermatogenesis continues throughout life; Oogenesis ceases around age 50 (Menopause)."
                },
                {
                    "topic": "Ch 3: Reproductive Health - Problems and Strategies",
                    "original": "You have already learnt about the human reproductive system and its functions in Chapter 2. Now, let us discuss a closely related topic – reproductive health. What do we understand by this term? The term simply refers to healthy reproductive organs with normal functions. However, it has a broader perspective and includes the emotional and social aspects of reproduction also. According to the World Health Organisation (WHO), reproductive health means a total well-being in all aspects of reproduction, i.e., physical, emotional, behavioural and social.",
                    "revised": "Reproductive Health (WHO definition): Total well-being in all aspects of reproduction — physical, emotional, behavioural, and social. National Programs: India was the first nation to initiate family planning programs (1951), currently operating as Reproductive and Child Health Care (RCH) programs targeting maternal/infant mortality reduction, STI prevention, and population stabilization."
                }
            ]
        },
        {
            "class": "Class 12",
            "unit": "Unit 7: Genetics and Evolution",
            "chapters": "Ch 4: Principles of Inheritance and Variation | Ch 5: Molecular Basis of Inheritance | Ch 6: Evolution",
            "analysis": "Frequently uses folk analogies ('Why does an elephant always give birth to an elephant and not some other animal?') and historical meandering that delays reaching Mendel's ratios and DNA replication machinery.",
            "examples": [
                {
                    "topic": "Ch 4: Introduction to Heredity and Variation",
                    "original": "Have you ever wondered why an elephant always gives birth only to a baby elephant and not some other animal? Or why a mango seed forms only a mango plant and not any other plant? Given that they do, are the offspring identical to their parents? Or do they show differences in some of their characteristics? Have you ever wondered why siblings sometimes look so similar to each other? Or sometimes even so different? These and several related questions are dealt with scientifically in a branch of biology known as Genetics.",
                    "revised": "Genetics: The study of Heredity (transmission of traits from parents to offspring) and Variation (degree of difference between progeny and parents). Gregor Mendel (1856–1863) established the fundamental laws of inheritance through hybridization experiments on Garden Pea (Pisum sativum) using 7 pairs of contrasting traits."
                },
                {
                    "topic": "Ch 5: The Search for Genetic Material",
                    "original": "Even though the discovery of nuclein by Meischer and the proposition for principles of inheritance by Mendel were almost at the same time, but that the DNA acts as a genetic material took a long time to be discovered and proven. By 1926, the quest to determine the mechanism for genetic inheritance had reached the molecular level. Previous discoveries by Gregor Mendel, Walter Sutton, Thomas Hunt Morgan and numerous other scientists had narrowed the search to the chromosomes located in the nucleus of most cells. But the question of what molecule was actually the genetic material, had not been answered.",
                    "revised": "Identification of Genetic Material: (1) Frederick Griffith (1928) - Transforming Principle: Heat-killed S-strain transformed live R-strain Streptococcus pneumoniae into virulent S-strain. (2) Avery, MacLeod & McCarty (1944) - Biochemical Proof: Transformation inhibited only by DNase (not RNase/Protease), proving DNA is the transforming agent. (3) Hershey & Chase (1952) - Unequivocal Proof: Used Bacteriophage T2 labeled with 35S (protein) and 32P (DNA); only 32P entered E. coli cells."
                },
                {
                    "topic": "Ch 6: Origin of Life and Miller's Experiment",
                    "original": "When we look at stars on a clear night sky we are, in a way, looking back in time. Stellar distances are measured in light years. What we see today is an object whose emitted light started its journey millions of years back and is only reaching us now. When we look at things around us on earth we are seeing them instantly because light travels fast. The origin of life is considered a unique event in the history of universe. The universe is vast. Relatively speaking the earth itself is almost only a speck. Let us explore how it began.",
                    "revised": "Origin of Life (Evolutionary Timeline): (1) Big Bang (20 bya): Universe expanded, temperature dropped; (2) Earth formed (4.5 bya): Reducing atmosphere (CH4, NH3, H2O vapor, H2; no free O2); (3) First cellular life (2.0 bya). (4) S.L. Miller's Experiment (1953): Simulated primitive earth with electric discharge in CH4, NH3, H2, H2O vapor at 800°C -> synthesized Amino acids (glycine, alanine, aspartic acid)."
                }
            ]
        },
        {
            "class": "Class 12",
            "unit": "Unit 8: Biology in Human Welfare",
            "chapters": "Ch 7: Human Health and Disease | Ch 8: Microbes in Human Welfare",
            "analysis": "Historical folklore (early Greeks, 'good humor' hypothesis) and lengthy culinary narrations of curd/cheese making before providing scientific species and metabolite pathways.",
            "examples": [
                {
                    "topic": "Ch 7: Concept of Health & Disease History",
                    "original": "Health, for a long time, was considered as a state of body and mind where there was a balance of certain 'humors'. This is what early Greeks like Hippocrates as well as Indian Ayurveda system of medicine asserted. It was thought that persons with 'blackbile' belonged to hot personality and would have fevers. This idea was arrived at by pure reflective thought. The discovery of blood circulation by William Harvey using experimental method and the demonstration of normal body temperature in persons with blackbile using thermometer disproved the 'good humor' hypothesis of health.",
                    "revised": "Definition & Determinants of Health: Health is a state of complete physical, mental, and social well-being (not merely absence of disease). Disproven: Early 'Good Humor' hypothesis (Hippocrates) was disproved by William Harvey (discovered blood circulation and demonstrated normal temperature in black bile individuals using thermometer). Determinants: Genetic disorders, Infections, and Lifestyle habits."
                },
                {
                    "topic": "Ch 8: Microbes in Household Products",
                    "original": "You would be surprised to know that we use microbes or products derived from them everyday. A common example is the production of curd from milk. Micro-organisms such as Lactobacillus and others commonly called lactic acid bacteria (LAB) grow in milk and convert it to curd. During growth, the LAB produce acids that coagulate and partially digest the milk proteins. A small amount of curd added to the fresh milk as inoculum or starter contains millions of LAB, which at suitable temperatures multiply, thus converting milk to curd, which also improves its nutritional quality by increasing vitamin B12.",
                    "revised": "Microbes in Household Products: (1) Lactic Acid Bacteria (LAB / Lactobacillus): Converts milk to curd by producing lactic acid (coagulates milk proteins) and enriches Vitamin B12; also checks disease-causing microbes in gut. (2) Saccharomyces cerevisiae (Baker's Yeast): Ferments dough releasing CO2 (causes puffing/porous texture in bread). (3) Propionibacterium shermanii: Produces Swiss Cheese (large holes due to CO2 production). (4) Penicillium roqueforti: Ripens Roquefort cheese."
                }
            ]
        },
        {
            "class": "Class 12",
            "unit": "Unit 9: Biotechnology",
            "chapters": "Ch 9: Biotechnology: Principles and Processes | Ch 10: Biotechnology and its Applications",
            "analysis": "Often repeats classical breeding limitations vs rDNA benefits in descriptive paragraphs rather than presenting the recombinant DNA engineering steps as a precise flowchart.",
            "examples": [
                {
                    "topic": "Ch 9: Traditional vs Modern Biotechnology & EFB Definition",
                    "original": "Biotechnology deals with techniques of using live organisms or enzymes from organisms to produce products and processes useful to humans. In this sense, making curd, bread or wine, which are all microbe-mediated processes, could also be thought as a form of biotechnology. However, it is used in a restricted sense today, to refer to such of those processes which use genetically modified organisms to achieve the same on a larger scale. Further, many other processes/techniques are also included under biotechnology. For example, in vitro fertilisation leading to a 'test-tube' baby, synthesising a gene and using it, developing a DNA vaccine or correcting a defective gene, are all part of biotechnology.",
                    "revised": "Biotechnology: The application of biological systems and organisms to technical and industrial processes. (1) Traditional: Microbe-mediated natural processes (curd, bread, wine). (2) Modern: Genetic engineering & Recombinant DNA technology. (3) EFB Definition: 'The integration of natural science and organisms, cells, parts thereof, and molecular analogues for products and services.'"
                },
                {
                    "topic": "Ch 10: Applications in Agriculture (Bt Cotton Mechanism)",
                    "original": "Let us take the example of Bt cotton. Some strains of Bacillus thuringiensis produce proteins that kill certain insects such as lepidopterans (tobacco budworm, armyworm), coleopterans (beetles) and dipterans (flies, mosquitoes). B. thuringiensis forms protein crystals during a particular phase of their growth. These crystals contain a toxic insecticidal protein. Why does this toxin not kill the Bacillus? Actually, the Bt toxin protein exist as inactive protoxins but once an insect ingest the inactive toxin, it is converted into an active form of toxin due to the alkaline pH of the gut which solubilise the crystals.",
                    "revised": "Bt Cotton Pest Resistance: (1) Source: Bacillus thuringiensis produces insecticidal crystal protein (Cry protein) active against Lepidopterans (armyworm), Coleopterans (beetles), Dipterans (flies). (2) Mechanism: Inactive protoxin ingested by insect -> solubilized by alkaline pH of insect midgut -> activated toxin binds midgut epithelial cells -> creates pores causing cell lysis and insect death. (3) Genes: cryIAc & cryIIAb control cotton bollworms; cryIAb controls corn borer."
                }
            ]
        },
        {
            "class": "Class 12",
            "unit": "Unit 10: Ecology",
            "chapters": "Ch 11: Organisms and Populations | Ch 12: Ecosystem | Ch 13: Biodiversity and Conservation",
            "analysis": "The exact source of the user's example! Filled with conversational transitions, nature analogies, and reflective storytelling about ecological degradation instead of direct quantitative models.",
            "examples": [
                {
                    "topic": "Ch 12: Ecosystem Structure and Functional Overview (User Reference)",
                    "original": "In earlier classes, you have looked at the various components of the environment - abiotic and biotic. You studied how the individual biotic and abiotic factors affected each other and their surrounding. Let us look at these components in a more integrated manner and see how the flow of energy takes place within these components of the ecosystem.",
                    "revised": "Ecosystem Structure & Function: We analyze an ecosystem via its four structural/functional components: (1) Productivity (Biomass synthesis/inputs); (2) Energy Flow (Unidirectional transfer via food chains and food webs); (3) Decomposition & Nutrient Cycling (Biogeochemical cycles); (4) Outputs (Degradation and respiratory heat loss)."
                },
                {
                    "topic": "Ch 11: Responses to Abiotic Factors (Thermoregulation)",
                    "original": "Having realised that the abiotic conditions of many habitats may vary drastically in time, we now ask - how do the organisms living in such habitats cope or manage with stressful conditions? But before attempting to answer this question, we should perhaps ask first why a highly variable external environment should bother organisms after all! One would expect that during the course of millions of years of their existence, many species would have evolved a relatively constant internal (within the body) environment...",
                    "revised": "Homeostasis & Adaptations to Abiotic Stress: Organisms maintain physiological constancy through four distinct evolutionary strategies: (1) Regulators: Maintain constant body temperature/osmolarity by physiological/behavioral means (Mammals, Birds); (2) Conformers: Internal conditions fluctuate with external environment (99% animals, nearly all plants); (3) Migrate: Temporary relocation to hospitable conditions (e.g., Keoladeo National Park, Bharatpur); (4) Suspend: Metabolic dormancy (Spores in bacteria, Diapause in zooplankton, Hibernation/Aestivation)."
                },
                {
                    "topic": "Ch 13: Why Should We Conserve Biodiversity?",
                    "original": "There are many reasons, some obvious and others not so obvious, but all equally important. They can be grouped into three categories: narrowly utilitarian, broadly utilitarian, and ethical. The narrowly utilitarian arguments for conserving biodiversity are obvious; humans derive countless direct economic benefits from nature - food (cereals, pulses, fruits), firewood, fibre, construction material, industrial products... What about broadly utilitarian arguments? It says that biodiversity plays a major role in many ecosystem services that nature provides. The Amazon forest is estimated to produce, through photosynthesis, 20 per cent of the total oxygen...",
                    "revised": "Arguments for Biodiversity Conservation: (1) Narrowly Utilitarian: Direct economic benefits (food, fibre, timber, tannins, lubricants, and 25% of commercial pharmaceuticals derived from 25,000 plant species; Bioprospecting). (2) Broadly Utilitarian: Crucial ecosystem services (Amazon rainforest produces 20% of global atmospheric O2; pollinator services; aesthetic value). (3) Ethical Argument: Moral obligation to protect all species co-inhabiting earth and pass healthy biological legacy to future generations."
                }
            ]
        }
    ]

    for unit_idx, u in enumerate(units_data, 1):
        # Unit Heading
        p_uh = doc.add_paragraph()
        p_uh.paragraph_format.space_before = Pt(14)
        p_uh.paragraph_format.space_after = Pt(2)
        r_uh = p_uh.add_run(f"UNIT {unit_idx}: {u['unit']} ({u['class']})")
        r_uh.font.name = "Calibri"
        r_uh.font.size = Pt(13)
        r_uh.font.bold = True
        r_uh.font.color.rgb = RGBColor(0x00, 0x4B, 0x87) # Cobalt Blue

        # Chapters included
        p_ch = doc.add_paragraph()
        p_ch.paragraph_format.space_after = Pt(4)
        r_ch = p_ch.add_run(f"Chapters: {u['chapters']}")
        r_ch.font.name = "Calibri"
        r_ch.font.size = Pt(9.5)
        r_ch.font.italic = True
        r_ch.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

        # Fluff Analysis Callout
        p_an = doc.add_paragraph()
        p_an.paragraph_format.space_after = Pt(6)
        r_an_l = p_an.add_run("Fluff & Padding Profile: ")
        r_an_l.font.name = "Calibri"
        r_an_l.font.size = Pt(9.5)
        r_an_l.font.bold = True
        r_an_l.font.color.rgb = RGBColor(0xC0, 0x39, 0x2B) # Dark Red
        r_an_t = p_an.add_run(u['analysis'])
        r_an_t.font.name = "Calibri"
        r_an_t.font.size = Pt(9.5)
        r_an_t.font.color.rgb = RGBColor(0x33, 0x33, 0x33)

        # Comparison Table
        table = doc.add_table(rows=1, cols=3)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        set_table_borders(table, color="CCCCCC", sz="4")

        # Column widths
        widths = [Inches(1.5), Inches(2.75), Inches(2.75)]
        for ci, w in enumerate(widths):
            table.columns[ci].width = w

        # Header Row
        hdr = table.rows[0]
        hdr_labels = ["Topic / Context", "NCERT Original (Fluff / Filler)", "Streamlined High-Yield Note (Proposal)"]
        for ci, label in enumerate(hdr_labels):
            cell = hdr.cells[ci]
            cell.width = widths[ci]
            set_cell_background(cell, "1B365D")
            set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(label)
            r.font.name = "Calibri"
            r.font.size = Pt(9.5)
            r.font.bold = True
            r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

        # Data Rows
        for ex_idx, ex in enumerate(u['examples']):
            row = table.add_row()
            bg_color = "F9FAFC" if ex_idx % 2 == 1 else "FFFFFF"

            # Col 0: Topic
            c0 = row.cells[0]
            c0.width = widths[0]
            set_cell_background(c0, bg_color)
            set_cell_margins(c0, top=90, bottom=90, left=100, right=100)
            p0 = c0.paragraphs[0]
            p0.paragraph_format.space_after = Pt(0)
            r0 = p0.add_run(ex['topic'])
            r0.font.name = "Calibri"
            r0.font.size = Pt(9)
            r0.font.bold = True
            r0.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

            # Col 1: Original
            c1 = row.cells[1]
            c1.width = widths[1]
            set_cell_background(c1, "FFF5F5" if ex_idx % 2 == 0 else "FFEFEF") # Soft Red tint
            set_cell_margins(c1, top=90, bottom=90, left=100, right=100)
            p1 = c1.paragraphs[0]
            p1.paragraph_format.space_after = Pt(0)
            r1 = p1.add_run(f'"{ex["original"]}"')
            r1.font.name = "Calibri"
            r1.font.size = Pt(8.5)
            r1.font.italic = True
            r1.font.color.rgb = RGBColor(0x77, 0x22, 0x22)

            # Col 2: Revised
            c2 = row.cells[2]
            c2.width = widths[2]
            set_cell_background(c2, "F0FFF4" if ex_idx % 2 == 0 else "E6F9EC") # Soft Green tint
            set_cell_margins(c2, top=90, bottom=90, left=100, right=100)
            p2 = c2.paragraphs[0]
            p2.paragraph_format.space_after = Pt(0)
            r2 = p2.add_run(ex['revised'])
            r2.font.name = "Calibri"
            r2.font.size = Pt(8.5)
            r2.font.color.rgb = RGBColor(0x11, 0x44, 0x22)

        doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Summary Implementation Guidelines section
    p_imp = doc.add_paragraph()
    p_imp.paragraph_format.space_before = Pt(14)
    p_imp.paragraph_format.space_after = Pt(4)
    r_imp = p_imp.add_run("Standardized Rewriting Rules for Notes Preparation")
    r_imp.font.name = "Calibri"
    r_imp.font.size = Pt(13)
    r_imp.font.bold = True
    r_imp.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

    guidelines = [
        ("Conversational Openings -> Structural Frameworks", "Drop 'Have you wondered', 'As we discussed', 'Let us now look at'. Start directly with the definition, structural components, or diagnostic criteria."),
        ("Rhetorical Questions -> Causality & Mechanisms", "Replace 'Why do leaves fall?' with 'Abscisic acid and ethylene induce petiole abscission layer formation.'"),
        ("Narrative Descriptions -> Tables & Flowcharts", "Convert multi-paragraph comparative texts (e.g. C3 vs C4, Mitosis vs Meiosis, Chordata vs Non-chordata) into standardized comparison tables."),
        ("Historical Digressions -> Milestone Timelines", "Condense long discovery narratives into bulleted scientist milestones: [Scientist (Year): Core discovery & technique]."),
        ("100% Strict NCERT Keyword Preservation", "Every bold keyword, scientific name (italicized), enzyme, organelle, and quantitative value from NCERT is strictly preserved.")
    ]

    for g_title, g_desc in guidelines:
        p_g = doc.add_paragraph()
        p_g.paragraph_format.left_indent = Inches(0.2)
        p_g.paragraph_format.space_after = Pt(3)
        rg_b = p_g.add_run(f"• {g_title}: ")
        rg_b.font.name = "Calibri"
        rg_b.font.size = Pt(9.5)
        rg_b.font.bold = True
        rg_b.font.color.rgb = RGBColor(0x00, 0x4B, 0x87)
        rg_t = p_g.add_run(g_desc)
        rg_t.font.name = "Calibri"
        rg_t.font.size = Pt(9.5)
        rg_t.font.color.rgb = RGBColor(0x33, 0x33, 0x33)

    doc.save(output_path)
    print(f"Successfully generated proposal document: {output_path}")

if __name__ == "__main__":
    build_proposal_document()
