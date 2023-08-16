#!/usr/bin/python3
def best_score(a_dictionary):
  """Returns a key with the biggest integer value.

  Args:
    a_dictionary: a dictionary

  You can assume that all values are only integers

  If no score found, return None
  You can assume all students have a different score

  You are not allowed to import any module
  """

  if a_dictionary is None:
    return None

  best_score = -1
  best_key = None
  for key, value in a_dictionary.items():
    if value > best_score:
      best_score = value
      best_key = key

  return best_key
