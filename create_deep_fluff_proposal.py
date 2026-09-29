"""
Deep, unit-wise fluff-removal / rewording proposal (Human Physiology excluded).

Every row is a real passage pulled from a chapter build script under notes/ (file + line
number), with an action and a proposed replacement. Source hits come from
scratch/scan_fluff.py -> scratch/strong.json (regenerated here if missing).
Output: NCERT_Biology_Fluff_Removal_Proposal_DEEP.docx
"""
import json, os, re, subprocess, sys, glob
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_ORIENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

ROOT = os.path.dirname(os.path.abspath(__file__))
HITS = os.path.join(ROOT, "scratch", "strong.json")
ALL = os.path.join(ROOT, "scratch", "fluff_hits.json")
if not os.path.exists(HITS):
    subprocess.run([sys.executable, os.path.join(ROOT, "scratch", "scan_fluff.py")], check=True)

D, R, T, K = "DELETE", "REWORD", "THINK BOX", "KEEP"

P = {
"11/Ch1": {
 0: (R, "A group name (dogs, mammals, wheat) instantly recalls a set of shared characters - this is the basis of classification."),
 1: (K, "Functional definitions list; the '?' is part of a definition, not rhetoric."),
 2: (D, "Replace with the plain heading 'Exercise Support'."),
 3: (R, "Species (Q8): individuals with fundamental similarities, distinguishable from related species by distinct morphological differences. Biological species concept - Ernst Mayr. (Drop 'In this chapter' / 'The unit profile adds'.)"),
},
"11/Ch2": {
 0: (R, "Table 2.1 - Five-kingdom comparison (high-yield)."),
 1: (R, "Three-domain system: Monera split into two domains; all eukaryotic kingdoms in the third -> six-kingdom classification. (Delete 'You will learn ... higher classes'.)"),
 2: (D, "Pure invitation; the next paragraph already explains the criteria."),
 3: (R, "Scope: Monera, Protista, Fungi (+ viruses, viroids, lichens). Plantae -> Ch3; Animalia -> Ch4."),
 4: (R, "Viruses - living or non-living? Non-living: no cell structure; inert crystals outside host. Living: infectious genetic material; replicate using host machinery inside a cell."),
 5: (R, "The algal and fungal partners are so intimately associated that a lichen appears to be one organism."),
 6: (D, "Duplicate exercise preamble - replace with heading 'Exercise Support'."),
 7: (D, "Repeats the 2.6a virus note verbatim. Replace with: 'Q12 -> see 2.6a.'"),
},
"11/Ch3": {
 0: (R, "Scope: classification within Kingdom Plantae - Algae (3.1), Bryophytes (3.2), Pteridophytes (3.3), Gymnosperms (3.4), Angiosperms (3.5)."),
},
"11/Ch5": {
 0: (R, "Stem vs root: stems bear nodes and internodes, multicellular hairs, and are positively phototropic."),
},
"11/Ch7": {
 0: (R, "Protonema - first, green, branched, filamentous gametophyte stage of moss (plant structure; outside this chapter's scope)."),
},
"11/Ch8": {
 0: (R, "Plasmids: small extra-chromosomal DNA giving unique phenotypes, e.g. antibiotic resistance. Used to monitor bacterial transformation (-> Class 12, Ch9)."),
 1: (R, "Usually one nucleus per cell; multinucleate cells also occur."),
 2: (R, "Some mature cells lack a nucleus - mammalian RBCs, sieve-tube cells."),
 3: (R, "Chromatin = DNA + histones + non-histone proteins + RNA. One human cell holds ~2 m of DNA across 46 chromosomes. (Packaging -> Class 12, Ch5.)"),
 4: (R, "Division of labour (Q9): a unicellular organism performs all life functions in one cell; in multicellular organisms cells specialise into tissues and organs for specific functions. (Delete the 'phrase appears nowhere' meta-sentence.)"),
 5: (R, "Centrosome (no NCERT figure): two cylindrical centrioles, perpendicular to each other, surrounded by amorphous pericentriolar material. (Delete 'none is invented here'.)"),
},
"11/Ch9": {
 0: (R, "Despite enormous diversity, all organisms share remarkably similar chemical composition and metabolic reactions."),
 1: (R, "Delete the last sentence ('Can you identify a fat from the market?'). Keep the glycerides / oils-vs-fats facts."),
 2: (R, "Lipids (<800 Da) are not polymers, yet they appear in the acid-insoluble fraction because on grinding they form insoluble membrane vesicles."),
 3: (R, "Heading: 'Mechanism of Enzyme Action - How Rates Increase'."),
 4: (R, "The organic compounds in living tissue are identified by chemical analysis."),
},
"11/Ch10": {
 0: (T, "Think Box - Which cells divide for life? Plants: meristems (apical, lateral cambium) -> growth throughout life. Most differentiated cells exit to G0. (Drop the 'NCERT stops the reader three times' framing.)"),
 1: (R, "Haploid animal cells can divide by mitosis - e.g. the male honey bee (10.1.1)."),
},
"11/Ch11": {
 0: (D, "Throat-clearing; the experiments follow immediately."),
 1: (R, "He later located the green substance (chlorophyll) in special bodies within plant cells - later named chloroplasts."),
 2: (R, "Leaves differ in shade of green because they contain several pigments (Chl a, Chl b, xanthophylls, carotenoids) in different proportions."),
 3: (R, "PS II supplies electrons continuously by replacing them through splitting of water (photolysis)."),
 4: (R, "ATP synthesis in the chloroplast is explained by the chemiosmotic hypothesis."),
 5: (R, "Central question of the dark reaction: what is the primary CO2 acceptor and the first stable product of CO2 fixation?"),
 6: (R, "Mesophyll cells of C4 plants lack RuBisCO."),
 7: (T, "Think Box - C3 vs C4 cannot be reliably told externally; confirm by leaf anatomy (Kranz anatomy = C4)."),
 8: (T, "Think Box - Chl a is the chief pigment (reaction centre). Chl b and carotenoids are accessory: they widen the usable spectrum and protect Chl a from photo-oxidation."),
 9: (T, "Think Box - Leaves kept in dark turn yellow/pale: chlorophyll degrades; carotenoids/xanthophylls are more stable."),
 10: (D, "Observation activity; no testable fact. Remove."),
},
"11/Ch12": {
 0: (R, "Pyruvate has three fates depending on cellular need: lactic acid fermentation, alcoholic fermentation, aerobic respiration."),
 1: (R, "ATP synthesis here follows the chemiosmotic mechanism (see Ch11)."),
},
"12/Ch2": {}, "12/Ch1": {},
"12/Ch3": {
 0: (K, "Q-and-A bullet format is functional; leave as is."),
 1: (K, "Q-and-A bullet format is functional; leave as is."),
},
"12/Ch4": {
 0: (R, "Genotype Tt -> tall phenotype (T is dominant)."),
 1: (R, "Use one letter for both alleles of a gene (T/t), never T/d."),
 2: (R, "Heading: 'Concept of Dominance'."),
 3: (R, "Each gene carries the information to express a particular trait."),
 4: (R, "One allele may be altered (mutated), modifying the information it carries."),
 5: (R, "Example: a gene coding for an enzyme, present as two alleles."),
 6: (R, "Usually the normal allele produces the normal enzyme that transforms substrate S."),
 7: (R, "ABO blood groups also show multiple alleles: three alleles (IA, IB, i) govern one character."),
 8: (R, "Symbols: Y yellow (dominant) / y green; R round (dominant) / r wrinkled."),
 9: (R, "Figure 4.8 - chromosome segregation during meiosis in a 4-chromosome cell: G2 -> bivalent -> Meiosis I (homologues separate) -> Meiosis II (sister chromatids separate). Delete 'Read the plate' / 'Can you see'."),
 10: (R, "Chromosomes and genes both occur in pairs (mitosis = equational, meiosis = reduction division)."),
 11: (R, "Many traits are not discrete but vary along a gradient -> polygenic inheritance."),
 12: (R, "Model: three genes A, B, C control human skin colour; dominant A, B, C -> dark, recessive a, b, c -> light."),
 13: (R, "XO and XY types both show male heterogamety: males produce two kinds of gametes."),
 14: (R, "Each chromatid carries one continuous, highly supercoiled DNA double helix (-> Ch5)."),
},
"12/Ch5": {
 0: (R, "Polynucleotide structure: a nucleotide is built in three steps, each adding one component."),
 1: (R, "End with a statement, not a question: '... ~2.2 m of DNA vs a ~10^-6 m nucleus -> DNA must be packaged (nucleosomes).'"),
 2: (R, "Nucleosomes per mammalian cell = 6.6x10^9 bp / 200 bp ~ 3.3x10^7."),
 3: (R, "DNA = genetic material; DNase = enzyme that degrades DNA (-ase marks an enzyme)."),
 4: (R, "Which was the first genetic material? RNA - evidence below."),
 5: (R, "Only one strand is transcribed: (i) both strands would code for different proteins; (ii) two complementary RNAs would pair into dsRNA and block translation."),
 6: (K, "Mnemonic block (I/II/III -> rRNA/mRNA/tRNA) is high-yield; keep."),
 7: (T, "Keep the worked forward example; move 'Now try the opposite' to a Think Box."),
 8: (R, "The gene-DNA relationship is best understood through mutation studies (Ch4)."),
 9: (R, "lac operon stays ON only while lactose lasts: lactose is both inducer and substrate of beta-galactosidase; once hydrolysed, the repressor rebinds the operator."),
 10: (R, "Genetic information lies in the DNA base sequence; individual differences reflect sequence differences - the rationale for HGP."),
 11: (R, "HGP - a mega project. Aims:"),
 12: (R, "99.9% of the sequence is identical -> ~3x10^6 bp differ between two individuals (genome 3x10^9 bp)."),
 13: (R, "Sequencing every individual for comparison is impractical -> DNA fingerprinting."),
 14: (R, "Erratum: NCERT prints 3x10^6 bp here; correct figure is 3x10^9 bp."),
 15: (D, "Pure recall prompt; no content."),
 16: (R, "Variation accumulates in non-coding DNA (no immediate effect on reproduction) -> basis of polymorphism, from single-nucleotide changes to large-scale changes."),
 17: (R, "PCR (Ch9) raised sensitivity - DNA from a single cell suffices. Many probes are now used."),
},
"12/Ch6": {
 0: (R, "Fossil age: radiometric dating (method itself is outside NCERT detail)."),
 1: (R, "Artificial selection argument: man created new breeds within hundreds of years; nature could do the same over millions."),
 2: (R, "Darwin could not explain the origin of variation or speciation; he ignored Mendel's inheritable factors."),
},
"12/Ch7": {
 0: (R, "Biotechnology (Ch10) is yielding newer, safer vaccines."),
 1: (R, "Most exposures to infectious agents do not cause disease because the body defends itself (immunity)."),
 2: (R, "Food/water-borne diseases in this chapter: typhoid, amoebiasis, ascariasis."),
 3: (D, "Meta-commentary about exercise wording; remove."),
},
"12/Ch8": {
 0: (R, "Microbes are major components of biological systems (Monera, Protista, Fungi - Class XI)."),
 1: (R, "Microbes cause disease (Ch7), but many are useful to humans; key contributions follow."),
 2: (T, "Keep: 'Dosa/idli dough is fermented by bacteria; puffing is due to CO2.' Move the two questions to a Think Box."),
 3: (R, "Other antibiotics followed penicillin; they treat plague, whooping cough, diphtheria and leprosy. (Delete 'worth naming...' and 'cannot imagine a world...'.)"),
 4: (K, "Exercise-support definition of SCP; keep, trim the 'appears nowhere' sentence."),
 5: (R, "Sewage is rich in organic matter and pathogens, so it is treated in STPs before discharge into water bodies."),
 6: (R, "N2 fixers: symbiotic Rhizobium (legume root nodules); free-living Azospirillum and Azotobacter."),
 7: (K, "Useful exercise summary; trim 'Assembled only from facts...' preamble."),
},
"12/Ch9": {
 0: (R, "Alien DNA multiplies in a host only when integrated into its genome (i.e. linked to an origin of replication) - it then replicates with the chromosome."),
},
"12/Ch10": {
 0: (R, "Biotechnology: industrial-scale production of biopharmaceuticals and biologicals using GM microbes, fungi, plants and animals."),
 1: (R, "Bt toxin does not kill Bacillus: it is stored as an inactive protoxin, activated only by the alkaline pH of the insect gut."),
 2: (R, "Animal insulin (cattle/pig) can trigger allergy / immune reactions -> rDNA human insulin made in E. coli (Eli Lilly, 1983)."),
},
"12/Ch11": {
 0: (R, "Ecology is studied at levels of organisation: organisms -> populations -> communities -> biomes."),
 1: (D, "List of rhetorical 'why' questions; no testable fact."),
 2: (R, "Ecology: study of interactions of organisms with the abiotic (physico-chemical) and biotic (other species) components of their environment."),
 3: (R, "Four levels: organisms, populations, communities, biomes. Focus here: organism and population levels."),
 4: (R, "Population growth follows predictable patterns (exponential, logistic); natural populations show restraints on growth."),
 5: (R, "Exponential growth: one Paramecium doubling daily reaches 2^64 individuals in 64 days (unlimited resources)."),
 6: (R, "Life-history traits evolve under the abiotic and biotic constraints of the habitat."),
 7: (R, "No natural habitat has a single species; every species needs at least one other species to feed on."),
 8: (R, "Even autotrophs depend on others: soil microbes (nutrient return) and animal pollinators."),
 9: (R, "Predation transfers energy fixed by plants to higher trophic levels."),
 10: (R, "Predation is not only tiger-deer: a sparrow eating seeds is also a predator."),
 11: (T, "Keep harm list (reduce survival, growth, reproduction, density; make host prone to predation). Move 'ideal parasite' question to Think Box."),
 12: (T, "Think Box - Female mosquito is not a parasite (feeds briefly, does not live on/in host). Delete the cuckoo-watching activity."),
 13: (R, "Mutualisms must guard against 'cheaters' - e.g. nectar thieves that do not pollinate."),
 14: (D, "Exercise preamble; replace with heading 'Exercise Support'."),
},
"12/Ch12": {
 0: (D, "Duplicates the roadmap; merged into row 2's rewrite."),
 1: (R, "We will first study the structure of an ecosystem to understand its inputs (productivity), energy transfer (food chains, food webs, and nutrient cycling), and outputs (degradation and energy loss). We will also examine the cycles, chains, and webs formed by these energy flows and how they interact."),
 2: (R, "Aquatic model - the pond: shallow, self-sustaining, and shows all four basic ecosystem components."),
 3: (R, "All steps of decomposition operate simultaneously on detritus; humification and mineralisation occur in soil."),
 4: (R, "Ecosystems obey both laws of thermodynamics: they need a constant energy input to build molecules and counter increasing disorder."),
 5: (T, "Keep grazing-chain levels. Move the detritus-chain prompt to a Think Box."),
 6: (T, "Keep: 'One organism can occupy several trophic levels - sparrow: primary (seeds) and secondary (insects) consumer.' Think Box: humans function at several trophic levels."),
 7: (R, "Pyramid of biomass in the sea is inverted: fish biomass exceeds phytoplankton biomass."),
 8: (D, "Exercise preamble; replace with heading."),
 9: (D, "Restates exercise questions 7-11; remove."),
},
"12/Ch13": {
 0: (D, "Dangling rhetorical question; merge into the Tilman paragraph."),
 1: (R, "These estimates exclude prokaryotes."),
 2: (R, "Why the tropics are more diverse - three hypotheses:"),
 3: (R, "Whether species richness affects ecosystem function is not settled; Tilman's plots: more species -> less year-to-year variation in total biomass."),
 4: (D, "Rhetorical; the rivet-popper hypothesis covers it."),
 5: (D, "Rhetorical; no fact."),
 6: (R, "The 'Sixth Extinction' differs in rate: 100-1,000x faster than pre-human times, driven by human activities."),
 7: (R, "Exercise 10 (outside NCERT): deliberate extinction is defensible only for pathogens - e.g. smallpox virus (eradicated), polio virus."),
 8: (R, "The Amazon forest produces ~20% of atmospheric O2 - an ecosystem service that is hard to value economically."),
 9: (R, "Pollination by bees, bumblebees, birds and bats is a key ecosystem service; without it plants give no fruits or seeds."),
 10: (R, "Intangible benefits: aesthetic value (woods, flowers, birdsong) - cannot be priced."),
 11: (K, "Useful summary list; trim the 'Summary-sourced list' preamble."),
},
}

UNITS = [
 ("UNIT 1 - Diversity in the Living World", ["11/Ch1", "11/Ch2", "11/Ch3", "11/Ch4"],
  ["Collapse the two identical 'Exercise Support' preambles (Ch1, Ch2) into bare headings.",
   "Ch2 repeats the viruses living/non-living argument twice (2.6a and Q12) - keep one, cross-reference the other.",
   "Every chapter opens with a scope sentence; standardise to one line: 'Scope: X, Y, Z (sections a-b).'"]),
 ("UNIT 2 - Structural Organisation in Plants and Animals", ["11/Ch5", "11/Ch6", "11/Ch7"],
  ["Cleanest unit - almost no narrative filler. Only convert question-led openers into statements.",
   "Ch7 Q10(e) Protonema is off-topic for an animal chapter; shrink to one line or drop."]),
 ("UNIT 3 - Cell: Structure and Functions", ["11/Ch8", "11/Ch9", "11/Ch10"],
  ["Replace every 'You will study ... in class XII' with a bracketed cross-ref: '(-> Class 12, ChX)'.",
   "Remove meta-sentences about what NCERT does or does not print ('appears nowhere', 'none is invented here').",
   "Ch9 section heading 'How do Enzymes bring about...?' -> declarative heading."]),
 ("UNIT 4 - Plant Physiology", ["11/Ch11", "11/Ch12", "11/Ch13"],
  ["Ch11 has five end-of-section reader questions (pigments, C3/C4, dark leaves) - gather them into ONE Think Box at the end of 11.4 / 11.8.",
   "'Let us now...' openers (ATP synthesis, dark reaction) -> start with the mechanism name.",
   "Ch12 back-references to the chemiosmotic hypothesis -> '(see Ch11)'."]),
 ("UNIT 6 - Reproduction", ["12/Ch1", "12/Ch2", "12/Ch3"],
  ["Lowest fluff density of Class 12. Ch3 MTP 'Why? / When?' bullets are functional Q-A - keep.",
   "No structural changes proposed."]),
 ("UNIT 7 - Genetics and Evolution", ["12/Ch4", "12/Ch5", "12/Ch6"],
  ["Heaviest unit (36 rows). Ch4 uses 'Let us assume / Let's take' five times in the dominance and polygenic sections - convert each to 'Model:' or 'Example:'.",
   "Ch5 in-text calculations (DNA length, nucleosome count, 99.9% identity) should END in a result, never in a question.",
   "Ch5 'Recall ... Chapter 4' prompts - delete; keep the fact, add '(Ch4)'.",
   "Ch6 'if man could ... could not nature?' - rewrite as a stated argument."]),
 ("UNIT 8 - Biology in Human Welfare", ["12/Ch7", "12/Ch8"],
  ["Ch8 opener has two back-reference paragraphs (Class XI kingdoms, Ch7 diseases) - fuse into one line.",
   "Remove emotive closers ('we cannot imagine a world without antibiotics').",
   "Ch8 dough / sewage 'worth wondering' questions -> statement + optional Think Box."]),
 ("UNIT 9 - Biotechnology", ["12/Ch9", "12/Ch10"],
  ["Ch10 insulin paragraph is a 4-sentence rhetorical chain - compress to one causal line.",
   "Bt toxin Q-and-A -> a single 'because' sentence."]),
 ("UNIT 10 - Ecology", ["12/Ch11", "12/Ch12", "12/Ch13"],
  ["Second-heaviest unit. Ch11 intro (5 rows) is almost entirely philosophy - reduce to definition + levels of organisation.",
   "Ch12 intro: two overlapping roadmap paragraphs -> one (your example rewrite).",
   "Ch13 ecosystem-services block asks 'Can we put a price...?' three times - convert to a 3-row table: Service | Example | Note.",
   "All NCERT 'prompts' in Ch11-12 -> one Think Box per section."]),
]

HP_SKIP = {"Ch14", "Ch15", "Ch16", "Ch17", "Ch18", "Ch19"}


def shade(cell, hexfill):
    cell._element.get_or_add_tcPr().append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hexfill}"/>'))


def run(p, text, bold=False, size=9, color=None, italic=False):
    r = p.add_run(text)
    r.bold, r.italic = bold, italic
    r.font.size = Pt(size)
    if color:
        r.font.color.rgb = RGBColor.from_string(color)
    return r


ACTION_COLOR = {D: "C0392B", R: "1F618D", T: "B9770E", K: "566573"}


def main():
    hits = json.load(open(HITS))
    allhits = json.load(open(ALL))
    short = {f"{k.split('/')[0].split()[-1]}/{k.split('/')[1].split('_')[0]}": k for k in hits}

    doc = Document()
    sec = doc.sections[0]
    sec.orientation = WD_ORIENT.LANDSCAPE
    sec.page_width, sec.page_height = sec.page_height, sec.page_width
    for m in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
        setattr(sec, m, Inches(0.6))
    doc.styles["Normal"].font.name = "Calibri"
    doc.styles["Normal"].font.size = Pt(10)

    h = doc.add_heading("NCERT Biology - Deep Fluff Removal & Rewording Proposal", 0)
    p = doc.add_paragraph()
    run(p, "Unit-wise, passage-level. Human Physiology (Class 11 Ch14-19) excluded. Every row is a real passage "
           "from the chapter build scripts in notes/, with file:line so it can be edited in place.", size=10, italic=True)

    doc.add_heading("Actions", 1)
    for a, desc in [(D, "Remove entirely - no testable content."),
                    (R, "Replace with the proposed text (same facts, no filler)."),
                    (T, "Keep the fact inline; move the reader question to a single 'Think Box' at the end of the section."),
                    (K, "Flagged by the scanner but functional - leave (or trim as noted).")]:
        q = doc.add_paragraph(style="List Bullet")
        run(q, a + ": ", bold=True, size=10, color=ACTION_COLOR[a]); run(q, desc, size=10)

    doc.add_heading("Global rules applied", 1)
    for rule in ["No back-references ('In earlier classes', 'You have studied', 'Recall') - use '(Ch X)' cross-refs.",
                 "No invitations ('Let us', 'Let's', 'We will now look') - start with the subject.",
                 "No rhetorical questions in body text - state the answer; genuine exam-style prompts go to a Think Box.",
                 "No throat-clearing ('It is important to note', 'It is interesting') - state the fact.",
                 "No meta-commentary about NCERT's wording ('appears nowhere', 'none is invented here').",
                 "No emotive adjectives or closers ('fascinatingly', 'mind-boggling', 'cannot imagine a world').",
                 "Section headings are declarative, never questions."]:
        doc.add_paragraph(rule, style="List Number")

    doc.add_heading("Overview", 1)
    ov = doc.add_table(rows=1, cols=6); ov.style = "Light Grid Accent 1"
    for i, t in enumerate(["Unit", "Rows", D, R, T, K]):
        ov.rows[0].cells[i].text = t
    totals = [0, 0, 0, 0, 0]
    for name, chs, _ in UNITS:
        c = {D: 0, R: 0, T: 0, K: 0}
        for s in chs:
            for idx, (a, _) in P.get(s, {}).items():
                c[a] += 1
        n = sum(c.values())
        row = ov.add_row().cells
        vals = [name, n, c[D], c[R], c[T], c[K]]
        for i, v in enumerate(vals):
            row[i].text = str(v)
        for i, v in enumerate(vals[1:]):
            totals[i] += v
    row = ov.add_row().cells
    for i, v in enumerate(["TOTAL"] + totals):
        row[i].text = str(v)
        row[i].paragraphs[0].runs[0].bold = True

    for name, chs, structural in UNITS:
        doc.add_page_break()
        doc.add_heading(name, 1)
        doc.add_heading("Structural recommendations", 3)
        for s in structural:
            doc.add_paragraph(s, style="List Bullet")
        for s in chs:
            full = short.get(s)
            if not full:
                continue
            items = hits[full]
            weak = len(allhits.get(full, [])) - len(items)
            doc.add_heading(full.split("/")[1].replace("_", " - ", 1), 2)
            pth = glob.glob(os.path.join(ROOT, "notes", full.split("/")[0], full.split("/")[1], "*.py"))
            pth = [x for x in pth if "extract" not in x]
            rel = os.path.relpath(pth[0], ROOT) if pth else ""
            meta = doc.add_paragraph()
            run(meta, f"{rel}  |  {len(items)} passages  |  +{weak} minor wording hits (various, rather, basically...) for a light sweep",
                size=8, italic=True, color="566573")
            if not items:
                run(doc.add_paragraph(), "No narrative filler found - no action needed.", size=9, italic=True)
                continue
            tbl = doc.add_table(rows=1, cols=5); tbl.style = "Table Grid"
            widths = [Inches(0.55), Inches(3.9), Inches(1.0), Inches(0.9), Inches(3.9)]
            for i, t in enumerate(["Line", "Original", "Fluff type", "Action", "Proposed"]):
                c = tbl.rows[0].cells[i]; c.text = ""; run(c.paragraphs[0], t, bold=True, size=9, color="FFFFFF")
                shade(c, "1C2833"); c.width = widths[i]
            for idx, x in enumerate(items):
                a, prop = P.get(s, {}).get(idx, (K, "Review manually."))
                cells = tbl.add_row().cells
                run(cells[0].paragraphs[0], str(x["line"]), size=8)
                run(cells[1].paragraphs[0], x["text"], size=8, italic=True, color="424949")
                run(cells[2].paragraphs[0], ", ".join(x["tags"]), size=8)
                run(cells[3].paragraphs[0], a, bold=True, size=8, color=ACTION_COLOR[a])
                run(cells[4].paragraphs[0], prop, size=8)
                if a == D:
                    shade(cells[4], "FDEDEC")
                elif a == T:
                    shade(cells[4], "FEF5E7")
                for i, c in enumerate(cells):
                    c.width = widths[i]

    out = os.path.join(ROOT, "NCERT_Biology_Fluff_Removal_Proposal_DEEP.docx")
    doc.save(out)
    print("saved", out)


if __name__ == "__main__":
    main()
