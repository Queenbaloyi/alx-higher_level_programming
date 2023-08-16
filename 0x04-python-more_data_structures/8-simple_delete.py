#!/usr/bin/python3
def simple_delete(a_dictionary, key):
  """Deletes a key in a dictionary.

  Args:
    a_dictionary: a dictionary
    key: a string

  If a key doesn’t exist, the dictionary won’t change

  You are not allowed to import any module
  """

  if key in a_dictionary:
    del a_dictionary[key]
  return a_dictionary


