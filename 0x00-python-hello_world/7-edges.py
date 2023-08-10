#!/usr/bin/python3
my_word = "Holberton"
first_3_letters = slice(0, 3)
last_2_letters = slice(-2, None)
middle_word = slice(1, -1)
print("First 3 letters: {}".format(my_word[first_3_letters]))
print("Last 2 letters: {}".format(my_word[last_2_letters]))
print("Middle word: {}".format(my_word[middle_word]))
