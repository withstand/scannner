import socket

def change_net(net='eth0'):
    import os
    if net == 'eth0':
        os.system('sudo ifdown wlan0 -v | sudo ifup eth0 -v')
    else:
        os.system('sudo ifdown eth0 -v | sudo ifup wlan0 -v')

def send(data, port=7000, addr='192.255.255.255'):
    """ send(data[, port[, addr]]) - multicast a UDP datagram."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('',0))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)    
    s.sendto(data, (addr, port))

def recv(port=7001, addr='localhost'):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((addr, port))

    i = 0
    while True:
        data, addr = sock.recvfrom(1024)
        print(i, addr, data)
        i = i + 1

if __name__ == "__main__":
    import threading
    t = threading.Thread(target=recv)
    t.start()
    # from multiprocessing.dummy import Pool
    import time
    # p = Pool(1)
    # p.map(recv,())
    time.sleep(1)

    
    send('psi9000'.encode('ASCII'))

    
    t.join(timeout=1)
    print('done')
