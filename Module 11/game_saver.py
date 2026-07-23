# Author: Erik Rumppe
# Date: 7/22/2026

import csv
import sys


class GameState:
    def __init__(self, score: int, level: int, lives: int) -> None:
        try:
            self.score = int(score)
            self.level = int(level)
            self.lives = int(lives)
        except ValueError:
            print("Game state error.  Parms must be integers.")
        except TypeError:
            print("Game state error.  Parms must be integers.")

    def __str__(self):
        return f"score:{self.score} level:{self.level} lives:{self.lives}"

    def toFile(self):
        return f"{self.score},{self.level},{self.lives}"

    def add_to_score(self, amount: int):
        # Add to score after type checking amount
        if not isinstance(amount, int):
            raise TypeError("Score must be a number")
        self.score += amount

    def next_level(self):
        # Adding 1 to the level
        self.level += 1

    def add_or_subtract_lives(self, amount):
        # Implement removing or adding a life. Make sure you don't go below zero
        tmp_lives = self.lives

        if not isinstance(amount, int):
            raise TypeError("Lives must be a number")
        if (tmp_lives + amount) <= 0:
            raise ValueError("Lives must be greater than 0")

        self.lives = tmp_lives + amount


def load_game(file_name):
    # Implement loading the data from a file and building a GameState object, then
    # return it.  Make sure to have default settings (like a new game) and error message
    # if the file is empty or missing and create a new one
    try:
        with open(file_name, 'r') as file:
            file_data = list(csv.reader(file))

            # This should be in the init method of the class.  I hate how unstrict Python is with datatypes!!!
            if not file_data:
                print("Save file error.  Delete save.txt manually to repair.")
                sys.exit()
            elif not file_data[0]:
                print("Save file error.  Delete save.txt manually to repair.")
                sys.exit()

            print(file_data)
            # This is also nasty code. I hate doing all the data conversions 100 times in code.  Not sure where to
            # put to it in python.  Should be part of the class.
            return GameState(int(file_data[0][0]), int(file_data[0][1]), int(file_data[0][2]))
    except FileNotFoundError:
        # If file is missing, create save file and set default game settings
        print("Save file missing.  Creating new one with default game settings.")
        with open(file_name, 'w') as file:
            writer = csv.writer(file)
            writer.writerow([0, 1, 5])

        # Loop back around to load file and create default game state object
        load_game(file_name)


def save_game(game_state, file_name):
    # Implement saving a GameState object to a file
    try:
        with open(file_name, 'w') as file:
            writer = csv.writer(file)
            # print(game_state.toFile())
            writer.writerow([game_state.score, game_state.level, game_state.lives])
    except FileNotFoundError:
        print("Save file error.  Restart program to create default environment.")


def main():
    try:
        game = load_game("save.txt")
        print(game)

        game.next_level()
        game.next_level()
        game.add_to_score(6000)
        game.add_or_subtract_lives(50)
        print(game)

        game.add_or_subtract_lives(-54)
        print(game)

        save_game(game, "save.txt")

        # delete the game to simulate quitting after it is saved
        del game
        # now your data is gone

        game = load_game("save.txt")
        print(game)
    except Exception as err:
        print(f"Error happened. {err}")


if __name__ == "__main__":
    main()