#!/usr/bin/python3
"""

This is a module that containts a clas that avoids
dynmaically created attributes

"""


class LockedClass:
    """LockedClass prevents dynamic creation of attributes other than
    `first_name`
    """
    __slots__ = ['first_name']


if __name__ == '__main__':
    lc = LockedClass()
    lc.first_name = "John"
    try:
        lc.last_name = "Snow"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
