#!/usr/bin/python3
# 100-print_tebahpla.py

""""Print the alphabet in reverse order alternating upper- and lower-case."""
current_letter = 0
for letter in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(letter - current_letter)), end="")
    current_letter = 32 if current_letter == 0 else 0
