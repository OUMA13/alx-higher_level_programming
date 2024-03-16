#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    Mdb = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], Mdb=argv[3])

    cr = Mdb.cursor()
    cr.execute("SELECT * FROM states")
    row2 = cr.fetchall()

    for row1 in row2:
        print(row1)
