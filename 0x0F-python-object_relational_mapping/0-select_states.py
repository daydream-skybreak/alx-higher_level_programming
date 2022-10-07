#!/usr/bin/python3
if __name__ == '__main__':
    import MySQLdb
    import sys

    usr = sys.argv[1]
    paswrd = sys.argv[2]
    data_base = sys.argv[3]
    datab = MySQLdb.connect("localhost", usr, paswrd, data_base, port=3306)
    cur = datab.cursor()
    cur.execute(" SELECT * FROM states ORDER BY states.id")
    r = cur.fetchall()
    for row in r:
        print(row)
