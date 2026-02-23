def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = int(input())

first = True
for num in fibonacci(n):
    if first:
        print(num, end="")
        first = False
    else:
        print("," + str(num), end="")