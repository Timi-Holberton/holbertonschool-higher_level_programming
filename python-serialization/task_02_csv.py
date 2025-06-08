#!/usr/bin/python3
"""
Module convertissant un fichier CSV en JSON.

Ce module contient une fonction qui permet de lire un fichier CSV,
de le convertir en liste de dictionnaires, puis de sauvegarder ces
données au format JSON dans un fichier nommé 'data.json'.
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    Convertit un fichier CSV en un fichier JSON.

    Cette fonction lit les données du fichier CSV spécifié par `filename`,
    les convertit en une liste de dictionnaires,
    puis les sérialise au format JSON
    dans un fichier nommé "data.json".

    Args:
        filename (str): Le nom du fichier CSV à lire.

    Returns:
        bool: True si la conversion et l'écriture du fichier JSON réussissent,
              False en cas d'erreur (fichier introuvable,
              erreur de lecture/écriture, etc.).
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lire_fichier = csv.DictReader(file)
            data = list(lire_fichier)

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file)
        return True
    except Exception:
        return False
