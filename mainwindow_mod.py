
import sys
from PyQt4 import QtGui,QtCore,Qt
from PyQt4.QtGui import *
import snake

Window_Width = Window_Height = 600

class GridLayout(QtGui.QWidget):
    global Window_Height,Window_Width

    def __init__(self, parent = None):
        global map
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('SnakeVersus')
        self.resize(Window_Width, Window_Height)
        self.setWindowIcon(QtGui.QIcon('./Image/snake_icon.png'))

        self.snake = snake.Snake()
        self.presnake = [0]             #means the position in the previous step
        map=[0 for x in range(400)]
        # for i in range(400):
        #     map.append(0)

        self.pe1 = QtGui.QPalette()
        self.pe1.setColor(self.backgroundRole(), QColor(192, 253, 123)) #configure the color of the Empty box
        self.pe2 = QtGui.QPalette()
        self.pe2.setColor(self.backgroundRole(), QColor(192, 0, 123))  # configure the color of the Not-Empty box
        self.grid = QtGui.QGridLayout()

        self.lables = []
        for i in range(20):
            for j in range(20):
                label = QtGui.QLabel(self)
                label.setAutoFillBackground(True)
                label.setPalette(self.pe1)
                self.grid.addWidget(label, i, j)
                self.lables.append(label)
        self.lables[0].setPalette(self.pe2)
        self.grid.setSpacing(1)
        self.setLayout(self.grid)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_S:
            self.snake.down()
        elif event.key() == QtCore.Qt.Key_W:
            self.snake.up()
        elif event.key() == QtCore.Qt.Key_A:
            self.snake.left()
        elif event.key() == QtCore.Qt.Key_D:
            self.snake.right()
        for i in self.presnake:
            if i not in self.snake.hold:
                self.lables[i].setPalette(self.pe1)
        for i in self.snake.hold:
            if i not in self.presnake:
                self.lables[i].setPalette(self.pe2)
        self.presnake = self.snake.hold[:]
app = QtGui.QApplication(sys.argv)
gridlayout = GridLayout()
gridlayout.show()
sys.exit(app.exec_())