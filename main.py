# -*- coding:utf-8 -*-
import sys
import mainwindow
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
game_start = mainwindow.MainWindow()
game_start.show()
sys.exit(app.exec_())

