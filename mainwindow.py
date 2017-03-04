# -*- coding:utf-8 -*-
import gamecontroller,introduction
import sys
from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtGui import *

Window_Width = Window_Height = 600

class MainWindow(QtGui.QWidget):
    global Window_Height,Window_Width

    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setWindowTitle('SnakeVersus')
        self.resize(Window_Width, Window_Height)
        self.setWindowIcon(QtGui.QIcon('./Image/snake_icon.png'))
        self.initUI()

    def initUI(self):
        self.gc = gamecontroller.Gamecontroller()
        self.begin = True  # 表示游戏未开始

        self.pe1 = QtGui.QPalette()
        self.pe1.setColor(self.backgroundRole(), QColor(192, 253, 123)) #configure the color of the Empty box
        self.pe2 = QtGui.QPalette()
        self.pe2.setColor(self.backgroundRole(), QColor(255, 255, 0))  # configure the color of the User box
        self.pe3 = QtGui.QPalette()
        self.pe3.setColor(self.backgroundRole(), QColor(255, 0, 0))  # configure the color of the AI box
        self.grid = QtGui.QGridLayout()

        self.user_pre = [0]  # means the user's position in the previous step
        self.ai_pre = [399]

        self.lables = []
        for i in range(20):
            for j in range(20):
                label = QtGui.QLabel(self)
                label.setAlignment(Qt.AlignCenter)
                label.setAutoFillBackground(True)
                label.setPalette(self.pe1)
                self.grid.addWidget(label, i, j)
                self.lables.append(label)
        self.grid.setSpacing(1)

        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(self.grid)

        bottom_hbox = QtGui.QHBoxLayout()
        help_button = QtGui.QPushButton('(H)elp', parent=self)
        help_button.clicked.connect(self.showHelp)
        restart_button = QtGui.QPushButton('(R)estart',parent=self)
        restart_button.clicked.connect(self.beginGame)
        bottom_hbox.addWidget(help_button)
        bottom_hbox.addWidget(restart_button)
        vbox.addLayout(bottom_hbox)
        self.setLayout(vbox)

        self.beginGame()

    def beginGame(self):
        'Reset the game'
        self.begin = True    #表示游戏开始
        for i in self.user_pre:
            self.lables[i].setPalette(self.pe1)
        self.lables[self.user_pre[-1]].setText('')
        for i in self.ai_pre:
            self.lables[i].setPalette(self.pe1)
        self.lables[self.ai_pre[-1]].setText('')
        self.user_pre = [0]
        self.ai_pre = [399]
        self.lables[0].setPalette(self.pe2)
        self.lables[399].setPalette(self.pe3)
        self.lables[0].setText('H')
        self.lables[399].setText('H')
        self.gc.reset()

    def showHelp(self):
        'show help document in new dialog'
        help_dialog = introduction.HelpWindow(parent=self)
        help_dialog.exec_()
        help_dialog.destroy()

    def keyPressEvent(self, event):
        'Use direction keys to control snake, Use R key to reset the game, Use H key for help'
        if not self.begin:
            return
        if event.key() == QtCore.Qt.Key_R:
            self.beginGame()
        if event.key() == QtCore.Qt.Key_H:
            self.showHelp()
        if event.key() == QtCore.Qt.Key_S or event.key() == QtCore.Qt.Key_Down:
            if self.gc.usersnake.down(self.gc.aisnake.hold) == None:
                return
        elif event.key() == QtCore.Qt.Key_W or event.key() == QtCore.Qt.Key_Up:
            if self.gc.usersnake.up(self.gc.aisnake.hold) == None:
                return
        elif event.key() == QtCore.Qt.Key_A or event.key() == QtCore.Qt.Key_Left:
            if self.gc.usersnake.left(self.gc.aisnake.hold) == None:
                return
        elif event.key() == QtCore.Qt.Key_D or event.key() == QtCore.Qt.Key_Right:
            if self.gc.usersnake.right(self.gc.aisnake.hold) == None:
                return

        else:
            return
        for i in self.user_pre:
            if i not in self.gc.usersnake.hold:
                self.lables[i].setPalette(self.pe1)
        for i in self.gc.usersnake.hold:
            if i not in self.user_pre:
                self.lables[i].setPalette(self.pe2)
        self.lables[self.user_pre[-1]].setText('')
        self.lables[self.gc.usersnake.hold[-1]].setText('H')
        self.user_pre = self.gc.usersnake.hold[:]
        if not self.gc.isAIOver():  # 若该条件成立，则输出用户赢
            self.begin = False
            end_dialog = introduction.EndWindow(1,parent=None)
            end_dialog.exec_()
            end_dialog.destroy()
            self.beginGame()
            return
        self.gc.AIChoose()
        for i in self.ai_pre:
            if i not in self.gc.aisnake.hold:
                self.lables[i].setPalette(self.pe1)
        for i in self.gc.aisnake.hold:
            if i not in self.ai_pre:
                self.lables[i].setPalette(self.pe3)
        self.lables[self.ai_pre[-1]].setText('')
        self.lables[self.gc.aisnake.hold[-1]].setText('H')
        self.ai_pre = self.gc.aisnake.hold[:]
        if not self.gc.isUserOver():  # 若该条件成立，则输出用户输
            self.begin = False
            end_dialog = introduction.EndWindow(2,parent=None)
            end_dialog.exec_()
            end_dialog.destroy()
            self.beginGame()