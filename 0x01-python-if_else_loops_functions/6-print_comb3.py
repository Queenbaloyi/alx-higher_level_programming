#!/usr/bin/python3

def print_combinations(digits):
  """Print all possible different combinations of two digits from the given list.

    The two digits must be different - 01 and 10 are considered identical.
    """
  for digit1 in digits:
    for digit2 in digits:
      if digit1 != digit2:
        if digit1 == 8 and digit2 == 9:
          print("{}{}".format(digit1, digit2))
        else:
          print("{}{}".format(digit1, digit2), end=" ")

if __name__ == "__main__":
  digits = list(range(0, 10))
  for i in range(len(digits) - 1):
    for j in range(i + 1, len(digits)):
      if digits[i] != digits[j]:
        if digits[i] == 8 and digits[j] == 9:
          print("{}{}".format(digits[i], digits[j]))
        else:
          print("{}{}".format(digits[i], digits[j]), end=" ")
