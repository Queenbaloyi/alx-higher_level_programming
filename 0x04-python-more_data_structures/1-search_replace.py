#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list
if __name__ == "__main__":
    my_list = ["apple", "banana", "cherry"]
    search = "apple"
    replace = "orange"
    new_list = search_replace(my_list, search, replace)
    print(new_list)
