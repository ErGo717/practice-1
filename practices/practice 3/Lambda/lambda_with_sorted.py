items = [("Notebook", 1200), ("Pencil", 300), ("Backpack", 4500)]
sorted_items = sorted(items, key=lambda x: x[1])
print(sorted_items)

words = ["window", "sun", "mountain", "sky"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

numbers = [5, -2, 7, 0, -9, 3, -1]
sorted_numbers = sorted(numbers, key=lambda x: abs(x))
print(sorted_numbers)
