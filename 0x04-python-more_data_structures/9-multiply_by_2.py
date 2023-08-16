#!/usr/bin/python3
def multiply_by_2(a_dictionary):
  """Returns a new dictionary with all values multiplied by 2.

  Args:
    a_dictionary: a dictionary

  You can assume that all values are only integers

  Returns a new dictionary

  You are not allowed to import any module
  """

  new_dictionary = {}
  for key, value in a_dictionary.items():
    new_value = value * 2
    new_dictionary[key] = new_value
  return new_dictionary
