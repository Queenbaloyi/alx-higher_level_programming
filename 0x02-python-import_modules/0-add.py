#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum of 1 and 2."""
    add_0 = "/path/to/add_0.py"

    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
