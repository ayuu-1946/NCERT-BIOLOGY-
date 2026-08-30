import importlib.util
from pathlib import Path
from PIL import Image
root=Path(__file__).resolve().parents[1]
inv=root/'notes/class 12/Ch2_HumanReproduction/Ch2_HumanReproduction_inventory.md'
assets=root/'notes/class 12/Ch2_HumanReproduction/assets'
spec=importlib.util.spec_from_file_location('check',root/'check_pdf.py'); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
text=inv.read_text()
labels=mod._extract_labels(text)
assert len(set(fig_id for fig_id, _ in labels))==14, len(set(fig_id for fig_id, _ in labels))
ids=[]
for line in text.splitlines():
    if line.startswith('| F') and line.split('|')[1].strip().startswith('F') and line.split('|')[1].strip()[1:].isdigit():
        ids.append(line.split('|')[1].strip())
assert ids==[f'F{i:03d}' for i in range(1,15)], ids
files=sorted(assets.glob('fig_*.png'))
assert len(files)==14, len(files)
for p in files:
    im=Image.open(p)
    assert im.mode=='L', (p,im.mode)
    assert im.width>=100 and im.height>=100, (p,im.size)
print('inventory_label_rows=',len(labels))
print('inventory_label_count=',len(labels))
print('facts_ids=',','.join(ids))
print('asset_count=',len(files))
print('all_assets_mode=L_and_dimensions_ok=yes')
print('chapter_pdf_present=',(root/'notes/class 12/Ch2_HumanReproduction/Ch2_HumanReproduction.pdf').exists())
