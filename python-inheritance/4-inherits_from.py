#!/usr/bin/python3
"""
Module qui fournit une fonction pour vérifier si un objet hérite d'une
classe donnée.
"""


def inherits_from(obj, a_class):
    """
    Vérifie si un objet hérite (directement ou indirectement) d'une classe
    donnée, sans être une instance directe de cette classe.

    Args:
        obj: L'objet à tester.
        a_class: La classe à comparer.

    Returns:
        True si l'objet est une instance d'une sous-classe de a_class,
        False si l'objet est une instance directe de a_class ou sans lien.
    """
    # Si la classe exacte de l'objet est a_class = ce n'est pas un héritage
    if a_class == type(obj):
        return False
    # Si la classe de l'objet = une sous-classe de a_class, c’est un héritage
    elif issubclass(type(obj), a_class):
        return True
    # Sinon, ce n’est pas un héritage
    else:
        return False
