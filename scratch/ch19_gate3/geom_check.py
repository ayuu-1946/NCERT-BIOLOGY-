import pymupdf, os
from PIL import Image
D="notes/class 11/Ch19_ChemicalCoordinationAndIntegration"
PDF=os.path.join(D,"Ch19_ChemicalCoordinationAndIntegration.pdf")
A=os.path.join(D,"assets")
doc=pymupdf.open(PDF)
print("--- embedded image display box vs asset native aspect ---")
assets=sorted(os.listdir(A))
native={f: Image.open(os.path.join(A,f)).size for f in assets}
for f,(w,h) in native.items():
    im=Image.open(os.path.join(A,f))
    print(f"{f:16s} native {w}x{h} ar={w/h:.4f} mode={im.mode}")
print()
for i,p in enumerate(doc,1):
    for info in p.get_image_info(xrefs=True):
        r=info["bbox"]; w=r[2]-r[0]; h=r[3]-r[1]
        print(f"p{i:02d} displayed {w:.1f}x{h:.1f}pt ar={w/h:.4f}  (src px {info['width']}x{info['height']} ar={info['width']/info['height']:.4f})")
print()
print("--- content extent per page (frame is y 39.7..802.3, x 42.5..552.5) ---")
for i,p in enumerate(doc,1):
    b=[]
    for blk in p.get_text("blocks"): b.append(blk[3])
    for info in p.get_image_info(): b.append(info["bbox"][3])
    for d in p.get_drawings(): b.append(d["rect"].y1)
    bot=max(b) if b else 0
    top=min([blk[1] for blk in p.get_text("blocks")]+[info["bbox"][1] for info in p.get_image_info()]+[d["rect"].y0 for d in p.get_drawings()])
    print(f"p{i:02d} top={top:7.1f} bottom={bot:7.1f} fill={(bot-39.7)/(802.3-39.7)*100:5.1f}%")
