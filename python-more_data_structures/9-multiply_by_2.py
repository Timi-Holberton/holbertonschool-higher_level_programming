#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dico = {cle: valeur * 2 for cle, valeur in a_dictionary.items()}
    return new_dico
