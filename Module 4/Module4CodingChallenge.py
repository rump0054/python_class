# Author: Erik Rumppe
# Date: 6/25/2026

# Used PyInputPlus 0.2.12 module to make things more fun and interactive
# pip install pyinputplus
import pyinputplus as pyip
import random

# Create our initial welcome prompts to the user
print("Welcome to the Magical Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("But beware, the number could change if you take too long!")

# Create our initial random secret number and a guess_counter to use in the for loop as a way to generate
# more interactive text even though guess_count is available in the for loop
secret_number = random.randint(1, 100)
guess_counter = 1

while True:
    for guess_count in range(1, 6):  # 5 guesses before the number changes
        # Ask for a guess with a guesses remaining countdown.  
        # Using inputInt to prompt user with automatic error handling for non int and out of range input
        user_prompt_message = "Take a guess.  You have " + str(6 - guess_counter) + " guesses remaining: "
        user_guess = pyip.inputInt(prompt= user_prompt_message, min=1, max=100)

        # Updating the guess_counter before the next code block so it triggers the correct responses based on
        # how many guesses the user has actually made at this point.
        guess_counter = guess_counter + 1

        # Check if the guess is correct, if it is, tell the user they won, print the secret number and break out of the for loop
        if user_guess == secret_number:
            print("You WON!  Amazing job!")
            print("The secret number was: " + str(secret_number))
            break
        # If the guess is incorrect AND user still has more chances to guess remainging, give incorrect try again message
        # and give hints (too high/too low)
        elif guess_counter < 6:
            print("That is incorrect!  Try again!")
            print("Hint - the number is " + ("LOWER" if user_guess > secret_number else "HIGHER"))
        # If the user did not guess the secret number AND has run out of guesses, display losing message and reveal current secret number
        # before asking to play again
        else:
            print("Oh no!  You ran out of guesses!")
            print("The secret number was: " + str(secret_number))
            
    # Ask if the player wants to continue. 
    # If they want to continue, change the secret number to a new random number and reset guess counter
    # If they do not want to continue, break out of the while loop.
    play_again = pyip.inputChoice(['yes', 'no'], prompt='Would you like to play again? (yes/no) ')
    if play_again.lower() == 'yes':
        secret_number = random.randint(1, 100)
        guess_counter = 1
    else:
        break

# Thank the user for playing.
print("Thanks for playing!")