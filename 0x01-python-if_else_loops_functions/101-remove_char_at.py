#!/usr/bin/python3
# 101-remove_char_at.py


def remove_character_at(str, position):
    """Create a copy of the string without the character at position n."""
    if position < 0:
        return (str)
    return (str[:position] + str[position+1:])
