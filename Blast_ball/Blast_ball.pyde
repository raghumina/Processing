
# this is the game which will use the the particle system
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
ballsStartingY = 50
#ballsStartingX = random(0, 1000)

# Unique for each ball 
ballsFallSpeed = [1, 2, 3, 4]
ballsPosX = [120, 240, 360, 480]
ballsPosY = [60, 60, 60, 60]
ballsColor = [color(255,0, 120), color(180, 250, 220), color(220, 180, 50), color(20, 100, 220)]


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
    global ballsStartingY, ballsStartingX
    global hudOffsetX, hudOffsetY
    global ballsColor
    
    x = int(random(screenWidth - hudOffsetX - (ballRadius * 2)))
    #for i in range(ballsPosX):
        
     # ballsPosX[i] = 
     #    ballsPosY[i] =  
    
def drawBar():
    global barPosX
    barPosX = mouseX
    fill(255, 255, 255)
    rect(barPosX, barPosY, barWidth, barHeight)
    
    
def drawHUD():
    global f
    global screenWidth, screenHeight
 #  global hudOffsetX, hudOffsetY
        
    background(0)
    
 #   fill(0, 0, 0)
  #  rect(screenWidth/2, screenHeight/2, screenWidth - hudOffsetX, screenHeight - hudOffsetY)

    # Print the game score 
    text("Score: ",5, 50)    
    text(gamescore, 5, 70)

    
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
    global ballsColor
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
                ballsPosY[i] = ballsStartingY
                ballsPosX[i] = random(0, 1000)
    
        # Ball falling of the screen 
        if ballsPosY[i] > (screenHeight + ballRadius):
            # Apply -negative score
           # randomizeBallPosition()
            ballsPosY[i] = ballsStartingY
            ballsPosX[i] = random(0, 1000)
            # gamescore = gamescore - 1  # hight negative score so that stakes are high for the player :)
        
    if gamescore > 10:
        gamelevel = 2
    elif gamescore > 20: 
        gamelevel = 3
    elif gamescore > 30:
        gamelevel = 4
    elif gamescore < 0:
        gamestate = 3 # stop the game
        
    for i in range(len(ballsPosX)):
        fill(ballsColor[i])
        circle(ballsPosX[i], ballsPosY[i], ballRadius)
    
            
def gameOver():
    if gamestate == 3:
        print("Reached Game state 3")
        fill(255)
        textFont(f, 40)
      #  text("Game Over \n Start the program again \n  THIS GAME IS IN \n ITS DEVELOPMENT \n PHASE \n:) :)", screenWidth/2, screenHeight/2)    
# THE GAME IS STILL IN DEVELOPMET PHASE 
        
def drawEnd():
    gameOver()
    
