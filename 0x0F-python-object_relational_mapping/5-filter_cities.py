#!/usr/bin/python3
"""
this module will list all 'states' starting where the name is `arg`
from the database 'hbtn_0e_0_usa'
protects from sql injection

This script will accept three arguments
    mysql_username: the username of the mysql server
    mysql_password: the password for the user
    database name: the database in which 'states' table is found

    server - localhost
    port - 3306
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    usr = sys.argv[1]
    paswrd = sys.argv[2]
    data_base = sys.argv[3]
    name = sys.argv[4]
    datab = MySQLdb.connect("localhost", usr, paswrd, data_base, port=3306)
    cur = datab.cursor()
    cur.execute(" SELECT cities.name FROM cities \
        join states on states.id = cities.state_id\
        WHERE states.name = '{0}'\
        ORDER BY cities.id".format(name))
    r = cur.fetchall()
    for id in range(len(r)):
        for i in r[id]:
            print(i, end=", ") if id != len(r) - 1 else print(i)
    cur.close()
    datab.close()
