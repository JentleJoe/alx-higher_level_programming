#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    results = []
    for i in range(list_length):
        try:
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            div = num1/num2
        except ZeroDivisionError:
            print("division by 0")
            div = 0
            continue
        except IndexError:
            print("out of range")
            div = 0
            continue
        except TypeError:
            print("wrong type")
            div = 0
            continue
        finally:
            results.append(div)
            continue

    return results
