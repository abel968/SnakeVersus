# -*- coding:utf-8 -*-
from PyQt4 import QtGui
from PyQt4.QtGui import QColor


class SetPreferences(QtGui.QDialog):
    def __init__(self, dog, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.resize(300,300)
        self.setWindowTitle('Preferences')

        self.mainvbox = QtGui.QVBoxLayout()
# add difficult radio box
        self.diff_radio_box = QtGui.QHBoxLayout()
        self.diff_label = QtGui.QLabel("Difficult level:  ")
        self.radiobutton1 = QtGui.QRadioButton("Easy")
        self.radiobutton1.toggled.connect(lambda: set_level(self.radiobutton1))
        self.radiobutton2 = QtGui.QRadioButton("Normal")
        self.radiobutton2.toggled.connect(lambda: set_level(self.radiobutton2))
        self.radiobutton3 = QtGui.QRadioButton("Hard")
        self.radiobutton3.toggled.connect(lambda: set_level(self.radiobutton3))
# set buttons isChecked or not
        import mainwindow
        diff = mainwindow.DIFFICULT
        self.radiobutton1.setChecked(diff == 1)
        self.radiobutton2.setChecked(diff == 2)
        self.radiobutton3.setChecked(diff == 3)
# add radio buttons into diff_radio_box
        self.diff_radio_box.addWidget(self.diff_label)
        self.diff_radio_box.addWidget(self.radiobutton1)
        self.diff_radio_box.addWidget(self.radiobutton2)
        self.diff_radio_box.addWidget(self.radiobutton3)
        self.mainvbox.addLayout(self.diff_radio_box)
# add theme combo box
        self.theme_hbox = QtGui.QHBoxLayout()
        self.theme_label = QtGui.QLabel("Theme:  ")
        self.theme_combo_box = QtGui.QComboBox()
        self.theme_combo_box.addItems(["GrassLand", "Dark", "ColorBlind"])
        self.theme_combo_box.currentIndexChanged.connect(lambda: set_theme(self.theme_combo_box, dog))
        self.theme_hbox.addWidget(self.theme_label)
        self.theme_hbox.addWidget(self.theme_combo_box)
        self.mainvbox.addLayout(self.theme_hbox)
#add bottom button
        self.accept_button = QtGui.QPushButton("Accept")
        self.accept_button.clicked.connect(self.accept)
        self.mainvbox.addWidget(self.accept_button)
# set layout
        self.setLayout(self.mainvbox)


def set_theme(combo,dog):
    if combo.currentText() == "GrassLand":
        dog.setcolor(QColor(192,253,123),QColor(255,255,0),QColor(255,0,0))
    elif combo.currentText() == "Dark":
        dog.setcolor(QColor(0,0,0),QColor(255,255,255),QColor(127,127,127))
    elif combo.currentText() == "ColorBlind":
        dog.setcolor(QColor(104,151,187),QColor(165,194,97),QColor(204,120,50))


def set_level(button):
    import mainwindow
    if button.text() == "Easy":
        if button.isChecked():
            mainwindow.DIFFICULT = 1
    if button.text() == "Normal":
        if button.isChecked():
            mainwindow.DIFFICULT = 2
    if button.text() == "Hard":
        if button.isChecked():
            mainwindow.DIFFICULT = 3
