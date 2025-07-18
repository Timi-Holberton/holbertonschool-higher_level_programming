#!/usr/bin/python3
"""
Script affichant tous les états dont le nom commence par 'N'
depuis une base MySQL.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
        )

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM states "
        "WHERE name LIKE BINARY 'N%' "
        "ORDER BY states.id ASC;"
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
