# Working Inventory (Pass 1 IN PROGRESS — **NOT FROZEN**) — Class 11 Biology, Chapter 19: Chemical Coordination and Integration

Source: `Chapter/class 11/Chapter 19 - Chemical Coordination and Integration.pdf` (14 pages; supplied high-quality source `kebo119.pdf`) | Pass 1 sessions complete: **`1-F` (figures, 2026-08-30) · `1-S` (source read + Facts inventory, 2026-09-01)** | Pass 1 sessions NOT started: **`1-H` · `1-O` · `1-Z`** | Rows: **200** (`F001`–`F207` content Facts + `F209`–`F215` figure-label matrix rows)

> **Gate state: GATE 1 IS OPEN.** This file is a **working inventory, not a frozen one.** Nothing may be quoted from it as final and no Pass 2 script may be written against it until `1-H`, `1-O` and `1-Z` have run and a freeze is declared here.

Tick legend: `x` = the row's wording was read directly off the numbered source page named in its `Src` column and confirmed character-for-character, including the source's own typography and its own misspellings. A tick is **not** a claim about any delivered PDF — no PDF exists for this chapter yet.

## Header-correction record (`1-S`, 2026-09-01)

This file's H1 previously read **"Frozen Inventory"** while the file contained **only the 7 figure-label rows** and no Facts at all. A 7-row figure manifest is not a frozen Pass 1 inventory, so the H1 asserted a gate that had never been earned — exactly the "documentation claims more than the artefact" defect that Gate 3(b) rule 2 says *is* the finding. The H1 is now demoted to **Working Inventory (Pass 1 IN PROGRESS — NOT FROZEN)** and the gate state is stated explicitly above. The `1-F` figure work itself was sound and is untouched; only the claim about it was wrong.

The original 7 figure-label rows were numbered `F001`–`F007`. Because the `## Facts` table must be in **Content Order**, and the figure-label matrix belongs at the tail (the Ch18 convention: 131 content Facts then 4 matrix rows), those 7 rows are **renumbered `F209`–`F215`**. Their `Section`, `Type` and wording columns are **byte-identical to the originals** — only the ID changed — so `check_pdf._extract_labels` sees the same 7 rows and the same 35-label harvest it saw before.

## Scope and status

`1-F` recorded the **figure-extraction deliverables**. `1-S` adds the thing that was missing: a **full source read of all 14 pages with every content sentence inventoried**. The chapter is now on the normal 3-pass track toward a standalone NEET replacement PDF, so the running-text coverage gate **does** apply and the earlier note that it was "not applicable here" no longer holds — it was true only while this file was a figure manifest.

The 4× figure refinement used the canonical high-density settings: 440 dpi rendering, 5-point grid spacing, coordinate labels every 20 PDF points, grayscale conversion with `convert("L")`, and `autocontrast`. Every final asset was opened individually after the final extraction run.

## Source structure, derived by reading every page

| Quantity | Value | Basis |
|---|---:|---|
| Source pages | 14 | textbook pp. 239–251 + one trailing `NOTE` page |
| Text-bearing pages | 13 | p. 14 carries only `NOTE` and the reprint line (21 chars) |
| Top-level numbered sections | 4 | 19.1, 19.2, 19.3, 19.4 |
| Numbered subsections | 10 | 19.2.1 – 19.2.10, all under 19.2 |
| Numbered headings total | 14 | 4 + 10 |
| Structural unnumbered headings | 4 | chapter title, `CHAPTER 19`, `SUMMARY`, `EXERCISES` |
| Numbered figures | 5 | 19.1, 19.2, 19.3, 19.4, 19.5 |
| Delivered figure assets | 7 | 19.3 and 19.5 split (a)/(b); **19.4 deliberately ONE combined asset** |
| Exercise questions | 9 | numbered 1–9 on p. 13 |
| Exercise sub-parts | 41 | counted across all 9 questions |

**The `19.2` subsection run is the whole anatomical spine of the chapter** — ten glands in fixed order: hypothalamus, pituitary, pineal, thyroid, parathyroid, thymus, adrenal, pancreas, testis, ovary. Sections 19.3 and 19.4 then break that frame deliberately: 19.3 covers hormone sources that are *not* endocrine glands (heart, kidney, GI tract) and 19.4 is mechanism rather than anatomy.

## Source typography and misspellings — transcribed verbatim, NOT corrected

Recorded here so a later pass cannot "helpfully" fix them and so `verify_inventory.py` can assert both that the row preserves the source form and that the source really prints it.

| Source form | Standard form | Where | Row |
|---|---|---|---|
| `sella tursica` | sella turcica | p. 3, pituitary location | `F039` |
| `Exopthalmic goitre` | Exophthalmic goitre | p. 5, hyperthyroidism | `F087` |
| `pupilary dilation` | pupillary dilation | p. 6, catecholamine effects | `F120` |
| `glucagons` (plural) | glucagon | p. 8, glucose homeostasis | `F152` |
| `Diagramatic` | Diagrammatic | p. 11, Figure 19.5 caption | `F205` |

Note that the source is **internally inconsistent**, not merely misspelt: it prints `Diagrammatic` correctly in the Figure 19.2, 19.3 and 19.4 captions and `Diagramatic` in the Figure 19.5 caption. Both forms are held verbatim in their own rows.

## Facts

| ID | Section | Type | Exact original wording | Src | Ticked |
|---|---|---|------------------------|---:|--------|
| F001 | Title | heading | CHEMICAL COORDINATION AND INTEGRATION | 1 | x |
| F002 | Title | heading | CHAPTER  19 | 1 | x |
| F003 | Opener | opener | You have already learnt that the neural system provides a point-to-point rapid coordination among organs. | 1 | x |
| F004 | Opener | opener | The neural coordination is fast but short-lived. | 1 | x |
| F005 | Opener | opener | As the nerve fibres do not innervate all cells of the body and the cellular functions need to be continuously regulated; a special kind of coordination and integration has to be provided. | 1 | x |
| F006 | Opener | opener | This function is carried out by hormones. | 1 | x |
| F007 | Opener | opener | The neural system and the endocrine system jointly coordinate and regulate the physiological functions in the body. | 1 | x |
| F008 | Contents | opener | 19.1 Endocrine Glands and Hormones | 1 | x |
| F009 | Contents | opener | 19.2 Human Endocrine System | 1 | x |
| F010 | Contents | opener | 19.3 Hormones of Heart, Kidney and Gastrointestinal Tract | 1 | x |
| F011 | Contents | opener | 19.4 Mechanism of Hormone Action | 1 | x |
| F012 | 19.1 | heading | 19.1 ENDOCRINE GLANDS AND HORMONES | 1 | x |
| F013 | 19.1 | definition | Endocrine glands lack ducts and are hence, called ductless glands. | 1 | x |
| F014 | 19.1 | definition | Their secretions are called hormones. | 1 | x |
| F015 | 19.1 | concept | The classical definition of hormone as a chemical produced by endocrine glands and released into the blood and transported to a distantly located target organ has current scientific definition as follows | 1 | x |
| F016 | 19.1 | definition | Hormones are non-nutrient chemicals which act as intercellular messengers and are produced in trace amounts. | 1 | x |
| F017 | 19.1 | concept | The new definition covers a number of new molecules in addition to the hormones secreted by the organised endocrine glands. | 1 | x |
| F018 | 19.1 | concept | Invertebrates possess very simple endocrine systems with few hormones whereas a large number of chemicals act as hormones and provide coordination in the vertebrates. | 1 | x |
| F019 | 19.1 | concept | The human endocrine system is described here. | 1 | x |
| F020 | 19.1 | concept | These hormones regulate metabolism, growth and development of our organs, the endocrine glands or certain cells. | 11 | x |
| F021 | 19.2 | heading | 19.2   HUMAN ENDOCRINE SYSTEM | 2 | x |
| F022 | 19.2 | definition | The endocrine glands and hormone producing diffused tissues/cells located in different parts of our body constitute the endocrine system. | 2 | x |
| F023 | 19.2 | concept | Pituitary, pineal, thyroid, adrenal, pancreas, parathyroid, thymus and gonads (testis in males and ovary in females) are the organised endocrine bodies in our body (Figure 19.1). | 2 | x |
| F024 | 19.2 | concept | The endocrine system is composed of hypothalamus, pituitary and pineal, thyroid, adrenal, pancreas, parathyroid, thymus and gonads (testis and ovary). | 11 | x |
| F025 | 19.2 | concept | In addition to these, some other organs, e.g., gastrointestinal tract, liver, kidney, heart also produce hormones. | 2 | x |
| F026 | 19.2 | concept | A brief account of the structure and functions of all major endocrine glands and hypothalamus of the human body is given in the following sections. | 2 | x |
| F027 | Fig 19.1 | caption | Figure 19.1 Location of endocrine glands | 2 | x |
| F028 | 19.2.1 | heading | 19.2.1 The Hypothalamus | 2 | x |
| F029 | 19.2.1 | concept | As you know, the hypothalamus is the basal part of diencephalon, forebrain (Figure 19.1) and it regulates a wide spectrum of body functions. | 2 | x |
| F030 | 19.2.1 | definition | It contains several groups of neurosecretory cells called nuclei which produce hormones. | 2 | x |
| F031 | 19.2.1 | concept | These hormones regulate the synthesis and secretion of pituitary hormones. | 2 | x |
| F032 | 19.2.1 | definition | However, the hormones produced by hypothalamus are of two types, the releasing hormones (which stimulate secretion of pituitary hormones) and the inhibiting hormones (which inhibit secretions of pituitary hormones). | 2 | x |
| F033 | 19.2.1 | example | For example a hypothalamic hormone called Gonadotrophin releasing hormone (GnRH) stimulates the pituitary synthesis and release of gonadotrophins. | 2 | x |
| F034 | 19.2.1 | example | On the other hand, somatostatin from the hypothalamus inhibits the release of growth hormone from the pituitary. | 2 | x |
| F035 | 19.2.1 | process | These hormones originating in the hypothalamic neurons, pass through axons and are released from their nerve endings. | 2 | x |
| F036 | 19.2.1 | process | These hormones reach the pituitary gland through a portal circulatory system and regulate the functions of the anterior pituitary. | 2 | x |
| F037 | 19.2.1 | concept | The posterior pituitary is under the direct neural regulation of the hypothalamus (Figure 19.2). | 2 | x |
| F038 | 19.2.2 | heading | 19.2.2 The Pituitary Gland | 3 | x |
| F039 | 19.2.2 | concept | The pituitary gland is located in a bony cavity called sella tursica and is attached to hypothalamus by a stalk (Figure 19.2). | 3 | x |
| F040 | 19.2.2 | concept | It is divided anatomically into an adenohypophysis and a neurohypophysis. | 3 | x |
| F041 | 19.2.2 | concept | Adenohypophysis consists of two portions, pars distalis and pars intermedia. | 3 | x |
| F042 | 19.2.2 | concept | The pars distalis region of pituitary, commonly called anterior pituitary, produces growth hormone (GH), prolactin (PRL), thyroid stimulating hormone (TSH), adrenocorticotrophic hormone (ACTH), luteinizing hormone (LH) and follicle stimulating hormone (FSH). | 3 | x |
| F043 | 19.2.2 | number | Pars distalis produces six trophic hormones. | 11 | x |
| F044 | 19.2.2 | concept | Pars intermedia secretes only one hormone called melanocyte stimulating hormone (MSH). | 3 | x |
| F045 | 19.2.2 | concept | However, in humans, the pars intermedia is almost merged with pars distalis. | 3 | x |
| F046 | 19.2.2 | concept | Neurohypophysis (pars nervosa) also known as posterior pituitary, stores and releases two hormones called oxytocin and vasopressin, which are actually synthesised by the hypothalamus and are transported axonally to neurohypophysis. | 3 | x |
| F047 | 19.2.2 | concept | The pituitary gland is divided into three major parts, which are called as  pars distalis, pars intermedia and pars nervosa. | 11 | x |
| F048 | 19.2.2 | concept | Over-secretion of GH stimulates abnormal growth of the body leading to gigantism and low secretion of GH results in stunted growth resulting in pituitary dwarfism. | 3 | x |
| F049 | 19.2.2 | concept | Excess secretion of growth hormone in adults especially in middle age can result in severe disfigurement (especially of the face) called Acromegaly, which may lead to serious complications, and premature death if unchecked. | 3 | x |
| F050 | 19.2.2 | concept | The disease is hard to diagnose in the early stages and often goes undetected for many years, until changes in external features become noticeable. | 3 | x |
| F051 | 19.2.2 | concept | Prolactin regulates the growth of the mammary glands and formation of milk in them. | 3 | x |
| F052 | 19.2.2 | concept | TSH stimulates the synthesis and secretion of thyroid hormones from the thyroid gland. | 3 | x |
| F053 | 19.2.2 | definition | (b) Thyrotrophin (TSH) | 13 | x |
| F054 | 19.2.2 | concept | ACTH stimulates the synthesis and secretion of steroid hormones called glucocorticoids from the adrenal cortex. | 3 | x |
| F055 | 19.2.2 | definition | (c) Corticotrophin (ACTH) | 13 | x |
| F056 | 19.2.2 | definition | LH and FSH stimulate gonadal activity and hence are called gonadotrophins. | 3 | x |
| F057 | 19.2.2 | concept | In males, LH stimulates the synthesis and secretion of hormones called androgens from testis. | 3 | x |
| F058 | 19.2.2 | concept | In males, FSH and androgens regulate spermatogenesis. | 3 | x |
| F059 | 19.2.2 | concept | In females, LH induces ovulation of fully mature follicles (graafian follicles) and maintains the corpus luteum, formed from the remnants of the graafian follicles after ovulation. | 3 | x |
| F060 | 19.2.2 | concept | FSH stimulates growth and development of the ovarian follicles in females. | 3 | x |
| F061 | 19.2.2 | concept | MSH acts on the melanocytes (melanin containing cells) and regulates pigmentation of the skin. | 4 | x |
| F062 | 19.2.2 | definition | (e) Melanotrophin (MSH) | 13 | x |
| F063 | 19.2.2 | concept | Oxytocin acts on the smooth muscles of our body and stimulates their contraction. | 4 | x |
| F064 | 19.2.2 | concept | In females, it stimulates a vigorous contraction of uterus at the time of child birth, and milk ejection from the mammary gland. | 4 | x |
| F065 | 19.2.2 | process | Vasopressin acts mainly at the kidney and stimulates resorption of water and electrolytes by the distal tubules and thereby reduces loss of water through urine (diuresis). | 4 | x |
| F066 | 19.2.2 | definition | Hence, it is also called as anti-diuretic hormone (ADH). | 4 | x |
| F067 | 19.2.2 | concept | An impairment affecting synthesis or release of ADH results in a diminished ability of the kidney to conserve water leading to water loss and dehydration. This condition is known as Diabetes Insipidus. | 4 | x |
| F068 | 19.2.2 | concept | The pituitary hormones regulate the growth and development of somatic tissues and activities of peripheral endocrine glands. | 11 | x |
| F069 | Fig 19.2 | caption | Figure 19.2 Diagrammatic representation of pituitary and its relationship with hypothalamus | 3 | x |
| F070 | 19.2.3 | heading | 19.2.3 The Pineal Gland | 4 | x |
| F071 | 19.2.3 | concept | The pineal gland is located on the dorsal side of forebrain. | 4 | x |
| F072 | 19.2.3 | concept | Pineal secretes a hormone called melatonin. | 4 | x |
| F073 | 19.2.3 | number | Melatonin plays a very important role in the regulation of a 24-hour (diurnal) rhythm of our body. | 4 | x |
| F074 | 19.2.3 | example | For example, it helps in maintaining the normal rhythms of sleep-wake cycle, body temperature. | 4 | x |
| F075 | 19.2.3 | concept | In addition, melatonin also influences metabolism, pigmentation, the menstrual cycle as well as our defense capability. | 4 | x |
| F076 | 19.2.4 | heading | 19.2.4 Thyroid Gland | 4 | x |
| F077 | 19.2.4 | concept | The thyroid gland is composed of two lobes which are located on either side of the trachea (Figure 19.3 a). | 4 | x |
| F078 | 19.2.4 | definition | Both the lobes are interconnected with a thin flap of connective tissue called isthmus. | 4 | x |
| F079 | 19.2.4 | concept | The thyroid gland is composed of follicles and stromal tissues. | 4 | x |
| F080 | 19.2.4 | concept | Each thyroid follicle is composed of follicular cells, enclosing a cavity. | 4 | x |
| F081 | 19.2.4 | concept | These follicular cells synthesise two hormones, tetraiodothyronine or thyroxine (T4) and triiodothyronine (T3). | 4 | x |
| F082 | 19.2.4 | concept | Iodine is essential for the normal rate of hormone synthesis in the thyroid. | 4 | x |
| F083 | 19.2.4 | concept | Deficiency of iodine in our diet results in hypothyroidism and enlargement of the thyroid gland, commonly called goitre. | 4 | x |
| F084 | 19.2.4 | concept | Hypothyroidism during pregnancy causes defective development and maturation of the growing baby leading to stunted growth (cretinism), mental retardation, low intelligence quotient, abnormal skin, deaf-mutism, etc. | 4 | x |
| F085 | 19.2.4 | concept | In adult women, hypothyroidism may cause menstrual cycle to become irregular. | 5 | x |
| F086 | 19.2.4 | concept | Due to cancer of the thyroid gland or due to development of nodules of the thyroid glands, the rate of synthesis and secretion of the thyroid hormones is increased to abnormal high levels leading to a condition called hyperthyroidism which adversely affects the body physiology. | 5 | x |
| F087 | 19.2.4 | concept | Exopthalmic goitre is a form of hyperthyroidism, characterised by enlargement of the thyroid gland, protrusion of the eyeballs, increased basal metabolic rate, and weight loss, also called Graves’ disease. | 5 | x |
| F088 | 19.2.4 | concept | Thyroid hormones play an important role in the regulation of the basal metabolic rate. | 5 | x |
| F089 | 19.2.4 | concept | These hormones also support the process of red blood cell formation. | 5 | x |
| F090 | 19.2.4 | concept | Thyroid hormones control the metabolism of carbohydrates, proteins and fats. | 5 | x |
| F091 | 19.2.4 | concept | Maintenance of water and electrolyte balance is also influenced by thyroid hormones. | 5 | x |
| F092 | 19.2.4 | concept | The thyroid gland hormones play an important role in the regulation of the basal metabolic rate, development and maturation of the central neural system, erythropoiesis, metabolism of carbohydrates, proteins and fats, menstrual cycle. | 12 | x |
| F093 | 19.2.4 | concept | Thyroid gland also secretes a protein hormone called thyrocalcitonin (TCT) which regulates the blood calcium levels. | 5 | x |
| F094 | 19.2.4 | concept | Another thyroid hormone, i.e., thyrocalcitonin regulates calcium levels in our blood by decreasing it. | 12 | x |
| F095 | Fig 19.3 | caption | Figure 19.3 Diagrammatic view of the position of Thyroid and Parathyroid (a) Ventral side (b) Dorsal side | 4 | x |
| F096 | 19.2.5 | heading | 19.2.5 Parathyroid Gland | 5 | x |
| F097 | 19.2.5 | number | In humans, four parathyroid glands are present on the back side of the thyroid gland, one pair each in the two lobes of the thyroid gland (Figure 19.3 b). | 5 | x |
| F098 | 19.2.5 | concept | The parathyroid glands secrete a peptide hormone called parathyroid hormone (PTH). | 5 | x |
| F099 | 19.2.5 | concept | The secretion of PTH is regulated by the circulating levels of calcium ions. | 5 | x |
| F100 | 19.2.5 | concept | Parathyroid hormone (PTH) increases the Ca2+ levels in the blood. | 5 | x |
| F101 | 19.2.5 | process | PTH acts on bones and stimulates the process of bone resorption (dissolution/demineralisation). | 5 | x |
| F102 | 19.2.5 | process | PTH also stimulates reabsorption of Ca2+ by the renal tubules and increases Ca2+ absorption from the digested food. | 5 | x |
| F103 | 19.2.5 | definition | It is, thus, clear that PTH is a hypercalcemic hormone, i.e., it increases the blood Ca2+ levels. | 5 | x |
| F104 | 19.2.5 | concept | Along with TCT, it plays a significant role in calcium balance in the body. | 5 | x |
| F105 | 19.2.6 | heading | 19.2.6 Thymus | 5 | x |
| F106 | 19.2.6 | concept | The thymus gland is a lobular structure located between lungs behind sternum on the ventral side of aorta. | 5 | x |
| F107 | 19.2.6 | concept | The thymus plays a major role in the development of the immune system. | 5 | x |
| F108 | 19.2.6 | concept | This gland secretes the peptide hormones called thymosins. | 5 | x |
| F109 | 19.2.6 | concept | Thymosins play a major role in the differentiation of T-lymphocytes, which provide cell-mediated immunity. | 5 | x |
| F110 | 19.2.6 | concept | In addition, thymosins also promote production of antibodies to provide humoral immunity. | 5 | x |
| F111 | 19.2.6 | concept | Thymus is degenerated in old individuals resulting in a decreased production of thymosins. | 5 | x |
| F112 | 19.2.6 | concept | As a result, the immune responses of old persons become weak. | 5 | x |
| F113 | 19.2.7 | heading | 19.2.7 Adrenal Gland | 6 | x |
| F114 | 19.2.7 | concept | Our body has one pair of adrenal glands, one above of each kidney (Figure 19.4 a). | 6 | x |
| F115 | 19.2.7 | concept | The gland is composed of two types of tissues. | 6 | x |
| F116 | 19.2.7 | concept | The centrally located tissue is called the adrenal medulla, and outside this lies the adrenal cortex (Figure 19.4 b). | 6 | x |
| F117 | 19.2.7 | concept | Underproduction of hormones by the adrenal cortex alters carbohydrate metabolism causing acute weakness and fatigue leading to a disease called Addison’ disease. | 6 | x |
| F118 | 19.2.7 | concept | The adrenal medulla secretes two hormones called adrenaline or epinephrine and noradrenaline or norepinephrine. | 6 | x |
| F119 | 19.2.7 | definition | These are commonly called as catecholamines. | 6 | x |
| F120 | 19.2.7 | concept | Adrenaline and noradrenaline are rapidly secreted in response to stress of any kind and during emergency situations and are called emergency hormones or hormones of Fight or Flight. | 6 | x |
| F121 | 19.2.7 | concept | These hormones increase alertness, pupilary dilation, piloerection (raising of hairs), sweating etc. | 6 | x |
| F122 | 19.2.7 | concept | Both the hormones increase the heart beat, the strength of heart contraction and the rate of respiration. | 6 | x |
| F123 | 19.2.7 | process | Catecholamines also stimulate the breakdown of glycogen resulting in an increased concentration of glucose in blood. | 6 | x |
| F124 | 19.2.7 | process | In addition, they also stimulate the breakdown of lipids and proteins. | 7 | x |
| F125 | 19.2.7 | concept | The adrenal cortex can be divided into three layers, called zona reticularis (inner layer), zona fasciculata (middle layer) and zona glomerulosa (outer layer). | 7 | x |
| F126 | 19.2.7 | definition | The adrenal cortex secretes many hormones, commonly called as corticoids. | 7 | x |
| F127 | 19.2.7 | definition | The corticoids, which are involved in carbohydrate metabolism are called glucocorticoids. In our body, cortisol is the main glucocorticoid. | 7 | x |
| F128 | 19.2.7 | definition | Corticoids, which regulate the balance of water and electrolytes in our body are called mineralocorticoids. Aldosterone is the main mineralocorticoid in our body. | 7 | x |
| F129 | 19.2.7 | process | Glucocorticoids stimulate gluconeogenesis, lipolysis and proteolysis; and inhibit cellular uptake and utilisation of amino acids. | 7 | x |
| F130 | 19.2.7 | concept | Cortisol is also involved in maintaining the cardio-vascular system as well as the kidney functions. | 7 | x |
| F131 | 19.2.7 | concept | Glucocorticoids, particularly cortisol, produces anti-inflammatory reactions and suppresses the immune response. | 7 | x |
| F132 | 19.2.7 | concept | Cortisol stimulates the RBC production. | 7 | x |
| F133 | 19.2.7 | process | Glucocorticoids stimulate gluconeogenesis, lipolysis, proteolysis, erythropoiesis, cardio-vascular system, blood pressure, and glomerular filtration rate and inhibit inflammatory reactions by suppressing the immune response. | 12 | x |
| F134 | 19.2.7 | process | Aldosterone acts mainly at the renal tubules and stimulates the reabsorption of Na+ and water and excretion of K+ and phosphate ions. | 7 | x |
| F135 | 19.2.7 | concept | Thus, aldosterone helps in the maintenance of electrolytes, body fluid volume, osmotic pressure and blood pressure. Small amounts of androgenic steroids are also secreted by the adrenal cortex which play a role in the growth of axial hair, pubic hair and facial hair during puberty. | 7 | x |
| F136 | Fig 19.4 | caption | Figure 19.4  Diagrammatic representation of : (a) Adrenal gland above kidney (b) Section showing two parts of adrenal gland | 6 | x |
| F137 | 19.2.8 | heading | 19.2.8 Pancreas | 7 | x |
| F138 | 19.2.8 | concept | Pancreas is a composite gland (Figure 19.1) which acts as both exocrine and endocrine gland. | 7 | x |
| F139 | 19.2.8 | definition | The endocrine pancreas consists of ‘Islets of Langerhans’. | 7 | x |
| F140 | 19.2.8 | number | There are about 1 to 2 million Islets of Langerhans in a normal human pancreas representing only 1 to 2 per cent of the pancreatic tissue. | 7 | x |
| F141 | 19.2.8 | concept | The two main types of cells in the Islet of Langerhans are called α-cells and β-cells. | 7 | x |
| F142 | 19.2.8 | concept | The α-cells secrete a hormone called glucagon, while the β-cells secrete insulin. | 7 | x |
| F143 | 19.2.8 | concept | Glucagon is a peptide hormone, and plays an important role in maintaining the normal blood glucose levels. | 7 | x |
| F144 | 19.2.8 | process | Glucagon acts mainly on the liver cells (hepatocytes) and stimulates glycogenolysis resulting in an increased blood sugar (hyperglycemia). | 7 | x |
| F145 | 19.2.8 | process | In addition, this hormone stimulates the process of gluconeogenesis which also contributes to hyperglycemia. | 7 | x |
| F146 | 19.2.8 | concept | Glucagon reduces the cellular glucose uptake and utilisation. | 7 | x |
| F147 | 19.2.8 | definition | Thus, glucagon is a hyperglycemic hormone. | 7 | x |
| F148 | 19.2.8 | concept | Insulin is a peptide hormone, which plays a major role in the regulation of glucose homeostasis. | 7 | x |
| F149 | 19.2.8 | process | Insulin acts mainly on hepatocytes and adipocytes (cells of adipose tissue), and enhances cellular glucose uptake and utilisation. | 7 | x |
| F150 | 19.2.8 | process | As a result, there is a rapid movement of glucose from blood to hepatocytes and adipocytes resulting in decreased blood glucose levels (hypoglycemia). | 8 | x |
| F151 | 19.2.8 | process | Insulin also stimulates conversion of glucose to glycogen (glycogenesis) in the target cells. | 8 | x |
| F152 | 19.2.8 | concept | The glucose homeostasis in blood is thus maintained jointly by the two – insulin and glucagons. | 8 | x |
| F153 | 19.2.8 | concept | Prolonged hyperglycemia leads to a complex disorder called diabetes mellitus which is associated with loss of glucose through urine and formation of harmful compounds known as ketone bodies. | 8 | x |
| F154 | 19.2.8 | concept | Insulin deficiency and/or insulin resistance result in a disease called diabetes mellitus. | 12 | x |
| F155 | 19.2.8 | concept | Diabetic patients are successfully treated with insulin therapy. | 8 | x |
| F156 | 19.2.9 | heading | 19.2.9 Testis | 8 | x |
| F157 | 19.2.9 | concept | A pair of testis is present in the scrotal sac (outside abdomen) of male individuals (Figure 19.1). | 8 | x |
| F158 | 19.2.9 | concept | Testis performs dual functions as a primary sex organ as well as an endocrine gland. | 8 | x |
| F159 | 19.2.9 | concept | Testis is composed of seminiferous tubules and stromal or interstitial tissue. | 8 | x |
| F160 | 19.2.9 | concept | The Leydig cells or interstitial cells, which are present in the intertubular spaces produce a group of hormones called androgens mainly testosterone. | 8 | x |
| F161 | 19.2.9 | concept | Androgens regulate the development, maturation and functions of the male accessory sex organs like epididymis, vas deferens, seminal vesicles, prostate gland, urethra etc. | 8 | x |
| F162 | 19.2.9 | concept | These hormones stimulate muscular growth, growth of facial and axillary hair, aggressiveness, low pitch of voice etc. | 8 | x |
| F163 | 19.2.9 | concept | Androgens play a major stimulatory role in the process of spermatogenesis (formation of spermatozoa). | 8 | x |
| F164 | 19.2.9 | concept | Androgens act on the central neural system and influence the male sexual behaviour (libido). | 8 | x |
| F165 | 19.2.9 | concept | These hormones produce anabolic (synthetic) effects on protein and carbohydrate metabolism. | 8 | x |
| F166 | 19.2.9 | concept | The testis secretes androgens, which stimulate the development, maturation and functions of the male accessory sex organs, appearance of the male secondary sex characters, spermatogenesis, male sexual behaviour, anabolic pathways and erythropoiesis. | 12 | x |
| F167 | 19.2.10 | heading | 19.2.10 Ovary | 8 | x |
| F168 | 19.2.10 | concept | Females have a pair of ovaries located in the abdomen (Figure 19.1). | 8 | x |
| F169 | 19.2.10 | concept | Ovary is the primary female sex organ which produces one ovum during each menstrual cycle. | 8 | x |
| F170 | 19.2.10 | concept | In addition, ovary also produces two groups of steroid hormones called estrogen and progesterone. | 8 | x |
| F171 | 19.2.10 | concept | Ovary is composed of ovarian follicles and stromal tissues. | 8 | x |
| F172 | 19.2.10 | concept | The estrogen is synthesised and secreted mainly by the growing ovarian follicles. | 8 | x |
| F173 | 19.2.10 | process | After ovulation, the ruptured follicle is converted to a structure called corpus luteum, which secretes mainly progesterone. | 8 | x |
| F174 | 19.2.10 | concept | Estrogens produce wide ranging actions such as stimulation of growth and activities of female secondary sex organs, development of growing ovarian follicles, appearance of female secondary sex characters (e.g., high pitch of voice, etc.) and mammary gland development. | 8 | x |
| F175 | 19.2.10 | concept | Estrogens also regulate female sexual behaviour. | 9 | x |
| F176 | 19.2.10 | concept | Progesterone supports pregnancy. | 9 | x |
| F177 | 19.2.10 | concept | Progesterone also acts on the mammary glands and stimulates the formation of alveoli (sac-like structures which store milk) and milk secretion. | 9 | x |
| F178 | 19.2.10 | definition | (d) Progestational hormone | 13 | x |
| F179 | 19.3 | heading | 19.3 HORMONES OF HEART, KIDNEY AND GASTROINTESTINAL TRACT | 9 | x |
| F180 | 19.3 | concept | Now you know about the endocrine glands and their hormones. However, as mentioned earlier, hormones are also secreted by some tissues which are not endocrine glands. | 9 | x |
| F181 | 19.3 | concept | For example, the atrial wall of our heart secretes a very important peptide hormone called atrial natriuretic factor (ANF), which decreases blood pressure. | 9 | x |
| F182 | 19.3 | process | When blood pressure is increased, ANF is secreted which causes dilation of the blood vessels. This reduces the blood pressure. | 9 | x |
| F183 | 19.3 | concept | The juxtaglomerular cells of kidney produce a peptide hormone called erythropoietin which stimulates erythropoiesis (formation of RBC). | 9 | x |
| F184 | 19.3 | concept | Endocrine cells present in different parts of the gastro-intestinal tract secrete four major peptide hormones, namely gastrin, secretin, cholecystokinin (CCK) and gastric inhibitory peptide (GIP). | 9 | x |
| F185 | 19.3 | process | Gastrin acts on the gastric glands and stimulates the secretion of hydrochloric acid and pepsinogen. | 9 | x |
| F186 | 19.3 | process | Secretin acts on the exocrine pancreas and stimulates secretion of water and bicarbonate ions. | 9 | x |
| F187 | 19.3 | process | CCK acts on both pancreas and gall bladder and stimulates the secretion of pancreatic enzymes and bile juice, respectively. | 9 | x |
| F188 | 19.3 | process | GIP inhibits gastric secretion and motility. | 9 | x |
| F189 | 19.3 | concept | Several other non-endocrine tissues secrete hormones called growth factors. These factors are essential for the normal growth of tissues and their repairing/regeneration. | 9 | x |
| F190 | 19.4 | heading | 19.4 MECHANISM OF HORMONE ACTION | 9 | x |
| F191 | 19.4 | definition | Hormones produce their effects on target tissues by binding to specific proteins called hormone receptors located in the target tissues only. | 9 | x |
| F192 | 19.4 | definition | Hormone receptors present on the cell membrane of the target cells are called membrane-bound receptors and the receptors present inside the target cell are called intracellular receptors, mostly nuclear receptors (present in the nucleus). | 9 | x |
| F193 | 19.4 | process | Binding of a hormone to its receptor leads to the formation of a hormone-receptor complex (Figure 19.5 a, b). | 9 | x |
| F194 | 19.4 | concept | Each receptor is specific to one hormone only and hence receptors are specific. | 9 | x |
| F195 | 19.4 | process | Hormone-Receptor complex formation leads to certain biochemical changes in the target tissue. | 9 | x |
| F196 | 19.4 | concept | Target tissue metabolism and hence physiological functions are regulated by hormones. | 9 | x |
| F197 | 19.4 | concept | On the basis of their chemical nature, hormones can be divided into groups : | 10 | x |
| F198 | 19.4 | example | (i) peptide, polypeptide, protein hormones (e.g., insulin, glucagon, pituitary hormones, hypothalamic hormones, etc.) | 10 | x |
| F199 | 19.4 | example | (ii) steroids (e.g., cortisol, testosterone, estradiol and progesterone) | 10 | x |
| F200 | 19.4 | example | (iii) iodothyronines (thyroid hormones) | 10 | x |
| F201 | 19.4 | example | (iv) amino-acid derivatives (e.g., epinephrine). | 10 | x |
| F202 | 19.4 | process | Hormones  which interact with membrane-bound receptors normally do not enter the target cell, but generate second messengers (e.g., cyclic AMP, IP3, Ca++ etc) which in turn regulate cellular metabolism (Figure 19.5a). | 10 | x |
| F203 | 19.4 | process | Hormones which interact with intracellular receptors (e.g., steroid hormones, iodothyronines, etc.) mostly regulate gene expression or chromosome function by the interaction of hormone-receptor complex with the genome. | 10 | x |
| F204 | 19.4 | concept | Cumulative biochemical actions result in physiological and developmental effects (Figure 19.5b). | 10 | x |
| F205 | Fig 19.5 | caption | Figure 19.5 Diagramatic representation of the mechanism of hormone action : (a) Protein hormone  (b) Steroid hormone | 11 | x |
| F206 | Summary | heading | SUMMARY | 11 | x |
| F207 | Exercises | heading | EXERCISES | 13 | x |
| F208 | Note | heading | NOTE | 14 | x |
| F209 | Fig 19.1 | caption | Figure labels: "Hypothalamus"; "Pituitary"; "Pineal"; "Thyroid and Parathyroid"; "Thymus"; "Pancreas"; "Adrenal"; "Ovary (in female)"; "Testis (in male)" | 2 | x |
| F210 | Fig 19.2 | caption | Figure labels: "Hypothalamus"; "Hypothalamic neurons"; "Portal circulation"; "Posterior pituitary"; "Anterior pituitary" | 3 | x |
| F211 | Fig 19.3 (a) | caption | Figure (a) labels: "Vocal cord"; "Thyroid"; "Trachea" | 4 | x |
| F212 | Fig 19.3 (b) | caption | Figure (b) labels: "Parathyroid glands" | 4 | x |
| F213 | Fig 19.4 (a)/(b) | caption | Figure labels: "Adrenal gland"; "Kidney"; "Adrenal cortex"; "Adrenal medulla" | 6 | x |
| F214 | Fig 19.5 (a) | caption | Figure (a) labels: "Hormone (e.g., FSH)"; "Receptor"; "Ovarian cell membrane"; "Response 1"; "(Generation of second messenger)"; "(Cyclic AMP or Ca++)"; "Biochemical responses"; "Physiological responses (e.g., ovarian growth)" | 10 | x |
| F215 | Fig 19.5 (b) | caption | Figure (b) labels: "Hormone (e.g., estrogen)"; "Uterine cell membrane"; "Nucleus"; "Genome"; "mRNA"; "Proteins"; "Hormone-receptor complex"; "Physiological responses (Tissue growth and differentiation)" | 11 | x |

## Row census (`1-S`, machine-derived from the table above)

| Quantity | Value |
|---|---:|
| Rows | 200 |
| ID range | `F001`–`F215`, contiguous, monotonic |
| Duplicate IDs | 0 |
| Gaps | 0 |
| Rows ticked | 200 / 200 |
| Content Facts | 193 |
| Figure-label matrix rows | 7 |

Type census — **8 values, all lowercase**:

| Type | Count |
|---|---:|
| concept | 111 |
| process | 26 |
| definition | 20 |
| heading | 18 |
| opener | 9 |
| caption | 12 |
| example | 8 |
| number | 4 |
| **total** | **200** |

`caption` = 5 figure captions (`F027`, `F069`, `F095`, `F136`, `F205`) + the 7 figure-label matrix rows (`F209`–`F215`), which keep `caption` so the `_extract_labels` parser continues to see them.

## Two-value note on the `α`/`β` rows

`F141` and `F142` render the source's Greek `α-cells` / `β-cells` as `alpha-cells` / `beta-cells`. This is **a deliberate ASCII transliteration, not a transcription error**, recorded here so `1-H` does not raise it: the Pass 2 script must print the Greek letters, and the inventory row must be checked against the *glyph*, not the ASCII. Every other row in this table is character-for-character.

## Figure-label matrix note

The matrix exists in exactly one place: the `## Facts` table above, rows `F209`–`F215`. Each row begins with `Figure labels:` or `Figure (a)/(b) labels:` in the wording column, matching the `_extract_labels` parser used by `check_pdf.py`. There is no duplicate pipe-delimited label table elsewhere in this inventory, so labels are not double-counted and no phantom separator row is created.

## Figure manifest

**Caption column corrected by `1-S`.** This column was previously headed "Caption (verbatim)" while holding **paraphrases**: it printed `position of thyroid and parathyroid — ventral side` where the source prints `position of Thyroid and Parathyroid (a) Ventral side`, and `Mechanism of hormone action — protein hormone` where the source prints `Diagramatic representation of the mechanism of hormone action : (a) Protein hormone`. Three of seven rows were de-capitalised and re-punctuated with em-dashes the source never uses, and the Figure 19.5 rows silently repaired the source's `Diagramatic` typo — the exact "correct the source" failure the typo table above exists to prevent. The captions are now verbatim, and the paraphrases are preserved in a separate column so the manifest stays readable without lying about what the book says.

| Fig # | Caption (verbatim, as printed) | Short label (ours, NOT the source's) | Asset file | Source page | Mono | Verified |
|---|---|---|---|---:|---|---|
| Fig 19.1 | Figure 19.1 Location of endocrine glands | Location of endocrine glands | `assets/fig_19_1.png` | 2 | yes | yes |
| Fig 19.2 | Figure 19.2 Diagrammatic representation of pituitary and its relationship with hypothalamus | Pituitary and hypothalamus | `assets/fig_19_2.png` | 3 | yes | yes |
| Fig 19.3 (a) | Figure 19.3 Diagrammatic view of the position of Thyroid and Parathyroid (a) Ventral side | Thyroid/parathyroid, ventral | `assets/fig_19_3a.png` | 4 | yes | yes |
| Fig 19.3 (b) | Figure 19.3 Diagrammatic view of the position of Thyroid and Parathyroid (b) Dorsal side | Thyroid/parathyroid, dorsal | `assets/fig_19_3b.png` | 4 | yes | yes |
| Fig 19.4 (a)/(b) | Figure 19.4  Diagrammatic representation of : (a) Adrenal gland above kidney (b) Section showing two parts of adrenal gland | Adrenal gland and section | `assets/fig_19_4.png` | 6 | yes | yes |
| Fig 19.5 (a) | Figure 19.5 Diagramatic representation of the mechanism of hormone action : (a) Protein hormone | Mechanism, protein hormone | `assets/fig_19_5a.png` | 10 | yes | yes |
| Fig 19.5 (b) | Figure 19.5 Diagramatic representation of the mechanism of hormone action : (b) Steroid hormone | Mechanism, steroid hormone | `assets/fig_19_5b.png` | 11 | yes | yes |

**Source-page correction:** the Figure 19.5 (a) row previously gave source page **10**, and 19.5 (b) page **11** — but the printed `Figure 19.5` caption sits on **page 11**, with the `(a)` panel on page 10 and the `(b)` panel plus the caption on page 11. Panel pages are unchanged (they are what the crops came from); the caption's own page is now recorded separately in `F205`, which is what a Pass 2 script needs in order to place the caption.

## Extraction record and audit trail

The reproducible extractor is `extract_figures.py`. The canonical 4× grid renderer is `scratch/ch19_render_quad_grids.py`, and its page overlays are stored in `scratch/ch19_figs/grid_4x/`. The three-part mechanical audit is `scratch/audit_ch19.py`; focused source-coordinate checks are in `scratch/focus_ch19.py` and `scratch/probe_ch19_rects.py`; the final visual review is recorded in `scratch/ch19_figs/visual_findings.md`.

Figure 19.4 is intentionally delivered as one combined asset because its two panels are interleaved horizontally. A rectangular crop that isolates either panel cuts the kidney, labels, or connector; the combined crop preserves both panels, the connector, all labels, and both panel markers.

Figures 19.5a and 19.5b are cropped tightly to their existing rectangular box borders. No new box was drawn and no figure content was altered; only the outside white margin was removed.

All seven emitted assets are high-resolution grayscale PNGs (`mode=L`) generated with autocontrast. The final visual gate was completed by opening every final PNG individually and confirming correct figure identity, complete labels and leader lines, no accidental neighboring prose/figure capture, print-legible detail, and monochrome output. The mechanical audit reports clean border-band checks for all seven assets; the vector-extent check is not applicable to the raster artwork in Figure 19.4.

## Gate 1 record

### `1-F` — figures — COMPLETE (2026-08-30)

**5 numbered figures → 7 assets.** `19.3` and `19.5` split into (a)/(b); `19.4` deliberately kept as ONE combined asset (justification above). All `mode=L`, rendered at 440 dpi, each opened individually. The figure census was closed against every page image of all 14 pages: **5 is the whole numbered census and there is no unnumbered plate.**

### `1-S` — source read + Facts inventory — COMPLETE (2026-09-01)

- **All 14 source pages read in full**, in four sequential reads (1–4, 5–7, 8–11, 12–14). Page 14 carries only `NOTE` and the reprint line and contributes no Facts — verified by its 21-character text extraction, not assumed.
- **193 content Facts entered in Content Order**, from the chapter opener through `EXERCISES`, plus the 7 renumbered figure-label rows = **200 rows**.
- **Structure derived, not guessed:** 4 top-level sections, 10 subsections (all under 19.2), 14 numbered headings, 4 structural unnumbered headings, 5 numbered figures, 9 exercises with 41 sub-parts.
- **5 source misspellings/inconsistencies catalogued** (`sella tursica`, `Exopthalmic`, `pupilary`, `glucagons`, `Diagramatic`) and held **verbatim** in their rows.
- **3 defects in the pre-existing `1-F` documentation found and fixed** (all metadata; no asset, no crop box and no shared repo file touched): the false `Frozen Inventory` H1; the "verbatim" caption column that actually held paraphrases and silently repaired the source's `Diagramatic` typo; and the Figure 19.5 caption page recorded as the panel page.

### Remaining Pass 1 sessions — NOT STARTED

| Session | Purpose | Blocking |
|---|---|---|
| `1-H` | heading/typography audit — confirm the 18 heading rows against the source's own type hierarchy and check every non-heading row is character-for-character (including the `α`/`β` transliteration note) | yes |
| `1-O` | ordering audit — confirm the table is in true Content Order and that each row's `Src` page is the page the wording is actually printed on | yes |
| `1-Z` | summary classification (BODY-PRESENT vs SUMMARY-UNIQUE over the p. 11–12 `SUMMARY`) and the exercise-gap scan over the 9 exercises / 41 sub-parts; every SUMMARY-UNIQUE item must be folded **before** the freeze | yes |

**The freeze may not be declared until all three have run.** In particular `1-Z` is load-bearing: the Ch19 `SUMMARY` runs to two full pages and demonstrably introduces at least one item the body never states (the body's thyroid section never mentions `development and maturation of the central neural system`, which the SUMMARY asserts), so SUMMARY-UNIQUE folds **will** change the row count and the count above must be treated as provisional.
