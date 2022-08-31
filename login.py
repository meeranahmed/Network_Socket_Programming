# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(557, 275)
        MainWindow.setMinimumSize(QtCore.QSize(557, 275))
        MainWindow.setMaximumSize(QtCore.QSize(557, 275))
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/doctor.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(26, 20, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setStyleSheet("color : rgb(85, 85, 255)")
        self.nameLabel.setObjectName("nameLabel")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(110, 20, 231, 20))
        self.name.setObjectName("name")
        self.age = QtWidgets.QLineEdit(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(110, 180, 51, 20))
        self.age.setObjectName("age")
        self.femaleButton = QtWidgets.QRadioButton(self.centralwidget)
        self.femaleButton.setGeometry(QtCore.QRect(110, 100, 81, 21))
        self.femaleButton.setObjectName("femaleButton")
        self.maleButton = QtWidgets.QRadioButton(self.centralwidget)
        self.maleButton.setGeometry(QtCore.QRect(240, 100, 71, 21))
        self.maleButton.setObjectName("maleButton")
        self.genderLabel = QtWidgets.QLabel(self.centralwidget)
        self.genderLabel.setGeometry(QtCore.QRect(20, 100, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.genderLabel.setFont(font)
        self.genderLabel.setStyleSheet("color : rgb(85, 85, 255)")
        self.genderLabel.setObjectName("genderLabel")
        self.ageLabel = QtWidgets.QLabel(self.centralwidget)
        self.ageLabel.setGeometry(QtCore.QRect(40, 180, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ageLabel.setFont(font)
        self.ageLabel.setStyleSheet("color : rgb(85, 85, 255)")
        self.ageLabel.setObjectName("ageLabel")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(450, 190, 75, 23))
        self.connectButton.setObjectName("connectButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 557, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login Page"))
        self.nameLabel.setText(_translate("MainWindow", "Name :"))
        self.femaleButton.setText(_translate("MainWindow", "Female"))
        self.maleButton.setText(_translate("MainWindow", "Male"))
        self.genderLabel.setText(_translate("MainWindow", "Gender :"))
        self.ageLabel.setText(_translate("MainWindow", "Age :"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))


import images_rc
