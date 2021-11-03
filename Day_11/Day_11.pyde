



sqrPos = []
sqrColor = []
GRID_CELL_SIZE = 100  # Size of the cell

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
    pos = PVector(mouseX, mouseY)
    sqrPos.append(pos)
    sqrColor.append(color(random(120, 155), random(120, 255), random(120, 255)))