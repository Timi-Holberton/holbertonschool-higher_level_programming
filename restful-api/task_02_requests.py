#!/usr/bin/python3
"""
Script pour interagir avec l'API JSONPlaceholder.

Ce script contient deux fonctions :
- fetch_and_print_posts() : récupère et affiche les titres des posts.
- fetch_and_save_posts() : récupère les posts et les enregistre
dans un fichier CSV.

Utilise la bibliothèque `requests` pour envoyer des requêtes HTTP
et le module `csv` pour générer un fichier CSV.

Encodage : UTF-8
"""
import requests  # Importe la bibliothèque pour faire des requêtes HTTP
import csv       # Importe le module pour écrire dans un fichier CSV


def fetch_and_print_posts():
    """
    Envoyer une requête GET à l'API JSONPlaceholder
    et afficher les titres des posts.

    Cette fonction récupère une liste de posts au format JSON depuis l'API,
    puis affiche le champ 'title' de chaque post dans la console.
    Elle affiche également le code de statut HTTP de la réponse.
    """
    # Envoie une requête GET à l'API pour récupérer les posts
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    # Affiche le code de statut HTTP de la réponse
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()   # Convertit la réponse JSON en liste de dict
        for item in data:  # Parcourt chaque post et affiche son titre
            print(item["title"])  # Affiche le champ 'title' de chaque post


def fetch_and_save_posts():
    """
    Récupérer les posts depuis l'API JSONPlaceholder
    et les enregistrer dans un fichier CSV.

    Cette fonction envoie une requête GET,
    transforme les données JSON en une liste
    de dictionnaires, puis enregistre les champs
    'id', 'title' et 'body' de chaque post dans un fichier CSV
    nommé 'posts.csv'.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        data = response.json()
        with open("posts.csv", "w", newline='') as csvfile:
            fieldnames = ["id", "title", "body"]  # Colonnes du fichier CSV
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()  # Écrit l'en-tête du fichier CSV
            for post in data:  # Parcourt les données récupérées
                row = {"id": post["id"], "title": post["title"],
                       "body": post["body"]}  # Crée un dico pour chaque ligne
                writer.writerow(row)  # Écrit une ligne à la fois
