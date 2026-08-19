"""§0.4 smoke test: fonts, banners, tables, icon badges, process flow, figure+caption, B&W safety."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer,
                                Image, KeepTogether)
from reportlab.graphics.shapes import Drawing, Circle, Rect, Polygon, String
from reportlab.graphics import renderPDF
from PIL import Image as PILImage, ImageDraw
import fitz, os

OUT = "scratch/smoke.pdf"
DARK_GREY = HexColor("#2C2C2C"); MED_GREY = HexColor("#4A4A4A"); SOFT_GREY = HexColor("#6B6B6B")
ROW_ALT = HexColor("#F0F0F0"); NOTE_BG = HexColor("#E8E8E8"); GRID_LINE = HexColor("#AAAAAA")
INK = HexColor("#1A1A1A")

S = {
    "Title": ParagraphStyle("Title", fontName="Times-Bold", fontSize=20, alignment=TA_CENTER),
    "H1": ParagraphStyle("H1", fontName="Times-Bold", fontSize=10.5, textColor=white, backColor=DARK_GREY, borderPadding=3, spaceAfter=6),
    "H2": ParagraphStyle("H2", fontName="Times-Bold", fontSize=9.5, textColor=white, backColor=MED_GREY, borderPadding=2, spaceAfter=5),
    "H3": ParagraphStyle("H3", fontName="Times-Bold", fontSize=9, textColor=white, backColor=SOFT_GREY, borderPadding=2, spaceAfter=4),
    "Body": ParagraphStyle("Body", fontName="Times-Roman", fontSize=10.8, leading=14.2),
    "Bullet1": ParagraphStyle("Bullet1", fontName="Times-Roman", fontSize=10.8, leftIndent=12, firstLineIndent=-8, leading=14.2),
    "NoteBox": ParagraphStyle("NoteBox", fontName="Times-Italic", fontSize=10.2, leading=13.5),
    "Caption": ParagraphStyle("Caption", fontName="Times-Italic", fontSize=9.5, alignment=TA_CENTER, leading=12.5, spaceBefore=3, spaceAfter=8),
}

def sec_badge(txt, size=13):
    d = Drawing(size, size)
    d.add(Rect(0, 0, size, size, fillColor=INK, strokeColor=INK))
    d.add(String(size/2, size*0.28, txt, fontName="Times-Bold", fontSize=size*0.5, fillColor=white, textAnchor="middle"))
    return d

def def_dot(size=8):
    d = Drawing(size, size); d.add(Circle(size/2, size/2, size/2, fillColor=INK, strokeColor=INK)); return d

def tri(size=10):
    d = Drawing(size, size); d.add(Polygon(points=[0,0,size,0,size/2,size], fillColor=INK, strokeColor=INK)); return d

def open_sq(size=9):
    d = Drawing(size, size); d.add(Rect(0.5,0.5,size-1,size-1, fillColor=None, strokeColor=INK, strokeWidth=0.9)); return d

def star(size=11):
    import math
    pts=[]; cx=cy=size/2; R=size/2; r=R*0.42
    for i in range(10):
        ang = math.pi/2 + i*math.pi/5
        rad = R if i%2==0 else r
        pts += [cx+rad*math.cos(ang), cy+rad*math.sin(ang)]
    d = Drawing(size,size); d.add(Polygon(points=pts, fillColor=None, strokeColor=INK, strokeWidth=0.9)); return d

def bang(size=11):
    d = Drawing(size, size)
    d.add(Circle(size/2, size/2, size/2-0.5, fillColor=None, strokeColor=INK, strokeWidth=0.9))
    d.add(Rect(size/2-0.6, size*0.34, 1.2, size*0.34, fillColor=INK, strokeColor=INK))
    d.add(Circle(size/2, size*0.26, 0.8, fillColor=INK, strokeColor=INK))
    return d

def process_flow(steps, cyclic=False):
    rows = []
    if cyclic:
        loop = Drawing(14,10); loop.add(Polygon(points=[2,0,12,0,7,9], fillColor=INK, strokeColor=INK))
        rows.append([loop, Paragraph("<i>(cycle - last step feeds back to step 1)</i>", S["Caption"])])
    for i, s in enumerate(steps, 1):
        rows.append([tri(14), Paragraph(s, S["Bullet1"])])
    t = Table(rows, colWidths=[0.7*cm, None])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LINEAFTER",(0,0),(0,-1),0.75,GRID_LINE),
        ("LEFTPADDING",(0,0),(0,-1),0),("RIGHTPADDING",(0,0),(0,-1),4),
        ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3)]))
    return t

def box(text, kind="NOTE"):
    icon = bang() if kind == "NOTE" else star()
    label = "[NOTE]" if kind == "NOTE" else "[MEMORY AID - not in NCERT]"
    inner = Table([[icon, Paragraph(f"<b>{label}</b> {text}", S["NoteBox"])]], colWidths=[0.55*cm, None])
    inner.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),2),
                              ("TOPPADDING",(0,0),(-1,-1),1),("BOTTOMPADDING",(0,0),(-1,-1),1)]))
    outer = Table([[inner]], colWidths=[None])
    st = [("BACKGROUND",(0,0),(-1,-1),NOTE_BG),("LEFTPADDING",(0,0),(-1,-1),6),
          ("RIGHTPADDING",(0,0),(-1,-1),6),("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5)]
    if kind == "NOTE":
        st += [("BOX",(0,0),(-1,-1),0.5,GRID_LINE),("INNERGRID",(0,0),(-1,-1),0,GRID_LINE)]
    else:
        st += [("BOX",(0,0),(-1,-1),0.75,GRID_LINE,None,(3,2))]
    outer.setStyle(TableStyle(st))
    return outer

# test image
os.makedirs("scratch", exist_ok=True)
img = PILImage.new("RGB", (600, 300), "white"); dr = ImageDraw.Draw(img)
dr.ellipse([50,50,250,250], outline="black", width=4); dr.text((300,140), "TEST FIGURE LABEL", fill="black")
img.save("scratch/test_fig.png")

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=1.5*cm, rightMargin=1.5*cm, topMargin=1.4*cm, bottomMargin=1.4*cm)
story = [Paragraph("Smoke Test Chapter", S["Title"]), Spacer(1, 8)]

def heading(num, text, level):
    b = sec_badge(num, {1:13,2:11.5,3:10}[level])
    p = Paragraph(text, S[f"H{level}"])
    t = Table([[b, p]], colWidths=[0.75*cm, None])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),("LEFTPADDING",(0,0),(-1,-1),0),
                           ("TOPPADDING",(0,0),(-1,-1),2),("BOTTOMPADDING",(0,0),(-1,-1),2)]))
    return t

story += [heading("9", "H1 BANNER SECTION", 1), Paragraph("Body text at 10.8pt with O<sub>2</sub> and Na<super>+</super> and <i>E. coli</i>.", S["Body"])]
story += [heading("9.1", "H2 banner subsection", 2), heading("9.1.1", "H3 banner sub-sub", 3)]
data = [["Header A","Header B","Header C"],["r1","v1","x"],["r2","v2","y"],["r3","v3","z"]]
t = Table(data, repeatRows=1)
st = [("BACKGROUND",(0,0),(-1,0),DARK_GREY),("TEXTCOLOR",(0,0),(-1,0),white),
      ("FONTNAME",(0,0),(-1,0),"Times-Bold"),("FONTNAME",(0,1),(-1,-1),"Times-Roman"),
      ("FONTSIZE",(0,0),(-1,-1),9.5),("GRID",(0,0),(-1,-1),0.4,GRID_LINE),
      ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
      ("LEFTPADDING",(0,0),(-1,-1),4),("RIGHTPADDING",(0,0),(-1,-1),4)]
for i in range(1,len(data)):
    if i%2==0: st.append(("BACKGROUND",(0,i),(-1,i),ROW_ALT))
    st.append(("LINEBELOW",(0,i),(-1,i),0.25,GRID_LINE))
t.setStyle(TableStyle(st))
story += [Spacer(1,4), t, Spacer(1,6)]
story += [process_flow(["First step of the process.","Second step.","Third step feeds onward."], cyclic=True)]
story += [Spacer(1,6), box("This is a factual NOTE from NCERT."), Spacer(1,5), box("SMOKE: mnemonic here.", "MEMORY AID")]
story += [Spacer(1,6), Paragraph("Icons: ", S["Body"])]
ic = Table([[def_dot(), tri(), open_sq(), star(), bang(), sec_badge("9")]], colWidths=[1.2*cm]*6)
story += [ic]
im = Image("scratch/test_fig.png", width=8*cm, height=4*cm)
story += [KeepTogether([im, Paragraph("Fig. 9.1 - Test figure caption.", S["Caption"])])]
doc.build(story)

d = fitz.open(OUT)
pix = d[0].get_pixmap(dpi=140); pix.save("scratch/smoke_render.png")
PILImage.open("scratch/smoke_render.png").convert("L").point(lambda p: 255 if p > 200 else 0).save("scratch/smoke_bw.png")
print("smoke built, pages:", d.page_count)
