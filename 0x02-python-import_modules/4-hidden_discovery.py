#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import my_module

    my_names = dir(my_module)
    for my_name in my_names:
        if my_name[:2] != "__":
            print(my_name)
