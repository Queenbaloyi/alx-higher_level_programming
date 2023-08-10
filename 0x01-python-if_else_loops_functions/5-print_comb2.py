#!/usr/bin/python3

def print_numbers(start_number, end_number):
  """Prints a list of numbers from start_number to end_number, formatted as two-digit strings.

  Args:
    start_number: The first number to print.
    end_number: The last number to print.
  """

  for number in range(start_number, end_number + 1):
    if number == end_number:
      print(number)
    else:
      print("{:02}".format(number), end=", ")

if __name__ == "__main__":
  print_numbers(0, 100)
