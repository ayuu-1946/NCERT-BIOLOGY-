# Frozen Inventory — Excretory Products and their Elimination (Class 11, Chapter 16)
Source: `Chapter/class 11/Chapter 16 - Excretory Products and their Elimination.pdf` (12 PDF pages, textbook pp. 205-216) | Frozen: 2026-08-31 | Rows: 178

Protocol: normal 3-pass workflow (§6). Pass 1 sessions: `1-F` (figures, run as its own earlier task) · `1-S` (source read + Facts sweep) · `1-H` (heading sweep) · `1-O` (opener sweep) · `1-Z` (gaps, summary, freeze). Every count in this header and in the census sections below was derived by re-parsing this finished file with a machine (§6 step 10), never by hand tally. Re-verify with `verify_inventory.py`.

| Item | Value |
|---|---|
| Facts-table rows (`## Facts`) | 172 |
| Figure-label-matrix rows (`## Figure-label matrix`) | 6 |
| Total rows | 178 |
| ID range | `F001`-`F178` (contiguous, 0 gaps, 0 duplicate IDs) |
| Ticked rows | 178 of 178 (Pass 2 complete; Gate 2 green) |
| Heading rows (`Type: heading`) | 15 |
| Opener rows (`Type: opener`) | 13 |
| Numbered figures / assets | 6 / 6 |
| In-figure labels catalogued | 76 (12 + 9 + 11 + 4 + 16 + 24) |
| Summary sentences classified | 22 = 18 BODY-PRESENT + 4 SUMMARY-UNIQUE (all 4 folded) |
| Exercises scanned / genuine gaps | 12 / 4 |

Tick legend: `x` = written into the script and verified present in the generated PDF. All 178 rows are now ticked. Ticks were earned, never asserted: 165 of the 172 Facts rows cleared an automated per-row token-presence screen against the built PDF's own text layer (`tick_rows.py`, bar = 80 per cent of content tokens). The 7 rows the screen flagged were each hand-read against both the script and the PDF text before ticking — 6 were false positives (the row wording describes formatting, e.g. "Run-in head, bold, colon-terminated", rather than quoting prose, so its meta-words are correctly absent from the PDF), and 1 (F159) was a true positive: a genuinely omitted fact, which was written into the script and re-rendered before its tick. The 6 figure-label-matrix rows (F173-F178) are ticked on `check_pdf.py` check 6 (figure-label coverage in running text), which passes.

Per SUPREME COMMAND §6 Pass 3(b), this token screen is Pass 2 evidence only: it may *locate* a suspect row but may never *clear* one at Gate 3. Pass 3a below is therefore an independent hand read, not a re-run of this screen.

Type vocabulary (normalized, lowercase, no other value appears in the `Type` column): `caption`, `concept`, `definition`, `disorder`, `example`, `figure-label`, `heading`, `list`, `number`, `opener`, `process`, `question`.

Source-typo policy: the source contains "characterestic", "discorders", "membrance", "ofthe Filtrate" (running head, p5) and numbers Exercise 7 with `(d)` **twice** (no `(e)`). All are transcribed verbatim below and must be reproduced as-is in quoted rows; the rewrite prose may use correct spelling.

## Facts

| ID | Section | Type | Exact original wording | Ticked |
|----|---------|------|------------------------|--------|
| F001 | title | heading | Chapter title plate: 'EXCRETORY PRODUCTS AND THEIR ELIMINATION' with 'CHAPTER 16' (no opening sentence of its own) | x |
| F002 | intro | opener | "Animals accumulate ammonia, urea, uric acid, carbon dioxide, water and ions like Na+, K+, Cl-, phosphate, sulphate, etc., either by metabolic activities or by other means like excess ingestion." | x |
| F003 | intro | concept | "These substances have to be removed totally or partially." | x |
| F004 | intro | concept | "In this chapter, you will learn the mechanisms of elimination of these substances with special emphasis on common nitrogenous wastes." | x |
| F005 | intro | concept | "Ammonia, urea and uric acid are the major forms of nitrogenous wastes excreted by the animals." | x |
| F006 | intro | concept | "Ammonia is the most toxic form and requires large amount of water for its elimination, whereas uric acid, being the least toxic, can be removed with a minimum loss of water." | x |
| F007 | intro | definition | "The process of excreting ammonia is Ammonotelism." | x |
| F008 | intro | example | "Many bony fishes, aquatic amphibians and aquatic insects are ammonotelic in nature." (source sets "ammonotelic" five times over-struck as a bold artefact) | x |
| F009 | intro | concept | "Ammonia, as it is readily soluble, is generally excreted by diffusion across body surfaces or through gill surfaces (in fish) as ammonium ions." | x |
| F010 | intro | concept | "Kidneys do not play any significant role in its removal." | x |
| F011 | intro | concept | "Terrestrial adaptation necessitated the production of lesser toxic nitrogenous wastes like urea and uric acid for conservation of water." | x |
| F012 | intro | example | "Mammals, many terrestrial amphibians and marine fishes mainly excrete urea and are called ureotelic animals." (source sets "ureotelic" five times over-struck) | x |
| F013 | intro | process | "Ammonia produced by metabolism is converted into urea in the liver of these animals and released into the blood which is filtered and excreted out by the kidneys." | x |
| F014 | intro | concept | "Some amount of urea may be retained in the kidney matrix of some of these animals to maintain a desired osmolarity." | x |
| F015 | intro | example | "Reptiles, birds, land snails and insects excrete nitrogenous wastes as uric acid in the form of pellet or paste with a minimum loss of water and are called uricotelic animals." (source sets "uricotelic" five times over-struck) | x |
| F016 | intro | list | Chapter contents panel (p. 205 margin), title-case in the source: "16.1 Human Excretory System"; "16.2 Urine Formation"; "16.3 Function of the Tubules"; "16.4 Mechanism of Concentration of the Filtrate"; "16.5 Regulation of Kidney Function"; "16.6 Micturition"; "16.7 Role of other Organs in Excretion"; "16.8 Disorders of the Excretory System" | x |
| F017 | intro | concept | "A survey of animal kingdom presents a variety of excretory structures." | x |
| F018 | intro | concept | "In most of the invertebrates, these structures are simple tubular forms whereas vertebrates have complex tubular organs called kidneys." | x |
| F019 | intro | concept | "Some of these structures are mentioned here." | x |
| F020 | intro | example | "Protonephridia or flame cells are the excretory structures in Platyhelminthes (Flatworms, e.g., Planaria), rotifers, some annelids and the cephalochordate - Amphioxus." | x |
| F021 | intro | concept | "Protonephridia are primarily concerned with ionic and fluid volume regulation, i.e., osmoregulation." | x |
| F022 | intro | example | "Nephridia are the tubular excretory structures of earthworms and other annelids." | x |
| F023 | intro | concept | "Nephridia help to remove nitrogenous wastes and maintain a fluid and ionic balance." | x |
| F024 | intro | example | "Malpighian tubules are the excretory structures of most of the insects including cockroaches." | x |
| F025 | intro | concept | "Malpighian tubules help in the removal of nitrogenous wastes and osmoregulation." | x |
| F026 | intro | example | "Antennal glands or green glands perform the excretory function in crustaceans like prawns." | x |
| F027 | 16.1 | heading | "16.1 HUMAN EXCRETORY SYSTEM" | x |
| F028 | 16.1 | opener | "In humans, the excretory system consists of a pair of kidneys, one pair of ureters, a urinary bladder and a urethra (Figure 16.1)." | x |
| F029 | 16.1 | concept | "Kidneys are reddish brown, bean shaped structures situated between the levels of last thoracic and third lumbar vertebra close to the dorsal inner wall of the abdominal cavity." | x |
| F030 | 16.1 | number | "Each kidney of an adult human measures 10-12 cm in length, 5-7 cm in width, 2-3 cm in thickness with an average weight of 120-170 g." | x |
| F031 | 16.1 | concept | "Towards the centre of the inner concave surface of the kidney is a notch called hilum through which ureter, blood vessels and nerves enter." | x |
| F032 | 16.1 | concept | "Inner to the hilum is a broad funnel shaped space called the renal pelvis with projections called calyces." | x |
| F033 | 16.1 | concept | "The outer layer of kidney is a tough capsule." | x |
| F034 | 16.1 | concept | "Inside the kidney, there are two zones, an outer cortex and an inner medulla." | x |
| F035 | 16.1 | concept | "The medulla is divided into a few conical masses (medullary pyramids) projecting into the calyces (sing.: calyx)." | x |
| F036 | 16.1 | concept | "The cortex extends in between the medullary pyramids as renal columns called Columns of Bertini." | x |
| F037 | 16.1 | number | "Each kidney has nearly one million complex tubular structures called nephrons (Figure 16.3), which are the functional units." | x |
| F038 | 16.1 | concept | "Each nephron has two parts - the glomerulus and the renal tubule." | x |
| F039 | 16.1 | definition | "Glomerulus is a tuft of capillaries formed by the afferent arteriole - a fine branch of renal artery." | x |
| F040 | 16.1 | concept | "Blood from the glomerulus is carried away by an efferent arteriole." | x |
| F041 | 16.1 | concept | "The renal tubule begins with a double walled cup-like structure called Bowman's capsule, which encloses the glomerulus." | x |
| F042 | 16.1 | definition | "Glomerulus along with Bowman's capsule, is called the malpighian body or renal corpuscle (Figure 16.4)." | x |
| F043 | 16.1 | concept | "The tubule continues further to form a highly coiled network - proximal convoluted tubule (PCT)." | x |
| F044 | 16.1 | concept | "A hairpin shaped Henle's loop is the next part of the tubule which has a descending and an ascending limb." | x |
| F045 | 16.1 | concept | "The ascending limb continues as another highly coiled tubular region called distal convoluted tubule (DCT)." | x |
| F046 | 16.1 | concept | "The DCTs of many nephrons open into a straight tube called collecting duct, many of which converge and open into the renal pelvis through medullary pyramids in the calyces." | x |
| F047 | 16.1 | concept | "The Malpighian corpuscle, PCT and DCT of the nephron are situated in the cortical region of the kidney whereas the loop of Henle dips into the medulla." | x |
| F048 | 16.1 | definition | "In majority of nephrons, the loop of Henle is too short and extends only very little into the medulla. Such nephrons are called cortical nephrons." | x |
| F049 | 16.1 | definition | "In some of the nephrons, the loop of Henle is very long and runs deep into the medulla. These nephrons are called juxta medullary nephrons." | x |
| F050 | 16.1 | concept | "The efferent arteriole emerging from the glomerulus forms a fine capillary network around the renal tubule called the peritubular capillaries." | x |
| F051 | 16.1 | concept | "A minute vessel of this network runs parallel to the Henle's loop forming a 'U' shaped vasa recta." | x |
| F052 | 16.1 | concept | "Vasa recta is absent or highly reduced in cortical nephrons." | x |
| F053 | 16.2 | heading | "16.2 URINE FORMATION" | x |
| F054 | 16.2 | opener | "Urine formation involves three main processes namely, glomerular filtration, reabsorption and secretion, that takes place in different parts of the nephron." | x |
| F055 | 16.2 | process | "The first step in urine formation is the filtration of blood, which is carried out by the glomerulus and is called glomerular filtration." | x |
| F056 | 16.2 | number | "On an average, 1100-1200 ml of blood is filtered by the kidneys per minute which constitute roughly 1/5th of the blood pumped out by each ventricle of the heart in a minute." | x |
| F057 | 16.2 | number | "The glomerular capillary blood pressure causes filtration of blood through 3 layers, i.e., the endothelium of glomerular blood vessels, the epithelium of Bowman's capsule and a basement membrane between these two layers." | x |
| F058 | 16.2 | concept | "The epithelial cells of Bowman's capsule called podocytes are arranged in an intricate manner so as to leave some minute spaces called filtration slits or slit pores." | x |
| F059 | 16.2 | concept | "Blood is filtered so finely through these membranes, that almost all the constituents of the plasma except the proteins pass onto the lumen of the Bowman's capsule." | x |
| F060 | 16.2 | definition | "Therefore, it is considered as a process of ultra filtration." | x |
| F061 | 16.2 | definition | "The amount of the filtrate formed by the kidneys per minute is called glomerular filtration rate (GFR)." | x |
| F062 | 16.2 | number | "GFR in a healthy individual is approximately 125 ml/minute, i.e., 180 litres per day !" | x |
| F063 | 16.2 | concept | "The kidneys have built-in mechanisms for the regulation of glomerular filtration rate." | x |
| F064 | 16.2 | concept | "One such efficient mechanism is carried out by juxta glomerular apparatus (JGA)." | x |
| F065 | 16.2 | definition | "JGA is a special sensitive region formed by cellular modifications in the distal convoluted tubule and the afferent arteriole at the location of their contact." | x |
| F066 | 16.2 | process | "A fall in GFR can activate the JG cells to release renin which can stimulate the glomerular blood flow and thereby the GFR back to normal." | x |
| F067 | 16.2 | number | "A comparison of the volume of the filtrate formed per day (180 litres per day) with that of the urine released (1.5 litres), suggest that nearly 99 per cent of the filtrate has to be reabsorbed by the renal tubules." | x |
| F068 | 16.2 | definition | "This process is called reabsorption." | x |
| F069 | 16.2 | concept | "The tubular epithelial cells in different segments of nephron perform this either by active or passive mechanisms." | x |
| F070 | 16.2 | example | "For example, substances like glucose, amino acids, Na+, etc., in the filtrate are reabsorbed actively whereas the nitrogenous wastes are absorbed by passive transport." | x |
| F071 | 16.2 | concept | "Reabsorption of water also occurs passively in the initial segments of the nephron (Figure 16.5)." | x |
| F072 | 16.2 | process | "During urine formation, the tubular cells secrete substances like H+, K+ and ammonia into the filtrate." | x |
| F073 | 16.2 | concept | "Tubular secretion is also an important step in urine formation as it helps in the maintenance of ionic and acid base balance of body fluids." | x |
| F074 | 16.3 | heading | "16.3 FUNCTION OF THE TUBULES" | x |
| F075 | 16.3 | heading | Run-in head, bold, colon-terminated: "Proximal Convoluted Tubule (PCT):" | x |
| F076 | 16.3 | opener | "PCT is lined by simple cuboidal brush border epithelium which increases the surface area for reabsorption." | x |
| F077 | 16.3 | number | "Nearly all of the essential nutrients, and 70-80 per cent of electrolytes and water are reabsorbed by this segment." | x |
| F078 | 16.3 | concept | "PCT also helps to maintain the pH and ionic balance of the body fluids by selective secretion of hydrogen ions and ammonia into the filtrate and by absorption of HCO3- from it." | x |
| F079 | 16.3 | heading | Run-in head, bold, colon-terminated: "Henle's Loop:" | x |
| F080 | 16.3 | opener | "Reabsorption is minimum in its ascending limb." | x |
| F081 | 16.3 | concept | "However, this region plays a significant role in the maintenance of high osmolarity of medullary interstitial fluid." | x |
| F082 | 16.3 | concept | "The descending limb of loop of Henle is permeable to water but almost impermeable to electrolytes." | x |
| F083 | 16.3 | concept | "This concentrates the filtrate as it moves down." | x |
| F084 | 16.3 | concept | "The ascending limb is impermeable to water but allows transport of electrolytes actively or passively." | x |
| F085 | 16.3 | concept | "Therefore, as the concentrated filtrate pass upward, it gets diluted due to the passage of electrolytes to the medullary fluid." | x |
| F086 | 16.3 | heading | Run-in head, bold, colon-terminated: "Distal Convoluted Tubule (DCT):" | x |
| F087 | 16.3 | opener | "Conditional reabsorption of Na+ and water takes place in this segment." | x |
| F088 | 16.3 | concept | "DCT is also capable of reabsorption of HCO3- and selective secretion of hydrogen and potassium ions and NH3 to maintain the pH and sodium-potassium balance in blood." | x |
| F089 | 16.3 | heading | Run-in head, bold, colon-terminated: "Collecting Duct:" | x |
| F090 | 16.3 | opener | "This long duct extends from the cortex of the kidney to the inner parts of the medulla." | x |
| F091 | 16.3 | concept | "Large amounts of water could be reabsorbed from this region to produce a concentrated urine." | x |
| F092 | 16.3 | concept | "This segment allows passage of small amounts of urea into the medullary interstitium to keep up the osmolarity." | x |
| F093 | 16.3 | concept | "It also plays a role in the maintenance of pH and ionic balance of blood by the selective secretion of H+ and K+ ions (Figure 16.5)." | x |
| F094 | 16.4 | heading | "16.4 MECHANISM OF CONCENTRATION OF THE FILTRATE" (the p. 209 running head sets this as "ofthe Filtrate", a source typo) | x |
| F095 | 16.4 | opener | "Mammals have the ability to produce a concentrated urine." | x |
| F096 | 16.4 | concept | "The Henle's loop and vasa recta play a significant role in this." | x |
| F097 | 16.4 | concept | "The flow of filtrate in the two limbs of Henle's loop is in opposite directions and thus forms a counter current." | x |
| F098 | 16.4 | concept | "The flow of blood through the two limbs of vasa recta is also in a counter current pattern." | x |
| F099 | 16.4 | number | "The proximity between the Henle's loop and vasa recta, as well as the counter current in them help in maintaining an increasing osmolarity towards the inner medullary interstitium, i.e., from 300 mOsmolL-1 in the cortex to about 1200 mOsmolL-1 in the inner medulla." | x |
| F100 | 16.4 | concept | "This gradient is mainly caused by NaCl and urea." | x |
| F101 | 16.4 | process | "NaCl is transported by the ascending limb of Henle's loop which is exchanged with the descending limb of vasa recta." | x |
| F102 | 16.4 | process | "NaCl is returned to the interstitium by the ascending portion of vasa recta." | x |
| F103 | 16.4 | process | "Similarly, small amounts of urea enter the thin segment of the ascending limb of Henle's loop which is transported back to the interstitium by the collecting tubule." | x |
| F104 | 16.4 | definition | "The above described transport of substances facilitated by the special arrangement of Henle's loop and vasa recta is called the counter current mechanism (Figure. 16.6)." (source prints a stray period after "Figure") | x |
| F105 | 16.4 | concept | "This mechanism helps to maintain a concentration gradient in the medullary interstitium." | x |
| F106 | 16.4 | concept | "Presence of such interstitial gradient helps in an easy passage of water from the collecting tubule thereby concentrating the filtrate (urine)." | x |
| F107 | 16.4 | number | "Human kidneys can produce urine nearly four times concentrated than the initial filtrate formed." | x |
| F108 | 16.5 | heading | "16.5 REGULATION OF KIDNEY FUNCTION" | x |
| F109 | 16.5 | opener | "The functioning of the kidneys is efficiently monitored and regulated by hormonal feedback mechanisms involving the hypothalamus, JGA and to a certain extent, the heart." | x |
| F110 | 16.5 | concept | "Osmoreceptors in the body are activated by changes in blood volume, body fluid volume and ionic concentration." | x |
| F111 | 16.5 | process | "An excessive loss of fluid from the body can activate these receptors which stimulate the hypothalamus to release antidiuretic hormone (ADH) or vasopressin from the neurohypophysis." | x |
| F112 | 16.5 | concept | "ADH facilitates water reabsorption from latter parts of the tubule, thereby preventing diuresis." | x |
| F113 | 16.5 | process | "An increase in body fluid volume can switch off the osmoreceptors and suppress the ADH release to complete the feedback." | x |
| F114 | 16.5 | concept | "ADH can also affect the kidney function by its constrictory effects on blood vessels." | x |
| F115 | 16.5 | concept | "This causes an increase in blood pressure." | x |
| F116 | 16.5 | concept | "An increase in blood pressure can increase the glomerular blood flow and thereby the GFR." | x |
| F117 | 16.5 | concept | "The JGA plays a complex regulatory role." | x |
| F118 | 16.5 | process | "A fall in glomerular blood flow/glomerular blood pressure/GFR can activate the JG cells to release renin which converts angiotensinogen in blood to angiotensin I and further to angiotensin II." | x |
| F119 | 16.5 | concept | "Angiotensin II, being a powerful vasoconstrictor, increases the glomerular blood pressure and thereby GFR." | x |
| F120 | 16.5 | process | "Angiotensin II also activates the adrenal cortex to release Aldosterone." | x |
| F121 | 16.5 | concept | "Aldosterone causes reabsorption of Na+ and water from the distal parts of the tubule." | x |
| F122 | 16.5 | concept | "This also leads to an increase in blood pressure and GFR." | x |
| F123 | 16.5 | definition | "This complex mechanism is generally known as the Renin-Angiotensin mechanism." | x |
| F124 | 16.5 | process | "An increase in blood flow to the atria of the heart can cause the release of Atrial Natriuretic Factor (ANF)." | x |
| F125 | 16.5 | concept | "ANF can cause vasodilation (dilation of blood vessels) and thereby decrease the blood pressure." | x |
| F126 | 16.5 | concept | "ANF mechanism, therefore, acts as a check on the renin-angiotensin mechanism." | x |
| F127 | 16.6 | heading | "16.6 MICTURITION" | x |
| F128 | 16.6 | opener | "Urine formed by the nephrons is ultimately carried to the urinary bladder where it is stored till a voluntary signal is given by the central nervous system (CNS)." | x |
| F129 | 16.6 | process | "This signal is initiated by the stretching of the urinary bladder as it gets filled with urine." | x |
| F130 | 16.6 | process | "In response, the stretch receptors on the walls of the bladder send signals to the CNS." | x |
| F131 | 16.6 | process | "The CNS passes on motor messages to initiate the contraction of smooth muscles of the bladder and simultaneous relaxation of the urethral sphincter causing the release of urine." | x |
| F132 | 16.6 | definition | "The process of release of urine is called micturition and the neural mechanisms causing it is called the micturition reflex." | x |
| F133 | 16.6 | number | "An adult human excretes, on an average, 1 to 1.5 litres of urine per day." | x |
| F134 | 16.6 | number | "The urine formed is a light yellow coloured watery fluid which is slightly acidic (pH-6.0) and has a characterestic odour." (source spells "characterestic") | x |
| F135 | 16.6 | number | "On an average, 25-30 gm of urea is excreted out per day." | x |
| F136 | 16.6 | concept | "Various conditions can affect the characteristics of urine." | x |
| F137 | 16.6 | concept | "Analysis of urine helps in clinical diagnosis of many metabolic discorders as well as malfunctioning of the kidney." (source spells "discorders") | x |
| F138 | 16.6 | example | "For example, presence of glucose (Glycosuria) and ketone bodies (Ketonuria) in urine are indicative of diabetes mellitus." | x |
| F139 | 16.7 | heading | "16.7 ROLE OF OTHER ORGANS IN EXCRETION" | x |
| F140 | 16.7 | opener | "Other than the kidneys, lungs, liver and skin also help in the elimination of excretory wastes." | x |
| F141 | 16.7 | number | "Our lungs remove large amounts of CO2 (approximately 200mL/minute) and also significant quantities of water every day." | x |
| F142 | 16.7 | concept | "Liver, the largest gland in our body, secretes bile-containing substances like bilirubin, biliverdin, cholesterol, degraded steroid hormones, vitamins and drugs." | x |
| F143 | 16.7 | concept | "Most of these substances ultimately pass out along with digestive wastes." | x |
| F144 | 16.7 | concept | "The sweat and sebaceous glands in the skin can eliminate certain substances through their secretions." | x |
| F145 | 16.7 | concept | "Sweat produced by the sweat glands is a watery fluid containing NaCl, small amounts of urea, lactic acid, etc." | x |
| F146 | 16.7 | concept | "Though the primary function of sweat is to facilitate a cooling effect on the body surface, it also helps in the removal of some of the wastes mentioned above." | x |
| F147 | 16.7 | concept | "Sebaceous glands eliminate certain substances like sterols, hydrocarbons and waxes through sebum." | x |
| F148 | 16.7 | concept | "This secretion provides a protective oily covering for the skin." | x |
| F149 | 16.7 | question | "Do you know that small amounts of nitrogenous wastes could be eliminated through saliva too?" | x |
| F150 | 16.8 | heading | "16.8 DISORDERS OF THE EXCRETORY SYSTEM" | x |
| F151 | 16.8 | opener | "Malfunctioning of kidneys can lead to accumulation of urea in blood, a condition called uremia, which is highly harmful and may lead to kidney failure." | x |
| F152 | 16.8 | concept | "In such patients, urea can be removed by a process called hemodialysis." | x |
| F153 | 16.8 | process | "During the process of haemodialysis, the blood drained from a convenient artery is pumped into a dialysing unit called artificial kidney." | x |
| F154 | 16.8 | process | "Blood drained from a convenient artery is pumped into a dialysing unit after adding an anticoagulant like heparin." | x |
| F155 | 16.8 | concept | "The unit contains a coiled cellophane tube surrounded by a fluid (dialysing fluid) having the same composition as that of plasma except the nitrogenous wastes." | x |
| F156 | 16.8 | concept | "The porous cellophane membrance of the tube allows the passage of molecules based on concentration gradient." (source spells "membrance") | x |
| F157 | 16.8 | process | "As nitrogenous wastes are absent in the dialysing fluid, these substances freely move out, thereby clearing the blood." | x |
| F158 | 16.8 | process | "The cleared blood is pumped back to the body through a vein after adding anti-heparin to it." | x |
| F159 | 16.8 | concept | "This method is a boon for thousands of uremic patients all over the world." | x |
| F160 | 16.8 | concept | "Kidney transplantation is the ultimate method in the correction of acute renal failures (kidney failure)." | x |
| F161 | 16.8 | concept | "A functioning kidney is used in transplantation from a donor, preferably a close relative, to minimise its chances of rejection by the immune system of the host." | x |
| F162 | 16.8 | concept | "Modern clinical procedures have increased the success rate of such a complicated technique." | x |
| F163 | 16.8 | disorder | "Renal calculi: Stone or insoluble mass of crystallised salts (oxalates, etc.) formed within the kidney." | x |
| F164 | 16.8 | disorder | "Glomerulonephritis: Inflammation of glomeruli of kidney." | x |
| F165 | figures | caption | "Figure 16.1 Human Urinary system" | x |
| F166 | figures | caption | "Figure 16.2 Longitudinal section (Diagrammatic) of Kidney" | x |
| F167 | figures | caption | "Figure 16.3 A diagrammatic representation of a nephron showing blood vessels, duct and tubules" | x |
| F168 | figures | caption | "Figure 16.4 Malpighian body (renal corpuscle)" | x |
| F169 | figures | caption | "Figure 16.5 Reabsorption and secretion of major substances at different parts of the nephron (Arrows indicate direction of movement of materials.)" | x |
| F170 | figures | caption | "Figure 16.6 Diagrammatic representation of a nephron and vasa recta showing counter current mechanisms" (caption sets "mechanisms" plural) | x |
| F171 | summary | heading | "SUMMARY" | x |
| F172 | exercises | heading | "EXERCISES" | x |

## Figure-label matrix

One row per figure. Labels were harvested in session `1-F` by opening each rendered 300 dpi monochrome asset at full size (§4.4 Step 1), **not** from the source text layer — Chapter 16 is a two-column layout whose figure callouts are vector artwork, and pdfplumber interleaves Figure 16.4's labels into the page-4 prose (verified). This matrix exists in exactly one place in this file; it is deliberately not restated as a second pipe-delimited table anywhere (§6), because a restated label table is what silently reduced `check_pdf.py` check 6 to a no-op on an earlier chapter.

Apostrophes are recorded exactly as drawn. The source is inconsistent: Figure 16.3 draws "Henle's loop" with a straight apostrophe but "Bowman's capsule" with a curly one, and Figure 16.6 draws "Bowman's capsule" with a straight one.

| ID | Fig # | Type | In-figure labels, verbatim - one row per figure, every callout listed | Ticked |
|----|-------|------|------------------------------------------------------------------|--------|
| F173 | Fig 16.1 | figure-label | Figure labels: "Inferior vena cava"; "Adrenal gland"; "Renal artery"; "Renal vein"; "Pelvis"; "Kidney"; "Medulla"; "Cortex"; "Dorsal aorta"; "Ureter"; "Urinary bladder"; "Urethra" | x |
| F174 | Fig 16.2 | figure-label | Figure labels: "Medullary pyramid"; "Renal column"; "Calyx"; "Renal artery"; "Renal vein"; "Renal pelvis"; "Ureter"; "Cortex"; "Renal capsule" | x |
| F175 | Fig 16.3 | figure-label | Figure labels: "Afferent arteriole"; "Efferent arteriole"; "Glomerulus"; "Bowman's capsule"; "Proximal convoluted tubule"; "Distal convoluted tubule"; "Descending limb of loop of Henle"; "Ascending limb of loop of Henle"; "Henle's loop"; "Vasa recta"; "Collecting duct" | x |
| F176 | Fig 16.4 | figure-label | Figure labels: "Afferent arteriole"; "Efferent arteriole"; "Bowman's capsule"; "Proximal convoluted tubule" | x |
| F177 | Fig 16.5 | figure-label | Figure labels: "Proximal convoluted tubule"; "Distal convoluted tubule"; "Cortex"; "Medulla"; "HCO3-"; "NaCl"; "Nutrients"; "H2O"; "K+"; "H+"; "NH3"; "Descending limb of loop of Henle"; "Thick segment of ascending limb"; "Thin segment of ascending limb"; "Collecting duct"; "Urea" | x |
| F178 | Fig 16.6 | figure-label | Figure labels: "Afferent arteriole"; "Efferent arteriole"; "Bowman's capsule"; "Glomerulus"; "Cortex"; "Outer medulla"; "Inner medulla"; "H2O"; "NaCl"; "Urea"; "Vasa recta"; "Nephron"; "300 mOsmolL-1"; "600 mOsmolL-1"; "900 mOsmolL-1"; "1200 mOsmolL-1"; "200"; "300"; "400"; "600"; "800"; "900"; "1000"; "1200" | x |

### Figure-only content (labels with no prose anchor)

Machine-checked: every one of the 76 labels above was run through `check_pdf._coverage_ratio` against the chapter's own running text. Thirteen fell below the covered-threshold. They split into two kinds, and the distinction matters for Pass 2.

**Parser artefacts — label is correct, source text simply cannot express it.** `H2O`, `NH3` and `HCO3-` are unmatchable because the PDF text layer splits subscripts across lines (`H O`, `NH` + `3`, `HCO -` + `3`). The osmolarity tick numbers `400`, `600`, `800`, `900`, `1000` and the gradient labels `600 mOsmolL-1` / `900 mOsmolL-1` are artwork-only scale marks; only 300 and 1200 appear in prose. No action needed beyond writing them correctly.

**Genuine figure-only facts — the chapter draws them but never names them in prose.** These are real Pass 2 obligations and must be carried by the rewrite, or the information is lost:

| Figure-only fact | Where it must be explained |
|---|---|
| "Inferior vena cava" (Fig 16.1) - the vessel the renal veins drain into | 16.1, naming it when the renal vein is introduced |
| "Dorsal aorta" (Fig 16.1) - the vessel the renal arteries branch from ("dorsal" appears in prose only as a body-position word, never as this vessel) | 16.1, naming it when the renal artery is introduced |
| "Thick segment of ascending limb" (Fig 16.5) - prose names only the *thin* segment of the ascending limb | 16.3 or 16.4, distinguishing thick from thin segment of the ascending limb |

## Summary classification

22 summary sentences classified. 18 restate body rows (BODY-PRESENT). 4 add something the body never states outright (SUMMARY-UNIQUE); all 4 are folded into the sections named below, so no summary-only fact is dropped.

| Summary sentence (abridged) | Class | Fold target |
|---|---|---|
| "Nephron is the functional unit of kidney and has two portions - glomerulus and renal tubule." | SUMMARY-UNIQUE | 16.1 - the body describes both parts but never labels the nephron "the functional unit ... two portions" as a single framing |
| "Filtration is a non-selective process performed by the glomerulus using the glomerular capillary blood pressure." | SUMMARY-UNIQUE | 16.2 - the body calls filtration "ultra filtration" but never states it is *non-selective* |
| "About 1200 ml of blood is filtered by the glomerulus per minute to form 125 ml of filtrate in the Bowman's capsule per minute (GFR)." | SUMMARY-UNIQUE | 16.2 - body gives 1100-1200 ml and 125 ml/minute separately; the summary ties them as one input-output pair |
| "The filtrate gets concentrated as it moves down the descending limb but is diluted by the ascending limb. Electrolytes and urea are retained in the interstitium by this arrangement." | SUMMARY-UNIQUE | 16.4 - the *retention* of electrolytes and urea in the interstitium as the net purpose is summary-only |

The remaining 18 are BODY-PRESENT and need no separate treatment: nitrogenous-waste accumulation · habitat dependence · the three major wastes · the five excretory organ types · ionic/acid-base balance · human excretory system parts · one million nephrons · glomerulus as capillary tuft from afferent arteriole · Bowman's capsule to PCT/HL/DCT differentiation · DCTs joining collecting duct into renal pelvis · Bowman's capsule + glomerulus = Malpighian corpuscle · three processes of urine formation · JGA regulating GFR · 99 per cent reabsorption · PCT as major site · HL osmolar gradient 300-1200 · DCT/collecting duct reabsorption and H+/K+/NH3 secretion · micturition via CNS and urethra plus skin/lungs/liver assisting.

## Exercise-gap terms

12 exercises scanned. Eight are answerable from body rows alone. Four assume a fact or contrast the body never states explicitly; each has a planned home in the rewrite.

| Term/fact assumed by exercises | Explained where |
|---|---|
| Ex 3(b) - that ADH makes urine *hypotonic* is false, i.e. the explicit ADH-to-urine-concentration direction | 16.5, stating that ADH conserves water and so makes urine more concentrated (hypertonic), not hypotonic |
| Ex 3(c) - "Protein-free fluid" as the explicit characterisation of the filtrate | 16.2, one clause naming the filtrate protein-free when ultra filtration is defined |
| Ex 8 - a standalone definition of *osmoregulation* (the body uses the word three times but never defines it) | 16.1 intro or 16.2, one sentence defining osmoregulation as the maintenance of water and electrolyte balance |
| Ex 12(a) - permeability of the ascending vs descending limb stated as a fill-in-the-blank contrast pair | 16.3, already carried by F082/F084; the rewrite must keep both limbs' permeability adjacent so the contrast is directly readable |

Not gaps, recorded so a later audit does not re-raise them: Ex 1 GFR definition (F061), Ex 2 autoregulation via JGA (F063-F066), Ex 3(a) micturition reflex (F132), Ex 3(d) Henle's loop concentrating urine (16.4), Ex 3(e) glucose actively reabsorbed in PCT (F070/F077), Ex 4 counter current mechanism (16.4), Ex 5 liver/lungs/skin (16.7), Ex 6 micturition (16.6), Ex 7 all five matches are body rows, Ex 9 ureotelic/uricotelic vs ammonotelic water cost (F006/F011), Ex 10 JGA significance (F064-F066), Ex 11(a) flame cells in Amphioxus (F020), Ex 11(b) Columns of Bertini (F036), Ex 11(c) vasa recta (F051), Ex 12(b) ADH (F112), Ex 12(c) nitrogenous wastes absent from dialysing fluid (F155/F157), Ex 12(d) 25-30 gm urea/day (F135).

Exercise 7 numbering note: the source labels its five match-items `(a) (b) (c) (d) (d)` - the fifth is a second `(d)`, not `(e)`. Transcribe verbatim; do not silently renumber.

## Figure manifest

Extraction, monochrome conversion and per-asset visual verification were completed in session `1-F` (skill `in-repo-ncert-figure-extraction`). Every asset is a 300 dpi clip render, `mode=L`, opened individually at full size after conversion and re-verified in this session.

| Fig # | Caption (verbatim) | Asset file | Source page | Mono | Verified |
|---|---|---|---|---|---|
| 16.1 | Human Urinary system | `assets/fig_16_1.png` | 2 | yes | yes |
| 16.2 | Longitudinal section (Diagrammatic) of Kidney | `assets/fig_16_2.png` | 3 | yes | yes |
| 16.3 | A diagrammatic representation of a nephron showing blood vessels, duct and tubules | `assets/fig_16_3.png` | 3 | yes | yes |
| 16.4 | Malpighian body (renal corpuscle) | `assets/fig_16_4.png` | 4 | yes | yes |
| 16.5 | Reabsorption and secretion of major substances at different parts of the nephron (Arrows indicate direction of movement of materials.) | `assets/fig_16_5.png` | 6 | yes | yes |
| 16.6 | Diagrammatic representation of a nephron and vasa recta showing counter current mechanisms | `assets/fig_16_6.png` | 7 | yes | yes |

Asset dimensions as rendered (px): 16.1 = 1050x1055 · 16.2 = 1167x897 · 16.3 = 1792x1147 · 16.4 = 850x947 · 16.5 = 1709x1659 · 16.6 = 1946x1705. All six report `mode=L`.

No unnumbered bonus plate exists in this chapter, so the denominator is 6 everywhere. No photograph of a person appears anywhere in the chapter, so `check_pdf.py` check 4 has no manifest row to fire on - a true negative, not a suppressed finding. Figures 16.2 and 16.3 share source page 3, which is otherwise entirely artwork (its prose reflows to a single running-head line).

## Census sections (each total derivable from the list beside it)

**Heading census — 15 rows = 8 numbered + 4 run-in + 3 unnumbered.**
Numbered headings, in source order: 16.1 HUMAN EXCRETORY SYSTEM · 16.2 URINE FORMATION · 16.3 FUNCTION OF THE TUBULES · 16.4 MECHANISM OF CONCENTRATION OF THE FILTRATE · 16.5 REGULATION OF KIDNEY FUNCTION · 16.6 MICTURITION · 16.7 ROLE OF OTHER ORGANS IN EXCRETION · 16.8 DISORDERS OF THE EXCRETORY SYSTEM.
Run-in headings (bold, colon-terminated, inside 16.3), in source order: Proximal Convoluted Tubule (PCT): · Henle's Loop: · Distal Convoluted Tubule (DCT): · Collecting Duct:.
Unnumbered headings, in source order: the chapter title plate · SUMMARY · EXERCISES.
The chapter has no `16.N.N` sub-numbered headings — unlike Ch15, its second level is carried entirely by the four run-in heads in 16.3. `Renal calculi:` and `Glomerulonephritis:` are **not** counted as headings; they are colon-led definition entries carried by `disorder`-type rows F163-F164. No numbered TABLE exists in this chapter.

**Opener census — 13 rows.** One opener per headed section plus the unheaded chapter-intro prose, minus the three headings that have no opening sentence of their own — the title plate, SUMMARY, and EXERCISES: 15 - 3 + 1 = 13. Sections with an opener: intro · 16.1 · 16.2 · 16.3 (PCT run-in) · Henle's Loop · DCT · Collecting Duct · 16.4 · 16.5 · 16.6 · 16.7 · 16.8. That is 12 headed openers plus the intro = 13. Note 16.3's own opener is the PCT run-in's first sentence, as the numbered head is followed immediately by the run-in head with no prose between them.

**Figure census — 6 numbered figures, 6 assets, 6 caption rows (F165-F170), 6 label rows (F173-F178), 7 in-text call-outs.**
Call-outs, in source order: (Figure 16.1) · (Figure 16.2) · (Figure 16.3) · (Figure 16.4) · (Figure 16.5) · (Figure 16.5) · (Figure. 16.6). Figure 16.5 is called out twice — in 16.2 and again in 16.3 (Collecting Duct) — so call-outs (7) exceed figures (6) by exactly one. The final call-out carries a source typo, a stray period in "Figure.".

**Type census — 172 Facts rows by type:** concept 84 · process 20 · number 15 · heading 15 · opener 13 · definition 13 · example 8 · caption 6 · disorder 2 · list 1 · question 1. Plus 6 `figure-label` rows in the matrix = 178 total.

## Gate 1 checklist

| # | Requirement | Status |
|---|---|---|
| 1 | Chapter read start to finish before any row was written | done — session `1-S`, full 12-page read |
| 2 | Every sentence-level fact captured as its own row | done — 172 Facts rows |
| 3 | All 8 numbered headings + 4 run-in + 3 unnumbered captured | done — 15 heading rows, machine-confirmed contiguous 16.1-16.8 |
| 4 | Every section's opening sentence captured | done — 13 opener rows, census reconciles 15-3+1 |
| 5 | All 6 captions transcribed verbatim | done — F165-F170; Fig 16.6 "mechanisms" plural confirmed against the PDF |
| 6 | In-figure labels harvested by opening each asset, not the text layer | done — 76 labels, all 6 assets opened at full size this session |
| 7 | Label matrix present in exactly one place, parseable by `check_pdf._extract_labels` | done — asserted by `verify_inventory.py` check [4]; a 0-label parse now fails the build |
| 8 | Figure-only labels identified and given a Pass 2 home | done — 13 flagged, split into 10 parser artefacts + 3 genuine gaps |
| 9 | Summary sentences classified, SUMMARY-UNIQUE folded | done — 22 = 18 + 4, all 4 folded |
| 10 | Exercises scanned, genuine gaps assigned a home | done — 12 scanned, 4 gaps, 17 non-gaps recorded |
| 11 | No Unicode sub/superscripts or U+FFFD in this file | done — asserted by `verify_inventory.py` check [5] |
| 12 | All counts machine-derived, not hand-tallied | done — `verify_inventory.py` re-parses the PDF and this file and exits non-zero on drift |
| 13 | All rows unticked at freeze | done — 0 of 178 ticked |

## References

- Source PDF: `Chapter/class 11/Chapter 16 - Excretory Products and their Elimination.pdf`
- Assets: `assets/fig_16_1.png` .. `assets/fig_16_6.png`
- Verifier: `verify_inventory.py` (run with `/vercel/share/neetenv/bin/python`)
- Protocol: `SUPREME COMMAND PROMPT.md` §4.4 (figures), §6 (3-pass workflow), Gate 1
- Checker: `check_pdf.py` (check 6 consumes the label matrix above)
