x=int(input())
c=False
for i in range(2,x):
    if(not(i*i<=x)):
        break
    if (x%i==0):
        c=True
        break
if(c):
    print("NO")
else:
    print("YES")