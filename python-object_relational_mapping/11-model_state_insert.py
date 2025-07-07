#!/usr/bin/python3
"""
Script qui ajoute un nouvel objet State ("Louisiana") à la base MySQL.

Le script prend en arguments la connexion MySQL (username, password, database),
ajoute un nouvel état avec le nom "Louisiana",
et affiche son id après insertion.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Récupération des paramètres MySQL depuis la ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Construction de l'URL de connexion à la base
    connection_url = (
    f"mysql+mysqldb://{username}:{password}@localhost/{database}"
)
    # Création de l'engine SQLAlchemy
    engine = create_engine(connection_url, pool_pre_ping=True)

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Création et ajout du nouvel objet State
    nouvel_etat = State(name="Louisiana")
    session.add(nouvel_etat)
    session.commit()

    # Affichage de l'id de l'objet nouvellement inséré
    print(nouvel_etat.id)

    # Fermeture de la session
    session.close()
