#!/usr/bin/python3
# 12-fizzbuzz.py

def fizzbuzz():
    """Print the numbers from 1 to 100 separated by a space.

    For multiples of three, print Fizz instead of the number.
    For multiples of five, print Buzz instead of the number.
    For multiples of three and five, print FizzBuzz instead of the number.
    """
    numbers = list(range(1, 101))
    fizzbuzz_numbers = [
        "FizzBuzz" if number % 3 == 0 and number % 5 == 0 else "Fizz" if number % 3 == 0 else "Buzz" if number % 5 == 0 else number
        for number in numbers
    ]
    print(" ".join(fizzbuzz_numbers))
