#!/usr/bin/python3
import random
random_number = random.randint(-10000, 10000)
digit = abs(random_number) % 10
if random_number < 0:
    digit = -digit
print("Last digit of {} is {} and is ".format(random_number, digit), end="")
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
