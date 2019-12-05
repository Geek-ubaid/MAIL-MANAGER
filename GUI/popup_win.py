# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popup_win.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_popup(object):
    def setupUi(self, popup):
        popup.setObjectName("popup")
        popup.resize(681, 298)
        self.gridLayout_2 = QtWidgets.QGridLayout(popup)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.popup_view = QtWidgets.QTableView(popup)
        self.popup_view.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.popup_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.popup_view.setObjectName("popup_view")
        self.popup_view.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.popup_view, 1, 0, 1, 1)
        self.goback = QtWidgets.QCommandLinkButton(popup)
        self.goback.setObjectName("goback")
        self.gridLayout_2.addWidget(self.goback, 0, 0, 1, 1)

        self.retranslateUi(popup)
        QtCore.QMetaObject.connectSlotsByName(popup)

    def retranslateUi(self, popup):
        _translate = QtCore.QCoreApplication.translate
        popup.setWindowTitle(_translate("popup", "Dialog"))
        self.goback.setText(_translate("popup", "Go Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    popup = QtWidgets.QDialog()
    ui = Ui_popup()
    ui.setupUi(popup)
    popup.show()
    sys.exit(app.exec_())

