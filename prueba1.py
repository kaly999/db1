#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui

import MySQLdb


class Database:

    host = "localhost" #"127.0.0.1"
    user = "root"
    password = "root123"
    db = "dbpyqt4"

    def __init__(self):
        self.connection = MySQLdb.connect(self.host,
                                          self.user,
                                          self.password,
                                          self.db)

    def query(self, q):
        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(q)

        return cursor.fetchall()

    def __del__(self):
        self.connection.close()


if __name__ == "__main__":

    db = Database()

    q = "SELECT * FROM person"

    people = db.query(q)

    for person in people:
        print "found: %s " % person['Per_Names']

    # generar ventana
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = QtGui.QMainWindow()
    ui.show()
    sys.exit(app.exec_())   # MainLoop que me mantiene viva a la aplicación