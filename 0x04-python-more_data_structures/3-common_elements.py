#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_elements = []

    for i in set_1:
        if i in set_2:
            common_elements.append(i)

    return common_elements

if __name__ == "__main__":
    set_1 = {1, 2, 3, 4, 5}
    set_2 = {2, 3, 5, 6, 7}
    common_elements = common_elements(set_1, set_2)
    print(common_elements)
