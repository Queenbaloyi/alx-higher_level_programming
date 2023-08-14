#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""

    # Check if the input is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Print the matrix
    for row in matrix:
        for col in row:
            print(f"{col:d}", end="")
        print()
