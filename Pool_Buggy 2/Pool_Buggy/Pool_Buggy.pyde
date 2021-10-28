# Pool Project
# Zac Emerzian
# 10-15-2021

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

def setup():
    
    size(960, 640)
    background(0, 0, 50)
    strokeWeight(4)
    textSize(28)
    

def draw():
    background(0, 0, 50)
    
    UpdateWand()
    
    UpdateBalls()
    
    text("Balls " + str(len(ballPos)), 10, 30)


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
            else:
                ballSize[i] -= BALL_SIZE_DECAY * 10
            
            fill(ballColor[i], 255 * ballSize[i]/float(INITIAL_BALL_SIZE))
            circle(ballPos[i].x, ballPos[i].y, ballSize[i])
        else:
            trashBin.append(i)
    
    # Empty the Trash
    for j in range(len(trashBin)):
        ballPos.pop(trashBin[j])
        ballVel.pop(trashBin[j])
        ballSize.pop(trashBin[j])
        ballColor.pop(trashBin[j])


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
