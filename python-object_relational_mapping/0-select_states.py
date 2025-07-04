#!/usr/bin/python3

"""
Liste tous les États depuis la base hbtn_0e_0_usa.
Connexion via MySQLdb, sans validation d’arguments.
Résultats triés par states.id (ordre croissant).
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Arguments passés en ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connexion à MySQL
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
        )

    # Création d’un curseur
    cursor = connection.cursor()

    # Requête SQL
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    row = cursor.fetchall()

    # Affichage des résultats ligne par ligne
    for row in row:
        print(row)

    # Fermeture
    cursor.close()
    connection.close()
