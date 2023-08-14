def print_matrix_integer(matrix=[[]]):
def print_matrix_integer(matrix=[[]]):
  """Prints a matrix of integers.

  Args:
    matrix: The matrix to print.

  Returns:
    None.
  """

  if not matrix:
    return

  for row in matrix:
    for col in row:
      print("%d" % col, end=" " if col != row[-1] else "")
    print()


if __name__ == "__main__":
  matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
  ]

  print_matrix_integer(matrix)
  print("--")
  print_matrix_integer()
