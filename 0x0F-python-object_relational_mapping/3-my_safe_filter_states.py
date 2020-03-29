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
    word = MySQLdb.escape_string(argv[4]).decode()
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE name LIKE '{}%'\
         ORDER BY id".format(word))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
    cur.close()
