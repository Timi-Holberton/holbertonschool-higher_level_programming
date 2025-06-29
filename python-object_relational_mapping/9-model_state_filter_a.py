#!/usr/bin/python3
"""
Script qui affiche tous les objets State dont le nom contient la lettre 'a'
dans la base MySQL.

Le script prend en arguments la connexion MySQL (username, password, database)
et affiche chaque état trouvé sous la forme : <id>: <name>.
Si aucun état n'est trouvé, il n'affiche rien.
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

    # Création de l'engine SQLAlchemy pour gérer la connexion à la base
    engine = create_engine(connection_url, pool_pre_ping=True)

    # Création des tables dans la base (si elles n'existent pas encore)
    Base.metadata.create_all(engine)

    # Création d'une session pour interagir avec la base
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête pour récupérer tous les objets State dont le nom contient un 'a'
    states_avec_a = session.query(State).filter(State.name.like('%a%')).all()

    # Parcours et affichage de chaque enregistrement trouvé
    for etat in states_avec_a:
        print(f"{etat.id}: {etat.name}")

    # Fermeture de la session pour libérer les ressources
    session.close()
