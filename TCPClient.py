import socket
import threading
import select
from collections import deque
import time
import selectors
import types

class TCPClient(threading.Thread):
    #needs a function that is called when data is available to receive, and the port number to bind the socket to.
    #receive callback should take two arguments, message (str) and address (tuple)
    def __init__(self, server_ip, port, receive_callback = None, timeout = 5):
        super(TCPClient, self).__init__()
        
        self.sel = selectors.DefaultSelector()
        self.receive_callback = receive_callback
        #initialize the socket.
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((server_ip, port))
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(transmitBuffer=b"", receiveBuffer=b"")
        
        self.sel.register(self.socket, events, data=data)
        
        self.active = True
        self.sendBuffer = deque()

        self.timeout = timeout
    def service_connection(self, key, mask):
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)  # Should be ready to read
            if recv_data:
                data.receiveBuffer += recv_data
                if self.receive_callback:
                    self.receive_callback(str(data.receiveBuffer, "UTF-8"))
                data.receiveBuffer = b''
            else:
                self.sel.unregister(sock)
                sock.close()
        if mask & selectors.EVENT_WRITE:
            if self.sendBuffer:
                data.transmitBuffer = self.sendBuffer.popleft()
                sent = sock.sendall(data.transmitBuffer)  # Should be ready to write
                #print(data.transmitBuffer)
                data.transmitBuffer = ""
    def send(self, message):
        self.sendBuffer.append(bytes(message, encoding="UTF-8"))
            
     #must be overridden when inheriting form threading.Thread
    def run(self):
        print("Starting TCP Socket")
        self.active = True
        while(self.active):
            events = self.sel.select(timeout=0)
            for key, mask in events:
                self.service_connection(key, mask)
            time.sleep(0.001)
        self.socket.close()
        self.sel.close()
    #stops thread execution by modifying state variable
    def stop(self):
        self.active = False
        print("Stopping TCP Socket")

    def running(self):
        return self.active