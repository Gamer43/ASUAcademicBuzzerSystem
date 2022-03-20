import TCPServer
import time

class BuzzerHost():
    def __init__(self):
        self.server = TCPServer.TCPServer("0.0.0.0", 9000, receive_callback=self.echo)
        self.server.start()
    def echo(self, string, addr):
        self.server.send(string, addr)
    #print(str(string) + str(addr))

host = BuzzerHost()

try:
    while(True):
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    host.server.stop()
    host.server.join()
