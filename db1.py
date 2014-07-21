# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui, QtSql
from Principal import MainWindow

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()

    sys.exit(app.exec_())
