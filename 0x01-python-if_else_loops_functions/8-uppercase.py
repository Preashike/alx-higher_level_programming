#!/usr/bin/python3


def uppercase(str):
    new_str = ''
    for a in str:
        if ord(a) >= 97 and ord(a) <= 122:
            new_str += chr(ord(a) - 32)
        else:
            new_str += a
    print('{}'.format(new_str))
