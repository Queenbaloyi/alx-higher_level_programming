#!/usr/bin/python3
def new_in_list(my_list, idx, element):
  """Replaces an element in a list at a specific position without modifying the original list.

  Args:
    my_list: The list to modify.
    idx: The index of the element to replace.
    element: The new element to insert.

  Returns:
    The modified list. If idx is negative or out of range, the original list is returned.
  """

  if idx < 0:
    return my_list

  length = len(my_list)
  if idx >= length:
    return my_list

  new_list = my_list[:]
  new_list[idx] = element
  return new_list
