#!/usr/bin/python3
"""Module that that lists all cities from the database"""


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
            'SELECT cities.name FROM cities ' +
            'INNER JOIN states ON cities.state_id = states.id ' +
            'WHERE CAST(states.name AS BINARY) = %s ' +
            'ORDER BY cities.id ASC;'
        )
        dbcur.execute(dbqry, (stname,))
        qryres = dbcur.fetchall()
        print(', '.join(map(lambda cty: cty[0], qryres)))
        dbconn.close()
