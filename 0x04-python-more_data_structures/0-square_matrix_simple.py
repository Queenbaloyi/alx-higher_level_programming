#!/usr/bin/python3
def square_matrix_simple(matrix):
  """Computes the square value of all integers of a matrix.

  Args:
    matrix: a 2 dimensional array

  Returns:
    a new matrix:
      Same size as matrix
      Each value should be the square of the value of the input
    Initial matrix should not be modified

  You are not allowed to import any module
  You are allowed to use regular loops, map, etc.
  """

  new_matrix = []
  for row in matrix:
    new_row = []
    for item in row:
      new_row.append(item ** 2)
    new_matrix.append(new_row)
  return new_matrix
