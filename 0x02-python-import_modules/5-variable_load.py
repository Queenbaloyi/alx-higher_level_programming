#!/usr/bin/python3

if __name__ == "__main__":
    """Print the value of variable a from variable_load_5."""
    from variable_load_5 import a

    # Get a reference to the original variable a
    a_global = globals()["a"]

    # Change the value of a_global to 100
    setattr(globals(), "a", 100)

    print(a)
