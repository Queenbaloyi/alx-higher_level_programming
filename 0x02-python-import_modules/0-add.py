#!/usr/bin/python3

def add(a, b):
    """This function adds two numbers."""
    return a + b


if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
