x=int(input())
y=list(map(int,input().split()))
maxi=[0]*2001

for i in range(x):
    maxi[y[i]+1000]+=1
num=max(maxi)
mass=[]
for i in range(len(maxi)):
    if(maxi[i]==num):
        mass.append(i-1000)
print(min(mass))
