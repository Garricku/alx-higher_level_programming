#!/usr/bin/python3
"""
Defines the module 1-filter_states
Write a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""


import MySQLdb
import sys
"""
Defines the imported modules
"""


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    s = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    cur = db.cursor()
    cur.execute(s)

    for row in cur.fetchall():
        print("({}, '{}')".format(row[0], row[1]))

    cur.close()
    db.close()
