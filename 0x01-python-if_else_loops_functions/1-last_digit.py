#!/usr/bin/python3
import random

def last_digit(number):
    if number < 0:
        number = -number
    return number % 10

def main():
    random_number = random.randint(-10000, 10000)
    last_digit = last_digit(random_number)
    print("The last digit of {} is {} and is ".format(random_number, last_digit), end="")
    if last_digit > 5:
        print("greater than 5")
    elif last_digit == 0:
        print("0")
    else:
        print("less than 6 and not 0")

if __name__ == "__main__":
    main()
