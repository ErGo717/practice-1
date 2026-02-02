#Short Hand If
a = 3
b = 8
if a < b: print("a is less than b")
#Short Hand If ... Else
a = 500
b = 33
print("YES") if a > b else print("NO")

#Assign a Value With If ... Else

a = 4
b = 25
bigger = a if a < b else b
print("The larger number is", bigger)

#Multiple Conditions on One Line

a = 120
b = 450
print("LEFT") if a > b else print("SAME") if a == b else print("RIGHT")

#Practical Examples

x = 42
y = 17
max_value = x if x > y else y
print("Largest number:", max_value)

username = ""
display_name = username if username else "Anonymous"
print("Hi,", display_name)