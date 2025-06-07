#!/usr/bin/python3
"""
Module permettant la sérialisation et la désérialisation d'un objet personnalisé en utilisant pickle.

Ce module définit la classe CustomObject, qui contient des méthodes pour afficher les attributs
de l'objet, le sérialiser dans un fichier binaire, et le désérialiser depuis un fichier.
"""

import pickle
import os


class CustomObject:
    """
    Objet personnalisé représentant une personne avec un nom,
    un âge et un statut étudiant.

    Attributs :
        name (str) : Nom de la personne.
        age (int) : Âge de la personne.
        is_student (bool) : Indique si la personne est étudiante.
    """

    def __init__(self, name, age, is_student):
        """
        Initialiser un objet CustomObject.

        Paramètres :
            name (str) : Le nom de la personne.
            age (int) : L'âge de la personne.
            is_student (bool) : True si la personne est étudiante, False sinon
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Afficher les attributs de l'objet de manière lisible.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Sérialiser l'objet et l'enregistrer dans un fichier binaire.

        Paramètre :
            filename (str) : Chemin du fichier où enregistrer l'objet.

        Retourne :
            None si une erreur survient.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Désérialiser un objet CustomObject depuis un fichier binaire.

        Paramètre :
            filename (str) : Chemin du fichier contenant l'objet sérialisé.

        Retourne :
            CustomObject : L'objet désérialisé.
            None : Si une erreur survient pendant la désérialisation.
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
