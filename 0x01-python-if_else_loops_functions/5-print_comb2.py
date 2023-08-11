#!/usr/bin/python3
for current_number in range(0, 100):
    if current_number == 99:
        print("{}".format(current_number))
    else:
        print("{:02}".format(current_number), end=", ")
