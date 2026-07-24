# Author: Erik Rumppe
# Date: 7/22/2026

import csv
import sys
import pyinputplus as pyip

# Constants
SAVE_FILE = "save.txt"

# Class GameState
class GameState:
    # init method with attempts to apply data conversion at instantiation
    # Throws errors if invalid params and hard exits as error must be fatal
    # to ensure incomplete object isn't instantiated.
    def __init__(self, score, level, lives):
        try:
            self.score = int(score)
            self.level = int(level)
            self.lives = int(lives)
        except ValueError:
            print("Fatal: Game state error.  Parms must be positive integers.")
            sys.exit()
        except TypeError:
            print("Fatal: Game state error.  Parms must be positive integers.")
            sys.exit()

    def __str__(self):
        return f"score:{self.score} level:{self.level} lives:{self.lives}"

    def add_to_score(self, amount: int):
        # Add to score after type checking amount as int, throw errors to main
        if not isinstance(amount, int):
            raise TypeError("Score must be a number")
        self.score += amount

    def next_level(self):
        # Adding 1 to the level
        self.level += 1

    def add_or_subtract_lives(self, amount):
        # Removing or adding a life - error checking for invalid argument types and values thrown
        # to main with messages
        tmp_lives = self.lives

        if not isinstance(amount, int):
            raise TypeError("Lives must be a number")
        if (tmp_lives + amount) <= 0:
            raise ValueError("Lives must be greater than 0")

        self.lives = tmp_lives + amount

def load_game(file_name):
    # Loading the data from a file and build the GameState object.
    # If file not found, creates file, writes default game save, and creates default GameState.
    # Returns GameState.
    try:
        with open(file_name, 'r') as file:
            file_data = list(csv.reader(file))

            # Run multiple data validation steps on file_data.
            # Method returns a tuple that is either empty or has 3 int values
            tmp_state = validate_save_file_data(file_data)
            if not tmp_state:
                raise FileNotFoundError

            # If we have passed all checks and validations to this point it is safe to create and
            # return our saved GameState object.
            g = GameState(tmp_state[0], tmp_state[1], tmp_state[2])
    except FileNotFoundError:
        # If file is missing or fails validation, create save file and write default game settings
        print("Error with save data.  Creating new save file with default game settings.")

        # Create a default GameState object and save to file
        g = GameState(0,1,5)
        save_game(g, file_name)

    # Return GameState
    return g

def validate_save_file_data(save_data):
    # Performs validations on the save file data, returns tuple
    # First check is the file is not empty.
    # Second check is that there is data on the first line in the file
    if not save_data:
        print("Save file exists but is empty.")
        return ()
    elif not save_data[0]:
        print("Save file exists but data is improperly formatted.")
        return ()

    # Third check is a try except block to validate there are 3 positive int values
    try:
        tmp_score = int(save_data[0][0])
        tmp_level = int(save_data[0][1])
        tmp_lives = int(save_data[0][2])

        if tmp_score >= 0 and tmp_level >= 1 and tmp_lives > 0:
            return tmp_score, tmp_level, tmp_lives
        else:
            raise Exception
    except Exception:
        print("Save file contains invalid information or is corrupted.")
        return ()

def save_game(game_state, file_name):
    # Saves a GameState object to save file
    try:
        with open(file_name, 'w') as file:
            writer = csv.writer(file)
            writer.writerow([game_state.score, game_state.level, game_state.lives])
    except FileNotFoundError:
        # Should never happen unless file is unavailable while application runs
        print("Save file error.  Restart program to create default environment.")


def main():
    try:
        # Ask user if they want to Load game or start a new one
        new_save_game = pyip.inputChoice(['yes', 'no'], prompt='Do you want to load a saved game? (yes/no): ')

        if new_save_game.lower() == 'yes':
            print("Loaded game setup: ")
            game = load_game(SAVE_FILE)
        else:
            print("New game setup: ")
            # Default GameState setup
            game = GameState(0,1,5)

        # Print initial game
        print(f"{game}")

        # Mess with game and print current variables
        game.next_level()
        game.next_level()
        game.add_to_score(6000)
        game.add_or_subtract_lives(50)
        print(f"Game with 2 level ups, score plus 6000, and lives plus 50:\n {game}")

        # Subtract several lives.
        # Eventually when using saved data it will throw an opps that lives is less than zero
        print("Game minus 54 lives:")
        game.add_or_subtract_lives(-54)
        print(f"{game}")

        # Save game to file
        save_game(game, SAVE_FILE)

        # delete the game to simulate quitting after it is saved
        del game
        # now your data is gone

        # Load save game data
        # Only error not handled is if save file data contains quotes
        game = load_game(SAVE_FILE)
        print(f"Final game loaded from save file:\n {game}")
    except Exception as err:
        # Catch all exceptions including ones raised as validation errors
        print(f"Opps! {err}")


if __name__ == "__main__":
    main()