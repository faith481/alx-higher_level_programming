#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
import sys


if __name__ == '__main__':
    if len(sys.argv) >= 5:
        dbconn = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
        )
        dbcur = dbconn.cursor()
        stname = sys.argv[4]
        dbqry = (
            'SELECT * FROM states WHERE CAST(name AS BINARY) LIKE ' +
            'CAST("{}" AS BINARY) ORDER BY id ASC;'.format(stname)
        )
        dbcur.execute(dbqry)
        qryres = dbcur.fetchall()
        for row in qryres:
            print(row)
        dbconn.close()
