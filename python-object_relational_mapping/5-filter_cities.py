#!/usr/bin/python3
"""
Script qui affiche toutes les villes d'un État donné
dans la base de données hbtn_0e_4_usa.
"""
# Module permettant de se connecter à une base de données MySQL
import MySQLdb
# Module permettant d'accéder aux arguments de la ligne de commande
import sys

# Récupération des arguments passés en ligne de commande
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connexion à la base de données MySQL sur localhost:3306
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
        )

    # Création d'un curseur pour exécuter des requêtes SQL
    cursor = connection.cursor()

    # Exécution d'une requête SQL pour récupérer toutes les villes
    # avec le nom de leur État, triées par identifiant de ville (cities.id)
    cursor.execute(
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC;", (state_name,))
    # ajout d'une virgyule à la fin de state_name pour faire un tuple

    # Récupération de toutes les lignes de résultats
    rows = cursor.fetchall()

    # Transforme les résultats en une liste de noms de villes
    # puis les affiche séparés par des virgules
    cities = []
    for row in rows:
        cities.append(row[0])
    print(", ".join(cities))
    # print(", ".join([row[0] for row in rows]))

    # Fermeture du curseur et de la connexion à la base de données
    cursor.close()
    connection.close()
