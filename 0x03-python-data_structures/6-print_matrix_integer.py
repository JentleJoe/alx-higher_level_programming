#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1:
        print()
    for lists in matrix:
        for num in lists:
            if num == lists[-1]:
                print("{}".format(num))
            else:
                print("{} ".format(num), end='')
