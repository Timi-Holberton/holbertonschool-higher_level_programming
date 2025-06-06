#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script principal pour l'ajout d'éléments à une liste JSON stockée
dans un fichier.

Ce script lit les arguments passés en ligne de commande
et les ajoute à une liste persistante contenue dans le fichier 'add_item.json'
Si ce fichier n'existe pas ou est invalide, une nouvelle liste est initialisée

Modules externes requis :
    - 5-save_to_json_file.py : pour la sérialisation de la liste
    au format JSON.
    - 6-load_from_json_file.py : pour la désérialisation de la liste
    depuis le fichier.

Usage :
    ./7-add_item.py élément1 élément2 ...

Exemple :
    $ ./7-add_item.py "apple" "banana"
    → ajoute "apple" et "banana" à la liste sauvegardée dans add_item.json
"""

import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

args = sys.argv
try:
    file = load_from_json_file("add_item.json")
    if file:  # si file contient quelque chose
        liste = file  # on assigne liste à file
    else:  # si file est None ou vide ou autre
        liste = []  # on créer une nouvelle liste vide et on l'assigne à liste
except Exception("erreur"):
    liste = []
liste.extend(args[1:])
save_to_json_file(liste, "add_item.json")
