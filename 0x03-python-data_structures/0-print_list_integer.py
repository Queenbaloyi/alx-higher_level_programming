#!/usr/bin/python3

def print_list_integer(list_of_integers=[]):
    """Print all integers of a list."""
    for i in range(len(list_of_integers)):
        print("{:d}".format(list_of_integers[i]))
