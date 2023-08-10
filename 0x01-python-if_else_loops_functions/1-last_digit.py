#!/usr/bin/python3
import random

def find_last_digit(number):
  """Finds the last digit of a number."""
  if number < 0:
    number = -number
  digit = number % 10
  return digit

def main():
  """Generates a random number and finds the last digit."""
  number = random.randint(-10000, 10000)
  last_digit = find_last_digit(number)

  print("Last digit of {} is {} and is ".format(number, last_digit), end="")
  if last_digit > 5:
    print("greater than 5")
  elif last_digit == 0:
    print("0")
  else:
    print("less than 6 but not 0")
