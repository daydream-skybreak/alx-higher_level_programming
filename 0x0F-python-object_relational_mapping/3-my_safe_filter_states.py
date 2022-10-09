#!/usr/bin/python3
"""
this module will list all 'states' starting where the name is `arg`
from the database 'hbtn_0e_0_usa'
protects from sql injection

This script will accept three arguments
    mysql_username: the username of the mysql server
    mysql_password: the password for the user
    database name: the database in which 'states' table is found
    name_constraint: the name where `states.name` should be

    server - localhost
    port - 3306
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    usr = sys.argv[1]
    paswrd = sys.argv[2]
    data_base = sys.argv[3]
    const = sys.argv[4]
    datab = MySQLdb.connect("localhost", usr, paswrd, data_base, port=3306)
    cur = datab.cursor()
    cur.execute(" SELECT * FROM states \
    WHERE name= \"{0}\" ORDER BY states.id".format(const))
    r = cur.fetchall()
    for row in r:
        print(row)
    cur.close()
    datab.close()
