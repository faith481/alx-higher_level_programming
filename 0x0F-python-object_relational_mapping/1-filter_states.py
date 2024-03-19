#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        dbconn = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
        )
        dbcur = dbconn.cursor()
        dbqry = (
            'SELECT * FROM states WHERE name IS NOT NULL AND' +
            ' LEFT(CAST(name AS BINARY), 1) = "N" ORDER BY states.id ASC;'
        )
        dbcur.execute(dbqry)
        qryres = dbcur.fetchall()
        for row in qryres:
            print(row)
        dbconn.close()
