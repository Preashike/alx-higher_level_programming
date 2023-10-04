#!/usr/bin/python3


def print_low_alpha_ex():
    for a in range(97, 123):
        if a != 101 and a != 113:
            print('{}'.format(chr(a)), end='')
