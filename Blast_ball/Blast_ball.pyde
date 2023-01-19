
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
    global rocketSprite, spaceBackground, f, ps 
    size(1200, 900)
    f = createFont("Arial", 23)
    
    # For Particle systetm 
    sprite = loadImage("18.png")
  #  p = Particle(circle(56, 46, 55))
    position = PVector(500, 500)
    
    ps = ParticleSystem(200, position)
    
    rocketSprite = loadImage("Rocket.png")
    spaceBackground = loadImage("SpaceBG.png")
    
def draw():
    ''' This function updates the screen with the help of other varialbes '''
    
    background(10, 120, 10)
    global rocketSprite, spaceBackground, ps
    drawHuD()
    ps.update()
    ps.draw()
   # ps.updatePos()
  #  ps.setEmitter(mouseX, mouseY)
    fill(255)
    textSize(16)
    text("Frame rate: " + str(int(frameRate)), 10, 20)
    # sprite = Particle(circle(56, 46, 55))
  
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
    
    # test = Particle("image.png")
    # Particle().__init__("image.png")

class Particle(object):

    def __init__(self, position):
        
        self.gravity = PVector(1, 2)
        #self.position = position
        self.position = PVector(position.x, position.y)
        self.lifespan = 255
        self.velocity = PVector(random(-1, 1.5), random(-2, 0))
        #print(self.velocity)
        self.size = random(20, 30)
      #  print(self.size)
        
    def updatePos(self):
        self.position.x = ( self.position.x) + (self.velocity.x)
        self.position.y = ( self.position.y) + (self.velocity.y)
        
    def isDead(self):
        return self.lifespan < 0

    def update(self):
        self.lifespan -= 1

        self.updatePos()
       
    def draw(self):
        fill(color(25, 255,255, self.lifespan))
        circle(self.position.x, self.position.y, self.size)
        
class ParticleSystem(object):

    def __init__(self, n, position):
        self.particles = [Particle(position) for _ in range(n)]
        
    def draw(self):
        for p in self.particles:
            p.draw()

    def update(self):
        for p in self.particles:
            p.update()
    
    
