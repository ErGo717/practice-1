n = int(input())
d = {}

for i in range(n):
    name, k = input().split()
    k = int(k)

    if name in d:
        d[name] += k
    else:
        d[name] = k

for name in sorted(d):
    print(name, d[name])