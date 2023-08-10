#!/usr/bin/python3
# 100-print_tebahpla.py

def print_tebahpla():
  """Prints the alphabet in reverse order alternating upper- and lower-case."""
  letters = []
  for c in range(ord('z'), ord('a') - 1, -1):
    if c % 2 == 0:
      letters.append(chr(c))
    else:
      letters.append(chr(c + 32))

  for letter in letters:
    print(letter, end="")

if __name__ == "__main__":
  print_tebahpla()
