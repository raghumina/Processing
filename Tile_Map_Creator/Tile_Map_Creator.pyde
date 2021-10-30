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


screenWidth = 600
screenHeight = 700
bgColor = color(0)



# HuD's variables 
hudOffsetX = 300
hudOffsetY = 200


def setup():
    global f 
    background(bgColor)
    size(screenHeight, screenWidth)
    rectMode(CENTER)
    stroke(10)
    fill(255)
    f = createFont("Arial", 30)
    
    
def draw():
    global f 
    text("Welcome to Tile-Map-Creator",250, 300)
    
    
    
