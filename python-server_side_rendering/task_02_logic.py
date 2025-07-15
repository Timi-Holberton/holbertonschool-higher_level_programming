#!/usr/bin/python3
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        # Tente d'ouvrir le fichier JSON contenant la liste d'objets
        with open('items.json', 'r') as file:
            # Charge le contenu JSON dans une variable Python (un dictionnaire)
            data = json.load(file)
            # Récupère la liste associée à la clé "items"
            # Si la clé "items" n'existe pas, retourne une liste vide par défaut
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        # Si le fichier est introuvable ou contient une erreur de format JSON,
        # on utilise une liste vide pour éviter que l'application plante
        items_list = []

    # Rend le template 'items.html' et transmet la liste des objets au template
    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
