# Assignment 5
# TILE MAP CREATION TOOL 
# Raghu Mina


'''
Create a tile map creation tool.

Submit: your Processing project folder with all code and assets a single .zip file.

Grading Rubric

4 point - clicking on the screen creates a tile on the grid
1 points - keyboard keys (specify which ones in comments at the top) allow for switching between
 at least 3 different tiles
4 points - the currently selected tile should be visible 
(either shown in some UI element or following the mouse cursor (perhaps with transparency?))
1 points - pressing a given key on the keyboard will save a screenshot
Extra Credit (1 points) - have more than 5 different tiles
Extra Credit (2 points) - add a second "object" layer on top of the ground layer with different tiles to place 
(this is harder, so make sure everything else is done first before starting it)

'''
# Lets Start 
# Game image 
#img = loadImage("BG.png")

screenWidth = 750
screenHeight = 900
bgColor = color(255)

# Grid 
shapeList = []
shapeList.append([28, 29, 30, 31])
gridOffset = PVector(80, 60)
gridGap = PVector(150, 70)

# HuD's variables 
hudOffsetX = 300
hudOffsetY = 200


# Button variables

buttonHeight = 20
buttonWidth = 90

#button1PosX
#button1PosY

def setup():
    global f 
    global wallSprite
    background(0)
    size(screenHeight, screenWidth)
    rectMode(CENTER)
    stroke(10)
    fill(0)
    f = createFont("Arial", 50)
  #  wallSprite = loadImage("Wall.png")
    
    # What is the sense of creating buttons when we can control all system or action by just pressing specific keys
    # buttona are just for showoff 
    
def draw():
    fill(255)
    #size(20)
    rect(screenWidth/2, 300, 200, 50)
    fill(0)
    text("Welcome to Tile-Map-Creator",250, 300)

    
    # Button 1 
    fill(255)
    rect(80, 700, 150, 40, 6)
    fill(0)
    text("Button1", 60, 700)
    
    # Button 2
    fill(25, 160, 220)
    rect(250, 700, 150, 40, 6)
    fill(0)
    text("Button2", 60, 700)
    
    # Button 3
    fill(255)
    rect(400, 700, 120, 40, 6)
    fill(0)
    text("Button3", 60, 700)

    # Button 4
    fill(255, 155, 55)
    rect(570, 700, 120, 40, 6)
    fill(0)
    text("Button4", 60, 700)
    
    
    DrawHud()
    
    
    
    
    
                                                                                                                  
    for i in range(len(shapeList)):   
        for j in range(len(shapeList[i])):
            tempPos = PVector( i * gridGap.x + gridOffset.x, j * gridGap.y + gridOffset.y)
            tint(255, 0 ,0)
            text(str(shapeList[i][j]), tempPos.x, tempPos.y)
    
    
def DrawHud():
    fill(255)
    rect(400, 300, 780, 700)
    
    stroke(10)
    line(85, 100, 155, 105)

    
