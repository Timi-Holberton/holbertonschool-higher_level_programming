#!/usr/bin/env python3
"""
Module principal d'une API Flask avec authentification basique et JWT.

Ce module définit une application Flask qui utilise l'authentification HTTP
Basic pour certaines routes et JSON Web Tokens (JWT) pour la gestion des
sessions et l'autorisation. Les utilisateurs sont stockés en mémoire avec
un rôle associé (p. ex. "user" ou "admin").

Fonctionnalités principales :
- Authentification HTTP Basic sur une route protégée.
- Authentification via JWT sur plusieurs routes.
- Génération de token JWT lors de la connexion + vérification des identifiants
- Gestion des erreurs liées aux tokens JWT
(manquants, invalides, expirés, révoqués, etc.).
- Contrôle d'accès aux routes admin uniquement.

Structures de données :
- `users` : dictionnaire en mémoire des utilisateurs avec leurs mots de passe
 hashés et rôles.

Routes exposées :
- `/basic-protected` : accessible uniquement avec HTTP Basic Auth valide.
- `/login` : POST, obtention d'un token JWT à partir de credentials JSON.
- `/jwt-protected` : accessible uniquement avec un JWT valide.
- `/admin-only` : accessible uniquement aux utilisateurs JWT avec rôle admin.

Utilisation :
Lancer le serveur avec la commande `python3 <nom_du_fichier>.py`.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (JWTManager, create_access_token,
                                jwt_required, get_jwt_identity)

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "extraordinaire"
jwt = JWTManager(app)


users = {
    "user1": {"username": "user1", "password":
              generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password":
               generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verif_password(username, password):
    """
    Vérifie le couple nom d'utilisateur / mot de passe pour HTTP Basic Auth.

    Args:
        username (str): Nom d'utilisateur fourni.
        password (str): Mot de passe fourni.

    Returns:
        str or None: Le nom d'utilisateur s'il est validé, sinon None.
    """
    if username in users:
        mdp_H = users[username]['password']
        if check_password_hash(mdp_H, password):
            return username


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """
    Route protégée accessible uniquement avec HTTP Basic Auth valide.

    Returns:
        Response JSON: Message confirmant l'accès.
    """
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """
    Route de connexion : vérifie les credentials et retourne un token JWT.

    Expects:
        JSON payload avec "username" et "password".

    Returns:
        Response JSON:
            - 200 avec access_token si succès.
            - 401 avec message d'erreur si échec.
    """
    username = request.json.get("username")
    password = request.json.get("password")
    if username in users:
        mdp_H = users[username]['password']
        if check_password_hash(mdp_H, password):
            access_token = create_access_token(
                identity={
                    "username": username,
                    "role": users[username]["role"]
                }
            )
            return jsonify({"access_token": access_token}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """
    Route protégée accessible uniquement avec un JWT valide.

    Returns:
        Response JSON: Message confirmant l'accès.
    """
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """
    Route accessible uniquement aux utilisateurs JWT ayant le rôle "admin".

    Returns:
        Response JSON:
            - 200 avec message de succès si rôle admin.
            - 403 avec message d'erreur sinon.
    """
    jwt_identity = get_jwt_identity()
    if jwt_identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    else:
        return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Gestionnaire d'erreur pour token JWT manquant ou invalide.

    Args:
        err (str): Message d'erreur généré.

    Returns:
        Response JSON: Message d'erreur et code HTTP 401.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Gestionnaire d'erreur pour token JWT invalide.

    Args:
        err (str): Message d'erreur généré.

    Returns:
        Response JSON: Message d'erreur et code HTTP 401.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Gestionnaire d'erreur pour token JWT expiré.

    Args:
        err (str): Message d'erreur généré.

    Returns:
        Response JSON: Message d'erreur et code HTTP 401.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Gestionnaire d'erreur pour token JWT révoqué.

    Args:
        err (str): Message d'erreur généré.

    Returns:
        Response JSON: Message d'erreur et code HTTP 401.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Gestionnaire d'erreur pour token JWT nécessitant un token "fresh".

    Args:
        err (str): Message d'erreur généré.

    Returns:
        Response JSON: Message d'erreur et code HTTP 401.
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
