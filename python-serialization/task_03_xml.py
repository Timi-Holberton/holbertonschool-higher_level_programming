#!/usr/bin/python3
"""
Module de sérialisation et désérialisation XML.

Ce module fournit deux fonctions principales pour convertir
des dictionnaires Python
en fichiers XML et inversement, en utilisant le module
standard `xml.etree.ElementTree`.

Fonctions :
- serialize_to_xml(dictionary, filename) : sérialise un dictionnaire en XML
et l'écrit dans un fichier.
- deserialize_from_xml(filename) : lit un fichier XML et retourne
un dictionnaire correspondant.

Exemple d’utilisation :
    sample_dict = {'name': 'John', 'age': '28', 'city': 'New York'}
    serialize_to_xml(sample_dict, 'data.xml')
    data = deserialize_from_xml('data.xml')
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Sérialise un dictionnaire Python en XML et sauvegarde dans un fichier.

    Args:
        dictionary (dict): Le dictionnaire à sérialiser.
        filename (str): Le chemin du fichier où écrire le contenu XML.

    Description:
        Cette fonction crée un document XML avec une racine <data>,
        puis ajoute chaque paire clé/valeur du dictionnaire comme
        élément enfant.
        Le document XML est ensuite écrit dans le fichier spécifié.
    """
    elem = ET.Element("data")  # Création de la racine <data>
    for key, val in dictionary.items():  # Parcours des paires clé/valeur
        child = ET.Element(key)  # Création d'un élément avec le nom de la clé
        child.text = str(val)  # Affectation de la valeur convertie en chaîne
        elem.append(child)  # Ajout de l'élément enfant à la racine
    tree = ET.ElementTree(elem)  # Création de l'arbre XML
    tree.write(filename)  # Écriture de l'arbre dans le fichier


def deserialize_from_xml(filename):
    """
    Désérialise un fichier XML en un dictionnaire Python.

    Args:
        filename (str): Le chemin du fichier XML à lire.

    Returns:
        dict: Le dictionnaire reconstruit à partir du fichier XML,
              avec les noms des balises comme clés et leurs textes
              comme valeurs.

    Description:
        Cette fonction lit un fichier XML attendu avec une racine <data>
        et des éléments enfants, puis crée un dictionnaire où chaque clé
        est le nom d’une balise enfant et la valeur associée est son
        contenu textuel.
    """
    dico = {}  # Initialisation du dictionnaire vide
    tree = ET.parse(filename)  # Parsing du fichier XML
    root = tree.getroot()  # Récupération de la racine <data>
    for child in root:  # Parcours des éléments enfants
        dico[child.tag] = child.text  # Ajout de la clé/valeur au dictionnaire
    return dico  # Retour du dictionnaire final
