import json
import sys
sys.setrecursionlimit(10000)

def serialize(val):
    if val == "<missing>":
        return val
    return json.dumps(val, separators=(',',':'))

def deep_diff(a, b, path=""):
    diffs = []
    keys = set(a.keys()) | set(b.keys())
    for key in keys:
        new_path = f"{path}.{key}" if path else key
        va = a.get(key, "<missing>")
        vb = b.get(key, "<missing>")
        if isinstance(va, dict) and isinstance(vb, dict):
            diffs.extend(deep_diff(va, vb, new_path))
        elif va != vb:
            diffs.append(f"{new_path} : {serialize(va)} -> {serialize(vb)}")
    return diffs

obj1 = json.loads(input())
obj2 = json.loads(input())
diffs = deep_diff(obj1, obj2)
if diffs:
    for line in sorted(diffs):
        print(line)
else:
    print("No differences")