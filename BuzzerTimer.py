import gpiozero
import guizero
import time

import TCPClient

MAROON_RGB = "#B03060"
GOLD_RGB = "#FFD700"

SERVER_ADDRESS = ("192.168.0.30", 9000)


class BuzzerTimer():
        def __init__(self):
            self.count = 600
            timerValue = time.strftime("%M:%S", time.gmtime(self.count))
            self.app = guizero.App(title="Player", width = 600, height = 300, bg=MAROON_RGB)
            self.app.when_closed = self.cleanup
            self.app.set_full_screen()
            self.name = guizero.Text(self.app, text=timerValue, size=200, font="Calibri", color="white", width = "fill", height = "fill")
            self.TCPSocket = TCPClient.TCPClient(SERVER_ADDRESS[0], SERVER_ADDRESS[1], self.handle_server_response)
            self.TCPSocket.start()
            self.TCPSocket.send("IDENTITY:Timer")
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
            responses = response.split(":")
            if responses[0] == "START":
                self.start_timer()
            elif responses[0] == "PAUSE":
                self.pause_timer()
            elif responses[0] == "SET TIME"
                self.set_timer_value(int(responses[1]))
            elif responses[0] == "ADD TIME":
                self.add_time(int(responses[1]))
Timer = BuzzerTimer()
