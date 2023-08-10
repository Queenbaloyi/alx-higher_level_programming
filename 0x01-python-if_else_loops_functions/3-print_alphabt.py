#!/usr/bin/python3
for alphabet_letter in range(97, 123):
    if chr(alphabet_letter) is not 'q' and chr(alphabet_letter) is not 'e':
        print("{}".format(chr(alphabet_letter)), end="")
