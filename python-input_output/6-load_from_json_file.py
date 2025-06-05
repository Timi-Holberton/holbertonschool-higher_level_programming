#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module de chargement d'objet Python depuis un fichier JSON.

Ce module contient une fonction permettant de lire un fichier au format JSON
et de convertir son contenu en objet Python standard (liste, dictionnaire...)
"""

import json

def load_from_json_file(filename):
    """
    Charger un objet Python depuis un fichier JSON.

    Ouvre le fichier spécifié, lit son contenu JSON et le convertit
    en un objet Python à l'aide du module `json`.

    Args:
        filename (str): Le chemin vers le fichier JSON à lire.

    Returns:
        Any: L'objet Python désérialisé depuis le fichier JSON.

    Raises:
        FileNotFoundError: Si le fichier spécifié n'existe pas.
        json.JSONDecodeError: Si contenu du fichier n'est pas un JSON valide.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
