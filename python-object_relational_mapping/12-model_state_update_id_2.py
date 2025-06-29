#!/usr/bin/env python3
"""
Script qui modifie le nom de l'objet State avec l'id 2 dans la base MySQL.

Le script prend en arguments la connexion MySQL (username, password, database),
recherche l'état avec l'id 2, modifie son nom en "New Mexico",
et valide la modification.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Récupération des paramètres MySQL depuis la ligne de commande :
    # username, password et nom de la base de données
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Construction de l'URL de connexion compatible SQLAlchemy avec MySQLdb
    connection_url = (
        f"mysql+mysqldb://{username}:{password}@localhost/"
        f"{database}"
    )

    # Création de l'engine SQLAlchemy qui gère la connexion à la base
    engine = create_engine(connection_url, pool_pre_ping=True)

    # Création d'une session (interface pour faire des opérations ORM)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Recherche dans la table states de l'objet State avec id égal à 2
    etat = session.query(State).filter(State.id == 2).first()

    # Si l'objet est trouvé
    if etat:
        # Modification de l'attribut name pour "New Mexico"
        etat.name = "New Mexico"
        # Enregistrement de la modification dans la base de données
        session.commit()

    # Fermeture de la session pour libérer les ressources système
    session.close()
