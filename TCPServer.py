import socket
import threading
import select
from collections import deque
import time
import selectors
import types

class TCPServer(threading.Thread):
    #needs a function that is called when data is available to receive, and the port number to bind the socket to.
    #receive callback should take two arguments, message (str) and address (tuple)
    def __init__(self, server_ip, port, receive_callback = None, timeout = 5):
        super(TCPServer, self).__init__()

        self.sel = selectors.DefaultSelector()
        self.receive_callback = receive_callback
        #initialize the socket.
        #self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lsock.bind((server_ip, port))
        self.lsock.listen()
        self.sel.register(self.lsock, selectors.EVENT_READ, data=None)
        #events = selectors.EVENT_READ | selectors.EVENT_WRITE
        #data = types.SimpleNamespace(transmitBuffer=b"", receiveBuffer=b"")

        #self.sel.register(self.socket, events, data=data)

        self.active = True
        self.sendBuffer = deque()

        self.connectionDict = {}

        self.timeout = timeout
    def accept_wrapper(self, socket):
        conn, addr = socket.accept()  # Should be ready to read
        print(type(addr))
        self.connectionDict[addr] = conn
        data = types.SimpleNamespace(addr=addr, receiveBuffer=b"", transmitBuffer=b"")
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.sel.register(conn, events, data=data)
    def service_connection(self, key, mask):
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)  # Should be ready to read
            if recv_data:
                data.receiveBuffer += recv_data
                if self.receive_callback:
                    self.receive_callback(str(data.receiveBuffer, "UTF-8"), data.addr)
                data.receiveBuffer = b""
            else:
                del(self.connectionDict[data.addr])
                self.sel.unregister(sock)
                sock.close()
                print("Closing Connection at: " + str(data.addr))
        if mask & selectors.EVENT_WRITE:
            if self.sendBuffer:
                if self.sendBuffer[0][1] == data.addr:
                    data.transmitBuffer = self.sendBuffer.popleft()[0]
                    sent = sock.send(data.transmitBuffer)  # Should be ready to write
                    data.transmitBuffer = ""
    def send(self, message, addr):
        self.sendBuffer.append((bytes(message, "UTF-8"), addr))

     #must be overridden when inheriting form threading.Thread
    def run(self):
        print("Starting TCP Socket")
        self.active = True
        while(self.active is True):
            events = self.sel.select(timeout=0)
            for key, mask in events:
                if key.data:
                    self.service_connection(key, mask)
                else:
                    self.accept_wrapper(key.fileobj)
            time.sleep(0.001)
        for key in self.connectionDict.keys():
            self.connectionDict[key].close()
        self.lsock.close()
        self.sel.close()
    #stops thread execution by modifying state variable
    def stop(self):
        self.active = False
        print("Stopping TCP Socket")

    def running(self):
        return self.active
