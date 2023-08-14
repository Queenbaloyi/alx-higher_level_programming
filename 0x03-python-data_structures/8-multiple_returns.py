#!/usr/bin/python3
# 8-multiple_returns.py
def multiple_returns(sentence):
    """Returns the length of a string and its first character."""

    if sentence == "":
        return (0, None)

    length = len(sentence)
    first_character = sentence[0] if sentence else None

    return length, first_character
