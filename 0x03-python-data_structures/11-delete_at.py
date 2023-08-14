#!/usr/bin/python3
# 11-delete_at.py

def delete_at(my_list=[], idx=0):
    """Delete an item at a specific position in a list."""
    if idx < 0 or idx >= len(my_list):
        return my_list

    i = 0
    while i < len(my_list):
        if i == idx:
            del my_list[i]
        else:
            my_list[i] = my_list[i + 1]
        i += 1

    return my_list
