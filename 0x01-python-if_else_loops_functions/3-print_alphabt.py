#!/usr/bin/python3
def print_alphabet_without_q_and_e():
  """This function prints the alphabet without the letters 'q' and 'e'."""
  for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
      print(chr(letter), end="")

print_alphabet_without_q_and_e()
