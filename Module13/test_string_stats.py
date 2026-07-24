# Author: Erik Rumppe
# Date: 7/24/2026

import unittest
from Module13 import string_stats

class TestMostCommonStrings(unittest.TestCase):
    #### Added 2 unit tests to test the most_common_first_letter method ####
    def test_most_common_first_letters_more_than_5(self):
        """Test that it when there are more than 5 first letters it is correct"""
        letters = ['aa', 'aa', 'bb', 'bb', 'cc', 'cc', 'dd', 'dd', 'ee', 'ee', 'f', 'g']
        result = string_stats.most_common_first_letters(letters)

        self.assertEqual(result, [('a', 2), ('b', 2), ('c', 2), ('d', 2), ('e', 2)])

    def test_most_common_first_letters_less_than_5(self):
        """Test that it when there are less than 5 string it still works"""
        letters = ['aa','aa','bb','bb','g']
        result = string_stats.most_common_first_letters(letters)

        self.assertEqual(result, [('a', 2), ('b', 2), ('g', 1)])



    def test_happy_path(self):
        """Test that it finds the rights strings"""
        letters = ["a", "b", "c", "d", "e", "f"]
        string_list = []
        for i in range(5): # adds the first 5 letters 5 times to the list
            string_list.extend([letters[l] for l in range(5)])
        # this f shouldn't show up in the results because there are only 1 of them
        string_list.append("f")
        # this e should show up first because there are the most of them
        string_list.append("d")
        result = string_stats.most_common_strings(string_list)

        self.assertListEqual(result, [("d", 6), ("a",5), ("b", 5), ("c", 5), ("e",5)])

    def test_order_maintained_on_tie(self):
        """Test that it on ties for last out of the 5, the first items in the list win"""
        letters = ["a", "b", "c", "d", "e", "f"]
        string_list = []
        for i in range(6):
            string_list.extend([letters[l] for l in range(6)])
        result = string_stats.most_common_strings(string_list)

        self.assertListEqual(result, [("a", 6), ("b",6), ("c", 6), ("d", 6), ("e",6)])

    def test_fewer_than_5(self):
        """Test that it when there are fewer than 5 different strings it still works"""
        letters = ["a", "b", "c"]
        string_list = []
        for i in range(3):
            string_list.extend([letters[l] for l in range(3)])
        string_list.append("d")
        result = string_stats.most_common_strings(string_list)

        self.assertListEqual(result, [("a", 3), ("b",3), ("c", 3), ("d", 1)])


class TestAverageStringLength(unittest.TestCase):
    def test_happy_path(self):
        """Test that it finds the rights strings"""
        letters = ["aaa", "bb", "cc", "dd", "ee", "f"]
        result = string_stats.average_length(letters)
        self.assertEqual(result, 2)

    def test_round_to_even(self):
        """test that of the average is in between 2 numbers it rounds to the even number"""
        letters = ["aa", "bb", "ccc", "ddd"]
        result = string_stats.average_length(letters)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()