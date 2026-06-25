# Author: Erik Rumppe
# Date: 6/25/2026

# Set constants
CAPACITY = 3

# Create list to store animal names
animal_names = {}

# Adds a new animal to the shelter if not at capacity
def add_animal(name, species, animals): 
    if get_animal_count(animals) < CAPACITY:
        animals[name] = species
        print(name + " has been added to the shelter.")
    else:
        print("Sorry! Couldn't add " + name + ".  The shelter is full!")

    return animals

# Removes an animal from the shelter when adopted.
def adopt_animal(name, animals):
    if find_animal(name, animals):
        animals.pop(name)
        print(name + " has been removed from the shelter.")
    else:
        print("Sorry, " + name + " is not in the list.")

    return animals

# Returns the total number of animals in the shelter.
def get_animal_count(animals):
    return len(animals)

# Method returns boolean if it finds the key in the dictonary 
def find_animal(name, animals):
    if name in animals:
        return True
    else:
        return False

# Get animals by species returns a list or message saying species not found
def get_animals_by_species(species, animals):
    name_list = []
    
    for x, y in animals.items():
        if y == species:
            name_list.append(x)
    
    if len(name_list) == 0:
        print("Sorry!  No " + species + " was found in the list.")

    return name_list

# Add 5 animals to set shelter to capacity
animal_names = add_animal("Kirby", "Dog", animal_names)
animal_names = add_animal("Kitty", "Cat", animal_names)
animal_names = add_animal("Joe", "Dog", animal_names)
animal_names = add_animal("Orville", "Cat", animal_names)
animal_names = add_animal("Joey", "Kangaroo", animal_names)

# Print current animal info in the shelter
print("Number of animals in the shelter: " + str(get_animal_count(animal_names)))
print("Current animal list: " + ", ".join(animal_names) + "\n")

# Attempt to add one too many animals to shelter
animal_names = add_animal("Bob", "Dog", animal_names)

# Print current animal info in the shelter
print("Number of animals in the shelter: " + str(get_animal_count(animal_names)))
print("Current animal list: " + ", ".join(animal_names) + "\n")

# Adopt an animal from the shelter
animal_names = adopt_animal("Orville", animal_names)

# Print current animal info in the shelter 
# 4 animals remain and Orville is out of the list
print("Number of animals in the shelter: " + str(get_animal_count(animal_names)))
print("Current animal list: " + ", ".join(animal_names))

# Get dogs and print list of names
animal_species = get_animals_by_species("Dog", animal_names)
if len(animal_species) !=0:
    print("\nCurrent dogs list: " + ", ".join(animal_species)) 

# Get snakes and print list of names
animal_species = get_animals_by_species("Snake", animal_names)
if len(animal_species) !=0:
    print("Current snakes list: " + ", ".join(animal_species))