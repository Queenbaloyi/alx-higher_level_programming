#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    num = 0

    for i in my_list:
        if i not in uniq_list:
            uniq_list.append(i)

    for i in uniq_list:
        num += i

    return num
