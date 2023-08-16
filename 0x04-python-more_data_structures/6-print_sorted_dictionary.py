def print_sorted_dictionary(a_dictionary):
  """Prints a dictionary by ordered keys.

  Args:
    a_dictionary: a dictionary

  You can assume that all keys are strings
  Keys should be sorted by alphabetic order
  Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
  Dictionary values can have any type
  You are not allowed to import any module
  """

  keys = sorted(a_dictionary.keys())
  for key in keys:
    print("{:s}: {:s}".format(key, a_dictionary[key]))
