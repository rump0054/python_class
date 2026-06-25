# Author: Erik Rumppe
# Date: 6/25/2026

import random
import os
import pyinputplus as pyip

# Create dad_jokes list using external txt file to populate the list
# As long as you are running this out of the correct folder, it should find the file which needs to be ANSI
jokes_file_path = os.getcwd() + "\\jokes_ansi.txt"

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

    # Ask if the user wants to see more jokes. 
    # If they do not want to continue, break out of the while loop otherwise restart loop by default
    play_again = pyip.inputChoice(['yes', 'no'], prompt='Would you like to see more jokes? (yes/no) ')
    if play_again.lower() == 'no':
        break

# Thank the user
print("Thank you for using the Dad Jokes Randomizer!")