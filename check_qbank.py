#!/usr/bin/env python3
"""
check_qbank.py — the automated **Gate 4 (Q-Gate)** for generated NEET question
banks, and the shared parsing library the question workflow is built on.

Why this file exists
--------------------
`NEET_QUESTION_GENERATION_PROMPT.md` asks the model to run a silent self-audit
and then *state* its tier mix, key distribution, cross-chapter count and
Pass-Q2 fix count in a run header. Per the Supreme prompt's Gate 3(b) rule 1,
**a stated PASS is a claim, not a fact.** Everything the model claims about a
bank is mechanically re-derivable from the bank itself, so it is re-derived
here and compared against the claim. A header that disagrees with its own
items is a FAIL, exactly as an inventory header that disagrees with its own
table is a Gate 1 FAIL.

It is deliberately **stdlib-only** — no reportlab/pymupdf/Pillow — so a red
Q-Gate can never be an artifact of a missing library or of the two-interpreter
trap (§0.2). Still invoke it through the venv interpreter for consistency:

    /vercel/share/neetenv/bin/python check_qbank.py "notes/class 11/Ch4_AnimalKingdom"
    /vercel/share/neetenv/bin/python check_qbank.py --qbank <path>_QBANK.md
    /vercel/share/neetenv/bin/python check_qbank.py "<folder>" --emit-ledger

Exit codes mirror `check_pdf.py`: 0 = clean, 1 = at least one FAIL, 2 = setup
error. `--strict` treats WARN as failure; `--json` emits a machine report.

This module is also the single home for the question workflow's parsers
(`parse_registry`, `parse_facts_table`, `resolve_chapter`, `tracker_status`,
`build_stamp`). `scripts/build_question_prompt.py` imports them from here
rather than restating them — the same discipline by which chapters import
`_extract_labels` from `check_pdf.py` instead of re-implementing it. The
prompt-builder and the gate must never be able to disagree about what a
bridge, a fact ID, or a build stamp is.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
NOTES_ROOT = REPO_ROOT / "notes"
PROMPT_PATH = REPO_ROOT / "NEET_QUESTION_GENERATION_PROMPT.md"
TRACKER_PATH = REPO_ROOT / "CHAPTER_TRACKER.md"

# ---------------------------------------------------------------------------
# thresholds — all of these are the prompt's own stated contracts, made hard
# ---------------------------------------------------------------------------
TIER_TARGET = {1: 0.20, 2: 0.45, 3: 0.35}
TIER_TOL = 0.10                 # +/- 10 percentage points around the target mix
KEY_MAX_SHARE = 0.35            # no option may hold more than 35% of keys
KEY_MIN_SHARE = 0.15            # nor less than 15%
CROSS_MIN_SHARE = 0.50          # >= 50% of Tier-2+3 items must be cross-chapter
FACTS_MIN = {1: 1, 2: 2, 3: 2}  # minimum cited fact IDs per tier
COVERAGE_WARN = 0.80            # fraction of anchor sections that must be touched

CANON_ARCHETYPES = [
    "single", "match", "count", "sequence",
    "assertion-reason", "negative", "numerical", "scenario",
]
ARCHETYPE_ALIASES = {
    "single-correct": "single", "factual": "single", "conceptual": "single",
    "match-list": "match", "matchlist": "match", "matching": "match",
    "multi-statement": "count", "how-many": "count", "statement-count": "count",
    "order": "sequence", "arrange": "sequence",
    "assertion": "assertion-reason", "ar": "assertion-reason",
    "assertion-reasoning": "assertion-reason",
    "negative-stem": "negative",
    "quantitative": "numerical", "calculation": "numerical",
    "data-interpretation": "scenario", "data": "scenario", "vignette": "scenario",
}

# Banned glyphs, same classes check_pdf.py's check 5 enforces on the PDF text
# stream. Restated (not imported) on purpose: importing check_pdf.py would drag
# in pymupdf and make this gate fail for an environment reason.
ARROWS = "\u2190\u2191\u2192\u2193\u2194\u2195\u21cc\u21d0\u21d2\u21cb\u27f6\u2b0e\u2b0f"
GREEK = "".join(chr(c) for c in range(0x0391, 0x03CA))
SUBSUP = "".join(chr(c) for c in range(0x2070, 0x209D))

FACTS_TABLE_RE = re.compile(
    r"^\|\s*(F\d+[a-z]?)\s*\|\s*([^|]*)\|\s*([^|]*)\|\s*(.*?)\s*\|\s*([^|]*)\|\s*$"
)
REGISTRY_ROW_RE = re.compile(r"^\|\s*(B\d+)\s*\|\s*([^|]*)\|\s*([^|]+)\|")
BACKTICK_RE = re.compile(r"`([A-Za-z0-9]+)`")

ITEM_TAG_RE = re.compile(
    r"^Q(\d+)\.\s*\[\s*Tier\s*([123])\s*\]\s*\[\s*([A-Za-z\-/ ]+?)\s*\]", re.IGNORECASE
)
OPTION_RE = re.compile(r"^\s*\((\d)\)\s*(\S.*)$")
KEY_RE = re.compile(r"^Q(\d+)\.\s*Correct:\s*\(\s*([1-4])\s*\)", re.IGNORECASE)
META_RE = re.compile(r"^Meta:\s*(.+)$", re.IGNORECASE)
FACT_REF_RE = re.compile(r"(?:([A-Za-z][A-Za-z0-9]*)\s*:\s*)?(F\d+[a-z]?)")


# =====================================================================================
# result plumbing (same shape as check_pdf.py so reports read alike)
# =====================================================================================

class Check:
    def __init__(self, name: str):
        self.name = name
        self.status = "PASS"
        self.detail: list[str] = []

    def fail(self, msg: str):
        self.status = "FAIL"
        self.detail.append(msg)

    def warn(self, msg: str):
        if self.status != "FAIL":
            self.status = "WARN"
        self.detail.append(msg)

    def note(self, msg: str):
        self.detail.append(msg)

    def skip(self, msg: str):
        self.status = "SKIP"
        self.detail.append(msg)

    def to_dict(self):
        return {"check": self.name, "status": self.status, "detail": self.detail}


def _read(path) -> str:
    return Path(path).read_text(encoding="utf-8", errors="replace")


# =====================================================================================
# shared library: chapters, inventories, registry, tracker, stamp
# =====================================================================================

def chapter_key(dir_name: str) -> str:
    """Ch4_AnimalKingdom -> AnimalKingdom (the canonical cross-chapter key)."""
    return dir_name.split("_", 1)[-1] if "_" in dir_name else dir_name


def chapter_topic_name(ch_dir: Path) -> str:
    """Ch4_AnimalKingdom -> 'Animal Kingdom'."""
    stem = chapter_key(ch_dir.name)
    spaced = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", stem)
    return re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", " ", spaced)


def find_chapter_dirs() -> list[tuple[str, Path]]:
    """[(class_label, chapter_dir), ...] for every chapter folder under notes/."""
    dirs = []
    for class_dir in sorted(NOTES_ROOT.glob("class *")):
        class_label = class_dir.name.replace("class ", "").strip()
        for ch_dir in sorted(class_dir.glob("Ch*_*")):
            if ch_dir.is_dir():
                dirs.append((class_label, ch_dir))
    return dirs


def resolve_chapter(class_arg, chapter_arg):
    """Substring-match a chapter dir. Returns (class_label, dir, ambiguous_list)."""
    query = re.sub(r"[\s_-]+", "", str(chapter_arg)).lower()
    candidates = []
    for class_label, ch_dir in find_chapter_dirs():
        if class_arg and class_label != str(class_arg):
            continue
        if query in re.sub(r"[\s_-]+", "", ch_dir.name).lower():
            candidates.append((class_label, ch_dir))
    if not candidates:
        return None, None, []
    if len(candidates) > 1:
        return "AMBIGUOUS", None, candidates
    return candidates[0][0], candidates[0][1], []


def resolve_key(key: str):
    """Resolve a canonical chapter key ('BodyFluidsAndCirculation') to a dir."""
    want = key.lower()
    for class_label, ch_dir in find_chapter_dirs():
        if chapter_key(ch_dir.name).lower() == want:
            return class_label, ch_dir
    return None, None


def find_inventory_file(ch_dir: Path):
    matches = sorted(ch_dir.glob("*_inventory.md"))
    return matches[0] if matches else None


def parse_facts_table(inventory_path) -> list[dict]:
    """
    Rows of the frozen inventory's Facts table: id, section, type, wording.

    Two shapes appear across the closed chapters and both must parse:
      - `## Facts` followed immediately by the table
      - `## Facts` followed by a Legend/prose line, then the table (Ch14, Ch16)

    So prose *before* the first row is skipped rather than treated as the end of
    the table, and the table ends at the next `## ` heading or at the first
    non-pipe line *after* rows have started. The stricter earlier rule made a
    fully gate-closed chapter parse as "no Facts table", which the builder then
    reported as an unavailable bridge — a silent degradation of exactly the kind
    the Supreme prompt's Gate 1 rules warn about.
    """
    facts: list[dict] = []
    in_section = False
    started = False
    for line in _read(inventory_path).splitlines():
        stripped = line.strip()
        if re.match(r"^##\s+Facts\b", stripped):
            in_section = True
            continue
        if not in_section:
            continue
        if stripped.startswith("## "):
            break
        if stripped.startswith("| ID") or stripped.startswith("|---"):
            continue
        m = FACTS_TABLE_RE.match(stripped)
        if m:
            started = True
            fid, section, ftype, wording, _ticked = m.groups()
            facts.append({
                "id": fid.strip(),
                "section": section.strip(),
                "type": ftype.strip().lower(),
                "wording": wording.strip(),
            })
        elif started and stripped and not stripped.startswith("|"):
            break
    return facts


def parse_registry(prompt_path=PROMPT_PATH) -> list[dict]:
    """
    Parse the cross-chapter bridge registry out of the prompt's APPENDIX table.

    The APPENDIX is the single source of truth for bridges; nothing here keeps a
    second copy. Each row: | B01 | 11 | `KeyA` + `KeyB` ... | NCERT basis |
    Only backticked tokens in the keys column are read, so the prose column can
    never leak a phantom chapter into the registry.
    """
    rows: list[dict] = []
    if not Path(prompt_path).exists():
        return rows
    for line in _read(prompt_path).splitlines():
        m = REGISTRY_ROW_RE.match(line.strip())
        if not m:
            continue
        bid, class_col, keys_col = m.groups()
        keys = BACKTICK_RE.findall(keys_col)
        if len(keys) >= 2:
            rows.append({"id": bid, "class": class_col.strip(), "keys": keys})
    return rows


def bridges_for(key: str, registry: list[dict]) -> set[str]:
    """Every chapter key legitimately bridged to `key` by the registry."""
    linked: set[str] = set()
    for row in registry:
        if key in row["keys"]:
            linked |= set(row["keys"]) - {key}
    return linked


def tracker_status(class_label: str, ch_dir: Path, tracker_path=TRACKER_PATH) -> str:
    """
    'DONE' | 'OPEN' | 'UNKNOWN' — the chapter's Gate 3 state per CHAPTER_TRACKER.md.

    The tracker is the repo's authority on which chapters are closed, so Gate 4's
    precondition is read from it rather than re-litigated here.
    """
    if not Path(tracker_path).exists():
        return "UNKNOWN"
    m = re.match(r"Ch(\d+)", ch_dir.name)
    if not m:
        return "UNKNOWN"
    want_num = int(m.group(1))
    current_class = None
    for line in _read(tracker_path).splitlines():
        h = re.match(r"^##\s+Class\s+(\d+)", line.strip())
        if h:
            current_class = h.group(1)
            continue
        if current_class != str(class_label):
            continue
        row = re.match(r"^\s*\|\s*(\d+)\.\s*([^|]+?)\s*\|\s*(.*)$", line)
        if row and int(row.group(1)) == want_num:
            cell = row.group(3)
            return "DONE" if "\u2705" in cell else "OPEN"
    return "UNKNOWN"


def build_stamp(anchor: tuple[str, Path], bridges: list[tuple[str, Path]]) -> str:
    """
    A fingerprint of the exact source text a bank was generated from:
    'AnimalKingdom@353+BodyFluidsAndCirculation@245,Evolution@0'

    The builder writes it into the prompt and the bank carries it back. If an
    inventory later gains or loses rows, the recomputed stamp differs and the
    bank is STALE — it was grounded in text that no longer exists. This is the
    Gate-4 answer to "a frozen inventory may be corrected in its metadata".
    """
    def one(item):
        _cl, ch_dir = item
        inv = find_inventory_file(ch_dir)
        n = len(parse_facts_table(inv)) if inv else 0
        return f"{chapter_key(ch_dir.name)}@{n}"

    left = one(anchor)
    right = ",".join(one(b) for b in sorted(bridges, key=lambda b: b[1].name))
    return f"{left}+{right}" if right else left


# =====================================================================================
# question-bank parsing
# =====================================================================================

def parse_header(text: str) -> dict:
    """Read the bank's claimed run header. Every value here is later re-derived."""
    hdr: dict = {"raw": {}}
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        m = re.match(r"^Anchor:\s*class\s*(\d+)\s*/\s*(\S+)", s, re.IGNORECASE)
        if m:
            hdr["class"], hdr["anchor_dir"] = m.group(1), m.group(2)
            continue
        m = re.match(r"^Prompt-build:\s*(\S+)", s, re.IGNORECASE)
        if m:
            hdr["stamp"] = m.group(1)
            continue
        m = re.match(r"^Items:\s*(\d+)", s, re.IGNORECASE)
        if m:
            hdr["items"] = int(m.group(1))
            t = re.search(r"T1/T2/T3\s*=\s*(\d+)\s*/\s*(\d+)\s*/\s*(\d+)", s)
            if t:
                hdr["tiers"] = {1: int(t.group(1)), 2: int(t.group(2)), 3: int(t.group(3))}
            continue
        if re.match(r"^Archetypes:", s, re.IGNORECASE):
            hdr["archetypes"] = {
                k.strip().lower(): int(v)
                for k, v in re.findall(r"([A-Za-z\-]+)\s*=\s*(\d+)", s)
            }
            continue
        m = re.match(r"^Cross-chapter:\s*(\d+)\s*/\s*(\d+)", s, re.IGNORECASE)
        if m:
            hdr["cross"] = (int(m.group(1)), int(m.group(2)))
            continue
        if re.match(r"^Key distribution:", s, re.IGNORECASE):
            hdr["keys"] = {
                int(k): int(v) for k, v in re.findall(r"\((\d)\)\s*=\s*(\d+)", s)
            }
            continue
        m = re.match(r"^Pass-Q2 fixes:\s*(\d+)\s*rewritten\s*/\s*(\d+)\s*discarded", s, re.IGNORECASE)
        if m:
            hdr["fixes"] = (int(m.group(1)), int(m.group(2)))
    return hdr


def normalize_archetype(raw: str) -> str:
    a = raw.strip().lower().replace(" ", "-").replace("/", "-")
    a = ARCHETYPE_ALIASES.get(a, a)
    return a


def split_sections(text: str) -> tuple[str, str]:
    """Return (section_a_text, section_b_text)."""
    idx = None
    for m in re.finditer(r"^.*SECTION\s+B\b.*$", text, re.MULTILINE):
        idx = m.start()
        break
    if idx is None:
        return text, ""
    return text[:idx], text[idx:]


def parse_items(section_a: str) -> dict[int, dict]:
    """Items from SECTION A: tier, archetype, links text, options."""
    items: dict[int, dict] = {}
    current = None
    for line in section_a.splitlines():
        m = ITEM_TAG_RE.match(line.strip())
        if m:
            n = int(m.group(1))
            current = {
                "n": n,
                "tier": int(m.group(2)),
                "archetype": normalize_archetype(m.group(3)),
                "archetype_raw": m.group(3).strip(),
                "tag_line": line.strip(),
                "links_declared": [],
                "options": {},
                "stem_lines": [],
            }
            links = re.search(r"Links:\s*([^|\]]*)", line)
            if links:
                raw = links.group(1).strip()
                if raw and raw not in {"-", "--", "—", "none", "None"}:
                    current["links_declared"] = [
                        p.strip() for p in re.split(r"[;,]", raw) if p.strip()
                    ]
            items[n] = current
            continue
        if current is None:
            continue
        om = OPTION_RE.match(line)
        if om:
            current["options"][int(om.group(1))] = om.group(2).strip()
        elif line.strip():
            current["stem_lines"].append(line.strip())
    return items


def parse_keys(section_b: str) -> dict[int, dict]:
    """Answer key + Meta line per item from SECTION B."""
    keys: dict[int, dict] = {}
    current = None
    for line in section_b.splitlines():
        s = line.strip()
        m = KEY_RE.match(s)
        if m:
            n = int(m.group(1))
            current = {"n": n, "correct": int(m.group(2)), "meta": {}, "facts": [], "body": []}
            keys[n] = current
            continue
        if current is None:
            continue
        mm = META_RE.match(s)
        if mm:
            for field in mm.group(1).split("|"):
                if "=" not in field:
                    continue
                k, v = field.split("=", 1)
                current["meta"][k.strip().lower()] = v.strip()
            facts_raw = current["meta"].get("facts", "")
            for prefix, fid in FACT_REF_RE.findall(facts_raw):
                current["facts"].append((prefix or "", fid))
            continue
        if s:
            current["body"].append(s)
    return keys


# =====================================================================================
# checks
# =====================================================================================

def check_provenance(hdr, anchor, bridges_used, registry, stamp_now) -> Check:
    c = Check("Q1 provenance & gate-4 precondition")
    class_label, anchor_dir = anchor
    anchor_key = chapter_key(anchor_dir.name)

    if hdr.get("anchor_dir") and hdr["anchor_dir"] != anchor_dir.name:
        c.fail(f"header Anchor '{hdr['anchor_dir']}' != folder '{anchor_dir.name}'")
    if not hdr.get("anchor_dir"):
        c.fail("no 'Anchor: class N / <ChapterDir>' line in the run header")

    st = tracker_status(class_label, anchor_dir)
    if st == "DONE":
        c.note(f"anchor class {class_label} {anchor_dir.name}: Gate 3 CLOSED per CHAPTER_TRACKER.md")
    elif st == "OPEN":
        c.fail(
            f"anchor {anchor_dir.name} is NOT Done in CHAPTER_TRACKER.md — Gate 4 may not "
            "close on an ungated chapter (a bank is only as sound as the inventory Pass 3 froze)"
        )
    else:
        c.fail(f"anchor {anchor_dir.name} has no resolvable status row in CHAPTER_TRACKER.md")

    allowed = bridges_for(anchor_key, registry)
    for key in sorted(bridges_used):
        b_class, b_dir = resolve_key(key)
        if b_dir is None:
            c.fail(f"cited chapter key '{key}' does not exist under notes/")
            continue
        if key not in allowed:
            c.fail(
                f"'{key}' is not a registered bridge of {anchor_key} — off-registry links are "
                "ungrounded (add the bridge to the APPENDIX with its NCERT basis, or drop the item)"
            )
        b_st = tracker_status(b_class, b_dir)
        if b_st != "DONE":
            c.fail(f"bridge {b_dir.name} is {b_st}, not Done — its facts are not gate-verified")
        else:
            c.note(f"bridge {b_dir.name}: Gate 3 CLOSED")

    claimed = hdr.get("stamp")
    if not claimed:
        c.fail("no 'Prompt-build:' stamp — cannot tell which source text this bank was built from")
    elif claimed.startswith("PROVISIONAL"):
        c.fail(f"prompt was built with --allow-open-gates ({claimed}); a provisional bank cannot close Gate 4")
    elif claimed != stamp_now:
        c.fail(f"STALE: built from '{claimed}', current inventories fingerprint '{stamp_now}' — regenerate")
    else:
        c.note(f"stamp matches current inventories: {stamp_now}")
    return c


def check_structure(hdr, items, keys) -> Check:
    c = Check("Q2 structure & item/key correspondence")
    if not items:
        c.fail("SECTION A has no parseable 'Q<n>. [Tier n] [archetype]' items")
        return c
    if not keys:
        c.fail("SECTION B has no parseable 'Q<n>. Correct: (x)' keys")
        return c

    n_items = len(items)
    expected = sorted(items)
    if expected != list(range(1, n_items + 1)):
        missing = sorted(set(range(1, max(expected) + 1)) - set(expected))
        c.fail(f"item numbers not contiguous from 1: {n_items} items, gaps at {missing}")
    if hdr.get("items") is not None and hdr["items"] != n_items:
        c.fail(f"header claims Items: {hdr['items']}, SECTION A contains {n_items}")
    else:
        c.note(f"{n_items} items, contiguous")

    only_a = sorted(set(items) - set(keys))
    only_b = sorted(set(keys) - set(items))
    if only_a:
        c.fail(f"items with no answer key: {only_a}")
    if only_b:
        c.fail(f"keys with no item in SECTION A: {only_b}")
    if not only_a and not only_b:
        c.note(f"every item has exactly one key ({len(keys)}/{n_items})")
    return c


def check_options(items, keys) -> Check:
    c = Check("Q3 options: four, distinct, one key")
    bad_count, dupes, bad_key = [], [], []
    for n, it in sorted(items.items()):
        opts = it["options"]
        if sorted(opts) != [1, 2, 3, 4]:
            bad_count.append(f"Q{n} has options {sorted(opts) or 'none'}")
        texts = [_norm(t) for t in opts.values()]
        if len(set(texts)) != len(texts):
            dupes.append(f"Q{n}")
        k = keys.get(n)
        if k and k["correct"] not in opts:
            bad_key.append(f"Q{n} keys ({k['correct']}) which is not an emitted option")
    for msg in bad_count:
        c.fail(msg)
    if dupes:
        c.fail(f"duplicate option text (so more than one option is 'correct'): {', '.join(dupes)}")
    for msg in bad_key:
        c.fail(msg)
    if not (bad_count or dupes or bad_key):
        c.note(f"{len(items)} items x 4 distinct options, every key in range")
    return c


def check_key_distribution(hdr, keys) -> Check:
    c = Check("Q4 key distribution (anti-clustering)")
    if not keys:
        c.skip("no keys parsed")
        return c
    derived = {i: 0 for i in (1, 2, 3, 4)}
    for k in keys.values():
        derived[k["correct"]] += 1
    total = len(keys)
    c.note("derived: " + " ".join(f"({i})={derived[i]}" for i in (1, 2, 3, 4)) + f"  n={total}")

    if hdr.get("keys") and hdr["keys"] != derived:
        c.fail(f"header claims {hdr['keys']}, derived {derived}")
    for i in (1, 2, 3, 4):
        share = derived[i] / total
        if share > KEY_MAX_SHARE:
            c.fail(f"option ({i}) holds {share:.0%} of keys (cap {KEY_MAX_SHARE:.0%})")
        elif share < KEY_MIN_SHARE:
            c.fail(f"option ({i}) holds {share:.0%} of keys (floor {KEY_MIN_SHARE:.0%})")
    return c


def check_tier_mix(hdr, items) -> Check:
    c = Check("Q5 tier mix (difficulty centre of gravity)")
    if not items:
        c.skip("no items parsed")
        return c
    derived = {1: 0, 2: 0, 3: 0}
    for it in items.values():
        derived[it["tier"]] += 1
    total = len(items)
    c.note("derived T1/T2/T3 = " + "/".join(str(derived[t]) for t in (1, 2, 3)))

    if hdr.get("tiers") and hdr["tiers"] != derived:
        c.fail(f"header claims T1/T2/T3 = {hdr['tiers']}, derived {derived}")
    for t in (1, 2, 3):
        share = derived[t] / total
        lo, hi = TIER_TARGET[t] - TIER_TOL, TIER_TARGET[t] + TIER_TOL
        if not (lo <= share <= hi):
            c.warn(f"Tier {t} is {share:.0%} of the set, outside the {lo:.0%}-{hi:.0%} band")
    return c


def check_grounding(items, keys, known_ids, anchor_key) -> Check:
    c = Check("Q6 fact grounding (every item traceable to frozen rows)")
    unknown, thin, nometa = [], [], []
    for n, it in sorted(items.items()):
        k = keys.get(n)
        if not k or not k["meta"]:
            nometa.append(f"Q{n}")
            continue
        refs = k["facts"]
        if not refs:
            nometa.append(f"Q{n}")
            continue
        for prefix, fid in refs:
            key = prefix or anchor_key
            if (key, fid) not in known_ids:
                unknown.append(f"Q{n} cites {key}:{fid}")
        need = FACTS_MIN[it["tier"]]
        if len({r for r in refs}) < need:
            thin.append(f"Q{n} (Tier {it['tier']}) cites {len(set(refs))} fact(s), needs {need}")
    if nometa:
        c.fail(f"items with no machine-readable 'Meta: ... facts=[...]' citation: {', '.join(nometa)}")
    for msg in unknown:
        c.fail(msg + " — no such row in the frozen inventory (hallucinated citation)")
    for msg in thin:
        c.fail(msg + " — a Tier-2/3 item citing one fact is one-line-solvable by construction")
    if not (nometa or unknown or thin):
        cited = {(p or anchor_key, f) for k in keys.values() for p, f in k["facts"]}
        c.note(f"{len(cited)} distinct frozen rows cited, all resolvable; per-tier minimums met")
    return c


def check_cross_chapter(hdr, items, keys, anchor_key) -> Check:
    c = Check("Q7 cross-chapter links are load-bearing")
    hard = [n for n, it in items.items() if it["tier"] in (2, 3)]
    if not hard:
        c.skip("no Tier-2/3 items")
        return c

    cross, decorative = [], []
    for n in sorted(hard):
        k = keys.get(n)
        if not k:
            continue
        cited_keys = {p for p, _f in k["facts"] if p and p != anchor_key}
        if cited_keys:
            cross.append(n)
        declared = items[n]["links_declared"]
        if declared and not cited_keys:
            decorative.append(f"Q{n} declares Links: {'; '.join(declared)} but cites no fact from any of them")

    share = len(cross) / len(hard)
    c.note(f"derived cross-chapter: {len(cross)}/{len(hard)} Tier-2+3 items ({share:.0%})")
    if hdr.get("cross") and hdr["cross"] != (len(cross), len(hard)):
        c.fail(f"header claims {hdr['cross'][0]}/{hdr['cross'][1]}, derived {len(cross)}/{len(hard)}")
    for msg in decorative:
        c.fail(msg + " — a decorative link, not a fused one")
    if share < CROSS_MIN_SHARE:
        c.fail(f"only {share:.0%} of Tier-2/3 items fuse a bridge fact (floor {CROSS_MIN_SHARE:.0%})")
    return c


def check_duplication_and_coverage(items, keys, anchor_facts, anchor_key) -> Check:
    c = Check("Q8 duplication & chapter coverage")
    seen: dict[frozenset, int] = {}
    for n in sorted(items):
        k = keys.get(n)
        if not k or not k["facts"]:
            continue
        sig = frozenset((p or anchor_key, f) for p, f in k["facts"])
        if sig in seen:
            c.fail(f"Q{n} tests the identical fact-cluster as Q{seen[sig]} — merge or replace")
        else:
            seen[sig] = n

    sections = {f["section"] for f in anchor_facts if f["section"]}
    if not sections:
        c.warn("anchor inventory exposes no Section column values; coverage not measurable")
        return c
    by_id = {f["id"]: f["section"] for f in anchor_facts}
    touched = {
        by_id.get(f)
        for k in keys.values() for p, f in k["facts"]
        if (p or anchor_key) == anchor_key
    } - {None, ""}
    share = len(touched) / len(sections)
    msg = f"anchor sections touched: {len(touched)}/{len(sections)} ({share:.0%})"
    if share < COVERAGE_WARN:
        c.warn(msg + f" — below the {COVERAGE_WARN:.0%} floor a 360 set needs; untouched: "
                     + ", ".join(sorted(sections - touched)[:12]))
    else:
        c.note(msg)
    return c


def check_hygiene(hdr, items, text) -> Check:
    c = Check("Q9 archetype spread, glyphs & negative-stem style")
    derived: dict[str, int] = {}
    for it in items.values():
        derived[it["archetype"]] = derived.get(it["archetype"], 0) + 1
    c.note("derived archetypes: " + " | ".join(f"{k}={v}" for k, v in sorted(derived.items())))

    unknown = sorted(set(derived) - set(CANON_ARCHETYPES))
    if unknown:
        c.fail(f"unrecognised archetype tag(s) {unknown}; use one of {CANON_ARCHETYPES}")
    if hdr.get("archetypes"):
        claimed = {k: v for k, v in hdr["archetypes"].items() if v}
        if claimed != {k: v for k, v in derived.items() if v}:
            c.fail(f"header claims {claimed}, derived {derived}")
    missing = [a for a in CANON_ARCHETYPES if not derived.get(a)]
    if missing:
        c.warn(f"archetypes absent (note the substitution in the header if unsupported): {missing}")

    banned = sorted({ch for ch in text if ch in ARROWS + GREEK + SUBSUP})
    if banned:
        names = ", ".join(f"U+{ord(ch):04X} {unicodedata.name(ch, '?')}" for ch in banned[:8])
        c.fail(f"banned glyphs present (check_pdf.py check 5 class): {names} — use ASCII '->', '<->', spelled-out Greek")

    unbolded = []
    for n, it in sorted(items.items()):
        if it["archetype"] != "negative":
            continue
        stem = " ".join(it["stem_lines"])
        if not re.search(r"\*\*\s*(not|incorrect|except|wrongly matched|false)\s*\*\*", stem, re.IGNORECASE):
            unbolded.append(f"Q{n}")
    if unbolded:
        c.warn(f"negative-stem items without a bolded negative word: {', '.join(unbolded)}")
    return c


def _norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


# =====================================================================================
# ledger
# =====================================================================================

def emit_ledger(path: Path, qbank_path: Path, anchor, bridges_used, hdr, items, keys,
                checks, verdict, n_fail, n_warn, stamp_now):
    class_label, anchor_dir = anchor
    tiers = {1: 0, 2: 0, 3: 0}
    for it in items.values():
        tiers[it["tier"]] += 1
    kd = {i: 0 for i in (1, 2, 3, 4)}
    for k in keys.values():
        kd[k["correct"]] += 1
    hard = [n for n, it in items.items() if it["tier"] in (2, 3)]
    cross = [n for n in hard if any(p and p != chapter_key(anchor_dir.name)
                                    for p, _f in keys.get(n, {"facts": []})["facts"])]
    arche: dict[str, int] = {}
    for it in items.values():
        arche[it["archetype"]] = arche.get(it["archetype"], 0) + 1
    cited = {(p or chapter_key(anchor_dir.name), f) for k in keys.values() for p, f in k["facts"]}

    lines = [
        f"# QBank Ledger — Class {class_label}, {anchor_dir.name}",
        "",
        "Every number below is **machine-derived by `check_qbank.py` from the bank itself**, ",
        "never copied from the model's run header. Where the header disagreed, the header is the defect.",
        "",
        f"- Bank: `{qbank_path.name}`",
        f"- Build stamp (recomputed): `{stamp_now}`",
        f"- Bridges cited: {', '.join(sorted(bridges_used)) or 'none'}",
        "",
        "## Derived counts",
        "",
        "| Quantity | Derived |",
        "|---|---|",
        f"| Items | {len(items)} |",
        f"| Tier mix T1/T2/T3 | {tiers[1]}/{tiers[2]}/{tiers[3]} |",
        f"| Archetypes | {' · '.join(f'{k}={v}' for k, v in sorted(arche.items()))} |",
        f"| Cross-chapter (Tier-2+3) | {len(cross)}/{len(hard)} |",
        f"| Key distribution | (1)={kd[1]} (2)={kd[2]} (3)={kd[3]} (4)={kd[4]} |",
        f"| Distinct frozen rows cited | {len(cited)} |",
        "",
        "## Gate 4 verdict",
        "",
        f"`check_qbank.py` VERDICT: **{verdict}** ({n_fail} fail, {n_warn} warn)",
        "",
        "| Check | Status | Detail |",
        "|---|---|---|",
    ]
    for c in checks:
        detail = "; ".join(c.detail).replace("|", "/") if c.detail else ""
        lines.append(f"| {c.name} | {c.status} | {detail} |")
    lines += [
        "",
        "## Human adjudication (Gate 4b — not machine-decidable)",
        "",
        "State explicitly, per the Supreme prompt's Gate 3(b) rules: which items were read",
        "against which frozen rows, which flags were investigated and dismissed (keep them,",
        "with reasoning), and any accepted WARN with its justification. A green linter does",
        "not close Gate 4 on its own.",
        "",
        "- Items read against source rows: _____ / " + str(len(items)),
        "- Confirmed defects fixed: ",
        "- Flags investigated and dismissed (do not re-raise): ",
        "- Accepted WARNs and why: ",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# =====================================================================================
# main
# =====================================================================================

def discover(args):
    if args.qbank:
        qb = Path(args.qbank)
        folder = qb.parent
    else:
        folder = Path(args.folder) if args.folder else None
        if not folder or not folder.is_dir():
            print(f"SETUP ERROR: not a folder: {args.folder!r}")
            sys.exit(2)
        cands = [Path(p) for p in glob.glob(str(folder / "*_QBANK.md"))
                 if "_ledger" not in os.path.basename(p)]
        if not cands:
            print(f"SETUP ERROR: no *_QBANK.md in {folder}")
            sys.exit(2)
        qb = sorted(cands)[0]
    if not qb.exists():
        print(f"SETUP ERROR: question bank not found: {qb}")
        sys.exit(2)
    return qb, folder


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Automated Gate 4 (Q-Gate) for NEET question banks — re-derives every "
                    "claim in the run header and verifies every cited fact ID."
    )
    ap.add_argument("folder", nargs="?", help="chapter folder (auto-discovers *_QBANK.md)")
    ap.add_argument("--qbank", help="explicit question-bank .md path")
    ap.add_argument("--json", action="store_true", help="emit JSON report")
    ap.add_argument("--strict", action="store_true", help="treat WARN as failure")
    ap.add_argument("--emit-ledger", action="store_true",
                    help="write <Chapter>_QBANK_ledger.md with the machine-derived numbers")
    args = ap.parse_args()

    if not args.folder and not args.qbank:
        ap.print_help()
        return 2

    qbank_path, folder = discover(args)
    text = _read(qbank_path)
    hdr = parse_header(text)

    # anchor chapter: the folder we were pointed at
    anchor_dir = folder.resolve()
    class_label = None
    for cl, cd in find_chapter_dirs():
        if cd.resolve() == anchor_dir:
            class_label = cl
            break
    if class_label is None:
        print(f"SETUP ERROR: {folder} is not a chapter folder under notes/class N/")
        return 2
    anchor_key = chapter_key(anchor_dir.name)

    inv = find_inventory_file(anchor_dir)
    if inv is None:
        print(f"SETUP ERROR: no *_inventory.md in {anchor_dir} — nothing to ground the bank against")
        return 2
    anchor_facts = parse_facts_table(inv)

    section_a, section_b = split_sections(text)
    items = parse_items(section_a)
    keys = parse_keys(section_b)

    bridges_used = sorted({p for k in keys.values() for p, _f in k["facts"] if p and p != anchor_key})
    bridge_dirs = []
    known_ids = {(anchor_key, f["id"]) for f in anchor_facts}
    for key in bridges_used:
        b_class, b_dir = resolve_key(key)
        if b_dir is None:
            continue
        bridge_dirs.append((b_class, b_dir))
        b_inv = find_inventory_file(b_dir)
        if b_inv:
            known_ids |= {(key, f["id"]) for f in parse_facts_table(b_inv)}

    registry = parse_registry()
    stamp_now = build_stamp((class_label, anchor_dir), bridge_dirs)

    checks = [
        check_provenance(hdr, (class_label, anchor_dir), bridges_used, registry, stamp_now),
        check_structure(hdr, items, keys),
        check_options(items, keys),
        check_key_distribution(hdr, keys),
        check_tier_mix(hdr, items),
        check_grounding(items, keys, known_ids, anchor_key),
        check_cross_chapter(hdr, items, keys, anchor_key),
        check_duplication_and_coverage(items, keys, anchor_facts, anchor_key),
        check_hygiene(hdr, items, text),
    ]
    checks.sort(key=lambda c: c.name)

    n_fail = sum(1 for c in checks if c.status == "FAIL")
    n_warn = sum(1 for c in checks if c.status == "WARN")
    verdict = "FAIL" if n_fail else ("WARN" if n_warn else "PASS")

    if args.emit_ledger:
        ledger = anchor_dir / f"{anchor_dir.name}_QBANK_ledger.md"
        emit_ledger(ledger, qbank_path, (class_label, anchor_dir), bridges_used, hdr,
                    items, keys, checks, verdict, n_fail, n_warn, stamp_now)

    if args.json:
        print(json.dumps({
            "qbank": str(qbank_path), "inventory": str(inv),
            "anchor": anchor_dir.name, "class": class_label,
            "items": len(items), "bridges": bridges_used, "stamp": stamp_now,
            "verdict": verdict, "fail": n_fail, "warn": n_warn,
            "checks": [c.to_dict() for c in checks],
        }, indent=2))
    else:
        print("=" * 78)
        print(f"check_qbank.py — {qbank_path.name}  ({len(items)} items)")
        print(f"anchor: class {class_label} / {anchor_dir.name}   inventory: {inv.name}")
        print(f"bridges cited: {', '.join(bridges_used) or '(none)'}")
        print("=" * 78)
        for c in checks:
            print(f"\n[{c.status}] {c.name}")
            for d in c.detail:
                print(f"       {d}")
        print("\n" + "=" * 78)
        print(f"VERDICT: {verdict}   ({n_fail} fail, {n_warn} warn)")
        print("=" * 78)

    if n_fail or (args.strict and n_warn):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
