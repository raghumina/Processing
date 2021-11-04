# Assignment 5
# TILE MAP CREATION TOOL 
# Raghu Mina



# Create a tile map creation tool.


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

# Variable for saving the file data 
saveFileName = "Level_Editor.txt"



def setup():
    global tile1Sprite, bg
    size(1200,750)
    background(255, 255, 255)
  #  loadSaveData(loadStrings(saveFileName))
    
    tile1Sprite = loadImage("1.png")
    tile2Sprite = loadImage("2.png")
    tile3Sprite = loadImage("3.png")
    tile4Sprite = loadImage("4.png")
    tile5Sprite = loadImage("5.png")
    tile6Sprite = loadImage("6.png")
    tile7Sprite = loadImage("7.png")
    tile8Sprite = loadImage("8.png")
    tile9Sprite = loadImage("9.png")
    tile10Sprite = loadImage("10.png")
    tile11Sprite = loadImage("11.png")
    tile12Sprite = loadImage("12.png")
    tile13Sprite = loadImage("13.png")
    tile14Sprite = loadImage("14.png")
    tile15Sprite = loadImage("15.png")
    tile16Sprite = loadImage("16.png")
    tile17Sprite = loadImage("17.png")
    tile18Sprite = loadImage("18.png")
    
    
def draw():
    global tile1Sprite, sqrPos, sqrColor 
    cursor(HAND)  # For cursor shape 
    
    # Have to remove this error clear() not working 
    # BUGGY CODE 
    if key == "c" or key == "C":
        sqrPos = []
        sqrColor = []
        clear()
    
    for i in range(len(shapeList)):
        for j in range(len(shapeList[i])):
            tempPos = PVector( i * gridGap.x + gridOffset.x, j * gridGap.y + gridOffset.y)

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
    
    
def keyPressed():  # This key is for exit the processing canvas 
    if key == "e" or key == "E":
        exit()
    
    if key == "q" or key == "Q":  # This key is for taking snap of the processing canvas
        saveFrame()
    


    
    '''
def loadSaveData(data):
    
    for line in data:
        lineList = line.split(",")
        sqrPos.append(PVector(float(lineList[0]), float(lineList[1])))
        sqrColor.append(lineList[2])
        '''
def dispose():
    saveData = []
    for i in range(len(sqrPos)):
        row  = str(sqrPos[i].x) + "," + str(sqrPos[i].y) + "," + str(sqrColor[i])
        saveData.append(row)
        
    saveStrings("data/" + saveFileName, saveData)
                      
# For new Page or Screen 
    
    
    

    
    
    
    
    
    
