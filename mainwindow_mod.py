import constants_mod

import sys
from PyQt4 import QtGui

class Center(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('SnakeVersus')
        self.resize(constants_mod.Window_Wideth, constants_mod.Window_Height)
        self.setWindowIcon(QtGui.QIcon('./Image/snake_icon.png'))
        self.center()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,(screen.height() - size.height()) / 2)

snake_app = QtGui.QApplication(sys.argv)
main_window = Center()
main_window.show()
sys.exit(snake_app.exec_())