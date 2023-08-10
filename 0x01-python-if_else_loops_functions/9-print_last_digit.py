#!/usr/bin/python3
# 9-print_last_digit.py

def print_last_digit(number):
    """Print the last digit of a number and return it."""
    last_digit = abs(number) % 10
    return last_digit

def main():
    number = 12345
    print_last_digit(number)

if __name__ == "__main__":
    main()
