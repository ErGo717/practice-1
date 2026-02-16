x=int(input())
y=map(int,input().split())
cnt=1
index=0
mx=-1000000001
for i in y:
    if(i>mx):
        mx=i
        index=pos
    pos+=1
print(index)