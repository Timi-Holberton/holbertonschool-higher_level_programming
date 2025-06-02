#!/usr/bin/python3
"""
Module save_to_json_file
Ce module fournit une fonction pour écrire un objet Python
dans un fichier texte en utilisant sa représentation JSON.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Écrit un objet Python dans un fichier texte au format JSON.

    Paramètres :
        my_obj (any) : Objet Python à sérialiser.
        filename (str) : Nom du fichier où écrire la représentation JSON.

    Retourne :
        None
    """
    with open(filename, "w", encoding="utf-8") as outfile:
        json.dump(my_obj, outfile)
