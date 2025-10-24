#!/usr/bin/python3
"""
File containing a script for connection to a mysql_database
Query all the states starting by N
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    mysql_database = argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_database,
        port=3306,
        charset="utf8mb4"
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE states.name LIKE 'N%' ORDER BY states.id ASC")
    for query in cursor.fetchall():
        print(query)

    cursor.close()
    db.close()
