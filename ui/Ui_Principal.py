# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kaly\Python\db1\ui\Principal.ui'
#
# Created: Sun Jul 20 18:24:22 2014
#      by: PyQt4 ui code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Principal(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("Principal"))
        MainWindow.resize(692, 616)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabla = QtGui.QTableWidget(self.centralWidget)
        self.tabla.setObjectName(_fromUtf8("tabla"))
        self.tabla.setColumnCount(0)
        self.tabla.setRowCount(0)
        self.gridLayout.addWidget(self.tabla, 0, 0, 1, 3)
        self.txt3 = QtGui.QLineEdit(self.centralWidget)
        self.txt3.setObjectName(_fromUtf8("txt3"))
        self.gridLayout.addWidget(self.txt3, 3, 0, 1, 1)
        self.txt4 = QtGui.QLineEdit(self.centralWidget)
        self.txt4.setObjectName(_fromUtf8("txt4"))
        self.gridLayout.addWidget(self.txt4, 4, 0, 1, 1)
        self.txt2 = QtGui.QLineEdit(self.centralWidget)
        self.txt2.setObjectName(_fromUtf8("txt2"))
        self.gridLayout.addWidget(self.txt2, 2, 0, 1, 1)
        self.txt1 = QtGui.QLineEdit(self.centralWidget)
        self.txt1.setObjectName(_fromUtf8("txt1"))
        self.gridLayout.addWidget(self.txt1, 1, 0, 1, 1)
        self.btnEliminar = QtGui.QPushButton(self.centralWidget)
        self.btnEliminar.setObjectName(_fromUtf8("btnEliminar"))
        self.gridLayout.addWidget(self.btnEliminar, 3, 1, 1, 2)
        self.btnGuardar = QtGui.QPushButton(self.centralWidget)
        self.btnGuardar.setObjectName(_fromUtf8("btnGuardar"))
        self.gridLayout.addWidget(self.btnGuardar, 2, 1, 1, 2)
        self.btnSalir = QtGui.QPushButton(self.centralWidget)
        self.btnSalir.setObjectName(_fromUtf8("btnSalir"))
        self.gridLayout.addWidget(self.btnSalir, 4, 1, 1, 2)
        self.btnCargar = QtGui.QPushButton(self.centralWidget)
        self.btnCargar.setObjectName(_fromUtf8("btnCargar"))
        self.gridLayout.addWidget(self.btnCargar, 1, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Principal", "Principal", None))
        self.btnEliminar.setText(_translate("Principal", "Eliminar", None))
        self.btnGuardar.setText(_translate("Principal", "Guardar", None))
        self.btnSalir.setText(_translate("Principal", "Salir", None))
        self.btnCargar.setText(_translate("Principal", "Cargar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_Principal()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

