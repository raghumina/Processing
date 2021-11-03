



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
            
    for pos in sqrPos:
    
        square(pos.x, pos.y, GRID_CELL_SIZE)
        
def mousePressed():    # 
    pos = PVector(mouseX, mouseY)
    sqrPos.append(pos)
