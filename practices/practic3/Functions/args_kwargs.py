def pick_third(*options):
  print("The third option is " + options[2])

pick_third("Tea", "Coffee", "Cocoa")


def inspect_args(*items):
  print("Type:", type(items))
  print("First item:", items[0])
  print("Second item:", items[1])
  print("All items:", items)

inspect_args("Red", "Green", "Blue")


def say_many(prefix, *words):
  for w in words:
    print(prefix, w)

say_many("Welcome,", "Erkebulan", "Dias", "Timur")


def add_numbers(*nums):
  total = 0
  for n in nums:
    total += n
  return total

print(add_numbers(4, 5, 6))
print(add_numbers(12, 8, 3, 7))
print(add_numbers(9))


def find_max(*nums):
  if len(nums) == 0:
    return None
  max_num = nums[0]
  for n in nums:
    if n > max_num:
      max_num = n
  return max_num

print(find_max(14, 2, 19, 7, 11))


def show_profile(**person):
  print("City is " + person["city"])

show_profile(name = "Erkebulan", city = "Almaty")
