from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

squared_numbers = list(map(lambda x: x * x, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
total_sum = reduce(lambda a, b: a + b, numbers)

print("Original numbers:", numbers)
print("Squared numbers using map():", squared_numbers)
print("Even numbers using filter():", even_numbers)
print("Sum using reduce():", total_sum)

print("\nOther built-in functions:")
print("len(numbers):", len(numbers))
print("sum(numbers):", sum(numbers))
print("min(numbers):", min(numbers))
print("max(numbers):", max(numbers))

string_numbers = ["10", "20", "30"]
converted_numbers = list(map(int, string_numbers))
print("\nType conversion:")
print("Original string list:", string_numbers)
print("Converted to integers:", converted_numbers)
print("Sorted descending:", sorted(converted_numbers, reverse=True))