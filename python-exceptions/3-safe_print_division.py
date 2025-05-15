#!/usr/bin/python3

def safe_print_division(a, b):

    resultat = None

    try:
        resultat = a / b

    except ZeroDivisionError:
        return None

    finally:
        (print("Inside result: {}".format(resultat)))

    return resultat
