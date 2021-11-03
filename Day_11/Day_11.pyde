
# GAME 235
# Raghu Mina



sqrPos = []
sqrColor = []
GRID_CELL_SIZE = 30  # Size of the cell
saveFileName = "saveInfo.txt"

def setup():
    size(600, 700)
    background(0)
    noStroke()

def draw():  # 
    global sqrPos, sqrColor
    background(0)
    
    if keyPressed:  
        if key == "r" or key == "R":
            sqrPos = []
            sqrColor = []
            
    for i in range (len(sqrPos)):
        fill(sqrColor[i])
        square(sqrPos[i].x, sqrPos[i].y, GRID_CELL_SIZE)
        
def mousePressed():    #
    pos = PVector(mouseX - (mouseX % GRID_CELL_SIZE), mouseY - (mouseY % GRID_CELL_SIZE))
    sqrPos.append(pos)
    sqrColor.append(color(random(120, 155), random(120, 255), random(120, 255)))
    
    
def loadSaveData(data):
    
    for line in data:
        lineList = line.split(",")
        sqrPos.append(PVector(lineList[0], lineList[1]))
        sqrColor.append(lineList[2])
    
    
    
    
    
    # Saves the program data before closing it 
def dispose():
    saveData = []
    for i in range(len(sqrPos)):
        row = str(sqrPos[i].x) + "," + str(sqrPos[i].y "," + str(sqrColor[i])
        saveData.append(row)
    saveStrings("data/" + savaFileName, saveData)
