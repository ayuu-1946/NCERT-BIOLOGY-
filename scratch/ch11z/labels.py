import importlib.util, collections
spec=importlib.util.spec_from_file_location("cp","check_pdf.py"); cp=importlib.util.module_from_spec(spec); spec.loader.exec_module(cp)
inv="notes/class 11/Ch11_PhotosynthesisInHigherPlants/Ch11_PhotosynthesisInHigherPlants_inventory.md"
res=cp._extract_labels(open(inv,encoding="utf-8").read())
print(type(res))
try:
    items=list(res.items())
    print("figures:", len(items))
    tot=0
    for k,v in items:
        print(" ", k, len(v))
        tot+=len(v)
    print("total labels:", tot)
    allv=[x for _,v in items for x in v]
    dups=[x for x,c in collections.Counter(allv).items() if c>1]
    print("labels appearing in >1 place:", dups)
except AttributeError:
    print(res[:20], len(res))
