#!/usr/bin/python3
# 102-magic_calculation.py


def magic_calculation(first_number, second_number, third_number):
    """Match bytecode provided by Holberton School."""
    if first_number < second_number:
        return (third_number)
    if third_number > second_number:
        return (first_number + second_number)
    return (first_number*second_number - third_number)
