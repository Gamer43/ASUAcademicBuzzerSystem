from guizero import *
from tkinter import colorchooser
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
import threading
import TCPServer


TEAM_SIZE = 4

class BuzzerHost():


    def __init__(self):
    # Initialize the window and app
        self.buzz = False
        self.app = App(title="Control Panel", width = 1100, height = 720)

        #export the sounds
        self.ding1 = AudioSegment.from_mp3("./ding.mp3")
        self.ding2 = AudioSegment.from_mp3("./ding2.mp3")
        self.endsound = AudioSegment.from_mp3("./endGameBuzzerSound.mp3")

        #****************************************************************
        # Need to create for loop that listens for Buzzes
        # If buzzer received, execute buzz event (play sound and change background of player that buzzed in first)
        # Do not execute any other buzz events until clear buzzer function has been executed


        self.gameSettingsWindow = Window(self.app, title = "Game Settings", width = 800, height = 550, layout = 'grid')

        self.gameSettingsBox1 = Box(self.gameSettingsWindow, align = 'top', width = 'fill', height = 'fill', grid = [0,0,5,1])
        self.settingsLabel = Text(self.gameSettingsBox1, text = 'Game Settings', align = 'bottom', size = 18)

        self.settingsBox = Box(self.gameSettingsWindow, width = 100, height = 20, align = 'left', grid = [0,1])

        self.gameSettingsBox2 = Box(self.gameSettingsWindow, align = 'left', layout = 'grid', width = 'fill', grid = [1,2])

        self.playerNameColorLabel = Text(self.gameSettingsBox2, text = 'Player Name Color:', grid = [0,0], align = 'right')
        self.playerNameColorPrev = Box(self.gameSettingsBox2, grid = [1,0], width = 15, height = 20)
        self.playerNameSpacer = Box(self.gameSettingsBox2, grid = [2,0], width = 10)
        self.playerNameColorButton = PushButton(self.gameSettingsBox2, text = 'Change', grid = [3,0], args = ["player", "text", self.playerNameColorPrev], command = self.changeTextColor)

        self.timerColorLabel = Text(self.gameSettingsBox2, text = 'Timer Color:', align = 'right', grid = [0,1])
        self.timerColorPrev = Box(self.gameSettingsBox2, grid = [1,1], width = 15, height = 20)
        self.timerColorSpacer = Box(self.gameSettingsBox2, grid = [2,1], width = 10)
        self.timerColorButton = PushButton(self.gameSettingsBox2, text = 'Change', grid = [3,1], args = ["timer", "text", self.timerColorPrev], command = self.changeTextColor)

        self.playerBackgroundColorLabel = Text(self.gameSettingsBox2, text = 'Player Background:', align = 'right', grid = [0,2])
        self.playerBackgroundColorPrev = Box(self.gameSettingsBox2, grid = [1,2], width = 15, height = 20)
        self.playerBackgroundSpacer = Box(self.gameSettingsBox2, grid = [2,2], width = 10)
        self.playerBackgroundColorButton = PushButton(self.gameSettingsBox2, text = 'Change', grid = [3,2], args = ["player", "background", self.playerBackgroundColorPrev], command = self.changeTextColor)

        self.timerBackgroundColorLabel = Text(self.gameSettingsBox2, text = 'Timer Background:', align = 'right', grid = [0,3])
        self.timerBackgroundColorPrev = Box(self.gameSettingsBox2, grid = [1,3], width = 15, height = 20)
        self.timerBackgroundSpacer = Box(self.gameSettingsBox2, grid = [2,3], width = 10)
        self.timerBackgroundColorButton = PushButton(self.gameSettingsBox2, text = 'Change', grid = [3,3], args = ["timer", "background", self.timerBackgroundColorPrev], command = self.changeTextColor)

        self.team1BackgroundColorLabel = Text(self.gameSettingsBox2, text = 'Team 1 Background:', align = 'right', grid = [0,4])
        self.team1BackgroundColorPrev = Box(self.gameSettingsBox2, grid = [1,4], width = 15, height = 20)
        self.team1BackgroundSpacer = Box(self.gameSettingsBox2, grid = [2,4], width = 10)
        self.team1BackgroundColorButton = PushButton(self.gameSettingsBox2, text = 'Change', grid = [3,4], args = ["team1", "background", self.team1BackgroundColorPrev], command = self.changeTextColor)

        self.team2BackgroundColorLable = Text(self.gameSettingsBox2, text = 'Team 2 Background:', align = 'right', grid = [0,5])
        self.team2BackgroundColorPrev = Box(self.gameSettingsBox2, grid = [1,5], width = 15, height = 20)
        self.team2BackgroundSpacer = Box(self.gameSettingsBox2, grid = [2,5], width = 10)
        self.team2BackgroundColorButton = PushButton(self.gameSettingsBox2, text = 'Change', grid = [3,5], args = ["team2", "background", self.team2BackgroundColorPrev], command = self.changeTextColor)

        self.team1ColorLabel = Text(self.gameSettingsBox2, text = 'Team 1 Color:', align = 'right', grid = [0,6])
        self.team1ColorPrev = Box(self.gameSettingsBox2, grid = [1,6], width = 15, height = 20)
        self.team1ColorSpacer = Box(self.gameSettingsBox2, grid = [2,6], width = 10)
        self.team1ColorButton = PushButton(self.gameSettingsBox2, text = 'Change', grid = [3,6], args = ["team1", "text", self.team1ColorPrev], command = self.changeTextColor)

        self.team2ColorLabel = Text(self.gameSettingsBox2, text = 'Team 2 Color:', align = 'right', grid = [0,7])
        self.team2ColorPrev = Box(self.gameSettingsBox2, grid = [1,7], width = 15, height = 20)
        self.team2ColorSpacer = Box(self.gameSettingsBox2, grid = [2,7], width = 10)
        self.team2ColorButton = PushButton(self.gameSettingsBox2, text = 'Change', grid = [3,7], args = ["team2", "text", self.team2ColorPrev], command = self.changeTextColor)

        self.team1ScoreColorLabel = Text(self.gameSettingsBox2, text = 'Team 1 Score Color:', align = 'right', grid = [0,8])
        self.team1ScoreColorPrev = Box(self.gameSettingsBox2, grid = [1,8], width = 15, height = 20)
        self.team1ScoreColorSpacer = Box(self.gameSettingsBox2, grid = [2,8], width = 10)
        self.team1ScoreColorButton = PushButton(self.gameSettingsBox2, text = 'Change', grid = [3,8], args = ["team1score", "text", self.team1ScoreColorPrev], command = self.changeTextColor)

        self.team2ScoreColorLabel = Text(self.gameSettingsBox2, text = 'Team 2 Score Color:', align = 'right', grid = [0,9])
        self.team2ScoreColorPrev = Box(self.gameSettingsBox2, grid = [1,9], width = 15, height = 20)
        self.team2ScoreColorSpacer = Box(self.gameSettingsBox2, grid = [2,9], width = 10)
        self.team2ScoreColorButton = PushButton(self.gameSettingsBox2, text = 'Change', grid = [3,9], args = ["team2score", "text", self.team2ScoreColorPrev], command = self.changeTextColor)


        self.leftSpacer = Box(self.gameSettingsWindow, width = 50, align = 'left', grid = [2,2])



        self.rightSpacer = Box(self.gameSettingsWindow, width = 100, align = 'right', grid = [3,2])


        self.gameSettingsBox3 = Box(self.gameSettingsWindow, align = 'right', layout = 'grid', width = 'fill', grid = [3,2])

        self.teamNameLabel = Text(self.gameSettingsBox3, text = "Input College/Team Name", grid = [0,0,2,1], align = 'top')
        self.teamNameSpacer = Box(self.gameSettingsBox3, grid = [0,1], height = 10)
        self.shortTeamNameLabel = Text(self.gameSettingsBox3, text = 'College Name', grid = [0,2], align = 'right')
        self.shortTeamNameTextBox = TextBox(self.gameSettingsBox3, grid = [1,2], align = 'left', width = 20)

        self.teamNameSpacer = Box(self.gameSettingsBox3, grid = [0,3], height = 10)

        self.displayedTeamNameLabel = Text(self.gameSettingsBox3, text = 'Displayed College Name', grid = [0,4], align = 'right')
        self.displayedTeamNameTextBox = TextBox(self.gameSettingsBox3, grid = [1,4], align = 'left', width = 20)

        self.teamLogoSpacer = Box(self.gameSettingsBox3, grid = [0,5], height = 10)

        self.selectLogoLabel = Text(self.gameSettingsBox3, text = 'Select College Logo:', grid = [0,6], align = 'right')
        self.selectLogoButton = PushButton(self.gameSettingsBox3, text = 'Choose File', grid = [1,6], align = 'left', command = self.selectLogoFile)

        self.collegeListSpacer = Box(self.gameSettingsBox3, grid = [0,7], height = 10)

        self.collegeListBox = ListBox(self.gameSettingsBox3, items = [], grid = [0,10,2,1], height = 'fill')


        self.insertCollegeButton = PushButton(self.gameSettingsBox3, text = 'Insert College', grid = [0,11], align = 'bottom', command = self.insertCollege)
        self.removeCollegeButton = PushButton(self.gameSettingsBox3, text = 'Remove College', grid = [1,11], align = 'bottom', command = self.removeCollege)




        """
        playerFontLabel = Text(gameSettingsBox3, text = 'Player Font:', align = 'right', grid = [0,0])
        Box(gameSettingsBox3, width = 10, grid = [1,0])
        playerFontButton = PushButton(gameSettingsBox3, text = 'Change', grid = [2,0])

        teamNameFontLable = Text(gameSettingsBox3, text = 'Team Name Font:', align = 'right', grid = [0,1])
        Box(gameSettingsBox3, width = 10, grid = [1,1])
        teamNameFontButton = PushButton(gameSettingsBox3, text = 'Change', grid = [2,1])

        timerFontLabel = Text(gameSettingsBox3, text = 'Timer Font:', align = 'right', grid = [0,2])
        Box(gameSettingsBox3, width = 10, grid = [1,2])
        timerFontButton = PushButton(gameSettingsBox3, text = 'Change', grid = [2,2])

        scoreFontLabel = Text(gameSettingsBox3, text = 'Score Font:', align = 'right', grid = [0,3])
        Box(gameSettingsBox3, width = 10, grid = [1,3])
        scoreFontButton = PushButton(gameSettingsBox3, text = 'Change', grid = [2,3])
        """

        self.gameSettingsBox4 = Box(self.gameSettingsWindow, align = 'bottom', width = 'fill', height = 'fill', grid = [3,3])
        #Box(gameSettingsBox4, width = 100, align = 'right', grid = [5,3])
        self.applyButton = PushButton(self.gameSettingsBox4, text = 'Save and Exit', align = 'bottom', width = 'fill', height = 'fill', command = self.saveAndExit)


        self.menuBar = MenuBar(self.app, toplevel = ['Game Settings'], options = [
                                                                        [['Game Settings',self.gameSettingsFunction]]
                                                                        ])


        #Title Box
        self.titleBox = Box(self.app, align = 'top', width = 'fill', height = 50)
        self.titleLabel = Text(self.titleBox, text = 'Academic Bowl Control Panel', size = 18)

        # Moderator Box
        self.moderatorBox = Box(self.app, align = 'top', width = 'fill', layout = 'grid')

        # Moderator Label, Text Box and Font Buttons
        self.moderatorLabelBox = Box(self.moderatorBox, grid = [0,0], width = 10)
        self.moderatorLabel = Text(self.moderatorBox, text = 'Moderator Name: ', align = 'left', grid = [1,0])
        self.moderatorLabelSpacer = Box(self.moderatorBox, grid = [2,0], width = 10)
        self.moderatorTextBox = TextBox(self.moderatorBox, align = 'left', grid = [3,0], width = 20)
        self.moderatorSizeSpacer1 = Box(self.moderatorBox, grid = [4,0], width = 11)
        self.decreaseModButton = PushButton(self.moderatorBox, text = '-', align = 'left', grid = [5,0])
        self.moderatorSizeSpacer2 = Box(self.moderatorBox, grid = [6,0], width = 12)
        self.increaseModButton = PushButton(self.moderatorBox, text = '+', align = 'left', grid = [7,0])

        self.parentBox1 = Box(self.app, align = 'top', width = 'fill', height = 'fill')

        # Team 1 Title Box
        self.team1TitleBox = TitleBox(self.parentBox1, text = "Team 1", align = 'left', width = 'fill', height = 'fill')
        self.team1Box = Box(self.team1TitleBox, layout = 'grid')
        # Team 1 Team and player names with text boxes and font buttons
        self.team1Label = Text(self.team1Box, text = "Team Name: ", grid = [0,0], align = 'left', size = 12)
        #teamNameTextBox = TextBox(team1Box, grid = [1,0], align = 'left')
        self.team1NameCombo = Combo(self.team1Box, options = [], grid = [1,0], align = 'left')
        self.decreaseTeam1Button = PushButton(self.team1Box, text = '-', grid = [3,0], align = 'left')
        #padBox = Box(team1Box, width = 10, grid = [3,0], align = 'left')
        self.increaseTeam1Button = PushButton(self.team1Box, text = '+', grid = [4,0], align = 'left')

        self.team1Player1Label = Text(self.team1Box, text = 'Player 1', grid = [0,1], align = 'left', size = 12)
        self.p1t1TextBox = TextBox(self.team1Box, grid = [1,1], align = 'left', width = 'fill')
        self.decreaseP1T1Button = PushButton(self.team1Box, text = '-', grid = [3,1], align = 'left')
        #padBox = Box(team1Box, width = 2, grid = [3,1], align = 'left')
        self.increaseP1T1Button = PushButton(self.team1Box, text = '+', grid = [4,1], align = 'left')

        self.team1Player2Label = Text(self.team1Box, text = 'Player 2', grid = [0,2], align = 'left', size = 12)
        self.p2t1TextBox = TextBox(self.team1Box, grid = [1,2], align = 'left', width = 'fill')
        self.decreaseP2T1Button = PushButton(self.team1Box, text = '-', grid = [3,2], align = 'left')
        #padBox = Box(team1Box, width = 2, grid = [3,2], align = 'left')
        self.increaseP2T1Button = PushButton(self.team1Box, text = '+', grid = [4,2], align = 'left')

        self.team1Player3Label = Text(self.team1Box, text = 'Player 3', grid = [0,3], align = 'left', size = 12)
        self.p3t1TextBox = TextBox(self.team1Box, grid = [1,3], align = 'left', width = 'fill')
        self.decreaseP3T1Button = PushButton(self.team1Box, text = '-', grid = [3,3], align = 'left')
        #padBox = Box(team1Box, width = 2, grid = [3,3], align = 'left')
        self.increaseP3T1Button = PushButton(self.team1Box, text = '+', grid = [4,3], align = 'left')

        self.team1Player4Label = Text(self.team1Box, text = 'Player 4', grid = [0,4], align = 'left', size = 12)
        self.p4t1TextBox = TextBox(self.team1Box, grid = [1,4], align = 'left', width = 'fill')
        self.decreaseP4T1Button = PushButton(self.team1Box, text = '-', grid = [3,4], align = 'left')
        #padBox = Box(team1Box, width = 2, grid = [3,4], align = 'left')
        self.increaseP4T1Button = PushButton(self.team1Box, text = '+', grid = [4,4], align = 'left')

        self.team1ScoreChangeSpacer1 = Box(self.team1Box, height = 20, grid = [0,5])
        self.team1CorrectButton = PushButton(self.team1Box, text = 'Correct', grid = [0,6, 2,6], align = 'left', width = 10, args = [1], command = self.correctAnswer)
        self.team1ScoreChangeSpacer2 = Box(self.team1Box, height = 20, grid = [2,5])
        self.team1IncorrectButton = PushButton(self.team1Box, text = 'Incorrect', grid = [2,6,4,6], align = 'left', width = 10, args = [1], command = self.incorrectAnswer)

        # Title box to hold buttons for the main functions of the game
        self.gameButtonsTitleBox = TitleBox(self.parentBox1, text = 'Game Functions', align = 'left', width = 200, height = 'fill')

        self.buzzerCommandSpacer1 = Box(self.gameButtonsTitleBox, height = 50)
        self.updateButton = PushButton(self.gameButtonsTitleBox, text = 'Update', align = 'top', width = 20, command = self.updateAll)
        self.buzzerCommandSpacer2 = Box(self.gameButtonsTitleBox, height = 50)
        self.clearButton = PushButton(self.gameButtonsTitleBox, text = 'Clear Buzzer', align = 'top', width = 20, command = self.clear_manual)


        # Team 2 Team and player names with text boxes and font buttons
        self.team2TitleBox = TitleBox(self.parentBox1, text = "Team 2", align = 'left', width = "fill", height = 'fill')
        self.team2Box = Box(self.team2TitleBox, layout = 'grid')

        self.team2Label = Text(self.team2Box, text = "Team Name: ", grid = [0,0], align = 'left', size = 12)
        #teamNameTextBox = TextBox(team2TitleBox, grid = [1,0], align = 'left')
        self.team2NameCombo = Combo(self.team2Box, options = [], grid = [1,0], align = 'left')
        self.decreaseTeamNameButton = PushButton(self.team2Box, text = '-', grid = [3,0], align = 'left')
        self.increaseTeamNameButton = PushButton(self.team2Box, text = '+', grid = [4,0], align = 'left')

        self.team2Player1Label = Text(self.team2Box, text = 'Player 1', grid = [0,1], align = 'left', size = 12)
        self.p1t2TextBox = TextBox(self.team2Box, grid = [1,1], align = 'left', width = 'fill')
        self.decreaseP1Button = PushButton(self.team2Box, text = '-', grid = [3,1], align = 'left')
        self.increaseP1Button = PushButton(self.team2Box, text = '+', grid = [4,1], align = 'left')

        self.team2Player1Label = Text(self.team2Box, text = 'Player 2', grid = [0,2], align = 'left', size = 12)
        self.p2t2TextBox = TextBox(self.team2Box, grid = [1,2], align = 'left', width = 'fill')
        self.decreaseP1Button = PushButton(self.team2Box, text = '-', grid = [3,2], align = 'left')
        self.increaseP1Button = PushButton(self.team2Box, text = '+', grid = [4,2], align = 'left')

        self.team2Player1Label = Text(self.team2Box, text = 'Player 3', grid = [0,3], align = 'left', size = 12)
        self.p3t2TextBox = TextBox(self.team2Box, grid = [1,3], align = 'left', width = 'fill')
        self.decreaseP1Button = PushButton(self.team2Box, text = '-', grid = [3,3], align = 'left')
        self.increaseP1Button = PushButton(self.team2Box, text = '+', grid = [4,3], align = 'left')

        self.team2Player1Label = Text(self.team2Box, text = 'Player 4', grid = [0,4], align = 'left', size = 12)
        self.p4t2TextBox = TextBox(self.team2Box, grid = [1,4], align = 'left', width = 'fill')
        self.decreaseP1Button = PushButton(self.team2Box, text = '-', grid = [3,4], align = 'left')
        self.increaseP1Button = PushButton(self.team2Box, text = '+', grid = [4,4], align = 'left')

        self.team2ScoreChangeSpacer1 = Box(self.team2Box, height = 20, grid = [0,5])
        self.team2CorrectButton = PushButton(self.team2Box, text = 'Correct', grid = [0,6,2,6], align = 'left', width = 10, args = [2], command = self.correctAnswer)
        self.team2ScoreChangeSpacer1 = Box(self.team2Box, height = 20, grid = [2,5])
        self.team2IncorrectButton = PushButton(self.team2Box, text = 'Incorrect', grid = [2,6,4,6], align = 'left', width = 10, args = [2], command = self.incorrectAnswer)



        self.parentBox2 = Box(self.app, align = 'top', width = 'fill', height = 'fill')

        self.pointTitleBox = TitleBox(self.parentBox2, text = 'Points', align = 'left', width = 'fill', height = 'fill')
        self.correctLabel = Text(self.pointTitleBox, text = 'Correct (+ Point Value)', align = 'left', size = 12)
        self.addPointTextBox = TextBox(self.pointTitleBox, align = 'left')
        self.incorrectLabel = Text(self.pointTitleBox, text = 'Incorrect (- Point Value)', align = 'left', size = 12)
        self.subPointTextBox = TextBox(self.pointTitleBox, align = 'left')

        self.timerTitleBox = TitleBox(self.parentBox2, text = 'Timer', align = 'left', width = 'fill', height = 'fill')
        self.minutesLabel = Text(self.timerTitleBox, text = 'Minutes:', align = 'left', size = 12)
        self.minuteTextBox = TextBox(self.timerTitleBox, align = 'left')
        self.secondsLabel = Text(self.timerTitleBox, text = 'Seconds:', align = 'left', size = 12)
        self.secondTextBox = TextBox(self.timerTitleBox, align = 'left')

        self.parentBox3 = Box(self.app, align = 'top', width = 'fill', height = 'fill')
        self.mainButtonTitleBox = TitleBox(self.parentBox3, text = 'Main Functions', height = 'fill', width = 'fill')

        self.buttonBox = Box(self.mainButtonTitleBox, layout = 'grid', align = 'top')

        self.startGameButton = PushButton(self.buttonBox, text = 'Start Game', grid = [0,0], align = 'left', command = self.startGame)
        self.startGameSpacer = Box(self.buttonBox, grid = [1,0], width = 10)
        self.pauseGameButton = PushButton(self.buttonBox, text = 'Pause Game', grid = [2,0], align = 'left', command = self.pauseGame)
        self.pauseGameSpacer = Box(self.buttonBox, grid = [3,0], width = 10)
        self.resetButton = PushButton(self.buttonBox, text = 'Reset Game', grid = [4,0], align = 'left', command = self.resetFields)
        self.resetGameSpacer = Box(self.buttonBox, grid = [5,0], width = 10)
        self.endGameButton = PushButton(self.buttonBox, text = 'End Game', grid = [6,0], align = 'left', command = self.endGame)

        self.collegeDict = {
            "IRA Fulton Maroon": "Ira A. Fulton  Schools of Engineering  Maroon",
            "IRA Fulton Gold": "Ira A. Fulton  Schools of Engineering  Gold",
            "WP Carey Maroon": "W. P. Carey  School of Business  Maroon",
            "WP Carey Gold": "W. P. Carey  School of Business  Gold",
            #"Sustainability": "School of Sustainability",
            #"Health Solutions": "College of Health Solutions",
            #"Walter Cronkite" : "Walter Cronkite School of  Journalism and  Mass Communication",
            "CISA" : "College of  Integrative Sciences and Arts",
            #"Herberger" : "Herberger  Institute for Design and Arts",
            #"Watts College" : "Watts College of  Public Service and  Commmunity Solutions",
            "The College Maroon": "The College of  Liberal Arts and Sciences  Maroon",
            "The College Gold": "The College of  Liberal Arts and Sciences  Gold",
            "Global Futures": "College of Global Futures"
        }
        self.TCPServer = TCPServer.TCPServer("0.0.0.0", 9000, self.client_request_callback)
        self.TCPServer.start()

        self.addressDict = {}

        self.initGame()

        self.app.display()

    def clear_manual(self):
        self.app.cancel(self.buzz_timeout)
        self.clear()

    def clear(self):
        self.buzz = False
        for key in self.addressDict.keys():
            self.TCPServer.send("CLEAR", self.addressDict[key])


# Define all of the functions
    def gameSettingsFunction(self):
        self.gameSettingsWindow.show()

    def initGame(self):
        self.startGameButton.text_size = 16
        self.endGameButton.text_size = 16
        self.pauseGameButton.text_size = 16
        self.resetButton.text_size = 16
        self.updateButton.text_size = 16
        self.clearButton.text_size = 16
        self.team1CorrectButton.text_size = 12
        self.team1IncorrectButton.text_size = 12
        self.team2CorrectButton.text_size = 12
        self.team2IncorrectButton.text_size = 12

        self.minuteTextBox.value = 15
        self.secondTextBox.value = 0

        self.addPointTextBox.value = 10
        self.subPointTextBox.value = 5

        self.startGameButton.width = 10
        self.endGameButton.width = 10
        self.pauseGameButton.width = 10
        self.resetButton.width = 10

        self.playerNameColorPrev.bg = 'black'
        self.timerColorPrev.bg = 'black'
        self.playerBackgroundColorPrev.bg = 'white'
        self.timerBackgroundColorPrev.bg = 'white'
        self.team1BackgroundColorPrev.bg = 'white'
        self.team2BackgroundColorPrev.bg = 'white'
        self.team1ColorPrev.bg = 'black'
        self.team2ColorPrev.bg = 'black'
        self.team1ScoreColorPrev.bg = 'black'
        self.team2ScoreColorPrev.bg = 'black'

        self.team1CorrectButton.text_color = 'Green'
        self.team2CorrectButton.text_color = 'Green'
        self.team1IncorrectButton.text_color = 'Red'
        self.team2IncorrectButton.text_color = 'Red'
        self.gameSettingsWindow.hide()

        for key in self.collegeDict:
            self.collegeListBox.append(key)
            self.team1NameCombo.append(key)
            self.team2NameCombo.append(key)

        self.app.full_screen = True






    def resetFields(self):
        self.p1t1TextBox.value = ''
        self.p2t1TextBox.value = ''
        self.p3t1TextBox.value = ''
        self.p4t1TextBox.value = ''

        self.p1t2TextBox.value = ''
        self.p2t2TextBox.value = ''
        self.p3t2TextBox.value = ''
        self.p4t2TextBox.value = ''

        self.TCPServer.send("RESET SCORE", self.addressDict.get("Team 1"))
        self.TCPServer.send("RESET SCORE", self.addressDict.get("Team 2"))


        #self.addPointTextBox.value = ''
        #self.subPointTextBox.value = ''

        self.minuteTextBox.value = '15'
        self.secondTextBox.value = '0'

        self.timerMinuteText = self.minuteTextBox.value
        self.timerSecondText = self.secondTextBox.value
        totalTime = (int(self.timerMinuteText) * 60) + int(self.timerSecondText)
        self.TCPServer.send("SET TIME:" + str(totalTime), self.addressDict.get("Timer"))

        #self.moderatorTextBox.value = ''

    def updateAll(self):
        #Send all values (text values, fonts, colors) to the respective Pis via TCP

        self.player1team1Text = self.p1t1TextBox.value

        self.TCPServer.send("UPDATE NAME:" + self.player1team1Text, self.addressDict.get("Player 1"))

        self.player1team1Color = self.playerNameColorPrev.bg
        self.player1team1Background = self.playerBackgroundColorPrev.bg

        self.player2team1Text = self.p2t1TextBox.value

        self.TCPServer.send("UPDATE NAME:" + self.player2team1Text, self.addressDict.get("Player 2"))

        self.player2team1Color = self.playerNameColorPrev.bg
        self.player2team1Background = self.playerBackgroundColorPrev.bg

        self.player3team1Text = self.p3t1TextBox.value

        self.TCPServer.send("UPDATE NAME:" + self.player3team1Text, self.addressDict.get("Player 3"))

        self.player3team1Color = self.playerNameColorPrev.bg
        self.player3team1Background = self.playerBackgroundColorPrev.bg

        self.player4team1Text = self.p4t1TextBox.value

        self.TCPServer.send("UPDATE NAME:" + self.player4team1Text, self.addressDict.get("Player 4"))

        self.player4team1Color = self.playerNameColorPrev.bg
        self.player4team1Background = self.playerBackgroundColorPrev.bg

        self.player1team2Text = self.p1t2TextBox.value

        self.TCPServer.send("UPDATE NAME:" + self.player1team2Text, self.addressDict.get("Player 5"))

        self.player1team2Color = self.playerNameColorPrev.bg
        self.player1team2Background = self.playerBackgroundColorPrev.bg

        self.player2team2Text = self.p2t2TextBox.value

        self.TCPServer.send("UPDATE NAME:" + self.player2team2Text, self.addressDict.get("Player 6"))

        self.player2team2Color = self.playerNameColorPrev.bg
        self.player2team2Background = self.playerBackgroundColorPrev.bg

        self.player3team2Text = self.p3t2TextBox.value

        self.TCPServer.send("UPDATE NAME:" + self.player3team2Text, self.addressDict.get("Player 7"))

        self.player3team2Color = self.playerNameColorPrev.bg
        self.player3team2Background = self.playerBackgroundColorPrev.bg

        self.player4team2Text = self.p4t2TextBox.value

        self.TCPServer.send("UPDATE NAME:" + self.player4team2Text, self.addressDict.get("Player 8"))

        self.player4team2Color = self.playerNameColorPrev.bg
        self.player4team2Background = self.playerBackgroundColorPrev.bg

        self.moderatorText = self.moderatorTextBox.value

        self.TCPServer.send("UPDATE NAME:" + self.moderatorText, self.addressDict.get("Player 0"))

        self.moderatorColor = self.playerNameColorPrev.bg
        self.moderatorBackground = self.playerBackgroundColorPrev.bg

        self.timerMinuteText = self.minuteTextBox.value
        self.timerSecondText = self.secondTextBox.value
        self.timerColor = self.timerColorPrev.bg
        self.timerBackground = self.timerBackgroundColorPrev.bg

        totalTime = (int(self.timerMinuteText) * 60) + int(self.timerSecondText)

        self.TCPServer.send("SET TIME:" + str(totalTime), self.addressDict.get("Timer"))

        self.team1Name = self.collegeDict[self.team1NameCombo.value]
        self.team2Name = self.collegeDict[self.team2NameCombo.value]

        self.TCPServer.send("UPDATE NAME:" + str(self.team1Name), self.addressDict.get("Team 1"))
        self.TCPServer.send("UPDATE NAME:" + str(self.team2Name), self.addressDict.get("Team 2"))

        self.team1NameColor = self.team1ColorPrev.bg
        self.team1NameBackground = self.team1BackgroundColorPrev.bg

        self.team2NameColor = self.team2ColorPrev.bg
        self.team2NameBackground = self.team2BackgroundColorPrev.bg

        # Send all values above to each of the Pis via TCP


    def startGame(self):
        # Disable the functionality of textboxes and buttons
        # Exclude resume, pause, correct and incorrect buttons
        self.moderatorTextBox.disable()

        self.team1NameCombo.disable()
        self.team2NameCombo.disable()
        self.p1t1TextBox.disable()
        self.p2t1TextBox.disable()
        self.p3t1TextBox.disable()
        self.p4t1TextBox.disable()

        self.p1t2TextBox.disable()
        self.p2t2TextBox.disable()
        self.p3t2TextBox.disable()
        self.p4t2TextBox.disable()

        self.minuteTextBox.disable()
        self.secondTextBox.disable()

        self.updateButton.disable()
        self.startGameButton.disable()
        self.resetButton.disable()

        self.addPointTextBox.disable()
        self.subPointTextBox.disable()

        self.TCPServer.send("START", self.addressDict.get("Timer"))

        # Start timer

    def pauseGame(self):
        # Enable the functionality of disabled textboxes and buttons
        self.moderatorTextBox.enable()

        self.team1NameCombo.enable()
        self.team2NameCombo.enable()
        self.p1t1TextBox.enable()
        self.p2t1TextBox.enable()
        self.p3t1TextBox.enable()
        self.p4t1TextBox.enable()

        self.p1t2TextBox.enable()
        self.p2t2TextBox.enable()
        self.p3t2TextBox.enable()
        self.p4t2TextBox.enable()

        self.minuteTextBox.enable()
        self.secondTextBox.enable()

        self.updateButton.enable()
        self.startGameButton.enable()
        self.resetButton.enable()

        self.addPointTextBox.enable()
        self.subPointTextBox.enable()

        self.TCPServer.send("PAUSE", self.addressDict.get("Timer"))


        # stop timer




    def endGame(self):
        endGameYesNo = self.app.yesno("End Game", "You are about to end the game. Are you sure?")
        if endGameYesNo == True:
            self.TCPServer.stop()
            self.TCPServer.join()
            self.app.destroy()



    def correctAnswer(self, team):
        # Add points to team that answered correctly
        # Point value is based on what the user entered in the text box
        # The points go to the team that is specified by the passed parameter
        try:
            correctValue = int(self.addPointTextBox.value)
            #send value to team's scoreboard
            self.TCPServer.send("UPDATE SCORE:" + str(correctValue), self.addressDict.get("Team " + str(team)))
        except ValueError:
            self.app.warn("Invalid Input", "Please enter a number")



    def incorrectAnswer(self, team):
        # Subtract points to team that answered correctly
        # Point value is based on what the user entered in the text box
        # The points go from the team that is specified by the passed parameter

        try:
            incorrectValue = int(self.subPointTextBox.value)
            incorrectValue = -incorrectValue
            #send value to team's scoreboard
            self.TCPServer.send("UPDATE SCORE:" + str(incorrectValue), self.addressDict.get("Team " + str(team)))
        except ValueError:
            self.app.warn("Invalid Input", "Please enter a number")

#def decreaseFont(team, player):
    # Decrease font size of player/moderator by x amount via TCP (Send new value = current value - x)


#def increaseFont(team, player):
    # Increase font size of player/moderator by x amount via TCP (Send new value = current value + x)

    def playSound(self, sound):
        try:
            if sound == 1:
                #t = threading.Thread(target=play, args=(self.ding1,))
                #t.start()
                playsound('./ding.wav', False)
            elif sound == 2:
                #t = threading.Thread(target=play, args=(self.ding2,))
                #t.start()
                playsound('./ding2.wav', False)
            elif sound == 3:
                playsound('./endGameBuzzerSound.wav', False)
            elif sound == 4:
                playsound('./timeOutSound.wav', False)
            print("playing sound")
        except Exception as e:
            print("playsound error" + str(e))


    def changeTextColor(self, entity, type, colorBox):
        colorChooser = colorchooser.askcolor()[1]
        self.gameSettingsWindow.focus()
        colorBox.bg = colorChooser

        #Send the color that was chosen to the appropriate Pi
        if entity == "player" and type == "text":
            print("Change player name text color")
            print(colorChooser)
        elif entity == "timer" and type == "text":
            print("Change timer text color")
            print(colorChooser)
        elif entity == "player" and type == "background":
            print("Change player background")
            print(colorChooser)
        elif entity == "timer" and type == "background":
            print("Change timer background")
            print(colorChooser)
        elif entity == "team1" and type == "background":
            print("Change Team 1 background")
            print(colorChooser)
        elif entity == "team2" and type == "background":
            print("Change team 2 background")
            print(colorChooser)
        elif entity == "team1" and type == "text":
            print("Change team1 text color")
            print(colorChooser)
        elif entity == "team2" and type == "text":
            print("Change team2 text color")
            print(colorChooser)
        elif entity == "team1score" and type == "text":
            print("Change team1 score text color")
            print(colorChooser)
        elif entity == "team2score" and type == "text":
            print("Change team2score text color")
            print(colorChooser)

    def saveAndExit(self):
        self.gameSettingsWindow.hide()

    def selectLogoFile(self):
        logoFile = self.app.select_file()
        self.gameSettingsWindow.focus()
        logoFileSplit = logoFile.split('/')
        self.selectLogoButton.text = logoFileSplit[-1]


    def insertCollege(self):
        self.team1NameCombo.append(self.shortTeamNameTextBox.value)
        self.team2NameCombo.append(self.shortTeamNameTextBox.value)
        self.collegeListBox.append(self.shortTeamNameTextBox.value)

        self.collegeDict[self.shortTeamNameTextBox.value] = self.displayedTeamNameTextBox.value

        #****Need to send color to player Pi over TCP and change player color
        # Replace placeholder for ip address of player that is passed in the parameter

    def removeCollege(self):
        self.team1NameCombo.remove(self.collegeListBox.value)
        self.team2NameCombo.remove(self.collegeListBox.value)
        del self.collegeDict[self.collegeListBox.value]
        self.collegeListBox.remove(self.collegeListBox.value)

    #def changeFont(label, font):
    def client_request_callback(self, request, addr):
        requests = request.split(":")
        if requests[0] == "IDENTITY":
            self.addressDict[requests[1]] = addr
        elif requests[0] == "BUZZ":
            if(self.buzz == False):
                playerNumber = int(requests[1])
                self.buzz = True
                print("sending buzz")
                self.TCPServer.send("BUZZ", addr)
                print("buzz sent")
                if(playerNumber > TEAM_SIZE):
                    self.playSound(2)
                else:
                    self.playSound(1)
                self.app.after(10000, self.buzz_timeout)
        elif requests[0] == "TIMEOUT":
            self.playSound(3)
    def buzz_timeout(self):
        self.playSound(4)
        self.clear()

buzzerHost = BuzzerHost()
