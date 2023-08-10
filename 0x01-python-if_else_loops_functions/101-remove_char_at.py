#!/usr/bin/python3
# 101-remove_char_at.py

def remove_character(str, n):
    """Removes the character at position n from the string.

    Args:
        str (str): The string to modify.
        n (int): The index of the character to remove.

    Returns:
        str: The string with the character at position n removed.
    """

    if n < 0 or n >= len(str):
        return str
    return str[:n] + str[n + 1:]
