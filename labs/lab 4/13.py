import json
import re

def resolve_query(data, query):
    tokens = re.findall(r'\w+|\[\d+\]', query)
    current = data
    try:
        for token in tokens:
            if token.startswith('['):
                idx = int(token[1:-1])
                current = current[idx]
            else:
                current = current[token]
        return json.dumps(current, separators=(',',':'))
    except (KeyError, IndexError, TypeError):
        return "NOT_FOUND"

data = json.loads(input())
q = int(input())
for _ in range(q):
    query = input().strip()
    print(resolve_query(data, query))