#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints the specified number of elements from a list.

    Args:
         my_custom_list (list): The list to print elements from.
        number_of_elements (int): The number of elements of my_custom_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
