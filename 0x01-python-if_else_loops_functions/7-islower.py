#!/usr/bin/python3
# 7-islower.py


def islower(lowercase_letter):
    """Check for lowercase characters."""
    if ord(lowercase_letter) >= 97 and ord(lowercase_letter) <= 122:
        return True
    else:
        return False
