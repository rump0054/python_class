# Author: Erik Rumppe
# Date: 6/25/2026

import random

goldfish = ["Bubbles", "Finley", "Goldie", "Splash", "Nemo"]

print("Welcome to the Goldfish Playdate Planner!")
print("Our goldfish friends are: " + ", ".join(goldfish))

new_fish = input("Enter the name of a new goldfish: ")
goldfish.append(new_fish)

print("Updated goldfish list: " + ", ".join(goldfish))

fish_to_remove = input("Enter the name of a goldfish to remove: ")
if fish_to_remove in goldfish:
    goldfish.remove(fish_to_remove)
    print(fish_to_remove + " has been removed from the list.")
else:
    print("Sorry, " + fish_to_remove + " is not in the list.")

print("Current goldfish list: " + ", ".join(goldfish))

print("\nLet's create some playdate pairs!")
random.shuffle(goldfish)

for i in range(0, len(goldfish), 2):
    if i + 1 < len(goldfish):
        print(goldfish[i] + " will have a playdate with " + goldfish[i+1])
    else:
        print(goldfish[i] + " will have a solo play session.")