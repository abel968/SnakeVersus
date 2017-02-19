
import sys
from PyQt4 import QtGui,QtCore,Qt
from PyQt4.QtGui import *
import snake, introduction

Window_Width = Window_Height = 600

class MainWindow(QtGui.QWidget):
    # global Window_Height,Window_Width

    def __init__(self, parent = None):
        global map
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('SnakeVersus')
        self.resize(Window_Width, Window_Height)
        self.setWindowIcon(QtGui.QIcon('./Image/snake_icon.png'))
        self.initUI()

    def initUI(self):

        self.snake = snake.Snake()
        self.prev_snake = [0]             #means the position in the previous step
        map=[0 for x in range(400)]

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

        self.VBOX = QtGui.QVBoxLayout()
        self.VBOX.addLayout(self.grid)

        self.HELP_BUTTON = QtGui.QPushButton('Help')
        self.HELP_BUTTON.clicked.connect(self.showHelp)
        self.VBOX.addWidget(self.HELP_BUTTON)

        self.setLayout(self.VBOX)

    def keyPressEvent(self, event):
        'Receive direction keys to control the user snake.'
        if event.key() == QtCore.Qt.Key_S or event.key() == QtCore.Qt.Key_Down:
            self.snake.down()
        elif event.key() == QtCore.Qt.Key_W or event.key() == QtCore.Qt.Key_Up:
            self.snake.up()
        elif event.key() == QtCore.Qt.Key_A or event.key() == QtCore.Qt.Key_Left:
            self.snake.left()
        elif event.key() == QtCore.Qt.Key_D or event.key() == QtCore.Qt.Key_Right:
            self.snake.right()
        for i in self.prev_snake:
            if i not in self.snake.hold:
                self.lables[i].setPalette(self.pe1)
        for i in self.snake.hold:
            if i not in self.prev_snake:
                self.lables[i].setPalette(self.pe2)
        self.prev_snake = self.snake.hold[:]

    def showHelp(self):
        'show help document in new dialog'
        HelpDialog = introduction.IntroWindow()
        HelpDialog.show()

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())