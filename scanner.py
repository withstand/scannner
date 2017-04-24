from socket import socket, SHUT_RDWR
from numpy import array, ndarray
import struct
import time
from retrying import retry

tdhs = lambda val: hex(val).lstrip('0x').zfill(2)

class Scanner():    
    def __init__(self,addr='192.168.31.177',port=9000):
        self.cs = socket()
        self.addr = addr
        self.port = port
        self.connect()
        self.t0 = time.time()
        self.hds = dict()
            
    def __del__(self):
        self.cs.shutdown(SHUT_RDWR)
        self.cs.close()
        
    @retry(wait_fixed=2000, stop_max_delay=40000)
    def connect(self):
        print('Connecting to ', self.addr, self.port)
        self.cs.connect((self.addr, self.port))
        
    def cal_set_offset(self):
        self.t0 = time.time()
        self.cs.send('hFFFF'.encode('ascii'))
        r = self.cs.recv(4096)
        return r
    
    def power_up_clear(self):
        self.cs.send('A'.encode('ascii'))
        return self.cs.recv(4096)

    def reset(self):
        self.cs.send('B'.encode('ascii'))
        return self.cs.recv(4096)

    def read_voltages(self):
        t = time.time()
        self.cs.send('VFFFF7'.encode('ascii'))
        r = self.cs.recv(4096)            
        p = array(struct.unpack('>'+'f'*16, r))*6895
        return p[-1::-1], t - self.t0
    
    def read_highspeed_data(self):
        t = time.time()
        self.cs.send('b'.encode('ascii'))
        r = self.cs.recv(4096)            
        p = array(struct.unpack('>'+'f'*16, r))*6895
        return p[-1::-1], t - self.t0

    def read_highprecision_data(self):
        t = time.time()
        self.cs.send('rFFFF7'.encode('ascii'))
        r = self.cs.recv(4096)            
        p = array(struct.unpack('>'+'f'*16, r))*6895
        return p[-1::-1], t - self.t0

    def read_transducer_temperature(self):
        t = time.time()
        self.cs.send('tFFFF7'.encode('ascii'))
        r = self.cs.recv(4096)            
        T = array(struct.unpack('>'+'f'*16, r))
        return T[-1::-1], t - self.t0

    def set_AD_samples_to_average(self, val):
        """ valid values are 4, 8(default), 16, 32, 64"""
        # valid = {4:'04', 8:'08', 16:'10', 32:'20', 64:'40'}
        # assert(valid.get(val)!=None)
        self.cs.send(('w10'+ tdhs(val)).encode('ascii'))
        return self.cs.recv(4096)

    def get_host_delivery_stream(self, id, period, number):
        # clear stream first
        self.cs.send(('c 03 ' + str(id)).encode('ascii'))
        self.cs.recv(4096)
        # set parameters
        cmd = 'c 00 ' + str(id) + ' FFFF 1 ' + str(period) + ' 7 ' + str(number)
        self.cs.send(cmd.encode('ascii'))
        self.hds[id] = {'per':period, 'num':number}
        r = self.cs.recv(4096)
        # return self

    # def get_host_delivery_stream(self, id):
        t = time.time()
        self.cs.send(('c 01 ' + str(id)).encode('ascii'))
        # recv data all in one buffer... can be change later
        data_size = 1+(5+16*4)*self.hds[id]['num']

        self.hds[id]['ts']= time.time() - self.t0
        data = b''
        while len(data) < data_size:        
            data += self.cs.recv(4096)
        self.hds[id]['te'] = time.time() - self.t0
        self.current_hds_data = data
        p_raw = struct.unpack('>c'+('bI'+'f'*16)*self.hds[id]['num'], data)
        self.current_p_raw = p_raw
        p = ndarray((self.hds[id]['num'], 16))
        for i in range(16):
            port_num = 16 - i
            pi = p_raw[3+i::18]
            p[:,port_num-1] = pi

        return p*6895, t - self.t0


# import matplotlib.pyplot as plt
from scipy.fftpack import rfft, fftshift
import numpy as np
import pyqtgraph as pg
import sys

##def sp(s, freq, dt,port):
##    pp,t = s.get_host_delivery_stream(1, int(1000/freq), int(dt*freq))
##    f = plt.figure()
##    N = len(pp[:,port])
##    f.add_subplot(2, 1, 1).plot(array(range(N))/freq, pp[:,port])
##    pfft = np.abs(rfft(pp[:,port]-pp[:,port].mean()))
##    f.add_subplot(2, 1, 2).plot(array(range(N)), pfft)
##    plt.show()

def update_port_show(s):

    win = pg.GraphicsWindow(title="Scanner Results")
    win.resize(1000,600)
    win.setWindowTitle('Scaner port 1 to port 16')
    # Enable antialiasing for prettier plots
    pg.setConfigOptions(antialias=True)
    
    fig = list()
    test_row = lambda i : i!=0 and i%4==0
    for i in range(16):
        if test_row(i):
            win.nextRow()
        f = win.addPlot(x=array(range(N))*period,y=p1[:,i],title='Port '+str(i+1))

   

     
if __name__ == '__main__':

    s = Scanner()
    s.cal_set_offset()

    period = 4    
    N = 1000
    
    p1,t = s.get_host_delivery_stream(1, period, N)

    win = pg.GraphicsWindow(title="Scanner Results")
    win.resize(1000,600)
    win.setWindowTitle('Scaner port 1 to port 16')
    # Enable antialiasing for prettier plots
    pg.setConfigOptions(antialias=True)
    
    fig = list()
    test_row = lambda i : i!=0 and i%4==0
    for i in range(16):
        if test_row(i):
            win.nextRow()
        f = win.addPlot(x=array(range(N))*period,y=p1[:,i],title='Port '+str(i+1))


    sys.exit(pg.QtGui.QApplication.instance().exec_())
##    p2,t = s.get_host_delivery_stream(1, 2, 1000)
##    p3,t = s.get_host_delivery_stream(1, 4, 1000)
##    p4,t = s.get_host_delivery_stream(1, 10, 1000)
##    
##
##    p = [p1,p2,p3,p4]
##    for i in range(4):
##        f = plt.figure()
##        f.add_subplot(2, 1, 1).plot(p[i][:,0])
##        pfft = np.abs(fftshift(rfft(p[i][:,0]-p[i][:,0].mean())))
##        f.add_subplot(2, 1, 2).plot(pfft)    
##        
##   
##    plt.show()
    
