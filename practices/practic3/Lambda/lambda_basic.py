y = lambda n : n + 750
print(y(6))

y = lambda p, q : p * q
print(y(4,5))

y = lambda x1, x2, x3 : x1 + x2 + x3
print(y(2, 7, 3))

y = lambda name : "user is " + name
print(y("Erkebulan"))

y = lambda a, b : a if a>b else b
print(y(9,4))

y = lambda arr : max(arr)
print(y([2,8,6,105]))
