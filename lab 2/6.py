x = int(input())
a = map(int, input().split())
mx = -10**9-1
for v in a:
    if v > mx:
        mx = v
print(mx)