# Author: Erik Rumppe
# Date: 7/22/2026

import csv
import sys

# Constants
SAVE_FILE = "save.txt"

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
            print("Fatal: Game state error.  Parms must be integers.  Delete save file.")
            sys.exit()
        except TypeError:
            print("Fatal: Game state error.  Parms must be integers.  Delete save file.")
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
    # If file not found, creates file and writes default game save and creates default GameState.
    # Returns GameState.
    try:
        with open(file_name, 'r') as file:
            file_data = list(csv.reader(file))

            # Checks to make sure save file is not empty and is properly formatted
            # Raises FileNotFoundError to trigger file repair methods - should be custom error type
            if not file_data:
                print("Save file empty.")
                raise FileNotFoundError
            elif not file_data[0]:
                print("Save file format error.")
                raise FileNotFoundError

            # Rough init method for GameState but needs to be integers
            # If a non int is passed, object init causes sys.exit
            g = GameState(file_data[0][0], file_data[0][1], file_data[0][2])
    except FileNotFoundError:
        # If file is missing, create save file and write default game settings
        print("Creating new save file with default game settings.")
        with open(file_name, 'w') as file:
            writer = csv.writer(file)
            writer.writerow([0, 1, 5])

        # Create a default GameState object
        g = GameState(0,1,5)

    # Return GameState
    return g


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
        # Load game or create new one using default setup and check save file exists and properly formatted or
        # create new one
        game = load_game(SAVE_FILE)

        # Print initial game
        print(f"Initial game setup:\n {game}")

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