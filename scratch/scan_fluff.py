import ast, glob, os, re, json
HP = {"Ch14","Ch15","Ch16","Ch17","Ch18","Ch19"}
PAT = [
 (r"\b(in )?(your )?(earlier|previous|lower) (classes|class|chapter|chapters)\b","Back-reference"),
 (r"\byou (have|had) (already )?(studied|learnt|learned|read|looked|seen|come across)\b","Back-reference"),
 (r"\blet us\b|\blet's\b","Invitation filler"),
 (r"\bwe (shall|will) (now |also |briefly )?(study|discuss|learn|look|examine|consider|see)\b","Roadmap filler"),
 (r"\byou (will|would|shall) (now )?(study|learn|read|find|see|appreciate)\b","Roadmap filler"),
 (r"\bin this chapter\b","Roadmap filler"),
 (r"\?(\s|$)","Rhetorical question"),
 (r"\b(interestingly|surprisingly|amazingly|fascinating|wonderful|beautiful|remarkable|astonishing)\b","Editorial adjective"),
 (r"\b(as you know|as we know|you (may|might|must) (be )?(know|aware|wonder|recall|remember)|have you (ever )?(wondered|thought|noticed|seen))\b","Reader address"),
 (r"\b(think|imagine|try to|can you|do you)\b","Reader address"),
 (r"\b(obviously|of course|naturally|indeed|in fact|actually|basically|simply)\b","Hedge/filler adverb"),
 (r"\b(it is (interesting|important|worth) (to note )?(that)?|it (should|may|must) be (noted|remembered|mentioned))\b","Throat-clearing"),
 (r"\b(a very|very much|quite a|rather|somewhat|a lot of|various)\b","Vague quantifier"),
]
def strings(path):
    src=open(path).read(); tree=ast.parse(src); out=[]
    for n in ast.walk(tree):
        if isinstance(n,ast.Call):
            for a in n.args:
                try: v=ast.literal_eval(a)
                except Exception: continue
                if isinstance(v,str) and len(v)>60: out.append((n.lineno,v))
    return out
res={}
for p in sorted(glob.glob("notes/class */Ch*/Ch*.py")):
    ch=os.path.basename(os.path.dirname(p)); cls=p.split("/")[1]
    if cls=="class 11" and ch.split("_")[0] in HP: continue
    if "extract" in p: continue
    hits=[]; seen=set()
    for ln,s in strings(p):
        clean=re.sub(r"<[^>]+>","",s).strip()
        if clean in seen: continue
        tags=sorted({t for r,t in PAT if re.search(r,clean,re.I)})
        if tags: seen.add(clean); hits.append({"line":ln,"text":clean,"tags":tags})
    res[f"{cls}/{ch}"]=hits
    print(f"{cls}/{ch}: {len(hits)}")
json.dump(res,open("scratch/fluff_hits.json","w"),indent=1)
