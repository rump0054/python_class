# Author: Erik Rumppe
# Date: 7/24/2026

from collections import Counter

# get the data from a file
def read_file_into_lines(file_string):
    """Read a file and copy each line to an array of Strings"""
    with open(file_string, "r") as file:
        return file.read().splitlines()

def most_common_strings(strings):
    """Returns the 10 most common strings and their counts in a list of tuples"""
    string_counts = Counter(strings)
    return string_counts.most_common(5)

def average_length(strings):
    """Returns the average string length rounded to the nearest integer"""
    return round(sum([len(string) for string in strings]) / len(strings))

def most_common_first_letters(strings):
    """Returns the 5 most common first letters"""
    first_letters = (string[0] for string in strings)
    letter_counts = Counter(first_letters)
    return letter_counts.most_common(5)

def find_letter_length_correlation(strings):
    """return the starting letters and the average length of string for that letter"""
    first_letters = set([string[0] for string in strings])
    letter_lengths = {}
    for letter in sorted(first_letters):
        letter_lengths[letter] = average_length([string for string in strings if string[0] == letter])
    return letter_lengths

