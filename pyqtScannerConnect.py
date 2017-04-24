# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqtScannerConnect.ui'
#
# Created: Mon Apr 17 15:25:02 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(306, 184)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 140, 271, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit_IP = QtGui.QLineEdit(Dialog)
        self.lineEdit_IP.setGeometry(QtCore.QRect(80, 30, 201, 33))
        self.lineEdit_IP.setObjectName("lineEdit_IP")
        self.lineEdit_port = QtGui.QLineEdit(Dialog)
        self.lineEdit_port.setGeometry(QtCore.QRect(80, 70, 201, 33))
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 40, 31, 21))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 31, 21))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QObject.connect(self.lineEdit_IP, QtCore.SIGNAL("returnPressed()"), self.lineEdit_port.setFocus)
        QtCore.QObject.connect(self.lineEdit_port, QtCore.SIGNAL("returnPressed()"), self.lineEdit_IP.setFocus)
        # QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "IP", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "port", None, QtGui.QApplication.UnicodeUTF8))

