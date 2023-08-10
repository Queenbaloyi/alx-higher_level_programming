#!/usr/bin/python3
# 102-magic_calculation.py

def magic_calculation(first_number, second_number, third_number):
    """Calculates a magic number based on the given three numbers."""
    if first_number < second_number:
        return third_number
    elif third_number > second_number:
        return first_number + second_number
    else:
        return first_number * second_number - third_number

