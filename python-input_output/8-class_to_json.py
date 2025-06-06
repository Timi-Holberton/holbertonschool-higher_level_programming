#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module fournissant une fonction utilitaire pour convertir une instance
d'une classe en dictionnaire sérialisable au format JSON.
"""

def class_to_json(obj):
    """
    Convertir une instance en dictionnaire JSON-compatible.

    Cette fonction retourne un dictionnaire contenant tous les attributs
    d'instance d'un objet, généralement stockés dans son attribut __dict__.
    Elle est utile pour la sérialisation des objets personnalisés
    en JSON, notamment avec le module json.

    Args:
        obj (object): L'objet dont on souhaite extraire les attributs.

    Returns:
        dict: Un dictionnaire contenant les paires attribut/valeur
              de l'objet, prêtes à être sérialisées en JSON.
    """
    return obj.__dict__
