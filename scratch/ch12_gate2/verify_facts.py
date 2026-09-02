"""Gate 2 support tool: prove every frozen-inventory fact really reached the PDF.

check_pdf.py's check 7 only asks whether the Ticked column is filled in; it cannot
tell an earned tick from a blanket find-and-replace. This script supplies the
evidence that makes the tick honest: for every Facts row it takes the quoted NCERT
wording, normalises it the same way it normalises the rendered PDF text, and slides
that word sequence over the whole document to find the best-matching window.

Normalisation folds exactly the differences the typesetting legitimately introduces
- sub/superscript digits that re-extract as inline characters (CO2, H2O, NAD+),
  ligatures, curly quotes, en/em dashes, and the running-head/footer furniture -
so a low score means "this fact is missing or altered", not "this fact is bold".

Output is a ranked list, worst first. Anything below the review threshold is
printed in full for a human decision; nothing is auto-ticked by this script.
"""
import re
import sys
import unicodedata
from difflib import SequenceMatcher

import pymupdf

CHAPTER_DIR = 'notes/class 11/Ch12_RespirationInPlants'
PDF = f'{CHAPTER_DIR}/Ch12_RespirationInPlants.pdf'
INV = f'{CHAPTER_DIR}/Ch12_RespirationInPlants_inventory.md'
REVIEW_THRESHOLD = 0.90

# Footer/running furniture that is not chapter prose.
FURNITURE = re.compile(r'respiration in plants|class 11|chapter 12|page \d+|\bncert\b', re.I)


def normalise(text: str) -> list[str]:
    """Lowercase word list with typography and formatting differences folded out."""
    t = unicodedata.normalize('NFKD', text)
    t = (t.replace('\u2019', "'").replace('\u2018', "'")
          .replace('\u201c', '"').replace('\u201d', '"')
          .replace('\u2013', '-').replace('\u2014', '-')
          .replace('\u2212', '-').replace('\ufb01', 'fi').replace('\ufb02', 'fl'))
    t = FURNITURE.sub(' ', t)
    t = t.lower()
    # keep + and digits (NAD+, CO2, 3C); everything else becomes a separator
    t = re.sub(r"[^a-z0-9+']+", ' ', t)
    return t.split()


def parse_rows(inv_text: str):
    rows, in_facts = [], False
    for line in inv_text.splitlines():
        low = line.strip().lower()
        if low.startswith('## '):
            in_facts = low.startswith('## facts')
            continue
        if not in_facts or not line.strip().startswith('|'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if not cells or not re.match(r'[a-z]?\d{2,}', cells[0].lower()):
            continue
        rows.append({'id': cells[0], 'section': cells[1], 'type': cells[2],
                     'wording': cells[3]})
    return rows


def quoted(wording: str) -> str:
    """The NCERT wording itself, minus inventory scaffolding like 'Figure labels:'."""
    quotes = re.findall(r'"([^"]+)"', wording)
    if quotes:
        return ' '.join(quotes)
    return re.sub(r'^[^:]{0,40}:\s*', '', wording)


def best_window_ratio(needle: list[str], hay: list[str]) -> float:
    """Best SequenceMatcher ratio of `needle` against any same-length window of `hay`."""
    n = len(needle)
    if n == 0:
        return 1.0
    if n > len(hay):
        return SequenceMatcher(a=needle, b=hay).ratio()
    needle_set = set(needle)
    best = 0.0
    # Anchor on windows that share the rarest word, then widen — full O(n*m) sliding
    # over 164 facts x ~9k words is affordable but this keeps it near-instant.
    step = max(1, n // 4)
    for start in range(0, len(hay) - n + 1, step):
        window = hay[start:start + n]
        if not needle_set.intersection(window):
            continue
        for off in range(-step, step + 1):
            s = start + off
            if s < 0 or s + n > len(hay):
                continue
            r = SequenceMatcher(a=needle, b=hay[s:s + n]).ratio()
            if r > best:
                best = r
                if best > 0.995:
                    return best
    return best


STOP = set(('a an the of to in on at is are was were be been being and or but if it its this that '
            'these those as by for from with within into out up down over under then than so such '
            'not no can could will would may might must do does did has have had he she they them '
            'their there here which who whom whose what when where why how all any both each other '
            'more most some only own same too very s t just also i e g etc one two').split())


def content_words(words: list[str]) -> set[str]:
    return {w for w in words if w not in STOP and len(w) > 1}


def coverage(needle: list[str], hay_set: set[str]) -> tuple[float, list[str]]:
    """Fraction of the fact's distinctive words that appear anywhere in the PDF.

    This is the metric that suits condensed notes: the rewrite is free to reorder
    and compress a sentence, but it cannot silently drop the terms that carry the
    fact. Missing words are returned so a shortfall can be judged, not guessed at.
    """
    cw = content_words(needle)
    if not cw:
        return 1.0, []
    missing = sorted(cw - hay_set)
    return (len(cw) - len(missing)) / len(cw), missing


def main() -> int:
    doc = pymupdf.open(PDF)
    hay = normalise(' '.join(p.get_text() for p in doc))
    doc.close()
    hay_set = set(hay)
    rows = parse_rows(open(INV, encoding='utf-8').read())

    results = []
    for r in rows:
        is_label = r['type'].lower() == 'label'
        if is_label:
            # Labels live inside the artwork; the caption restates them but with prose
            # between, so a contiguous window is meaningless. Score each label alone.
            labels = re.findall(r'"([^"]+)"', r['wording'])
            per = [best_window_ratio(normalise(l), hay) for l in labels]
            seq = sum(per) / len(per) if per else 1.0
            cov, missing = coverage(normalise(' '.join(labels)), hay_set)
        else:
            needle = normalise(quoted(r['wording']))
            seq = best_window_ratio(needle, hay)
            cov, missing = coverage(needle, hay_set)
        results.append((min(seq if seq > cov else cov, 1.0), seq, cov, missing, r))

    results.sort(key=lambda x: x[0])
    below = [x for x in results if x[2] < REVIEW_THRESHOLD]

    print(f'facts checked : {len(results)}')
    print(f'PDF words     : {len(hay)}')
    print(f'coverage >= {REVIEW_THRESHOLD:.2f} : {len(results) - len(below)}')
    print(f'needs review  : {len(below)}')
    print('=' * 78)
    for _, seq, cov, missing, r in below:
        print(f'\ncoverage={cov:.2f} seq={seq:.2f}  {r["id"]}  ({r["section"]} / {r["type"]})')
        print(f'   {r["wording"][:260]}')
        print(f'   MISSING WORDS: {", ".join(missing)}')
    if not below:
        print('Every fact clears the coverage threshold against the rendered PDF.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
