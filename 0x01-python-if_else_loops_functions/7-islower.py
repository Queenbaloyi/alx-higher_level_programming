#!/usr/bin/python3
# 7-islower.py

def islower(c):
    """Check for lowercase characters."""
    lowercase_alphabet = {
        chr(i): True for i in range(97, 123)
    }
    return c in lowercase_alphabet
