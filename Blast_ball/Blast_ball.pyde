
# Defender of Earth 
# You are the last line of defence of the earth save the earth form the upcoming asterioids with your ship
# Seven billion hopes lie's upon you 
# Good luck


# Rocket: 
# SpaceBackground: Author TheDarkBear, ItchIo

# Game Varaibles

# Bullet Varaibles
bullets = []
bulletSpeed = 10
bulletHeight = 6
bulletWidth = 8

# Enemy Varialbles
enemy = []
enemyHeight = 20
enemyWidth = 40
enemyFallSpeed = []
enemyColor = []
enemyPosX = []
enemyPosY = []

# Score Variable 
score = 0


def setup():
    ''' Create Canvas where all changes updates were made it is basically the game screen '''
    global rocketSprite, spaceBackground, f 
    size(1200, 900)
    f = createFont("Arial", 23)
    
    
    
    
    rocketSprite = loadImage("Rocket.png")
    spaceBackground = loadImage("SpaceBG.png")
    
def draw():
    ''' This function updates the screen with the help of other varialbes '''
    
    background(10, 120, 10)
    global rocketSprite, spaceBackground
    drawHuD()

def drawHuD():
    ''' This function creates a HuD in the main screen where game is played 
        This screen have all the updates which are created or made in the game screen 
        It have image keyword which creates the image background and other game images '''
        
    global rocketSprite, spaceBackground
    global f    # for text 



    textSize(20)
    text("Score: ", 5, 50)

    rect(80, 80, 1000, 750)
    image(spaceBackground, 80, 80, 1000, 750)
    
    
    image(rocketSprite, mouseX, mouseY)
    
    
