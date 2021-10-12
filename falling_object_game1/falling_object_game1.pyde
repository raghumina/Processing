# Raghu Mina
# Date October/04/2021
# GAME-235, Assignment 2 & 3


# Falling Object Catching Game 
# Create a Falling Object Game where player have control on the slab/bar/puck but not on the falling object 

#Revamp your old falling object catching game from last week using loops and arrays.

#Submit: your Processing project folder with all code and assets a single .zip file.

 

#Grading Rubric

#4 point - use arrays and loop to programmatically move the falling objects (that means more than 1 falling object!)
#1 points - the catching object must move based on player input (using the same method as last time is fine)
#4 points - collision detection between the two objects now done with loops and arrays (distance or rectangular, 
#depending on visuals)
#1 points - the falling objects respawns to a random location when caught or fall off the screen
#Extra Credit (1 points) - display a score and design a more complex scoring system 
#(eg. different point values, multipliers, etc.)
#Extra Credit (2 points) - add hysteresis to the player controlled object and/or
# the score display (check out the first minute or so from this video to see what that might look like:
# Super Mario 64 Coin Count (Links to an external site.)


# Let's create 

 #add_library("sound")


# Creating Variable for the game objets/ entities like ball, bar,screen size etc.





# Game Variables 
gamestate = 1       # 1 state  = menue, 2nd = play, 3rd = end 
gamescore = 0
gamelevel = 1
gametime = 0

# Screen Variables
screenWidth = 1000
screenHeight = 600

# HUD variables
hudOffsetX = 250
hudOffsetY = 0

# Bar Variables 
barPosX = 0      # Variable for position of bar on X axis 
barPosY = 450    # Varialbe for position of bar on Y axis
barHeight = 20   # Varibale for the Size of the bar 
barWidth = 90    # ''  ''    ''    ''    ''     '' 

# Ball Variables
ballRadius = 40
ballFallSpeedFactor = 1.3
ballStartingY = 50

# Unique for each ball 
ballsFallSpeed = [1, 2, 3, 4]
ballsPosX = [120, 240, 360, 480]
ballsPosY = [60, 60, 60, 60]


def setup():
   # global sf          # for sound
    global f           # for font
    global gamestate   # for game state 
    
    size(screenWidth, screenHeight)
    background(0)
    rectMode(CENTER)
    noStroke()
    f = createFont("Arial", 23)
    gamestate = 1
   # sf = SoundFile(this,"pop.wav")
   
    #randomizeBallsPosition()


# Creating a random function to assign random positions to the ball on a specific height 
def randomizeBallsPosition():
    global ballsPosX
    global ballsPosY
    global ballStartingY 
    global hudOffsetX, hudOffsetY
    
    x = int(random(screenWidth - hudOffsetX - (ballRadius * 2)))
    #for i in range(ballsPosX):
        
     #   ballsPosX[i] = 
     #    ballsPosY[i] =  
    
def drawBar():
    global barPosX
    barPosX = mouseX
    fill(255, 255, 255)
    rect(barPosX, barPosY, barWidth, barHeight)
    
    
def drawHUD():
    global f
    global screenWidth, screenHeight
    global hudOffsetX, hudOffsetY
        
    background(143, 40, 40)
    
    fill(0, 0, 0)
    rect(screenWidth/2, screenHeight/2, screenWidth - hudOffsetX, screenHeight - hudOffsetY)

    # Print the game score 
    text("Score: ",5, 120)    
    text(gamescore, 55, 120)

    
def draw():
    if gamestate == 1:
        drawMenu()
    elif gamestate == 2: 
        drawGame()
    elif gamestate == 3:
        drawEnd() 

def drawMenu():    
    global gamestate
    # draw rect button to play game
    background(0)
    fill(0, 255, 0)
    rect(screenWidth/2, screenHeight/2, 200, 50)
    fill(255, 0, 0)
    textFont(f, 16)
    text("Play!",screenWidth/2, screenHeight/2)    
    if mousePressed and mouseX > (screenWidth/2 - 200/2) and mouseX < (screenWidth/2 + 200/2) and mouseY > (screenHeight/2 - 50/2) and mouseY < (screenHeight/2 + 50/2):
        gamestate = 2
      #  sf.play

def drawGame():
    global ballsPosY
    global barPosX, barPosY
    global gamescore, gamelevel, ballFallSpeedFactor, ballsFallSpeed, gamestate
    
    drawHUD()
    drawBar()    
    
    for i in range(len(ballsPosY)):
        ballsPosY[i] = ballsPosY[i] + (ballsFallSpeed[i] * ballFallSpeedFactor * gamelevel)
    
        # Collison Check ball with bar 
        if (ballsPosX[i] > (barPosX - barWidth/2) and \
                ballsPosX[i] < (barPosX + barWidth/2)) and \
            (ballsPosY[i] > barPosY - barHeight/2 and \
                 ballsPosY[i] < barPosY + barHeight/2):
                # Increase score
                gamescore = gamescore + 1
                ballsPosY[i] = ballStartingY
    
        # Ball falling of the screen 
        if ballsPosY[i] > (screenHeight + ballRadius):
            # Apply -negative score
            #randomizeBallPosition()
            ballsPosY[i] = ballStartingY
            # gamescore = gamescore - 1  # hight negative score so that stakes are high for the player :)
        
    if gamescore > 10:
        gamelevel = 2
    elif gamescore > 20: 
        gamelevel = 3
    elif gamescore > 30:
        gamelevel = 4
    elif gamescore < 0:
        gamestate = 3 # stop the game
        
    fill(0, 255, 255)
    for i in range(len(ballsPosX)):
        circle(ballsPosX[i], ballsPosY[i], ballRadius)
    
            
def gameOver():
    if gamestate == 3:
        print("Reached Game state 3")
        fill(255)
        textFont(f, 40)
        text("Game Over \n Start the program again \n  THIS GAME IS IN \n ITS DEVELOPMENT \n PHASE \n:) :)", screenWidth/2, screenHeight/2)    
# THE GAME IS STILL IN DEVELOPMET PHASE 
        
def drawEnd():
    gameOver()
    
    

# Features to add 
# 1. sound 
# 2. game levels
# 3. Proper interactive HUD 
# 4. more types of balls with different differnet properties 
# 5. Storyline 
# 6. Timer 
# 7. Array to store high score and other statistical data like timer, scores, player names and game state 
# 8. Adding partical effect



    
