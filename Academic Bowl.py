from guizero import *
from tkinter import colorchooser
from playsound import playsound


# Initialize the window and app
app = App(title="Control Panel", width = 1100, height = 720)

collegeDict = {"College 1": "This is the long name of College 1"
              ,"College 2": "This is the long name of College 2"
              }

# Define all of the functions
def gameSettingsFunction():
    gameSettingsWindow.show()

def initGame(): 
    startGameButton.text_size = 16
    endGameButton.text_size = 16
    pauseGameButton.text_size = 16
    resetButton.text_size = 16
    updateButton.text_size = 16
    clearButton.text_size = 16
    team1CorrectButton.text_size = 12
    team1IncorrectButton.text_size = 12
    team2CorrectButton.text_size = 12
    team2IncorrectButton.text_size = 12

    startGameButton.width = 10
    endGameButton.width = 10
    pauseGameButton.width = 10
    resetButton.width = 10

    playerNameColorPrev.bg = 'black'
    timerColorPrev.bg = 'black'
    playerBackgroundColorPrev.bg = 'white'
    timerBackgroundColorPrev.bg = 'white'
    team1BackgroundColorPrev.bg = 'white'
    team2BackgroundColorPrev.bg = 'white'
    team1ColorPrev.bg = 'black'
    team2ColorPrev.bg = 'black'
    team1ScoreColorPrev.bg = 'black'
    team2ScoreColorPrev.bg = 'black'

    team1CorrectButton.text_color = 'Green'
    team2CorrectButton.text_color = 'Green'
    team1IncorrectButton.text_color = 'Red'
    team2IncorrectButton.text_color = 'Red'
    
    

    gameSettingsWindow.hide()
    
    


    

def resetFields():
    p1t1TextBox.value = ''
    p2t1TextBox.value = ''
    p3t1TextBox.value = ''
    p4t1TextBox.value = ''

    p1t2TextBox.value = ''
    p2t2TextBox.value = ''
    p3t2TextBox.value = ''
    p4t2TextBox.value = ''

    addPointTextBox.value = ''
    subPointTextBox.value = ''

    minuteTextBox.value = ''
    secondTextBox.value = ''

    moderatorTextBox.value = ''

#def clearBuzzer():


def updateAll():
    #Send all values (text values, fonts, colors) to the respective Pis via TCP
    
    player1team1Text = p1t1TextBox.value
    player1team1Color = playerNameColorPrev.bg
    player1team1Background = playerBackgroundColorPrev.bg
    
    player2team1Text = p2t1TextBox.value
    player2team1Color = playerNameColorPrev.bg
    player2team1Background = playerBackgroundColorPrev.bg
    
    player3team1Text = p3t1TextBox.value
    player3team1Color = playerNameColorPrev.bg
    player3team1Background = playerBackgroundColorPrev.bg
    
    player4team1Text = p4t1TextBox.value
    player4team1Color = playerNameColorPrev.bg
    player4team1Background = playerBackgroundColorPrev.bg
    
    
    player1team2Text = p1t2TextBox.value
    player1team2Color = playerNameColorPrev.bg
    player1team2Background = playerBackgroundColorPrev.bg

    player2team2Text = p2t2TextBox.value
    player2team2Color = playerNameColorPrev.bg
    player2team2Background = playerBackgroundColorPrev.bg
    
    player3team2Text = p3t2TextBox.value
    player3team2Color = playerNameColorPrev.bg
    player3team2Background = playerBackgroundColorPrev.bg

    player4team2Text = p4t2TextBox.value
    player4team2Color = playerNameColorPrev.bg
    player4team2Background = playerBackgroundColorPrev.bg
    
    
    moderatorText = moderatorTextBox.value
    moderatorColor = playerNameColorPrev.bg
    moderatorBackground = playerBackgroundColorPrev.bg
    
    timerMinuteText = minuteTextBox.value
    timerSecondText = secondTextBox.value
    timerColor = timerColorPrev.bg
    timerBackground = timerBackgroundColorPrev.bg
    
    
    team1Name = collegeDict[team1NameCombo.value]
    team2Name = collegeDict[team2NameCombo.value]
        
    team1NameColor = team1ColorPrev.bg
    team1NameBackground = team1BackgroundColorPrev.bg
    
    team2NameColor = team2ColorPrev.bg
    team2NameBackground = team2BackgroundColorPrev.bg
    
    # Send all values above to each of the Pis via TCP


def startGame():
    # Disable the functionality of textboxes and buttons
    # Exclude resume, pause, correct and incorrect buttons
    moderatorTextBox.disable()
    
    team1NameCombo.disable()
    team2NameCombo.disable()
    p1t1TextBox.disable()
    p2t1TextBox.disable()
    p3t1TextBox.disable()
    p4t1TextBox.disable()
    
    p1t2TextBox.disable()
    p2t2TextBox.disable()
    p3t2TextBox.disable()
    p4t2TextBox.disable()
    
    minuteTextBox.disable()
    secondTextBox.disable()
    
    updateButton.disable()
    startGameButton.disable()
    resetButton.disable()
    
    addPointTextBox.disable()
    subPointTextBox.disable()
    
    

    # Start timer

def pauseGame():
    # Enable the functionality of disabled textboxes and buttons
    moderatorTextBox.enable()
    
    team1NameCombo.enable()
    team2NameCombo.enable()
    p1t1TextBox.enable()
    p2t1TextBox.enable()
    p3t1TextBox.enable()
    p4t1TextBox.enable()
    
    p1t2TextBox.enable()
    p2t2TextBox.enable()
    p3t2TextBox.enable()
    p4t2TextBox.enable()
    
    minuteTextBox.enable()
    secondTextBox.enable()
    
    updateButton.enable()
    startGameButton.enable()
    resetButton.enable()
    
    addPointTextBox.enable()
    subPointTextBox.enable()
    

    # stop timer


    

def endGame():
    endGameYesNo = app.yesno("End Game", "You are about to end the game. Are you sure?")
    if endGameYesNo == True:
        app.destroy()
   
        

def correctAnswer(team):
    # Add points to team that answered correctly
    # Point value is based on what the user entered in the text box
    # The points go to the team that is specified by the passed parameter
    try:
        correctValue = int(addPointTextBox.value)
        if team == 1:
            #send value to team 1 scoreboard ********Input Needed***********
            print("1")
        elif team == 2:
            # send value to team 2 scoreboard ********Input Needed***********
            print("2")
    except ValueError:
        app.warn("Invalid Input", "Please enter a number")
        
    

def incorrectAnswer(team):
    # Subtract points to team that answered correctly
    # Point value is based on what the user entered in the text box
    # The points go from the team that is specified by the passed parameter
    incorrectValue = subPointTextBox.value 
    
    try:
        incorrectValue = int(subPointTextBox.value)
        if team == 1:
            #send value to team 1 scoreboard ********Input Needed***********
            print("1")
        elif team == 2:
            #send value to team 2 scoreboard ********Input Needed***********
            print("2")
    except ValueError:
        app.warn("Invalid Input", "Please enter a number")

#def decreaseFont(team, player):
    # Decrease font size of player/moderator by x amount via TCP (Send new value = current value - x)
    

#def increaseFont(team, player):
    # Increase font size of player/moderator by x amount via TCP (Send new value = current value + x)

def playSound(sound):
    if sound == 1:
        playsound('./ding.mp3')
    elif sound == 2:
        playsound('./ding2.mp3')


def changeTextColor(entity, type, colorBox):
    colorChooser = colorchooser.askcolor()[1]
    gameSettingsWindow.focus()
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
    
def saveAndExit():
    gameSettingsWindow.hide()
    
def selectLogoFile():
    logoFile = app.select_file()
    gameSettingsWindow.focus()
    logoFileSplit = logoFile.split('/')
    selectLogoButton.text = logoFileSplit[-1]
    
    
def insertCollege():
    team1NameCombo.append(shortTeamNameTextBox.value)
    team2NameCombo.append(shortTeamNameTextBox.value)
    collegeListBox.append(shortTeamNameTextBox.value)
    
    collegeDict[shortTeamNameTextBox.value] = displayedTeamNameTextBox.value

    #****Need to send color to player Pi over TCP and change player color
    # Replace placeholder for ip address of player that is passed in the parameter

def removeCollege():
    team1NameCombo.remove(collegeListBox.value)
    team2NameCombo.remove(collegeListBox.value)
    collegeListBox.remove(collegeListBox.value)
    
    collegeDict.pop(collegeListBox.value)
#def changeFont(label, font):

#****************************************************************
# Need to create for loop that listens for Buzzes 
# If buzzer received, execute buzz event (play sound and change background of player that buzzed in first)
# Do not execute any other buzz events until clear buzzer function has been executed


gameSettingsWindow = Window(app, title = "Game Settings", width = 800, height = 550, layout = 'grid')

gameSettingsBox1 = Box(gameSettingsWindow, align = 'top', width = 'fill', height = 'fill', grid = [0,0,5,1])
Text(gameSettingsBox1, text = 'Game Settings', align = 'bottom', size = 18)

Box(gameSettingsWindow, width = 100, height = 20, align = 'left', grid = [0,1])

gameSettingsBox2 = Box(gameSettingsWindow, align = 'left', layout = 'grid', width = 'fill', grid = [1,2])

playerNameColorLabel = Text(gameSettingsBox2, text = 'Player Name Color:', grid = [0,0], align = 'right')
playerNameColorPrev = Box(gameSettingsBox2, grid = [1,0], width = 15, height = 20)
Box(gameSettingsBox2, grid = [2,0], width = 10)
playerNameColorButton = PushButton(gameSettingsBox2, text = 'Change', grid = [3,0], args = ["player", "text", playerNameColorPrev], command = changeTextColor)

timerColorLabel = Text(gameSettingsBox2, text = 'Timer Color:', align = 'right', grid = [0,1])
timerColorPrev = Box(gameSettingsBox2, grid = [1,1], width = 15, height = 20)
Box(gameSettingsBox2, grid = [2,1], width = 10)
timerColorButton = PushButton(gameSettingsBox2, text = 'Change', grid = [3,1], args = ["timer", "text", timerColorPrev], command = changeTextColor)

playerBackgroundColorLabel = Text(gameSettingsBox2, text = 'Player Background:', align = 'right', grid = [0,2])
playerBackgroundColorPrev = Box(gameSettingsBox2, grid = [1,2], width = 15, height = 20)
Box(gameSettingsBox2, grid = [2,2], width = 10)
playerBackgroundColorButton = PushButton(gameSettingsBox2, text = 'Change', grid = [3,2], args = ["player", "background", playerBackgroundColorPrev], command = changeTextColor)

timerBackgroundColorLabel = Text(gameSettingsBox2, text = 'Timer Background:', align = 'right', grid = [0,3])
timerBackgroundColorPrev = Box(gameSettingsBox2, grid = [1,3], width = 15, height = 20)
Box(gameSettingsBox2, grid = [2,3], width = 10)
timerBackgroundColorButton = PushButton(gameSettingsBox2, text = 'Change', grid = [3,3], args = ["timer", "background", timerBackgroundColorPrev], command = changeTextColor)

team1BackgroundColorLabel = Text(gameSettingsBox2, text = 'Team 1 Background:', align = 'right', grid = [0,4])
team1BackgroundColorPrev = Box(gameSettingsBox2, grid = [1,4], width = 15, height = 20)
Box(gameSettingsBox2, grid = [2,4], width = 10)
team1BackgroundColorButton = PushButton(gameSettingsBox2, text = 'Change', grid = [3,4], args = ["team1", "background", team1BackgroundColorPrev], command = changeTextColor)

team2BackgroundColorLable = Text(gameSettingsBox2, text = 'Team 2 Background:', align = 'right', grid = [0,5])
team2BackgroundColorPrev = Box(gameSettingsBox2, grid = [1,5], width = 15, height = 20)
Box(gameSettingsBox2, grid = [2,5], width = 10)
team2BackgroundColorButton = PushButton(gameSettingsBox2, text = 'Change', grid = [3,5], args = ["team2", "background", team2BackgroundColorPrev], command = changeTextColor)

team1ColorLabel = Text(gameSettingsBox2, text = 'Team 1 Color:', align = 'right', grid = [0,6])
team1ColorPrev = Box(gameSettingsBox2, grid = [1,6], width = 15, height = 20)
Box(gameSettingsBox2, grid = [2,6], width = 10)
team1ColorButton = PushButton(gameSettingsBox2, text = 'Change', grid = [3,6], args = ["team1", "text", team1ColorPrev], command = changeTextColor)

team2ColorLabel = Text(gameSettingsBox2, text = 'Team 2 Color:', align = 'right', grid = [0,7])
team2ColorPrev = Box(gameSettingsBox2, grid = [1,7], width = 15, height = 20)
Box(gameSettingsBox2, grid = [2,7], width = 10)
team2ColorButton = PushButton(gameSettingsBox2, text = 'Change', grid = [3,7], args = ["team2", "text", team2ColorPrev], command = changeTextColor)

team1ScoreColorLabel = Text(gameSettingsBox2, text = 'Team 1 Score Color:', align = 'right', grid = [0,8])
team1ScoreColorPrev = Box(gameSettingsBox2, grid = [1,8], width = 15, height = 20)
Box(gameSettingsBox2, grid = [2,8], width = 10)
team1ScoreColorButton = PushButton(gameSettingsBox2, text = 'Change', grid = [3,8], args = ["team1score", "text", team1ScoreColorPrev], command = changeTextColor)

team2ScoreColorLabel = Text(gameSettingsBox2, text = 'Team 2 Score Color:', align = 'right', grid = [0,9])
team2ScoreColorPrev = Box(gameSettingsBox2, grid = [1,9], width = 15, height = 20)
Box(gameSettingsBox2, grid = [2,9], width = 10)
team2ScoreColorButton = PushButton(gameSettingsBox2, text = 'Change', grid = [3,9], args = ["team2score", "text", team2ScoreColorPrev], command = changeTextColor)


Box(gameSettingsWindow, width = 50, align = 'left', grid = [2,2])



Box(gameSettingsWindow, width = 100, align = 'right', grid = [3,2])


gameSettingsBox3 = Box(gameSettingsWindow, align = 'right', layout = 'grid', width = 'fill', grid = [3,2])

teamNameLabel = Text(gameSettingsBox3, text = "Input College/Team Name", grid = [0,0,2,1], align = 'top')
Box(gameSettingsBox3, grid = [0,1], height = 10)
shortTeamNameLabel = Text(gameSettingsBox3, text = 'College Name', grid = [0,2], align = 'right')
shortTeamNameTextBox = TextBox(gameSettingsBox3, grid = [1,2], align = 'left', width = 20)

Box(gameSettingsBox3, grid = [0,3], height = 10)

displayedTeamNameLabel = Text(gameSettingsBox3, text = 'Displayed College Name', grid = [0,4], align = 'right')
displayedTeamNameTextBox = TextBox(gameSettingsBox3, grid = [1,4], align = 'left', width = 20)

Box(gameSettingsBox3, grid = [0,5], height = 10)

selectLogoLabel = Text(gameSettingsBox3, text = 'Select College Logo:', grid = [0,6], align = 'right')
selectLogoButton = PushButton(gameSettingsBox3, text = 'Choose File', grid = [1,6], align = 'left', command = selectLogoFile)

Box(gameSettingsBox3, grid = [0,7], height = 10)

collegeListBox = ListBox(gameSettingsBox3, items = [], grid = [0,10,2,1], height = 'fill')


insertCollegeButton = PushButton(gameSettingsBox3, text = 'Insert College', grid = [0,11], align = 'bottom', command = insertCollege)
removeCollegeButton = PushButton(gameSettingsBox3, text = 'Remove College', grid = [1,11], align = 'bottom', command = removeCollege)




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

gameSettingsBox4 = Box(gameSettingsWindow, align = 'bottom', width = 'fill', height = 'fill', grid = [3,3])
#Box(gameSettingsBox4, width = 100, align = 'right', grid = [5,3])
applyButton = PushButton(gameSettingsBox4, text = 'Save and Exit', align = 'bottom', width = 'fill', height = 'fill', command = saveAndExit)


menuBar = MenuBar(app, toplevel = ['Game Settings'], options = [
                                                                [['Game Settings',gameSettingsFunction]]
                                                                ])


#Title Box 
titleBox = Box(app, align = 'top', width = 'fill', height = 50)
Text(titleBox, text = 'Academic Bowl Control Panel', size = 18)

# Moderator Box
moderatorBox = Box(app, align = 'top', width = 'fill', layout = 'grid')

# Moderator Label, Text Box and Font Buttons
Box(moderatorBox, grid = [0,0], width = 10)
Text(moderatorBox, text = 'Moderator Name: ', align = 'left', grid = [1,0])
Box(moderatorBox, grid = [2,0], width = 10)
moderatorTextBox = TextBox(moderatorBox, align = 'left', grid = [3,0], width = 20)
Box(moderatorBox, grid = [4,0], width = 11)
decreaseModButton = PushButton(moderatorBox, text = '-', align = 'left', grid = [5,0])
Box(moderatorBox, grid = [6,0], width = 12)
increaseModButton = PushButton(moderatorBox, text = '+', align = 'left', grid = [7,0])

parentBox1 = Box(app, align = 'top', width = 'fill', height = 'fill')

# Team 1 Title Box
team1TitleBox = TitleBox(parentBox1, text = "Team 1", align = 'left', width = 'fill', height = 'fill')
team1Box = Box(team1TitleBox, layout = 'grid')
# Team 1 Team and player names with text boxes and font buttons
Text(team1Box, text = "Team Name: ", grid = [0,0], align = 'left', size = 12)
#teamNameTextBox = TextBox(team1Box, grid = [1,0], align = 'left')
team1NameCombo = Combo(team1Box, options = [], grid = [1,0], align = 'left')
decreaseTeam1Button = PushButton(team1Box, text = '-', grid = [3,0], align = 'left')
#padBox = Box(team1Box, width = 10, grid = [3,0], align = 'left')
increaseTeam1Button = PushButton(team1Box, text = '+', grid = [4,0], align = 'left')

Text(team1Box, text = 'Player 1', grid = [0,1], align = 'left', size = 12)
p1t1TextBox = TextBox(team1Box, grid = [1,1], align = 'left', width = 'fill')
decreaseP1T1Button = PushButton(team1Box, text = '-', grid = [3,1], align = 'left')
#padBox = Box(team1Box, width = 2, grid = [3,1], align = 'left')
increaseP1T1Button = PushButton(team1Box, text = '+', grid = [4,1], align = 'left')

Text(team1Box, text = 'Player 2', grid = [0,2], align = 'left', size = 12)
p2t1TextBox = TextBox(team1Box, grid = [1,2], align = 'left', width = 'fill')
decreaseP2T1Button = PushButton(team1Box, text = '-', grid = [3,2], align = 'left')
#padBox = Box(team1Box, width = 2, grid = [3,2], align = 'left')
increaseP2T1Button = PushButton(team1Box, text = '+', grid = [4,2], align = 'left')

Text(team1Box, text = 'Player 3', grid = [0,3], align = 'left', size = 12)
p3t1TextBox = TextBox(team1Box, grid = [1,3], align = 'left', width = 'fill')
decreaseP3T1Button = PushButton(team1Box, text = '-', grid = [3,3], align = 'left')
#padBox = Box(team1Box, width = 2, grid = [3,3], align = 'left')
increaseP3T1Button = PushButton(team1Box, text = '+', grid = [4,3], align = 'left')

Text(team1Box, text = 'Player 4', grid = [0,4], align = 'left', size = 12)
p4t1TextBox = TextBox(team1Box, grid = [1,4], align = 'left', width = 'fill')
decreaseP4T1Button = PushButton(team1Box, text = '-', grid = [3,4], align = 'left')
#padBox = Box(team1Box, width = 2, grid = [3,4], align = 'left')
increaseP4T1Button = PushButton(team1Box, text = '+', grid = [4,4], align = 'left')

Box(team1Box, height = 20, grid = [0,5])
team1CorrectButton = PushButton(team1Box, text = 'Correct', grid = [0,6, 2,6], align = 'left', width = 10, args = [1], command = correctAnswer)
Box(team1Box, height = 20, grid = [2,5])
team1IncorrectButton = PushButton(team1Box, text = 'Incorrect', grid = [2,6,4,6], align = 'left', width = 10, args = [1], command = incorrectAnswer)

# Title box to hold buttons for the main functions of the game
gameButtonsTitleBox = TitleBox(parentBox1, text = 'Game Functions', align = 'left', width = 200, height = 'fill')

Box(gameButtonsTitleBox, height = 50)
updateButton = PushButton(gameButtonsTitleBox, text = 'Update', align = 'top', width = 20, command = updateAll)
Box(gameButtonsTitleBox, height = 50)
clearButton = PushButton(gameButtonsTitleBox, text = 'Clear Buzzer', align = 'top', width = 20)


# Team 2 Team and player names with text boxes and font buttons
team2TitleBox = TitleBox(parentBox1, text = "Team 2", align = 'left', width = "fill", height = 'fill')
team2Box = Box(team2TitleBox, layout = 'grid')

Text(team2Box, text = "Team Name: ", grid = [0,0], align = 'left', size = 12)
#teamNameTextBox = TextBox(team2TitleBox, grid = [1,0], align = 'left')
team2NameCombo = Combo(team2Box, options = [], grid = [1,0], align = 'left')
decreaseTeamNameButton = PushButton(team2Box, text = '-', grid = [3,0], align = 'left')
increaseTeamNameButton = PushButton(team2Box, text = '+', grid = [4,0], align = 'left')

Text(team2Box, text = 'Player 1', grid = [0,1], align = 'left', size = 12)
p1t2TextBox = TextBox(team2Box, grid = [1,1], align = 'left', width = 'fill')
decreaseP1Button = PushButton(team2Box, text = '-', grid = [3,1], align = 'left')
increaseP1Button = PushButton(team2Box, text = '+', grid = [4,1], align = 'left')

Text(team2Box, text = 'Player 2', grid = [0,2], align = 'left', size = 12)
p2t2TextBox = TextBox(team2Box, grid = [1,2], align = 'left', width = 'fill')
decreaseP1Button = PushButton(team2Box, text = '-', grid = [3,2], align = 'left')
increaseP1Button = PushButton(team2Box, text = '+', grid = [4,2], align = 'left')

Text(team2Box, text = 'Player 3', grid = [0,3], align = 'left', size = 12)
p3t2TextBox = TextBox(team2Box, grid = [1,3], align = 'left', width = 'fill')
decreaseP1Button = PushButton(team2Box, text = '-', grid = [3,3], align = 'left')
increaseP1Button = PushButton(team2Box, text = '+', grid = [4,3], align = 'left')

Text(team2Box, text = 'Player 4', grid = [0,4], align = 'left', size = 12)
p4t2TextBox = TextBox(team2Box, grid = [1,4], align = 'left', width = 'fill')
decreaseP1Button = PushButton(team2Box, text = '-', grid = [3,4], align = 'left')
increaseP1Button = PushButton(team2Box, text = '+', grid = [4,4], align = 'left')

Box(team2Box, height = 20, grid = [0,5])
team2CorrectButton = PushButton(team2Box, text = 'Correct', grid = [0,6,2,6], align = 'left', width = 10, args = [2], command = correctAnswer)
Box(team2Box, height = 20, grid = [2,5])
team2IncorrectButton = PushButton(team2Box, text = 'Incorrect', grid = [2,6,4,6], align = 'left', width = 10, args = [2], command = incorrectAnswer)



parentBox2 = Box(app, align = 'top', width = 'fill', height = 'fill')

pointTitleBox = TitleBox(parentBox2, text = 'Points', align = 'left', width = 'fill', height = 'fill')
Text(pointTitleBox, text = 'Correct (+ Point Value)', align = 'left', size = 12)
addPointTextBox = TextBox(pointTitleBox, align = 'left')
Text(pointTitleBox, text = 'Incorrect (- Point Value)', align = 'left', size = 12)
subPointTextBox = TextBox(pointTitleBox, align = 'left')

timerTitleBox = TitleBox(parentBox2, text = 'Timer', align = 'left', width = 'fill', height = 'fill')
Text(timerTitleBox, text = 'Minutes:', align = 'left', size = 12)
minuteTextBox = TextBox(timerTitleBox, align = 'left')
Text(timerTitleBox, text = 'Seconds:', align = 'left', size = 12)
secondTextBox = TextBox(timerTitleBox, align = 'left')

parentBox3 = Box(app, align = 'top', width = 'fill', height = 'fill')
mainButtonTitleBox = TitleBox(parentBox3, text = 'Main Functions', height = 'fill', width = 'fill')

buttonBox = Box(mainButtonTitleBox, layout = 'grid', align = 'top')

startGameButton = PushButton(buttonBox, text = 'Start Game', grid = [0,0], align = 'left', command = startGame)
Box(buttonBox, grid = [1,0], width = 10)
pauseGameButton = PushButton(buttonBox, text = 'Pause Game', grid = [2,0], align = 'left', command = pauseGame)
Box(buttonBox, grid = [3,0], width = 10)
resetButton = PushButton(buttonBox, text = 'Reset', grid = [4,0], align = 'left', command = resetFields)
Box(buttonBox, grid = [5,0], width = 10)
endGameButton = PushButton(buttonBox, text = 'End Game', grid = [6,0], align = 'left', command = endGame)



initGame()


app.display()

