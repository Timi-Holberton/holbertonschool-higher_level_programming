#!/usr/bin/python3
"""
Script qui affiche tous les objets State triés par id dans la base MySQL.
"""

import sys
# Importe la classe Base (classe de base ORM) et la classe State
# (modèle de la table states) depuis le fichier model_state.py
from model_state import Base, State
# Importe create_engine, la fonction qui crée un moteur de connexion
# permettant de gérer la communication avec la base de données
from sqlalchemy import create_engine
# Importe la fonction sessionmaker qui permet de créer des objets session
# pour interagir avec la base de données via SQLAlchemy ORM
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Récupération des paramètres de connexion depuis la ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Construction de l'URL de connexion à la base MySQL avec SQLAlchemy
    connection_url = (
        f"mysql+mysqldb://{username}:{password}@localhost/"
        f"{database}"
    )
    # engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
    # (sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Création de l'engine SQLAlchemy pour gérer la connexion à la base
    engine = create_engine(connection_url, pool_pre_ping=True)

    # Création des tables dans la base (si elles n'existent pas encore)
    Base.metadata.create_all(engine)

    # Création d'une session pour interagir avec la base
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête pour récupérer tous les objets State triés par id (ordre croissant)
    states = session.query(State).order_by(State.id).all()

    # Affichage des résultats au format "id: name"
    for state in states:
        print(f"{state.id}: {state.name}")

    # Fermeture de la session pour libérer les ressources
    session.close()
