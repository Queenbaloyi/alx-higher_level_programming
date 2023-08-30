#!/usr/bin/python3

import sys

def print_safe_integer_with_error(number):
    """Prints an integer with "{:d}".format().

    If a ValueError message is caught, a corresponding
    message is printed to standard error.

    Args:
        number (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(number))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)


if __name__ == "__main__":
    print(print_safe_integer_with_error(10))
    print(print_safe_integer_with_error("10"))
