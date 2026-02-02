a = 120
b = 180
if b < a:
    print("b is smaller than a")
elif a != b:
    print("a and b are not equal")
else:
    print("a is smaller than b")
    
#Complete If-Elif-Else Chain
temperature = 15
if temperature > 35:
    print("It's very hot outside!")
elif temperature > 25:
    print("It's pleasantly warm outside")
elif temperature > 5:
    print("It's a bit chilly outside")
else:
    print("It's very cold outside!")


score = 85
if score > 100:
    print("You got a perfect score!")
elif score > 70:
    print("You passed with a good score")
elif score > 50:
    print("You barely passed")
else:
    print("You failed the game")

speed = 90

if speed > 150:
    print("You are driving way too fast!")
elif speed > 100:
    print("You are speeding")
elif speed > 60:
    print("You are driving at a normal speed")
else:
    print("You are driving slowly")


age = 25
if age > 60:
    print("You are a senior citizen")
elif age > 30:
    print("You are middle-aged")
elif age > 18:
    print("You are a young adult")
else:
    print("You are a minor")