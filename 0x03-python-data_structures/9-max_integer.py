#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_ = my_list[0]
    for num in my_list:
        if max_ <= num:
            max_ = num
    return (max_)
