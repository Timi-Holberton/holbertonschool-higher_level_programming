#!/usr/bin/python3
"""
Script principal pour l'ajout d'éléments à une liste JSON stockée
dans un fichier.

Ce script lit les arguments passés en ligne de commande
et les ajoute à une liste persistante contenue dans le fichier 'add_item.json'
Si ce fichier n'existe pas ou est invalide, une nouvelle liste est initialisée
"""
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

args = sys.argv[1:]
file = load_from_json_file("add_item.json")
if file:
    liste = file
else:
    liste = []
liste.extend(args)
save_to_json_file(liste, "add_item.json")
