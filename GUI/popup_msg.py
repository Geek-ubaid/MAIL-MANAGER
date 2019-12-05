# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popup_msg.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_message_box(object):
    def setupUi(self, message_box):
        message_box.setObjectName("message_box")
        message_box.resize(655, 399)
        self.gridLayout = QtWidgets.QGridLayout(message_box)
        self.gridLayout.setObjectName("gridLayout")
        self.messagebox = QtWidgets.QTextBrowser(message_box)
        self.messagebox.setObjectName("messagebox")
        self.gridLayout.addWidget(self.messagebox, 1, 0, 1, 1)
        self.goback = QtWidgets.QCommandLinkButton(message_box)
        self.goback.setObjectName("goback")
        self.gridLayout.addWidget(self.goback, 0, 0, 1, 1)

        self.retranslateUi(message_box)
        QtCore.QMetaObject.connectSlotsByName(message_box)

    def retranslateUi(self, message_box):
        _translate = QtCore.QCoreApplication.translate
        message_box.setWindowTitle(_translate("message_box", "Dialog"))
        self.goback.setText(_translate("message_box", "Go Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    message_box = QtWidgets.QDialog()
    ui = Ui_message_box()
    ui.setupUi(message_box)
    message_box.show()
    sys.exit(app.exec_())

