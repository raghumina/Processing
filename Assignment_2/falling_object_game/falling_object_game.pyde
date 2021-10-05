# Raghu Mina
# Date October/04/2021
# GAME-235, Assignment 2 


# Falling Object Catching Game 
# Create a Falling Object Game where player have control on the slab/bar/puck but not on the falling object 

#Grading Rubric

# 2 point - the falling object must move programmatically (ie. not controlled by the player)
# 2 points - the catching object must move based on player input (mouse, keyboard, etc.)
# 4 points - collision detection between the two objects (distance or rectangular, depending on visuals)
# 2 points - the falling object respawns to a random location when caught or falls off the screen
# Extra Credit (1 points) - display a score
# Extra Credit (1 points) - display the high score (involves a fail state)
# Extra Credit (2 points) - add acceleration or more interesting velocities to either object

# My feature that I Want to add 
# Two differnet kind of object 
# One obuncing Object that can alter the trajectory of falling objects after collision with them.


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
ballFallSpeed = 4
ballFallSpeedFactor = 1.3
ballPosX = screenWidth/2
ballStartingY = 50
ballPosY =  ballStartingY

'''
# Creating a bomb/asteroid variable to make game more fun 
bombRadius = 60
bombFallSpeed = 6
bombPosX = screenWidth/2
bombStartingY = 30
bombPosY = bombStartingY

ballA_name = "BOMB"
'''


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
    randomizeBallPosition()
   # sf = SoundFile(this,"pop.wav")


# Creating a random function to assign random positions to the ball on a specific height 
def randomizeBallPosition():
    global ballPosX
    global ballPosY
    global ballStartingY
    global hudOffsetX, hudOffsetY
    
    x = int(random(screenWidth - hudOffsetX - (ballRadius * 2)))

    ballPosX = x + (hudOffsetX / 2) + (ballRadius)
    ballPosY = ballStartingY
    # y = int(random(600))
    
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

    # Ball A stastics 
    fill(0, 255, 0)
    textFont(f, 16)
    text("Ball_A Statstics",5,50)    
    text(ballPosY, 55, 70)
    
    # Print the game score 
    text("Score: ",5, 120)    
    text(gamescore, 55, 120)

'''
    # Ball B stastics 
    fill(0, 255, 0)
    textFont(f, 16)
    text("Ball_B Statstics",0,100)    
    text(ballPosY, 10, 120)

   
#def drawBallA():
# TEST
    
def randomizeBombPosition():
    global bombPosX
    global bombPosY
    global bombStartingY
    
    x = int(random(500))
    x_offset = 30
    bombPosX = x + x_offset
    bombPosY = bombSartingY    
    '''
    
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
    global ballPosY
    global barPosX, barPosY
    global gamescore, gamelevel, ballFallSpeedFactor, ballFallSpeed, gamestate
    
    drawHUD()
    drawBar()    
    
    
    ballPosY = ballPosY + ballFallSpeed * ballFallSpeedFactor * gamelevel
    
    # Collison Check ball with bar 
    if ballPosX > barPosX - barWidth/2 and ballPosX < barPosX + barWidth/2:
        if ballPosY > barPosY - barHeight/2 and ballPosY < barPosY + barHeight/2:
            # Increase score
            gamescore = gamescore + 1
            randomizeBallPosition()
    
    # Ball falling of the screen 
    if ballPosY > (screenHeight + ballRadius):
        # Apply -negative score
        randomizeBallPosition()
        gamescore = gamescore - 3  # hight negative score so that stakes are high for the player :)
        
    if gamescore > 10:
        gamelevel = 2
    elif gamescore > 20: 
        gamelevel = 3
    elif gamescore > 30:
        gamelevel = 4
    elif gamescore < 0:
        gamestate = 3 # stop the game
        
    fill(0, 255, 255)
    circle(ballPosX, ballPosY, ballRadius)
    
            
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



    
