
# Rocket: 
# SpaceBackground: Author TheDarkBear, ItchIo

def setup():
    global rocketSprite, spaceBackground
    size(1200, 900)
    
    rocketSprite = loadImage("Rocket.png")
    spaceBackground = loadImage("SpaceBG.png")
    
def draw():
    background(255)

    global rocketSprite, spaceBackground
    



    drawHuD()



def drawHuD():
    global rocketSprite, spaceBackground
    
    fill(0)
    rect(80, 80, 1000, 750)
    image(spaceBackground, 80, 80, 1000, 750)
    
    
    image(rocketSprite, mouseX, mouseY)
