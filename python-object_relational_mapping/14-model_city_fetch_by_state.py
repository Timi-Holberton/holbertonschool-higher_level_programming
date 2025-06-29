#!/usr/bin/python3
"""
Script qui affiche toutes les villes de la base MySQL hbtn_0e_14_usa
associées à leur état (State). Affiche les résultats au format :
<state name>: (<city id>) <city name>, triés par identifiant croissant.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import State

def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    connection_url = f"mysql+mysqldb://{username}:{password}@localhost/{database}"

    engine = create_engine(connection_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    session.close()

if __name__ == "__main__":
    main()
