#!/usr/bin/python3
"""
    Vérifie si un objet est exactement une instance d'une classe donnée
    (et non d'une classe dérivée).
"""


def is_same_class(obj, a_class):
    """
    Vérifie si un objet est exactement une instance d'une classe donnée
    (et non d'une classe dérivée).

    Args:
        obj: L'objet à vérifier.
        a_class: La classe à comparer avec le type de l'objet.

    Returns:
        True si l'objet est exactement une instance de la classe donnée,
        sinon False.
    """
    if a_class == type(obj):
        return True
    else:
        return False
