#!/usr/bin/python3
"""
Lists all states with a name given in arguments
from the database hbtn_0e_0_usa.
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    mysql_database = argv[3]
    name = argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_database,
        port=3306,
        charset="utf8mb4"
    )

    cursor = db.cursor()
    cursor.execute(
                   "SELECT * FROM states "
                   "WHERE states.name = %s"
                   "ORDER BY states.id ASC",
                   (name,)
                   )
    for query in cursor.fetchall():
        print(query)

    cursor.close()
    db.close()
