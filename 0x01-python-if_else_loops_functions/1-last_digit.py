 #!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
print("Last digit of {} is {} and is ".format(number, digit), end="")
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
     if digit > 5:
        print("greater than 5")
    elif digit == 0:
        print("0")
    elif number < 0:
        print("less than 6 and negative")
    else:
        print("less than 6 and not 0")
