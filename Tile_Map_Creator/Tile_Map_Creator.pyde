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

# Varaibles for tiles 
shapeList = []
shapeList.append([20, 30, 30, 40])

gridOffset = PVector(1060, 50)
gridGap = PVector(1, 55)


# Varaiables for grid 
sqrPos = []
sqrColor = []
GRID_CELL_SIZE = 50  # Size of the cell

# for background image size 
y = 0 





def setup():
    global tile1Sprite, bg
    size(1200,750)
    background(255, 255, 255)
    
    bg = loadImage("BG.png")
    
    
    tile1Sprite = loadImage("1.png")
   # textSize(32)
    
def draw():
    global tile1Sprite, bg
    
    
    
    for i in range(len(shapeList)):
        for j in range(len(shapeList[i])):
            tempPos = PVector( i * gridGap.x + gridOffset.x, j * gridGap.y + gridOffset.y)
            tint(255, 0, 0)
            image(tile1Sprite, tempPos.x, tempPos.y)
     
            
    drawHuD()
   
        

def drawHuD():
    global sqrPos, sqrColor, bg
    fill(0)
    rect(5,5, 1050, 650)

 
    # Save button   # Assignes with button S
    fill(120, 121, 200)
    rect(20, 680, 170, 50, 5)
    fill(0)
    textSize(30)
    text("Save", 50, 710)
    
    # ScreenShot Button   # Assigned with button Q
    fill(90, 181, 250)
    rect(200, 680, 170, 50, 5)
    fill(0)
    textSize(30)
    text("ScreenShot", 200, 710)
    
    # Refresh  # Assigned with button W
    fill(221, 121, 21)
    rect(380, 680, 170, 50, 5)
    fill(0)
    textSize(30)
    text("Refresh", 400, 710)
    
 
    # Exit Button   # Assignes with button "E"
    fill(123, 255, 180)
    rect(560, 680, 170, 50, 5)
    fill(0)
    textSize(30)
    text("Exit", 570, 710)
    
    
    # Left arrow key   # Assigned with button "L"
    fill(100, 221, 200)
    rect(900, 680, 50, 50, 5)
    fill(0)
    textSize(50)
    text("L", 910, 720)

    
    # Up arrow key   # Assigned with button "U"
    fill(100, 221, 200)
    rect(960, 680, 50, 50, 5)
    fill(0)
    textSize(50)
    text("U", 970, 720)
    
    # Down arrow key   # Assigned with button "D"
    fill(100, 221, 200)
    rect(1020, 680, 50, 50, 5)
    fill(0)
    textSize(50)
    text("D", 1030, 720)
    
    # Right arrow key   # Assigned with button "r"
    fill(100, 221, 200)
    rect(1080, 680, 50, 50, 5)
    fill(0)
    textSize(50)
    text("R", 1090, 720)
    
    for i in range (len(sqrPos)):
        fill(sqrColor[i])
        square(sqrPos[i].x, sqrPos[i].y, GRID_CELL_SIZE)
        
            
def mousePressed():    #
    pos = PVector(mouseX - (mouseX % GRID_CELL_SIZE), mouseY - (mouseY % GRID_CELL_SIZE))
    
    sqrPos.append(pos)
    sqrColor.append(color(random(120, 155), random(120, 255), random(120, 255)))
    
    
def keyPressed():
    if key == "e" or key == "E":
        exit()
    
    if key == "q" or key == "Q":
        saveFrame()

    
    
    

    
    
    
    
    
    
