#!/usr/bin/python3
"""
Script qui supprime tous les objets State dont le nom contient la lettre 'a'
dans la base MySQL.

Le script prend en arguments la connexion MySQL (username, password, database),
recherche tous les états contenant la lettre 'a' dans leur nom,
supprime ces enregistrements de la base,
puis valide et applique la suppression.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Récupération des arguments de connexion MySQL passés en ligne de commande :
    # - username : nom d'utilisateur MySQL
    # - password : mot de passe MySQL
    # - database : nom de la base de données ciblée
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Construction de l'URL de connexion pour SQLAlchemy avec MySQLdb
    connection_url = (
        f"mysql+mysqldb://{username}:{password}@localhost/"
        f"{database}"
    )

    # Création de l'engine SQLAlchemy gère la connexion physique
    # à la base de données
    engine = create_engine(connection_url, pool_pre_ping=True)

    # Création d'une session ORM pour interagir avec la base via  objets Python
    Session = sessionmaker(bind=engine)
    session = Session()

    # Recherche de tous les objets State dont le nom contient la lettre 'a'
    etats_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Parcours des objets trouvés et suppression un par un
    for etat in etats_delete:
        session.delete(etat)

    # Validation des suppressions dans la base (exécution des DELETE)
    session.commit()

    # Fermeture de la session pour libérer les ressources système
    session.close()
