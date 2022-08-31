# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtChatApp.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChatApp(object):
    def setupUi(self, ChatApp):
        ChatApp.setObjectName("ChatApp")
        ChatApp.setEnabled(True)
        ChatApp.resize(764, 548)
        ChatApp.setMinimumSize(QtCore.QSize(764, 548))
        ChatApp.setMaximumSize(QtCore.QSize(764, 548))
        ChatApp.setAutoFillBackground(False)
        ChatApp.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.messagesList = QtWidgets.QListWidget(ChatApp)
        self.messagesList.setGeometry(QtCore.QRect(170, 70, 451, 311))
        self.messagesList.setMinimumSize(QtCore.QSize(451, 311))
        self.messagesList.setMaximumSize(QtCore.QSize(451, 311))
        self.messagesList.setObjectName("messagesList")
        self.yesButton = QtWidgets.QPushButton(ChatApp)
        self.yesButton.setGeometry(QtCore.QRect(250, 400, 81, 21))
        self.yesButton.setMinimumSize(QtCore.QSize(81, 21))
        self.yesButton.setMaximumSize(QtCore.QSize(81, 21))
        font = QtGui.QFont()
        font.setKerning(True)
        self.yesButton.setFont(font)
        self.yesButton.setStyleSheet("color : rgb(73, 56, 255)")
        self.yesButton.setObjectName("yesButton")
        self.noButton = QtWidgets.QPushButton(ChatApp)
        self.noButton.setGeometry(QtCore.QRect(440, 400, 81, 21))
        self.noButton.setMinimumSize(QtCore.QSize(81, 21))
        self.noButton.setMaximumSize(QtCore.QSize(81, 21))
        self.noButton.setStyleSheet("color : rgb(73, 56, 255)")
        self.noButton.setObjectName("noButton")
        self.resultLabel = QtWidgets.QLabel(ChatApp)
        self.resultLabel.setGeometry(QtCore.QRect(160, 460, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.resultLabel.setFont(font)
        self.resultLabel.setStyleSheet("color : rgb(73, 56, 255)")
        self.resultLabel.setObjectName("resultLabel")
        self.result = QtWidgets.QLineEdit(ChatApp)
        self.result.setGeometry(QtCore.QRect(230, 450, 381, 41))
        self.result.setObjectName("result")
        self.Title = QtWidgets.QLabel(ChatApp)
        self.Title.setGeometry(QtCore.QRect(230, 20, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color : rgb(73, 56, 255)")
        self.Title.setObjectName("Title")

        self.retranslateUi(ChatApp)
        QtCore.QMetaObject.connectSlotsByName(ChatApp)

    def retranslateUi(self, ChatApp):
        _translate = QtCore.QCoreApplication.translate
        ChatApp.setWindowTitle(_translate("ChatApp", "ChatApp - Client"))
        self.yesButton.setText(_translate("ChatApp", "Yes"))
        self.noButton.setText(_translate("ChatApp", "No"))
        self.resultLabel.setText(_translate("ChatApp", "Result:"))
        self.Title.setText(_translate("ChatApp", " Depression Self Assessment"))


import images_rc
