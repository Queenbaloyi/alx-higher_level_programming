#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    multiples = [False for i in range(len(my_list))]
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples[i] = True

    return multiples
