import pymupdf,re
src='Chapter/class 11/Chapter 07 - Structural Organisation in Animals.pdf'
with pymupdf.open(src) as doc:
 for pno in [17,18,19]:
  p=doc[pno-1]; print(f'--- PAGE {pno} ---'); print(p.get_text())
