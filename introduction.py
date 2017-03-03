import sys
from PyQt4 import QtGui,QtCore

class HelpWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.resize(200,200)
        self.setWindowTitle('Introduction')
        #self.drawText()

    # def drawText(self, event, qp):
    #     qp.setPen(QtGui.QColor(168, 34, 3))
    #     qp.setFont(QtGui.QFont('Decorative', 10))
    #     qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)

class EndMessage(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.resize(200,200)
        self.setWindowTitle('GameOver')


def callEndMessage(SIGNAL):
    'SIGNAL here should be the method isAI/UserOver'
    end_message = EndMessage()
    if SIGNAL == 1:
        text = 'You Win!'
    elif SIGNAL == 2:
        text = 'Defeat...'
    end_message.show()
