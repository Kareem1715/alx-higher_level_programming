#!/usr/bin/python3
'''In this module we will lists all cities from the database hbtn_0e_4_usa'''
import MySQLdb
from sys import argv


if __name__ == '__main__':

    data_base = MySQLdb.connect(host='localhost',
                                port=3306,
                                user=argv[1],
                                passwd=argv[2],
                                database=argv[3])

    cur = data_base.cursor()
    cur.execute('SELECT cities.name \
                   FROM cities \
                   JOIN states ON cities.state_id = states.id \
                  WHERE states.name = %s', (argv[4], ))

    rows = cur.fetchall()

    # This line use list comprehension to exract the first index
    # that have city name of the given state
    print(', '.join(each_row[0] for each_row in rows))

    # This is the first solution I did then I found the power
    # of join() function in python and used it
    #
    # x = 0
    # for i in rows:
    #     for col in i:
    #         print(col, end='')
    #     if (x < len(rows) - 1):
    #         print(', ', end='')
    #         x += 1
    # print()

    cur.close()
    data_base.close()
