from socket import socket, SHUT_RDWR
import numpy as np
import struct
import time

def expand_array_dim1(arr):
    arr.resize((arr.shape[0]+1,arr.shape[1]))
    return arr

cs = socket()
cs.connect(('192.168.31.177',9000))
## cs.send(bytes('hFFFF','ASCII'))
## r = cs.recv(4096)
p = np.zeros((1000,16))
t = np.zeros((1000,1))
try:
    t0 = time.time()
    for i in range(1000):
        t[i] = time.time()-t0
        cs.send('b'.encode('ASCII'))
        r = cs.recv(4096)
        p[i] = np.array(struct.unpack('>'+'f'*16, r))*6895
        time.sleep(1e-3)
finally:
    cs.shutdown(SHUT_RDWR)
    cs.close()


print(t)
