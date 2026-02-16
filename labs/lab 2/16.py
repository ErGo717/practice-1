x=int(input())
a=list(map(int,input().split()))
b=set({})
for i in range(x):
    if not(a[i] in b):
        print("YES")
        b.add(a[i])
    else:
        print("NO")