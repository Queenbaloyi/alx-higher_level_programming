#!/usr/bin/python3
def number_keys(a_dictionary):
  """Returns the number of keys in a dictionary.

  Args:
    a_dictionary: a dictionary

  Returns:
    The number of keys in the dictionary

  You are not allowed to import any module
  """

  number_of_keys = 0
  for key in a_dictionary:
    number_of_keys += 1
  return number_of_keys
