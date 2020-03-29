#!/usr/bin/python3
"""script that takes in the name of a state as an argument
 and lists all cities of that state,
 using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(
        host="localhost", user=argv[1],
        passwd=argv[2], port=3306, db=argv[3])
    word = MySQLdb.escape_string(argv[4]).decode()
    cur = db.cursor()
    cur.execute("SELECT cities.name\
         FROM states INNER JOIN cities ON \
             states.name='{}' AND states.id=cities.state_id ORDER BY cities.id".format(word))
    rows = cur.fetchall()
    i = 0
    for row in rows:
        if i != 0:
            print(", ", end="")
        i+=1
        print(row[0], end="")
    print()
    db.close()
    cur.close()

