import gpiozero
import guizero
import time
import TCPClient

MAROON_RGB = "#B03060"
GOLD_RGB = "#FFD700"
SERVER_ADDRESS = ("192.168.0.30", 9000)


class BuzzerTeamScore():
        def __init__(self, teamNumber):
            self.teamNumber = teamNumber
            self.scoreValue = 0
            self.app = guizero.App(title="Player", width = 600, height = 300, bg=MAROON_RGB, layout="vertical")
            self.app.when_closed = self.cleanup
            self.app.set_full_screen()
            self.name = guizero.Text(self.app, text="Team " + str(teamNumber), size=200, font="Calibri", color="white", width = "fill", height = "fill")
            self.score = guizero.Text(self.app, text=self.scoreValue, size=200, font="Calibri", color="white", width = "fill", height = "fill")
            self.TCPSocket = TCPClient.TCPClient(SERVER_ADDRESS[0], SERVER_ADDRESS[1], self.handle_server_response)
            self.TCPSocket.start()
            self.TCPSocket.send("IDENTITY:Team " + str(teamNumber))
            self.app.display()
        def cleanup(self):
            self.TCPSocket.stop()
            self.TCPSocket.join()
            time.sleep(0.5)
            self.app.destroy()
        def update_score(self, valueToAdd):
            self.scoreValue = self.scoreValue + valueToAdd
            self.score.value = self.scoreValue
        def update_name(self, newName):
            newName = newName.replace("  ", "\n")
            self.name.value = newName
        def handle_server_response(self, response):
            responses = response.split(":")
            if responses[0] == "UPDATE NAME":
                self.update_name(responses[1])
            elif responses[0] == "UPDATE SCORE":
                self.update_score(int(responses[1]))

teamNumber = int(input("Please enter team number:"))
Score = BuzzerTeamScore(teamNumber)

