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


# Creating Variable for the game objets/ entities like ball, bar,screen size etc.

#
gamestate = 1 # 1 - menu, 2 - play, 3 - end

# Screen Variables
screenWidth = 800
screenHeight = 600

# HUD variables
hudOffsetX = 200
hudOffsetY = 0


# Bar Variables 
barPosX = 0      # Variable for position of bar on X axis 
barPosY = 450    # Varialbe for position of bar on Y axis
barHeight = 20   # Varibale for the Size of the bar 
barWidth = 60    # ''  ''    ''    ''    ''     '' 

# Ball Variables
ballRadius = 40
ballFallSpeed = 4
ballPosX = screenWidth/2
ballStartingY = 50
ballPosY =  ballStartingY


# Creating a bomb/asteroid variable to make game more fun 
bombRadius = 60
bombFallSpeed = 6
bombPosX = screenWidth/2
bombStartingY = 30
bombPosY = bombStartingY

ballA_name = "BOMB"


def setup():
    global f
    global gamestate
    
    size(screenWidth, screenHeight)
    background(0)
    rectMode(CENTER)
    noStroke()
    f = createFont("Arial", 23)
    gamestate = 1
    randomizeBallPosition()


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
        
    background(255)
    
    fill(0, 0, 0)
    rect(screenWidth/2, screenHeight/2, screenWidth - hudOffsetX, screenHeight - hudOffsetY)
    
    fill(0, 255, 0)
    textFont(f, 16)
    text("High Score!",10,100)    
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
    
    
def draw():
        
    if gamestate == 1:
        drawMenu()
    if gamestate == 2: 
        drawGame()
    if gamestate == 3:
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
    if mousePressed and 
        mouseX > (screenWidth/2 - 200/2) and 
            mouseX < (screenWidth/2 + 200/2) and 
                mouseY > (screenHeight/2 - 50/2) and 
                    mouseY < (screenHeight/2 + 50/2):
        gamestate = 2
        


def drawGame():
    global ballPosY
    global barPosX, barPosY
    
    drawHUD()
    drawBar()    
    
    
    ballPosY = ballPosY + ballFallSpeed
    # Collison Check ball with bar 
    if ballPosX > barPosX - barWidth/2 and ballPosX < barPosX + barWidth/2:
        if ballPosY > barPosY - barHeight/2 and ballPosY < barPosY + barHeight/2:
            # Increase score
            randomizeBallPosition()
    
    # Ball falling of the screen 
    if ballPosY > screenHeight + ballRadius:
        # Apply -negative score
        randomizeBallPosition()        
            
    fill(0, 255, 255)
    circle(ballPosX, ballPosY, ballRadius)    
     
           





    
