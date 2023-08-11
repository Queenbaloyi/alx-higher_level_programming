#!/usr/bin/python3
for lowercase_letter in range(97, 123):
    if chr(lowercase_letter) is not 'q' and chr(lowercase_letter) is not 'e':
        print("{}".format(chr(lowercase_letter)), end="")
