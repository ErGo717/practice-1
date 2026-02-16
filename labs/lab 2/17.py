n = int(input())
d = {}
for i in range(n):
    s = input()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
cnt = 0
for k in d:
    if d[k] == 3:
        cnt += 1
print(cnt)
