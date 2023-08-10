#!/usr/bin/python3
# 9-print_last_digit.py


def print_last_digit(user_number):
    """Print the last digit of a number and return it."""
    print(abs(user_number) % 10, end="")
    return (abs(user_number) % 10)
