# Frozen Inventory — Class 11 Biology, Chapter 19: Chemical Coordination and Integration

Source: `Chapter/class 11/Chapter 19 - Chemical Coordination and Integration.pdf` (14 pages; supplied high-quality source `kebo119.pdf`) | Frozen: 2026-09-01 | Pass 1 sessions complete: **all five — `1-F` (2026-08-30) · `1-S` (2026-09-01) · `1-H` (2026-09-01) · `1-O` (2026-09-01) · `1-Z` (2026-09-01)** | Rows: **218** (`F001`–`F211` content Facts + `F212`–`F218` figure-label matrix rows)

> **Gate state: ALL GATES CLOSED — GATE 1, GATE 2, GATE 3(a) AND GATE 3(b) ARE GREEN (Gate 1 2026-09-01, Gate 2 2026-09-01, Gate 3(a) 2026-09-01, Gate 3(b) 2026-09-01; real `check_pdf.py` re-run 2026-09-02 confirmed exit 0 — VERDICT PASS, 0 fail / 0 warn).** All five Pass 1 sessions have run, each reporting its own machine-derived row count; every count below was derived by re-parsing the finished `## Facts` table, not by hand tally. The inventory is **frozen** and 218/218 rows are ticked against the delivered script. **No row may be added, removed or reworded** — a Pass 3 discovery that this file was incomplete would reopen Gate 1, not get patched silently; none was found. The Gate 2 evidence is in `## Gate 2 record`, the layout review in `## Gate 3(a) record`, and the bidirectional full read in `## Gate 3(b) record — CLOSED`, all at the foot of this file.

Tick legend: `x` = the row's wording was read directly off the numbered source page named in its `Src` column and confirmed character-for-character, including the source's own typography and its own misspellings. A tick is **not** a claim that a human has verified the row inside the delivered PDF — that claim belongs to Gate 3 and has not been made. It does now mean the row was written into the Pass 2 script, which is what `check_pdf.py` check 7 gates on.

## Header-correction record (`1-S`, 2026-09-01)

This file's H1 previously read **"Frozen Inventory"** while the file contained **only the 7 figure-label rows** and no Facts at all. A 7-row figure manifest is not a frozen Pass 1 inventory, so the H1 asserted a gate that had never been earned — exactly the "documentation claims more than the artefact" defect that Gate 3(b) rule 2 says *is* the finding. `1-S` demoted the H1 to **Working Inventory (Pass 1 IN PROGRESS — NOT FROZEN)** and stated the gate state explicitly. The `1-F` figure work itself was sound and is untouched; only the claim about it was wrong.

**The H1 reads `Frozen Inventory` again as of 2026-09-01, and this time it is earned** — `1-H`, `1-O` and `1-Z` have since run, the freeze is declared in the Gate 1 record at the foot of this file, and every count is a re-parse. This paragraph is kept rather than deleted so the word `Frozen` in the H1 has a traceable history: it was false when written, was removed, and was restored only after the five sessions it asserts actually closed. **Do not read this paragraph as the current gate state** — line 5 is the current gate state.

The original 7 figure-label rows were numbered `F001`–`F007`. Because the `## Facts` table must be in **Content Order**, and the figure-label matrix belongs at the tail (the Ch18 convention: 131 content Facts then 4 matrix rows), those 7 rows are **renumbered `F212`–`F218`**. Their `Section`, `Type` and wording columns are **byte-identical to the originals** — only the ID changed — so `check_pdf._extract_labels` sees the same 7 rows and the same label harvest it saw before.

**The label count in this paragraph was wrong and is corrected here (`1-Z`).** It read **35 labels**, a number no parse of these rows returns: importing `_extract_labels` from `check_pdf.py` and running it over this file returns **38 labels across 7 figure rows** (`19.1` 9 · `19.2` 5 · `19.3a` 3 · `19.3b` 1 · `19.4` 4 · `19.5a` 8 · `19.5b` 8 = 38), with no doubling and no phantom `Fig #` row. The 35 was the *only* live restatement of the figure-label count in this file, which is why it survived two sessions: nothing contradicted it. Pass 2's check 6 will demand **38** labels in the running text, so a script written against 35 would have gone to Gate 2 three labels short.

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
| Structural unnumbered headings | 5 | chapter title, `CHAPTER 19`, `SUMMARY`, `EXERCISES`, `NOTE` |
| Numbered figures | 5 | 19.1, 19.2, 19.3, 19.4, 19.5 |
| Delivered figure assets | 7 | 19.3 and 19.5 split (a)/(b); **19.4 deliberately ONE combined asset** |
| Exercise questions | 9 | numbered 1–9 on p. 13 |
| Exercise lettered sub-parts | 39 | `3+0+12+5+6+6+3+0+4`, per question, Q1…Q9 |
| Q9 Column II matching options | 4 | `(i)`–`(iv)`; the answer set, **not** sub-parts |
| Exercise labelled items total | 43 | 39 + 4 |
| SUMMARY sentences | 32 | p. 11 (after the `SUMMARY` heading) + p. 12 |

**Two corrections `1-H`/`1-Z` made to this table.** The unnumbered-heading count was **4**, omitting the trailing `NOTE` page even though the row for it exists (`F211`) — the census contradicted its own table. The sub-part count was a single unexplained **41**, which is neither of the two defensible readings; the machine count is 39 lettered items, or 43 counting Q9's Column II. Both readings are now stated with the per-question addition beside them, so the total is derivable from the list rather than asserted next to it. Derivation: `scratch/ch19_gate1/exercise_census.py`.

**The `(s)` trap, recorded because it produced a wrong number once.** A naive `\(([a-z])\)` scan of p. 13 returns **40**, because Q6's stem reads `Give example(s) of:` and the inflectional `(s)` is counted as a label. A sub-part label always sits at start-of-line or after whitespace; inflection is always glued to the preceding word. That one anchor condition is the whole difference between 40 and the true 39.

**The `19.2` subsection run is the whole anatomical spine of the chapter** — ten glands in fixed order: hypothalamus, pituitary, pineal, thyroid, parathyroid, thymus, adrenal, pancreas, testis, ovary. Sections 19.3 and 19.4 then break that frame deliberately: 19.3 covers hormone sources that are *not* endocrine glands (heart, kidney, GI tract) and 19.4 is mechanism rather than anatomy.

## Source typography and misspellings — transcribed verbatim, NOT corrected

Recorded here so a later pass cannot "helpfully" fix them and so `verify_inventory.py` can assert both that the row preserves the source form and that the source really prints it.

| Source form | Standard form | Where | Row |
|---|---|---|---|
| `sella tursica` | sella turcica | p. 3, pituitary location | `F039` |
| `Exopthalmic goitre` | Exophthalmic goitre | p. 5, hyperthyroidism | `F087` |
| `pupilary dilation` | pupillary dilation | p. 6, catecholamine effects | `F120` |
| `glucagons` (plural) | glucagon | p. 8, glucose homeostasis | `F153` |
| `Diagramatic` | Diagrammatic | p. 11, Figure 19.5 caption | `F208` |

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
| F008 | Contents | contents | 19.1 Endocrine Glands and Hormones | 1 | x |
| F009 | Contents | contents | 19.2 Human Endocrine System | 1 | x |
| F010 | Contents | contents | 19.3 Hormones of Heart, Kidney and Gastrointestinal Tract | 1 | x |
| F011 | Contents | contents | 19.4 Mechanism of Hormone Action | 1 | x |
| F012 | 19.1 | heading | 19.1 ENDOCRINE GLANDS AND HORMONES | 1 | x |
| F013 | 19.1 | opener | Endocrine glands lack ducts and are hence, called ductless glands. | 1 | x |
| F014 | 19.1 | definition | Their secretions are called hormones. | 1 | x |
| F015 | 19.1 | concept | The classical definition of hormone as a chemical produced by endocrine glands and released into the blood and transported to a distantly located target organ has current scientific definition as follows | 1 | x |
| F016 | 19.1 | definition | Hormones are non-nutrient chemicals which act as intercellular messengers and are produced in trace amounts. | 1 | x |
| F017 | 19.1 | concept | The new definition covers a number of new molecules in addition to the hormones secreted by the organised endocrine glands. | 1 | x |
| F018 | 19.1 | concept | Invertebrates possess very simple endocrine systems with few hormones whereas a large number of chemicals act as hormones and provide coordination in the vertebrates. | 1 | x |
| F019 | 19.1 | concept | The human endocrine system is described here. | 1 | x |
| F020 | 19.1 | concept | These hormones regulate metabolism, growth and development of our organs, the endocrine glands or certain cells. | 11 | x |
| F021 | 19.2 | heading | 19.2   HUMAN ENDOCRINE SYSTEM | 2 | x |
| F022 | 19.2 | opener | The endocrine glands and hormone producing diffused tissues/cells located in different parts of our body constitute the endocrine system. | 2 | x |
| F023 | 19.2 | concept | Pituitary, pineal, thyroid, adrenal, pancreas, parathyroid, thymus and gonads (testis in males and ovary in females) are the organised endocrine bodies in our body (Figure 19.1). | 2 | x |
| F024 | 19.2 | concept | The endocrine system is composed of hypothalamus, pituitary and pineal, thyroid, adrenal, pancreas, parathyroid, thymus and gonads (testis and ovary). | 11 | x |
| F025 | 19.2 | concept | In addition to these, some other organs, e.g., gastrointestinal tract, liver, kidney, heart also produce hormones. | 2 | x |
| F026 | 19.2 | concept | A brief account of the structure and functions of all major endocrine glands and hypothalamus of the human body is given in the following sections. | 2 | x |
| F027 | Fig 19.1 | caption | Figure 19.1 Location of endocrine glands | 2 | x |
| F028 | 19.2.1 | heading | 19.2.1 The Hypothalamus | 2 | x |
| F029 | 19.2.1 | opener | As you know, the hypothalamus is the basal part of diencephalon, forebrain (Figure 19.1) and it regulates a wide spectrum of body functions. | 2 | x |
| F030 | 19.2.1 | definition | It contains several groups of neurosecretory cells called nuclei which produce hormones. | 2 | x |
| F031 | 19.2.1 | concept | These hormones regulate the synthesis and secretion of pituitary hormones. | 2 | x |
| F032 | 19.2.1 | definition | However, the hormones produced by hypothalamus are of two types, the releasing hormones (which stimulate secretion of pituitary hormones) and the inhibiting hormones (which inhibit secretions of pituitary hormones). | 2 | x |
| F033 | 19.2.1 | example | For example a hypothalamic hormone called Gonadotrophin releasing hormone (GnRH) stimulates the pituitary synthesis and release of gonadotrophins. | 2 | x |
| F034 | 19.2.1 | example | On the other hand, somatostatin from the hypothalamus inhibits the release of growth hormone from the pituitary. | 2 | x |
| F035 | 19.2.1 | process | These hormones originating in the hypothalamic neurons, pass through axons and are released from their nerve endings. | 2 | x |
| F036 | 19.2.1 | process | These hormones reach the pituitary gland through a portal circulatory system and regulate the functions of the anterior pituitary. | 2 | x |
| F037 | 19.2.1 | concept | The posterior pituitary is under the direct neural regulation of the hypothalamus (Figure 19.2). | 2 | x |
| F038 | 19.2.2 | heading | 19.2.2 The Pituitary Gland | 3 | x |
| F039 | 19.2.2 | opener | The pituitary gland is located in a bony cavity called sella tursica and is attached to hypothalamus by a stalk (Figure 19.2). | 3 | x |
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
| F068 | 19.2.2 | concept | The pituitary hormones regulate the growth and development of somatic tissues and activities of peripheral endocrine glands. | 12 | x |
| F069 | Fig 19.2 | caption | Figure 19.2 Diagrammatic representation of pituitary and its relationship with hypothalamus | 3 | x |
| F070 | 19.2.3 | heading | 19.2.3 The Pineal Gland | 4 | x |
| F071 | 19.2.3 | opener | The pineal gland is located on the dorsal side of forebrain. | 4 | x |
| F072 | 19.2.3 | concept | Pineal secretes a hormone called melatonin. | 4 | x |
| F073 | 19.2.3 | number | Melatonin plays a very important role in the regulation of a 24-hour (diurnal) rhythm of our body. | 4 | x |
| F074 | 19.2.3 | example | For example, it helps in maintaining the normal rhythms of sleep-wake cycle, body temperature. | 4 | x |
| F075 | 19.2.3 | concept | In addition, melatonin also influences metabolism, pigmentation, the menstrual cycle as well as our defense capability. | 4 | x |
| F076 | 19.2.4 | heading | 19.2.4 Thyroid Gland | 4 | x |
| F077 | 19.2.4 | opener | The thyroid gland is composed of two lobes which are located on either side of the trachea (Figure 19.3 a). | 4 | x |
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
| F097 | 19.2.5 | opener | In humans, four parathyroid glands are present on the back side of the thyroid gland, one pair each in the two lobes of the thyroid gland (Figure 19.3 b). | 5 | x |
| F098 | 19.2.5 | concept | The parathyroid glands secrete a peptide hormone called parathyroid hormone (PTH). | 5 | x |
| F099 | 19.2.5 | concept | The secretion of PTH is regulated by the circulating levels of calcium ions. | 5 | x |
| F100 | 19.2.5 | concept | Parathyroid hormone (PTH) increases the Ca2+ levels in the blood. | 5 | x |
| F101 | 19.2.5 | process | PTH acts on bones and stimulates the process of bone resorption (dissolution/demineralisation). | 5 | x |
| F102 | 19.2.5 | process | PTH also stimulates reabsorption of Ca2+ by the renal tubules and increases Ca2+ absorption from the digested food. | 5 | x |
| F103 | 19.2.5 | definition | It is, thus, clear that PTH is a hypercalcemic hormone, i.e., it increases the blood Ca2+ levels. | 5 | x |
| F104 | 19.2.5 | concept | Along with TCT, it plays a significant role in calcium balance in the body. | 5 | x |
| F105 | 19.2.6 | heading | 19.2.6 Thymus | 5 | x |
| F106 | 19.2.6 | opener | The thymus gland is a lobular structure located between lungs behind sternum on the ventral side of aorta. | 5 | x |
| F107 | 19.2.6 | concept | The thymus plays a major role in the development of the immune system. | 5 | x |
| F108 | 19.2.6 | concept | This gland secretes the peptide hormones called thymosins. | 5 | x |
| F109 | 19.2.6 | concept | Thymosins play a major role in the differentiation of T-lymphocytes, which provide cell-mediated immunity. | 5 | x |
| F110 | 19.2.6 | concept | In addition, thymosins also promote production of antibodies to provide humoral immunity. | 5 | x |
| F111 | 19.2.6 | concept | Thymus is degenerated in old individuals resulting in a decreased production of thymosins. | 5 | x |
| F112 | 19.2.6 | concept | As a result, the immune responses of old persons become weak. | 5 | x |
| F113 | 19.2.7 | heading | 19.2.7 Adrenal Gland | 6 | x |
| F114 | 19.2.7 | opener | Our body has one pair of adrenal glands, one above of each kidney (Figure 19.4 a). | 6 | x |
| F115 | 19.2.7 | concept | The gland is composed of two types of tissues. | 6 | x |
| F116 | 19.2.7 | concept | The centrally located tissue is called the adrenal medulla, and outside this lies the adrenal cortex (Figure 19.4 b). | 6 | x |
| F117 | 19.2.7 | concept | Underproduction of hormones by the adrenal cortex alters carbohydrate metabolism causing acute weakness and fatigue leading to a disease called Addison’s disease. | 6 | x |
| F118 | 19.2.7 | concept | The adrenal medulla secretes two hormones called adrenaline or epinephrine and noradrenaline or norepinephrine. | 6 | x |
| F119 | 19.2.7 | definition | These are commonly called as catecholamines. | 6 | x |
| F120 | 19.2.7 | concept | Adrenaline and noradrenaline are rapidly secreted in response to stress of any kind and during emergency situations and are called emergency hormones or hormones of Fight or Flight. | 6 | x |
| F121 | 19.2.7 | concept | These hormones increase alertness, pupilary dilation, piloerection (raising of hairs), sweating etc. | 6 | x |
| F122 | 19.2.7 | concept | Both the hormones increase the heart beat, the strength of heart contraction and the rate of respiration. | 6 | x |
| F123 | 19.2.7 | process | Catecholamines also stimulate the breakdown of glycogen resulting in an increased concentration of glucose in blood. | 6 | x |
| F124 | 19.2.7 | process | In addition, they also stimulate the breakdown of lipids and proteins. | 7 | x |
| F125 | 19.2.7 | process | These hormones increase alertness, pupilary dilation, piloerection, sweating, heart beat, strength of heart contraction, rate of respiration, glycogenolysis, lipolysis, proteolysis. | 12 | x |
| F126 | 19.2.7 | concept | The adrenal cortex can be divided into three layers, called zona reticularis (inner layer), zona fasciculata (middle layer) and zona glomerulosa (outer layer). | 7 | x |
| F127 | 19.2.7 | definition | The adrenal cortex secretes many hormones, commonly called as corticoids. | 7 | x |
| F128 | 19.2.7 | definition | The corticoids, which are involved in carbohydrate metabolism are called glucocorticoids. In our body, cortisol is the main glucocorticoid. | 7 | x |
| F129 | 19.2.7 | definition | Corticoids, which regulate the balance of water and electrolytes in our body are called mineralocorticoids. Aldosterone is the main mineralocorticoid in our body. | 7 | x |
| F130 | 19.2.7 | process | Glucocorticoids stimulate gluconeogenesis, lipolysis and proteolysis; and inhibit cellular uptake and utilisation of amino acids. | 7 | x |
| F131 | 19.2.7 | concept | Cortisol is also involved in maintaining the cardio-vascular system as well as the kidney functions. | 7 | x |
| F132 | 19.2.7 | concept | Glucocorticoids, particularly cortisol, produces anti-inflammatory reactions and suppresses the immune response. | 7 | x |
| F133 | 19.2.7 | concept | Cortisol stimulates the RBC production. | 7 | x |
| F134 | 19.2.7 | process | Glucocorticoids stimulate gluconeogenesis, lipolysis, proteolysis, erythropoiesis, cardio-vascular system, blood pressure, and glomerular filtration rate and inhibit inflammatory reactions by suppressing the immune response. | 12 | x |
| F135 | 19.2.7 | process | Aldosterone acts mainly at the renal tubules and stimulates the reabsorption of Na+ and water and excretion of K+ and phosphate ions. | 7 | x |
| F136 | 19.2.7 | concept | Thus, aldosterone helps in the maintenance of electrolytes, body fluid volume, osmotic pressure and blood pressure. Small amounts of androgenic steroids are also secreted by the adrenal cortex which play a role in the growth of axial hair, pubic hair and facial hair during puberty. | 7 | x |
| F137 | Fig 19.4 | caption | Figure 19.4  Diagrammatic representation of : (a) Adrenal gland above kidney (b) Section showing two parts of adrenal gland | 6 | x |
| F138 | 19.2.8 | heading | 19.2.8 Pancreas | 7 | x |
| F139 | 19.2.8 | opener | Pancreas is a composite gland (Figure 19.1) which acts as both exocrine and endocrine gland. | 7 | x |
| F140 | 19.2.8 | definition | The endocrine pancreas consists of ‘Islets of Langerhans’. | 7 | x |
| F141 | 19.2.8 | number | There are about 1 to 2 million Islets of Langerhans in a normal human pancreas representing only 1 to 2 per cent of the pancreatic tissue. | 7 | x |
| F142 | 19.2.8 | concept | The two main types of cells in the Islet of Langerhans are called α-cells and β-cells. | 7 | x |
| F143 | 19.2.8 | concept | The α-cells secrete a hormone called glucagon, while the β-cells secrete insulin. | 7 | x |
| F144 | 19.2.8 | concept | Glucagon is a peptide hormone, and plays an important role in maintaining the normal blood glucose levels. | 7 | x |
| F145 | 19.2.8 | process | Glucagon acts mainly on the liver cells (hepatocytes) and stimulates glycogenolysis resulting in an increased blood sugar (hyperglycemia). | 7 | x |
| F146 | 19.2.8 | process | In addition, this hormone stimulates the process of gluconeogenesis which also contributes to hyperglycemia. | 7 | x |
| F147 | 19.2.8 | concept | Glucagon reduces the cellular glucose uptake and utilisation. | 7 | x |
| F148 | 19.2.8 | definition | Thus, glucagon is a hyperglycemic hormone. | 7 | x |
| F149 | 19.2.8 | concept | Insulin is a peptide hormone, which plays a major role in the regulation of glucose homeostasis. | 7 | x |
| F150 | 19.2.8 | process | Insulin acts mainly on hepatocytes and adipocytes (cells of adipose tissue), and enhances cellular glucose uptake and utilisation. | 7 | x |
| F151 | 19.2.8 | process | As a result, there is a rapid movement of glucose from blood to hepatocytes and adipocytes resulting in decreased blood glucose levels (hypoglycemia). | 8 | x |
| F152 | 19.2.8 | process | Insulin also stimulates conversion of glucose to glycogen (glycogenesis) in the target cells. | 8 | x |
| F153 | 19.2.8 | concept | The glucose homeostasis in blood is thus maintained jointly by the two – insulin and glucagons. | 8 | x |
| F154 | 19.2.8 | concept | Prolonged hyperglycemia leads to a complex disorder called diabetes mellitus which is associated with loss of glucose through urine and formation of harmful compounds known as ketone bodies. | 8 | x |
| F155 | 19.2.8 | concept | Insulin deficiency and/or insulin resistance result in a disease called diabetes mellitus. | 12 | x |
| F156 | 19.2.8 | concept | Diabetic patients are successfully treated with insulin therapy. | 8 | x |
| F157 | 19.2.9 | heading | 19.2.9 Testis | 8 | x |
| F158 | 19.2.9 | opener | A pair of testis is present in the scrotal sac (outside abdomen) of male individuals (Figure 19.1). | 8 | x |
| F159 | 19.2.9 | concept | Testis performs dual functions as a primary sex organ as well as an endocrine gland. | 8 | x |
| F160 | 19.2.9 | concept | Testis is composed of seminiferous tubules and stromal or interstitial tissue. | 8 | x |
| F161 | 19.2.9 | concept | The Leydig cells or interstitial cells, which are present in the intertubular spaces produce a group of hormones called androgens mainly testosterone. | 8 | x |
| F162 | 19.2.9 | concept | Androgens regulate the development, maturation and functions of the male accessory sex organs like epididymis, vas deferens, seminal vesicles, prostate gland, urethra etc. | 8 | x |
| F163 | 19.2.9 | concept | These hormones stimulate muscular growth, growth of facial and axillary hair, aggressiveness, low pitch of voice etc. | 8 | x |
| F164 | 19.2.9 | concept | Androgens play a major stimulatory role in the process of spermatogenesis (formation of spermatozoa). | 8 | x |
| F165 | 19.2.9 | concept | Androgens act on the central neural system and influence the male sexual behaviour (libido). | 8 | x |
| F166 | 19.2.9 | concept | These hormones produce anabolic (synthetic) effects on protein and carbohydrate metabolism. | 8 | x |
| F167 | 19.2.9 | concept | The testis secretes androgens, which stimulate the development, maturation and functions of the male accessory sex organs, appearance of the male secondary sex characters, spermatogenesis, male sexual behaviour, anabolic pathways and erythropoiesis. | 12 | x |
| F168 | 19.2.10 | heading | 19.2.10 Ovary | 8 | x |
| F169 | 19.2.10 | opener | Females have a pair of ovaries located in the abdomen (Figure 19.1). | 8 | x |
| F170 | 19.2.10 | concept | Ovary is the primary female sex organ which produces one ovum during each menstrual cycle. | 8 | x |
| F171 | 19.2.10 | concept | In addition, ovary also produces two groups of steroid hormones called estrogen and progesterone. | 8 | x |
| F172 | 19.2.10 | concept | Ovary is composed of ovarian follicles and stromal tissues. | 8 | x |
| F173 | 19.2.10 | concept | The estrogen is synthesised and secreted mainly by the growing ovarian follicles. | 8 | x |
| F174 | 19.2.10 | process | After ovulation, the ruptured follicle is converted to a structure called corpus luteum, which secretes mainly progesterone. | 8 | x |
| F175 | 19.2.10 | concept | Estrogens produce wide ranging actions such as stimulation of growth and activities of female secondary sex organs, development of growing ovarian follicles, appearance of female secondary sex characters (e.g., high pitch of voice, etc.) and mammary gland development. | 8 | x |
| F176 | 19.2.10 | concept | Estrogens also regulate female sexual behaviour. | 9 | x |
| F177 | 19.2.10 | concept | Progesterone supports pregnancy. | 9 | x |
| F178 | 19.2.10 | concept | Progesterone also acts on the mammary glands and stimulates the formation of alveoli (sac-like structures which store milk) and milk secretion. | 9 | x |
| F179 | 19.2.10 | concept | Progesterone plays a major role in the maintenance of pregnancy as well as in mammary gland development and lactation. | 12 | x |
| F180 | 19.2.10 | definition | (d) Progestational hormone | 13 | x |
| F181 | 19.3 | heading | 19.3 HORMONES OF HEART, KIDNEY AND GASTROINTESTINAL TRACT | 9 | x |
| F182 | 19.3 | opener | Now you know about the endocrine glands and their hormones. However, as mentioned earlier, hormones are also secreted by some tissues which are not endocrine glands. | 9 | x |
| F183 | 19.3 | concept | For example, the atrial wall of our heart secretes a very important peptide hormone called atrial natriuretic factor (ANF), which decreases blood pressure. | 9 | x |
| F184 | 19.3 | process | When blood pressure is increased, ANF is secreted which causes dilation of the blood vessels. This reduces the blood pressure. | 9 | x |
| F185 | 19.3 | concept | The juxtaglomerular cells of kidney produce a peptide hormone called erythropoietin which stimulates erythropoiesis (formation of RBC). | 9 | x |
| F186 | 19.3 | concept | Endocrine cells present in different parts of the gastro-intestinal tract secrete four major peptide hormones, namely gastrin, secretin, cholecystokinin (CCK) and gastric inhibitory peptide (GIP). | 9 | x |
| F187 | 19.3 | process | Gastrin acts on the gastric glands and stimulates the secretion of hydrochloric acid and pepsinogen. | 9 | x |
| F188 | 19.3 | process | Secretin acts on the exocrine pancreas and stimulates secretion of water and bicarbonate ions. | 9 | x |
| F189 | 19.3 | process | CCK acts on both pancreas and gall bladder and stimulates the secretion of pancreatic enzymes and bile juice, respectively. | 9 | x |
| F190 | 19.3 | process | GIP inhibits gastric secretion and motility. | 9 | x |
| F191 | 19.3 | process | These hormones regulate the secretion of digestive juices and help in digestion. | 12 | x |
| F192 | 19.3 | concept | Several other non-endocrine tissues secrete hormones called growth factors. These factors are essential for the normal growth of tissues and their repairing/regeneration. | 9 | x |
| F193 | 19.4 | heading | 19.4 MECHANISM OF HORMONE ACTION | 9 | x |
| F194 | 19.4 | opener | Hormones produce their effects on target tissues by binding to specific proteins called hormone receptors located in the target tissues only. | 9 | x |
| F195 | 19.4 | definition | Hormone receptors present on the cell membrane of the target cells are called membrane-bound receptors and the receptors present inside the target cell are called intracellular receptors, mostly nuclear receptors (present in the nucleus). | 9 | x |
| F196 | 19.4 | process | Binding of a hormone to its receptor leads to the formation of a hormone-receptor complex (Figure 19.5 a, b). | 9 | x |
| F197 | 19.4 | concept | Each receptor is specific to one hormone only and hence receptors are specific. | 9 | x |
| F198 | 19.4 | process | Hormone-Receptor complex formation leads to certain biochemical changes in the target tissue. | 9 | x |
| F199 | 19.4 | concept | Target tissue metabolism and hence physiological functions are regulated by hormones. | 9 | x |
| F200 | 19.4 | concept | On the basis of their chemical nature, hormones can be divided into groups : | 10 | x |
| F201 | 19.4 | example | (i) peptide, polypeptide, protein hormones (e.g., insulin, glucagon, pituitary hormones, hypothalamic hormones, etc.) | 10 | x |
| F202 | 19.4 | example | (ii) steroids (e.g., cortisol, testosterone, estradiol and progesterone) | 10 | x |
| F203 | 19.4 | example | (iii) iodothyronines (thyroid hormones) | 10 | x |
| F204 | 19.4 | example | (iv) amino-acid derivatives (e.g., epinephrine). | 10 | x |
| F205 | 19.4 | process | Hormones  which interact with membrane-bound receptors normally do not enter the target cell, but generate second messengers (e.g., cyclic AMP, IP3, Ca++ etc) which in turn regulate cellular metabolism (Figure 19.5a). | 10 | x |
| F206 | 19.4 | process | Hormones which interact with intracellular receptors (e.g., steroid hormones, iodothyronines, etc.) mostly regulate gene expression or chromosome function by the interaction of hormone-receptor complex with the genome. | 10 | x |
| F207 | 19.4 | concept | Cumulative biochemical actions result in physiological and developmental effects (Figure 19.5b). | 10 | x |
| F208 | Fig 19.5 | caption | Figure 19.5 Diagramatic representation of the mechanism of hormone action : (a) Protein hormone  (b) Steroid hormone | 11 | x |
| F209 | Summary | heading | SUMMARY | 11 | x |
| F210 | Exercises | heading | EXERCISES | 13 | x |
| F211 | Note | heading | NOTE | 14 | x |
| F212 | Fig 19.1 | caption | Figure labels: "Hypothalamus"; "Pituitary"; "Pineal"; "Thyroid and Parathyroid"; "Thymus"; "Pancreas"; "Adrenal"; "Ovary (in female)"; "Testis (in male)" | 2 | x |
| F213 | Fig 19.2 | caption | Figure labels: "Hypothalamus"; "Hypothalamic neurons"; "Portal circulation"; "Posterior pituitary"; "Anterior pituitary" | 3 | x |
| F214 | Fig 19.3 (a) | caption | Figure (a) labels: "Vocal cord"; "Thyroid"; "Trachea" | 4 | x |
| F215 | Fig 19.3 (b) | caption | Figure (b) labels: "Parathyroid glands" | 4 | x |
| F216 | Fig 19.4 (a)/(b) | caption | Figure labels: "Adrenal gland"; "Kidney"; "Adrenal cortex"; "Adrenal medulla" | 6 | x |
| F217 | Fig 19.5 (a) | caption | Figure (a) labels: "Hormone (e.g., FSH)"; "Receptor"; "Ovarian cell membrane"; "Response 1"; "(Generation of second messenger)"; "(Cyclic AMP or Ca++)"; "Biochemical responses"; "Physiological responses (e.g., ovarian growth)" | 10 | x |
| F218 | Fig 19.5 (b) | caption | Figure (b) labels: "Hormone (e.g., estrogen)"; "Uterine cell membrane"; "Nucleus"; "Genome"; "mRNA"; "Proteins"; "Hormone-receptor complex"; "Physiological responses (Tissue growth and differentiation)" | 11 | x |

## Row census (machine-derived from the table above at freeze time)

Derivation: `scratch/ch19_gate1/gate1_close.py`, run against this file after the last edit to the table. Every number here is a re-parse, not a tally.

| Quantity | Value |
|---|---:|
| Rows | 218 |
| ID range | `F001`–`F218`, contiguous, monotonic |
| Duplicate IDs | 0 |
| Gaps | 0 |
| Rows ticked | 218 / 218 |
| Content Facts | 211 |
| Figure-label matrix rows | 7 |

Type census — **9 values, all lowercase**:

| Type | Count |
|---|---:|
| concept | 108 |
| process | 27 |
| definition | 19 |
| heading | 19 |
| opener | 19 |
| caption | 12 |
| example | 7 |
| contents | 4 |
| number | 3 |
| **total** | **218** |

`caption` = 5 figure captions (`F027`, `F069`, `F095`, `F137`, `F208`) + the 7 figure-label matrix rows (`F212`–`F218`), which keep `caption` so the `_extract_labels` parser continues to see them.

### Heading census (`1-H`) — 19 rows = 14 numbered + the 5 unnumbered IDs below

`14 + 5 = 19`, and 19 is the `heading` count in the type census above.

- **14 numbered:** `F012` (19.1), `F021` (19.2), `F028` (19.2.1), `F038` (19.2.2), `F070` (19.2.3), `F076` (19.2.4), `F096` (19.2.5), `F105` (19.2.6), `F113` (19.2.7), `F138` (19.2.8), `F157` (19.2.9), `F168` (19.2.10), `F181` (19.3), `F193` (19.4).
- **5 unnumbered:** `F001` (chapter title), `F002` (`CHAPTER  19`), `F209` (`SUMMARY`), `F210` (`EXERCISES`), `F211` (`NOTE`).

`1-H` walked the source's own type hierarchy rather than trusting the prose sweep, and found **no missing sub-heading**: sections 19.1–19.4 and 19.2.1–19.2.10 are the complete set, and there is no unnumbered sub-heading sitting inside any of them (the Ch9 D4 failure mode does not occur in this chapter). See the `1-H` record below for the font-hierarchy finding that makes this non-trivial.

### Opener census (`1-O`) — 19 rows = 5 chapter-opener + the 14 section-opener IDs below

`5 + 14 = 19`, and 19 is the `opener` count in the type census above.

- **5 chapter-opener** (the pre-19.1 lead paragraph on p. 1): `F003`–`F007`.
- **14 section-opener**, one per numbered section, in section order: `F013` (19.1), `F022` (19.2), `F029` (19.2.1), `F039` (19.2.2), `F071` (19.2.3), `F077` (19.2.4), `F097` (19.2.5), `F106` (19.2.6), `F114` (19.2.7), `F139` (19.2.8), `F158` (19.2.9), `F169` (19.2.10), `F182` (19.3), `F194` (19.4).

**Every numbered section has exactly one `opener` row and the count is 14 = the numbered-heading count** — the two censuses cross-check each other, which is the property that makes a dropped opener detectable.

## Note on the `α`/`β` rows — and a correction `1-H` made to this note

`F142` and `F143` hold the source's Greek **`α-cells` / `β-cells` as real Greek glyphs** (U+03B1, U+03B2), character-for-character with the source, like every other row in this table.

**This paragraph previously claimed the opposite** — that the two rows were "a deliberate ASCII transliteration" reading `alpha-cells` / `beta-cells`. That claim was false about the file it was printed in: a byte inspection of both rows returns `α` and `β`. It is the more dangerous direction of error, because a Pass 2 author trusting it would "restore" Greek letters that were never lost, or worse, treat the ASCII spelling as the frozen wording and ship it.

**Carry-forward for Pass 2, which is the real constraint here:** `check_pdf.py` check 5 bans Greek letters from the *generated* PDF's text stream. So the inventory row is Greek (it must match the source) while the rendered page must not be — the script has to spell these two out as `alpha-cells` / `beta-cells` in the running text. That is a rendering decision at Pass 2, **not** an edit to these rows.

## Figure-label matrix note

The matrix exists in exactly one place: the `## Facts` table above, rows `F212`–`F218`. Each row begins with `Figure labels:` or `Figure (a)/(b) labels:` in the wording column, matching the `_extract_labels` parser used by `check_pdf.py`. There is no duplicate pipe-delimited label table elsewhere in this inventory, so labels are not double-counted and no phantom separator row is created.

**Machine re-parse, run by `1-Z` after the last edit to this file** (`scratch/ch19_gate1/gate1_close.py`, which imports the real `_extract_labels` out of `check_pdf.py` rather than reimplementing it):

| Quantity | Value |
|---|---:|
| Figure rows parsed | 7 |
| Labels parsed | 38 |
| Per-figure split | `19.1` 9 · `19.2` 5 · `19.3 (a)` 3 · `19.3 (b)` 1 · `19.4 (a)/(b)` 4 · `19.5 (a)` 8 · `19.5 (b)` 8 |
| Doubled labels | 0 |
| Phantom `Fig #` rows | 0 |

`9+5+3+1+4+8+8 = 38`, so the total is derivable from the split beside it. The re-parse was re-run **after** the two pipe-delimited tables in `## Summary classification` and `## Exercise-gap terms` were added, because `_extract_labels` scans every pipe-delimited line in the file and those tables are exactly the shape that produced Ch12's phantom-row failure; the count is unchanged at 7 / 38, so neither table is visible to the parser.

## Summary classification

`1-Z`, over the `SUMMARY` block that runs from the heading on p. 11 to the end of p. 12. **32 sentences**, enumerated by machine (`scratch/ch19_gate1/summary_classify.py`) so the census total is the length of this list — not a hand tally, and with no sentence classified that was never read.

Method, stated because the verdict column is a judgement and the evidence for it should be inspectable: for each sentence the script reports (a) the best-matching Facts rows by content-word overlap and (b) every content word in the sentence that appears in **no** Facts row at all. A word occurring nowhere in the body is the signal for SUMMARY-UNIQUE; a high-overlap match with no unmatched words is the signal for BODY-PRESENT.

Only **2 of 32** sentences flagged a word absent from every body row — S09 (`state`, `awake`) and S20 (`contents`) — and both resolved to wording variants on inspection: S09's `state of being awake` is `F074`'s `sleep-wake cycle`, and S20's `electrolyte contents` is `F129`'s `balance of water and electrolytes`. **The vocabulary test is a filter, not the verdict**, and this is the direction it fails in: it cannot see a sentence that reuses only body words while restating them, so S12 (`calcium homeostasis` for `F104`'s `calcium balance`) and S14 (`increase` for `F110`'s `promote`) are wording variants that the machine passed clean. Four sentences are therefore marked `BODY-PRESENT (wording variant)` — S09, S12, S14, S20 — against two the machine flagged. Every one of the 32 was read against its named body row by hand; the script only guarantees none was skipped.

| Summary sentence | Classification | Folded into |
|---|---|---|
| S01 There are special chemicals which act as hormones and provide chemical coordination, integration and regulation in the human body. | BODY-PRESENT | `F018` |
| S02 These hormones regulate metabolism, growth and development of our organs, the endocrine glands or certain cells. | BODY-PRESENT | `F020` |
| S03 The endocrine system is composed of hypothalamus, pituitary and pineal, thyroid, adrenal, pancreas, parathyroid, thymus and gonads (testis and ovary). | BODY-PRESENT | `F024` |
| S04 In addition to these, some other organs, e.g., gastrointestinal tract, kidney, heart etc., also produce hormones. | BODY-PRESENT | `F025` |
| S05 The pituitary gland is divided into three major parts, which are called as pars distalis, pars intermedia and pars nervosa. | BODY-PRESENT | `F047` |
| S06 Pars distalis produces six trophic hormones. | BODY-PRESENT | `F043` |
| S07 Pars intermedia secretes only one hormone, while pars nervosa (neurohypophysis) secretes two hormones. | BODY-PRESENT | `F044`, `F046` |
| S08 The pituitary hormones regulate the growth and development of somatic tissues and activities of peripheral endocrine glands. | BODY-PRESENT | `F068` |
| S09 Pineal gland secretes melatonin, which plays a very important role in the regulation of 24-hour (diurnal) rhythms of our body (e.g., rhythms of sleep and state of being awake, body temperature, etc.). | BODY-PRESENT (wording variant) | `F072`, `F073`, `F074` |
| S10 The thyroid gland hormones play an important role in the regulation of the basal metabolic rate, development and maturation of the central neural system, erythropoiesis, metabolism of carbohydrates, proteins and fats, menstrual cycle. | BODY-PRESENT | `F092` |
| S11 Another thyroid hormone, i.e., thyrocalcitonin regulates calcium levels in our blood by decreasing it. | BODY-PRESENT | `F094` |
| S12 The parathyroid glands secrete parathyroid hormone (PTH) which increases the blood Ca2+ levels and plays a major role in calcium homeostasis. | BODY-PRESENT (wording variant) | `F100`, `F104` |
| S13 The thymus gland secretes thymosins which play a major role in the differentiation of T-lymphocytes, which provide cell-mediated immunity. | BODY-PRESENT | `F109` |
| S14 In addition, thymosins also increase the production of antibodies to provide humoral immunity. | BODY-PRESENT (wording variant) | `F110` |
| S15 The adrenal gland is composed of the centrally located adrenal medulla and the outer adrenal cortex. | BODY-PRESENT | `F116` |
| S16 The adrenal medulla secretes epinephrine and norepinephrine. | BODY-PRESENT | `F118` |
| S17 These hormones increase alertness, pupilary dilation, piloerection, sweating, heart beat, strength of heart contraction, rate of respiration, glycogenolysis, lipolysis, proteolysis. | **SUMMARY-UNIQUE** | **`F125` (folded)** |
| S18 The adrenal cortex secretes glucocorticoids and mineralocorticoids. | BODY-PRESENT | `F127`, `F128`, `F129` |
| S19 Glucocorticoids stimulate gluconeogenesis, lipolysis, proteolysis, erythropoiesis, cardio-vascular system, blood pressure, and glomerular filtration rate and inhibit inflammatory reactions by suppressing the immune response. | BODY-PRESENT | `F134` |
| S20 Mineralocorticoids regulate water and electrolyte contents of the body. | BODY-PRESENT (wording variant) | `F129` |
| S21 The endocrine pancreas secretes glucagon and insulin. | BODY-PRESENT | `F140`, `F143` |
| S22 Glucagon stimulates glycogenolysis and gluconeogenesis resulting in hyperglycemia. | BODY-PRESENT | `F145` |
| S23 Insulin stimulates cellular glucose uptake and utilisation, and glycogenesis resulting in hypoglycemia. | BODY-PRESENT | `F150`, `F151` |
| S24 Insulin deficiency and/or insulin resistance result in a disease called diabetes mellitus. | BODY-PRESENT | `F155` |
| S25 The testis secretes androgens, which stimulate the development, maturation and functions of the male accessory sex organs, appearance of the male secondary sex characters, spermatogenesis, male sexual behaviour, anabolic pathways and erythropoiesis. | BODY-PRESENT | `F167` |
| S26 The ovary secretes estrogen and progesterone. | BODY-PRESENT | `F171` |
| S27 Estrogen stimulates growth and development of female accessory sex organs and secondary sex characters. | BODY-PRESENT | `F175` |
| S28 Progesterone plays a major role in the maintenance of pregnancy as well as in mammary gland development and lactation. | **SUMMARY-UNIQUE** | **`F179` (folded)** |
| S29 The atrial wall of the heart produces atrial natriuretic factor which decreases the blood pressure. | BODY-PRESENT | `F183` |
| S30 Kidney produces erythropoietin which stimulates erythropoiesis. | BODY-PRESENT | `F185` |
| S31 The gastrointestinal tract secretes gastrin, secretin, cholecystokinin and gastric inhibitory peptide. | BODY-PRESENT | `F186` |
| S32 These hormones regulate the secretion of digestive juices and help in digestion. | **SUMMARY-UNIQUE** | **`F191` (folded)** |

**Census: 32 sentences = 29 BODY-PRESENT + the 3 SUMMARY-UNIQUE IDs below.** `29 + 3 = 32`, which is the sentence count in the source-structure table above.

**The 3 SUMMARY-UNIQUE facts, all folded before the freeze** (this is what changed the row count from 208 to 211 content Facts):

- **`F125`** (§19.2.7, after the catecholamine-effects run) — the SUMMARY names `glycogenolysis`, `lipolysis` and `proteolysis` as catecholamine effects. The body lists the *physiological* effects (alertness, pupilary dilation, piloerection, sweating, heart beat, respiration) but never these three metabolic terms, which are exactly the marks-critical vocabulary Rule 4 exists to protect.
- **`F179`** (§19.2.10, after the progesterone actions) — the body gives progesterone's role in pregnancy maintenance; the SUMMARY adds `mammary gland development and lactation`.
- **`F191`** (§19.3, after the four GI hormones) — the body states each GI hormone's individual action; the SUMMARY adds the generalisation that these hormones regulate the secretion of digestive juices and help in digestion.

Each was inserted **in Content Order at its own body section**, not appended at the tail, which is why the whole table was renumbered and every cross-reference in this file was rewritten through an explicit old→new ID map (`scratch/ch19_gate1/apply_h_o_z.py`).

**Wording variants are not folds.** S09, S12 and S20 restate a body fact in new words; folding them would duplicate a fact the inventory already holds and inflate the row count with no new information. They are marked BODY-PRESENT with the body row named, so the judgement is auditable rather than invisible.

## Exercise-gap terms

`1-Z`, over the 9 questions / 39 lettered sub-parts on p. 13. Every term an exercise *assumes* was checked against the Facts table by machine; the terms below are the ones whose status needed a decision.

| Term/fact assumed by exercises | Explained where |
|---|---|
| `Exocrine gland` — Q1(a) asks the student to **define** it | **GAP.** The body uses the word (`F139`: pancreas "acts as both exocrine and endocrine gland"; `F188`: "the exocrine pancreas") but never defines it, while `F013`/`F014` define the endocrine gland by contrast. Pass 2 places the contrast in §19.1 beside `F013`, phrased **only** from what the source itself supplies — ductless vs. duct-bearing — since Rule 5 forbids importing an outside definition. |
| `Endocrine gland`, `Hormone` — Q1(b), Q1(c) | Defined in §19.1: `F013` (ductless glands), `F014` (secretions are hormones), `F016` (the current definition). No gap. |
| `Atrium`, `G-I Tract` — Q3(j), Q3(l) | Body-present under the source's own spellings: `F183` (`atrial wall`), `F186` (`gastro-intestinal tract`). The exercise's shorter forms are the same referent, so this is a wording difference, not a gap. Pass 2 must keep the body's spellings. |
| `Hypoglycemic` / `Hyperglycemic` hormone — Q6(a) | Body-present as the noun: `F151` (`hypoglycemia`), `F145`/`F148` (`hyperglycemia`). The adjective form appears only in the exercise. No gap. |
| `Gonadotrophic hormones` — Q6(c) | `F056`: "LH and FSH stimulate gonadal activity and hence are called gonadotrophins." No gap. |
| `Blood pressure lowering hormone` — Q6(e) | `F183`/`F184`: ANF decreases blood pressure. No gap. |
| `Mechanism of action of FSH` — Q8 | §19.4 supplies the mechanism (`F205`, membrane-bound receptor → second messenger) and `F217` supplies the FSH-specific figure labels (Figure 19.5a is drawn with `Hormone (e.g., FSH)`). No gap; Pass 2 must keep the figure adjacent to §19.4 so the two halves of the answer are not separated. |
| `Thymosins`, `Androgens`, `Estrogens`, `Insulin`, `Glucagon`, `PTH`, `Thyroid hormones` — Q5 | All body-present in their own sections. No gap. |
| `Diabetes mellitus`, `Goitre`, `Cretinism` — Q7 | `F155`, `F083`, `F084`. No gap. |
| `Melanotrophin`, `Thyrotrophin`, `Corticotrophin`, `Gonadotrophins`, `Hypothalamic hormones` — Q4 | Body-present: `F044` (MSH), `F052` (TSH), `F054` (ACTH), `F056` (LH/FSH), `F032`–`F034` (releasing/inhibiting hormones). The exercise's own labels are additionally held verbatim as rows `F053` (`(b) Thyrotrophin (TSH)`) and `F055` (`(c) Corticotrophin (ACTH)`), since the exercise is the only place the chapter prints those two names. No gap. |

**Exactly one gap, and it has a planned home.** Under Rule 2 this is closed as a gap-only addition in §19.1 — not an answer key, and not an imported definition.

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

**Source-page correction:** the Figure 19.5 (a) row previously gave source page **10**, and 19.5 (b) page **11** — but the printed `Figure 19.5` caption sits on **page 11**, with the `(a)` panel on page 10 and the `(b)` panel plus the caption on page 11. Panel pages are unchanged (they are what the crops came from); the caption's own page is now recorded separately in `F208`, which is what a Pass 2 script needs in order to place the caption.

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
- **`1-S`'s own machine-derived count: 208 content Facts** entered in Content Order, from the chapter opener through `EXERCISES`, plus the 7 renumbered figure-label rows = **215 rows** at the close of `1-S`. (`1-S` first reported 193/200; that was a hand tally against a table that already held 215 rows, and it is the reason step 10 forbids hand tallies. The re-parse is the number of record. The later sessions then took the table to 218 — see `1-Z`.)
- **Structure derived, not guessed:** 4 top-level sections, 10 subsections (all under 19.2), 14 numbered headings, 5 structural unnumbered headings, 5 numbered figures, 9 exercises with 39 lettered sub-parts. (`1-S` reported 4 unnumbered headings and 41 sub-parts; both were corrected by machine in `1-H`/`1-Z` — see the source-structure table above.)
- **5 source misspellings/inconsistencies catalogued** (`sella tursica`, `Exopthalmic`, `pupilary`, `glucagons`, `Diagramatic`) and held **verbatim** in their rows.
- **3 defects in the pre-existing `1-F` documentation found and fixed** (all metadata; no asset, no crop box and no shared repo file touched): the false `Frozen Inventory` H1; the "verbatim" caption column that actually held paraphrases and silently repaired the source's `Diagramatic` typo; and the Figure 19.5 caption page recorded as the panel page.

### `1-H` — heading sweep — COMPLETE (2026-09-01)

Deliverable: `scratch/ch19_gate1/heading_sweep.py`, which walks the source's own type hierarchy — **headings only, prose deliberately ignored** — and prints the census as `14 numbered + 5 unnumbered = 19`, matching the `heading` count in the type census above.

- **`1-H`'s own machine-derived count: 19 heading rows.** No heading row was added by this session; the sweep's job was to prove the 19 already in the table are the complete set, and it did — sections 19.1–19.4 and 19.2.1–19.2.10 are all present, and **no unnumbered sub-heading sits inside any of them.** The Ch9 D4 failure mode (content present, heading silently missing) does not occur in this chapter.
- **The finding that makes the sweep non-trivial: the source's own heading font-name is inconsistent.** Heading-sized spans use `Bookman-Demi` **26 times** and `Bookman,Bold` **7 times** for the same structural levels — `19.2.7 Adrenal Gland`, `19.3`, `19.4` and `SUMMARY` are set in the minority spelling. **A font-NAME filter would therefore have silently dropped four real headings, including a whole gland subsection**, and reported a clean 15. The sweep filters on **size** (≥ 12.0 pt: 12.0 = subsection, 13.0 = section, 15.4/26.8 = chapter title, 12.6 = chapter label, 18.0 = `NOTE`) for exactly that reason. Inline `Bookman-Demi` at 10.5 pt is *bold key-term emphasis inside body text*, not a heading, and is excluded — including it would have invented dozens of phantom headings.
- **Two structural facts that would otherwise be miscounted.** (a) The chapter title prints on **two lines** (`CHEMICAL COORDINATION` / `AND INTEGRATION`) and is **one row** (`F001`) — a line-counting sweep reports 20. (b) The source sets each numbered heading's *number* and *title* as separate text lines, so a naive "unnumbered = line without a section number" rule classifies all 14 titles as unnumbered and returns 19 unnumbered headings; the classifier pairs number-lines with the title-line that follows, which is why the honest figure is 5.
- **Corrections `1-H` made:** the source-structure table's unnumbered-heading count (**4 → 5**; the `NOTE` row `F211` existed while the census omitted it, so the census contradicted its own table), and the false `α`/`β` "ASCII transliteration" note (see that section — a byte inspection returns real U+03B1/U+03B2).
- **Carry-forward for Pass 2, from this session's page-6 inspection:** the source renders essentially all of page 6 (§19.2.7's opening) in *italic* `Bookman` — a source typesetting accident, not emphasis. Pass 2 must **not** reproduce page 6 as italic body text.

### `1-O` — opener sweep — COMPLETE (2026-09-01)

Deliverable: `scratch/ch19_gate1/opener_verify.py`, which reads **openers only, headings ignored**, and asserts two properties against the source PDF rather than against this file's own prose.

- **`1-O`'s own machine-derived count: 19 opener rows = 5 chapter-opener (`F003`–`F007`) + 14 section-opener, one per numbered section.** `5 + 14 = 19`, which is the `opener` count in the type census, and the 14 equals the numbered-heading count — the two censuses cross-check each other.
- **Property A ��� Content Order (§5) holds.** `Src` page numbers are non-decreasing across the **189 body-prose rows**: 0 out-of-order rows. Two row classes are excluded, and the exclusion is printed by the script so it can be audited rather than believed: the **17 FOLD rows** (a numbered section carrying `Src` p11–p13 — a SUMMARY-UNIQUE fact folded into its body section, or an exercise label held verbatim beside the body fact it assumes) and the **5 caption rows**, which sit beside the prose that refers to the figure. `189 + 17 + 5 = 211` content rows.
- **Property B — every section's `opener` row really is that section's first sentence.** For all **14/14** numbered sections, the row typed `opener` is located earliest in the source token stream of all that section's prose rows. This is the check that catches the failure 1-S cannot: the opening sentence existing *somewhere* in the table is not enough, it must be the row marked `opener`.
- **A matcher artefact caught and fixed inside this session, recorded because it presented as a content defect.** The first run reported §19.2.10's opener `F169` ranked **2nd**, behind `F170` — an apparent real ordering defect. It was not. The matcher tolerates bounded gaps (NCERT's marginal contents column extracts *inside* body paragraphs, and long sentences wrap across page breaks), and `F170` begins `Ovary is the primary female sex organ…` while the token `Ovary` also occurs one token earlier **in the heading `19.2.10 Ovary`** — so the earliest-start match began at the heading and skipped the entire opening sentence within its gap budget. The fix is to rank by the **tightest** match (smallest span), not the earliest start: a true occurrence has span `len(needle)` and any heading-anchored match is strictly longer. After the fix all 14 sections are `1/N`. **Verdict: the source, the table and the types were right; the measurement was wrong** — which is the direction of error worth writing down, because the tempting "fix" was to edit a correct row.
- **No opener row was added or reclassified by this session.** The `opener` typing and the `contents` typing of `F008`–`F011` (the marginal contents column, which is not a section opener) were applied in the preceding session's transform; `1-O`'s deliverable is the machine proof that the result is right.

### `1-Z` — gaps, summary & freeze — COMPLETE (2026-09-01)

- **Summary scan (step 8):** **32 SUMMARY sentences = 29 BODY-PRESENT + 3 SUMMARY-UNIQUE**, all 3 folded **before** the freeze — `F125` (S17, `glycogenolysis, lipolysis, proteolysis`), `F179` (S28, progesterone → mammary gland development and lactation) and `F191` (S32, hormones regulate the secretion of digestive juices). **This is what took the table from 208 to 211 content Facts.** Enumeration and evidence: `scratch/ch19_gate1/summary_classify.py`; the full sentence-by-sentence table with its named body row is in `## Summary classification` above. Four sentences are BODY-PRESENT **wording variants** (S09, S12, S14, S20) against the two the vocabulary filter flagged — the filter cannot see a sentence that restates a body fact using only body words, which is why every one of the 32 was also read against its named row by hand.
- **Exercise-gap scan (step 7, Rule 2):** **9 questions / 39 lettered sub-parts / exactly 1 gap** — Q1(a) `Exocrine gland`, which the body *uses* (`F139`, `F188`) but never defines. Its planned home is §19.1 beside `F013`, phrased only from what the source itself supplies (ductless vs. duct-bearing), since Rule 5 forbids importing an outside definition. Every other exercise-assumed term resolves to a named body row — see `## Exercise-gap terms`.
- **Corrections `1-Z` made:** the sub-part count (**41 → 39 lettered**, or 43 counting Q9's Column II, both readings now stated with the per-question addition beside them), and the figure-label count (**35 → 38**, see the header-correction record — the only live restatement of that number in the file, and a script written against 35 would have arrived at Gate 2 three labels short of check 6).
- **`1-Z`'s own machine-derived count: 218 rows** = 211 content Facts + 7 figure-label matrix rows, `F001`–`F218`, contiguous and monotonic, 0 gaps, 0 duplicates, 218/218 ticked, type census summing to 218 across 9 all-lowercase values. Derivation: `scratch/ch19_gate1/gate1_close.py`.

### Freeze declaration (2026-09-01)

**This inventory is FROZEN.** All five Pass 1 sessions have run — `1-F` (2026-08-30) · `1-S`, `1-H`, `1-O`, `1-Z` (2026-09-01) — each reporting its own machine-derived row count, and every count in this file was re-derived by re-parsing the finished `## Facts` table after the last edit to it.

**No row may be added, removed or reworded from here on.** A Pass 2 discovery that this file is incomplete **reopens Gate 1** and is recorded as a Pass 1 gap; it is not patched into the freeze silently and never back-dated.

Pass 2 may now be written against this file, ticking rows in place as each is written into the script.

### Gate 1 checklist — every criterion, with the evidence

| §6 Gate 1 criterion | State | Evidence |
|---|---|---|
| Every fact has a Facts row; every in-figure label has a matrix row, harvested by **opening each rendered asset** | ✅ | 211 content Facts + 7 matrix rows; labels harvested in `1-F` by opening all 7 PNGs individually at 440 dpi, not by text extraction |
| Inventory validated by running **`check_pdf.py`'s own `_extract_labels`** — expected figure count, no doubling, no phantom rows | ✅ | `gate1_close.py` imports the real parser from `check_pdf.py`: **7 figures / 38 labels / 0 doubled / 0 phantom `Fig #`**, re-run after the two new pipe tables were added |
| Every header count matches a re-parse; `F001..FNNN` contiguous, no gaps or duplicates; every **restatement** fixed, not just the header; each census total equals the length of its own list | ✅ | 218 rows, `F001`–`F218`, contiguous, monotonic, 0 gaps, 0 dupes, 218/218 ticked; heading `14+5=19`, opener `5+14=19`, summary `29+3=32`, sub-parts `3+0+12+5+6+6+3+0+4=39`, labels `9+5+3+1+4+8+8=38` — each written so the total is derivable from the list beside it |
| `Type` column uses one normalized spelling/casing per value | ✅ | 9 values, **all lowercase**, summing to 218; `gate1_close.py` reports `non-lowercase Type values: none` |
| Every heading has a `heading` row, **including unnumbered sub-headings**, confirmed by walking the headings as their own list | ✅ | `1-H` / `heading_sweep.py`: 19 rows = 14 numbered + 5 unnumbered; no unnumbered sub-heading exists inside any section; size-based filter used because the source's heading **font names** are inconsistent (26 `Bookman-Demi` vs 7 `Bookman,Bold`) |
| Every section's opening sentence has an `opener` row, confirmed by walking the openers as their own list | ✅ | `1-O` / `opener_verify.py`: 14/14 sections' `opener` row is the earliest-positioned prose row of its section in the source; Content Order also asserted (0 out-of-order body rows) |
| **All five Pass 1 sessions actually ran**, each reporting its own machine-derived count | ✅ | `1-F` 7 assets / 38 labels · `1-S` 208 Facts + 7 = 215 rows · `1-H` 19 heading rows · `1-O` 19 opener rows · `1-Z` +3 folds → **218 rows** |
| Every figure in the manifest is `Mono: yes` and `Verified: yes` | ✅ | 7/7 rows in `## Figure manifest`, all `mode=L`, each opened individually |
| Every exercise-gap term has a planned home; every SUMMARY-UNIQUE fact folded into a body row | ✅ | 1 gap (Q1(a) `Exocrine gland` → §19.1 beside `F013`); 3 SUMMARY-UNIQUE folded into `F125`, `F179`, `F191` |
| Inventory file saved to the chapter folder | ✅ | `notes/class 11/Ch19_ChemicalCoordinationAndIntegration/Ch19_ChemicalCoordinationAndIntegration_inventory.md` |

**Verdict: GATE 1 GREEN (2026-09-01).** `gate1_close.py` prints `VERDICT: GREEN`; `opener_verify.py` prints `VERDICT: GREEN`. Pass 2 may begin.

**Housekeeping done at the freeze:** the stale duplicate `Ch19_ChemicalCoordinationAndIntegration_inventory.new.md` was **deleted**. It was a 43 KB intermediate from an earlier PR holding a *subset* of this table (the canonical `.md` was already the promoted superset), and leaving two files whose names differ by one word beside a freeze is how a later session ticks rows in the wrong file.

### What Gate 1 does NOT claim

*This subsection is the Gate 1 record as written on 2026-09-01 and is kept unaltered for history. **It is superseded on the script/PDF point by `## Gate 2 record` below**, which is the current state: the script and the PDF now exist and checks 6 and 7 have been run against them. What still holds is the last sentence — Gate 3 is open and the chapter is counted in no completion tally.*

No script and no PDF exist for this chapter yet. Every `x` in the `Ticked` column means **"read off the numbered source page and confirmed character-for-character"** — it is not a claim about any delivered PDF, and `check_pdf.py`'s checks 6 and 7 have never been run against a Ch19 PDF because there is nothing to run them against. Gates 2 and 3 are **open**, and this chapter must not be counted in any completion tally.

**Carry-forward list for Pass 2** (each item is a decision already made, not a question to re-litigate):

| # | Carry-forward | Why |
|---|---|---|
| 1 | Render `α-cells` / `β-cells` as `alpha-cells` / `beta-cells` in the running text | Rows `F142`/`F143` hold real Greek glyphs to match the source; `check_pdf.py` check 5 bans Greek from the generated PDF. A rendering decision, **not** an edit to those rows |
| 2 | Keep all 5 source misspellings verbatim (`sella tursica`, `Exopthalmic goitre`, `pupilary dilation`, `glucagons`, `Diagramatic`) | Rule 4; the source is internally inconsistent (`Diagrammatic` in three captions, `Diagramatic` in the fourth) and both forms are frozen in their own rows |
| 3 | Do **not** set page 6's content in italic | The source italicises essentially all of page 6 by accident (`1-H` finding) |
| 4 | Close the one exercise gap in §19.1 beside `F013`, ductless-vs-duct-bearing only | Rule 2 gap-only; Rule 5 forbids an imported definition |
| 5 | Keep Figure 19.5 adjacent to §19.4 | Q8 (`mechanism of action of FSH`) is answered only by §19.4's prose **plus** `F217`'s figure labels; separating them splits the answer |
| 6 | Keep the body's spellings `atrial wall` / `gastro-intestinal tract` even though the exercise prints `Atrium` / `G-I Tract` | Same referent, source wording wins |
| 7 | All 38 figure labels must appear in the running text | check 6 gates on the matrix, and the count is 38 — not the 35 this file previously claimed |
| 8 | Figure 19.4 stays ONE combined asset | Its two panels interleave horizontally; any rectangular split cuts the kidney, labels or the connector |

## Gate 2 record

### Pass 2 — script + PDF (2026-09-01)

`Ch19_ChemicalCoordinationAndIntegration.py` was written **linearly from this frozen file in Content Order (§5)**, one `# ---- N.N ----` block per NCERT section, importing the repo-level `neet_template.py` (§0.6). Machine-checked properties of the delivered script and PDF:

- **18 block markers**, in source order: title block · `19.intro` · `19.1` · `19.2` · `19.2.1`–`19.2.10` (all ten glands, in NCERT's own order) · `19.3` · `19.4` · `Recap` (source `SUMMARY`, `F209`) · `Appendix` (source `EXERCISES` `F210` + the trailing `NOTE` page `F211`).
- **No style is re-declared:** `0` occurrences of `ParagraphStyle` and `0` of `fontName` in the script; its only imports are `os`, `sys`, `neet_template` (names + `figure as _shared_figure`) and `reportlab.platypus`'s `Paragraph`/`Spacer`. No colour, geometry, margin or font constant is defined locally.
- **PDF: 14 pages, A4 portrait, 1,657 KB, 7 embedded images, 31,149 extracted characters (pymupdf)**, pymupdf text SHA-256 (first 16) `f4850a48c881f3b3`. *(Corrected at Gate 3(b), 2026-09-01 — D1. This record originally read `31,137` / `08d68d03f8d3c05f`, which was true when Pass 2 wrote it but was left stale by commit `957c1dd`, which applied the two Pass 3(a) D1 string fixes `SS19.2`→`Section 19.2` and `SS19.2.5`→`Section 19.2.5` (+6 chars each, +12 total: 31,137 + 12 = 31,149) and rebuilt the PDF without updating this line. The extractor is now named because a bare char count without its extractor is what made Ch16 ambiguous; pdfplumber reads 31,422 / `4297a27a6e8b6a98` on the same file.)*
- **218/218 rows ticked in this file** as each was written — ticked while writing, not reconciled afterwards. All 7 plates sit inside the section that cites them, each followed by a "Read the plate" NOTE that names its in-figure labels verbatim, which is how the 38 matrix labels reach the running text.

### Disposition of the eight Pass 1 carry-forwards

Each was honoured in the script; none was re-litigated and no frozen row was edited.

1. Greek glyphs — running text spells the islet cells `alpha-cells` / `beta-cells` with a NOTE recording that the source prints `α` / `β`; ionic charges use ReportLab `<super>` tags, never Unicode superscripts (check 5 stays green).
2. All five source spellings printed as the source prints them and flagged in place — `sella tursica` (`F039`), `Exopthalmic goitre` (`F087`), `pupilary dilation` (`F121`/`F125`), `glucagons` (`F153`), `Diagramatic` in the Figure 19.5 captions (`F208`), while the 19.2/19.3/19.4 captions keep the source's correct `Diagrammatic`.
3. §19.2.7 is set as ordinary body text — the source's page-6 italics are a typesetting accident and were not reproduced.
4. The single exercise gap, Q1(a) `Exocrine gland`, is closed in §19.1 beside `F013`, phrased only from the chapter's own ductless-vs-duct-bearing contrast and **labelled as an addition** (Rules 2 and 5).
5. Both Figure 19.5 panels sit inside §19.4, so Q8's answer (prose + `F217`'s labels) is not split.
6. The body keeps `atrial wall` and `gastro-intestinal tract`; the exercises' shorter `Atrium` / `G-I Tract` appear only in the appendix.
7. All **38** figure labels appear in the running text (check 6 confirms 38/38).
8. Figure 19.4 ships as the single combined plate `fig_19_4.png` and is read in one note.

### Gate 2 (linter) — `check_pdf.py --strict` exit 0, re-verified 2026-09-01

Command, from the repo root, with the §0.2 venv interpreter (rebuilt this session because `/vercel/share/neetenv` was absent — the expected post-session state, checked **before** any diagnosis):

```bash
/vercel/share/neetenv/bin/python check_pdf.py --strict "notes/class 11/Ch19_ChemicalCoordinationAndIntegration"
```

| # | Check | Result |
|---|---|---|
| 1 | Footer/header band | PASS — no text in the top/bottom 1.4 cm margin bands |
| 2 | Legibility floor | PASS — smallest rendered glyph **6.0 pt** (FAIL < 5.0, WARN < 6.0) |
| 3 | Grayscale-only images | PASS — all **7** embedded images monochrome |
| 4 | No person image embedded | PASS — the manifest has no such row (a true negative: Ch19 has no scientist panel) |
| 5 | Banned glyphs | PASS — no Unicode arrows, sub/superscripts, Greek letters or emoji in the text stream |
| 6 | Figure-label coverage | PASS — **38/38** labels fully in text; 0 partial; 0 missing |
| 7 | Frozen inventory ticked | PASS — all **218** Facts rows ticked |
| 8 | Page geometry | PASS — all **14** pages A4 upright (595×842 pt) |
| 9 | Orphaned headings | PASS — **57** banner headings all followed by content on their own page |
| 10 | Badge plate / heading collision | PASS — **147** filled plates all clear of their neighbours |

**VERDICT: PASS (0 fail, 0 warn), exit 0 — green under `--strict`, so no warning had to be waived to advance.** This is the ideal condition §6 Gate 2 asks for.

**Reproducibility (checked here, not deferred to Gate 3):** the committed PDF was copied aside, the script re-run from a clean copy of the chapter folder, and the two compared — **14 pages / 31,149 chars / 7 images / pymupdf text SHA `f4850a48c881f3b3` on both** *(re-confirmed at Gate 3(b), 2026-09-01; the fingerprint originally recorded here — `31,137` / `08d68d03f8d3c05f` — was superseded by commit `957c1dd`, see the PDF line above)*. The committed PDF was then restored byte-for-byte, so the rebuild check left no diff.

### What Gate 2 does NOT claim

Gate 2 is the **mechanical** gate. It says nothing about content fidelity or page layout, and Ch9 was fully green under `--strict` with three real content defects present — so nothing here may stand in for the Pass 3 read.

- **Pass 3(b) has not been run.** No bidirectional full read (inventory → script, source → inventory) exists for this chapter, so `MISSING` / `FABRICATED` / `DRIFTED` / `UNINVENTORIED` are all **undetermined**, not zero.
- **Pass 3(a) has not been run.** Only pages **1, 4, 8, 12 and 14** were spot-rendered while building; the other **9 of 14** pages have not been looked at by a human eye and must not be treated as layout-verified.
- **Gate 3 is OPEN and this chapter is counted in no completion tally.** Gate 2 green is not chapter closure.

*(The second bullet above is the state Pass 2 left behind; it was superseded on 2026-09-01 by the record below, which closes Pass 3(a) over all 14 pages. The first and third bullets still stand.)*

## Gate 3(a) record — visual render check (2026-09-01)

§6 Pass 3(a) asks for two things: **every page rendered and looked at directly**, and **cross-page style consistency** confirmed by pulling one instance of each element type from at least three different points in the chapter. Both were done on the **committed PDF** (not a fresh build), under the §0.2 venv interpreter.

### Coverage — 14 of 14 pages inspected, not spot-checked

Every page was rendered with `pymupdf` and opened individually (`scratch/ch19_gate3a_recheck/r01.png` … `r14.png`), plus a true-print-DPI 1-bit threshold render of each page for the B&W consistency read. **14/14 pages inspected; 0 pages inferred from a neighbour.**

| Page | What is on it | Layout verdict |
|---|---|---|
| 1 | Title · intro · chapter-map table · §19.1 banner + duct table · §19.2 banner | clean |
| 2 | §19.2 prose · Figure 19.1 plate + caption + label read · §19.2.1 banner | clean |
| 3 | Hypothalamic-hormone table · 4-step flow · §19.2.2 banner + pituitary-division table | clean, short foot (see benign observations) |
| 4 | Figure 19.2 plate + caption + label read · GH-error table · anterior-hormone table | clean |
| 5 | Anterior table continues · posterior-hormone table · §19.2.3 · §19.2.4 | clean |
| 6 | Figure 19.3 (a) and (b) plates, each with caption + label read · iodine/hormone table | clean |
| 7 | Hyperthyroid table · thyroid-hormone list · §19.2.5 + PTH flow · §19.2.6 · §19.2.7 | clean |
| 8 | Figure 19.4 combined plate + caption + label read · medulla band + catecholamine table | clean |
| 9 | Cortex band + corticoid table · aldosterone flow · §19.2.8 + islet table · glucagon flow | clean |
| 10 | Glucagon flow continues · insulin flow · §19.2.9 · §19.2.10 + ovary cycle flow | clean |
| 11 | Ovary flow continues · estrogen/progesterone table · §19.3 + ANF flow + GI table · §19.4 | clean |
| 12 | Receptor-class table · 4-step flow · chemical-nature table · Figure 19.5 (a) plate | clean |
| 13 | Figure 19.5 (a) label read · Figure 19.5 (b) plate + caption + label read · Recap band | clean |
| 14 | Recap list continues · Appendix band + exercise-term table · closing panel | clean, short foot (last page) |

### Geometry, machine-re-derived on the same file

| Measure | Result |
|---|---|
| Page size | **14/14** at 595×842 pt, upright |
| Lowest text baseline anywhere | **792.9 pt** on page 10, against a bottom band starting at **802.3 pt** — no page reaches the band |
| Highest text top anywhere | **45.1 pt**, against a top band ending at **39.7 pt** |
| Smallest glyph | **6.0 pt** — the T3/T4 and IP3 subscripts only, set by the template, legible in the 1-bit render |
| Figure aspect fidelity | **7/7** plates placed at their native ratio, largest deviation **0.00000** — nothing squashed or stretched |
| Plate colour | **7/7** single-channel |

### Cross-page style consistency — one signature per element type

Element instances were pulled by span attributes (font · size · colour) from across the chapter, not eyeballed in isolation:

| Element type | Signature | Instances / where |
|---|---|---|
| H1 chapter title | `Times-Bold` 20.0 pt | 1 · p1 |
| §-level banner | `Times-Bold` 10.5 pt reversed | 7 · pp. 1, 11, 13, 14 |
| Sub-banner + table header cells | `Times-Bold` 9.5 pt reversed | 63 · pp. 1–14 |
| Mid-level band (medulla / cortex) | `Times-Bold` 9.0 pt reversed | 2 · pp. 8, 9 |
| Section-number chip | `Times-Bold` 6.21 pt (§) and 6.0 pt (§.§) reversed | 6 + 12 · pp. 1–14 |
| Step badge | `Times-Bold` 8.0 pt reversed | 33 · pp. 3, 7, 9, 10, 11, 12 |
| NOTE lead-in | `Times-BoldItalic` 10.2 pt | 11 pages |
| MEMORY AID lead-in | `Times-BoldItalic` 10.2 pt | 8 pages |
| Figure caption | `Times-Italic` 9.5 pt | 7 captions across 6 pages |

**Every element type resolves to exactly one signature.** Frame alignment matches too: the banner band, the NOTE panel fill and the MEMORY AID panel fill all run **48.5 → 558.8 pt**, so the three panel types share one frame edge on every page they appear. This is the expected outcome of importing styles from `neet_template.py` — the check confirms the template held rather than hunting hand-typed drift.

### Defects found

**Zero confirmed layout defects.** No overflow, no clipping, no table running off the frame, no orphaned heading, no flow rule misaligned with its badges, no figure at the wrong ratio. The two cross-reference wordings corrected in the previous session render as intended — the Figure 19.1 memory aid now points at **Section 19.2** and the Figure 19.3 (b) label read at **Section 19.2.5**.

**Benign observations, deliberately not "fixed":**

- **Page 3 ends at 546 pt** because Figure 19.2's plate travels with its caption and label read as one unit and would not fit; it opens page 4 instead. Breaking that unit to fill page 3 would separate a plate from its caption, which §4.4 forbids.
- **Page 14 ends at 496 pt** — it is the last page.
- **The cyclic-flow marker prints above step 1** of the ovary cycle (p10). That is `process_flow(cyclic=True)` in `neet_template.py` placing the loop-back note at the head of the flow; it is template behaviour shared by every chapter, not chapter-local drift.

### What Gate 3(a) does NOT claim

**Pass 3(a) is the layout half of Gate 3 only.** It looks at pages, not at meaning — a page can be typographically perfect and still carry a drifted qualifier or be missing an NCERT sentence entirely.

*The three bullets below are kept as written for history but are **now superseded** — Pass 3(b) has since run and closed with zero confirmed defects (see `## Gate 3(b) record — CLOSED`). The point that still holds is the first one: no coverage score stood in for the read; a full bidirectional read was performed.*

- ~~**Pass 3(b) has still not been run.**~~ Superseded — the bidirectional full read ran 2026-09-01 with 0 confirmed content defects; see the record below.
- **No coverage percentage or text-match score anywhere in this file may close Gate 3.** §6's hard bar stands — and it was met by a real read, not a score.
- ~~**Gate 3 is therefore still OPEN, and Ch19 belongs in no completion tally.**~~ Superseded — the verdict for this chapter is now *Gate 1 closed · Gate 2 closed · Gate 3(a) closed · Gate 3(b) closed · **FULLY COMPLETE***.

## Gate 3(b) record — CLOSED (2026-09-01; real gate re-confirmed 2026-09-02)

Bidirectional full read + zero confirmed defects. Full log: `scratch/ch19_gate3b/FINDINGS.md`. Merged here from `CHAPTER_STATUS.md`'s `### Gate 3 — closed 2026-09-01` so the chapter's own inventory carries the closure record (the §0.5 convention every closed chapter follows).

- **Re-derivation (Gate 1 closure rule 1).** All counts re-parsed from disk: 218 rows `F001`–`F218` contiguous/monotonic/0-dupes, 218/218 ticked, type census sums to 218 (9 lowercase values), 7 label-bearing figures / 38 labels / 0 doubling / 0 phantom, 14 A4-upright pages, 7 mono images. All confirmed.
- **Gate 2 re-confirmed.** `check_pdf.py --strict` exits 0 — 0 fail / 0 warn, all 10 checks green. Rebuild is content-identical to the committed PDF (14 pp / 31,149 chars / 7 img / pymupdf SHA `f4850a48c881f3b3`). Re-run 2026-09-02 for this reconciliation returned the same clean verdict.
- **Direction 1 (inventory → source).** Coverage screen flagged 10 rows; a full read confirmed **all 10 are false positives** — function words / inflections the token screen cannot match (`hand`, `originating`, `region`, `due`, `characterised`, `another`, `suppresses`, `interact` ×2) plus the intentional `SUMMARY`→`Recap` section rename (`F209`). Every flagged wording was verified present in the source. **0 MISSING / 0 FABRICATED / 0 DRIFTED.**
- **Direction 2 (source → inventory).** All 14 source pages read sentence-by-sentence against the citing inventory rows; every source sentence maps to a row, including the 3 SUMMARY-UNIQUE folds (`F125`/`F179`/`F191`) and all section headings (`EXERCISES` `F210`, `NOTE` `F211`). **0 UNINVENTORIED.**
- **Confirmed defects: content 0; documentation 2 — both fixed at closure.** D1: the Gate 2 fingerprint (`31,137` / `08d68d03f8d3c05f`) was stale after commit `957c1dd` applied the two Pass 3(a) string fixes (+12 chars) — corrected to `31,149` / pymupdf `f4850a48c881f3b3`. D2: stale roll-up wording corrected.
- **Roll-up.** Ch19 counts as ✅ FULLY COMPLETE — CLOSED.
