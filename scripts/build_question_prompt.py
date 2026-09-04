#!/usr/bin/env python3
"""
build_question_prompt.py — assemble a ready-to-paste NEET question-generation
prompt for one chapter, with zero manual copy-pasting of source text.

This is the **entry point of Gate 4 (the Q-Pass)** described in
`SUPREME COMMAND PROMPT.md` §7 and `NEET_QUESTION_GENERATION_PROMPT.md`. It
does what the operator should not have to do by hand:

  1. Refuses to build unless the anchor chapter's **Gate 3 is closed** in
     `CHAPTER_TRACKER.md`. A question bank inherits the trustworthiness of the
     inventory it is generated from, so generating from an ungated chapter
     produces items that look rigorous and rest on unverified rows.
  2. Locates the chapter's frozen Facts inventory (the verified NCERT source
     ledger — not the raw PDF, not model memory).
  3. Resolves cross-chapter "bridge" chapters **from the registry table in the
     prompt's APPENDIX** (the single source of truth; this script keeps no
     second copy), drops any bridge whose own Gate 3 is still open, and pulls
     the Facts tables of the ones that survive.
  4. Fills in {{CLASS}}/{{CHAPTER}}/{{COUNT}}/{{STAMP}}/{{BRIDGES}} and appends
     the SUPPLIED NCERT SOURCE TEXT section built from those Facts tables.
  5. Writes the assembled prompt to
     `scratch/question_prompts/<chapter>_prompt.md`.

Every parser it uses (chapter resolution, Facts-table parse, registry parse,
tracker status, build stamp) is **imported from `check_qbank.py`**, so the
builder and the gate cannot drift apart about what a bridge or a fact ID is.

Usage — always through the venv interpreter (§0.2; bare `python3` is the
two-interpreter trap):

    /vercel/share/neetenv/bin/python scripts/build_question_prompt.py --class 11 --chapter Ch4
    /vercel/share/neetenv/bin/python scripts/build_question_prompt.py --class 12 --chapter Ecosystem --count 60
    /vercel/share/neetenv/bin/python scripts/build_question_prompt.py --class 11 --chapter Ch4 --list-bridges

`--chapter` matches by substring (case-insensitive) against the chapter
directory name: "Ch4", "Ch4_AnimalKingdom", "AnimalKingdom", "animal kingdom"
all resolve to the same chapter.

`--allow-open-gates` exists for drafting only. It stamps the prompt
`PROVISIONAL` and `check_qbank.py` then FAILs Gate 4 by design — a provisional
bank can be experimented with but can never be recorded as closed.
"""

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from check_qbank import (  # noqa: E402  (path bootstrap must precede the import)
    PROMPT_PATH as PROMPT_TEMPLATE,
    build_stamp,
    bridges_for,
    chapter_key,
    chapter_topic_name,
    find_chapter_dirs,
    find_inventory_file,
    parse_facts_table,
    parse_registry,
    resolve_chapter,
    resolve_key,
    tracker_status,
)

OUTPUT_DIR = REPO_ROOT / "scratch" / "question_prompts"


def format_facts_block(label: str, facts) -> str:
    if not facts:
        return (f"### {label}\n"
                "_No inventory Facts table found. This chapter supplies NO usable source text; "
                "any item leaning on it is UNGROUNDED and must be omitted._\n")
    lines = [f"### {label} — {len(facts)} supplied source facts (frozen inventory rows)"]
    for f in facts:
        lines.append(f"- **{f['id']}** [{f['section']}] ({f['type']}): {f['wording']}")
    return "\n".join(lines) + "\n"


def resolve_bridges(anchor_dir: Path, registry):
    """
    Return (usable, rejected) bridge chapters.

    Usable = registered bridge + exists under notes/ + Gate 3 closed + has a
    Facts table. Everything else is rejected with its reason, and the reasons
    are written into the prompt so the model knows those links are unavailable
    rather than silently inventing them.
    """
    linked = bridges_for(chapter_key(anchor_dir.name), registry)
    usable, rejected = [], []
    for key in sorted(linked):
        b_class, b_dir = resolve_key(key)
        if b_dir is None:
            rejected.append((key, "no chapter folder under notes/ yet"))
            continue
        status = tracker_status(b_class, b_dir)
        if status != "DONE":
            rejected.append((key, f"Gate 3 {status.lower()} — facts not gate-verified"))
            continue
        b_inv = find_inventory_file(b_dir)
        facts = parse_facts_table(b_inv) if b_inv else []
        if not facts:
            rejected.append((key, "no Facts table in its inventory"))
            continue
        usable.append((b_class, b_dir, facts))
    return usable, rejected


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--class", dest="class_arg", required=True, help='e.g. "11" or "12"')
    parser.add_argument("--chapter", dest="chapter_arg", required=True, help='e.g. "Ch4", "AnimalKingdom"')
    parser.add_argument("--count", dest="count", default="45", help="number of questions (default 45)")
    parser.add_argument("--list-bridges", action="store_true",
                        help="report the registry bridges and their gate state, then exit")
    parser.add_argument("--allow-open-gates", action="store_true",
                        help="draft from an ungated chapter; stamps PROVISIONAL and cannot close Gate 4")
    args = parser.parse_args()

    class_label, ch_dir, ambiguous = resolve_chapter(args.class_arg, args.chapter_arg)
    if class_label == "AMBIGUOUS":
        print("Ambiguous chapter query. Matches:", file=sys.stderr)
        for cl, cd in ambiguous:
            print(f"  class {cl}: {cd.name}", file=sys.stderr)
        return 2
    if ch_dir is None:
        print(f"No chapter found matching class={args.class_arg!r} chapter={args.chapter_arg!r}",
              file=sys.stderr)
        return 2

    topic = chapter_topic_name(ch_dir)
    registry = parse_registry()
    if not registry:
        print(f"SETUP ERROR: no bridge registry parsed from {PROMPT_TEMPLATE.name}'s APPENDIX table.",
              file=sys.stderr)
        return 2

    usable, rejected = resolve_bridges(ch_dir, registry)

    if args.list_bridges:
        print(f"Class {class_label} — {ch_dir.name} ({topic}); anchor Gate 3: "
              f"{tracker_status(class_label, ch_dir)}")
        print(f"Registry bridges usable ({len(usable)}):")
        for b_class, b_dir, facts in usable:
            print(f"  + {b_dir.name} (class {b_class}, {len(facts)} facts)")
        print(f"Registry bridges rejected ({len(rejected)}):")
        for key, why in rejected:
            print(f"  - {key}: {why}")
        return 0

    # ---- Gate 4 precondition -------------------------------------------------
    anchor_status = tracker_status(class_label, ch_dir)
    if anchor_status != "DONE" and not args.allow_open_gates:
        print(
            f"GATE 4 BLOCKED: class {class_label} {ch_dir.name} is {anchor_status}, not Done in "
            "CHAPTER_TRACKER.md.\nA question bank is only as sound as the inventory it cites, and an "
            "un-closed chapter's rows have not survived Pass 3.\nClose Gate 3 first, or pass "
            "--allow-open-gates to draft a PROVISIONAL bank that cannot close Gate 4.",
            file=sys.stderr,
        )
        return 1

    inventory_path = find_inventory_file(ch_dir)
    if inventory_path is None:
        print(f"SETUP ERROR: no *_inventory.md in {ch_dir}", file=sys.stderr)
        return 2
    anchor_facts = parse_facts_table(inventory_path)
    if not anchor_facts:
        print(f"SETUP ERROR: {inventory_path.name} has no parseable Facts table — "
              "the anchor chapter supplies no source text.", file=sys.stderr)
        return 2

    stamp = build_stamp((class_label, ch_dir), [(b[0], b[1]) for b in usable])
    if anchor_status != "DONE":
        stamp = f"PROVISIONAL-{anchor_status}-{stamp}"

    bridge_labels = [f"{chapter_key(b_dir.name)} (class {b_class} {chapter_topic_name(b_dir)})"
                     for b_class, b_dir, _f in usable]

    if not PROMPT_TEMPLATE.exists():
        print(f"Missing template: {PROMPT_TEMPLATE}", file=sys.stderr)
        return 2

    filled = (
        PROMPT_TEMPLATE.read_text(encoding="utf-8")
        .replace("{{CLASS}}", class_label)
        .replace("{{CHAPTER}}", f"{ch_dir.name} ({topic})")
        .replace("{{COUNT}}", str(args.count))
        .replace("{{STAMP}}", stamp)
        .replace("{{BRIDGES}}", ", ".join(chapter_key(b[1].name) for b in usable) or "none")
    )

    source_sections = [format_facts_block(
        f"ANCHOR CHAPTER — Class {class_label}, {ch_dir.name} ({topic}) — cite these as bare `F###`",
        anchor_facts,
    )]
    for b_class, b_dir, b_facts in usable:
        source_sections.append(format_facts_block(
            f"BRIDGE CHAPTER — Class {b_class}, {b_dir.name} ({chapter_topic_name(b_dir)}) — "
            f"cite these as `{chapter_key(b_dir.name)}:F###`",
            b_facts,
        ))

    rejected_note = (
        "\n".join(f"- `{key}` — UNAVAILABLE: {why}" for key, why in rejected)
        or "- (none — every registered bridge for this anchor is supplied above)"
    )

    source_block = (
        "\n\n---\n\n"
        "## SUPPLIED NCERT SOURCE TEXT (auto-assembled — the ONLY text you may treat as ground truth)\n\n"
        f"Build stamp: `{stamp}`  ·  Anchor: **Class {class_label} — {ch_dir.name} ({topic})**  ·  "
        f"Anchor Gate 3: **{anchor_status}**\n\n"
        f"Bridge chapters supplied ({len(usable)}): "
        f"{', '.join(bridge_labels) if bridge_labels else 'none — every Tier-2/3 item must fuse facts inside the anchor chapter'}\n\n"
        "**Citation contract.** Anchor facts are cited bare (`F012`); bridge facts are cited with their "
        "chapter key (`BodyFluidsAndCirculation:F031`). `check_qbank.py` resolves every ID you write "
        "against these exact tables, so an invented ID is a hard FAIL, not a stylistic slip.\n\n"
        "**Bridges deliberately withheld** — do not link to these; NCERT may support the connection, but "
        "this repo has not gate-verified the facts, so any such link is UNGROUNDED:\n"
        f"{rejected_note}\n\n"
        + "\n".join(source_sections)
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / f"{ch_dir.name}_prompt.md"
    out_path.write_text(filled + source_block, encoding="utf-8")

    print(f"Chapter resolved: Class {class_label} — {ch_dir.name} ({topic})  [Gate 3: {anchor_status}]")
    print(f"Anchor facts supplied: {len(anchor_facts)}")
    print(f"Bridge chapters supplied: {len(usable)} -> "
          f"{', '.join(chapter_key(b[1].name) for b in usable) or '(none)'}")
    if rejected:
        print(f"Bridges withheld: {len(rejected)} -> " +
              ", ".join(f"{k} ({why})" for k, why in rejected))
    print(f"Build stamp: {stamp}")
    print(f"Assembled prompt written to: {out_path.relative_to(REPO_ROOT)}")
    print("Paste that file's contents into the model. Nothing else to attach.")
    print(f"Then gate the result: /vercel/share/neetenv/bin/python check_qbank.py "
          f"\"notes/class {class_label}/{ch_dir.name}\" --emit-ledger")
    return 0


if __name__ == "__main__":
    sys.exit(main())
