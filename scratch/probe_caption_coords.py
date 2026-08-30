import pdfplumber
src='Chapter/class 12/Chapter 2 - Human Reproduction.pdf'
with pdfplumber.open(src) as pdf:
    for pno in range(1,13):
        page=pdf.pages[pno-1]
        words=page.extract_words()
        hits=[w for w in words if w['text'].lower().startswith('figure')]
        if hits:
            print('p',pno,[(w['text'],round(w['x0'],1),round(w['top'],1),round(w['x1'],1),round(w['bottom'],1)) for w in hits])
