import pymupdf, hashlib, os, shutil, subprocess, sys
D="notes/class 11/Ch19_ChemicalCoordinationAndIntegration"
NAME="Ch19_ChemicalCoordinationAndIntegration"
PDF=os.path.join(D,NAME+".pdf")
def fp(path):
    d=pymupdf.open(path)
    txt="".join(p.get_text() for p in d)
    imgs=sum(len(p.get_images(full=True)) for p in d)
    return (len(d), len(txt), imgs, hashlib.sha256(txt.encode()).hexdigest()[:16])
before=fp(PDF); print("committed  :", before)
aside=PDF+".aside"; shutil.copy2(PDF, aside)
r=subprocess.run([sys.executable, os.path.join(D,NAME+".py")], capture_output=True, text=True)
print(r.stdout.strip() or r.stderr.strip()[-200:])
after=fp(PDF); print("rebuilt    :", after)
print("content-identical:", before==after)
b1=open(aside,'rb').read(); b2=open(PDF,'rb').read()
print("byte-identical   :", b1==b2, "| size delta:", len(b2)-len(b1))
shutil.copy2(aside, PDF); os.remove(aside)
print("committed PDF restored; fingerprint now:", fp(PDF))
