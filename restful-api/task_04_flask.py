"""
Flask API minimaliste pour la gestion d'utilisateurs en mémoire.

Ce module expose plusieurs endpoints :
- /                  : Affiche un message de bienvenue.
- /data              : Retourne la liste des noms d'utilisateurs.
- /status            : Vérifie que l'API est active.
- /add_user (POST)   : Ajoute un utilisateur à partir de données JSON.
- /users/<username>  : Retourne les détails d'un utilisateur spécifique.

Données stockées en mémoire dans un dictionnaire global `users`.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """
    Flask API minimaliste pour la gestion d'utilisateurs en mémoire.

    Ce module expose plusieurs endpoints :
    - /                  : Affiche un message de bienvenue.
    - /data              : Retourne la liste des noms d'utilisateurs.
    - /status            : Vérifie que l'API est active.
    - /add_user (POST)   : Ajoute un utilisateur à partir de données JSON.
    - /users/<username>  : Retourne les détails d'un utilisateur spécifique.

    Données stockées en mémoire dans un dictionnaire global `users`.
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def get_user():
    """
    Route qui retourne la liste des noms d'utilisateurs enregistrés.

    Returns:
        Response: Liste JSON des usernames.
    """
    liste_user = list(users.keys())
    return jsonify(liste_user)


@app.route('/status')
def get_statut():
    """
    Route de vérification de l'état de l'API.

    Returns:
        str: "OK" si le serveur est actif.
    """
    return "OK"


@app.route('/add_user', methods=["POST"])
def post_add_user():
    """
    Route POST pour ajouter un nouvel utilisateur.

    Le JSON envoyé doit contenir au minimum une clé "username".

    Returns:
        Response: Confirmation avec les données utilisateur ajoutées (201),
                  ou message d'erreur si "username" est manquant (400).
    """
    user_data = request.get_json()
    if "username" not in user_data:
        return jsonify({"error": "Username is required"}), 400
    username = user_data["username"]
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


@app.route('/users/<username>')
def get_user_details(username):
    """
    Route dynamique pour obtenir les détails d'un utilisateur.

    Args:
        username (str): Nom d'utilisateur à rechercher.

    Returns:
        Response: Données JSON de l'utilisateur s'il existe (200),
                  ou message d'erreur (404).
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run()
