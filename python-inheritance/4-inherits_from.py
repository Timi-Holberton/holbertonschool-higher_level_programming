#!/usr/bin/python3
"""
Module qui fournit une fonction pour vérifier si un objet hérite d'une
classe donnée.
"""


def inherits_from(obj, a_class):
    """
    Vérifie si un objet hérite (directement ou indirectement) d'une classe
    donnée.

    Args:
        obj: L'objet à tester.
        a_class: La classe à comparer.

    Returns:
        True si l'objet est une instance d'une classe fille de a_class,
        False si l'objet est une instance directe de a_class ou sans lien
    """
    # issubclass pour tester si la classe de l'objet hérite de a_class
    # type(obj) donne la classe exacte de l'objet
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
