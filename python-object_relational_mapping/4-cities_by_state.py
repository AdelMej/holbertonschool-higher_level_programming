#!/usr/bin/python3
"""
File containing a script that lists all cities
from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    mysql_database = argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_database,
        charset="utf8mb4"
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM cities "
        "INNER JOIN states "
        "ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
