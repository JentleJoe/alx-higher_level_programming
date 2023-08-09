#!/usr/bin/python3
start = 0
end = 0
for start in range(0, 9):
    for end in range(1, 10):
        if (start == 8 and end == 9):   # prints last number with newline
            print("{}{}".format(start, end))
            break
        if (start < end):
            print("{}{}, ".format(start, end), end='')
        elif (start == end):
            continue
