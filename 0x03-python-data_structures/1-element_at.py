def retrieve_element(my_sequence, index):
    """Retrieve an element from a sequence."""
    if index < 0 or index >= len(my_sequence):
        return None
    return my_sequence[index]
