#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        numerator = 0
        denomenator = 0
        for tup in my_list:
            numerator += (tup[0] * tup[1])
            denomenator += (tup[1])
        return (numerator/denomenator)
    return 0
