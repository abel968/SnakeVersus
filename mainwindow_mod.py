
import sys
from PyQt4 import QtGui,QtCore,Qt
from PyQt4.QtGui import *

Window_Width = Window_Height = 600

class GridLayout(QtGui.QWidget):
    global Window_Height,Window_Width

    def __init__(self, parent = None):
        global map
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('SnakeVersus')
        self.resize(Window_Width, Window_Height)
        self.setWindowIcon(QtGui.QIcon('./Image/snake_icon.png'))

        map=[]
        for i in range(400):
            map.append(0)

        pe1 = QtGui.QPalette()
        pe1.setColor(self.backgroundRole(), QColor(192, 253, 123)) #configure the color of the Empty box
        pe2 = QtGui.QPalette()
        pe2.setColor(self.backgroundRole(), QColor(192, 0, 123))  # configure the color of the Not-Empty box
        grid = QtGui.QGridLayout()

        for i in range(20):
            for j in range(20):
                label = QtGui.QLabel()
                label.setAutoFillBackground(True)
                if(map[i*20+j] == 0):
                    label.setPalette(pe1)
                else:
                    label.setPalette(pe2)
                label.setPalette(pe1)

                grid.addWidget(label, i, j)

        grid.setSpacing(1)
        self.setLayout(grid)

app = QtGui.QApplication(sys.argv)
gridlayout = GridLayout()
gridlayout.show()
sys.exit(app.exec_())