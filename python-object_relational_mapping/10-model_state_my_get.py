#!/usr/bin/python3
"""
Script qui affiche l'id de l'objet State dont le nom correspond
exactement au nom passé en argument dans la base MySQL.

Le script prend en arguments la connexion MySQL (username, password, database)
et le nom de l'état à rechercher, puis affiche l'id correspondant.
Si aucun état ne correspond au nom recherché, affiche "Not found".
"""

import sys
# Importe la classe Base (classe de base ORM) et la classe State
# (modèle représentant la table states) depuis le fichier model_state.py
from model_state import Base, State
# Importe create_engine, qui permet de créer un moteur de connexion
# à la base de données
from sqlalchemy import create_engine
# Importe sessionmaker pour créer une session SQLAlchemy,
# outil d'interaction avec la base via ORM
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Récupération des paramètres MySQL et du nom de l'état
    # depuis la ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Construction de l'URL de connexion à la base MySQL
    connection_url = (
        f"mysql+mysqldb://{username}:{password}@localhost/"
        f"{database}"
    )

    # Création de l'engine SQLAlchemy pour gérer la connexion à la base
    engine = create_engine(connection_url, pool_pre_ping=True)

    # Création des tables dans la base si elles n'existent pas déjà
    Base.metadata.create_all(engine)

    # Création d'une session pour effectuer les opérations ORM
    Session = sessionmaker(bind=engine)
    session = Session()

    # Recherche sécurisée du premier enregistrement State avec un nom exact
    enregistrement_etat = session.query(State).filter(
        State.name == state_name).first()

    # Affiche l'id si trouvé, sinon affiche "Not found"
    if enregistrement_etat is None:
        print("Not found")
    else:
        print(enregistrement_etat.id)

    # Fermeture de la session pour libérer les ressources
    session.close()
