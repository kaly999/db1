__author__ = 'kaly'
# -*- coding: utf-8 -*-

import MySQLdb


class Database:

    host = "localhost" #"127.0.0.1"
    user = "root"
    password = "root123"
    db = "dbpyqt4"

    def __init__(self):
        self.connection = MySQLdb.connect(host=self.host,
                                          user=self.user,
                                          password=self.password,
                                          db=self.db)

    def query(self, q):
        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(q)

        return cursor.fetchall()

    def __del__(self):
        self.connection.close()

if __name__ == "__main__":
    db = Database()

    q = "DELETE FROM person"

    db.query(q)

    q = """
        INSERT INTO `person`
        (`Per_Dni`, `Per_Names`, `Per_Surname`, `Per_Date`)
        VALUES
        ('1111','jose','tomas','2014-01-01'),
        ('1112','Miguel','Solis','2014-01-01')
        """

    people = db.query(q)

    for person in people:
        print "found: %s " % person['Per_Names']