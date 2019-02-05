# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ComposantTP4.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(753, 604)
        self.mLabel = QtWidgets.QLabel(Form)
        self.mLabel.setGeometry(QtCore.QRect(10, 30, 640, 480))
        self.mLabel.setMinimumSize(QtCore.QSize(640, 480))
        self.mLabel.setStyleSheet("\n"
"background-color: rgb(0, 255, 0);")
        self.mLabel.setText("")
        self.mLabel.setObjectName("mLabel")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 560, 641, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mLineEdit = QtWidgets.QLineEdit(self.widget)
        self.mLineEdit.setReadOnly(True)
        self.mLineEdit.setObjectName("mLineEdit")
        self.horizontalLayout.addWidget(self.mLineEdit)
        spacerItem = QtWidgets.QSpacerItem(288, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.mButtonBrowse = QtWidgets.QPushButton(self.widget)
        self.mButtonBrowse.setObjectName("mButtonBrowse")
        self.horizontalLayout.addWidget(self.mButtonBrowse)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(660, 200, 82, 81))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mButtonN = QtWidgets.QPushButton(self.widget1)
        self.mButtonN.setObjectName("mButtonN")
        self.verticalLayout.addWidget(self.mButtonN)
        self.mButtonP = QtWidgets.QPushButton(self.widget1)
        self.mButtonP.setObjectName("mButtonP")
        self.verticalLayout.addWidget(self.mButtonP)

        self.retranslateUi(Form)
        self.mButtonN.clicked.connect(Form.Next)
        self.mButtonP.clicked.connect(Form.Previous)
        self.mButtonBrowse.clicked.connect(Form.LoadFiles)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.mButtonBrowse.setText(_translate("Form", "..."))
        self.mButtonN.setText(_translate("Form", "Next"))
        self.mButtonP.setText(_translate("Form", "Previous"))

