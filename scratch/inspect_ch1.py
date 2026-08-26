import pymupdf
for name in ["scratch/ch1_release/lebo101.pdf","scratch/ch1_release/lebo102.pdf"]:
    doc = pymupdf.open(name)
    print("="*60)
    print(name, "pages:", doc.page_count)
    for i in range(doc.page_count):
        p = doc[i]
        words = p.get_text("words")
        imgs = p.get_images(full=True)
        txt = p.get_text().strip().replace("\n"," ")
        print(f" p{i+1}: {round(p.rect.width,1)}x{round(p.rect.height,1)} words={len(words)} imgs={len(imgs)} :: {txt[:80]}")
