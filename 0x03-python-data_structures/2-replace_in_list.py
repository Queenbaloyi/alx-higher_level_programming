#!/usr/bin/python3
# 2-replace_in_list.py

def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position."""

    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 2
    element = 10
    print(f"The original list is: {my_list}")
    print(f"The modified list is: {replace_in_list(my_list, idx, element)}")
