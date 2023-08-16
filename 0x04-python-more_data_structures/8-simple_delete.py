#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
  """Replaces or adds key/value in a dictionary.

  Args:
    a_dictionary: a dictionary
    key: a string
    value: any type

  If a key exists in the dictionary, the value will be replaced
  If a key doesn’t exist in the dictionary, it will be created

  You are not allowed to import any module
  """

  if key in a_dictionary:
    a_dictionary[key] = value
  else:
    a_dictionary[key] = value
  return a_dictionary
