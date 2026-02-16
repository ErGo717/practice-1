x=int(input())
y=list(map(int,input().split()))
y.sort()
for i in range(x):
    print(y[x-1-i],end=" ")