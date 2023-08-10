#!/usr/bin/python3
# 4-print_hexa.py

"""Print numbers 0 to 98 in decimal and hexadecimal."""

def print_hexa(number):


    print("{} = {}".format(number, hex(number)))

for number in range(0, 99):


    print_hexa(number)
