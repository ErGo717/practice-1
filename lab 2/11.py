n, l, r = map(int, input().split())
a = list(map(int, input().split()))

for i in range(l - 1):
    print(a[i], end=' ')

for i in range(r - 1, l - 2, -1):
    print(a[i], end=' ')

for i in range(r, n):
    print(a[i], end=' ')