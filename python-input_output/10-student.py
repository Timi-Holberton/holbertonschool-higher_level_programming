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
        # Vérifie si attrs est exactement une liste
        if isinstance(attrs, list):
            dico = {}  # Initialise un dictionnaire vide
            for key in attrs:  # Parcourt chaque élément de la liste attrs
                # Vérifie que l'objet a un attribut nommé key
                if hasattr(self, key):
                    # Récupère la valeur de cet attribut et l'ajoute au dico
                    dico[key] = getattr(self, key)
                    # Retourne le dico filtré contenant uniquement
                    # les attributs demandés
                else:
                    return dico
            # Retourne un dictionnaire complet des attributs de l'objet
            return self.__dict__
