#!/usr/bin/python3
"""
Defines the module 2-my_filter_states
Script that takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys
"""
Defines the imported modules
"""


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    sql = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"\
          .format(sys.argv[4])

    cur = db.cursor()
    cur.execute(sql)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
