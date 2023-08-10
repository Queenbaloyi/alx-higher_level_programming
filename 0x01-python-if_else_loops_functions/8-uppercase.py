#!/usr/bin/python3
# 8-uppercase.py


def uppercase(str):
    """Print a string in uppercase."""
    for c in str:
        if c.islower():
            c = c.upper()
        print(c, end="")
    print("")


if __name__ == "__main__":
    str = input("Enter a string: ")
    uppercase(str)
