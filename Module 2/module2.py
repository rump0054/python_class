# Name: Erik Rumppe
# Date: 6/20/2026
# Description: Fortune Cookie App - Displays personalized fortunes for users
# added random lucky number generator for fun.

import random

# Ask for the user's name
user_name = input("Please enter your name: ")

# Create a fortune message with random lucky number
lucky_number = str(random.randint(1, 100))
fortune = "Get ready me to rock your world!  Your lucky number is " + lucky_number + "."

# Display the fortune
print("Your fortune cookie says:")
print(fortune)

# Create and display thank you message
print("Thank you for using the Fortune Cookie App, " + user_name + "!")
