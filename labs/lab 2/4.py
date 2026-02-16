n = int(input())
a = input().split()
cnt = 0
for x in a:
    if int(x) > 0:
        cnt += 1
print(cnt)
