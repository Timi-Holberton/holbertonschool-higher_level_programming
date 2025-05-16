#!/usr/bin/python3
"""

    Additionne deux entiers après validation de leurs types.

"""


def add_integer(a, b=98):
    """
    Additionne deux entiers après validation de leurs types.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
