#!/usr/bin/python3
"""
Script qui affiche toutes les villes de la base MySQL hbtn_0e_14_usa
associées à leur état (State). Affiche les résultats au format :
<state name>: (<city id>) <city name>, triés par identifiant croissant.
"""

import sys
from model_city import City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    Connexion à la base de données MySQL, récupération et affichage
    des villes avec leur état associé.
    """
    # Récupère les arguments passés en ligne de commande :
    # username, password, database
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Construire l'URL de connexion SQLAlchemy pour MySQLdb
    connection_url = (
        f"mysql+mysqldb://{username}:{password}@localhost/{database}"
    )

    # Création de l'engine SQLAlchemy qui gère la connexion physique à la base
    engine = create_engine(connection_url, pool_pre_ping=True)

    # Création d'une session ORM liée à l'engine pour interagir avec la BDD
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête pour récupérer toutes les villes et leurs états associés,
    # triées par identifiant de ville (id) croissant
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Parcours de la liste de tuples (City, State) et affichage formaté
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Fermeture de la session pour libérer les ressources
    session.close()


if __name__ == "__main__":
    main()
