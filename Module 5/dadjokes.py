# Author: Erik Rumppe
# Date: 6/25/2026

import random
import pyinputplus as pyip
from pathlib import Path

# Create dad_jokes list using external txt file to populate the list (must be ANSI encoded)
# As long as you are running this script out of the same directory the file is in it will work
script_dir = Path(__file__).parent
jokes_file_path = script_dir / "jokes_ansi.txt"

with open(jokes_file_path, 'r') as file:
    dad_jokes = [line.rstrip() for line in file]

# Display number of jokes in the list using len() and str()
# Output should read -  We have x dad jokes in our collection.
dad_jokes_quantity = len(dad_jokes)
print("We have " + str(dad_jokes_quantity) + " dad jokes in our collection.")

# Added while loop to ask if user wants to see more jokes or exit the program
while True:
    # Display random jokes
    # Use loop that runs 4 times
    # In each iteration:
    # Use random.choice(dad_jokes) to select a random joke from the list.  Print this joke.
    for i in range(4):
        print(random.choice(dad_jokes))

    # Ask if the user wants to see another joke. 
    # If they do not want to continue, break out of the while loop otherwise restart loop by default
    while True:
        play_again = pyip.inputChoice(['yes', 'no'], prompt='\nWould you like to see another joke? (yes/no): ')
        if play_again.lower() == 'yes':
            print(random.choice(dad_jokes))
        else:
            break
    break

# Thanks to the user
print("Thank you for using the Dad Jokes Randomizer!")