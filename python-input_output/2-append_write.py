#!/usr/bin/python3
"""
Module append_write
Ce module fournit une fonction pour ajouter du texte à la fin
d’un fichier UTF-8, en le créant s’il n’existe pas.
"""


def append_write(filename="", text=""):
    """
    Ajoute une chaîne de caractères à la fin d’un fichier texte en UTF-8.
    Crée le fichier s’il n’existe pas.

    Paramètres :
        filename (str) : Le nom du fichier dans lequel écrire.
        text (str) : Le texte à ajouter à la fin du fichier.

    Retourne :
        int : Le nombre de caractères ajoutés.
    """
    with open(filename, "a+", encoding="utf-8") as file:
        return file.write(text)
