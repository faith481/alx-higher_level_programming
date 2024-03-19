#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
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
            'SELECT * FROM states WHERE CAST(name AS BINARY) ' +
            'LIKE %s ORDER BY id ASC;'
        )
        dbcur.execute(dbqry, ('%' + stname + '%',))
        qryres = dbcur.fetchall()
        for row in qryres:
            print(row)
        dbconn.close()
