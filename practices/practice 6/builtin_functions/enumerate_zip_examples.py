names = ["Erkebulan", "Nursultan", "Dana"]
scores = [95, 88, 91]

print("Using enumerate():")
for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")

print("\nUsing zip():")
for name, score in zip(names, scores):
    print(f"{name} -> {score}")

print("\nType checking and conversions:")
value = "123"
print("Original value:", value, "| type:", type(value))

converted_int = int(value)
converted_float = float(value)
converted_str = str(converted_int)

print("As int:", converted_int, "| type:", type(converted_int))
print("As float:", converted_float, "| type:", type(converted_float))
print("Back to string:", converted_str, "| type:", type(converted_str))

print("\nChecking types with isinstance():")
print("Is converted_int an int?", isinstance(converted_int, int))
print("Is names a list?", isinstance(names, list))