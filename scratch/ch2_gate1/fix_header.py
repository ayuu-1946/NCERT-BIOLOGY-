INV = "notes/class 12/Ch2_HumanReproduction/Ch2_HumanReproduction_inventory.md"
t = open(INV).read()

def rep(old, new):
    global t
    assert old in t, "NOT FOUND:\n" + old
    assert t.count(old) == 1, "AMBIGUOUS:\n" + old
    t = t.replace(old, new)

# 1) row count in source line
rep("| Frozen: 2026-09-02 | Rows: 205",
    "| Frozen: 2026-09-02 | Rows: 220")

# 2) dedup F076 (drop trailing clause that duplicates F077)
rep("[SUMMARY-UNIQUE, folded] Ovarian follicles in different stages of development are embedded in the stroma; the mammary glands are one of the female secondary sexual characteristics.",
    "[SUMMARY-UNIQUE, folded] Ovarian follicles in different stages of development are embedded in the stroma.")

# 3) rewrite the whole Pass-1 session log + census block with correct new IDs/counts
old_block = """Pass 1 session log (each session's sole machine-derived deliverable count):
- **1-S** (source read + facts inventory): 168 content/number/term/process/fact rows drafted (F001, F002, F003\u2013F008, and all non-heading/non-opener/non-caption/non-title rows).
- **1-H** (heading sweep): 10 heading rows \u2014 7 numbered (F009, F037, F078, F121, F170, F146, F190) + 3 unnumbered (F144 Menstrual Hygiene, F205 SUMMARY, F206 EXERCISES). Chapter title carried separately as 1 `title` row (F001).
- **1-O** (opener sweep): 8 opener rows (F002, F010, F038, F079, F122, F147, F191 + chapter-intro opener F002). See census below.
- **1-F** (figures): 14 figure-label `caption` rows (F159-a \u2026 see Figure-label rows block); figure manifest complete; all assets `Mono: yes`, `Verified: yes` (see `Ch2_figure_audit.md`).
- **1-Z** (gaps, summary, freeze): summary classification (20 sentences) + exercise-gap scan (21 exercises) + freeze.

Census (derivable from the lists, not asserted separately):
- **Heading rows (10):** 7 numbered + the 3 unnumbered IDs F144, F205, F206.
- **Opener rows (8):** F002, F010, F038, F079, F122, F147, F191, F121-opener \u2192 listed explicitly as the 8 rows typed `opener` below.
- **Figure-label rows (14):** one per asset \u2014 2.1a, 2.1b, 2.2, 2.3a, 2.3b, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 2.10, 2.11, 2.12.
- **Summary sentences (20):** 17 BODY-PRESENT + 3 SUMMARY-UNIQUE (folded into F077, F076, F204).
- **Exercises (21):** 19 COVERED + 2 GAP (Q20, Q21). Arithmetic: **21 exercises, 2 answered by design (GAP), 19 unanswered by design (COVERED), 0 overlooked.**"""

new_block = """Pass 1 session log (each session's sole machine-derived deliverable count):
- **1-S** (source read + facts inventory): 187 content rows drafted \u2014 every `fact`/`number`/`term`/`process`/`structure`/`function`/`hormone`/`comparison`/`exception` row (i.e. all rows except the 1 title, 8 openers, 10 headings and 14 captions).
- **1-H** (heading sweep): 10 heading rows \u2014 7 numbered (F009, F037, F078, F121, F146, F170, F190) + 3 unnumbered (F144 Menstrual Hygiene, F205 SUMMARY, F206 EXERCISES). Chapter title carried separately as 1 `title` row (F001).
- **1-O** (opener sweep): 8 opener rows \u2014 F002 (chapter intro), F010 (2.1), F038 (2.2), F079 (2.3), F122 (2.4), F147 (2.5), F171 (2.6), F191 (2.7).
- **1-F** (figures): 14 figure-label `caption` rows (F207\u2013F220 \u2014 one per rendered asset); figure manifest complete; all assets `Mono: yes`, `Verified: yes` (see `Ch2_figure_audit.md`).
- **1-Z** (gaps, summary, freeze): summary classification (20 sentences) + exercise-gap scan (21 exercises) + freeze.

Census (each total is derivable from the list beside it, not asserted separately):
- **Total rows = 220** = 1 title (F001) + 8 openers + 10 headings + 14 captions + 187 content rows. IDs are contiguous F001..F220 with no gaps or duplicates.
- **Heading rows (10):** 7 numbered [F009, F037, F078, F121, F146, F170, F190] + 3 unnumbered [F144, F205, F206]; 7 + 3 = 10.
- **Opener rows (8):** [F002, F010, F038, F079, F122, F147, F171, F191]; list length = 8.
- **Figure-label rows (14):** one per asset \u2014 [2.1a, 2.1b, 2.2, 2.3a, 2.3b, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 2.10, 2.11, 2.12] = 14 (IDs F207..F220).
- **Summary sentences (20):** 17 BODY-PRESENT + 3 SUMMARY-UNIQUE (folded into F076, F077, F204); 17 + 3 = 20.
- **Exercises (21):** 19 COVERED + 2 GAP (Q20, Q21). Arithmetic: **21 exercises, 2 answered by design (GAP), 19 unanswered by design (COVERED), 0 overlooked.**"""

rep(old_block, new_block)

open(INV, "w").write(t)
print("header fixed OK")
