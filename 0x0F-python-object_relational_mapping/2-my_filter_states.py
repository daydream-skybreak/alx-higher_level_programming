#!/usr/bin/python3
"""
this module will list all 'states' starting with 'N'
from the database 'hbtn_0e_0_usa'

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
