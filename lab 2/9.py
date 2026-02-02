x=int(input())
y=list(map(int,input().split()))
mx=max(y)
mn=min(y)
for i in range(x):
    if(y[i]==mx):
        y[i]=mn
for i in y:
    print(i,end=" ")