#!/usr/bin/python3

def print_arguments():
  """Prints the number of and the list of its arguments."""
  # Get the number of arguments
  num_args = len(argv)

  # If no arguments were passed, print a message and exit
  if num_args == 0:
    print("No arguments were passed.")
    return

  # Print the number of arguments
  print("Number of arguments:", num_args)

  # Print the list of arguments
  print("Arguments:")
  for i in range(1, num_args + 1):
    print(i, ":", argv[i - 1])

if __name__ == "__main__":
  # This line will be executed only if the program is run directly,
  # not if it is imported as a module
  print_arguments()
