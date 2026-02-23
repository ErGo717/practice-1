def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input())

first = True
for num in even_generator(n):
    if first:
        print(num, end="")
        first = False
    else:
        print("," + str(num), end="")