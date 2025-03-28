import gpiozero
import guizero
import time
import TCPClient

MAROON_RGB = "#B03060"
GOLD_RGB = "#FFD700"
SERVER_ADDRESS = ("192.168.0.30", 9000)
SERVER_PORT = 9000
LED_GPIO = 4
BUTTON_GPIO = 3


class BuzzerPlayer():
        def __init__(self, playerNumber, serverIP):
            self.count = 0
            self.playerNumber = playerNumber
            self.serverIP = serverIP
            #button pullup enabled by default, pass kwarg pull_up=false to set pulldown
            self.btn = gpiozero.Button(BUTTON_GPIO)
            self.led = gpiozero.LED(LED_GPIO)
            self.btn.when_pressed = self.check_buzz
            self.app = guizero.App(title="Player " + str(playerNumber), width = 600, height = 300, bg=MAROON_RGB)
            self.app.when_closed = self.cleanup
            self.app.set_full_screen()
            if playerNumber == 0:
                fontSize = 100
            else:
                fontSize = 200
            self.name = guizero.Text(self.app, text="Player " + str(playerNumber), size=200, font="Calibri", color="white", width = "fill", height = "fill")
            self.TCPSocket = TCPClient.TCPClient(serverIP, SERVER_PORT, receive_callback=self.handle_server_response)
            self.TCPSocket.start()
            self.TCPSocket.send("IDENTITY:Player " + str(playerNumber))
            self.app.display()
        def pressed(self):
            if self.count % 2:
                self.app.cancel(self.flash_color)
                self.app.bg = MAROON_RGB
            else:
                self.app.repeat(500, self.flash_color)
            self.count = self.count + 1
        def flash_color(self):
            if self.app.bg == MAROON_RGB:
                self.app.bg = GOLD_RGB
            else:
                self.app.bg = MAROON_RGB
        def cleanup(self):
            if self.count % 2:
                self.app.cancel(self.flash_color)
            self.TCPSocket.stop()
            self.TCPSocket.join()
            time.sleep(0.5)
            self.app.destroy()
        def update_name(self, newName):
            newName = newName.replace("  ", "\n")
            self.name.value = newName
        def buzz(self):
            self.app.repeat(500, self.flash_color)
            self.led.on()
        def clear(self):
            self.app.cancel(self.flash_color)
            self.app.bg = MAROON_RGB
            self.led.off()
        def check_buzz(self):
            self.TCPSocket.send("BUZZ:" + str(self.playerNumber))
        def handle_server_response(self, response):
            responses = response.split(":")
            if responses[0] == "BUZZ":
                self.buzz()
            elif responses[0] == "CLEAR":
                self.clear()
            elif responses[0] == "UPDATE NAME":
                self.update_name(responses[1])

playerNumber = int(input("Please input player number:"))
serverIP = input("Please input server IP address:")
Player = BuzzerPlayer(playerNumber, serverIP)

