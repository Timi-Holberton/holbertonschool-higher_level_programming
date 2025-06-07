#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module de sérialisation JSON.

Ce module fournit deux fonctions :
- `serialize_and_save_to_file` : pour sérialiser un dictionnaire Python
et l'enregistrer dans un fichier JSON.
- `load_and_deserialize` : pour charger un dictionnaire depuis un fichier JSON

Utilisation typique :
    data = {'nom': 'Alice', 'âge': 30}
    serialize_and_save_to_file(data, 'data.json')
    loaded_data = load_and_deserialize('data.json')
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialiser un dictionnaire Python et l'enregistrer dans un fichier JSON.

    Args:
        data (dict): Les données à sérialiser.
        filename (str): Le nom du fichier de sortie (écrasé s’il existe).

    Returns:
        None
    """
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Charger un dictionnaire à partir d’un fichier JSON.

    Args:
        filename (str): Le nom du fichier JSON à lire.

    Returns:
        dict: Les données désérialisées sous forme de dictionnaire Python.
    """
    with open(filename, "r") as file:
        return json.load(file)
