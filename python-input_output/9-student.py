#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module définissant une classe Student avec une méthode
permettant de sérialiser ses attributs au format JSON-compatible.
"""


class Student:
    """
    Représente un étudiant avec un prénom, un nom et un âge.

    Attributs :
        first_name (str): Prénom de l'étudiant.
        last_name (str): Nom de l'étudiant.
        age (int): Âge de l'étudiant.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialiser une nouvelle instance de Student.

        Args:
            first_name (str): Le prénom de l'étudiant.
            last_name (str): Le nom de l'étudiant.
            age (int): L'âge de l'étudiant.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retourner un dictionnaire représentant l'instance.

        Cette méthode permet d'obtenir une structure de données
        JSON-compatible à partir de l'objet Student.

        Returns:
            dict: Dictionnaire contenant les attributs de l'étudiant.
        """
        return self.__dict__
