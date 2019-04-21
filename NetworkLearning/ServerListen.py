# -*- coding: UTF-8 -*-

import socket
import threading

#初始化一个socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#将socket绑定到('127.0.0.1', 8888)
s.bind(('127.0.0.1', 8888))

s.listen(5)

def handle_tcp(sock, addr):
    print("new connection from %s:%s" % addr)
    sock.send(b'Welcome!')

    while True:
        #1024代表每次最大接受的字节数
        data = sock.recv(1024)
        if not data:
            break
        sock.send(b'Hello, %s!' % data)
    sock.close()

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=handle_tcp, args=(sock, addr))
    t.start()


