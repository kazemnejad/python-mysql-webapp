from mysql.connector import MySQLConnection
import calendar
from twisted.test.test_adbapi import MySQLConnector

import time

db = MySQLConnection(
        host="localhost",
        user="root",
        password="12345",
        database="test",
        autocommit=True
)

cursor = db.cursor()
cursor.execute("SELECT * FROM posts ORDER BY id LIMIT 9")
posts = cursor.fetchall()
for post in posts:
    post_id = post[0]
    for i in xrange(3):
        query = "INSERT INTO comments (id, body, created_on, post_id) " +\
            "VALUES (null"+\
            ', "Comment for ' + post[1] + '"' + \
            ', 9'+\
            ', ' + str(post_id) +\
            ')'
        print query
        cursor = db.cursor()
        cursor.execute(str(query))


db.close()