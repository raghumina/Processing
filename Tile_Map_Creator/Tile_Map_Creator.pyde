# Assignment 5
# TILE MAP CREATION TOOL 
# Raghu Mina

# Create a tile map creation tool.
# You can select, draw tiles in this editor 
# there are total 28 tiles in this editor 
# Tile assest source: itch.io "wintertileset" author: 
# Contorls 
# To select tiles user can use "U" or "u" to go up in tiles grid to select the tile that we want to draw on the editor
# User can use "D" or "d" to go down in the tiles grid to select the tiles 
# User can use mouse press in the tile editor area to draw the selected tile.
# By default the tile count starts from 0 to draw the desired tile the user have to select tile first.
# the tile count show on the number of tile we have selected from 1-28


# buttons are not functional they are there only for visualization purpose to give command press the mentioned key's
# To save the data press key "s" or "S"
# To exit the canvas press "e", "E" 
# to take screenshot of the canvas press "q", "Q"

# "Refresh button dont work"


# Mouse didn't work on the tilegrid area 
# Mouse only works in the editor area 

# the editor is 273 cell area 


# Varaibles for tiles 
shapeList = []
shapeList.append([])

# Varaiables for grid 
sqrPos = []
sqrColor = []
GRID_CELL_SIZE = 50  # Size of the cell

# Varaibles for selected row and coloumn in grid edit area array
selRow = 3
selCol = 10
tileGrid = []

# VARIABLE FOR SELECTED TILE:
selectedTile = 0

# for background image size 
y = 0 

# Variable for saving the file data 
saveFileName = "Level_Editor.txt"

# 2d array variables 
numberOfRows = 21
numberOfColoumns = 13


# list variable
myList = []
sprites = []


def setup():
    global tile1Sprite, bg, numberOfRows, numberOfColoumns, sprites, nRow, nCol, GRID_CELL_SIZE
    global myList, tileGrid
    size(1200,750)
    background(255, 255, 255)
  #  loadSaveData(loadStrings(saveFileName))
      
    # Layer 1 images 
    # total number of images = 18
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
    
    # Layer 2 images 
    # Total number of images = 10
    
    layer2Sprite1 = loadImage("Crate.png")
    layer2Sprite2 = loadImage("Crystal.png")
    layer2Sprite3 = loadImage("IceBox.png")
    layer2Sprite4 = loadImage("Igloo.png")
    layer2Sprite5 = loadImage("Sign_1.png")
    layer2Sprite6 = loadImage("Sign_2.png")
    layer2Sprite7 = loadImage("SnowMan.png")
    layer2Sprite8 = loadImage("Stone.png")
    layer2Sprite9 = loadImage("Tree_1.png")
    layer2Sprite10 = loadImage("Tree_2.png")
    
    sprites = [tile1Sprite, tile2Sprite, tile3Sprite,  tile4Sprite,  tile5Sprite, tile6Sprite, tile7Sprite, tile8Sprite, tile9Sprite,  tile10Sprite, tile11Sprite, tile12Sprite, tile13Sprite, tile14Sprite, tile15Sprite, tile16Sprite, tile17Sprite, tile18Sprite,layer2Sprite1, layer2Sprite2,layer2Sprite3,layer2Sprite4,layer2Sprite5,layer2Sprite6,layer2Sprite7,layer2Sprite8,layer2Sprite9,layer2Sprite10]
     
    tileGrid = TileGridList(selRow, selCol)
    
    myList = make2dList(numberOfRows, numberOfColoumns)
    
def draw():
    global tile1Sprite, sqrPos, sqrColor, tileGrid, selectedTile
    
    ## will try to add new type mouse cursor 
    cursor(HAND)  # For cursor shape 
    # Have to remove this error clear() not working 
    # BUGGY CODE 
    if key == "c" or key == "C":
        sqrPos = []
        sqrColor = []
        clear()
        
    line(50, 0, 50, 650)
    
    for i in range(len(shapeList)):
        for j in range(len(shapeList[i])):
            tempPos = PVector( i * gridGap.x + gridOffset.x, j * gridGap.y + gridOffset.y)

            image(tile1Sprite, tempPos.x, tempPos.y)
    
    drawHuD()

    # For tile array in tile editor area
def make2dList(numberOfRows, numberOfColoumns):
    newList = []
    for row in range(numberOfRows):
        newList.append([])
        print("yup")
        for col in range(numberOfColoumns):
            newList[row].append(0)
            print("lol")
    print("done")
    return newList

# FOR TILE LIST IN HUD 

def TileGridList(selRow, selCol):
    newList1 = []
    index = 0
    for row in range(selRow):
        newList1.append([])
        for col in range(selCol):
            newList1[row].append(index) # 0, 1, 2, ...
            index = index + 1
        
    return newList1
        
def drawHuD():
    global sqrPos, sqrColor, bg, sprites, tileGrid, selectedTile
    fill(255)
    rect(0,0, 1200, 750)
    
    fill(0)
    rect(0,0, 1050, 650)
 
    stroke(255)
    for i in range(numberOfRows):
        line(50 * (i + 1), 0, 50 * (i + 1), 650)
    for j in range(numberOfColoumns):
        line(0, 50 * (j + 1), 1050 , 50 * (j + 1))

    fill(128)
    textSize(20)
    text("Tile: " + str(selectedTile), 1050+25, 600)
    
    image(sprites[selectedTile],mouseX, mouseY)
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

    
    # for the editor area 
    for i in range(numberOfRows):
        for j in range(numberOfColoumns):
            if myList[i][j] >= 1:
                x = i * 50
                y = j * 50
                index = myList[i][j]
                image(sprites[index],x, y)
  
    # for the tile area        
    for i in range(selRow):
        x = 1050 + (i * 50)
        for j in range(selCol): # 0,1,2
            y = j * 50
            tileIndex = tileGrid[i][j]
            if tileIndex < 28:
                image(sprites[tileIndex],x, y)        
                    
def mousePressed():
    global myList, selectedTile
   
    if mouseX >= 1050 or mouseY >= 650:
        
        pass
    else:
        pos = PVector(mouseX - (mouseX % GRID_CELL_SIZE), mouseY - (mouseY % GRID_CELL_SIZE))
        
        # sprites
        x = mouseX/50
        y = mouseY/50
        myList[x][y] = selectedTile

    
def keyPressed():  # This key is for exit the processing canvas
    global selectedTile
    if key == "e" or key == "E":
        exit()
    
    if key == "q" or key == "Q":  # This key is for taking snap of the processing canvas
        saveFrame()
        
    if key == "U" or key == "u":
        if selectedTile < 27:
            selectedTile = selectedTile + 1
        print(selectedTile)
        
    if key == "d" or key == "D":
        if selectedTile >0:
            selectedTile = selectedTile - 1
        print(selectedTile)
        
def loadSaveData(data):
    
    for line in data:
        lineList = line.split(",")
        sqrPos.append(PVector(float(lineList[0]), float(lineList[1])))
        sqrColor.append(lineList[2])
        
def dispose():
    saveData = []
    for i in range(len(sqrPos)):
        row  = str(sqrPos[i].x) + "," + str(sqrPos[i].y) + "," + str(sqrColor[i])
        saveData.append(row)
    
    saveStrings("data/" + saveFileName, saveData)

    
    
    

    
    
    
    
    
    
