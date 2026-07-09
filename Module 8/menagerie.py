# Author: Erik Rumppe
# Date: 7/8/2026

# Create Animal class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # What an instance returns when called as a string
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Speak function
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Create Animal subclasses with method speak overridden
class Dog(Animal):
    def speak(self, sound = "Woof"):
        return super().speak(sound)

class Duck(Animal):
    def speak(self, sound = "Quack"):
        return super().speak(sound)

class Pig(Animal):
    def speak(self, sound = "Oink"):
        return super().speak(sound)

class Cat(Animal):
    def speak(self, sound = "Meow"):
        return super().speak(sound)

# Create Animal and print
bob = Animal("Bob", 5)
print(bob)

# Create Dog and print dog then print speak
bob = Dog("Bob", 5)
print(bob)
print(bob.speak())

# Create several types of Animals
winston = Dog("Winston", 12)
loki = Dog("Loki", 4)
delilah = Cat("Delilah", 2)
howard = Duck("Howard", 52)
babe = Pig("Babe", 30)

# Creat list of several different types of animals and print
menagerie = [winston, loki, delilah, howard, babe]
for creature in menagerie:
    print(creature)
    print(creature.speak())

# Given a list of items, check instance of each for animal and print the animal
menagerie2 = [1, winston, 2, loki, delilah, "hello world", howard, babe]
for creature in menagerie2:
    if isinstance(creature, Animal):
        print(creature)
        print(creature.speak())

# Playing around with class comparisons methods.
a = Animal("Joe", 12)
b = Animal("Joe", 12)
c = Cat("Joe", 12)
d = Dog("Joe", 12)

print("Playing around with class comparisons methods.")
print(a == b)  # This should be true. Hmmmm... does this require a __compare__ type thing
print(a == c)
print(a == d)
print(c == d)