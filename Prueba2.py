#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="root123",
                     db="dbpyqt4")


cursor = db.cursor()

q = """
        INSERT INTO `person`
        (`Per_Dni`, `Per_Names`, `Per_Surname`, `Per_Date`)
        VALUES
        ('1116','jose','tomas','2014-01-01'),
        ('1117','Miguel','Solis','2014-01-01')
        """
cursor.execute(q)
db.commit()

cursor.execute("SELECT * FROM person")

for row in cursor.fetchall():
    print str(row[0]) + " " + row[1] + " " + row[2]

cursor.close()
db.close()