#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 10-student
Définit une classe Student capable de renvoyer une représentation JSON
filtrée ou complète de ses attributs d'instance.
"""


class Student:
    """
    Représente un étudiant avec prénom, nom et âge.
    Fournit une méthode pour sérialiser les attributs en dictionnaire.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialiser un nouvel étudiant.

        Args:
            first_name (str): Prénom de l'étudiant.
            last_name (str): Nom de famille de l'étudiant.
            age (int): Âge de l'étudiant.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Renvoyer un dictionnaire représentant les attributs de l'instance.

        Si `attrs` est une liste de noms d'attributs (chaînes de caractères),
        seuls les attributs correspondants sont inclus s'ils existent.

        Sinon, tous les attributs sont renvoyés.

        Args:
            attrs (list, optional): Liste de chaînes correspondant aux noms
                                    d'attributs à inclure.

        Returns:
            dict: Dictionnaire des attributs filtrés ou complets.
        """
        if isinstance(attrs, list):
            dico = {}
            for key in attrs:
                if hasattr(self, key):
                    dico[key] = getattr(self, key)
            return dico
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Remplacer les attributs de l’instance à partir d’un dictionnaire.

        Args:
            json (dict): Dictionnaire contenant les nouvelles valeurs
                        pour les attributs existants.
        """
        for key in json:
            if hasattr(self, key):
                setattr(self, key, json[key])

# Vérifie si attrs est exactement une liste
# Initialise un dictionnaire vide pour stocker les attributs filtrés
# Parcourt chaque élément de la liste attrs
# Vérifie que l'objet a un attribut nommé key
# Récupère la valeur de cet attribut et l'ajoute au dictionnaire
# Retourne le dictionnaire filtré contenant uniquement les attributs demandés
# Retourne un dictionnaire complet des attributs de l'objet
