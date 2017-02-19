import sys
from PyQt4 import QtGui

class IntroWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.text = 'Test text.'
        self.setGeometry = (300, 300, 280, 170)
        self.setWindowTitle = ('Introduction')
        #self.drawText()

    # def drawText(self, event, qp):
    #     qp.setPen(QtGui.QColor(168, 34, 3))
    #     qp.setFont(QtGui.QFont('Decorative', 10))
    #     qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)
