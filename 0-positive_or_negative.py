#!/usr/bin/python3
import random

def is_positive(random_number):
    if random_number > 0:
        return True
    elif random_number == 0:
        return False
    else:
        return False

def main():
    random_number = random.randint(-10, 10)
    print(is_positive(random_number))

if __name__ == "__main__":
    main()
