def limited_cycle(lst, n):
    for _ in range(n):
        for item in lst:
            yield item

lst = input().split()
n = int(input())

first = True
for x in limited_cycle(lst, n):
    if first:
        print(x, end="")
        first = False
    else:
        print(" " + str(x), end="")