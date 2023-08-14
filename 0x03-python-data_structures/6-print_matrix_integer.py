#!/usr/bin/python3
def print_matrix_integer(my_matrix=[[]]):
    for row in my_matrix:
        for col in row:
            print("{:d}".format(col), end=" " if col != row[-1] else "")
        print()
