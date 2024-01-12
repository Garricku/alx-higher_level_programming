#!/usr/bin/python3
"""
Defines the module 1-filter_states.py
"""


import MySQLdb
import sys
"""
Defines the imported modules
"""


if __name__ == "__main__":
    # Connects to the MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # Executes the SQL query to retrieve all states starting with N
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Prints the results in the format specified in the prompt
    for row in cur.fetchall():
        print(row)

    # Closes the cursor and database connection
    cur.close()
    db.close()
