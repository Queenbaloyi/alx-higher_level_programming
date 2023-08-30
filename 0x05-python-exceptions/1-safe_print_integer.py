#!/usr/bin/python3


def safe_print_integer(number):
    """Print an integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(number))
        return (True)
    except (TypeError, ValueError):
        return (False)
