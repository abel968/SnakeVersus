# -*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore

class HelpWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.initUI()

    def initUI(self):
        self.resize(400,400)
        self.setWindowTitle('Introduction')
        self.intro_text= '这是一款人机对战游戏\n玩家控制一条逐渐增长\n的蓝色巨龙，\n与AI土蛇PK，将对方\n怼死算赢。\n祝游戏愉快～～'

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        back_button = QtGui.QPushButton('Back',parent=self)
        back_button.clicked.connect(self.reject)
        vbox.addWidget(back_button)

        self.setLayout(vbox)

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawText(event,qp)
        qp.end()

    def drawText(self, event, qp):
        qp.setPen(QtGui.QColor(168, 34, 3))
        qp.setFont(QtGui.QFont('Decorative', 18))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.intro_text)

class EndWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self,parent)
        initUI()

    def initUI(self):
        self.resize(200,200)
        self.setWindowTitle('GameOver')
        vbox = QtGui.QVBoxLayout()


def callEndMessage(SIGNAL):
    'SIGNAL here should be the method isAI/UserOver'
    win_text = 'Congratuations! :D'
    defeat_text = 'Defeat >_<'
    end_message = EndMessage()
    if SIGNAL == 1:
        text = 'You Win!'
    elif SIGNAL == 2:
        text = 'Defeat...'
    end_message.show()
