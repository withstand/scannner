# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqtgraphdraw.ui'
#
# Created: Mon Apr 17 14:36:19 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 471, 471))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import PlotWidget
import sys
from scanner import pyqtScannerConnect

if __name__ == "__main__":
    app =  QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    
    ui.graphicsView.plot([1,2,3],[4,3,5])

    window.show()

    dia = QtGui.QDialog()
    connect = pyqtScannerConnect.Ui_Dialog()
    connect.setupUi(dia)
    dia.show()
    
    sys.exit(app.exec_())


    
