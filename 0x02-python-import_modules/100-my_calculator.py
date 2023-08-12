#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div 
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    my_first_number = int(sys.argv[1])
    my_second_number = int(sys.argv[3])
    print("{} {} {} = {}".format(my_first_number, sys.argv[2], my_second_number, ops[sys.argv[2]](my_first_number, my_second_number)))
