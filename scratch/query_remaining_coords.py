import pymupdf
SRC='Chapter/class 11/Chapter 11 - Photosynthesis in Higher Plants.pdf'
d=pymupdf.open(SRC)
for pno in (6,7,14):
 print('PAGE',pno)
 for w in d[pno-1].get_text('words'):
  if (pno==6 and 350<w[1]<700) or (pno==7 and 100<w[1]<680) or (pno==14 and 400<w[1]<560):
   print(w[4],tuple(round(v,1) for v in w[:4]))
