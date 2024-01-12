#!/usr/bin/python3
"""
Defines the module 3-my_safe_filter_states
Your script should take 4 arguments: mysql username, mysql password, database
name and state name searched (safe from MySQL injection)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
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
