# -*- coding: utf-8 -*-

"""
Module implementing Principal.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from PyQt4 import QtGui, QtCore, QtSql

import MySQLdb

from ui.Ui_Principal import Ui_Principal

class MainWindow(QMainWindow, Ui_Principal):

    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        self.db_conexion()

        QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def db_conexion(self):
        db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        db.setHostName("127.0.0.1")
        db.setDatabaseName("dbpyqt4")
        db.setUserName("root")
        db.setPassword("root123")
        return db

    @pyqtSignature("")
    def on_btnEliminar_released(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_btnGuardar_released(self):
        db = self.db_conexion()
        sql = "INSERT INTO person(Per_Dni, Per_Names, Per_Surname, Per_Date) VALUES ('9966224', 'joselito',  'pinga',  '2014-07-06'"
        QtSql.QSqlQuery.executedQuery(sql)
        QtSql.QSqlQuery.exec_()
    
    @pyqtSignature("")
    def on_btnSalir_released(self):
        self.close()

    @pyqtSignature("")
    def on_btnCargar_released(self):
        db = self.db_conexion()
        if (db.open()==False):
            QtGui.QMessageBox.critical(None, "Database Error", db.lastError().text())

        query = QtSql.QSqlQuery("SELECT * FROM person")

        self.tabla.setColumnCount(query.record().count())
        self.tabla.setRowCount(query.size())

        index=0
        while (query.next()):
            self.tabla.setItem(index,0,QtGui.QTableWidgetItem(query.value(0).toString()))
            self.tabla.setItem(index,1,QtGui.QTableWidgetItem(query.value(1).toString()))
            index = index+1

        self.tabla.show()

