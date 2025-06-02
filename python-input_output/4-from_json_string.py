#!/usr/bin/python3
"""
Module from_json_string
Ce module fournit une fonction pour convertir une chaîne JSON en objet Python.
"""

import json


def from_json_string(my_str):
    """
    Convertit une chaîne JSON en un objet Python.

    Paramètre :
        my_str (str) : Chaîne JSON à désérialiser.

    Retourne :
        any : Objet Python représenté par la chaîne JSON
        (par exemple : dict, list).
    """
    return json.loads(my_str)
