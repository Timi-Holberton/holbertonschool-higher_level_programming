#!/usr/bin/python3
"""
Script qui affiche toutes les villes de la base MySQL hbtn_0e_14_usa
associées à leur état (State).

Le script prend en arguments la connexion MySQL (username, password, database),
et affiche chaque ville au format :
<state name>: (<city id>) <city name>

Les résultats sont triés par identifiant de ville (id croissant).
"""

import sys
from model_city import City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Récupération des arguments de connexion MySQL passés en ligne commande
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Construction de l'URL de connexion pour SQLAlchemy avec MySQLdb
    connection_url = (
        f"mysql+mysqldb://{username}:{password}@localhost/"
        f"{database}"
    )

    # Création de l'engine SQLAlchemy
    engine = create_engine(connection_url, pool_pre_ping=True)

    # Création d'une session ORM
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête pour récupérer les villes et leur état associé
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Affichage des résultats
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Fermeture de la session
    session.close()
