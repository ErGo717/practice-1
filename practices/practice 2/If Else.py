a = 75
b = 150
if a < b:
    print("a is less than b")
else:
    print("a is not less than b")

#The Else Keyword
a = 50
b = 75
if a > b:
    print("a is bigger than b")
elif a != b:
    print("a and b are not equal")
else:
    print("b is bigger than a")
    
#How Else Works
number = 10
if number % 2 != 0:
    print("The number is odd")
else:
    print("The number is even")
    
#Else as Fallback
username = "Alex"
if len(username) >= 1:
    print(f"Hello, {username}!")
else:
    print("Error: Name cannot be blank")
    
x=input()
if (not (x=="student")):
    print("yor are not a student")
else:
    print("you are a student")