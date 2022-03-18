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
    def __init__(self, server_ip, receive_callback = None, timeout = 5):
        super(TCPClient, self).__init__()
        
        self.sel = selectors.DefaultSelector()
        self.receive_callback = receive_callback
        #initialize the socket.
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_ip)
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
            if str(data.receiveBuffer).find("#")
                if self.receive_callback:
                    self.receive_callback(str(data.receiveBuffer))
                data.receiveBuffer = b""
        else:
            sel.unregister(sock)
            sock.close()
     if mask & selectors.EVENT_WRITE:
        if not data.transmitBuffer:
            if self.sendBuffer:
                data.transmitBuffer = self.sendBuffer.popleft()
        else:
            sent = sock.send(data.outb)  # Should be ready to write
            data.transmitBuffer = data.transmitBuffer[sent:]
        
     #must be overridden when inheriting form threading.Thread
    def run(self):
        print("Starting TCP Socket")
        self.active = True
        while(self.active):
            events = sel.select(timeout=None)
            for key, mask in events:
                self.service_connection(key, mask)
            time.sleep(0.001)
        sel.close()
    #stops thread execution by modifying state variable
    def stop(self):
        self.active = False
        print("Stopping TCP Socket")

    def running(self):
        return self.active