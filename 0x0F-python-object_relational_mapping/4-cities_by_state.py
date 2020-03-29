#!/usr/bin/python3
"""script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!.
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(
        host="localhost", user=argv[1],
        passwd=argv[2], port=3306, db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
         FROM states INNER JOIN cities ON \
             states.id=cities.state_id ORDER BY cities.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
    cur.close()
