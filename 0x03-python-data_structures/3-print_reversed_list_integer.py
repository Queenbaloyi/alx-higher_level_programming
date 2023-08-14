#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list, in reverse order."""

    if not my_list:
        return

    for i in reversed(my_list):
        print(f"{i}")


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(my_list)
