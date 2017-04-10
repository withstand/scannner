import math

from PySide import QtCore, QtGui

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backend_bases import key_press_handler

import multiprocessing

class MyFigure(Figure):
    def __init__(self, parent, *args, **kwargs):
##        QtCore.QThread.__init__(self, parent)
##        threading.Thread.__init__(self)
        Figure.__init__(self, *args, **kwargs)

        self.plot_data = list()
        self.figures = list()

    def start_plotting_thread(self, plot_data, on_finish=None):
        """ Start plotting """
        self.plot_data = plot_data
        if len(self.figures) == 0:
            self.setup_subplot()       


        if on_finish is not None:
            self.finished = on_finish

        job_for_another_core = multiprocessing.Process(target=self.run,args=())
        job_for_another_core.start()
##        self.start()

    def setup_subplot(self):
        """ Run as a thread """
        # Figure out rows and columns
        total_plots = len(self.plot_data)

        columns = int(math.sqrt(total_plots))
        if columns < 1:
            columns = 1

        rows = int(total_plots / columns)
        if (total_plots % columns) > 0:
            rows += 1
        if rows < 1:
            rows = 1

        # Plot Data
        for plot_index, _plot_data in enumerate(self.plot_data):
            plot_number = plot_index + 1
            args = (rows, columns, plot_number)
            kwargs = {
                'title': _plot_data['title'],
                'xlabel': _plot_data['xlabel'],
                'ylabel': _plot_data['ylabel']
            }

            figure = self.add_subplot(*args, **kwargs)

            figure.plot(_plot_data['x'], _plot_data['y'], '.b')

            self.figures.append(figure)

        self.subplots_adjust(hspace=0.5, wspace=0.4)        

    def run(self):
        for i, pd in enumerate(self.plot_data):
            self.figures[i].plot(pd['x'], pd['y'], '.b')
        self.finished()



class PlotDialog(QtGui.QDialog):
    def __init__(self, parent):
        
        QtGui.QDialog.__init__(self, parent, QtCore.Qt.WindowMinMaxButtonsHint | QtCore.Qt.WindowCloseButtonHint)

        self.figure = MyFigure(self)
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.layout = QtGui.QGridLayout()
        self.setLayout(self.layout)

        layout = [
            [self.toolbar],
            [self.canvas],            
        ]

        for row_index, columns in enumerate(layout):
            if type(columns) is list:
                for column_index, widget in enumerate(columns):
                    if widget is not None:
                        self.layout.addWidget(widget, row_index, column_index)

        self.canvas.mpl_connect('key_press_event', lambda event:key_press_handler(event, self.canvas, self.toolbar))

    def draw_plots(self, plot_data):
        """ Plot Plots """
        self.figure.start_plotting_thread(plot_data, on_finish=self.finish_drawing_plots)

    def finish_drawing_plots(self):
        """ Finish drawing plots """
        self.canvas.draw()
        self.show()

import sys
if __name__ == "__main__":
    qApp = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    p = PlotDialog(w)
    p.draw_plots([{'title': 'Port 0',
                             'xlabel': 't(s)',
                             'ylabel': 'Pressure(Pa)',
                             'x' : [1,2],
                             'y' : [1,2]},
                  {'title': 'Port 1',
                             'xlabel': 't(s)',
                             'ylabel': 'Pressure(Pa)',
                             'x' : [1,2],
                             'y' : [1,2]},
                 {'title': 'Port 2',
                             'xlabel': 't(s)',
                             'ylabel': 'Pressure(Pa)',
                             'x' : [1,2],
                             'y' : [1,2]},
                  {'title': 'Port 3',
                             'xlabel': 't(s)',
                             'ylabel': 'Pressure(Pa)',
                             'x' : [1,2],
                             'y' : [1,2]},
                 {'title': 'Port 0',
                             'xlabel': 't(s)',
                             'ylabel': 'Pressure(Pa)',
                             'x' : [1,2],
                             'y' : [1,2]},
                  ])
    w.setWindowTitle('Scanner...')
    sys.exit(qApp.exec_())

    
