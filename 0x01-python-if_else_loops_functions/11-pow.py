#!/usr/bin/python3
# 11-pow.py

def calculate_power(base, exponent):
    """Calculate the power of a number.

    Args:
        base: The base number.
        exponent: The exponent.

    Returns:
        The power of the base number to the exponent.
    """

    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * calculate_power(base, exponent - 1)


if __name__ == "__main__":
    print(calculate_power(2, 3))
