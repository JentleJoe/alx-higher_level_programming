#!/usr/bin/python3
start = 0
end = 0
while (start <= 9):
    if (start == 9 and end == 9):   # prints last number with newline
        print("{}{}".format(start, end))
        break

    print("{}{}, ".format(start, end), end="")
    if (start < 9 and end == 9):  # increments start when end = 9
        start = start + 1
        end = 0
    else:
        end = end + 1
