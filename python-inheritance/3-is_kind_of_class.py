#!/usr/bin/python3
"""
Module qui définit la fonction is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """
    Vérifie si un objet est une instance d'une classe donnée
    ou d'une classe qui en hérite.

    Args:
        obj: L'objet à tester.
        a_class: La classe à comparer.

    Returns:
        True si obj est instance de a_class ou d'une sous-classe de a_class,
        False sinon.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
