#!/usr/bin/python3

def add(x, y):
    """This function adds two numbers."""
    return x + y


if __name__ == "__main__":
    """Print the sum of 1 and 2."""
    from my_add_function import add

    first_number = 1
    second_number = 2
    print("{} + {} = {}".format(first_number, second_number, add(first_number, second_number)))
