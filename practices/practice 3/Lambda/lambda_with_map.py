values = [3, 6, 9, 12, 15]
tripled = list(map(lambda n: n * 3, values))
print(tripled)

labels = ["Book", "Pen", "Phone"]
same = list(map(lambda t: t, labels))
print(same)

nums = [7, -4, 2, -11]
positives = list(map(lambda n: abs(n), nums))
print(positives)
