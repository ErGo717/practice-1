class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hi, I am " + self.name)

a = Person("Erkebulan")
a.greet()

class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(8, 4))
print(calc.multiply(6, 9))

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Erkebulan", 19)
print(p1.get_info())

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Congrats! Now you are {self.age}")

x = Person("Erkebulan", 20)
x.celebrate_birthday()
x.celebrate_birthday()

class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("My list")
my_playlist.add_song("Blinding Lights")
my_playlist.add_song("Levitating")
my_playlist.show_songs()
