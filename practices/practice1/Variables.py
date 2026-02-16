#Creating Variables
x = 10
y = "Sandy"
print(x)
print(y)

x = 6       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Get the Type
x = 5
y = "John"
print(type(x))
print(type(y))

#Variable Names
myvar = "Wow"
my_var = "Wow"
_my_var = "Wow"
myVar = "Wow"
MYVAR = "Wow"
myvar7 = "Wow"

#Assign Multiple Values
x, y, z = "Fanta", "Apple", "Mango"
print(x)
print(y)
print(z)
#Output Variables
x = "World "
y = "is "
z = "awesome"
print(x + y + z)

#Global Variables
x = "awesome"

def myfunc():
  x = "fantastic"
  print("World is " + x)

myfunc()

print("World is " + x)

#The global Keyword
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("World is " + x)