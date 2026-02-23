# Iterator and generator exercises

#1.
def squares_up_to(n):
    for i in range(1, n + 1):
        yield i * i


#2.
def evens(n):
    for i in range(0, n + 1, 2):
        yield i
n = int(input("Enter n: "))
print(",".join(str(x) for x in evens(n)))


#3.
def div_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 12 == 0:
            yield i
n = int(input("Enter n: "))
for x in div_by_3_and_4(n):
    print(x)


#4.
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i
a = int(input("Enter a: "))
b = int(input("Enter b: "))
for x in squares(a, b):
    print(x)


#5.
def countdown(n):
    for i in range(n, -1, -1):
        yield i
n = int(input("Enter n: "))
for x in countdown(n):
    print(x)