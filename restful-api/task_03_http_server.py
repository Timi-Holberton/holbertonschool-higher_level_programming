#!/usr/bin/python3
"""
Serveur HTTP simple utilisant module http.server pour gérer des requêtes GET.

Ce module implémente une API minimale avec trois points d'entrée :
- /data : retourne des données JSON représentant un utilisateur fictif.
- /status : retourne un message texte simple indiquant que serveur fonctionne.
- /info : retourne des informations sur l'API au format JSON.

Exécute un serveur sur le port 8000 en mode bloquant.

Encodage : UTF-8
"""

from http.server import *
import json


class Serveur(BaseHTTPRequestHandler):
    """
    Gestionnaire de requêtes HTTP personnalisées pour un serveur simple.

    Hérite de BaseHTTPRequestHandler et redéfinit la méthode do_GET afin de
    traiter des routes spécifiques (/data, /status, /info) avec des réponses
    en JSON ou en texte brut.
    """

    def do_GET(self):
        """
        Traite les requêtes HTTP GET.

        Routes prises en charge :
        - /data : renvoie un objet JSON avec des informations utilisateur.
        - /status : renvoie un message "OK" en texte brut.
        - /info : renvoie des informations sur l'API en JSON (NB : contient
          un appel redondant).
        - toute autre route : renvoie une erreur 404 avec un message d'erreur.

        La réponse est envoyée avec l'encodage UTF-8.
        """
        if self.path == "/data":
            data_set = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data_set_json = bytes(json.dumps(data_set), "utf-8")
            self.wfile.write(data_set_json)

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            data_info = {"version": "1.0", "description": "A simple API built "
                         "with http.server"}
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            data_info_json = bytes(json.dumps(data_info), "utf-8")
            self.wfile.write(data_info_json)

        elif self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


httpd = HTTPServer(("", 8000), Serveur)
httpd.serve_forever()
