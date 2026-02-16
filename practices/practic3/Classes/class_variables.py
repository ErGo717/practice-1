class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

x= Person("Erkebulan", 19)
print(x.age)

x.age = 27
print(x.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

y = Person("Erkebulan", 21)

del y.age

print(y.name)
