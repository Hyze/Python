# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DebutCasino.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(938, 300)
        self.Gauche = QtWidgets.QLabel(Form)
        self.Gauche.setGeometry(QtCore.QRect(0, 0, 300, 300))
        self.Gauche.setStyleSheet("background-color: rgb(0, 85, 0);")
        self.Gauche.setObjectName("Gauche")
        self.Centre = QtWidgets.QLabel(Form)
        self.Centre.setGeometry(QtCore.QRect(300, 0, 300, 300))
        self.Centre.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.Centre.setObjectName("Centre")
        self.Droite = QtWidgets.QLabel(Form)
        self.Droite.setGeometry(QtCore.QRect(600, 0, 300, 300))
        self.Droite.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.Droite.setObjectName("Droite")
        self.Start = QtWidgets.QPushButton(Form)
        self.Start.setGeometry(QtCore.QRect(900, 0, 41, 300))
        self.Start.setObjectName("Start")

        self.retranslateUi(Form)
        self.Start.clicked.connect(Form.casino)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Gauche.setText(_translate("Form", "TextLabel"))
        self.Centre.setText(_translate("Form", "TextLabel"))
        self.Droite.setText(_translate("Form", "TextLabel"))
        self.Start.setText(_translate("Form", "PushButton"))

