# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loginwindow(object):
    def setupUi(self, loginwindow):
        loginwindow.setObjectName("loginwindow")
        loginwindow.resize(925, 508)
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(11)
        font.setItalic(False)
        loginwindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../DBMS Project/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        loginwindow.setWindowIcon(icon)
        self.title = QtWidgets.QLabel(loginwindow)
        self.title.setGeometry(QtCore.QRect(390, 80, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.title.setObjectName("title")
        self.username = QtWidgets.QLabel(loginwindow)
        self.username.setGeometry(QtCore.QRect(150, 160, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.username.setFont(font)
        self.username.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLabel(loginwindow)
        self.password.setGeometry(QtCore.QRect(160, 230, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.login = QtWidgets.QPushButton(loginwindow)
        self.login.setGeometry(QtCore.QRect(350, 310, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        font.setItalic(False)
        self.login.setFont(font)
        self.login.setObjectName("login")
        self.reset = QtWidgets.QPushButton(loginwindow)
        self.reset.setGeometry(QtCore.QRect(470, 310, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        font.setItalic(False)
        self.reset.setFont(font)
        self.reset.setObjectName("reset")
        self.user = QtWidgets.QLineEdit(loginwindow)
        self.user.setGeometry(QtCore.QRect(380, 150, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.user.setFont(font)
        self.user.setObjectName("user")
        self.pass_input = QtWidgets.QLineEdit(loginwindow)
        self.pass_input.setGeometry(QtCore.QRect(380, 220, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.pass_input.setFont(font)
        self.pass_input.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_input.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.pass_input.setObjectName("pass_input")
        self.title_2 = QtWidgets.QLabel(loginwindow)
        self.title_2.setGeometry(QtCore.QRect(320, 20, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.title_2.setFont(font)
        self.title_2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.title_2.setObjectName("title_2")

        self.retranslateUi(loginwindow)
        QtCore.QMetaObject.connectSlotsByName(loginwindow)

    def retranslateUi(self, loginwindow):
        _translate = QtCore.QCoreApplication.translate
        loginwindow.setWindowTitle(_translate("loginwindow", "Dialog"))
        self.title.setText(_translate("loginwindow", " LOGIN"))
        self.username.setText(_translate("loginwindow", "EMAIL ADDRESS"))
        self.password.setText(_translate("loginwindow", "PASSWORD"))
        self.login.setText(_translate("loginwindow", "OK"))
        self.reset.setText(_translate("loginwindow", "RESET"))
        self.user.setPlaceholderText(_translate("loginwindow", "enter mail address"))
        self.pass_input.setPlaceholderText(_translate("loginwindow", "********"))
        self.title_2.setText(_translate("loginwindow", "MAIL MANAGER"))

