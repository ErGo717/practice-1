print(True and True)#true
print(True and False)#false
print(False or True)#true
print(False or False)#false

m=True 
d=False
print(m and d)
print(m or d)
print(not m,not d)

#some basic examples
profit=int(input())
race=input()
print(profit>=999999 and race=="Asian")

prof=input()
print(not (prof=="engineer"))

#some adavanced logic operators
a=True
b=False
print(a^b) #this is xor
print((a^b)==((a and not b) or (not a and  b))) #def of the xor

a=True
b=False
imp=(not a) or b #this is an impication
print(imp)

a=True
b=False
eq=(a==b)
print(a==b) #This is the  equivalence
