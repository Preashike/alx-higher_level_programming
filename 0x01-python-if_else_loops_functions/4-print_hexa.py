#!/usr/bin/python3


def get_hexa(number):
    hexstr = '0123456789abcdef'
    tens = number // 16
    ones = number % 16
    if tens > 0:
        return hexstr[tens] + hexstr[ones]
