# Pool Project
# MID TERM
# Question #1: Fix the Buggy Code 

'''
Submitte by:
Raghu Mina
Date: 10/28/2021
'''


#Remove the bugs

'''
BUG #906 -  Balls can leave the screen
Status:- Debugged

BUG #1075 - Balls don't fully disappear
Status:- Debugged

BUG #204 - Balls rendering incorrectly
Status:- Debugged

BUG #205 - The wand and ball counter text are the wrong color
Status:- Debugged
'''



# Varaibles 
isPressed = False
isReleased = False
startPos = None
ballPos = []
ballVel = []
ballSize = []
ballColor = []
INITIAL_BALL_SIZE = 60
BALL_IMPACT_DECAY = 0.95
BALL_SIZE_DECAY = -0.02
backGround = color(0, 0, 50) # Added new variable for bg color

# Setting Up the canvas on which all changes will be made 
def setup():
    size(960, 640)
    strokeWeight(4)
    textSize(28)
    
# This function will draw, update all the changes on the canvas 
def draw():
    global backGround
    background(backGround)
    stroke(255)
    UpdateWand()
    
    fill(backGround)
    UpdateBalls()
    fill(255)
    text("Balls " + str(len(ballPos)), 10, 30)

'''
function updates the wand movements.
conditionls statements in this function contorl the outcome of the wand color. ball color, speed when conditions meet
'''
def UpdateWand():
    global isPressed, isReleased, startPos
    if mousePressed:
        isReleased = True
        if isPressed == False:
            startPos = PVector(mouseX, mouseY)
            isPressed = True
        else:
            fill(255)
            line(startPos.x, startPos.y, mouseX, mouseY)
        
    elif isReleased:
        if startPos.x - mouseX != 0 and startPos.y - mouseY != 0:
            ballPos.append(startPos)
            ballVel.append(PVector(startPos.x - mouseX, startPos.y - mouseY)/10.0)
            ballSize.append(INITIAL_BALL_SIZE)
            ballColor.append(color(random(120, 255), random(120, 255), random(120, 255)))
        
        isPressed = False
        isReleased = False
'''
This functions update the ball movement, size when conditions fullfilled 
It updates ball color, ball decay, vanishing of the ball, color of the outline of the ball

'''
def UpdateBalls():
    trashBin = []
    for i in range(len(ballPos)):
        ballPos[i] += ballVel[i]
        
        whichWall = offScreen(ballPos[i])
        if whichWall > 0:
            ballSize[i] *= BALL_IMPACT_DECAY
            
            # Reflecting Off of Walls (No bugs here!)
            if whichWall == 1 or whichWall == 3:
                ballVel[i].rotate(PI - 2*ballVel[i].heading())
            else:
                ballVel[i].rotate(-2*ballVel[i].heading())
        
        if ballSize[i] > 0:
            if ballSize[i] > INITIAL_BALL_SIZE/4:
                ballSize[i] += BALL_SIZE_DECAY
          
            
            stroke(ballColor[i], 255 * ballSize[i]/float(INITIAL_BALL_SIZE))
            circle(ballPos[i].x, ballPos[i].y, ballSize[i])
        else:
            trashBin.append(i)
    
    # Empty the Trash
    for j in range(len(trashBin)):
        ballPos.pop(trashBin[j])
        ballVel.pop(trashBin[j])
        ballSize.pop(trashBin[j])
        ballColor.pop(trashBin[j])

'''
This functions controls the collision of the ball with the canvas edges

'''
def offScreen(vector):
    if vector.x <= 0:
        return 1  # left     
    elif vector.y > height:
        return 2  # bottom
    elif vector.x > width:
        return 3 # Right
    elif vector.y <= 0:
        return 4 # Top
    return 0  

# Time taken to debug this code: 90 minutes 
