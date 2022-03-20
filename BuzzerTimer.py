import gpiozero
import guizero
import time

import TCPClient

MAROON_RGB = "#B03060"
GOLD_RGB = "#FFD700"


class BuzzerTimer():
        def __init__(self):
            self.count = 600
            timerValue = time.strftime("%M:%S", time.gmtime(self.count))
            self.app = guizero.App(title="Player", width = 600, height = 300, bg=MAROON_RGB)
            self.app.when_closed = self.cleanup
            self.app.set_full_screen()
            self.name = guizero.Text(self.app, text=timerValue, size=200, font="Calibri", color="white", width = "fill", height = "fill")
            self.TCPSocket = TCPClient.TCPClient("127.0.0.1", 9000)
            self.TCPSocket.start()
            self.TCPSocket.send("Timer")
            self.app.display()
        def start_timer(self):
            self.app.repeat(1000, self.countdown)
        def pause_timer(self):
            self.app.cancel(self.countdown)
        def set_timer_value(self, newValue):
            self.count = newValue
            timerValue = time.strftime("%M:%S", time.gmtime(self.count))
            self.name.value = timerValue
        def add_time(self, timeToAdd):
            self.count = self.count + timeToAdd
            timerValue = time.strftime("%M:%S", time.gmtime(self.count))
            self.name.value = timerValue
        def countdown(self):
            if self.count > 0:
                self.count = self.count - 1
            timerValue = time.strftime("%M:%S", time.gmtime(self.count))
            self.name.value = timerValue
        def cleanup(self):
            self.app.cancel(self.countdown)
            self.TCPSocket.stop()
            self.TCPSocket.join()
            time.sleep(0.5)
            self.app.destroy()
        def handle_server_response(self, response):
            pass
            
Timer = BuzzerTimer()