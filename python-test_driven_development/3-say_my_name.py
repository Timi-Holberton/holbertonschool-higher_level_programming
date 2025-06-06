#!/usr/bin/python3
"""

    Affiche "My name is <prénom> <nom>".

"""


def say_my_name(first_name, last_name=""):
    """
        Affiche "My name is <prénom> <nom>".
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
