def print_reversed_list_integer(my_list=list()):
    """Print all integers of a list in reverse order."""

    # Check if the input is a list
    if not isinstance(my_list, list):
        raise TypeError("my_list must be a list")

    # Reverse the list
    my_list.reverse()

    # Print the elements of the list in reverse order
    for i in my_list:
        print(i)
