#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script principal pour l'ajout d'éléments à une liste JSON stockée
dans un fichier.

Ce script lit les arguments passés en ligne de commande
et les ajoute à une liste persistante contenue dans le fichier 'add_item.json'
Si ce fichier n'existe pas ou est invalide, une nouvelle liste est initialisée
"""

import sys
import os

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
args = sys.argv[1:]

if os.path.exists(filename):
    liste = load_from_json_file(filename)
else:
    liste = []

liste.extend(args)
save_to_json_file(liste, filename)
