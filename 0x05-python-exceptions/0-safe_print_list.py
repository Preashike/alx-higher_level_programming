#!/usr/bin/python3


def safe_print_list(my_list=[], a=0):
    i = 0
    printed = 0
    for i in range(0, a):
        try:
            print("{}".format(my_list[i]), end="")
            printed += 1
        except:
            continue
    print()
    return printed
