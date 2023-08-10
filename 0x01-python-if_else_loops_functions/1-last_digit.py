#!/usr/bin/python3
import random

def last_digit(number):
    """Calculates the last digit of a number."""
    return abs(number) % 10

def main():
    number = random.randint(-10000, 10000)
    digit = last_digit(number)
    print("Last digit of {} is {} and is ".format(number, digit), end="")

    if digit > 5:
        print("greater than 5")
    elif digit == 0:
        print("0")
    elif number < 0:
        print("less than 6 and negative")
    else:
        print("less than 6 and not 0")

if __name__ == "__main__":
    main()
