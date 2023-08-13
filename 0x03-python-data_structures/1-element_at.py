def retrieve_element(my_sequence, index):
    """Retrieve an element from a sequence."""
    if index < 0 or index >= len(my_sequence):
        return None
    return my_sequence[index]

if __name__ == "__main__":
    my_sequence = [1, 2, 3, 4, 5]
    index = 3
    print(retrieve_element(my_sequence, index))
