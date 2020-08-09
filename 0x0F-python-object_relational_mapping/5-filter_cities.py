#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                   FROM states, cities
                   WHERE cities.state_id = states.id
                   AND BINARY states.name = %s
                   ORDER BY cities.id""", (sys.argv[4], ))
    rows = cur.fetchall()
    for i in range(len(rows)):
        if i == len(rows) - 1:
            print("{}".format(rows[i][1]), end="")
        else:
            print("{}, ".format(rows[i][1]), end="")
    print()
    cur.close()
    conn.close()
