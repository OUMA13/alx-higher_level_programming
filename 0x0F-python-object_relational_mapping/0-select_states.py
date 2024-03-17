#!/usr/bin/python3
"""This script lists all states from the
database `hbtn_0e_0_usa"""

import MySQLdb
import sys
if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    Mdb = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], Mdb=sys.argv[3], port=3306)

    cr = mdb.cursor()
    cr.execute(
        "SELECT * FROM states;"

    )
    states = cr.fetchall()
    for state in states:
        print(state)
    cr.close()
    mdb.close()
