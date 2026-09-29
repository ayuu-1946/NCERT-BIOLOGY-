import sys, re, difflib, pymupdf
ref, cur = pymupdf.open(sys.argv[1]), pymupdf.open(sys.argv[2])
norm = lambda t: re.sub(r'\s+', ' ', t).strip()
print('pages ref/cur:', len(ref), len(cur))
for i in range(min(len(ref), len(cur))):
    r, c = norm(ref[i].get_text()), norm(cur[i].get_text())
    print(i + 1, 'start ok' if r[:22] == c[:22] else f'START DIFF ref={r[:35]!r} cur={c[:35]!r}')
print('\nreference image widths (cm):')
for i, p in enumerate(ref):
    for im in p.get_image_info():
        b = im['bbox']; print(' p%d %.1f' % (i + 1, (b[2] - b[0]) / 28.35))
sents = lambda s: [x.strip() for x in re.split(r'(?<=[.;:?!])\s+', s) if x.strip()]
a = sents(' '.join(norm(p.get_text()) for p in cur)); b = sents(' '.join(norm(p.get_text()) for p in ref))
for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
    if tag != 'equal':
        print('\n==', tag)
        for x in a[i1:i2]: print(' CUR', x[:160])
        for x in b[j1:j2]: print(' REF', x[:160])
