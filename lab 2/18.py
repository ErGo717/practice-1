n = int(input())
d = {}

for i in range(1, n + 1):
    s = input()
    if s not in d:
        d[s] = i  

for k in sorted(d):
    print(k, d[k])
