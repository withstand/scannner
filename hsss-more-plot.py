# embedding_in_qt4.py --- Simple Qt4 application embedding matplotlib canvases
#
# Copyright (C) 2005 Florent Rougon
#               2006 Darren Dale
#
# This file is an example program for matplotlib. It may be used and
# modified with no restriction; raw copies as well as modified versions
# may be distributed without limitation.

from __future__ import unicode_literals
import sys
import os
import random
from matplotlib.backends import qt_compat
use_pyside = qt_compat.QT_API == qt_compat.QT_API_PYSIDE
if use_pyside:
    from PySide import QtGui, QtCore
else:
    from PyQt4 import QtGui, QtCore

from numpy import arange, sin, pi
# from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler

from socket import socket, SHUT_RDWR
import numpy as np
import struct
import time
from retrying import retry

from more_plot import PlotDialog

progname = os.path.basename(sys.argv[0])
progversion = "0.1"

class Scanner():    
    def __init__(self,addr='192.168.31.177',port=9000):
        self.cs = socket()
        self.addr = addr
        self.port = port
        self.connect()
        pass

    @retry(wait_fixed=2000, stop_max_delay=10000)
    def connect(self):
        print('Rety to connect')
        self.cs.connect((self.addr, self.port))
        
    def offset(self):
        self.cs.send(bytes('hFFFF','ASCII'))
        r = self.cs.recv(4096)
        return r

    def __del__(self):
        self.cs.shutdown(SHUT_RDWR)
        self.cs.close() 

    
@retry(wait_fixed=2000, stop_max_delay=10000)
def connect_scanner(addr='192.168.31.177',port=9000):
    print(time.strftime('%H:%M:%S'), ' Try connect to ', addr, ':', port, sep='')
    cs = socket()
    # cs.settimeout(1.0)
    cs.connect((addr, port))
    cs.send(bytes('hFFFF','ASCII'))
    r = cs.recv(4096)
    return cs

def get_highspeed_val(cs):
    t = time.time()
    cs.send('b'.encode('ascii'))
    r = cs.recv(4096)            
    p = np.array(struct.unpack('>'+'f'*16, r))*6895
    return p, t

def close_connection(cs):
    cs.shutdown(SHUT_RDWR)
    cs.close()    

##class MyMplCanvas(FigureCanvas):
##    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
##
##    def __init__(self, parent=None, width=5, height=4, dpi=100):
##        fig = Figure(figsize=(width, height), dpi=dpi)
##
##        FigureCanvas.__init__(self, fig)
##
##        self.compute_initial_figure()
##
##        self.setParent(parent)
##
##        FigureCanvas.setSizePolicy(self,
##                                   QtGui.QSizePolicy.Expanding,
##                                   QtGui.QSizePolicy.Expanding)
##        FigureCanvas.updateGeometry(self)
##
##    def compute_initial_figure(self):
##        pass

##class ScannerCanvas(MyMplCanvas):
##
##    """A canvas that updates itself every
##     second with a new plot."""

##    def __init__(self, scanner=None, *args, **kwargs):

##        self.cs = scanner
##        MyMplCanvas.__init__(self, *args, **kwargs)

        
##    def set_scanner(cs):
##        self.cs = cs

    

     



##class ScannerApplicationWindow(QtGui.QMainWindow):
##    def __init__(self, scanner_connection):
##        QtGui.QMainWindow.__init__(self)
##        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
##        self.setWindowTitle("application main window")
##
##        self.file_menu = QtGui.QMenu('&File', self)
##        self.file_menu.addAction('&Quit', self.fileQuit,
##                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
##        self.menuBar().addMenu(self.file_menu)
##
##        self.help_menu = QtGui.QMenu('&Help', self)
##        self.menuBar().addSeparator()
##        self.menuBar().addMenu(self.help_menu)
##
##        self.help_menu.addAction('&About', self.about)
##
##        self.main_widget = QtGui.QWidget(self)
##
##        l = QtGui.QVBoxLayout(self.main_widget)
##        # sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
##        dc = ScannerCanvas(scanner_connection, parent=self.main_widget, width=5, height=4, dpi=100)
##        # l.addWidget(sc)
##        l.addWidget(dc)
##
##        self.main_widget.setFocus()
##        self.setCentralWidget(self.main_widget)
##
##        self.statusBar().showMessage("All hail matplotlib!", 2000)
##
##
##    def fileQuit(self):
##        print('fileQuit')
##        self.close()
##
##    def closeEvent(self, ce):
##        self.fileQuit()
##
##    def about(self):
##        QtGui.QMessageBox.about(self, "About",
##                                """embedding_in_qt4.py example
##Copyright 2005 Florent Rougon, 2006 Darren Dale
##
##This program is a simple example of a Qt4 application embedding matplotlib
##canvases.
##
##It may be used and modified with no restriction; raw copies as well as
##modified versions may be distributed without limitation."""
##                                )


def compute_initial_figure(cs, parent):

    plots = PlotDialog(parent)
    plots.showMaximized()
    
    datas = list()

    p, t = get_highspeed_val(cs)
    t0 = t

    for i in range(16):
        datas.append({'title': 'Port '+str(16-i),
             'xlabel': 't(s)',
             'ylabel': 'Pressure(Ps)',
             'x' : [0],
             'y' : [p[i]]})
    return plots, datas, t0


def update_figure(plots, datas, cs, t0):
    p, t = get_highspeed_val(cs)
    print(t - t0)

    for i in range(16):
        datas[i]['x'].append( (t-t0) )
        datas[i]['y'].append(p[i])

    plots.draw_plots(datas)

class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, socket):
        super(ControlMainWindow, self).__init__(None)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_f)
        timer.start(1000)        
        self.plots, self.datas, self.t0 = compute_initial_figure(socket, self)
        self.cs = socket
    def update_f(self):
        update_figure(self.plots, self.datas, self.cs, self.t0)

if __name__ == "__main__":
    cs = connect_scanner()
    
    qApp = QtGui.QApplication(sys.argv)
    try:       

        wd = ControlMainWindow(cs)
       
        sys.exit(qApp.exec_())
    finally:
        close_connection(cs)
