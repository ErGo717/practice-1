#Strings
print("Bunny")
print('Bunny')

#Quotes Inside Quotes
print("It's alright")
print("He is called 'Bunny'")
print('He is called "Bunny"')

#Multiline Strings
a = """eththst ethaetheat ethaehae hsdhath,
sthtrrs rstrhts rthruktts htyjttn,aehetae
etheahtea bnbdbniuare"""
print(a)

#Strings are Arrays
a = "Hi, Gimmy!"
print(a[2])

#String Length
a = "I can fly!"
print(len(a))

#Check String
txt = "I love eat Pizza!"
print("Pizza" in txt)

txt = "I love eat Pizza!"
if "Pizza" in txt:
  print("Yes, 'Pizza' is present.")

#Slicing String

b = "Hello, Arnold!"
print(b[2:5])
#Negative Indexing
b = "Hello, Arnold!"
print(b[-6:-3])

#Modify Strings

#Upper Case & Lower Case
a = "Hello, World!"
print(a.upper())
print(a.lower())

#Remove Whitespace
a = " I am Spider-man ! "
print(a.strip()) # returns "I am Spider-man!"

#Replace String & Split String
a = "Hello, Bro!"
print(a.replace("H", "r"))

#String Concatenation
a = "Hey"
b = "Bro"
c = a + b
print(c)

#Format Strings (F-Strings)
age = 685
pip = f"My name is Spider man and I am {age}"
print(pip)

#Display the price with 2 decimals
price = 59
neq = f"The price for car is {price:.2f} dollars"
print(neq)

#Escape Characters
txt = "We are the so-called \"Unbeatable people\" from the ancient time."

