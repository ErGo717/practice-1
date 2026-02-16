class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Erkebulan", 20)

print(p1.name)
print(p1.age)

class Person:
  pass

p1 = Person()
p1.name = "Erkebulan"
p1.age = 19

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Sultan", 22)

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Erkebulan")
p2 = Person("Sanzhar", 21)

print(p1.name, p1.age)
print(p2.name, p2.age)

class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Erkebulan", 20, "Almaty", "Kazakhstan")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)
