#!/usr/bin/python3
"""
Module write_file
Ce module contient une fonction pour écrire du texte dans un fichier en UTF-8.
"""

def write_file(filename="", text=""):
    """
    Écrit une chaîne de caractères dans un fichier texte encodé en UTF-8.
    Crée le fichier s’il n’existe pas ou écrase son contenu s’il existe déjà.

    Paramètres :
        filename (str) : Le nom du fichier à écrire.
        text (str) : Le texte à écrire dans le fichier.

    Retourne :
        int : Le nombre de caractères écrits.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
