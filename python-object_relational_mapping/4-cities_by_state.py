#!/usr/bin/python3
"""
Script affichant toutes les villes de la base de données hbtn_0e_4_usa,
avec leur identifiant, leur nom et le nom de l'État auquel elles appartiennent.
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
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id;")

    # Récupération de toutes les lignes de résultats
    rows = cursor.fetchall()

    # Affichage de chaque ligne sous forme de tuple
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion à la base de données
    cursor.close()
    connection.close()
