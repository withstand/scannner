# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hsdelivery.ui'
#
# Created: Sat Apr  8 03:42:38 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(727, 499)
        self.radioButton = QtGui.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(40, 420, 118, 26))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtGui.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(170, 420, 118, 26))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtGui.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(300, 420, 118, 26))
        self.radioButton_3.setObjectName("radioButton_3")
        self.listView = QtGui.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(30, 50, 221, 341))
        self.listView.setObjectName("listView")
        self.spinBox = QtGui.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(40, 450, 64, 33))
        self.spinBox.setObjectName("spinBox")
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 450, 113, 33))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 450, 113, 33))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.commandLinkButton = QtGui.QCommandLinkButton(Form)
        self.commandLinkButton.setGeometry(QtCore.QRect(491, 450, 91, 31))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(370, 450, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 311, 21))
        self.label.setObjectName("label")
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(270, 40, 431, 331))
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("Form", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("Form", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("Form", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLinkButton.setText(QtGui.QApplication.translate("Form", "CommandLinkButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Data Plot", None, QtGui.QApplication.UnicodeUTF8))

class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

import sys
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())
