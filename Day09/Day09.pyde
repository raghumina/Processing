# Day 9 of the GAME 235 CLASS



boxPos = []
boxColor = []
Max_Size = 100
boxSize = []

def setup():
    size(640, 480)
    background(0)
    noStroke()
    rectMode(CENTER)
    textSize(28)
    
    
    
def draw():
    background(255)
    
    

    for i in range(len(boxPos)):
        boxSize[i] += 0.5
        
        fill(boxColor[i], 255 * (Max_Size - boxSize[i]) / Max_Size)
        square(boxPos[i].x, boxPos[i].y, boxSize[i])
        
    if boxSize[i] > Max_Size:
        boxPos.pop(i)
        boxSize.pop(i)
        boxColor.pop(i)

    
    fill(0)
    text("Boxes: " + str(len(boxPos)), 20, 30)
        
def mousePressed():
    boxPos.append(PVector(mouseX, mouseY))
    boxSize.append(4)
    boxColor.append(color(random(100, 255), random(120, 255), random(100, 255)))
        
