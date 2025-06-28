#!/usr/bin/env python3
"""
Script affichant les états dont le nom correspond exactement à un nom donné.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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
        "WHERE BINARY name = '{}' ORDER BY id ASC;".format(state_name)
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
