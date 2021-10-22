# Raghu Mina 
# GAMES-235, Assignment 3 
# 11/10/2021
# Falling Object Game V2


# Assignment requirments:
#4 point - use arrays and loop to programmatically move the falling objects (that means more than 1 falling object!)
#1 points - the catching object must move based on player input (using the same method as last time is fine)
#4 points - collision detection between the two objects now done with loops and arrays (distance or rectangular, 
#depending on visuals)
#1 points - the falling objects respawns to a random location when caught or fall off the screen
#Extra Credit (1 points) - display a score and design a more complex scoring system 
#(eg. different point values, multipliers, etc.)
#Extra Credit (2 points) - add hysteresis to the player controlled object 
#and/or the score display (check out the first minute or so from this video to see what that might
   

# Lets start 


# Game Varaibles

# Bar Variables 
barPosX = 0      # Variable for position of bar on X axis 
barPosY = 550    # Varialbe for position of bar on Y axis
barHeight = 20   # Varibale for the Size of the bar 
barWidth = 90    # ''  ''    ''    ''    ''     '' 


ballX = [100, 150, 200]
ballY = [60, 65, 60]

ballColor = [color(255), color(225), color(50)]
ballRadius = 30
ballFallSpeed = 3




def setup():
    background(0)
    size(900,700)
    textSize = 32
    
'''
def drawBar():
  #  global barPosX
    barPosX = mouseX
    fill(255, 255, 255)
    rect(barPosX, barPosY, barWidth, barHeight)
'''

def draw():
    background(0)
    barPosX = mouseX
    fill(255, 255, 255)
    rect(barPosX, barPosY, barWidth, barHeight)

    
    if mousePressed:
        ballX.append(random(width))
        ballY.append(random(-4))
        ballColor.append(color(random(255), random(255), random(255)))
        
    for i in range(len(ballX)):
        ballX[i] += random(-2, 2)
        ballY[i] += ballFallSpeed

        if ballY[i] > height + ballRadius:
            ballX[i] = random(width)
            ballY[i] = random(-10)

        fill(ballColor[i])
        circle(ballX[i], ballY[i], ballRadius)
    
    fill(255)
    text("Ball Count: "+ str(len(ballX)), 10, 30)
    text("Score: ", 120, 30)
    text("High Score: ", 260, 30)
    text("Life: ", 400, 30)
