import pymupdf
from PIL import Image
PDF="notes/class 11/Ch19_ChemicalCoordinationAndIntegration/Ch19_ChemicalCoordinationAndIntegration.pdf"
OUT="scratch/ch19_gate3"
doc=pymupdf.open(PDF)
SC=3.0  # 216 dpi

def crop(page_no, y0, y1, x0=40, x1=560, bw=False):
    p=doc[page_no-1]
    clip=pymupdf.Rect(x0,y0,x1,y1)
    pm=p.get_pixmap(matrix=pymupdf.Matrix(SC,SC), clip=clip, colorspace=pymupdf.csGRAY)
    img=Image.frombytes("L",[pm.width,pm.height],pm.samples)
    if bw:
        img=img.point(lambda v:255 if v>200 else 0, mode="L")
    return img

def find(page_no, needle, nth=0):
    p=doc[page_no-1]
    hits=p.search_for(needle)
    return hits[nth] if len(hits)>nth else None

def stack(imgs, path, gap=14):
    w=max(i.width for i in imgs); h=sum(i.height for i in imgs)+gap*(len(imgs)-1)
    out=Image.new("L",(w,h),255); y=0
    for i in imgs:
        out.paste(i,(0,y)); y+=i.height+gap
    out.save(path); print(path, out.size)

# ---- A) NOTE + MEMORY AID boxes, 1-bit, from 3 different points ----
specs=[(1,"[NOTE] Exocrine gland"),(1,"[MEMORY AID"),(9,"[NOTE] Small amounts"),(9,"[MEMORY AID"),(13,"[NOTE] Both Figure"),(13,"[MEMORY AID")]
imgs=[]
for pg,needle in specs:
    r=find(pg,needle)
    if r is None: print("MISS",pg,needle); continue
    imgs.append(crop(pg, r.y0-14, r.y0+70, 40, 560, bw=True))
stack(imgs, f"{OUT}/cmp_boxes_bw.png")

# ---- B) heading banners: H1 (3 instances) + H3 (3 instances) ----
specs=[(1,"ENDOCRINE GLANDS AND HORMONES"),(11,"HORMONES OF HEART"),(11,"MECHANISM OF HORMONE ACTION"),
       (2,"The Hypothalamus"),(7,"Parathyroid Gland"),(10,"Ovary"),(8,"Adrenal medulla - the catecholamines"),(9,"Adrenal cortex - the corticoids"),(13,"Quick recap of the whole chapter"),(14,"Terms the exercises use")]
imgs=[]
for pg,needle in specs:
    r=find(pg,needle)
    if r is None: print("MISS",pg,needle); continue
    imgs.append(crop(pg, r.y0-8, r.y1+6, 40, 560))
stack(imgs, f"{OUT}/cmp_headings.png")

# ---- C) table header rows from 3 points ----
specs=[(1,"Gland type"),(9,"Corticoid class"),(14,"Term as the exercises print it")]
imgs=[]
for pg,needle in specs:
    r=find(pg,needle)
    if r is None: print("MISS",pg,needle); continue
    imgs.append(crop(pg, r.y0-10, r.y1+34, 40, 560))
stack(imgs, f"{OUT}/cmp_tables.png")

# ---- D) process-flow badges from 3 points + figure box top-left corners ----
specs=[(3,"These hormones originate"),(7,"Parathyroid hormone (PTH) increases"),(11,"Blood pressure is increased.")]
imgs=[]
for pg,needle in specs:
    r=find(pg,needle)
    if r is None: print("MISS",pg,needle); continue
    imgs.append(crop(pg, r.y0-10, r.y0+42, 40, 400))
stack(imgs, f"{OUT}/cmp_flow.png")
