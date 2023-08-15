#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
    from calculator_1 import Addition, Subtraction, Multiplication, Division


a = 10
b = 5

print("Addition: {} + {} = {}".format(a, b, calculator_1.add(a, b)))
print("Subtraction: {} - {} = {}".format(a, b, calculator_1.subtract(a, b)))
print("Multiplication: {} * {} = {}".format(a, b, calculator_1.multiply(a, b)))
print("Division: {} / {} = {}".format(a, b, calculator_1.divide(a, b)))
