# Author: Erik Rumppe
# Date: 6/25/2026

import random

# Changed fuel to 70 from initial 100
fuel = 70
planets_visited = 0
alien_encounters = 0

print("Welcome aboard the Python Explorer!")
print("Initial fuel: ")
print(fuel)
print("Mission: Visit 5 planets and meet 3 friendly aliens.")

while fuel > 0 and planets_visited < 5:
    print("\nCurrent fuel: ")
    print(fuel)
    print("Planets visited: ")
    print(planets_visited)
    
    fuel -= 20
    planets_visited += 1
    
    print("Visiting planet ")
    print(planets_visited)
    
print("\nMission status:")
if planets_visited == 5:
    print("Success! You've visited all 5 planets.")
else:
    print("Mission failed. You did not visit all of the planets before running out of fuel.")

friendly_aliens = ["Zorg", "Blip", "Glorp", "Xena", "Qwark"]

print("\nTime to meet some aliens!")
for alien in friendly_aliens:
    # Set alien_encounters to 5 from 3 to meet all the aliens
    if alien_encounters >= 5:
        break
    
    print("You've met "+ alien + "!")
    alien_encounters += 1

print("\nYou've encountered ")
print(alien_encounters)
print("friendly aliens.")