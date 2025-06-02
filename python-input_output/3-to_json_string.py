#!/usr/bin/python3
"""
Module to_json_string
Ce module fournit une fonction pour convertir un objet Python en chaîne JSON.
"""

import json


def to_json_string(my_obj):
    """
    Convertit un objet Python en une chaîne JSON.

    Paramètre :
        my_obj (any) : Objet Python à sérialiser
        (par exemple : dict, list, str, int).

    Retourne :
        str : Chaîne JSON représentant l’objet, encodée en UTF-8.
    """
    return json.dumps(my_obj)
