import sys
n = int(sys.stdin.readline())
d = {}
for _ in range(n):
    parts = sys.stdin.readline().split()
    if parts[0] == "set":
        d[parts[1]] = " ".join(parts[2:])
    else:
        key = parts[1]
        if key in d:
            sys.stdout.write(d[key] + "\n")
        else:
            sys.stdout.write(f"KE: no key {key} found in the document\n")