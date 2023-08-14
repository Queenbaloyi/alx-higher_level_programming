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
      print(f"{col:d}", end=" " if col != row[-1] else "")
    print()
