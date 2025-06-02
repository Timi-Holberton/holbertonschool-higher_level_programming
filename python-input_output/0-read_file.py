#!/usr/bin/python3
"""
    Lit et affiche le contenu d’un fichier texte encodé en UTF-8.
"""


def read_file(filename=""):
    """
    Lit et affiche le contenu d’un fichier texte encodé en UTF-8.

    Paramètre :
        filename (str) : Le chemin du fichier à lire.

    Lève une exception si le fichier n'existe pas ou n'est pas lisible.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
