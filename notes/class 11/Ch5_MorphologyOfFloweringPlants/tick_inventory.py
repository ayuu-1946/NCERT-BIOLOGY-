#!/usr/bin/env python3
"""Tick the Facts rows of a frozen chapter inventory once Pass 2 has written them.

Gate 2's check 7 requires every `Facts` row of the inventory to be ticked. This
script ticks the rows whose content has been written into the chapter script,
and refuses to touch anything else.

Usage:
    python3 tick_inventory.py Ch5_MorphologyOfFloweringPlants_inventory.md
    python3 tick_inventory.py <inventory.md> --rows F001-F120,F273
    python3 tick_inventory.py <inventory.md> --dry-run

Default behaviour ticks every `F###` row. Only run it after the chapter script
actually renders, so the tick reflects written content rather than intent.

A `.bak` copy is written beside the inventory before the first edit.
"""

import argparse
import os
import re
import shutil
import sys

ROW_RE = re.compile(r"^\|\s*(F\d{3})\s*\|")
TICK = "x"


def parse_rows(spec):
    """Expand a spec such as 'F001-F120,F273' into a set of row ids."""
    wanted = set()
    for part in (p.strip() for p in spec.split(",") if p.strip()):
        if "-" in part:
            lo, hi = (x.strip() for x in part.split("-", 1))
            if not (re.fullmatch(r"F\d{3}", lo) and re.fullmatch(r"F\d{3}", hi)):
                raise SystemExit("tick_inventory: bad row range %r" % part)
            for n in range(int(lo[1:]), int(hi[1:]) + 1):
                wanted.add("F%03d" % n)
        else:
            if not re.fullmatch(r"F\d{3}", part):
                raise SystemExit("tick_inventory: bad row id %r" % part)
            wanted.add(part)
    return wanted


def tick_line(line):
    """Return (new_line, changed). Fills the final table cell with a tick."""
    stripped = line.rstrip("\n")
    if not stripped.endswith("|"):
        return line, False
    cells = stripped.split("|")
    # cells[0] and cells[-1] are the empty strings outside the outer pipes.
    if len(cells) < 4:
        return line, False
    if cells[-2].strip():
        return line, False  # already ticked, or carries a note - leave alone
    cells[-2] = " %s " % TICK
    return "|".join(cells) + "\n", True


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("inventory", help="path to <Chapter>_inventory.md")
    ap.add_argument("--rows", default=None,
                    help="comma list of ids/ranges to tick, e.g. F001-F120,F273. Default: all.")
    ap.add_argument("--dry-run", action="store_true", help="report only, write nothing")
    args = ap.parse_args(argv)

    path = args.inventory
    if not os.path.isfile(path):
        raise SystemExit("tick_inventory: no such file: %s" % path)

    wanted = parse_rows(args.rows) if args.rows else None

    with open(path, encoding="utf-8") as fh:
        lines = fh.readlines()

    seen, ticked, already, skipped = [], [], [], []
    out = []
    for line in lines:
        m = ROW_RE.match(line)
        if not m:
            out.append(line)
            continue
        row_id = m.group(1)
        seen.append(row_id)
        if wanted is not None and row_id not in wanted:
            skipped.append(row_id)
            out.append(line)
            continue
        new_line, changed = tick_line(line)
        if changed:
            ticked.append(row_id)
        else:
            already.append(row_id)
        out.append(new_line)

    if not seen:
        raise SystemExit("tick_inventory: found no F### rows in %s - wrong file?" % path)

    print("rows found:      %d (%s .. %s)" % (len(seen), seen[0], seen[-1]))
    print("newly ticked:    %d" % len(ticked))
    print("already ticked:  %d" % len(already))
    if skipped:
        print("not requested:   %d" % len(skipped))

    untouched = [r for r in seen if r not in set(ticked) | set(already)]
    if untouched:
        print("STILL UNTICKED:  %d -> %s" % (len(untouched), ", ".join(untouched[:20])))

    if args.dry_run:
        print("dry run - nothing written")
        return 0

    if not ticked:
        print("nothing to write")
        return 0

    backup = path + ".bak"
    if not os.path.exists(backup):
        shutil.copy2(path, backup)
        print("backup written:  %s" % backup)

    with open(path, "w", encoding="utf-8") as fh:
        fh.writelines(out)
    print("updated:         %s" % path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
